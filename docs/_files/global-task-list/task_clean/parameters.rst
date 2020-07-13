Parameters
==========

.. container:: documentDescription description

   task clean parameters

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               vis : string stringArray

            Name of input visibility file

Example

.. container:: param

   .. container:: parameters2

      imagename : string stringArray

   Pre-name of output images

Example

.. container:: param

   .. container:: parameters2

      outlierfile : string

   Text file with image names, sizes, centers for outliers

Example

.. container:: param

   .. container:: parameters2

      field : string stringArray

   Field Name or id

Example

.. container:: param

   .. container:: parameters2

      spw : string stringArray

   Spectral windows e.g. \\'0~3\', \\'\' is all

Example

.. container:: param

   .. container:: parameters2

      selectdata : bool = True

   Other data selection parameters

Example

.. container:: param

   .. container:: parameters2

      timerange : string stringArray

   Range of time to select from data

Example

.. container:: param

   .. container:: parameters2

      uvrange : string stringArray

   Select data within uvrange

Example

.. container:: param

   .. container:: parameters2

      antenna : string stringArray

   Select data based on antenna/baseline

Example

.. container:: param

   .. container:: parameters2

      scan : string stringArray

   Scan number range

Example

.. container:: param

   .. container:: parameters2

      observation : string int

   Observation ID range

Example

.. container:: param

   .. container:: parameters2

      intent : string stringArray

   Scan Intent(s)

Example

.. container:: param

   .. container:: parameters2

      mode : string = mfs

   Spectral gridding type (mfs, channel, velocity, frequency)

Allowed Value(s)

mfs channel velocity frequency

Example

.. container:: param

   .. container:: parameters2

      resmooth : bool = False

   Re-restore the cube image to a common beam when True

Example

.. container:: param

   .. container:: parameters2

      gridmode : string

   Gridding kernel for FFT-based transforms, default=\'\' None

Allowed Value(s)

widefield aprojection advancedaprojection

Example

.. container:: param

   .. container:: parameters2

      wprojplanes : int = -1

   Number of w-projection planes for convolution; -1 => automatic
   determination

Example

.. container:: param

   .. container:: parameters2

      facets : int = 1

   Number of facets along each axis (main image only)

Example

.. container:: param

   .. container:: parameters2

      cfcache : string = cfcache.dir

   Convolution function cache directory

Example

.. container:: param

   .. container:: parameters2

      rotpainc : double = 5.0

   Parallactic angle increment (degrees) for OTF A-term rotation

Example

.. container:: param

   .. container:: parameters2

      painc : double = 360.0

   Parallactic angle increment (degrees) for computing A-term

Example

.. container:: param

   .. container:: parameters2

      aterm : bool = True

   Switch-on the A-Term?

Example

.. container:: param

   .. container:: parameters2

      psterm : bool = False

   Switch-on the PS-Term?

Example

.. container:: param

   .. container:: parameters2

      mterm : bool = True

   Switch-on the M-Term?

Example

.. container:: param

   .. container:: parameters2

      wbawp : bool = False

   Trigger the wide-band A-Projection algorithm?

Example

.. container:: param

   .. container:: parameters2

      conjbeams : bool = True

   Use frequency conjugate beams in WB A-Projection algorithm?

Example

.. container:: param

   .. container:: parameters2

      epjtable : string

   Table of EP-Jones parameters

Example

.. container:: param

   .. container:: parameters2

      interpolation : string = linear

   Spectral interpolation (nearest, linear, cubic).

Allowed Value(s)

nearest linear cubic spline

Example

.. container:: param

   .. container:: parameters2

      niter : int = 500

   Maximum number of iterations

Example

.. container:: param

   .. container:: parameters2

      gain : double = 0.1

   Loop gain for cleaning

Example

.. container:: param

   .. container:: parameters2

      threshold : double = 0.0

   Flux level to stop cleaning, must include units: \\'1.0mJy\'

Example

.. container:: param

   .. container:: parameters2

      psfmode : string = clark

   Method of PSF calculation to use during minor cycles

Allowed Value(s)

clark clarkstokes hogbom

Example

.. container:: param

   .. container:: parameters2

      imagermode : string = csclean

   Options: \\'csclean\' or \\'mosaic\', \\'\', uses psfmode

Allowed Value(s)

csclean mosaic

Example

.. container:: param

   .. container:: parameters2

      ftmachine : string = mosaic

   Gridding method for the image

Allowed Value(s)

ft wproject mosaic sd both awproject

Example

.. container:: param

   .. container:: parameters2

      mosweight : bool = False

   Individually weight the fields of the mosaic

Example

.. container:: param

   .. container:: parameters2

      scaletype : string = SAULT

   Controls scaling of pixels in the image plane. default=\'SAULT\';
   example: scaletype=\'PBCOR\' Options: \\'PBCOR\',\'SAULT\'

Allowed Value(s)

SAULT PBCOR

Example

.. container:: param

   .. container:: parameters2

      multiscale : intArray = 0

   Deconvolution scales (pixels); [] = standard clean

