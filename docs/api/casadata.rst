casadata
====================

.. currentmodule:: casadata

Routines for handling external data dependencies in CASA. These functions are needed to manipulate the runtime data
necessary for proper CASA operation.

update-data
^^^^^^^^^^^

.. data:: update-data

   Command line application bundled in monolitic CASA.  Takes no inputs.  Updates default casadata package installation to latest.
   Callable from within the CASA shell via:

   ::

      CASA <1>: !update-data


update-user-data
^^^^^^^^^^^^^^^^

.. data:: update-user-data

   runtime argument passed to Python when calling casatools module directly.  Updates the casadata contents from specified location
   to match current contents of casadata repository.  If no location is specified, defaults to the location pointed to by the rundata
   variable in config.py.

   ::

      bash$ python -m casatools --update-user-data=/tmp/mydata

   ::

      bash$ python -m casatools --update-user-data


rsync
^^^^^

.. data:: rsync

   rsync server holding a copy of the casadata repo and updated daily. Available as an alternative method of syncing user directories.

   ::

      rsync -avz rsync://casa-rsync.nrao.edu/casa-data <location of casadata tables>

