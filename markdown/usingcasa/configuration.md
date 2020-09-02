

# Configuration 

CASA accepts a variety of options through two mechanisms: configuration files and command line arguments.  Configuration files are typically stored in a \~/.casa folder while command line options (only applicable to the full installation) are specified after the casa command at startup.

 

## Configuration Files

Each modular CASA 6 package as well as the full installation reads a single **config.py** configuration file. This file should be placed in the user root .casa folder (**\~/.casa**) prior to starting the casa installation or importing the packages in to a standard python environment for the first time.

The configuration file currently supports four parameters:

<div class="alert alert-info">
datapath              : list of paths where CASA should search for runtime data

logfile               : log file path/name

telemetry_enabled     : allow anonymous usage reporting

crashreporter_enabled :* *allow anonymous crash reporting
</div>

The configuration file is a standard python script, so any valid python syntax and libraries can be used.  A typical config.py file might look something like this:

```
$ cat ~/.casa/config.py

import time

[datapath=["/home/casa/data/casa-data", "/home/casa/data/casa-data-req"]]{
logfile='casalog-%s.log' % time.strftime("%Y%m%d-%H",time.localtime())
telemetry_enabled = True
crashreporter_enabled = True
```

At runtime the datapath(s) are expanded through a resolve(\...) function to find the needed data tables. For example

```
>>> casatools.ctsys.resolve('geodetic/IERSpredict')

'/home/casa/data/casa-data/geodetic/IERSpredict'
```

<div class="alert alert-warning">
**WARNING**: CASA 5 does not use config.py. Instead ~/.casa/prelude.py is evaluated during startup before anything else and ~/.casa/init.py is evaluated just before the CASA prompt is presented. The configuration options are different and more limited 
</div>

 

## Command Line Arguments (full installation only)

With the full installation of CASA from a tar file, the python environment itself is included and started through ./bin/casa.  This ./bin/casa executable can be provided the following options to change configuration values at run time: 

<div class="alert alert-info">
[  -h, --help            show this help message and exit
  --logfile LOGFILE     path to log file
  --log2term            direct output to terminal
  --nologger            do not start CASA logger
  --nologfile           do not create a log file
  --nogui               avoid starting GUI tools
  --rcdir RCDIR         location for startup files
  --norc                do not load user config.py
  --colors {Neutral,NoColor,Linux,LightBG}
                        prompt color
  --pipeline            start CASA pipeline run
  --agg                 startup without graphical backend
  --iplog               create ipython log
  --notelemetry         disable telemetry collection
  --nocrashreport       do not submit an online report when CASA crashes
  --datapath DATAPATH   data path(s) [colon separated]
  --user-site           include user's local site-packages lib in path
]{  -c ...                python eval string or python script to execute

</div>

These options **take precedence over the configuration files.**

Some options imply or take precedence over other options:

-   \--nologfile takes precedence over \--logfile
-   \--nogui implies \--nologger
-   \--pipeline implies \--agg

<div class="alert alert-warning">
**WARNING**: the command line arguments listed above apply to CASA 6. CASA 5 (including CASA 5.7) do not include --notelemetry and --norc.
</div>

 

## Starting CASA

CASA packages installed through pip may be imported in to the standard Python environment on the host machine. For example:

```
(casa6) $ python

Python 3.6.9 (default, Nov 7 2019, 10:44:02) 
[[GCC 8.3.0] on linux]{
Type "help", "copyright", "credits" or "license" for more information.
>>> import casatasks
>>> help(casatasks)
```

The \~/.casa/**config.py** file will be read and processed when the casatasks package is imported.

The full installation of CASA includes a python environment and is executed like an application.  Any desired command line arguments may be included.  For example:

```
$ ./casa6/bin/casa --logfile MyTestRun.txt --nogui
```

The \~/.casa/**config.py** file will be read and processed as the casa application executes, with the supplied command line arguments (logfile and nogui) added on top.

Users may wish to set shortcuts, links, aliases or add bin/casa to their envrionment PATH.  See the documentation for your operating system. 

