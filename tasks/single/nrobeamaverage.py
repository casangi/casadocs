#
# stub function definition file for docstring parsing
#

def nrobeamaverage(infile, datacolumn='float_data', field='', spw='', timerange='', scan='', beam='', timebin='0s', outfile=''):
    """
Average SD data over beams and do time averaging

| The task nrobeamaverage is for Nobeyama dataset of ON-ON observations.
|    It averages on-source spectra having specified beam IDs over specified 
|    time bins.

Parameters
----------
infile : string
   name of input SD dataset
datacolumn : string
   name of data column to be used ["data", "float_data", or "corrected_data"]
field : string
   select data by field IDs and names, e.g. "3C2*" (""=all)
spw : string
   select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all)
timerange : string
   select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)
scan : string
   select data by scan numbers, e.g. "21~23" (""=all)
beam : string
   beam IDs to be averaged over, e.g. "1,3" (""=all)
timebin : string
   bin width for time averaging.
outfile : string
   name of output file

Other Parameters
----------

Notes
-----


msview
======


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
