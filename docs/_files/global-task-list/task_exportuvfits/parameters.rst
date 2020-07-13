Parameters
==========

.. container:: documentDescription description

   task applycal parameters

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               vis : string

            Name of input visibility file Default: none Example:
            vis='ngc5921.ms'

Example

.. container:: param

   .. container:: parameters2

      fitsfile : string

   Name of output UV FITS file Default: none Example:
   vis='ngc5921XC1.fits'

Example

.. container:: param

   .. container:: parameters2

      datacolumn : string = corrected

   Visibility file data column Default: corrected Options:
   'data'(raw)|'corrected'|'model'|'weight' Example: datacolumn='model'

Allowed Value(s)

data corrected model weight

Example

.. container:: param

   .. container:: parameters2

      field : string stringArray int intArray

   Select field using field id(s) or field name(s) Default: '' --> all
   fields Use 'go listobs' to obtain the list id's or names. If field
   string is a non-negative integer, it is assumed a field index,
   otherwise, it is assumed a field name. Examples: field='0~2'; field
   ids 0,1,2 field='0,4,5~7'; field ids 0,4,5,6,7 field='3C286,3C295';
   field named 3C286 and 3C295 field = '3,4C*'; field id 3, all names
   starting with 4C

Example

.. container:: param

   .. container:: parameters2

      spw : string

   Select spectral window/channels Examples: spw='0~2,4'; spectral
   windows 0,1,2,4 (all channels) spw='<2'; spectral windows less than 2
   (i.e. 0,1) spw='0:5~61'; spw 0, channels 5 to 61, INCLUSIVE
   spw='*:5~61'; all spw with channels 5 to 61 spw='0,10,3:3~45'; spw
   0,10 all channels, spw 3, channels 3 to 45. spw='0~2:2~6'; spw 0,1,2
   with channels 2 through 6 in each. spw='0:0~10;15~60'; spectral
   window 0 with channels 0-10,15-60. (NOTE ';' to separate channel
   selections) spw='0:0~10^2,1:20~30^5'; spw 0, channels 0,2,4,6,8,10,
   spw 1, channels 20,25,30 type 'help par.selection' for more examples.

Example

.. container:: param

   .. container:: parameters2

      antenna : string

   Select data based on antenna/baseline Subparameter of selectdata=True
   Default: '' (all) If antenna string is a non-negative integer, it is
   assumed an antenna index, otherwise, it is assumed as an antenna name
   Examples: antenna='5&6'; baseline between antenna index 5 and index
   6. antenna='VA05&VA06'; baseline between VLA antenna 5 and 6.
   antenna='5&6;7&8'; baselines with indices 5-6 and 7-8 antenna='5';
   all baselines with antenna index 5 antenna='05'; all baselines with
   antenna number 05 (VLA old name) antenna='5,6,10'; all baselines with
   antennas 5,6,10 index numbers

Example

.. container:: param

   .. container:: parameters2

      timerange : string

   Select data based on time range Subparameter of selectdata=True
   Default = '' (all) Examples: timerange =
   'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss' (Note: if YYYY/MM/DD is
   missing date defaults to first day in data set.)
   timerange='09:14:0~09:54:0' picks 40 min on first day timerange=
   '25:00:00~27:30:00' picks 1 hr to 3 hr 30min on NEXT day
   timerange='09:44:00' pick data within one integration of time
   timerange='>10:24:00' data after this time

Example

.. container:: param

   .. container:: parameters2

      writesyscal : bool = False

   Write GC and TY tables. Not yet available. Default: False

Example

.. container:: param

   .. container:: parameters2

      multisource : bool = True

   Write in multi-source format? Default: True Set to False if only one
   source is selected. Note: diffmap does not work on multisource uvfits
   files, so if planning on using diffmap on the resulting uvfits file,
   select a single source and set multisource = False. Otherwise use
   True. (If multiple sources are selected, a multi-source file will be
   written no matter what the setting of this parameter).

Example

.. container:: param

   .. container:: parameters2

      combinespw : bool = True

   Export the spectral windows as IFs? Default: True If True, export the
   spectral windows as IFs. All spectral windows must have same shape.
   Otherwise multiple windows will use multiple FREQIDs.

Example

.. container:: param

   .. container:: parameters2

      writestation : bool = True

   Write station name instead of antenna name Default: True

Example

.. container:: param

   .. container:: parameters2

      padwithflags : bool = False

   Fill in missing data with flags to fit IFs Subparameter of
   combinespw=True Default: True If True, and combinespw is True, fill
   in missing data as needed to fit the IF structure. This is
   appropriate if the MS had a few frequency-dependent flags applied,
   and was then time-averaged by split, or when exporting for use by
   difmap. If the spectral windows were observed at different times,
   padwithflags=True will add a large number of flags, making the output
   file significantly longer. It does not yet support spectral windows
   with different widths.

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   Overwrite output file if it exists? Default: False Options:
   False|True

Example

.. container:: section
   :name: viewlet-below-content-body