Example

.. container:: param

   .. container:: parameters2

      negcomponent : int = -1

   Stop cleaning if the largest scale finds this number of neg
   components

Example

.. container:: param

   .. container:: parameters2

      smallscalebias : double = 0.6

   a bias to give more weight toward smaller scales

Example

.. container:: param

   .. container:: parameters2

      interactive : bool = False

   Use interactive clean (with GUI viewer)

Example

.. container:: param

   .. container:: parameters2

      mask : undefined

   Cleanbox(es), mask image(s), region(s), or a level

Example

.. container:: param

   .. container:: parameters2

      nchan : int = -1

   Number of channels (planes) in output image; -1 = all

Example

.. container:: param

   .. container:: parameters2

      start : undefined = 0

   start of output spectral dimension

Example

.. container:: param

   .. container:: parameters2

      width : undefined = 1

   width of output spectral channels

Example

.. container:: param

   .. container:: parameters2

      outframe : string

   default spectral frame of output image

Allowed Value(s)

lsrk lsrd bary geo topo galacto lgroup cmb

Example

.. container:: param

   .. container:: parameters2

      veltype : string = radio

   velocity definition (radio, optical, true)

Allowed Value(s)

radio optical true relativistic

Example

.. container:: param

   .. container:: parameters2

      imsize : intArray = 256256

   x and y image size in pixels. Single value: same for both

Example

.. container:: param

   .. container:: parameters2

      cell : doubleArray = 1.0

   x and y cell size(s). Default unit arcsec.

Example

.. container:: param

   .. container:: parameters2

      phasecenter : undefined

   Image center: direction or field index

Example

.. container:: param

   .. container:: parameters2

      restfreq : string

   Rest frequency to assign to image (see help)

Example

.. container:: param

   .. container:: parameters2

      stokes : string = I

   Stokes params to image (eg I,IV,IQ,IQUV)

Allowed Value(s)

I Q U V IV IQ QU UV IQU IUV IQUV RR LL RRLL XX YY XXYY

Example

.. container:: param

   .. container:: parameters2

      weighting : string = natural

   Weighting of uv (natural, uniform, briggs, ...)

Allowed Value(s)

natural uniform briggs briggsabs radial superuniform

Example

.. container:: param

   .. container:: parameters2

      robust : double = 0.0

   Briggs robustness parameter

Allowed Value(s)

-2.0 2.0

Example

.. container:: param

   .. container:: parameters2

      uvtaper : bool = False

   Apply additional uv tapering of visibilities

Example

.. container:: param

   .. container:: parameters2

      outertaper : stringArray =

   uv-taper on outer baselines in uv-plane

Example

.. container:: param

   .. container:: parameters2

      innertaper : stringArray = 1.0

   uv-taper in center of uv-plane (not implemented)

Example

.. container:: param

   .. container:: parameters2

      modelimage : undefined

   Name of model image(s) to initialize cleaning

Example

.. container:: param

   .. container:: parameters2

      restoringbeam : stringArray

   Output Gaussian restoring beam for CLEAN image

Example

.. container:: param

   .. container:: parameters2

      pbcor : bool = False

   Output primary beam-corrected image

Example

.. container:: param

   .. container:: parameters2

      minpb : double = 0.2

   Minimum PB level to use

Example

.. container:: param

   .. container:: parameters2

      usescratch : bool = False

   True if to save model visibilities in MODEL_DATA column

Example

.. container:: param

   .. container:: parameters2

      noise : undefined = 1.0Jy

   noise parameter for briggs abs mode weighting

Example

.. container:: param

   .. container:: parameters2

      npixels : int = 0

   number of pixels for superuniform or briggs weighting

Example

.. container:: param

   .. container:: parameters2

      npercycle : int = 100

   Clean iterations before interactive prompt (can be changed)

Example

.. container:: param

   .. container:: parameters2

      cyclefactor : double = 1.5

   Controls how often major cycles are done. (e.g. 5 for frequently)

Example

.. container:: param

   .. container:: parameters2

      cyclespeedup : int = -1

   Cycle threshold doubles in this number of iterations

Example

.. container:: param

   .. container:: parameters2

      nterms : int = 1

   Number of Taylor coefficients to model the sky frequency dependence

Example

.. container:: param

   .. container:: parameters2

      reffreq : string

   Reference frequency (nterms > 1),\'\' uses central data-frequency

Example

.. container:: param

   .. container:: parameters2

      chaniter : bool = False

   Clean each channel to completion (True), or all channels each cycle
   (False)

Example

.. container:: param

   .. container:: parameters2

      flatnoise : bool = True

   Controls whether searching for clean components is done in a constant
   noise residual image (True) or in an optimal signal-to-noise residual
   image (False)

Example

.. container:: param

   .. container:: parameters2

      allowchunk : bool = False

   Divide large image cubes into channel chunks for deconvolution

Example

.. container:: section
   :name: viewlet-below-content-body
