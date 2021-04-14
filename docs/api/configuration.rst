configuration
=====================

CASA accepts a variety of options through two mechanisms: configuration files and command line arguments.  Configuration files are
typically stored in a \~/.casa folder while command line options (only applicable to the full installation) are specified after the
casa command at startup.


config.py
^^^^^^^^^

Each modular CASA 6 package as well as the full installation reads a single **config.py** configuration file. This file should be
placed in the user root .casa folder (**\~/.casa**) prior to starting the casa installation or importing the packages in to a standard
python environment for the first time.

The following parameters can be set in the configuration file. Finer control over telemetry can also be set in the configuration file,
as described `here <../../notebooks/usingcasa.ipynb#telemetry>`__.

- *datapath*              : list of paths where CASA should search for runtime data
- *logfile*               : log file path/name
- *telemetry_enabled*     : allow anonymous usage reporting, default True
- *crashreporter_enabled* : allow anonymous crash reporting, default True

The configuration file is a standard python script, so any valid python syntax and libraries can be used.  A typical config.py file
might look something like this:

::

   $ cat ~/.casa/config.py

   import time

   datapath=["/home/casa/data/casa-data", "/home/casa/data/casa-data-req"]
   logfile='casalog-%s.log' % time.strftime("%Y%m%d-%H",time.localtime())
   telemetry_enabled = True
   crashreporter_enabled = True


At runtime the datapath(s) are expanded through a resolve(\...) function to find the needed data tables. For example

::

   >>> casatools.ctsys.resolve('geodetic/IERSpredict')

   '/home/casa/data/casa-data/geodetic/IERSpredict'

The command line arguments take precendence over the equivalent config.py value.


.. warning::

   **WARNING**: CASA 5 does not use config.py. Instead ~/.casa/prelude.py is evaluated during startup before anything else
   and ~/.casa/init.py is evaluated just before the CASA prompt is presented. The configuration options are different and more limited.


startup.py
^^^^^^^^^^

*This section only applies to the monolithic/tar-file CASA distribution, and it only applies to CASA 6.*

For CASA 5, use *\~/.casa/init.py* instead. *startup.py* should be Python 3 compliant whereas *init.py* is assumed to be Python 2.7.

The \'*startup.py*\' file found in *\$HOME/.casa* (i.e. *\~/.casa/startup.py*) is evaluated by the CASA shell just before the CASA
prompt is presented to the user. This allows users to customize their CASA shell environment beyond the standard settings in
\'*config.py*\', by importing packages, setting variables or modifying the python system path.

One case where this is useful is for configuring CASA for ALMA data reduction. A package called \'analysisUtils\' is often used as part
of ALMA analysis. It is typically imported and instantiated in startup.py:

::

   $ cat ~/.casa/startup.py

   import sys, os
   sys.path.append("/home/casa/contrib/AIV/science/analysis_scripts/")
   import analysisUtils as aUes = aU.stuffForScienceDataReduction()


In this example, the standard python modules *os* and *sys* are made available in the CASA shell. The path where the *analysisUtils*
module can be found is added to the Python system path, and finally the package is imported and an object is created. These modules
and objects will then be available for the user within the CASA shell environment.



command line
^^^^^^^^^^^^

With the full installation of CASA from a tar file, the python environment itself is included and started through ./bin/casa.
This ./bin/casa executable can be provided the following options to change configuration values at run time:

::

   -h, --help            show this help message and exit
   --logfile LOGFILE     path to log file
   --log2term            direct output to terminal
   --nologger            do not start CASA logger
   --nologfile           do not create a log file
   --nogui               avoid starting GUI tools
   --rcdir RCDIR         location for startup files
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


These options **take precedence over the configuration files.**

Some options imply or take precedence over other options:

-   \--nologfile takes precedence over \--logfile
-   \--nogui implies \--nologger
-   \--pipeline implies \--agg

.. note::

   --rcdir is used to change the location of the root .casa folder to something other than **\~/.casa**. In addition to the startup
   files (config.py and startup.py) the root .casa folder contains working files and directories used by CASA components (e.g. ipython,
   telemetry).

.. warning::

   the command line arguments listed above apply to CASA 6. In CASA 5 (including CASA 5.7):


- The following command line arguments are still available (removed/replaced in CASA 6):

::

   --telemetry (removed in favor of --notelemetry in CASA 6)
   --trace
   --maclogger

- the following command line arguments are not available:

::

   --norc
   --notelemetry
   --datapath
   --user-site


