

.. _Description:

Description
   The msview task will display a MeasurementSet in raster form. Many
   display and editing options are available. Executing the
   **msview** task will bring up a display panel window, which can be
   re-sized (see below). 
   
   If no data file was specified, a Load Data window will also
   appear. Click on the desired MeasurementSet and the rendered data
   should appear on the display panel. A Data Display Options window
   will also appear. It has drop-down subsections for related
   options, most of which are self-explanatory. 
   
   The state of the **msview** task, i.e. the loaded data and related
   display options, can be saved in a 'restore' file for later
   use. You can provide the restore filename on the command line
   or select it from the Load Data window.
   
   For more detailed on how to use the msview task, please read the
   dedicated CASADocs chapter on `2-D Visualization and Flagging of
   Visibility Data
   (viewer/msview)<../../notebooks/data_examination.ipynb#2-D-Plot/Flag:-viewer/msview>`__.

   
   +---------+-----------------------------------------------------------+
   | Type    | Figure                                                    |
   +---------+-----------------------------------------------------------+
   | ID      | examination-fig-plotants                                  |
   +---------+-----------------------------------------------------------+
   | Caption | Display panel of **msview**, showing the MeasurementSet   |
   |         | when plotting channel against baseline. The color-coding  |
   |         | shows the amplitudes. A variety of data display options   |
   |         | are available.                                            |
   +---------+-----------------------------------------------------------+
   

.. _Examples:

Examples
   .. rubric:: Display a MeasurementSet as a raster image

   ::
   
      # In CASA
      msview(infile='my_MeasurementSet.ms', displaytype='raster')
   
   This displays the MeasurementSet as a raster image. Settings
   (e.g., axes) can then be manually adjusted using the interactive
   Viewer Display Panel. If no *infile* is specified, the Load Data
   window will appear for selecting data.
   
   The parameter *displaytype* (optional) gives the method of
   rendering data visually using one of the following settings:
   raster (default), contour, vector or marker. You can also set this
   parameter to 'lel' to provide a `Lattice Expression
   Language <../../notebooks/image_analysis.html#Lattice-Expression-Language>`__ expression for
   *infile* (advanced).
   

.. _Development:

Development
   No additional development details

