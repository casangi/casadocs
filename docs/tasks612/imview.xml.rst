imview -- View an image -- utility, visualization task
=======================================

Description
---------------------------------------

        The imview task will display images in raster, contour, vector or
        marker form.  Images can be blinked, and movies are available
        for spectral-line image cubes.

        Executing the imview task will bring up a display panel
        window, which can be resized.  If no data file was specified,
        a Load Data window will also appear. Click on the desired data
        file and choose the display type; the rendered data should appear
        on the display panel.

        A Data Display Options window will also appear.  It has drop-down
        subsections for related options, most of which are self-explanatory.

        The state of the imview task -- loaded data and related display
        options -- can be saved in a 'restore' file for later use.
        You can provide the restore filename on the command line or
        select it from the Load Data window.

        It is possible to use the viewer GUI tool to perform image manipulation
        and analysis tasks that are not available from the command-line start.
    


Parameters
---------------------------------------
.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   * - Parameter
     - Default
     - Description
   * - raster
     - :code:`{ }`
     - 
   * - contour
     - :code:`{ }`
     - 
   * - zoom
     - :code:`int(1)`
     - 
   * - axes
     - :code:`{ }`
     - 
   * - out
     - :code:`''`
     - 


Parameter Explanations
=======================================



raster
---------------------------------------

:code:`{ }`

(Optional)  Raster filename (string) or complete raster config dictionary. The allowed dictionary keys are file (string), scaling (numeric), range (2 element numeric vector), colormap (string), and colorwedge (bool).


contour
---------------------------------------

:code:`{ }`

(Optional)  Contour filename (string) or complete contour config dictionary. The allowed dictionary keys are file (string), levels (numeric vector), unit (float), and base (float).


zoom
---------------------------------------

:code:`int(1)`

(Optional)  zoom can specify intermental zoom (integer), zoom region read from a file (string) or dictionary specifying the zoom region. The dictionary can have two forms. It can be either a simple region specified with blc (2 element vector) and trc (2 element vector) [along with an optional coord key ("pixel" or "world"; pixel is the default) or a complete region rectangle e.g. loaded with "rg.fromfiletorecord( )". The dictionary can also contain a channel (integer) field which indicates which channel should be displayed.


axes
---------------------------------------

:code:`{ }`

(Optional)  this can either be a three element vector (string) where each element describes what should be found on each of the x, y, and z axes or a dictionary containing fields "x", "y" and "z" (string).


out
---------------------------------------

:code:`''`

(Optional)  Output filename or complete output config dictionary. If a string is passed, the file extension is used to determine the output type (jpg, pdf, eps, ps, png, xbm, xpm, or ppm). If a dictionary is passed, it can contain the fields, file (string), scale (float), dpi (int), or orient (landscape or portrait). The scale field is used for the bitmap formats (i.e. not ps or pdf) and the dpi parameter is used for scalable formats (pdf or ps).




