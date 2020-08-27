#
# stub function definition file for docstring parsing
#

def msview(infile, displaytype='raster', channel=0, zoom=1, outfile='', outscale=1.0, outdpi=300, outformat='jpg', outlandscape=False, gui=True):
    """
View a visibility data set

| The msview task will display measurements in raster form.
|        Many display and editing options are available.
|
|        Executing the msview task will bring up a display panel
|        window, which can be resized.  If no data file was specified,
|        a Load Data window will also appear. Click on the desired measurement
|        set,and the rendered data should appear on the display panel.
|
|        A Data Display Options window will also appear.  It has drop-down
|        subsections for related options, most of which are self-explanatory.
|
|        The state of the msview task -- loaded data and related display
|        options -- can be saved in a 'restore' file for later use.
|        You can provide the restore filename on the command line or
|        select it from the Load Data window.
|
|        See the cookbook for more details on using the msview task.

Parameters
----------
infile : string
   
displaytype : string
   
channel : int
   
zoom : int
   
outfile : string
   
outscale : double
   
outdpi : int
   
outformat : string
   
outlandscape : bool
   
gui : bool
   

Other Parameters
----------

Notes
-----





   task description



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

    """
    pass
