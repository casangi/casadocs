casashell
====================

CASA shell environment for interactive Python-based analysis

Tasks require input parameters which maybe be specified when you call the task as a function, or be set as parameters
in the interface. A task is a function under Python and may be written in Python, C, or C++ (the CASA toolkit is made
up of C++ functions).

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
   datacolumn='data'
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

   CASA <18>: execfile('listobs.last')

or ::

   CASA <19>: run listobs.last

Note that the .last file in generally not created until the task actually finished (successfully), so it is often best
to manually create a save file beforehand using the ``saveinputs`` command if you are running a critical task that you
strongly desire to have the inputs saved for.


.. currentmodule:: casashell

.. autosummary::

   ~taskhelp
   ~default


.. function:: casashell.taskhelp()

   Prints a one line description of all available tasks

.. function:: casashell.default(taskname)

   Set the current default task for inp and go commands amd reset task parameter values

   Parameters
      - **taskname** (*string*) - name of task

   Description
      Each task has a special set of default parameters defined for its parameters. You can
      use the **default()** command to reset the parameters for a specified task (or the
      current task as defined by the taskname variable) to their default.

      The ``default()`` command resets the values of the task parameters to a set
      of "defaults" as specified in the task code. Some defaults are blank strings '' or empty
      lists [], others are specific numerical values, strings, or lists. It is important to
      understand that just setting a string parameter to an empty string '' is not setting it
      to its default! Some parameters do not have a blank as an allowed value. See the help for
      a particular task to find out its default. If '' is the default or an allowed value, it
      will say so explicitly.


.. function:: saveinputs(taskname=None, filename=None)

   Save current task parameters to file

   Parameters
      - **taskname** (*obj* or *None*) - task object, None will use current default
      - **filename** (*string* or *None*) - output file name, None will use current default

   Description
      The ``saveinputs`` command will save the current values of a given task parameters to a
      Python (plain ascii) file. It can take up to two arguments, e.g. ::

         saveinputs(taskname, outfile)

      The first is the usual taskname parameter. The second is the name for the output Python file.
      If there is no second argument, for example, ::

         saveinputs('clean')

      a file with name \<taskname\>.saved (in this case 'clean.saved' will be created or overwritten
      if extant. If invoked with no arguments, e.g. ::

         saveinputs

      it will use the current values of the taskname variable (as set using ``inp <taskname>`` or
      ``default <taskname>``). You can also use the taskname global parameter explicitly, ::

         saveinputs(taskname, taskname+'_1.save')

      For example, starting from default values ::

         CASA <1>: default('listobs')
         CASA <2>: vis='ngc5921.demo.ms'
         CASA <3>: saveinputs
         CASA <4>: !more 'listobs.saved'
         taskname = "listobs"
         vis = "ngc5921.demo.ms"
         selectdata = True
         spw = ""
         field = ""
         antenna = ""
         uvrange = ""
         timerange = ""
         correlation = ""
         scan = ""
         intent = ""
         feed = ""
         array = ""
         observation = ""
         verbose = True
         listfile = ""
         #listobs(vis="ngc5921.demo.ms",selectdata=True,spw="",field="",
         antenna="",uvrange="",timerange="",correlation="",scan="",intent="",
         feed="",array="",observation="",verbose=True,listfile="")

      An example save to a custom named file: ::

         saveinputs('listobs','ngc5921_listobs.par')



.. function:: tput(taskname=None)

   Save the current parameter values of a task to its ``<taskname>.last`` file

   Parameters
      - **taskname** (*obj* or *None*) - task object, None will use current default

   Description
      This is a shorthand to ``saveinputs`` and is a counterpart to ``tget``. Typing
      ``tput`` without a taskname will save the values of the inputs for the current
      task as given in the current value of the taskname parameter.

      Adding a task name, e.g. ``tput <taskname>`` will save the values for the specified task.
      For example, ::

         default('gaincal') #set current task to gaincal and default
         tget #read saved inputs from gaincal.last (or gaincal.saved)
         inp() #see these inputs!
         vis = 'new.ms' #change the vis parameter
         tput #save back to the gaincal.last file for later use



