Parameters
==========

.. container:: documentDescription description

   task parameters

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               imagename : string

            Name of the input image

Example

imagename='ngc5921_task.image'

.. container:: param

   .. container:: parameters2

      box : string

   Rectangular region to select in direction plane. Default is to use
   the entire direction plane.

Example

box="4,4,10,10"

.. container:: param

   .. container:: parameters2

      region : string

   Region selection. Default is to use the full image.

Example

region="myregion.rgn"

.. container:: param

   .. container:: parameters2

      chans : string

   Channels to use. Default is to use all channels.

Example

.. container:: param

   .. container:: parameters2

      stokes : string

   Stokes planes to use. Default is to use all Stokes planes.

Example

stokes="I"

.. container:: param

   .. container:: parameters2

      axis : int = -1

   The profile axis. Default: use the spectral axis if one exists, axis
   0 otherwise (<0).

Example

axis=3

.. container:: param

   .. container:: parameters2

      mask : string

   Mask to use. Default is none..

Example

.. container:: param

   .. container:: parameters2

      ngauss : int = 1

   Number of Gaussian elements. Default: 1.

Example

ngauss=2

.. container:: param

   .. container:: parameters2

      poly : int = -1

   Order of polynomial element. Default: do not fit a polynomial (<0).

Example

poly=4

.. container:: param

   .. container:: parameters2

      estimates : string

   Name of file containing initial estimates. Default: No initial
   estimates ("").

Example

.. container:: param

   .. container:: parameters2

      minpts : int = 1

   Minimum number of unmasked points necessary to attempt fit.

Example

.. container:: param

   .. container:: parameters2

      multifit : bool = False

   If true, fit a profile along the desired axis at each pixel in the
   specified region. If false, average the non-fit axis pixels and do a
   single fit to that average profile. Default False.

Example

multifit=True

.. container:: param

   .. container:: parameters2

      model : string

   Name of model image. Default: do not write the model image ("").

Example

model="mymodel.im"

.. container:: param

   .. container:: parameters2

      residual : string

   Name of residual image. Default: do not write the residual image
   ("").

Example

residual="myresid.im"

.. container:: param

   .. container:: parameters2

      amp : string

   Name of amplitude solution image. Default: do not write the image
   ("").

Example

amp="amp"

.. container:: param

   .. container:: parameters2

      amperr : string

   Name of amplitude solution error image. Default: do not write the
   image ("").

Example

amperr="ampErr"

.. container:: param

   .. container:: parameters2

      center : string

   Name of center solution image. Default: do not write the image ("").

Example

center="center"

.. container:: param

   .. container:: parameters2

      centererr : string

   Name of center solution error image. Default: do not write the image
   ("").

Example

centererr="centerErr"

.. container:: param

   .. container:: parameters2

      fwhm : string

   Name of fwhm solution image. Default: do not write the image ("").

Example

fwhm="fwhm"

.. container:: param

   .. container:: parameters2

      fwhmerr : string

   Name of fwhm solution error image. Default: do not write the image
   ("").

Example

fwhmerr="fwhmErr"

.. container:: param

   .. container:: parameters2

      integral : string

   Prefix of ame of integral solution image. Name of image will have
   gaussian component number appended. Default: do not write the image
   ("").

Example

integral="integral"

.. container:: param

   .. container:: parameters2

      integralerr : string

   Prefix of name of integral error solution image. Name of image will
   have gaussian component number appended. Default: do not write the
   image ("").

Example

integralerr="integralErr"

.. container:: param

   .. container:: parameters2

      wantreturn : bool = True

   Should a record summarizing the results be returned?

Example

wantreturn=True

.. container:: param

   .. container:: parameters2

      stretch : bool = False

   Stretch the mask if necessary and possible?

Example

.. container:: param

   .. container:: parameters2

      logresults : bool = True

   Output results to logger?

Example

.. container:: param

   .. container:: parameters2

      pampest : variant

   Initial estimate of PCF profile (gaussian or lorentzian) amplitudes.

Example

.. container:: param

   .. container:: parameters2

      pcenterest : variant

   Initial estimate PCF profile centers, in pixels.

Example

.. container:: param

   .. container:: parameters2

      pfwhmest : variant

   Initial estimate PCF profile FWHMs, in pixels.

Example

.. container:: param

   .. container:: parameters2

      pfix : variant

   PCF profile parameters to fix during fit.

Example

.. container:: param

   .. container:: parameters2

      gmncomps : variant = 0

   Number of components in each gaussian multiplet to fit

Example

.. container:: param

   .. container:: parameters2

      gmampcon : variant

   The amplitude ratio constraints for non-reference components to
   reference component in gaussian multiplets.

Example

.. container:: param

   .. container:: parameters2

      gmcentercon : variant

   The center offset constraints (in pixels) for non-reference
   components to reference component in gaussian multiplets.

Example

.. container:: param

   .. container:: parameters2

      gmfwhmcon : variant

   The FWHM ratio constraints for non-reference components to reference
   component in gaussian multiplets.

Example

.. container:: param

   .. container:: parameters2

      gmampest : doubleArray = 0.0

   Initial estimate of individual gaussian amplitudes in gaussian
   multiplets.

Example

.. container:: param

   .. container:: parameters2

      gmcenterest : doubleArray = 0.0

   Initial estimate of individual gaussian centers in gaussian
   multiplets, in pixels.

Example

.. container:: param

   .. container:: parameters2

      gmfwhmest : doubleArray = 0.0

   Initial estimate of individual gaussian FWHMss in gaussian
   multiplets, in pixels.

Example

.. container:: param

   .. container:: parameters2

      gmfix : variant

   Parameters of individual gaussians in gaussian multiplets to fix
   during fit.

Example

.. container:: param

   .. container:: parameters2

      logfile : string

   File in which to log results. Default is not to write a logfile.

Example

.. container:: param

   .. container:: parameters2

      append : bool = True

   Append results to logfile? Logfile must be specified. Default is to
   append. False means overwrite existing file if it exists.

Example

.. container:: param

   .. container:: parameters2

      pfunc : string stringArray

   PCF singlet functions to fit. "gaussian" or "lorentzian" (minimal
   match supported). Unspecified means all gaussians.

Example

.. container:: param

   .. container:: parameters2

      goodamprange : doubleArray = 0.0

   Acceptable amplitude solution range. [0.0] => all amplitude solutions
   are acceptable.

Example

.. container:: param

   .. container:: parameters2

      goodcenterrange : doubleArray = 0.0

   Acceptable center solution range in pixels relative to region start.
   [0.0] => all center solutions are acceptable.

Example

.. container:: param

   .. container:: parameters2

      goodfwhmrange : doubleArray = 0.0

   Acceptable FWHM solution range in pixels. [0.0] => all FWHM solutions
   are acceptable.

Example

.. container:: param

   .. container:: parameters2

      sigma : string doubleArray intArray

   Standard deviation array or image name.

Example

.. container:: param

   .. container:: parameters2

      outsigma : string

   Name of output image used for standard deviation. Ignored if sigma is
   empty.

Example

.. container:: section
   :name: viewlet-below-content-body
