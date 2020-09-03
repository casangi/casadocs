#
# stub function definition file for docstring parsing
#

def smoothcal(vis, tablein, caltable='', field=[''], smoothtype='median', smoothtime=60.0):
    r"""
Smooth calibration solution(s) derived from one or more sources:

Parameters
   - **vis** (string) - Name of input visibility file (MS)
   - **tablein** (string) - Input calibration table
   - **caltable** (string='') - Output calibration table (overwrite tablein if unspecified)
   - **field** (stringArray=['']) - Field name list
   - **smoothtype** (string='median') - Smoothing filter to use
   - **smoothtime** ({double, int}=60.0) - Smoothing time (sec)


Description
   .. rubric:: Summary
      

   The **smoothcal** task will smooth calibration solutions (most
   usefully 'G' or 'T') over a specified time interval to reduce
   noise and outliers. Flagged solutions will be unflagged and
   replaced with smoothed solutions if unflagged solutions are
   available within the smoothing window. Smoothing will be applied
   per field and per spw; these cannot be combined.

   

   .. rubric:: Parameter Descriptions
      

   .. rubric:: Input/output: *vis, tablein, caltable*
      

   Specify the relevant MS in *vis* (for meta-info purposes; will
   someday deprecate), and the input calibration table in *tablein*.
   Specify the output (smoothed) calibration table name in
   *caltable*. If *caltable* is left unspecified, the input
   calibration table (*tablein*) will be overwritten with the
   smoothed result.

   .. rubric:: Selection: *field*
      

   Specify the subset of fields to be smoothed in *field*. All fields
   wil be copied to the new calibration table, but only the specified
   fields will be smoothed.

   .. rubric:: Smoothing parameters: *smoothtype, smoothtime*
      

   Specify the smoothing type, 'mean' or 'median' in *smoothtype*.
   The timescale (the boxcar width) over which the smooth operation
   is applied should be specified in *smoothtime*, in seconds.
   Amplitude and phase will each be (separately) smoothed with the
   specified *smoothtype* and *smoothtime*. Currently, it is not
   possible to smooth amplitude and phase with different values
   of*smoothtype*or *smoothtime.*

    """
    pass