.. function:: tget(taskname=None)

   Recover saved values of the inputs to a task

   Parameters
      - **taskname** (*obj* or *None*) - task object, None will use current default

   Description
      This is a convenient alternative to using the Python execfile command. Typing ``tget`` without a
      taskname will recover the saved values of the inputs for the current task as given in the current
      value of the taskname parameter.

      Adding a task name, e.g. ``tget <taskname>`` will recover values for the specified task. This is
      done by searching for

      1. a ``<taskname>.last`` file
      2. a ``<taskname>.saved`` file

      and then executing the Python in these files. For example, ::

         default('gaincal') #set current task to gaincal and default
         tget #read saved inputs from gaincal.last (or gaincal.saved)
         inp() #see these inputs!
         tget bandpass #now get from bandpass.last (or bandpass.saved)
         inp() #task is now bandpass, with recovered inputs



.. function:: execfile(filename)

   Execute file

   Parameters
      - **filename** (*string*) - name of file to execute

   Description
      This can be used to restore saved task parameters


.. function:: inp(taskname=None)

   Inspect the parameter values of the given task

   Parameters
      - **taskname** (*string* or *None*) - name of task, None will use current default

   Description
      You can set the values for the parameters for tasks (but currently not for tools) by performing the
      assignment within the CASA shell and then inspecting them using the inp() command. This command can
      be invoked in any of three ways: via function call ``inp('<taskname>')`` or ``inp(<taskname>)``,
      without parentheses ``inp '<taskname>'`` or ``inp <taskname>``, or using the current taskname variable
      setting with inp(). For example, ::

         CASA <1>: inp('clean')
         ...
         CASA <2>: inp 'clean'
         ----------> inp('clean')
         ...
         CASA <3>: inp(clean)
         ...
         CASA <4>: inp clean
         ----------> inp(clean)
         ...
         CASA <5>: taskname = 'clean'
         CASA <6>: inp()
         ----------> inp()

      all do the same thing.

      When you invoke the task inputs via **inp()**, you see a list of the parameters, their current values,
      and a short description of what that parameters does. For example, starting from the default values, ::

         CASA <18>: inp('clean')
         #clean :: Deconvolve an image with selected algorithm
         vis = '' #name of input visibility file
         imagename = '' #Pre-name of output images
         field = '' #Field Name
         spw = '' #Spectral windows:channels: '' is all
         selectdata = False #Other data selection parameters
         mode = 'mfs' #Type of selection (mfs, channel, velocity, frequency)
         niter = 500 #Maximum number of iterations
         gain = 0.1 #Loop gain for cleaning
         threshold = '0.0mJy' #Flux level to stop cleaning. Must include units
         psfmode = 'clark' #method of PSF calculation to use during minor cycles
         imagermode = '' #Use csclean or mosaic. If '', use psfmode
         multiscale = [] #multi-scale deconvolution scales (pixels)
         interactive = False #use interactive clean (with GUI viewer)
         mask = [] #cleanbox(es), mask image(s), and/or region(s)
         imsize = [256, 256] #x and y image size in pixels
         cell = ['1.0arcsec', '1.0arcsec'] #x and y cell size. default unit arcsec
         phasecenter = '' #Image phase center: position or field index
         restfreq = '' #rest frequency to assign to image (see help)
         stokes = 'I' #Stokes params to image (eg I,IV, QU,IQUV)
         weighting = 'natural' #Weighting of uv (natural, uniform, briggs, ...)
         uvtaper = False #Apply additional uv tapering of visibilities.
         modelimage = '' #Name of model image(s) to initialize cleaning
         restoringbeam = [''] #Output Gaussian restoring beam for CLEAN image
         pbcor = False #Output primary beam-corrected image
         minpb = 0.1 #Minimum PB level to use

      The Figure below shows how this will look to you on your terminal. Note that some parameters are in
      boldface with a gray background. This means that some values for this parameter will cause it to expand,
      revealing new sub-parameters to be set.

      |image1|

      .. |image1| image:: ../notebooks/media/e0fa0682fce60b01cb671d3bead80a659d00eca1.png

      CASA uses color and font to indicate different properties of parameters and their values:

      .. raw:: html

         <table><colgroup><col style="width: 20%" /><col style="width: 20%" /><col style="width: 20%" /><col style="width: 20%" /><col style="width: 20%" /></colgroup><thead><tr class="header"><th><h4 id="text-font">Text Font</h4></th><th><h4 id="text-color">Text Color</h4></th><th><h4 id="highlight">Highlight</h4></th><th><h4 id="indentation">Indentation</h4></th><th><h4 id="meaning">Meaning</h4></th></tr></thead><tbody><tr class="odd"><td><h4 id="parameters">Parameters:</h4></td><td> </td><td> </td><td> </td><td> </td></tr><tr class="even"><td>plain</td><td>black</td><td>none</td><td>none</td><td>standard parameter</td></tr><tr class="odd"><td>bold</td><td>black</td><td>grey</td><td>none</td><td>expandable parameter</td></tr><tr class="even"><td>plain</td><td>green</td><td>none</td><td>yes</td><td>sub-parameter</td></tr><tr class="odd"><td><h4 id="values">Values:</h4></td><td> </td><td> </td><td> </td><td> </td></tr><tr class="even"><td>plain</td><td>black</td><td>none</td><td>none</td><td>default value</td></tr><tr class="odd"><td>plain</td><td>blue</td><td>none</td><td>none</td><td>non-default value</td></tr><tr class="even"><td>plain</td><td>red</td><td>none</td><td>none</td><td>invalid value</td></tr></tbody></table>

      The Figure below shows what happens when you set some of the **clean** parameters to non-default values.
      Some have opened up sub-parameters, which can now be seen and set. The Figure thereafter shows what
      happens when you set a parameter, in this case *vis* and *mode*, to an invalid value. Its value now
      appears in red. Reasons for invalidation include incorrect type, an invalid menu choice, or a filename
      that does not exist. For example, since *vis* expects a filename, it will be invalidated (red) if it is
      set to a non-string value, or a string that is not the name of a file that can be found. The *mode='happy'*
      is invalid because it's not a supported choice (*'mfs', 'channel', 'velocity', or 'frequency'*).

      |image2|

      .. |image2| image:: ../notebooks/media/4999580bbc7b35124cbad59dee1cec5c975bde1e.png

      The **clean** inputs after setting values away from their defaults (blue text). Note that some of the
      boldface ones have opened up new dependent sub-parameters (indented and green).

      |image3|

      .. |image3| image:: ../notebooks/media/a1c7b7cef488ae5a8e53fa7c43fac4cab28b9170.png

      The **clean** inputs where one parameter has been set to an invalid value. This is drawn in red to draw
      attention to the problem. This hapless user probably confused the *'hogbom'* clean algorithm with Harry Potter.


