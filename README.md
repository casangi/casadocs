# casabench
## Tracking the performance of CASA
The scope of this repository is the automatic execution of performance benchmarking tests that satisfy two use-cases:
1. To characterize trends in performance metrics across [CASA6](https://open-bitbucket.nrao.edu/projects/CASA/repos/casa6/browse/casatasks) repository history (after releases are published from the main trunk)
2. To detect code causing performance issues during verification of development branches (before changes are merged with the main trunk)

To satisfy these use cases, this prototype uses a wrapper script to coordinate calls to the [airspeed-velocity](https://asv.readthedocs.io/en/stable/) (`asv`) framework, which manages the execution of tests (located in the `benchmarks` directory). The successful execution of benchmarks produces environment-specific performance data (stored in [JSON](https://www.json.org/json-en.html) format in the `results` directory), and further calls to `asv` generate an [HTML](https://html.spec.whatwg.org/) representation of the results and automatic regression analysis (published to the web from a dedicated branch via [GitHub pages](https://pages.github.com/both)). This repository could be modified to work with other tools in the future, including `asv`'s integration with the Python standard library [profiler](https://docs.python.org/3/library/profile.html#the-python-profilers).  

Right now casabench is pre-alpha software, not intended for general use.

## Installation
This package is not yet installable, either from a source or wheel distribution. Early-stage usage relies on creation of a python environment, using either [`conda`](https://docs.conda.io/en/latest/miniconda.html) or [`virtualenv`](https://virtualenv.pypa.io/en/latest/); installation of `asv>=0.4.2` and dependencies; cloning of the repository onto the target host; and manual calls to `asv` from the command line. This works until the wrapper script exists.

The package will be made installable through the specification of [PEP-518](https://www.python.org/dev/peps/pep-0518/)-compliant build requirements in the form of setup.py, setup.cfg, and pyproject.toml files. Wheels will be available for download via `pypi` (and eventually, `conda`).

## Setup
casabench installs CASA into `asv` runtime environments from wheels published in an NRAO-managed package repository, so the user's [pip configuration](https://pip.pypa.io/en/stable/topics/configuration/#location) needs to have these URLs included in the list that will be searched by the installer. Using the global level ensures that the configuration is respected by test executions inside each of the virtual environments created by asv.
```
[global]
extra-index-url = 
		https://casa-pip.nrao.edu:443/repository/pypi-group/simple
		https://casa-pip.nrao.edu/repository/pypi-casa-release/simple
```

An additonal step is required to configure access to test data:
```
git clone --no-checkout https://open-bitbucket.nrao.edu/scm/casa/casatestdata.git
cd casatestdata/
git config core.sparseCheckout true
echo performance/* >> .git/info/sparse-checkout
git checkout master
```
Note that is not working for all the tests right now since some prototype functions reference data which have not yet been added to the casatestdata repository. This will be fixed in the future. In the meantime, if you know where copies of the files live, you can place them in the expected directory structure:
```
casatestdata/
└── performance
    ├── calibration_runtime
    │   ├── uid___A002_Xe1f219_X6d0b.ms
    │   ├── uid___A002_Xe1f219_X6d0b.ms.hifa_bandpassflag.s12_1.spw16_18_20_22.channel.solintinf.bcal.tbl
    │   ├── uid___A002_Xe1f219_X6d0b.ms.hifa_bandpassflag.s12_3.spw16_18_20_22.solintinf.gacal.tbl
    │   ├── uid___A002_Xe1f219_X6d0b.ms.hifa_bandpassflag.s12_4.spw16_18_20_22.solintint.gpcal.tbl
    │   ├── uid___A002_Xe1f219_X6d0b.ms.h_tsyscal.s6_1.tsyscal.tbl
    │   └── uid___A002_Xe1f219_X6d0b.ms.s12.4.callibrary
    ├── flagdata_runtime
    │   ├── uid___A002_Xe1f219_X6d0b_data_autocorr_WRAY_scan7.ms
    │   └── uid___A002_Xe1f219_X6d0b.flagcmds.txt
    └── tclean_mem_setweighting
        └── uid___A002_Xb9dfa4_X4724_target_spw16.ms
```

## Running tests
The first time tests are run on a new machine you will have the option to contribute identifying [machine information](https://asv.readthedocs.io/en/stable/using.html#machine-information) if the host is not recognized, otherwise sensible defaults will be assigned automatically.

Invocation of the wrapper script that calls `asv` is yet to be completely defined, but will be supplied from the command line interface and have the form:
```bash
python -m casabench --use-case 1 --versions revision.txt --push-results repo
python -m casabench --use-case 2 --versions branches.txt --push-results web
```
These practically represent chained calls to `asv`, i.e.,
```
asv run --hashfile=revisions.txt
asv publish
git add results && git commit -m "Publish new results" && git push
```
and
```asv run --hashfile=revisions.txt
asv compare
asv gh-pages
```
respectively, but with the complication introduced by our build process properly accounted for by the wrapper script.

## Saving output
Once test results have been generated, they can saved by those with repository write access. One usage mode formats and pushes the results files themselves, and another generates static HTML content and either pushes it to the main [website](casangi.github.io/casabench/) or launches a local web server for transient analysis of the results.

For now, updating results in the repository will only be supported for those with repository write access. Contribution of results via pull request and command line interface will be considered in the future.

Alternative publication methods to explore include parsing the JSON ourselves to include it at the bottom of the [casadocs changelog](https://casadocs.readthedocs.io/en/latest/changelog.html).

## Details
### What the wrapper script does
Since the parts of casa6 this repo tests are split between two sub-repositories and it's complicated to make that (version-specific) build process conform to the project structure that `asv` expects, `casatasks` (and its `casatools` dependency) are installed via `airspeed-velocity`'s dependency handler. This is intended to be refactored once per-commit build and installation of both casatools and casatasks is working properly. 

Until then, it is necessary to edit the `asv.config.json` config file so that the value of the "include" parameter is unary (i.e., we can only test against one version at a time without producing redundant results at a large performance penalty). Then, the `asv run` command can be appropriately invoked, with input to the revision argument that matches the wheel version specified in the config file.

For example, to have `asv` build against CASA version 6.4.0.2, the configuration file must specify
`"include":[{"python":"3.6", "pip+casatools": "6.4.0.2", "pip+casatasks":"6.4.0.2"}]`, then all tests can be invoked using:
```
asv run tags/6.4.0.2^! --machine "NRAO workstation"
```
To run a particular class of benchmarks, the `--bench` parameter is specified, which accepts multiple arguments each of which is handled as a regular expression:
```
asv run --bench "flagdata" -b "calib" tags/6.4.0.2^! --machine "NRAO workstation"
```

The results database (a collection of JSON files) is tracked in the repository. Results files are organized by machine, so tests run from a fresh clone of the repository will build their own database. The HTML is generated from the files stored in the results database. In order to force `asv` to write HTML that treats the results as contiguous tests of the same package instead of separate entries in a dependency matrix, it is necessary to remove the build number from the casatools/casatasks specifications in the `params` and `requirements` dictionaries contained in the file corresponding to a given test configuration. For example,
```
...
"params": {"arch": "x86_64", "cpu": "Intel(R) Xeon(R) CPU E5-1660 v4 @ 3.20GHz", "machine": "NRAO workstation", "num_cpu": "16", "os": "Linux 3.10.0-1160.15.2.el7.x86_64", "ram": "32GB", "python": "3.6", "pip+casatools": "6.4.0.2", "pip+casatasks": "6.4.0.2"}, 
"requirements": {"pip+casatools": "6.4.0.2", "pip+casatasks": "6.4.0.2"},
...
```
is changed to
```
...
"params": {"arch": "x86_64", "cpu": "Intel(R) Xeon(R) CPU E5-1660 v4 @ 3.20GHz", "machine": "NRAO workstation", "num_cpu": "16", "os": "Linux 3.10.0-1160.15.2.el7.x86_64", "ram": "32GB", "python": "3.6", "pip+casatools": "6.4.0", "pip+casatasks": "6.4.0"}, 
"requirements": {"pip+casatools": "6.4.0", "pip+casatasks": "6.4.0"},
...
```
Someday in the future it would be great to refactor casabench to build both `casatools` and `casatasks` from source, since that's what the framework is designed to do and it would make the wrapper script redundant. In practice, after many attempts, the `casatools` build process proved too cumbersome to integrate with `asv` in this fashion (we got `casatasks` to work, but since there is a requirement that both tools and tasks are at the same version, it was equally complicated to manage so we decided to follow the current architecture).
