# casabench
Tracking performance metrics of CASA

## Setup
Once the repository is cloned, an additonal step is required to configure access to test data:
.. code-block:: console
    git clone --no-checkout https://open-bitbucket.nrao.edu/scm/casa/casatestdata.git
    cd casatestdata/
    git config core.sparseCheckout true
    echo performance/* >> .git/info/sparse-checkout
    git checkout master

Note that is not working for all the tests right now since some prototype functions were written to directly reference files on disk in the sandbox environment. This will be fixed in the future when all data required to run the tests have been added to the casatestdata repository.

## Running tests

Right now the building of the project is skipped (since the parts of casa6 this repo will tests are split between two repositories and it's complicated to make that work with the project structure that `asv` expects...work in progress) and the project is installed via `airspeed-velocity`'s dependency handler. So this is kind of hacky for now, but to run all of the tests for all of the versions specified in the config file::

    asv run master^! --machine "NRAO workstation"

To run a particular class of benchmarks::

    asv run master^! --bench "calibration" --machine "NRAO workstation"

If adding a new benchmark on a new machine, you will need to follow the prompts for contributing machine information. For more details see the `asv docs<https://asv.readthedocs.io/en/stable/using.html#running-benchmarks>`_