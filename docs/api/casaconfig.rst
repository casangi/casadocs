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

The defaults are shown below. **Note** that the default *logfile* uses the time module to set the value to a string that depends on when 
the config file is evaluated. **Note** that in the monolithic casa case, *datapath* and *measurespath* will default to the data directory 
in the casaconfig package (returned by *get_data_dir()*).

.. include:: ../config_defaults_static.py
   :literal:
