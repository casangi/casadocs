#
# stub function definition file for docstring parsing
#

def msview(infile, displaytype='raster', channel=0, zoom=1, outfile='', outscale=1.0, outdpi=300, outformat='jpg', outlandscape=False, gui=True):
    r"""
View a visibility data set

Parameters
   - infile_ (string)
   - displaytype_ (string='raster')
   - channel_ (int=0)
   - zoom_ (int=1)
   - outfile_ (string='')
   - outscale_ (double=1.0)
   - outdpi_ (int=300)
   - outformat_ (string='jpg')
   - outlandscape_ (bool=False)
   - gui_ (bool=True)


Description
   The msview task will display a MeasurementSet in raster form.Many
   display and editing options are available.Executing the
   **msview** task will bring up a display panelwindow, which can be
   re-sized (see below).

   If no data file was specified,a Load Data window will also
   appear. Click on the desired MeasurementSet and the rendered data
   should appear on the display panel.A Data Display Options window
   will also appear. It has drop-downsubsections for related
   options, most of which are self-explanatory.

   The state of the **msview** task, i.e. the loaded data and related
   displayoptions, can be saved in a 'restore' file for later
   use.You can provide the restore filename on the command line
   orselect it from the Load Data window.

   For more detailed on how to use the msview task, please read the
   dedicated CASADocs chapter on `2-D Visualization and Flagging of
   Visibility Data
   (viewer/msview) <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing/2-d-visualization-of-visibility-data-msview>`__.

   

   

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


.. _infile:

infile (string)
   | (Optional)  Name of file to visualize.

.. _displaytype:

displaytype (string='raster')
   | (Optional)  Type of visual rendering (raster, contour, vector or marker).  lel  if an lel expression is given for infile  (advanced).

.. _channel:

channel (int=0)
   | (Optional)  access a specific channel in the image cube

.. _zoom:

zoom (int=1)
   | (Optional)  zoom in/out by increments

.. _outfile:

outfile (string='')
   | (Optional)  name of the output file to generate

.. _outscale:

outscale (double=1.0)
   | (Optional)  amount to scale output bitmap formats (non-PS, non-PDF)

.. _outdpi:

outdpi (int=300)
   | (Optional)  output DPI for PS/PDF

.. _outformat:

outformat (string='jpg')
   | (Optional)  format of the output e.g. jpg or pdf (this is overridden by the output files extension

.. _outlandscape:

outlandscape (bool=False)
   | (Optional)  should the output mode be landscape (PS or PDF)

.. _gui:

gui (bool=True)
   | (Optional)  Display the panel in a GUI.


    """
    pass
