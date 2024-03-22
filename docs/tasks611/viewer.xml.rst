viewer -- View an image or visibility data set -- visualization task
=======================================

Description
---------------------------------------

        The viewer will display images in raster, contour, vector or
        marker form.  Images can be blinked, and movies are available
        for spectral-line image cubes.  For measurement sets, many
        display and editing options are available.

        The viewer can be run outside of casapy by typing <casaviewer>.

        Executing viewer <viewer> will bring up a display panel
        window, which can be resized.  If no data file was specified,
        a Load Data window will also appear. Click on the desired data
        file and choose the display type; the rendered data should appear
        on the display panel.

        A Data Display Options window will also appear.  It has drop-down
        subsections for related options, most of which are self-explanatory.
          
        The state of the viewer -- loaded data and related display
        options -- can be saved in a 'restore' file for later use.
        You can provide the restore filename on the command line or
        select it from the Load Data window.

        See the cookbook for more details on using the viewer.
        
    


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - infile
     - :code:`''`
     - (Optional)  Name of file to visualize.
   * - displaytype
     - :code:`'raster'`
     - (Optional)  Type of visual rendering (raster, contour, vector or marker).  lel  if an lel expression is given for infile  (advanced).
   * - channel
     - :code:`int(0)`
     - (Optional)  access a specific channel in the image cube
   * - zoom
     - :code:`int(1)`
     - (Optional)  zoom in/out by increments
   * - outfile
     - :code:`''`
     - (Optional)  name of the output file to generate
   * - outscale
     - :code:`float(1.0)`
     - (Optional)  amount to scale output bitmap formats (non-PS, non-PDF)
   * - outdpi
     - :code:`int(300)`
     - (Optional)  output DPI for PS/PDF
   * - outformat
     - :code:`'jpg'`
     - (Optional)  format of the output e.g. jpg or pdf (this is overridden by the output files extension
   * - outlandscape
     - :code:`False`
     - (Optional)  should the output mode be landscape (PS or PDF)
   * - gui
     - :code:`True`
     - (Optional)  Display the panel in a GUI.


Parameter Explanations
=======================================



infile
---------------------------------------

:code:`''`

 (Optional)  Name of file to visualize.


displaytype
---------------------------------------

:code:`'raster'`

 (Optional)  Type of visual rendering (raster, contour, vector or marker).  lel  if an lel expression is given for infile  (advanced).


channel
---------------------------------------

:code:`int(0)`

 (Optional)  access a specific channel in the image cube


zoom
---------------------------------------

:code:`int(1)`

 (Optional)  zoom in/out by increments


outfile
---------------------------------------

:code:`''`

 (Optional)  name of the output file to generate


outscale
---------------------------------------

:code:`float(1.0)`

 (Optional)  amount to scale output bitmap formats (non-PS, non-PDF)


outdpi
---------------------------------------

:code:`int(300)`

 (Optional)  output DPI for PS/PDF


outformat
---------------------------------------

:code:`'jpg'`

 (Optional)  format of the output e.g. jpg or pdf (this is overridden by the output files extension


outlandscape
---------------------------------------

:code:`False`

 (Optional)  should the output mode be landscape (PS or PDF)


gui
---------------------------------------

:code:`True`

 (Optional)  Display the panel in a GUI.




