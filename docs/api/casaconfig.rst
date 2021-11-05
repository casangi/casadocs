casaconfig
====================

Routines for handling the runtime configuration and external data dependencies in CASA. These functions are needed to manipulate the runtime data
necessary for proper CASA operation.

.. automodsumm:: casaconfig
   :toctree: tt
   :nosignatures:
   :functions-only:



config.py
^^^^^^^^^

.. data:: config.py

Each modular CASA 6 package as well as the full monolithic installation reads a single **config.py** configuration file
to setup the CASA runtime options. A default config.py is included within the casaconfig package.
This default config.py provides automatic initial population and daily maintenance of casaconfig data tables,
and defines the allowable configuration settings for the CASA runtime.

This file will be loaded unless the user places their own version in
their home area .casa folder (**\~/.casa**) prior to starting the casa installation or importing the packages into a standard
python environment for the first time.

.. include:: ../config.py
   :literal:



terminal
^^^^^^^^

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
   --rcdir RCDIR         location for startup files, internal working files
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


These options **take precedence over the configuration files.** See the discussion of equivalent config.py parameters
for more details on these command line options.
