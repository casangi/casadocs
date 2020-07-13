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

imagename=ngc5921_task.image

.. container:: param

   .. container:: parameters2

      axes : undefined = -1

   List of axes to evaluate statistics over. Default is all axes.

Example

[0, 1]

.. container:: param

   .. container:: parameters2

      region : string

   Region selection. Default is to use the full image.

Example

.. container:: param

   .. container:: parameters2

      box : string

   Rectangular region(s) to select in direction plane. Default is to use
   the entire direction plane.

Example

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

stokes="IQ"stokes="RR,LL"

.. container:: param

   .. container:: parameters2

      listit : bool = True

   Print stats and bounding box to logger?

Example

.. container:: param

   .. container:: parameters2

      verbose : bool = True

   Print additional messages to logger?

Example

.. container:: param

   .. container:: parameters2

      mask : string

   Mask to use. Default is none.

Example

.. container:: param

   .. container:: parameters2

      stretch : bool = False

   Stretch the mask if necessary and possible?

Example

.. container:: param

   .. container:: parameters2

      logfile : string

   Name of file to write fit results.

Example

logfile="myimfitlog.txt"

.. container:: param

   .. container:: parameters2

      append : bool = True

   If logfile exists, append to it if True or overwrite it if False

Example

append=True

.. container:: param

   .. container:: parameters2

      algorithm : string = classic

   Algorithm to use. Supported values are "biweight", "chauvenet",
   "classic", "fit-half", and "hinges-fences". Minimum match is
   supported.

Example

.. container:: param

   .. container:: parameters2

      fence : double = -1

   Fence value for hinges-fences. A negative value means use the entire
   data set (ie default to the "classic" algorithm). Ignored if
   algorithm is not "hinges-fences".

Example

.. container:: param

   .. container:: parameters2

      center : string = mean

   Center to use for fit-half. Valid choices are "mean", "median", and
   "zero". Ignored if algorithm is not "fit-half".

Example

.. container:: param

   .. container:: parameters2

      lside : bool = True

   For fit-half, use values <= center for real data if True? If False,
   use values >= center as real data. Ignored if algorithm is not
   "fit-half".

Example

.. container:: param

   .. container:: parameters2

      zscore : double = -1

   For chauvenet, this is the target maximum number of standard
   deviations data may have to be included. If negative, use Chauvenet"s
   criterion. Ignored if algorithm is not "chauvenet".

Example

.. container:: param

   .. container:: parameters2

      maxiter : int = -1

   For chauvenet, this is the maximum number of iterations to attempt.
   Iterating will stop when either this limit is reached, or the zscore
   criterion is met. If negative, iterate until the zscore criterion is
   met. Ignored if algorithm is not "chauvenet".

Example

.. container:: param

   .. container:: parameters2

      clmethod : string = auto

   Method to use for calculating classical statistics. Supported methods
   are "auto", "tiled", and "framework". Ignored if algorithm is not
   "classic".

Example

.. container:: param

   .. container:: parameters2

      niter : int = 3

   For biweight, this is the maximum number of iterations to attempt.
   Iterating will stop when either this limit is reached, or the zscore
   criterion is met. If negative, do a fast, simple computation (see
   description). Ignored if the algorithm is not "biweight".

Example

.. container:: section
   :name: viewlet-below-content-body
