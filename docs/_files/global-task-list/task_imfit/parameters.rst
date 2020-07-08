.. container::
   :name: viewlet-above-content-title

Parameters
==========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task applycal parameters

.. container:: section
   :name: viewlet-above-content-body

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

imagename='ngc5921.im'

.. container:: param

   .. container:: parameters2

      box : string

   Rectangular region(s) to select in direction plane. Default is to use
   the entire direction plane.

Example

box='100,120,200,200'

.. container:: param

   .. container:: parameters2

      region : undefined

   Region selection. Default is to use the full image.

Example

region='myregion'

.. container:: param

   .. container:: parameters2

      chans : undefined

   Channels to use. Default is to use all channels.

Example

.. container:: param

   .. container:: parameters2

      stokes : string

   Stokes planes to use. Default is to use first Stokes plane.

Example

stokes='Q'

.. container:: param

   .. container:: parameters2

      mask : string

   Mask to use. Default is none.

Example

.. container:: param

   .. container:: parameters2

      includepix : intArray

   Range of pixel values to include for fitting.

Example

includepix=[0.5,500]

.. container:: param

   .. container:: parameters2

      excludepix : intArray

   Range of pixel values to exclude for fitting.

Example

excludepix=[-500,.05]

.. container:: param

   .. container:: parameters2

      residual : string

   Name of output residual image.

Example

residual='ngc5921_fit_resid.im'

.. container:: param

   .. container:: parameters2

      model : string

   Name of output model image.

Example

model='ngc5921_fit_model.im'

.. container:: param

   .. container:: parameters2

      estimates : string

   Name of file containing initial estimates of component parameters.

Example

estimates='ngc5921_fit_estimates.txt'

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

      newestimates : string

   File to write fit results which can be used as initial estimates for
   next run.

Example

newestimates="myestimates.txt"

.. container:: param

   .. container:: parameters2

      complist : string

   Name of output component list table.

Example

complist='myoutputcomplist.tbl'

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   Overwrite component list table if it exists?

Example

overwrite=true

.. container:: param

   .. container:: parameters2

      dooff : bool = False

   Also fit a zero level offset? Default is False

Example

.. container:: param

   .. container:: parameters2

      offset : double = 0.0

   Initial estimate of zero-level offset. Only used if doff is True.
   Default is 0.0

Example

.. container:: param

   .. container:: parameters2

      fixoffset : bool = False

   Keep the zero level offset fixed during fit? Default is False

Example

.. container:: param

   .. container:: parameters2

      stretch : bool = False

   Stretch the mask if necessary and possible?

Example

.. container:: param

   .. container:: parameters2

      rms : int double record string = -1

   RMS to use in calculation of uncertainties. Numeric or valid quantity
   (record or string). If numeric, it is given units of the input image.
   If quantity, units must conform to image units. If not positive, the
   rms of the residual image, in the region of the fit, is used.

Example

.. container:: param

   .. container:: parameters2

      noisefwhm : int double record string

   Noise correlation beam FWHM. If numeric value, interpreted as pixel
   widths. If quantity (dictionary, string), it must have angular units.

Example

.. container:: param

   .. container:: parameters2

      summary : string

   File name to which to write table of fit parameters.

Example

.. container:: section
   :name: viewlet-below-content-body
