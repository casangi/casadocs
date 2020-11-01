inp
====

.. currentmodule:: casashell


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

      .. |image1| image:: ../../notebooks/media/e0fa0682fce60b01cb671d3bead80a659d00eca1.png

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

      .. |image2| image:: ../../notebooks/media/4999580bbc7b35124cbad59dee1cec5c975bde1e.png

      The **clean** inputs after setting values away from their defaults (blue text). Note that some of the
      boldface ones have opened up new dependent sub-parameters (indented and green).

      |image3|

      .. |image3| image:: ../../notebooks/media/a1c7b7cef488ae5a8e53fa7c43fac4cab28b9170.png

      The **clean** inputs where one parameter has been set to an invalid value. This is drawn in red to draw
      attention to the problem. This hapless user probably confused the *'hogbom'* clean algorithm with Harry Potter.