.. function:: go(taskname=None)

   Execute given task using parameters from the workspace

   If the task is successfully executed, then a ``<taskname>.last`` file
   is created in the working directory containing the parameter values

   Parameters
      - **taskname** (*string* or *None*) - name of task, None will use current default

   Description
      You can execute a task using the ``go()`` command, either explicitly ::

         CASA <44>: go listobs
         ---------> go(listobs)
         Executing: listobs()
         ...

      or implicitly if taskname is defined (e.g. by previous use of ``default()`` or ``inp()`` ) ::

         CASA <45>: taskname = 'clean'
         CASA <46>: go()
         ---------> go()
         Executing: clean()
         ...

      You can also execute a task simply by typing the taskname. ::

         CASA <46>: clean
         ---------> clean()
         Executing: clean()
         ...

      The ``go()`` command can also be used to launch a different task without changing the current
      taskname, without disrupting the ``inp()`` process on the current task you are working on.
      For example ::

         default 'gaincal' #set current task to gaincal and default
         vis = 'n5921.ms' #set the working ms
         ... #set some more parameters
         go listobs #launch listobs w/o changing current task
         inp() #see the inputs for gaincal (not listobs!)

      **ALERT:** Doing ``go listobs(vis='foo.ms')`` will currently change the taskname, and will change *vis*,
      which might not be what is desired.
