casashell
====================

CASA shell environment for interactive Python-based analysis using CASA tasks.

.. toctree::
   :maxdepth: 3

   casashell/buildmytasks
   casashell/default
   casashell/doc
   casashell/execfile
   casashell/go
   casashell/inp
   casashell/saveinputs
   casashell/taskhelp
   casashell/toolhelp
   casashell/tget
   casashell/tput


.. rubric:: Running Tasks and Tools

Tools are functions linked to the Python interface which must be called by name with arguments. Tasks have higher-level
capabilities than tools. Tasks require input parameters which maybe be specified when you call the task as a function,
or be set as parameters in the interface. A task, like a tool, is a function under Python and may be written in Python,
C, or C++ (the CASA toolkit is made up of C++ functions).

There are two distinct ways to run tasks. You can either set the global CASA parameters relevant to the task and tell
the task to ``go()``, or you can call the task as a function with one or more arguments specified. These two invocation
methods differ in whether the global parameter values are used or not.

For example, ::

   default('plotms')
   vis='ngc5921.ms'
   xaxis='channel'
   yaxis='amp'
   datacolumn='data'
   go()

will execute **plotms** with the set values for the parameters. Instead of using the ``go()`` command to invoke the task,
you can also call the task with no arguments, e.g. ::

   default('plotms')
   vis='ngc5921.ms'
   xaxis='channel'
   yaxis='amp'
   ydatacolumn='data'
   plotms()

which will also use the global parameter values.

Second, one may call tasks and tools by name with parameters set on the same line. Parameters may be set either as explicit
``<parameter>=<value>`` arguments, or as a series of comma delimited \<value\>s in the correct order for that task or tool.
Note that missing parameters will use the default values for that task. For example, the following are equivalent: ::

   #Specify parameter names for each keyword input:
   plotms(vis='ngc5921.ms',xaxis='channel',yaxis='amp',datacolumn='data')

   #when specifying the parameter name, order doesn't matter, e.g.:
   plotms(xaxis='channel',vis='ngc5921.ms',datacolumn='data',yaxis='amp')

   #use parameter order for invoking tasks
   plotms('ngc5921.ms',1,1,0,0,0,'channel','data','amp','data')

This non-use of globals when calling as a function is so that robust scripts can be written. One need only cut-and-paste the
calls and need not worry about the state of the global variables or what has been run previously. It is also more like the
standard behavior of function calls in Python and other languages.

.. rubric:: Aborting Tasks

If you are running CASA tasks, you can usually use *CTRL-C* to abort execution of the task. If this does not work, try *CTRL-Z*
followed by a kill.

You may have to quit and restart CASA after an abort, as the internal state can get mixed up.

.. rubric:: Getting Return Values

Some tasks and tools return a record (usually a Python dictionary) to the interface. For example, the **imstat** task returns a
dictionary with the image statistics in it. To catch these return values into a Python variable, you MUST assign that variable
to the task call, e.g. ::

   xstat = imstat('ngc5921.clean.image')

or ::

   default('imstat')
   imagename = 'ngc5921.clean.image'
   xstat = imstat()

You can print or use the return value in Python for controlling scripts. For example, ::

   CASA <1>: xstat = imstat('ngc5921.clean.image')
   CASA <2>: xstat
   Out[2]:
   {'blc': array([0, 0, 0, 0]),
    'blcf': '15:24:08.404, +04.31.59.181, I, 1.41281e+09Hz',
    'flux': array([ 4.15292207]),
    'max': array([ 0.05240594]),
    'maxpos': array([134, 134, 0, 38]),
    'maxposf': '15:21:53.976, +05.05.29.998, I, 1.41374e+09Hz',
    'mean': array([ 1.62978083e-05]),
    'medabsdevmed': array([ 0.00127287]),
    'median': array([ -1.10467618e-05]),
    'min': array([-0.0105249]),
    'minpos': array([160, 1, 0, 30]),
    'minposf': '15:21:27.899, +04.32.14.923, I, 1.41354e+09Hz',
    'npts': array([ 3014656.]),
    'quartile': array([ 0.00254587]),
    'rms': array([ 0.00201818]),
    'sigma': array([ 0.00201811]),
    'sum': array([ 49.1322855]),
    'sumsq': array([ 12.27880404]),
    'trc': array([255, 255, 0, 45]),
    'trcf': '15:19:52.390, +05.35.44.246, I, 1.41391e+09Hz'}
   CASA <3>: myrms = xstat['rms'][0]
   CASA <4>: print 10.0*myrms
   0.0201817648485

If you do not catch the return variable, it will be lost ::

   imstat('ngc5921.clean.image')

or ::

   default('imstat')
   imagename = 'ngc5921.clean.image'
   imstat()

and spewed to terminal. Note that go() will trap and lose the return value, e.g. ::

   default('imstat')
   imagename = 'ngc5921.clean.image'
   go()

will not dump the return to the terminal either.


.. rubric:: Setting Parameters and Invoking Tasks

