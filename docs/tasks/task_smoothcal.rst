

.. _Description:

Description
   The **smoothcal** task will smooth calibration solutions (most
   usefully 'G' or 'T') over a specified time interval to reduce
   noise and outliers. Flagged solutions will be unflagged and
   replaced with smoothed solutions if unflagged solutions are
   available within the smoothing window. Smoothing will be applied
   per field and per spw; these cannot be combined.

   
   .. rubric:: Parameter Descriptions
   
   Input/output: *vis, tablein, caltable*
   
   Specify the relevant MS in *vis* (for meta-info purposes; will
   someday deprecate), and the input calibration table in *tablein*.
   Specify the output (smoothed) calibration table name in
   *caltable*. If *caltable* is left unspecified, the input
   calibration table (*tablein*) will be overwritten with the
   smoothed result.
   
   Selection: *field*
   
   Specify the subset of fields to be smoothed in *field*. All fields
   wil be copied to the new calibration table, but only the specified
   fields will be smoothed.
   
   Smoothing parameters: *smoothtype, smoothtime*
   
   Specify the smoothing type, 'mean' or 'median' in *smoothtype*.
   The timescale (the boxcar width) over which the smooth operation
   is applied should be specified in *smoothtime*, in seconds.
   Amplitude and phase will each be (separately) smoothed with the
   specified *smoothtype* and *smoothtime*. Currently, it is not
   possible to smooth amplitude and phase with different values
   of *smoothtype* or *smoothtime.*

   Experimental rate smoothing parameter: *ratesmooth*

   When smoothing on fringefit solutions setting this to True
   will use the rates to assist in detecting phase cycles.
   The rates present will be smoothed with the specified smooth time.
   This is currently an experimental feature.
   

.. _Examples:

Examples
   To smooth the caltable 'n4826_16apr.gcal' on a 3-hour timescale
   with a boxcar mean:
   
   ::
   
      smoothcal(vis='n4826_16apr.ms',
                tablein='n4826_16apr.gcal',
                caltable='n4826_16apr.smoothcal',
                smoothtime=7200.,
                smoothtype='mean')
   
   
   Results can be plotted with **plotms**.


.. _Development:

Development
   No additional development details

