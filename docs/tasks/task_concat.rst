

.. _Description:

Description
   This task concatenates several visibility data sets into a single
   MeasurementSet (MS).

   .. rubric:: Input and output MeasurementSets

   The list of data sets given in the *vis* argument are
   chronologically concatenated into an output data set (named in
   *concatvis*), i.e. the data sets in *vis* are first ordered by the
   time of their earliest integration and then concatenated.
   
   For example, *vis =
   ['src2.ms','ngc5921.ms','ngc315.ms'], concatvis = 'src2.ms'. *
   
   If *concatvis* already exists (e.g., it is the same as the first
   input data set), then the other input data sets will be appended
   to the *concatvis* data set. There is no limit to the number of
   input data sets. If none of the input data sets has any scratch
   columns (model or corrected columns), none is created in the
   *concatvis*. Otherwise these columns are created on output and
   initialized to their default value (1 in model column, data in
   corrected column) for those data with no input scratch columns. 
   
   .. note:: **NOTE**: If the *concatvis* output file exits on disk then the
      input files are added to this file. Otherwise the new file
      contains the concatenated data. Be careful here when
      concatenating to an existing file.

   .. rubric:: Spectral and position shift tolerances

   Spectral windows for each data set with the same channelization
   (equal numbers of channels), and within a specified frequency
   tolerance (parameter *freqtol*) of another data set, will be
   combined into one spectral window. By default, *freqtol* = '',
   which is understood by CASA to be a frequency tolerance of 1 Hz.
   For example, *freqtol = '10MHz'* will not combine spectral
   windows unless they are within 10 MHz of each other. 
   
   .. note:: **NOTE**: This option is useful to combine spectral windows
      with very slight frequency differences caused by Doppler
      tracking, for example.
   
   A field position in one data set that is within a specified
   direction tolerance (parameter *dirtol*) of another field position
   in any other data set will be combined into one field. The field
   names need not be the same -- only their position is used. In
   these cases, the actual direction and field name in the resulting,
   merged output field will be the ones from the
   chronologically-first input MS. Each appended dataset is assigned
   a new observation ID (provided the entries in the observation
   table are indeed different). By default, *dirtol* = '', which is
   understood by CASA to be a position tolerance of 1 milliarcsec
   (mas). For example, *dirtol = '1arcsec'* will not combine fields
   unless their phase centers differ by less than 1 arcsec. If the
   field names are different in the input data sets, the name in the
   output data set will be the first relevant data set in the list.
   Use the parameter *respectname = True * to indicate that fields
   with a different name should not be merged even if their direction
   agrees (within *dirtol*). 
   
   .. note:: **NOTE**: There is no constraint on data that is simultaneously
      observed for more than one field; for example multi-source
      correlation of VLBA data.

   .. rubric:: Operations performed on output MeasurementSets 

   Use the parameter *timesort = True* to sort the output visibility
   table in time. 
   
   Set *copypointing = True* (the default behavior) to make a proper
   copy of the POINTING subtable (though this can be time-consuming).
   If *False*, the result is an empty POINTING table.
   
   The weights of the individual MSs will be scaled in the
   concatenated output MS by the factors in the list given in
   *visweightscale*. SIGMA will be scaled by 1/sqrt(factor). This
   parameter is useful for handling heterogeneous arrays. Use plotms
   to inspect the "Wt" columns as reference for determining the
   scaling factors. For example, *visweightscale* = [1.,3.,3.] will
   scale the weights of the second and third MS by a factor 3 and the
   SIGMA column of these MSs by a factor 1/sqrt(3).
   
   By default, **concat** will only merge two ephemeris fields if the
   first ephemeris covers the time range of the second. Otherwise,
   two separate fields with separate ephemerides are placed in the
   output MS. In order to override this behaviour and
   force **concat** to merge the non-overlapping or only partially
   overlapping input ephemerides, the name or ID of the field in
   question needs to be placed into the list in parameter
   *forcesingleephemfield*. For example, *forcesingleephemfield
   =* ['Neptune'] will make sure that there is only one joint
   ephemeris for field Neptune in the output MS.


.. _Examples:

Examples
   Concatenate 'ngc5921.ms' into 'src2.ms' (the original src2.ms is
   lost):
   
   ::
   
      concat(vis=['src2.ms','ngc5921.ms'], concatvis='src2.ms')
   
   Concatenate 'ngc5921.ms' and 'src2.ms' into a file named 'out.ms'
   (the original 'ngc5921.ms' and 'src2.ms' are untouched):
   
   ::
   
      concat(vis=['src2.ms','ngc5921.ms'], concatvis='out.ms')
   
   Like the previous example but using a direction tolerance
   increased to 0.5 arcsec. Fields whose directions differ by less
   than this limit are merged into one field with the name and
   direction from the chronologically first input MS:
   
   ::
   
      concat(vis=['src2.ms','ngc5921.ms'], concatvis='out.ms',
      dirtol='0.5arcsec')
   
   Concatenate many MSs:
   
   ::
   
      concat(vis=['v1.ms','v2.ms'], concatvis = 'vall.ms') #then
      concat(vis=['v3.ms','v4.ms'], concatvis = 'vall.ms')
   
   vall.ms will contain v1.ms+v2.ms+v3.ms+v4.ms .
   
   .. note:: **NOTE**: Run flagmanager to save flags in the *concatvis.*
   

.. _Development:

Development
   No additional development details

