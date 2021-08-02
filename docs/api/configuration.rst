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
as described `here <../notebooks/usingcasa.ipynb#Information-Collection>`__.

- *datapath*              : list of paths where CASA should search for runtime data
- *rundata*               : location to update runtime data
- *logfile*               : log file path/name
- *nologfile*             : do not create a log file when True, default False. If *nologfile* is true, then any *logfile* value is ignored and there is no log file.
- *log2term*              : print log output to terminal when True (in addition to any logfile and CASA logger), default False
- *nologger*              : do not start the CASA logger when True, default False
- *nogui*                 : avoid starting GUI tools when True, default False. If *nogui* is True then the CASA logger is not started even if *nologger* is False.
- *colors*                : the IPython prompt color scheme. Must be one of "Neutral", "NoColor", "Linux" or "LightBG", default "Neutral". If an invalid color is given a warning message is printed and logged but CASA continues using the default color.
- *agg*                   : startup without a graphical backend if True, default False
- *pipeline*              : attempt to load the pipeline modules and set other options appropriate for pipeline use if True, default False. When *pipeline* is True then *agg* will be assumed to be true even if *agg* is set to False here or on the command line.
- *iplog*                 : create and use an IPython log in the current directory if True, default False.
- *telemetry_enabled*     : allow anonymous usage reporting, default True
- *crashreporter_enabled* : allow anonymous crash reporting, default True
- *user_site*             : include the user's local site-packages in the python path if True. Normally these are excluded to avoid any conflicts with CASA modules (when False, the default).

The configuration file is a standard python script, so any valid python syntax and libraries can be used.  A typical config.py file
might look something like this:

::

   datapath=["/home/casa/data/casa-data", "~/.casa/mydata"]
   rundata="~/.casa/mydata"
   log2term=True
   nologger=True
   
An example config.py file showing all recognized configurable parameters is shown here, this also illustrates that config.py can contain other python commands. This shows setting logfile using the time module. Note that some of the parameters shown here are set to the their default values.

::

   import time
   
   datapath=["/home/casa/data/casa-data", "~/.casa/mydata"]
   rundata="~/.casa/mydata"
   logfile='casalog-%s.log' % time.strftime("%Y%m%d-%H",time.localtime())
   telemetry_enabled = True
   crashreporter_enabled = True
   nologfile = False
   log2term = True
   nologger = True
   nogui = False
   colors = "LightBG"
   agg = False
   pipeline = False
   iplog = True
   user_site = False
   telemetry_log_directory = /tmp
   telemetry_log_limit = 1650
   telemetry_log_size_interval = 30
   telemetry_submit_interval = 20
   

At runtime the datapath(s) are expanded through a resolve(\...) function to find the needed data tables. For example

::

   >>> casatools.ctsys.resolve('geodetic/IERSpredict')

   '/home/casa/data/casa-data/geodetic/IERSpredict'

The command line arguments discussed later take precendence over the equivalent config.py value.

.. note::

   *rcdir* is used to change the location of the root .casa folder to something other than **\~/.casa**. In addition to the startup
   files (config.py and startup.py) the root .casa folder contains working files and directories used by CASA components (e.g. ipython,
   telemetry). It is expected to be writable by the user for use by those components.

startup.py
^^^^^^^^^^

*This section only applies to the monolithic/tar-file CASA distribution.*

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
