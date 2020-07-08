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

            Name of the input (CASA, FITS, MIRIAD) image

Example

imagename='ngc5921.im'

.. container:: param

   .. container:: parameters2

      pbimage : undefined = ""

   Name of the image (CASA, FITS, MIRIAD) of the primary beam pattern or
   an array of pixel values. Default: ''

Example

.. container:: param

   .. container:: parameters2

      outfile : string

   Name of output CASA image. Default: none. Must be specified.

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   If output file is specified, controls if an already existing file by
   the same name can be overwritten. Default: True Options: True|False
   If true, the user is not prompted, the file if it exists is
   automatically overwritten.

Example

.. container:: param

   .. container:: parameters2

      box : string

   Rectangular region to select in direction plane. Default: '' (use the
   entire direction plane)

Example

.. container:: param

   .. container:: parameters2

      region : undefined

   Region selection. Default: '' (use the full image)

Example

.. container:: param

   .. container:: parameters2

      chans : string

   Channels to use. Default: '' (use all channels)

Example

.. container:: param

   .. container:: parameters2

      stokes : string

   Stokes planes to use. Default: '' (use all Stokes planes)

Example

.. container:: param

   .. container:: parameters2

      mask : string

   Mask to use. Default: none

Example

.. container:: param

   .. container:: parameters2

      mode : string = divide

   Divide or multiply the image by the primary beam image. Default:
   'divide' Minimal match supported.

Example

.. container:: param

   .. container:: parameters2

      cutoff : double = -1.0

   Primary beam cutoff. Default: -1.0 (no cutoff) If mode is "d", all
   values less than this will be masked. If "m", all values greater will
   be masked. Less than 0, no cutoff (default)

Example

.. container:: param

   .. container:: parameters2

      stretch : bool = False

   Stretch the mask if necessary and possible? Default: False Options:
   False|True

Example

.. container:: section
   :name: viewlet-below-content-body
