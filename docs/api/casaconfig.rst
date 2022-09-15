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

.. data:: configuration values

::

    from casaconfig import config

Each modular CASA 6 package as well as the full monolithic installation reads a set of configuration files
to setup the CASA runtime options. The configuration is set when config is imported from casaconfig. The
configuration files include the default values (always provided by casaconfig), an optional site configuration file, 
and an optional user configuration file.

The optional user configuration file is found in their home .casa folder as config.py (**\_/.casa/config.py**).

The optional site configuration file is named **casasiteconfig.py** and is found anywhere within **sys.path** following the usual pyhthon import rules.

The user configuration files is ignored when **\-\-noconfig** is used on the command line. The site configuration file is 
ignored when **\-\-nositeconfig** is used on the command line.

An alternative path to the user configuration file can be given using the **--configfile <path_to_file>** option on the command line.

The configuration files are used in order of defaults, site configuration, user configuration. The optional configuration files need
only set parameters that differ from the defaults. The resulting configuration will always include all of the recognized
configuration values. The configuration files are evaluated python files so any valid python can be used. **Note:**, configuration h
appens before any parts of CASA are loaded so no CASA modules except casaconfig should be used within the configuration steps
(the casaconfig functions do not depened on config.py and can be used within a configuration file). **Note:** during regular 
use of the configuration process all print output is suppressed so that it does not interfere with module initialization. 

Use the get_config() function to get a list of strings showing the configuration parameters with values.

The following parameters can be set in a configuration file. Additional details related to the
telemetry parameters are descrbed `here <../notebooks/usingcasa.ipynb#Information-Collection>`__. Many of these
parameters can be set or ignored through the casashell command line options.

- *datapath*              : list of paths where CASA should search for data subdirectories
- *measurespath*          : location of required measures data, takes precedence over any measures data also present in datapath
- *measures_update*       : when True, casatools uses *measures_update()* to update the measures data as necessary when casatools starts. See *measures_update()* for additional details.
- *startupfile*           : path to a python script used at startup by casashell when present
- *cachedir*              : location of the directory where ipython writes information (history, etc), also the location of the rc file used by the casaviewer.
- *logfile*               : log file path/name
- *nologfile*             : do not create a log file when True, default False. If *nologfile* is true, then any *logfile* value is ignored and there is no log file.
- *log2term*              : print log output to terminal when True (in addition to any logfile and CASA logger), default False
- *nologger*              : do not start the CASA logger GUI when True, default False
- *nogui*                 : avoid starting GUI tools when True, default False. If *nogui* is True then the CASA logger is not started even if *nologger* is False.
- *colors*                : the IPython prompt color scheme. Must be one of "Neutral", "NoColor", "Linux" or "LightBG", default "Neutral". If an invalid color is given a warning message is shown but CASA continues using the default color.
- *agg*                   : startup without a graphical backend if True, default False
- *pipeline*              : attempt to load the pipeline modules and set other options appropriate for pipeline use if True, default False. When *pipeline* is True then *agg* will be assumed to be true even if *agg* is set to False here or on the command line.
- *iplog*                 : create and use an IPython log if True, default False.
- *iplogfile*             : IPython log file path/name, used only when iplog is True.
- *telemetry_enabled*     : allow anonymous usage reporting, default True
- *telemetry_log_directory* : path to location where telemetry log is recorded
- *telemetry_log_limit*   : maximum telemetry log usage in kilobytes
- *telemetry_log_size_interval* : the interval between checks on the telemetry log size in seconds
- *telemetry_submit_interval* : the interval between submissions of telemetry data on CASA startup in seconds
- *crashreporter_enabled* : allow anonymous crash reporting, default True
- *user_site*             : include the user's local site-packages in the python path if True. Normally these are excluded to avoid potential conflicts with CASA modules (when False, the default).

A typical config.py file might look something like this:

::

   datapath=["/home/casa/data/casa-data", "~/.casa/my_additional_data"]
   log2term=True
   nologger=True

The defaults are shown below. **Note** that the default *logfile* uses the time module to set the value to a string that depends on when 
the config file is evaluated. **Note** that in the monolithic casa case, *datapath* and *measurespath* will default to the data directory 
in the casaconfig package (returned by *get_data_dir()*).

.. include:: ../config_defaults_static.py
   :literal:
   
 startup.py
 ^^^^^^^^^^
 
 .. data:: startup.py

*This section only applies to the monolithic/tar-file CASA distribution*

The \'*startup.py*\' file found at the *startupfile* configuration value (defaults to *\~/.casa/startup.py*) is evaluated 
by the CASA shell just before the CASA prompt is presented to the user. This allows users to customize their CASA shell 
environment beyond the standard settings in \'*config.py*\', by importing packages, setting variables or modifying 
the python system path. The startup file is optional. It can be ignored setting startupfile in configuration file to 
indicate a path that does not exist or by using the *\-\-nostartupfile* casashell command line option.

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

terminal
^^^^^^^^

.. data:: terminal(-h, --help, --logfile, --log2term, --nologger, --nologfile, --nogui, --rcdir, --norc, --colors, --pipeline, --agg, --iplog, --notelemetry, --nocrashreport, --datapath, --user-site, -v, --version, -c)

With the full installation of CASA  (monolithic CASA), the python environment itself is included and started through ./bin/casa.
This ./bin/casa executable can be provided the following options to change configuration values at run time:

::

   -h, --help               show this help message and exit
   --configfile CONFIGFILE  location of the user configuration file
   --noconfig               do not load user configuration file
   --nositeconfig           do not load site configuration file
   --startupfile            path to user's startup file
   --nostartupfile          do not use any startup file
   --logfile LOGFILE        path to log file
   --log2term               direct output to terminal
   --nologger               do not start CASA logger
   --nologfile              do not create a log file
   --nogui                  avoid starting GUI tools
   --cachedirr CACHEDIR     location for internal working files
   --colors {Neutral,NoColor,Linux,LightBG} prompt color
   --pipeline               start CASA pipeline run
   --agg                    startup without graphical backend
   --iplog                  create ipython log
   --notelemetry            disable telemetry collection
   --nocrashreport          do not submit an online report when CASA crashes
   --datapath DATAPATH      data path(s) [colon separated]
   --user-site              include user's local site-packages lib in path
   -v, --version            show CASA version
   -c ...                   python eval string or python script to execute


These options **take precedence over the configuration files.** 

THe \-\-configfile option is used to provide an alternative path to the user's configuration file. When that
option is used the file at that location is used insteead of the default user configuration file (~/.casa/config.py).
The \-\-noconfig option turns off all use of aany user's configuration file. If \-\-configfile and \-\-noconfig file
are used at the same time, the user's configuration file is ignored and a warning message is printed.

Tthe \-\-nostartupfile option is provided as a way to turn off loading of the startup file, That can also be
done by setting startupfile to a non-existant file or empty string in a configuration file. If \-\-startupfile
and \-\-nostartupfile are used at the same time no startup file is used and a warning message is printed.

\-\-notelemetry sets the telemetry_enabled configuration parameter to False.

\-\-nocrashreport sets the crashreporter_enabled configuration parameter to False.

