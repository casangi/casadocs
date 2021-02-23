inp
====

.. currentmodule:: casashell


.. function:: inp(taskname=None)

   Inspect the parameter values of the given task. If given a taskname, sets taskname as the current active (default) task.

   Parameters
      - **taskname** (*obj*, *string*, or *None*) - task object or task name. None will use current active (default) task.

   Description
      You can set the values for the parameters for tasks (but currently not for tools) by performing the
      assignment within the CASA shell and then inspecting them using the inp() command. This command can
      be invoked in any of three ways: via function call ``inp('<taskname>')`` or ``inp(<taskname>)``,
      without parentheses ``inp '<taskname>'`` or ``inp <taskname>``, or using the current active (default) task
      with inp(). For example, ::

         CASA <1>: inp('tclean')
         ...
         CASA <2>: inp 'tclean'
         ----------> inp('tclean')
         ...
         CASA <3>: inp(tclean)
         ...
         CASA <4>: inp tclean
         ----------> inp(tclean)
         ...
         CASA <5>: inp()
         ----------> inp()

      all do the same thing (the final example shows the parameters for the current active task, which is tclean
      here since the previous line set the current active task to tclean).

      When you invoke the task inputs via **inp()**, you see a list of the parameters, their current values,
      and a short description of what that parameters does. For example, starting from the default values, ::

         CASA <18>: inp('tclean')
         vis = '' # Name of input visibility file(s)
         selectdata = True # Enable data selection parameters
         field = '' # field(s) to select
         spw = '' # spw(s)/channels to select
         timerange = '' # Range of time to select from data
         uvrange = '' # Select data within uvrange
         antenna = '' # Select data based on antenna/baseline
         scan = '' # Scan number range
         observation = '' # Observation ID range
         intent = '' # Scan Intent(s)
         datacolumn = 'corrected' # Data column to image(data,corrected)
         imagename = '' # Pre-name of output images
         imsize = [] # Number of pixels
         cell = [] # Cell size
         phasecenter = '' # Phase center of the image
         stokes = 'I' # Stokes Planes to make
         projection = 'SIN' # Coordinate projection
         startmodel = '' # Name of starting model image
         specmode = 'mfs' # Spectral definition mode (mfs,cube,cubedata, cubesource)
         reffreq = '' # Reference frequency
         gridder = 'standard' # Gridding options (standard, wproject, widefield, mosaic, awproject)
         vptable = '' # Name of Voltage Pattern table
         pblimit = 0.2 # PB gain level at which to cut off normalizations
         deconvolver = 'hogbom' # Minor cycle algorithm (hogbom,clark,multiscale,mtmfs,mem,clarkstokes)
         restoration = True # Do restoration steps (or not)
         restoringbeam = [] # Restoring beam shape to use. Default is the PSF main lobe
         pbcor = False # Apply PB correction on the output restored image
         outlierfile = '' # Name of outlier-field image definitions
         weighting = 'natural' # Weighting scheme (natural,uniform,briggs, briggsabs[experimental])
         uvtaper = [] # uv-taper on outer baselines in uv-plane
         niter = 0 # Maximum number of iterations
         usemask = 'user' # Type of mask(s) for deconvolution: user, pb, or auto-multithresh
         mask = '' # Mask (a list of image name(s) or region file(s) or region string(s) )
         pbmask = 0.0 # primary beam mask
         fastnoise = True # True: use the faster (old) noise calculation. False: use the new improved noise calculations
         restart = True # True : Re-use existing images. False : Increment imagename
         savemodel = 'none' # Options to save model visibilities (none, virtual, modelcolumn)
         calcres = True # Calculate initial residual image
         calcpsf = True # Calculate PSF
         parallel = False # Run major cycles in parallel

      The Figure below shows how this will look to you on your terminal. Note that some parameters are in
      boldface with a gray background. This means that some values for this parameter will cause it to expand,
      revealing new sub-parameters to be set. Some default values cause the related sub-parameteers to be revealed.

      |image1|

      .. |image1| image:: ../../notebooks/media/tclean_inp_default.png

      CASA uses color and font to indicate different properties of parameters and their values:

      .. raw:: html

         <table><colgroup><col style="width: 20%" /><col style="width: 20%" /><col style="width: 20%" /><col style="width: 20%" /><col style="width: 20%" /></colgroup><thead><tr class="header"><th><h4 id="text-font">Text Font</h4></th><th><h4 id="text-color">Text Color</h4></th><th><h4 id="highlight">Highlight</h4></th><th><h4 id="indentation">Indentation</h4></th><th><h4 id="meaning">Meaning</h4></th></tr></thead><tbody><tr class="odd"><td><h4 id="parameters">Parameters:</h4></td><td> </td><td> </td><td> </td><td> </td></tr><tr class="even"><td>plain</td><td>black</td><td>none</td><td>none</td><td>standard parameter</td></tr><tr class="odd"><td>bold</td><td>black</td><td>grey</td><td>none</td><td>expandable parameter</td></tr><tr class="even"><td>plain</td><td>green</td><td>none</td><td>yes</td><td>sub-parameter</td></tr><tr class="odd"><td><h4 id="values">Values:</h4></td><td> </td><td> </td><td> </td><td> </td></tr><tr class="even"><td>plain</td><td>black</td><td>none</td><td>none</td><td>default value</td></tr><tr class="odd"><td>plain</td><td>blue</td><td>none</td><td>none</td><td>non-default value</td></tr><tr class="even"><td>plain</td><td>red</td><td>none</td><td>none</td><td>invalid value</td></tr></tbody></table>

      The Figure below shows what happens when you set some of the **tclean** parameters to non-default values.
      Some have opened up sub-parameters, which can now be seen and set. Some have closed sub-parameters because
      that non-default value has no related sub-parameters. The Figure thereafter shows what
      happens when you set a parameter to an invalid value. Its value now
      appears in red. Reasons for invalidation include incorrect type, an invalid menu choice, or a filename
      that does not exist. For example, since *vis* expects a filename, it will be invalidated (red) if it is
      set to a non-string value, or a string that is not the name of a file that can be found. The *deconvolver*
      value is invalid because it's not a supported choice (*'hogbom', 'clark', 'multiscale', 'mtmfs', 'mem', 'clarkstokes'*).

      |image2|

      .. |image2| image:: ../../notebooks/media/tclean_inp_set.png

      The **tclean** inputs after setting values away from their defaults (blue text). Note that some of the
      boldface ones have opened up new dependent sub-parameters (indented and green).

      |image3|

      .. |image3| image:: ../../notebooks/media/tclean_inp_invalid.png

      The **tclean** inputs where one parameter has been set to an invalid value. This is drawn in red to draw
      attention to the problem. This hapless user probably confused the *'hogbom'* clean algorithm with Harry Potter.

