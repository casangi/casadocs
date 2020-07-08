.. container::
   :name: viewlet-above-content-title

Parameters
==========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task parameters

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               imagename : undefined

            Name of the input image(s)

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

   Mask to use. Default is none.

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

      spxtype : string = plp

   Type of function to fit. "plp" = power logarithmic polynomial, "ltp"
   = logarithmic transformed polynomial.

Example

.. container:: param

   .. container:: parameters2

      spxest : doubleArray

   REQUIRED. Initial estimates as array of numerical values for the
   spectral index function coefficients. eg [1.5, -0.8] if fitting a plp
   function thought to be close to 1.5*(x/div)**(-0.8) or [0.4055, -0.8]
   if fitting an lpt function thought to be close to ln(1.5) -
   0.8*ln(x/div).

Example

.. container:: param

   .. container:: parameters2

      spxfix : boolArray

   Fix the corresponding spectral index function coefficients during the
   fit. True means hold fixed.

Example

.. container:: param

   .. container:: parameters2

      div : undefined = 0

   Divisor (numerical value or quantity) to use in the logarithmic terms
   of the plp or ltp function. 0 means calculate a useful value on the
   fly.

Example

.. container:: param

   .. container:: parameters2

      spxsol : string

   Name of the spectral index function coefficient solution image to
   write.

Example

.. container:: param

   .. container:: parameters2

      spxerr : string

   Name of the spectral index function coefficient error image to write.

Example

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

      sigma : string stringArray doubleArray intArray

   Standard deviation array or image name(s).

Example

.. container:: param

   .. container:: parameters2

      outsigma : string

   Name of output image used for standard deviation. Ignored if sigma is
   empty.

Example

.. container:: section
   :name: viewlet-below-content-body
