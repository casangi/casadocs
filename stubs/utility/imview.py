#
# stub function definition file for docstring parsing
#

def imview(raster='', contour='', zoom='1', axes='', out=''):
    r"""
View an image

Parameters
   - **raster** ({string, record}='') -  [1]_
   - **contour** ({string, record}='') -  [2]_
   - **zoom** ({int, string, record}='1') -  [3]_
   - **axes** ({string, record}='') -  [4]_
   - **out** ({string, record}='') -  [5]_


Description
   .. rubric:: Summary
      

   Displays images and data cubes in raster, contour, vector
   ormarker form.

   Executing the imview task will bring up a display panelwindow,
   which can be resized. If no data file was specified,a Load Data
   window will also appear. Click on the desired datafile and choose
   the display type; the rendered data should appearon the display
   panel.Images can be blinked, and movies are availablefor
   spectral-line image cubes.The loaded data and related
   displayoptions can be saved in a 'restore' file for later
   use.You can provide the 'restore' filename on the command line
   orselect it from the Load Data window.

   AData Display Options window will also appear. It has
   drop-downsubsections for related options, most of which are
   self-explanatory. It is also possible to use the viewer GUI tool
   to perform image manipulationand analysis tasks that are not
   available from the command-line start.

   The imview task provides access to a subset of all of the
   configurationoptions for loading and configuring the display of
   images in the casaviewer, but support for this task is limited.
   See the chapter pages on `Image Cube
   Visualization <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization>`__ for
   more information.

   

   .. rubric:: Parameter descriptions
      

   There are five optional parameters for imview -- raster, contour,
   zoom, axes, and out. Each of these parameters are optional, can
   take a few different forms, and are treated as python
   dictionaries:

   .. rubric:: *raster*
      

   Raster filename (string) or complete raster config dictionary. The
   allowed dictionary keys are:

   -  file (string) => image file to open
   -  scaling (float) => scaling power cycles
   -  range (float*2) => data range
   -  colormap (string) => name of colormap
   -  colorwedge (bool) => show color wedge?

   .. rubric:: *contour*
      

   Contour filename (string) or complete contour config dictionary.
   The allowed dictionary keys are:

   -  file (string) => file to load
   -  levels (float*N) => relative levels
   -  base (numeric) => zero in relative levels
   -  unit (numeric) => one in the relative levels

   .. rubric:: *zoom*
      

   Zoom can specify incremental zoom (integer), zoom region read from
   a file (string), or dictionary specifying the zoom region. The
   dictionary can have different forms. It can be a simple region
   specified with blc (2 element vector) and trc (2 element vector),
   along with an optional coord key ("pixel" or "world"; pixel is the
   default), or it can be a complete region rectangle, e.g., loaded
   with **rg.fromfiletorecord** ( ). The dictionary can also contain
   a channel (integer) field which indicates which channel should be
   displayed.

   -  (int) integral zoom level
   -  (string) region file to load as the zoom region
   -  (dict) blc (numeric*2) => bottom left corner
   -  trc (numeric*2) => top right corner
   -  coord (string) => pixel or world
   -  channel (int) => chanel to display
   -  (dict)<region record> => record loaded, e.g.,
      rg.fromfiletorecord ( )

   .. rubric:: *axes*
      

   This can either be a three-element vector (string) where each
   element describes what should be found on each of the x, y, and z
   axes, or a dictionary containing fields "x", "y" and "z" (string):

   -  (dict) x => dimension for x-axes
   -  y => dimension for y-axes
   -  z => dimension for z-axes

   .. rubric:: *out*
      

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




Details
   Explanation of each parameter

.. [1] 
   **raster** ({string, record}='')
      | (Optional)  Raster filename (string) or complete raster config dictionary. The allowed dictionary keys are file (string), scaling (numeric), range (2 element numeric vector), colormap (string), and colorwedge (bool).
.. [2] 
   **contour** ({string, record}='')
      | (Optional)  Contour filename (string) or complete contour config dictionary. The allowed dictionary keys are file (string), levels (numeric vector), unit (float), and base (float).
.. [3] 
   **zoom** ({int, string, record}='1')
      | (Optional)  zoom can specify intermental zoom (integer), zoom region read from a file (string) or dictionary specifying the zoom region. The dictionary can have two forms. It can be either a simple region specified with blc (2 element vector) and trc (2 element vector) [along with an optional coord key ("pixel" or "world"; pixel is the default) or a complete region rectangle e.g. loaded with "rg.fromfiletorecord( )". The dictionary can also contain a channel (integer) field which indicates which channel should be displayed.
.. [4] 
   **axes** ({string, record}='')
      | (Optional)  this can either be a three element vector (string) where each element describes what should be found on each of the x, y, and z axes or a dictionary containing fields "x", "y" and "z" (string).
.. [5] 
   **out** ({string, record}='')
      | (Optional)  Output filename or complete output config dictionary. If a string is passed, the file extension is used to determine the output type (jpg, pdf, eps, ps, png, xbm, xpm, or ppm). If a dictionary is passed, it can contain the fields, file (string), scale (float), dpi (int), or orient (landscape or portrait). The scale field is used for the bitmap formats (i.e. not ps or pdf) and the dpi parameter is used for scalable formats (pdf or ps).

    """
    pass
