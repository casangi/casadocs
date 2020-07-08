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

               imagename : undefined

            a list of input images

Example

.. container:: param

   .. container:: parameters2

      mode : string = evalexpr

   mode for math operation (evalexpr, spix, pola, poli, lpoli, tpoli)

Allowed Value(s)

evalexpr spix pola poli lpoli tpoli

Example

'evalexpr', 'spix', 'pola', or 'poli'

.. container:: param

   .. container:: parameters2

      outfile : string = immath_results.im

   File where the output is saved

Example

outfile="newimage"

.. container:: param

   .. container:: parameters2

      expr : string = IM0

   Mathematical expression using images

Example

expr='"sin(image1.im)+(image2.im*2)+real(image3.im)"'

.. container:: param

   .. container:: parameters2

      varnames : undefined

   a list of variable names to use with the image files

Example

.. container:: param

   .. container:: parameters2

      sigma : string = 0.0mJy/beam

   standard deviation of noise for debiasing

Example

.. container:: param

   .. container:: parameters2

      polithresh : string

   Threshold in linear polarization intensity image below which to mask
   pixels.

Example

.. container:: param

   .. container:: parameters2

      mask : string

   Mask to use. Default is none.

Example

.. container:: param

   .. container:: parameters2

      region : string

   Region selection. Default is to use the full image.

Example

.. container:: param

   .. container:: parameters2

      box : string

   Rectangular region to select in direction plane. Default is to use
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

stokes='IQ'stokes='RR,LL'

.. container:: param

   .. container:: parameters2

      stretch : bool = False

   Stretch the mask if necessary and possible? See help stretch.par

Example

.. container:: param

   .. container:: parameters2

      imagemd : string

   An image name from which metadata should be copied. The input can be
   either an image listed under imagename or any other image on disk.
   Leaving this parameter unset may copy header metadata from any of the
   input images, which one is not guaranteed.

Example

.. container:: param

   .. container:: parameters2

      prec : string = float

   Precision for the output image pixels if mode="evalexpr" or "spix".
   "float" or "double" (minimum match supported)

Example

.. container:: section
   :name: viewlet-below-content-body
