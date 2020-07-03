.. container::
   :name: viewlet-above-content-title

Examples
========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task examples

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      To simply create a CASA viewer to set up interactively, you can
      use:

      .. container:: casa-input-box

         imview

      To open a particular image:

      .. container:: casa-input-box

         imview "ngc5921.clean.image"

      To open an image and overlay a contour:

      .. container:: casa-input-box

         imview "ngc5921.clean.image", "ngc5921.clean.image"

      or equivalently:

      .. container:: casa-input-box

         imview(raster="ngc5921.clean.image",
         contour="ngc5921.clean.image")

      To output an image:

      .. container:: casa-input-box

         imview(raster="ngc5921.clean.image", out="ngc5921-01.png")   

      To plot a subset (zoom) of a raster image, noting the notation of
      curly brackets:

      .. container:: casa-input-box

         imview(raster="ngc5921.clean.image", out="ngc5921-02.png",
         zoom={'channel': 10, 'blc': [113,109], 'trc': [141,136]} )

      To make an overlay of a raster image (ngc5921.clean.image) with a
      contour map of the same image (ngc5921.clean.image). Data ranges,
      the colormap, and the scaling cycles of the raster image are
      selected. Contours are auto-generated, and the x-axis will be
      declination. The image is written out to a file named myout.png
      (in png format).

      .. container:: casa-input-box

         imview(raster={'file': 'ngc5921.clean.image', 'range':
         [-0.01,0.03], 'colormap': 'Hot Metal 2', 'scaling': -1},
         contour={'file': 'ngc5921.clean.image'},
         axes={'x':'Declination'}, zoom={'channel': 7, 'blc': [75,75],
         'trc': [175,175], 'coord': 'pixel'}, out='myout.png')

      Same as the previous example, but with an integral zoom level and
      no output to a file:

      .. container:: casa-input-box

         imview(raster={'file': 'ngc5921.clean.image', 'range':
         [-0.01,0.03], 'colormap': 'Hot Metal 2'},contour={'file':
         'ngc5921.clean.image'}, axes={'x':'Declination'}, zoom=2)

      Here, the contour levels are explicitely given, and a region file
      is used to define the zoom area:

      .. container:: casa-input-box

         imview(raster={'file': 'ngc5921.clean.image', 'range':
         [-0.01,0.03], 'colormap': 'Hot Metal 2'}, contour={'file':
         'ngc5921.clean.image', 'levels': [-0.2, 0.2, 0.25, 0.3, 0.35,
         0.4, 0.6, 0.8] }, zoom='myregion.rgn')

      Specifying zoom={'file': 'myregion.rgn', 'channel': 10} would
      result in the same level of zoom and would display channel number
      10 from the cube.

       

.. container:: section
   :name: viewlet-below-content-body
