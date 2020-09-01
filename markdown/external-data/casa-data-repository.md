

# CASA Data Repository 

The CASA Data Repository, and how to update geodetic and ephemeris data in CASA.

Each CASA distribution comes with a minimal repository of binary data that is required for CASA to function properly. This repository includes [Measures Tables](https://casa.nrao.edu/casadocs-devel/stable/external-data/casacore-measures-tables) that deal with reference frames, as well as ephemeris data. Over time (couple of months), the geodetic and possibly ephemeris data in this repository slowly drifts out of date. Because of this, the distribution data repository must be updated occasionally. Other data that is updated less frequently is also stored in the repository, such as beam models, antenna and Jy/K correction tables, and the antenna configuration files for the CASA simulator.

A snapshot of this repository is included in each tarball distribution of CASA, and in the casadata module for CASA 6+. The owner (in the Linux filesystem sense) of the CASA distribution can update the data repository to the latest available version by running from within CASA:

``` {.p1}
CASA <2>: ! update-data
```

 or, when using the modular pip-wheel CASA distribution:

``` {.p1}
-bash-4.2$ pip install casadata --upgrade
```

 

It is possible to use rsync to get the partial data repository as used in the CASA distributions (CASA 5 and 6):

``` {.p1}
rsync -avz rsync://casa-rsync.nrao.edu/casa-data casa-data
```

This does not contain the regression data.

 

 

<div>

It is also possible to use rsync to get the complete data repository:

</div>

``` {.p1}
rsync -avz rsync://casa-rsync.nrao.edu/casa-data-repository casa-data
```

In this case you get the entire repository, but there is no way to pick and choose which pieces you get.

 

 

