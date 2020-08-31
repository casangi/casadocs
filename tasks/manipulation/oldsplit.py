#
# stub function definition file for docstring parsing
#

def oldsplit(vis, outputvis='', datacolumn='corrected', field='', spw='', width='1', antenna='', timebin='0s', timerange='', array='', uvrange='', scan='', intent='', correlation='', observation='', combine='', keepflags=True, keepmms=False):
    r"""
Create a visibility subset from an existing visibility set

Parameters
   - **vis** (string) - Name of input measurement set
   - **outputvis** (string) - Name of output measurement set
   - **datacolumn** (string) - Data column(s) to Oldsplit out
   - **field** (string, stringArray, int, intArray) - Select field using ID(s) or name(s)
   - **spw** (string, stringArray, int, intArray) - Select spectral window/channels
   - **width** (string, stringArray, int, intArray) - Number of channels to average to form one output channel
   - **antenna** (string, stringArray, int, intArray) - Select data based on antenna/baseline
   - **timebin** (string) - Interval for time averaging
   - **timerange** (string) - Select data by time range
   - **array** (string) - Select (sub)array(s) by array ID number
   - **uvrange** (string) - Select data by baseline length (default units meters)
   - **scan** (string) - Select data by scan numbers
   - **intent** (string) - Select data by scan intents
   - **correlation** (string, stringArray) - Select correlations
   - **observation** (string, int) - Select by observation ID(s)
   - **keepflags** (bool) - If practical, keep *completely flagged rows* instead of dropping them.
   - **keepmms** (bool) - If the input is a multi-MS, make the output one,too.

Subparameters
   .. raw:: html

      <details><summary><i> timebin != 0s </i></summary>

   - **combine** (string='', stringArray) - Let time bins span changes in scan and/or stat

   .. raw:: html

      </details>


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
