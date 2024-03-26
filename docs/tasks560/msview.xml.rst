msview -- View a visibility data set -- utility, visualization, editing task
=======================================

Description
---------------------------------------

        The msview task will display measurements in raster form.
        Many display and editing options are available.

        Executing the msview task will bring up a display panel
        window, which can be resized.  If no data file was specified,
        a Load Data window will also appear. Click on the desired measurement
        set,and the rendered data should appear on the display panel.

        A Data Display Options window will also appear.  It has drop-down
        subsections for related options, most of which are self-explanatory.

        The state of the msview task -- loaded data and related display
        options -- can be saved in a 'restore' file for later use.
        You can provide the restore filename on the command line or
        select it from the Load Data window.

        See the cookbook for more details on using the msview task.

    


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
     - 
   * - displaytype
     - :code:`'raster'`
     - 
   * - channel
     - :code:`int(0)`
     - 
   * - zoom
     - :code:`int(1)`
     - 
   * - outfile
     - :code:`''`
     - 
   * - outscale
     - :code:`float(1.0)`
     - 
   * - outdpi
     - :code:`int(300)`
     - 
   * - outformat
     - :code:`'jpg'`
     - 
   * - outlandscape
     - :code:`False`
     - 
   * - gui
     - :code:`True`
     - 


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