One can set parameters for tasks (but not for tools) by performing the assignment within the CASA shell and then
inspecting them using the ``inp()`` command: ::

   CASA <30>: default(bandpass)
   CASA <31>: vis = 'ngc5921.demo.ms'
   CASA <32>: caltable = 'ngc5921.demo.bcal'
   CASA <33>: field = '0'
   CASA <34>: refant = '15'
   CASA <35>: inp('bandpass')
   #bandpass :: Calculates a bandpass calibration solution
   vis = 'ngc5921.demo.ms' #Name of input visibility file
   caltable = 'ngc5921.demo.bcal' #Name of output gain calibration table
   field = '0' #Select field using field id(s) or field
   #name(s)
   spw = '' #Select spectral window/channels
   intent = '' #Select observing intent
   selectdata = True #Other data selection parameters
   timerange = '' #Select data based on time range
   uvrange = '' #Select data within uvrange (default units meters)
   antenna = '' #Select data based on antenna/baseline
   scan = '' #Scan number range
   observation = '' #Select by observation ID(s)
   msselect = '' #Optional complex data selection (ignore for now)
   solint = 'inf' #Solution interval in time[,freq]
   combine = 'scan' #Data axes which to combine for solve (obs, scan, spw, and/or field)
   refant = '15' #Reference antenna name(s)
   minblperant = 4 #Minimum baselines _per antenna_ required for solve
   minsnr = 3.0 #Reject solutions below this SNR (only applies for bandtype = B)
   solnorm = False #Normalize average solution amplitudes to 1.0
   bandtype = 'B' #Type of bandpass solution (B or BPOLY)
   fillgaps = 0 #Fill flagged solution channels by interpolation
   smodel = [] #Point source Stokes parameters for source model.
   append = False #Append solutions to the (existing) table
   docallib = False #Use callib or traditional cal apply parameters
   gaintable = [] #Gain calibration table(s) to apply on the fly
   gainfield = [] #Select a subset of calibrators from gaintable(s)
   interp = [] #Interpolation mode (in time) to use for each gaintable
   spwmap = [] #Spectral windows combinations to form for gaintables(s)
   parang = False #Apply parallactic angle correction

All task parameters have global scope within CASA: the parameter values are common
to all tasks and also at the CASA command line. This allows the convenience of not
changing parameters that are shared between tasks but does require care when
chaining together sequences of task invocations (to ensure proper values are
provided).

If you want to reset the input keywords for a single task, use the ``default()``
command. For example, to set the defaults for the **bandpass** task, type: ::

   CASA <30>: default('bandpass')

To inspect a single parameter value just type it at the command line. Continuing the above example: ::

   CASA <36>: combine
   Out[14]: 'scan'


.. rubric:: The scope of parameters in CASA

By default the scope of CASA parameters is global. However, if you call a task as a function with one
or more arguments specified, e.g. ``task(arg1=val1,...)``, then non-specified parameters will be
defaulted and no globals used. This makes scripting more robust. Tasks DO NOT change the value of globals.
All task parameters have global scope within CASA: the parameter values are common to all tasks and also
at the CASA command line. This allows the convenience of not changing parameters that are shared between
tasks but does require care when chaining together sequences of task invocations (to ensure proper values
are provided). Tasks DO NOT change the values of the global parameters, nor does the invocation of tasks
using the functional call with arguments change the globals.

This does mean that unless you do an explicit default of the task, previously set values may be unexpectedly
used if you do not inspect the **inp()** carefully. For example, good practice is:

::

   default('imhead')
   imagename = 'ngc5921.demo.cleanimg.image'
   mode = 'list'
   imhead()

If you supply the task call with arguments, then these will be used for the values of those parameters.
However, if some but not all arguments are supplied, then those parameters not given as arguments will
default and NOT use the current global values. Thus,

::

   imhead('ngc5921.demo.cleanimg.image',mode='list')


will reproduce the above.


For example, suppose we have been running CASA on a particular dataset, e.g.

::

   CASA <40>: inp clean
   ---------> inp('clean')
   #clean :: Deconvolve an image with selected algorithm
   vis = 'ngc5921.demo.src.split.ms.contsub' #name of input visibility file
   imagename = 'ngc5921.demo.cleanimg' #Pre-name of output images
   field = '0' #Field Name
   spw = '' #Spectral windows:channels: '' is all
   selectdata = False #Other data selection parameters
   mode = 'channel' #Type of selection (mfs, channel, velocity, frequency)
   nchan = 46 #Number of channels (planes) in output image
   start = 5 #first input channel to use
   width = 1 #Number of input channels to average
   interpolation = 'nearest' #Spectral interpolation (nearest, linear, cubic)
   niter = 6000 #Maximum number of iterations
   ...

and now we wish to switch to a different one. We can reset the parameter values using
``default()``:

::

   CASA <41>: default()
   ---------> default()

   CASA <42>: inp()
   ---------> inp()
   #clean :: Deconvolve an image with selected algorithm
   vis = '' #name of input visibility file
   imagename = '' #Pre-name of output images
   field = '' #Field Name
   spw = '' #Spectral windows:channels: '' is all
   selectdata = False #Other data selection parameters
   mode = 'mfs' #Type of selection (mfs, channel, velocity, frequency)
   niter = 500 #Maximum number of iterations
   ...

It is good practice to use ``default()`` before running a task if you are unsure what state the CASA global
variables are in.

.. warning:: You can only reset ALL of the parameters for a given task to their defaults.


.. rubric::  The .last file

Whenever you successfully execute a CASA task, a Python script file called ``<taskname>.last`` will be written
(or over-written) into the current working directory. For example, if you ran the ``listobs`` task as detailed
above, then ::

   CASA <14>: vis = 'ngc5921.ms'
   CASA <15>: verbose = True
   CASA <16>: listobs()
   CASA <17>: !more 'listobs.last'
   IPython system call: more listobs.last
   taskname = "listobs"
   vis = "ngc5921.ms"
   verbose = True
   listfile = ""
   #listobs(vis="ngc5921.ms",verbose=False,listfile="")

You can restore the parameter values from the save file using ::

   CASA <18>: tget("listobs")
   
or (since the current active task is ``listobs``) ::

   CASA <19>: tget

or ::

   CASA <19>: run listobs.last

Note that the .last file in generally not created until the task actually finished (successfully), so it is often best
to manually create a save file beforehand using the ``saveinputs`` command if you are running a critical task that you
strongly desire to have the inputs saved for.

