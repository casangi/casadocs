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

The defaults are shown below. **Note** that the default *logfile* uses the time module to set the value to a string that depends on when 
the config file is evaluated. **Note** that in the monolithic casa case, *datapath* and *measurespath* will default to the data directory 
in the casaconfig package (returned by *get_data_dir()*).

.. include:: ../config_defaults_static.py
   :literal:
