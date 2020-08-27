#
# stub function definition file for docstring parsing
#

def viewer(infile, displaytype='raster', channel=0, zoom=1, outfile='', outscale=1.0, outdpi=300, outformat='jpg', outlandscape=False, gui=True):
    """
View an image or visibility data set

| The viewer will display images in raster, contour, vector or
|        marker form.  Images can be blinked, and movies are available
|        for spectral-line image cubes.  For measurement sets, many
|        display and editing options are available.
|
|        The viewer can be run outside of casapy by typing <casaviewer>.
|
|        Executing viewer <viewer> will bring up a display panel
|        window, which can be resized.  If no data file was specified,
|        a Load Data window will also appear. Click on the desired data
|        file and choose the display type; the rendered data should appear
|        on the display panel.
|
|        A Data Display Options window will also appear.  It has drop-down
|        subsections for related options, most of which are self-explanatory.
|          
|        The state of the viewer -- loaded data and related display
|        options -- can be saved in a 'restore' file for later use.
|        You can provide the restore filename on the command line or
|        select it from the Load Data window.
|
|        See the cookbook for more details on using the viewer.

Parameters
----------
infile : string
    (Optional)  Name of file to visualize.
displaytype : string
    (Optional)  Type of visual rendering (raster, contour, vector or marker).  lel  if an lel expression is given for infile  (advanced).
channel : int
    (Optional)  access a specific channel in the image cube
zoom : int
    (Optional)  zoom in/out by increments
outfile : string
    (Optional)  name of the output file to generate
outscale : double
    (Optional)  amount to scale output bitmap formats (non-PS, non-PDF)
outdpi : int
    (Optional)  output DPI for PS/PDF
outformat : string
    (Optional)  format of the output e.g. jpg or pdf (this is overridden by the output files extension
outlandscape : bool
    (Optional)  should the output mode be landscape (PS or PDF)
gui : bool
    (Optional)  Display the panel in a GUI.

Other Parameters
----------

Notes
-----





   



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
      Visualization <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization>`__ and
      `Data Examination and
      Editing <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing>`__
      chapters in CASAdocs for (many) more details on using the
      **viewer** to display images and MSes.

       

      |image1|

      ======= ===============
      Type    Figure
      ID      1
      Caption The CASA viewer
      ======= ===============

.. |image1| image:: ../../_media/c21233cc58158c9088713800a5694cfaf3f94963.png
   :class: image-inline

    """
    pass
