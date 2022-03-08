casalith
====================

CASA monolithic environment bundling Python and library dependencies into a single download package.

.. currentmodule:: casalith


executables
^^^^^^^^^^^

The following executable applications are located in the <casa release>/bin directory of the expanded monolithic CASA tarball:

.. data:: python3(v3.6.7)

.. data:: pip3(v9.0.1)

.. data:: 2to3

.. data:: casa

.. data:: mpicasa

.. data:: casaviewer

.. data:: buildmytasks



startup options
^^^^^^^^^^^^^^^

.. data:: terminal(-h, --help, --logfile, --log2term, --nologger, --nologfile, --nogui, --rcdir, --norc, --colors, --pipeline, --agg, --iplog, --notelemetry, --nocrashreport, --datapath, --user-site, -c)

With the full installation of CASA from a tar file, the python environment itself is included and started through ./bin/casa.
This ./bin/casa executable can be provided the following options to change configuration values at run time:

::

   -h, --help            show this help message and exit
   --logfile LOGFILE     path to log file
   --log2term            direct output to terminal
   --nologger            do not start CASA logger
   --nologfile           do not create a log file
   --nogui               avoid starting GUI tools
   --rcdir RCDIR         location for startup files, internal working files and config.py
   --norc                do not load user config.py (startup.py is unaffected)
   --colors {Neutral,NoColor,Linux,LightBG} prompt color
   --pipeline            load CASA pipeline modules on startup
   --agg                 startup without graphical backend
   --iplog               create ipython log
   --notelemetry         disable telemetry collection
   --nocrashreport       do not submit an online report when CASA crashes
   --datapath DATAPATH   data path(s) [colon separated]
   --user-site           include user's local site-packages lib in path
   (toggling this option turns it on; use startup.py to append to the path)
   -c ...                python eval string or python script to execute



tasks
^^^^^

A few remaining tasks are found only in the monolithic environment

.. automodsumm:: casalith
   :toctree: tt
   :nosignatures:
   :functions-only:



python libraries
^^^^^^^^^^^^^^^^

The following third party libraries are included in the python distribution of monolithic casa and available as imports:

.. data:: libraries(attrs==19.3.0, backcall==0.1.0, certifi==2020.12.5, cycler==0.10.0, decorator==4.4.2, grpcio==1.29.0, importlib-metadata==1.6.0, ipython==7.15.0, ipython-genutils==0.2.0, jedi==0.17.0, kiwisolver==1.2.0, matplotlib==3.2.1, more-itertools==8.3.0, mpi4py==3.0.3, numpy==1.18.4, packaging==20.4, parso==0.7.0, pexpect==4.8.0, pickleshare==0.7.5, pluggy==0.13.1, prompt-toolkit==3.0.5, protobuf==3.12.2, ptyprocess==0.6.0, py==1.8.1, pyfits==3.5, Pygments==2.6.1, pyparsing==2.4.7, pytest==5.4.2, python-dateutil==2.8.1, pytz==2020.1, scipy==1.4.1, six==1.15.0, traitlets==4.3.3, wcwidth==0.2.2, zipp==3.1.0)


Note that each component in the modular CASA distribution uses a subset of these same dependencies.

The definition is provided here in pip compatible format such that one could save the preceding list to a list.txt file and
recreate using:

::

   pip install -r list.txt



startup.py
^^^^^^^^^^

.. data:: startup.py

*This section only applies to the monolithic/tar-file CASA distribution, and it only applies to CASA 6.*

For CASA 5, please see `an earlier version of CASA Docs <https://casadocs.readthedocs.io/en/v6.2.0/api/configuration.html#startup-py>`__.

The \'*startup.py*\' file found in *\$HOME/.casa* (i.e. *\~/.casa/startup.py*) is evaluated by the CASA shell just before the CASA
prompt is presented to the user. This allows users to customize their CASA shell environment beyond the standard settings in
\'*config.py*\', by importing packages, setting variables or modifying the python system path.

One case where this is useful is for configuring CASA for ALMA data reduction. A package called \'analysisUtils\' is often used as part
of ALMA analysis. It is typically imported and instantiated in startup.py:

::

   $ cat ~/.casa/startup.py

   import sys, os
   import analysisUtils as aU
   
   sys.path.append("/home/casa/contrib/AIV/science/analysis_scripts/")
   es = aU.stuffForScienceDataReduction()


In this example, the standard python modules *os* and *sys* are made available in the CASA shell. The path where the *analysisUtils*
module can be found is added to the Python system path, and finally the package is imported and an object is created. These modules
and objects will then be available for the user within the CASA shell environment.
