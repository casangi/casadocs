#
# stub function definition file for docstring parsing
#

def rmfit(imagename, rm='', rmerr='', pa0='', pa0err='', nturns='', chisq='', sigma=-1, rmfg=0.0, rmmax=0.0, maxpaerr=1e30):
    r"""
Calculate rotation measure.

Parameters
   - imagename_ (variant) - Name(s) of the input image(s). Must be specified.
   - rm_ (string='') - Output rotation measure image name. If not specified, no image is written.
   - rmerr_ (string='') - Output rotation measure error image name. If not specified, no image is written.
   - pa0_ (string='') - Output position angle (degrees) at zero wavelength image name. If not specified, no image is written.
   - pa0err_ (string='') - Output position angle (degrees) at zero wavelength error image name. If not specified, no image is written.
   - nturns_ (string='') - Output number of turns image name. If not specified, no image is written.
   - chisq_ (string='') - Output reduced chi squared image name. If not specified, no image is written.
   - sigma_ (double=-1) - Estimate of the thermal noise.  A value less than 0 means auto estimate.
   - rmfg_ (double=0.0) - Foreground rotation measure in rad/m/m to subtract.
   - rmmax_ (double=0.0) - Maximum rotation measure in rad/m/m for which to solve. IMPORTANT TO SPECIFY.
   - maxpaerr_ (double=1e30) - Maximum input position angle error in degrees to allow in solution determination.


Description
   This task generates the rotation measure (RM) image from stokes Q
   and U measurements at several different frequencies. You are
   required to specify the name of at least one image with a
   polarization axis containing Stokes Q and U planes and with a
   frequency axis containing more than two channels. The frequencies
   do not have to be equally spaced (i.e., the frequency coordinate
   can be a tabular coordinate).The task will work out the position
   angle images for you. You may also specify multiple image names,
   in which case these images will first be concatenated along the
   spectral axis using **ia.imageconcat**. The requirements are that
   for all images, the axis order must be the same and the number of
   pixels along each axis must be identical, except for the spectral
   axis which may differ in length between images. The spectral axis
   need not be contiguous from one image to another.

   Rotation measure algorithms that work robustly are few. The main
   problem is in trying to account for the n-pi ambiguity
   `[1] <#cit1>`__ .

   This task uses the algorithm published in Appendix A.1 ofLeahy et
   al. `[1] <#cit1>`__ But as in all these algorithms, the basic
   process is that for each spatial pixel, the position angle vs
   frequency data is fit to determine the rotation measure and the
   position angle at zero wavelength (and associated errors). An
   image containing the number of n-pi turns that were added to the
   data at each spatial pixel and for which the best fit was found
   can be written. The reduced chi-squared image for the fits can
   also be written.

   Note that no assessment of curvature (i.e., deviation from the
   simple linear position angle - lambda :sup:`2` functional form)
   is made.

   Any combination of output images can be written.

   The parameter *sigma* gives the thermal noise in Stokes Q and U.
   By default it is determined automatically using the image data.
   But if it proves to be inaccurate (maybe not many signal-free
   pixels), it may be specified. This is used for calculating the
   error in the position angles (via propagation of Gaussian errors).

   The *maxpaerr* parameter specifies the maximum allowable error in
   the position angle that is acceptable. The default is an infinite
   value. From the standard propagation of errors, the error in the
   linearly polarized position angle is determined from the Stokes Q
   and U images (at each directional pixel for each frequency). If
   the position angle error for any pixel exceeds the specified
   value, the position angle at that pixel is omitted from the fit.
   The process generates an error for the fit and this is used to
   compute the errors in the output images.

   Note that *maxpaerr* is not used to mask pixels in the output
   images.

   The *rmfg* parameter is used to specify a foreground RM value. For
   example, you may know the mean RM in some direction out of the
   Galaxy, then including this can improve the algorithm by reducing
   ambiguity.

   The parameter *rmmax* specifies the maximum absolute RM value that
   should be solved for. This is quite an important parameter. The
   default value, 0, indicates no ambiguity handling will be used. So
   some apriori information should be supplied; this is the basic
   problem with rotation measure algorithms.


   Bibliography
      :sup:`1. Leahy et al. 1986, Astronomy & Astrophysics, 156,
      234` `(ADS) <http://adsabs.harvard.edu/full/1986A%26A...156..234L>`__ `<#ref-cit1>`__




Details
   Explanation of each parameter

.. _imagename:

   .. rubric:: imagename

   | Name(s) of the input image(s). Must be specified.

.. _rm:

   .. rubric:: rm

   | Output rotation measure image name. If not specified, no image is written.

.. _rmerr:

   .. rubric:: rmerr

   | Output rotation measure error image name. If not specified, no image is written.

.. _pa0:

   .. rubric:: pa0

   | Output position angle (degrees) at zero wavelength image name. If not specified, no image is written.

.. _pa0err:

   .. rubric:: pa0err

   | Output position angle (degrees) at zero wavelength error image name. If not specified, no image is written.

.. _nturns:

   .. rubric:: nturns

   | Output number of turns image name. If not specified, no image is written.

.. _chisq:

   .. rubric:: chisq

   | Output reduced chi squared image name. If not specified, no image is written.

.. _sigma:

   .. rubric:: sigma

   | Estimate of the thermal noise.  A value less than 0 means auto estimate.

.. _rmfg:

   .. rubric:: rmfg

   | Foreground rotation measure in rad/m/m to subtract.

.. _rmmax:

   .. rubric:: rmmax

   | Maximum rotation measure in rad/m/m for which to solve. IMPORTANT TO SPECIFY.

.. _maxpaerr:

   .. rubric:: maxpaerr

   | Maximum input position angle error in degrees to allow in solution determination.


    """
    pass
