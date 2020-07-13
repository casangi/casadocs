.. container::
   :name: viewlet-above-content-title

imview
======

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   imval task: Get the data value(s) and/or mask value in an image.

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Summary
         :name: summary

      Displays images and data cubes in raster, contour, vector
      or marker form.

      Executing the imview task will bring up a display panel window,
      which can be resized. If no data file was specified, a Load Data
      window will also appear. Click on the desired data file and choose
      the display type; the rendered data should appear on the display
      panel.Images can be blinked, and movies are available for
      spectral-line image cubes.The loaded data and related
      display options can be saved in a 'restore' file for later
      use. You can provide the 'restore' filename on the command line
      or select it from the Load Data window.

      A Data Display Options window will also appear. It has
      drop-down subsections for related options, most of which are
      self-explanatory. It is also possible to use the viewer GUI tool
      to perform image manipulation and analysis tasks that are not
      available from the command-line start.

      The imview task provides access to a subset of all of the
      configuration options for loading and configuring the display of
      images in the casaviewer, but support for this task is limited.
      See the chapter pages on\ `Image Cube
      Visualization <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization>`__\ for
      more information.

       

      .. rubric:: Parameter descriptions
         :name: parameter-descriptions
         :class: p1

      There are five optional parameters for imview -- raster, contour,
      zoom, axes, and out. Each of these parameters are optional, can
      take a few different forms, and are treated as python
      dictionaries:

      .. rubric:: *raster*
         :name: raster
         :class: p1

      Raster filename (string) or complete raster config dictionary. The
      allowed dictionary keys are:

      -  file (string) => image file to open
      -  scaling (float) => scaling power cycles
      -  range (float*2) => data range
      -  colormap (string) => name of colormap
      -  colorwedge (bool) => show color wedge?

      .. rubric:: *contour*
         :name: contour
         :class: p1

      Contour filename (string) or complete contour config dictionary.
      The allowed dictionary keys are:

      -  file (string) => file to load
      -  levels (float*N) => relative levels
      -  base (numeric) => zero in relative levels
      -  unit (numeric) => one in the relative levels

      .. rubric:: *zoom*
         :name: zoom
         :class: p1

      Zoom can specify incremental zoom (integer), zoom region read from
      a file (string), or dictionary specifying the zoom region. The
      dictionary can have different forms. It can be a simple region
      specified with blc (2 element vector) and trc (2 element vector),
      along with an optional coord key ("pixel" or "world"; pixel is the
      default), or it can be a complete region rectangle, e.g., loaded
      with **rg.fromfiletorecord**\ ( ). The dictionary can also contain
      a channel (integer) field which indicates which channel should be
      displayed.

      -  (int) integral zoom level
      -  (string) region file to load as the zoom region
      -  (dict) blc (numeric*2) => bottom left corner
      -  trc (numeric*2) => top right corner
      -  coord (string) => pixel or world
      -  channel (int) => chanel to display
      -  (dict) <region record> => record loaded, e.g.,
         rg.fromfiletorecord\ ( )

      .. rubric:: *axes*
         :name: axes
         :class: p1

      This can either be a three-element vector (string) where each
      element describes what should be found on each of the x, y, and z
      axes, or a dictionary containing fields "x", "y" and "z" (string):

      -  (dict) x => dimension for x-axes
      -  y => dimension for y-axes
      -  z => dimension for z-axes

      .. rubric:: *out*
         :name: out
         :class: p1

      Output filename or complete output config dictionary. If a string
      is passed, the file extension is used to determine the output type
      (jpg, pdf, eps, ps, png, xbm, xpm, or ppm). If a dictionary is
      passed, it can contain the fields, file (string), scale (float),
      dpi (int), or orient (landscape or portrait). The scale field is
      used for the bitmap formats (i.e., not ps or pdf) and the dpi
      parameter is used for scalable formats (pdf or ps).

      -  (dict) file (string) => filename
      -  format (string) => valid ext (filename ext overrides)
      -  scale (numeric) => scale for non-eps, non-ps output
      -  dpi (numeric) => dpi for eps or ps output
      -  orient (string) => portrait or landscape

       

      imview interactive display

      ======= ==============================
      Type    Figure
      ID      1
      Caption **imview** interactive display
      ======= ==============================

       

.. container:: section
   :name: viewlet-below-content-body

.. toctree::
   :hidden:
   :maxdepth: 3

   task_imview/about
   task_imview/examples
