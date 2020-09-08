#
# stub function definition file for docstring parsing
#

def uvcontsub(vis, field='', fitspw='', excludechans=False, combine='', solint='int', fitorder=0, spw='', want_cont=False):
    r"""
Continuum fitting and subtraction in the uv plane

Parameters
   - vis_ (string) - Name of input MS.  Output goes to vis + ".contsub" (will be overwritten if already exists)
   - field_ ({string, stringArray, int, intArray}='') - Select field(s) using id(s) or name(s)
   - fitspw_ (string='') - Spectral window:channel selection for fitting the continuum
   - combine_ (string='') - Data axes to combine for the continuum estimation (none, or spw and/or scan)
   - solint_ (variant='int') - Continuum fit timescale (int recommended!)
   - fitorder_ (int=0) - Polynomial order for the fits
   - spw_ (string='') - Spectral window selection for output
   - want_cont_ (bool=False) - Create vis + ".cont" to hold the continuum estimate.


Description


      **uvcontsub** is a task to perform continuum fitting and
      subtraction in the uv plane


      This task estimates the continuum emission by fitting
      polynomials to the real and imaginary parts of the spectral
      windows and channels selected by *fitspw*. This fit represents
      a model of the continuum in all channels.The fitted continuum
      spectrum is subtracted from all channels selected in *spw*, and
      the result (presumably only line emission) is stored in a new
      MS that is always called vis + ".contsub". If an MS with the
      output name already exists, it will be overwritten.


      **uvcontsub** will read from the CORRECTED_DATA column of *vis*
      if it is present, or DATA if it is not. Whichever column is
      read is presumed to have already been calibrated.


      .. note::

            **WARNING:** Strictly speaking, the **uvcontsub** model
            is only a good representation of the continuum at the
            phase center. Residuals may be visible for sources far
            away and one may try**imcontsub**in the image domain
            for improved results.

      .. note:: **WARNING** **:** *fitorders*> 1 are strongly discouraged
         because high order polynomials have more flexibility, may
         absorb line emission, and tend to go wild at the edges
         of*fitspw*, which is not what you
         want.default:*0*(constant)

      If *want_cont*= *True*, the continuum fit is placed in a
      second new MS with the name vis + '.cont', also overwritten if
      it already exists.

      .. note::

            **INFO:** because the continuum model is necessarily a
            smoothed fit, images made with it are liable to have
            their field of view reduced in some strange way. Images
            of the continuum should be made by simply excluding the
            line channels (and probably averaging the remaining ones)
            in **tclean**.


      

   .. rubric:: Parameter descriptions
      

   .. rubric:: *vis*
      

   Name of input MS. Output goes to vis + ".contsub" (will be
   overwritten if already exists)

   .. rubric:: *field*
      

   `Field
   selection <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__
   for continuum estimation and subtraction. The estimation and
   subtraction is done for each selected field separately in
   turn.default:*''*(all fields)(See`Data Selection in a
   MeasurementSet <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__)

   .. rubric:: *fitspw*
      

   Selection of spectral windows and channels to use in the fit for
   the continuum, using general`MS selection
   syntax <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__for
   spectral windows, e.g. in spw:chan format (spw ids are required
   but*'*'*can be used) or as frequencies.See the note under
   *combine*. default: *fitspw=''* (all)

   .. warning:: **WARNING:**The *fitspw* selection is based on the channel
      numbers in the uv-data of the input MS file, which are most
      likely different from the channel numbers in the image plane
      after running **tclean**.

   .. rubric:: *excludechans (fitspw subparameter)*
      

   if *True*, it will exclude the channels (or frequency range) that
   is specified in *fitspw* for the fit; this is useful to specify
   the line channels to exclude rather than the continuum channels to
   include in the fit. (default: *False*)

   .. rubric:: *combine*
      

   Continuum solutions will break at scan, field, and spw boundaries
   according to *solint.* To allow solutions across these boundaries,
   *combine* can be set to'*spw*', '*scan*', or *'spw, scan'.
   combine* must include *'spw'* ifspw contains spws that are not
   in *fitspw*! default: *''* which is that solutions will break at
   scan, field, and spw

   .. rubric:: *solint*
      

   | Timescale for per-baseline fit (units optional) options are time
     ranges, e.g. '*10s*', or '*inf*' per scan, or '*int*' per
     integration. default (recommended): '*int*', i.e. no time
     averaging, do afit for each integration and let the noisy fits
     average out in the image.continuum fit.If *solint* is longer
     than '*int*', the continuum estimate can be
   | corrupted by time smearing.

   .. rubric:: *fitorder*
      

   | Polynomial order for the fits of the continuum w.r.t. frequency.
     *fitorders* > 1 are strongly discouraged because high order
     polynomials have more flexibility, may
   | absorb line emission, and tend to go wild at the edges of
     *fitspw*, which is not what you want.default: *0* (constant)

   .. rubric:: *spw*
      

   Optional per spectral window selection of channels to include in
   the output. See the note under *combine*.The sub-MS output
   spectral windows will be renumbered to start from 0, as in
   **split**. default: *''* (all spws)(See`Data Selection in a
   MeasurementSet <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__)

   .. rubric:: *want_cont*
      

   Create vis + '.cont' to hold the continuum estimate.




Details
   Explanation of each parameter

.. _vis:

   .. rubric:: vis

   | Name of input MS.  Output goes to vis + ".contsub" (will be overwritten if already exists)

.. _field:

   .. rubric:: field

   | Select field(s) using id(s) or name(s)

.. _fitspw:

   .. rubric:: fitspw

   | Spectral window:channel selection for fitting the continuum

.. _excludechans:

   .. rubric:: excludechans

   | exclude Spectral window:channel selection in fitspw for fitting

.. _combine:

   .. rubric:: combine

   | Data axes to combine for the continuum estimation (none, or spw and/or scan)

.. _solint:

   .. rubric:: solint

   | Continuum fit timescale (int recommended!)

.. _fitorder:

   .. rubric:: fitorder

   | Polynomial order for the fits

.. _spw:

   .. rubric:: spw

   | Spectral window selection for output

.. _want_cont:

   .. rubric:: want_cont

   | Create vis + ".cont" to hold the continuum estimate.


    """
    pass
