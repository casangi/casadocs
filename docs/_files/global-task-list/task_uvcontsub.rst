.. container::
   :name: viewlet-above-content-title

uvcontsub
=========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task description

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. container:: description

          

      .. container:: description

         **uvcontsub** is a task to perform continuum fitting and
         subtraction in the uv plane

      .. container:: description

          

      .. container:: description

         This task estimates the continuum emission by fitting
         polynomials to the real and imaginary parts of the spectral
         windows and channels selected by *fitspw*. This fit represents
         a model of the continuum in all channels. The fitted continuum
         spectrum is subtracted from all channels selected in *spw*, and
         the result (presumably only line emission) is stored in a new
         MS that is always called vis + ".contsub". If an MS with the
         output name already exists, it will be overwritten.

      .. container:: description

          

      .. container:: description

         **uvcontsub** will read from the CORRECTED_DATA column of *vis*
         if it is present, or DATA if it is not. Whichever column is
         read is presumed to have already been calibrated.

      .. container:: description

           

      .. container:: description

         .. container:: info-box

            .. container:: description

               **WARNING:** Strictly speaking, the **uvcontsub** model
               is only a good representation of the continuum at the
               phase center. Residuals may be visible for sources far
               away and one may try **imcontsub** in the image domain
               for improved results. 

      .. container:: description

         .. container:: info-box

            **WARNING**\ **:**\ *fitorders* > 1 are strongly discouraged
            because high order polynomials have more flexibility, may
            absorb line emission, and tend to go wild at the edges
            of *fitspw*, which is not what you
            want. default: *0* (constant)

      .. container:: description

         If *want_cont* =\ *True*, the continuum fit is placed in a
         second new MS with the name vis + '.cont', also overwritten if
         it already exists. 

      .. container:: description

         .. container:: info-box

            .. container:: description

               **INFO: ** because the continuum model is necessarily a
               smoothed fit, images made with it are liable to have
               their field of view reduced in some strange way. Images
               of the continuum should be made by simply excluding the
               line channels (and probably averaging the remaining ones)
               in **tclean**.

      .. container:: description

          

      .. container:: description

          

      .. rubric:: Parameter descriptions
         :name: title0

      .. rubric:: *vis*
         :name: vis

      Name of input MS. Output goes to vis + ".contsub" (will be
      overwritten if already exists)

      .. rubric:: *field*
         :name: field

      `Field
      selection <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__
      for continuum estimation and subtraction. The estimation and
      subtraction is done for each selected field separately in
      turn. default: *''* (all fields) (See `Data Selection in a
      MeasurementSet <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__)

      .. rubric:: *fitspw  *
         :name: fitspw

      Selection of spectral windows and channels to use in the fit for
      the continuum, using general `MS selection
      syntax <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__ for
      spectral windows, e.g. in spw:chan format (spw ids are required
      but *'*'* can be used) or as frequencies. See the note under
      *combine*. default: *fitspw='' * (all)

      .. container:: alert-box

         **WARNING:** The *fitspw* selection is based on the channel
         numbers in the uv-data of the input MS file, which are most
         likely different from the channel numbers in the image plane
         after running **tclean**. 

      .. rubric:: *excludechans (fitspw subparameter)*
         :name: excludechans-fitspw-subparameter

      if *True*, it will exclude the channels (or frequency range) that
      is specified in *fitspw *\ for the fit; this is useful to specify
      the line channels to exclude rather than the continuum channels to
      include in the fit. (default: *False*)

      .. rubric:: *combine*
         :name: combine

      Continuum solutions will break at scan, field, and spw boundaries
      according to *solint.* To allow solutions across these boundaries,
      *combine* can be set to '*spw*', '*scan*', or *'spw, scan'. 
      combine *\ must include *'spw'*  if spw contains spws that are not
      in *fitspw*!  default: *''*  which is that solutions will break at
      scan, field, and spw

      .. rubric:: *solint*
         :name: solint

      | Timescale for per-baseline fit (units optional) options are time
        ranges, e.g. '*10s*', or '*inf*' per scan, or '*int*' per
        integration. default (recommended): '*int*', i.e. no time
        averaging, do a fit for each integration and let the noisy fits
        average out in the image.continuum fit. If *solint* is longer
        than '*int*', the continuum estimate can be
      | corrupted by time smearing.

      .. rubric:: *fitorder*
         :name: fitorder

      | Polynomial order for the fits of the continuum w.r.t. frequency.
        *fitorders* > 1 are strongly discouraged because high order
        polynomials have more flexibility, may
      | absorb line emission, and tend to go wild at the edges of
        *fitspw*, which is not what you want. default: *0* (constant)

      .. rubric:: *spw*
         :name: spw

      Optional per spectral window selection of channels to include in
      the output. See the note under *combine*. The sub-MS output
      spectral windows will be renumbered to start from 0, as in
      **split**. default: *''* (all spws) (See `Data Selection in a
      MeasurementSet <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__)

      .. rubric:: *want_cont*
         :name: want_cont

      Create vis + '.cont' to hold the continuum estimate. 

       

.. container:: section
   :name: viewlet-below-content-body


.. toctree::
   :hidden:
   :maxdepth: 3

   task_uvcontsub/about
   task_uvcontsub/parameters
   task_uvcontsub/changelog
   task_uvcontsub/examples
   task_uvcontsub/developer