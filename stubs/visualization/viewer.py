#
# stub function definition file for docstring parsing
#

def viewer(infile, displaytype='raster', channel=0, zoom=1, outfile='', outscale=1.0, outdpi=300, outformat='jpg', outlandscape=False, gui=True):
    r"""
View an image or visibility data set

Parameters
   - infile_ (string) -  (Optional)  Name of file to visualize.
   - displaytype_ (string='raster') -  (Optional)  Type of visual rendering (raster, contour, vector or marker).  lel  if an lel expression is given for infile  (advanced).
   - channel_ (int=0) -  (Optional)  access a specific channel in the image cube
   - zoom_ (int=1) -  (Optional)  zoom in/out by increments
   - outfile_ (string='') -  (Optional)  name of the output file to generate
   - outscale_ (double=1.0) -  (Optional)  amount to scale output bitmap formats (non-PS, non-PDF)
   - outdpi_ (int=300) -  (Optional)  output DPI for PS/PDF
   - outformat_ (string='jpg') -  (Optional)  format of the output e.g. jpg or pdf (this is overridden by the output files extension
   - outlandscape_ (bool=False) -  (Optional)  should the output mode be landscape (PS or PDF)
   - gui_ (bool=True) -  (Optional)  Display the panel in a GUI.


Description
   Displays images, data cubes and MeasurementSets.

   The **viewer** will display images in raster, contour, vector or
   marker form. Images can be blinked, and movies are available for
   spectral-line image cubes. For MeasurementSets, many display and
   editing options are available.

   The **viewer** can be run by typing viewer within CASA, or
   casaviewer outside of CASA. Executing **viewer** will bring up a
   display panel window, which can be resized. If no data file was
   specified, a Load Data window will also appear. Click on the
   desired data file and choose the display type; the rendered data
   should appear on the display panel. A Data Display Options window
   will also appear. It has drop-down subsections for related
   options, most of which are self-explanatory.

   The loaded data and related display options can be saved in a
   'restore' file for later use. You can provide the restore filename
   on the command line or select it from the Load Data window.

   See the `Image Cube
   Visualization <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization>`__and
   `Data Examination and
   Editing <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing>`__
   chapters in CASAdocs for (many) more details on using the
   **viewer**to display images and MSes.

   

   |image1|

   ======= ===============
   Type    Figure
   ID      1
   Caption The CASA viewer
   ======= ===============

.. |image1| image:: docs/tasks/_apimedia/c21233cc58158c9088713800a5694cfaf3f94963.png
:class: image-inline




Details
   Explanation of each parameter

.. _infile:

   .. rubric:: infile

   | (Optional)  Name of file to visualize.

.. _displaytype:

   .. rubric:: displaytype

   | (Optional)  Type of visual rendering (raster, contour, vector or marker).  lel  if an lel expression is given for infile  (advanced).

.. _channel:

   .. rubric:: channel

   | (Optional)  access a specific channel in the image cube

.. _zoom:

   .. rubric:: zoom

   | (Optional)  zoom in/out by increments

.. _outfile:

   .. rubric:: outfile

   | (Optional)  name of the output file to generate

.. _outscale:

   .. rubric:: outscale

   | (Optional)  amount to scale output bitmap formats (non-PS, non-PDF)

.. _outdpi:

   .. rubric:: outdpi

   | (Optional)  output DPI for PS/PDF

.. _outformat:

   .. rubric:: outformat

   | (Optional)  format of the output e.g. jpg or pdf (this is overridden by the output files extension

.. _outlandscape:

   .. rubric:: outlandscape

   | (Optional)  should the output mode be landscape (PS or PDF)

.. _gui:

   .. rubric:: gui

   | (Optional)  Display the panel in a GUI.


    """
    pass
