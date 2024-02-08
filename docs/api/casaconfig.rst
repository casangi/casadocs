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

Each modular CASA package as well as the full monolithic installation reads a set of configuration files
to set the CASA runtime options. The configuration is set when config is imported from casaconfig. The
configuration files include the default values (provided by casaconfig), an optional site configuration file, 
and an optional user configuration file.

The optional user configuration file is found in their home .casa folder as config.py (**\~/.casa/config.py**).

The optional site configuration file is named **casasiteconfig.py** and is found anywhere within **sys.path** 
following the usual python import rules.

The user configuration file is ignored when **\-\-noconfig** is used on the command line. 

The site configuration file is ignored when **\-\-nositeconfig** is used on the command line.

An alternative path to the user configuration file can be given using the **\-\-configfile <path_to_file>** option 
on the command line.

The configuration files are used in order of defaults, site configuration, user configuration. The optional 
configuration files need only set parameters that differ from the defaults. The resulting configuration 
will always include the full set of configuration parameters recognized by CASA. The configuration files are 
evaluated python files so any valid python can be used.

On import, the dict of config values also contains 2 functions: **load_success** and **load_failure**. **load_success**
returns a list of config file paths used when config was imported, in the order they were used. **load_failure** 
returns a dictionary of exceptions encountered by config file when loading that config file (and then that config file
is not found in the list returned by **load_success**).

**Note:** configuration happens before any parts of CASA are loaded so no CASA modules should be used within the 
configuration steps.

**Note:** during regular use of the configuration process all print output is suppressed so that it 
does not interfere with module initialization. 

Use the **get_config()** function to get a list of strings showing the configuration parameters with values.

**Note:** all path configuration values are expanded using expanduser and abspath.

The following parameters can be set in a configuration file. Many of these
parameters can be set or ignored through the casashell command line options. The default values are also shown here.

- *datapath*              : list of paths where CASA should search for data subdirectories. Default [*measurespath*].
- *measurespath*          : location of required measures data, takes precedence over any measures data also present in datapath. Default "~/.casa/data".
- *measures_auto_update*  : when True, casatools uses **measures_update()** to update the measures data as necessary when casatools starts. See **measures_update()** for additional details. Default True.
- *data_auto_update*      : when True, casatools uses **data_update()** followed by **measures_update()** to update the reference **AND** measures data. See **data_update()** and **measures_update()** for additional details. Default True.
- *startupfile*           : path to a python script used at startup by casashell when present. Default "~/.casa/startup.py".
- *cachedir*              : location of the directory where ipython writes information (history, etc), also the location of the rc file used by the casaviewer. Default "~/.casa".
- *logfile*               : log file path/name. Default "casa-yyyymmdd-hhmmss.log". Note that this default value is set using gmtime() from the time module on import of config.
- *nologfile*             : do not create a log file when True, default False. If *nologfile* is True, then any *logfile* value is ignored and there is no log file.
- *log2term*              : print log output to terminal when True (in addition to any logfile and CASA logger), default False.
- *nologger*              : do not start the CASA logger GUI when True, default False.
- *nogui*                 : avoid starting GUI tools when True, default False. If *nogui* is True then the CASA logger is not started even if *nologger* is False.
- *colors*                : the IPython prompt color scheme. Must be one of "Neutral", "NoColor", "Linux" or "LightBG", default "Neutral". If an invalid color is given a warning message is shown but CASA continues using the default color.
- *agg*                   : startup without a graphical backend if True, default False.
- *pipeline*              : attempt to load the pipeline modules and set other options appropriate for pipeline use if True, default False. When *pipeline* is True then *agg* will be assumed to be True even if *agg* is set to False here or on the command line.
- *iplog*                 : create and use an IPython log if True, default False.
- *iplogfile*             : IPython log file path/name, used only when iplog is True. Default "ipython-yyyymmdd-hhmmss.log". Note that this default value is set using gmtime() from the time module on import of config.
- *user_site*             : include the user's local site-packages in the python path if True. Normally these should be excluded to avoid potential conflicts with CASA modules. Default False.

**Note:** The auto update parameters are used during casatools initialization. 

**Note:** It is an error for *measures_auto_update* to be False when *data_auto_update* is True. In that case no auto updates will happen and CASA will continue after printing out an error message.

A typical config.py file might look something like this:

::

   datapath=[measurespath, "~/.casa/my_additional_data"]
   data_auto_update = False
   measures_auto_update = False
   log2term=True
   nologger=True


