# casabench
## Tracking the performance of CASA
The scope of this repository is the automatic execution of performance benchmarking tests that satisfy two use-cases:
1. To characterize trends in performance metrics across [CASA6](https://open-bitbucket.nrao.edu/projects/CASA/repos/casa6/browse/casatasks) repository history (after releases are published from the main trunk)
2. To detect code causing performance issues during verification of development branches (before changes are merged with the main trunk)

To satisfy these use cases, this prototype uses a wrapper script to coordinate calls to the [airspeed-velocity](https://asv.readthedocs.io/en/stable/) (`asv`) framework, which manages the execution of tests (located in the `benchmarks` directory). The successful execution of benchmarks produces environment-specific performance data (stored in [JSON](https://www.json.org/json-en.html) format in the `results` directory), and further calls to `asv` generate an [HTML](https://html.spec.whatwg.org/) representation of the results and automatic regression analysis (published to the web from a dedicated branch via [GitHub pages](https://pages.github.com/both)). This repository could be modified to work with other tools in the future, including `asv`'s integration with the Python standard library [profiler](https://docs.python.org/3/library/profile.html#the-python-profilers).  

Right now casabench is open-beta software, mainly intended to satisfy internal use cases, automation of which is accomplished through the use of wrapper scripts deployed using Bamboo for [use case 1](https://open-bamboo.nrao.edu/chain/viewChain.action?planKey=CASA-PERF) and [use case 2](https://open-bamboo.nrao.edu/chain/viewChain.action?planKey=CASA-PERFDEV).

## Installation
This package is not intended to be installable from a wheel distribution at this time. Usage at this stage relies on creation of a python environment, using either [`conda`](https://docs.conda.io/en/latest/miniconda.html) or [`virtualenv`](https://virtualenv.pypa.io/en/latest/); installation of `asv>=0.4.2` and dependencies; cloning of this repository onto the target host; and manual calls to `asv` from a shell.

## Setup
When asv is run, casabench clones and installs CASA into `asv` runtime environments from wheels published in an NRAO-managed package repository, so the user's [pip configuration](https://pip.pypa.io/en/stable/topics/configuration/#location) needs to have these URLs included in the list that will be searched by the installer. Using the global level ensures that the configuration is respected by test executions inside each of the virtual environments created by asv.
```
[global]
extra-index-url = 
		https://casa-pip.nrao.edu:443/repository/pypi-group/simple
		https://casa-pip.nrao.edu/repository/pypi-casa-release/simple
```

Additonally, it is required to configure access to the test data repository (see [casadocs](https://casadocs.readthedocs.io/en/stable/api/configuration.html?#config-py) for more details), i.e., ensure that the `config.py` for the user who will run the tests contains an entry that references a clone of the CASA runtime data repository:
```
datapath=['/path/to/casatestdata/']
```

## Adding tests
Tests are organized by casatask name, so new tests for an existing task should be appended to the casabench/benchmarks/bench_taskname.py script, and new tests for tasks without an existing test script should follow this convention. Timing tests should include only the task invocation itself, with steps that modify state confined to a setup method so that their runtime is not included in the results. asv test iteration (configuration parameters)[https://asv.readthedocs.io/en/stable/benchmarks.html#timing-benchmarks] are defined on a per-script basis, so shorter running tests can include more samples for better statistics.

## Running tests
The first time tests are run on a new machine you will have the option to contribute identifying [machine information](https://asv.readthedocs.io/en/stable/using.html#machine-information) if the host is not recognized, otherwise sensible defaults will be assigned.

Since the parts of CASA6 this repo imports to test are split between submodules (`casatasks`, `casatools`, `casatestutils`) and it's complicated to make that (version-specific) build process conform to the project structure expected by `asv`, CASA6 is installed via `asv`'s dependency handler. To make this work, it is necessary to edit the `asv.config.json` config file so that the value of the "include" parameter is unary (i.e., we can only test against one version at a time without producing redundant results at a large performance penalty). This version string must be consistent for each of the wheels we want to test with, then the `asv run` command can be appropriately invoked, with input to the revision argument that matches the wheel version specified in the config file.

For example, to have `asv` build against CASA version 6.5.3.1, the configuration file must specify
```
  "include": [
    {
      "python": "3.6",
      "pip+casatasks": "6.5.3.1",
      "pip+casatestutils": "6.5.3.1"
    }
  ],
```
Note that casatools is installed as an implicit dependency of casatasks.  After that, all tests can be invoked using:
```
asv run tags/6.5.3.1^! --machine "myhost"
```
To run a particular class of benchmarks, the `--bench` parameter is specified, which accepts multiple arguments each of which is handled as a regular expression:
```
asv run --bench "flagdata" --bench "calib" tags/6.5.3.1^! --machine "myhost"
```

Warning: it is possible to run asv using a CASA6 git tag that does not match the wheel version specified in the asv config file. In this case, the requested wheel will be installed and tested against, but the CASA6 repository state will reflect the version specified by the "include" parameter of the asv config file. This can lead to confusing/erroneous results.

## Saving results
Once test results have been generated, they can be saved by those with repository write access. The results database (a collection of JSON files) is tracked in the repository and published on a dedicated branch. Results files are categorized by machine, so tests run from a fresh clone of the repository will build their own entry in the database. The HTML is generated from the files stored in the results database. In order to force `asv` to write HTML that treats the results as contiguous tests of the same package instead of separate entries in a dependency matrix, it is necessary to strip the build number from the casatools/casatasks specifications in the `params` and `requirements` dictionaries contained in the file corresponding to a given test configuration. For example,
```
{"commit_hash": "3024d7185f18b56ed8bc709d823ac56cb311c66e", "env_name": "virtualenv-py3.6-pip+casatasks-pip+casatasks6.5.0.1-pip+casatestutils6.5.0.1", "date": 1648490240000, "params": {"arch": "x86_64", "cpu": "Intel(R) Xeon(R) CPU E5-2670 0 @ 2.60GHz", "machine": "casa-perf-test", "num_cpu": "16", "os": "Linux 3.10.0-1160.71.1.el7.x86_64", "ram": "263925792", "python": "3.6", "pip+casatasks": "6.5.0.1", "pip+casatestutils": "6.5.0.1"}, "python": "3.6", "requirements": {"pip+casatasks": "trunk", "pip+casatestutils": "6.5.0.1"}, 
...
```
is changed to
```
{"commit_hash": "3024d7185f18b56ed8bc709d823ac56cb311c66e", "env_name": "virtualenv-py3.6-pip+casatasks-trunk", "date": 1648490240000, "params": {"arch": "x86_64", "cpu": "Intel(R) Xeon(R) CPU E5-2670 0 @ 2.60GHz", "machine": "casa-perf-test", "num_cpu": "16", "os": "Linux 3.10.0-1160.71.1.el7.x86_64", "ram": "263925792", "python": "3.6", "pip+casatasks": "trunk"}, "python": "3.6", "requirements": {"pip+casatasks": "trunk"},
...
```
This ensures that all entries in the results database are treated as a single dependency: "casatasks" with version "trunk". Also note that the casatools and casatestutils dependencies are removed from the results files for the sake of brevity.

For now, updating results in the repository will only be supported for those with repository write access. Contribution of results via pull request and command line interface will be considered in the future.
