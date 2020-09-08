#
# stub function definition file for docstring parsing
#

def specflux(imagename, region='', box='', chans='', stokes='', mask='', stretch=False, function='flux density', unit='km/s', major='', minor='', logfile='', overwrite=False):
    r"""
Report spectral profile and calculate spectral flux over a user specified region

Parameters
   - imagename_ (string) - Name of the input image
   - region_ (variant='') - Region selection. Default is to use the full image.
   - box_ (string='') - Rectangular region to select in direction plane. Default is to use the entire direction plane.
   - chans_ (string='') - Channels to use. Default is to use all channels.
   - stokes_ (string='') - Stokes planes to use. Default is to use all Stokes planes.
   - mask_ (string='') - Mask to use. Default is none.
   - function_ (string='flux density') - Aggregate function to use for computing per channel values. Supported values are "flux density", "mean", "median", "sum". Minimal match supported.
   - unit_ (string='km/s') - Unit to use for the spectral flux calculation. Must be conformant with a typical spectral axis unit.
   - major_ (variant='') - Major axis of overriding restoring beam. If specified, must be a valid quantity.
   - minor_ (variant='') - Minor axis of overriding restoring beam. If specified, must be a valid quantity
   - logfile_ (string='') - File which to write details. Default is to not write to a file.


Description
   .. warning:: **Note**:**specflux**is currently an experimental task.

   **specflux**retrieves details ofa multi-channel image spectrum
   which has been integrated over agiven region (or the entire image
   by default). One may specify which function to use tocombine the
   pixel values within the region using the *function* parameter.
   Supported values are 'flux density', 'mean', 'median', and 'sum'.
   Minimal match is supported. **specflux** also calculates
   spectrally integrated flux (brightness) values.

   The task uses the brightness units that arespecified in the image
   header (e.g., Jy/beam or K). When 'flux density' is calculated,
   the resulting spectra are in units of Jy for cube units of Jy/beam
   and :math:`K*arcsec^2`for cube units of K.

   The spectral integral that **specflux**calculatesis the sum of
   the spectrummultipliedby the channel width. The units are
   updated accordingly.

   If the units are :math:`K*arcsec^2`, multiply the reported value
   by :math:`2.3504\times10^{-8}\times d^2`, where :math:`d` is in
   pc, to convert from units of :math:`K*arcsec^2` to units of
   :math:`K*pc^2`.

   If provided, *major* and *minor* will be used to compute the beam
   size, and hence the per channel flux densities (if *function="flux
   density"*), overriding the input image beam information (if
   present).

   .. note:: **NOTE**: When it is not possible to compute the spectral flux
      (e.g., in the case where the brightness units are Jy/beam but
      the image has no synthesized beam and none is provided to the
      task), then the application will fail.

   The output of **specflux** is written to the CASA logger and an
   ASCII file if *logfile* is specified.

   

   .. rubric:: Parameter descriptions
      

   .. rubric:: *imagename*
      

   Name of the input image (CASA, FITS or MIRIAD images are
   accepted).

   .. rubric:: *region*
      

   Region selection, using a `CASA region
   file <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/region-files>`__.
   Default is the entire image.

   .. rubric:: *box*
      

   `Rectangularspatial
   selection <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/image-selection-parameters>`__,
   if no region file is supplied. Default is the entire image.

   .. rubric:: *chans*
      

   `Spectral/channel
   selection <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/image-selection-parameters>`__,
   if no region file is supplied. Default is the entire channel
   range.

   .. rubric:: *stokes*
      

   `Stokes
   selection <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/image-selection-parameters>`__,
   if no region file is supplied. Default are all Stokes planes.

   .. rubric:: *mask*
      

   An `image
   mask <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/image-masks>`__
   file. Default is not to use a mask.

   .. rubric:: *stretch*
      

   If the image mask is a single plane and not a cube of the same
   dimension as the input data cube, *stretch*can by set to True to
   extendthe mask to all planes. (Default: False)

   .. rubric:: *function*
      

   Aggregate function to use for computing per channel values.
   Supported values are 'flux density', 'mean', 'median', 'sum'.
   Minimal match is supported. *
   *

   .. rubric:: *unit*
      

   Unit to use for the spectral flux calculation. Must be conformant
   with a typical spectral axis unit.Velocity units may only be used
   if the spectral coordinate has a rest frequency and if it is
   :math:`> 0`.

   .. rubric:: *major*
      

   Major axis of overriding restoring beam. If specified, it must be
   a valid quantity (e.g., "4arcsec").

   .. rubric:: *minor*
      

   Minor axis of overriding restoring beam. If specified, it must be
   a valid quantity (e.g., "3arcsec").

   .. rubric:: *logfile*
      

   File which to write details. Default is to not write to a file.

   .. rubric:: *overwrite*
      

   Overwrite exisitng*logfile* file if it exists. (Default: False)




Details
   Explanation of each parameter

.. _imagename:

   .. rubric:: imagename

   | Name of the input image

.. _region:

   .. rubric:: region

   | Region selection. Default is to use the full image.

.. _box:

   .. rubric:: box

   | Rectangular region to select in direction plane. Default is to use the entire direction plane.

.. _chans:

   .. rubric:: chans

   | Channels to use. Default is to use all channels.

.. _stokes:

   .. rubric:: stokes

   | Stokes planes to use. Default is to use all Stokes planes.

.. _mask:

   .. rubric:: mask

   | Mask to use. Default is none.

.. _stretch:

   .. rubric:: stretch

   | Stretch the mask if necessary and possible?

.. _function:

   .. rubric:: function

   | Aggregate function to use for computing per channel values. Supported values are "flux density", "mean", "median", "sum". Minimal match supported.

.. _unit:

   .. rubric:: unit

   | Unit to use for the spectral flux calculation. Must be conformant with a typical spectral axis unit.

.. _major:

   .. rubric:: major

   | Major axis of overriding restoring beam. If specified, must be a valid quantity.

.. _minor:

   .. rubric:: minor

   | Minor axis of overriding restoring beam. If specified, must be a valid quantity

.. _logfile:

   .. rubric:: logfile

   | File which to write details. Default is to not write to a file.

.. _overwrite:

   .. rubric:: overwrite

   | Overwrite exisitng ouput file if it exists?


    """
    pass
