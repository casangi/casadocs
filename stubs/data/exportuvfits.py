#
# stub function definition file for docstring parsing
#

def exportuvfits(vis, fitsfile='', datacolumn='corrected', field='', spw='', antenna='', timerange='', writesyscal=False, multisource=True, combinespw=True, writestation=True, padwithflags=False, overwrite=False):
    r"""
Convert a CASA visibility data set to a UVFITS file:

Parameters
   - vis_ (string) - Name of input visibility file
   - fitsfile_ (string='') - Name of output UV FITS file
   - datacolumn_ (string='corrected') - Visibility file data column
   - field_ ({string, stringArray, int, intArray}='') - Select field using field id(s) or field name(s)
   - spw_ (string='') - Select spectral window/channels
   - antenna_ (string='') - Select data based on antenna/baseline
   - timerange_ (string='') - Select data based on time range
   - writesyscal_ (bool=False) - Write GC and TY tables (not yet available)
   - multisource_ (bool=True) - Write in multi-source format?
   - combinespw_ (bool=True) - Export the spectral windows as IFs

      .. raw:: html

         <details><summary><i> combinespw = True </i></summary>

      - padwithflags_ (bool=False) - Fill in missing data with flags to fit IFs

      .. raw:: html

         </details>
   - writestation_ (bool=True) - Write station name instead of antenna name
   - overwrite_ (bool=False) - Overwrite output file if it exists?


Description
   The task **exportuvfits** takes a MeasurementSet and exports it to
   a UVFITS format file.

   UVFITS is a general format dataset used to transfer data between
   different software systems. In CASA, exportuvfits is mainly
   developed to transfer data from CASA to AIPS, but it also serves
   the UVFITS format used in other software packages (e.g., MIRIAD).
   A UVFITS file is written in floating point format.
   **exportuvfits** accepts a number of parameters that can control
   what is written out (see e.g. the *spw*, *multisource*,
   *combinespw* parameter descriptions).

   .. warning:: **WARNING:** Some external software packages (e.g., GILDAS)
      cannot easily read CASA UVFITS files when more than one
      spectral window are exported in exportuvfits. In those cases,
      please export a single spectral window at a time by setting the
      *‘spw’* parameter.

   The parameters of *field*, *spw*, *antenna*, and *timerange*
   select the data that are exported from the MS dataset. The
   *datacolumn* parameter chooses which data-containing column of the
   MS is to be written out to the UVFITS file. Choices are: '*data*',
   '*corrected*', '*model*', and '*weight*'.

   The *multisource* parameter determines whether the UVFITS file is
   a multi-source file or a single-source file, if you have a
   single-source MS or choose only a single source. Multi-source
   UVFITS files have multiple source IDs in the source (SU) table.
   Some programs (i.e. difmap) only accept single-source format
   files. Note that if you select more than one source in *field*,
   then the *multisource* parameter will be overridden to be *True*
   regardless.

   MSes where the tuning changed with time should be exported to
   multiple UVFITS files using *spw* to select one tuning (set of
   simultaneous spectral windows) per file (e.g. 10 minutes at 4.8
   GHz followed by 15 minutes at 8.4 GHz).

   The *combinespw* parameter allows combination of all spectral
   windows at one time. If *True*, then all spectral windows must
   have the same shape. In other words, they should have the same
   number of channels and polarizations, and each channel must have
   the same width, and each IF (Intermediate Frequency) must be
   present (even if flagged) throughout the entire observation. If
   these conditions are met, all spectral windows are exported as a
   set of IFs in a single FREQID setup instead of giving each
   spectral window its own FREQID in the FITS file. (IF and FREQID
   are the identification number of a spectral window and the
   spectral set up of a baseband in the FITS file, respectively.) If
   these conditions are not met the data must be exported using
   multiple FREQIDs, the UVFITS equivalent of a general spectral
   window. This matters since many (sub)programs will work with
   multiple IFs, but not multiple FREQIDs. For example, a UVFITS file
   with multiple FREQIDs can be read by AIPS, but you may find that
   you have to separate the FREQIDs with **split** before you can do
   very much with them.

   You can fill in missing data as needed to fit the IF structure
   using *padwithflags* option. To do that, not only set
   *padwithflags* =True, but also *combinespw=* True. This is
   appropriate if the MS had a few frequency-dependent flags applied,
   and was then time-averaged by split, or when exporting for use by
   difmap. If the spectral windows were observed at different times,
   *padwithflags* =True will add a large number of flags, making the
   output file significantly longer. It does not yet support
   spectral windows with different widths.

   It is recommended to perform any required data averaging using
   other tasks (e.g., **split** or**mstransform**) before exporting
   the UVFITS file with **exportuvfits**.

   A NOTE ON WEIGHTS: If the MS has no WEIGHT_SPECTRUM column, or if
   it does but that column contains no data, **exportuvfits** will
   compute for each visibility the weight it writes to the UVFITS
   file by dividingthe associated WEIGHT column value in the MS by
   the number of channels in the relevantspectral window within
   which that visibility is located.

   Optionally, the parameter *overwrite* can be use to overwrite
   existing uvfits files with the same name as that specified in the
   *fitsfile* parameter.


.. _vis:

vis (string)
   | Name of input visibility file
   |                      Default: none
   | 
   |                         Example: vis='ngc5921.ms'

.. _fitsfile:

fitsfile (string='')
   | Name of output UV FITS file
   |                      Default: none
   | 
   |                         Example: vis='ngc5921XC1.fits'

.. _datacolumn:

datacolumn (string='corrected')
   | Visibility file data column
   |                      Default: corrected
   |                      Options: 'data'(raw)|'corrected'|'model'|'weight'
   | 
   |                         Example: datacolumn='model'

.. _field:

field ({string, stringArray, int, intArray}='')
   | Select field using field id(s) or field name(s)
   |                      Default: '' --> all fields
   |                      
   |                      Use 'go listobs' to obtain the list id's or
   |                      names. If field string is a non-negative integer,
   |                      it is assumed a field index,  otherwise, it is
   |                      assumed a field name.
   | 
   |                         Examples:
   |                         field='0~2'; field ids 0,1,2
   |                         field='0,4,5~7'; field ids 0,4,5,6,7
   |                         field='3C286,3C295'; field named 3C286 and
   |                         3C295
   |                         field = '3,4C*'; field id 3, all names
   |                         starting with 4C

.. _spw:

spw (string='')
   | Select spectral window/channels
   | 
   |                         Examples:
   |                         spw='0~2,4'; spectral windows 0,1,2,4 (all
   |                         channels)
   |                         spw='<2';  spectral windows less than 2
   |                         (i.e. 0,1)
   |                         spw='0:5~61'; spw 0, channels 5 to 61,
   |                         INCLUSIVE
   |                         spw='*:5~61'; all spw with channels 5 to 61
   |                         spw='0,10,3:3~45'; spw 0,10 all channels, spw
   |                         3, channels 3 to 45.
   |                         spw='0~2:2~6'; spw 0,1,2 with channels 2
   |                         through 6 in each.
   |                         spw='0:0~10;15~60'; spectral window 0 with
   |                         channels 0-10,15-60. (NOTE ';' to separate
   |                         channel selections)
   |                         spw='0:0~10^2,1:20~30^5'; spw 0, channels
   |                         0,2,4,6,8,10, spw 1, channels 20,25,30 
   |                         type 'help par.selection' for more examples.

.. _antenna:

antenna (string='')
   | Select data based on antenna/baseline
   |                      Subparameter of selectdata=True
   |                      Default: '' (all)
   | 
   |                      If antenna string is a non-negative integer, it
   |                      is assumed an antenna index, otherwise, it is
   |                      assumed as an antenna name
   |   
   |                          Examples: 
   |                          antenna='5&6'; baseline between antenna
   |                          index 5 and index 6.
   |                          antenna='VA05&VA06'; baseline between VLA
   |                          antenna 5 and 6.
   |                          antenna='5&6;7&8'; baselines with
   |                          indices 5-6 and 7-8
   |                          antenna='5'; all baselines with antenna index
   |                          5
   |                          antenna='05'; all baselines with antenna
   |                          number 05 (VLA old name)
   |                          antenna='5,6,10'; all baselines with antennas
   |                          5,6,10 index numbers

.. _timerange:

timerange (string='')
   | Select data based on time range
   |                      Subparameter of selectdata=True
   |                      Default = '' (all)
   | 
   |                         Examples:
   |                         timerange =
   |                         'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
   |                         (Note: if YYYY/MM/DD is missing date defaults
   |                         to first day in data set.)
   |                         timerange='09:14:0~09:54:0' picks 40 min on
   |                         first day 
   |                         timerange= '25:00:00~27:30:00' picks 1 hr to 3
   |                         hr 30min on NEXT day
   |                         timerange='09:44:00' pick data within one
   |                         integration of time
   |                         timerange='>10:24:00' data after this time

.. _writesyscal:

writesyscal (bool=False)
   | Write GC and TY tables. Not yet available.
   |                      Default: False

.. _multisource:

multisource (bool=True)
   | Write in multi-source format? 
   |                      Default: True
   | 
   |                      Set to False if only one source is selected. 
   | 
   |                      Note: diffmap does not work on multisource uvfits
   |                      files, so if planning on using diffmap on the
   |                      resulting uvfits file, select a single source and
   |                      set multisource = False. Otherwise use True. (If
   |                      multiple sources are selected, a multi-source
   |                      file will be written no matter what the setting
   |                      of this parameter).

.. _combinespw:

combinespw (bool=True)
   | Export the spectral windows as IFs?
   |                      Default: True
   | 
   |                      If True, export the spectral windows as
   |                      IFs. All spectral windows must have same
   |                      shape. Otherwise multiple windows will use
   |                      multiple FREQIDs.

.. _writestation:

writestation (bool=True)
   | Write station name instead of antenna name
   |                      Default: True

.. _padwithflags:

padwithflags (bool=False)
   | Fill in missing data with flags to fit IFs
   |                      Subparameter of combinespw=True
   |                      Default: True
   |                      
   |                      If True, and combinespw is True, fill in missing
   |                      data as needed to fit the IF structure. This is
   |                      appropriate if the MS had a few
   |                      frequency-dependent flags applied, and was then
   |                      time-averaged by split, or when exporting for use
   |                      by difmap. If the spectral windows were observed
   |                      at different times, padwithflags=True will add a
   |                      large number of flags, making the output file
   |                      significantly longer. It does not yet support
   |                      spectral windows with different widths.

.. _overwrite:

overwrite (bool=False)
   | Overwrite output file if it exists?
   |                      Default: False
   |                      Options: False|True


    """
    pass
