

.. _Description:

Description
   This is primarily designed for importing AIPS data into CASA, but
   also works for other UVFITS data (e.g., MIRIAD).
   
   The current UVFITS specification can be found in `AIPS Memo
   117 <https://library.nrao.edu/public/memos/aips/memos/AIPSM_117.pdf>`__.
   
   The *antnamescheme* parameter specifies the naming scheme for
   VLA/JVLA/CARMA antennas. The default is "old". For "old", antnnea
   names are numerical, eg "04". This option exists for backwards
   compatibility but can lead to ambiguous results when antenna
   indices are used for data selection. When set to "new", Antenna
   names are not strictly numerical, eg "VA04" or "EA04". With this
   scheme, data selection via antenna names and indices is
   non-ambiguous.
   
   A NOTE ON WEIGHTS: **importuvfits** will generate a
   WEIGHT_SPECTRUM column in which it will fill the absolute value of
   the weight associated with each visibility in the uvfits file.
   Negative weights will have the associated FLAGs set to True. It
   will compute the associated WEIGHT value for that MS row to be the
   sum of the absolute values of the associated WEIGHT_SPECTRUM
   values. 
   
   .. warning:: Importing of MSs with Nant>255 via **importuvfits** should be considered experimental and datasets transported this way may not behave as expected in other packages (e.g., AIPS).  
   
   .. note:: Remember to flag the autocorrelations if you do not want them, using the
      task **flagdata** with parameter *autocorr = true*
   

.. _Examples:

Examples
   ::
   
      importuvfits(fitsfile="my.uvfits", vis="my.ms")
   

.. _Development:

Development
   No additional development details

