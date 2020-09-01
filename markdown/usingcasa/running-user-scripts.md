

# Running User Scripts 

#### CASA 6: modular version

The modular version of CASA behaves like a standard Python package and user scripts should include the relevant modules as they would any other python module (i.e. numpy).  Executing external user scripts with modular CASA is just like any other python application.  Note we recommend running in a Python venv, see the [installation instructions](https://casa.nrao.edu/casadocs-devel/stable/usingcasa/obtaining-and-installing) for more information.

```
$ (casa6) python myscript.py param1 param2
```

#### CASA 6: all-inclusive version 

Since the full CASA installation from a tar file includes its own python environment that is (typically) not called directly, alternative methods of feeding in user scripts are necessary.  There are three main standard Python ways of executing external user scripts in the full installation of CASA:

1.  -c startup parameter (see configuration instructions)
2.  exec(open(\"./filename\").read()) within the CASA Python environment
3.  add your script to startup.py in the \~/.casa directory

In addition, an *\"execfile\"* python shortcut has been added to the full installation of CASA 6 for backwards compatibility with ALMA scriptForPI.py restore scripts. This allows running scripts with the following command:

4. execfile \'filename.py\' within the CASA Python environment

The *execfile* command in CASA 6 has been tested and found to work in the same way as in (Python 2 based) CASA 5 with the exception that the treatment of global variables has changed in Python 3. For *execfile* calls within a script which itself is run via *execfile*, it is necessary to add *globals()* as the second argument to those *execfile* calls in order for the nested script to know about the global variables of the calling script. For example, within a script *\'mainscript.py\'*, calls to another script *\'myscript.py\'* should be written as follows: *execfile(\'myscript.py\', globals())* . 

 

# Startup.py

**This section only applies to the monolithic/tar-file CASA distribution, and it only applies to CASA 6.**

For CASA 5, use *\~/.casa/init.py* instead. *startup.py* should be Python 3 compliant whereas *init.py* is assumed to be Python 2.7.

The \'*startup.py*\' file found in *\$HOME/.casa* (i.e. *\~/.casa/startup.py*) is evaluated by the CASA shell just before the CASA prompt is presented to the user. This allows users to customize their CASA shell environment beyond the standard settings in [config.py](https://casa.nrao.edu/casadocs-devel/stable/usingcasa/configuration), by importing packages, setting variables or modifying the python system path. 

One case where this is useful is for configuring CASA for ALMA data reduction. A package called \'analysisUtils\' is often used as part of ALMA analysis. It is typically imported and instantiated in startup.py:

```
> <div>
>
> $ cat ~/.casa/startup.py
>
> </div>
>
> <div>
>
> import sys, os
>
> </div>
>
> <div>
>
> sys.path.append("/home/casa/contrib/AIV/science/analysis_scripts/")
>
> </div>
>
> <div>
>
> import analysisUtils as aU
>
> </div>
>
> <div>
>
> es=aU.stuffForScienceDataReduction()
>
> </div>
```

In this example, the standard python modules *os* and *sys* are made available in the CASA shell. The path where the *analysisUtils* module can be found is added to the Python system path, and finally the package is imported and an object is created. These modules and objects will then be available for the user within the CASA shell environment.