**Note** that in a monolithic CASA installation the casasiteconfig.py will typically set *measurespath* to a shared data location and set *data_auto_update* and *measures_auto_update* to False.
This example config.py might be appropriate for a shared *measurespath* location with an additional user-controlled data location added at the end of *datapath*.
Auto updates are turned off to prevent the user from accidentally updating that shared location (they are likely also False in casasiteconfig.py and setting 
that to False in the user config.py here is unnecessary). Auto updates require that the user own *measurespath*, providing additional protection against 
accidentally updating a shared data location.

**Note** that the default *logfile* and the default *iplogfile* use the time module to set the value to a string that depends on when 
the config file is evaluated. 

casasiteconfig.py
^^^^^^^^^^^^^^^^^
 
 .. data:: casasiteconfig.py

Monolithic CASA is distributed with a casasiteconfig.py. A casasiteconfig.py can also be placed anywhere in the PYTHON path (sys.path). When present,
this file is evaluated after the default configuration values are set and before any user's config.py is used. The casasiteconfig.py is ignored when
the *\-\-nositeconfig* command line option is used.

The casasiteconfig.py found in the monolithic CASA initially looks like this:

::

   # The default site config file. This may be placed at any location in the PYTHONPATH used by CASA

   # This file should be edited to set measurespath as appropriate

   # Set this to point to the location where the site maintained casarundata can be found
   # by default datapath will include measurespath

   measurespath = None

   # turn off all auto updates of data

   measures_auto_update = False
   data_auto_update = False


