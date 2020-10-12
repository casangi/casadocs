

.. _Description:

Description
   task viewer description
   
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
   
   .. |image1| image:: _apimedia/c21233cc58158c9088713800a5694cfaf3f94963.png
   

.. _Examples:

Examples
   task examples
   
   To simply create a CASA viewer to set up interactively, you can
   type within CASA:
   
   ::
   
      viewer
   
   To open an image:
   
   ::
   
      viewer "myimage.im"
   
    To open a MeasurementSet:
   
   ::
   
      viewer "mymeasurementset.ms"
   
   To open an image and overlay a contour:
   
   ::
   
      viewer "myimage.im", "contour"
   
   To open a previously saved state of the **viewer**:
   
   ::
   
      viewer "myrestorefile.rstr"
   

.. _Development:

Development
   