# casabench
## Tracking performance metrics of CASA

The scope of this study is to use performance and benchmarking tests to satisfy two use-cases:
1. For every CASA master tarball created, to characterize trends in performance metrics across repository history
2. As part of the verification of development branches, to detect and isolate code that causes issues with performance metrics before it is merged with the main trunk

This prototype makes use of the [airspeed-velocity](https://asv.readthedocs.io/en/stable/) framework to satisfy use case 1 (UC2 is a work in progress). This repository could be modified to work with other tools in the future.  Right now casabench is pre-alpha software, not intended for general use.

## Setup
Once the repository is cloned, it can be used from any conda or pip virtual environment that has `asv>=0.4.2` installed (to be reflected in a pyproject.toml or requirements.txt file soon).

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
If running tests on a new machine (i.e., not the development sandbox), you will need to follow the prompts for contributing machine information. For more details see the [asv docs](https://asv.readthedocs.io/en/stable/using.html#running-benchmarks).

## Running tests

Right now the building of the project is skipped (since the parts of casa6 this repo will test are split between two repositories and it's complicated to make that work with the project structure that `asv` expects...work in progress) and the project is installed via `airspeed-velocity`'s dependency handler. This is intended to be refactored once per-commit build and installation of both casatools and casatasks is working properly. 

Until then, it is necessary to edit the `asv.config.json` config file so that the value of the "include" parameter is unary (i.e., we can only test against one version at a time). Then, the `asv run` command can be invoked with input to the revision argument that matches the wheel version specified in the config file.

For example, to have `asv` build against CASA version 6.4.0.2, the configuration file must specify
`"include":[{"python":"3.6", "pip+casatools": "6.4.0.2", "pip+casatasks":"6.4.0.2"}]`, then all tests can be invoked using:
```
asv run tags/6.4.0.2^! --machine "NRAO workstation"
```
To run a particular class of benchmarks, use the `--bench` (or `-b`) parameter, which accepts multiple arguments each of which is handled as a regular expression:
```
asv run --bench "flagdata" -b "calibration" tags/6.4.0.2^! --machine "NRAO workstation"
```
For now it is necessary to remove the build number from the casatools/casatasks specifications in the `params` and `requirements` dictionaries contained by the generated JSON results file corresponding to a given test configuration. This allows `asv publish` to build HTML that treats the results from different environments as contiguous tests instead of separate entries in a dependency matrix. For example,
```
...
"params": {"arch": "x86_64", "cpu": "Intel(R) Xeon(R) CPU E5-1660 v4 @ 3.20GHz", "machine": "NRAO workstation", "num_cpu": "16", "os": "Linux 3.10.0-1160.15.2.el7.x86_64", "ram": "32GB", "python": "3.6", "pip+casatools": "6.4.0.2", "pip+casatasks": "6.4.0.2"}, 
"requirements": {"pip+casatools": "6.4.0.2", "pip+casatasks": "6.4.0.2"},
...
```
should be changed to
```
...
"params": {"arch": "x86_64", "cpu": "Intel(R) Xeon(R) CPU E5-1660 v4 @ 3.20GHz", "machine": "NRAO workstation", "num_cpu": "16", "os": "Linux 3.10.0-1160.15.2.el7.x86_64", "ram": "32GB", "python": "3.6", "pip+casatools": "6.4.0", "pip+casatasks": "6.4.0"}, 
"requirements": {"pip+casatools": "6.4.0", "pip+casatasks": "6.4.0"},
...
```
We could simply automate this step if it proves to be too cumbersome, but it shouldn't be necessary once per-commit builds are working as expected.

## Preparing results for publication

Details about committing results back to the repository are forthcoming.
We can explore the use of a branch for publishing results using gh-pages (a built-in feature of `asv`), parse the JSON to include it at the bottom of the [casadocs changelog](https://casadocs.readthedocs.io/en/latest/changelog.html), or explore alternative methods.