These settings are appropriate for site installations where the CASA data is maintained for all site users. The *measurespath*
value should be set to the location of the site data. Site data can be shared across multiple CASA installations. The site
administrators are responsible for installing the CASA data and keeping it up to date. Methods provided by casaconfig should be used to
populate that location (**update_all()** or **pull_data()**) and keep it up to date (**data_update()** or **measures_update()** or the *update-data* script
found in the CASA installation or the **\-\-update_all** casaconfig module command-line option.

Auto updates are turned off in casasiteconfig.py because the site data location should not be updated by individual users (auto updates
also require that the user own *meausurespath*, which is not typical for a site installation). 

Individual users who install monolithic CASA for their personal use may remove casasiteconfig.py from their installation. 
In that case, *measurespath* defaults to ~/.casa/data and the user would need to populate that location before using CASA. 
Auto updates are then on by default and each subsequent use of CASA would check for updates (once a day) and update the measures
and casarundata when new versions are found.

**Note** measurespath must be set to some valid location when CASA starts. For monolithic CASA, when measurespath is None it will exit
with a message that it needs to be set. It should be set in the casasiteconfig.py for monolithic casa by the site administrator or the user may set it in
their personal config.py, but it must be set somewhere.

   
startup.py
^^^^^^^^^^
 
 .. data:: startup.py

*This section only applies to the monolithic/tar-file CASA distribution*

The \'*startup.py*\' file found at the *startupfile* configuration value (defaults to *\~/.casa/startup.py*) is evaluated 
by the CASA shell just before the CASA prompt is presented to the user. This allows users to customize their CASA shell 
environment beyond the standard settings in \'*config.py*\', by importing packages, setting variables or modifying 
the python system path. The startup file is optional. It can be ignored by setting *startupfile* in their configuration file to 
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

casa command line
^^^^^^^^^^^^^^^^^
 
 .. data:: casa(-h, --help, --configfile, ---noconfig, --nositeconfig, --startupfile, --nostartupfile, --logfile, --log2term, --nologger, --nologfile, --nogui, --cachedir, --colors, --pipeline, --agg, --iplog, --datapath, --reference-testing, --no-auto-update, --user-site, -v, --version, -c)

With the full installation of CASA  (monolithic CASA), the python environment itself is included and started through <CASA_installation_Path>/bin/casa.
This <CASA_installation_path>/bin/casa executable can be provided the following options to change configuration values at run time:

::

   -h, --help               show this help message and exit
   --configfile CONFIGFILE  location of the user configuration file
   --noconfig               do not load user configuration file
   --nositeconfig           do not load site configuration file
   --startupfile STARTFILE  path to user's startup file
   --nostartupfile          do not use any startup file
   --logfile LOGFILE        path to log file
   --log2term               direct output to terminal
   --nologger               do not start CASA logger
   --nologfile              do not create a log file
   --nogui                  avoid starting GUI tools
   --cachedir CACHEDIR      location for internal working files
   --colors {Neutral,NoColor,Linux,LightBG} prompt color
   --pipeline               start CASA pipeline run
   --agg                    startup without graphical backend
   --iplog                  create ipython log
   --datapath DATAPATH      data path(s) [colon separated]
   --reference-testing      force *measurespath* to contain the casarundata when this version was produced, used for testing purposes
   --no-auto-update         turn off all auto updates
   --user-site              include user's local site-packages lib in path
   -v, --version            show CASA version
   -c ...                   python eval string or python script to execute


These options **take precedence over the configuration files.** 

The \-\-configfile option is used to provide an alternative path to the user's configuration file. When that
option is used the file at that location is used instead of the default user configuration file (~/.casa/config.py).
The \-\-noconfig option turns off all use of the user's configuration file. If \-\-configfile and \-\-noconfig file
are used at the same time, the user's configuration file is ignored and a warning message is printed.

The \-\-nostartupfile option is provided as a way to turn off loading of the startup file, That can also be
done by setting startupfile to a non-existant file or empty string in a configuration file. If \-\-startupfile
and \-\-nostartupfile are used at the same time no startup file is used and a warning message is printed.

The \-\-reference-testing option is provided to help testers ensure that a known casarundata is installed in 
*measurespath* before CASA starts. Use of this option turns off all auto updates.

The \-\-no-auto-update option turns off any automatic data updates even if *data_auto_update* or *measures_auto_update* 
are True.

casaconfig command line
^^^^^^^^^^^^^^^^^^^^^^^
 
 .. data:: casaconfig(-h, --help, --configfile, ---noconfig, --nositeconfig, --measurespath, --pull-data, --data-update, --measures-update, --update-all, --reference-testing, --current-data)

The casaconfig module may be used by itself with these options. The full set of config files are first used (except as omitted by the options) then the 
options are used and then python exits. 

For all of the update options the most recent version is assumed and the *force* argument is False. These are **NOT** auto updates so the auto update
rules do not apply. If the user has permission to update that data then that data will be updated if a new version is found.

The casaconfig module can be used to initially populate a measurespath location with data or to update it or to check on the status of a measurespath.
Note that unlike the auto update rules, measurespath need not already exist before it's used here. 

::

   python -m casaconfig .. options ...

::

   -h, --help                  show this help message and exit
   --configfile CONFIGFILE     location of the user configuration file
   --noconfig                  do not load user configuration file
   --nositeconfig              do not load site configuration file
   --measurespath MEASUREPATH  location of casarundata
   --pull-data                 invoke pull_data() to populate measurespath with the latest casarundata
   --data-update               invoke data_update() to update measurespath to the latest casarundata
   --measures-update           invoke measures_update() to update measurespath to the latest measures data
   --update-all                invoke update_all() to populate (update) measurespath with the latest casarundata and measures data.
   --reference-testing         set measurespath to contain the casarundata when this version was produced, used for testing purposes
   --current-data              print out a summary of the current casarundata and measures data installed in measurespath and then exit.
   --force                     force an update using the force=True option to update_all, data_update, and measures_update

For a monolithic CASA installation the python to use on the command line is the one that is packaged in the bin directory with
the casa script and is typically *python3*. For modular casa the python should be the one with the environment containing the 
installed casaconfig module.

The \-\-configfile option is used to provide an alternative path to the user's configuration file. When that
option is used the file at that location is used instead of the default user configuration file (~/.casa/config.py).

The \-\-noconfig option turns off all use of any user's configuration file. If --configfile and --noconfig file
are both used then the user's configuration file is ignored and a warning message is printed.

The \-\-nositeconfig option turns off all use of any site configuration file.

The \-\-measurespath option allows the user to specify the path to the data for use by the data related options.
This overrides the value of *measurespath* in the configuration files.

The data related options (\-\-pull-data,\-\-data-update, \-\-measures-update, and \-\-update-all) use *measurespath*
without explicitly setting the version string. The *force* parameter rmemains False as does the *auto_update_rules*
parameter. This means that if a new version exists and the user has read and write permissions in *measurespath* then
an update will happen as if those functions were used from a python session.

When the \-\-current-data option is used no updates happen even if those options are also used.

The \-\-reference-testing option can not be used with \-\-pull-data, \-\-data-update, \-\-measures-update, 
and \-\-update-all.

The \-\-force option can be used to force casaconfig to check for updates (and install any that are available)
when the normal once-a-day checking rules might have caused it to not update measurespath. 

**Note** that if *measurespath* does not exist then \-\-pull-data, \-\-update-all, and \-\-reference-testing 
will create it before populating it.
