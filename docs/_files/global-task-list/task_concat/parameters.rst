.. container::
   :name: viewlet-above-content-title

Parameters
==========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task concat parameters

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               vis : stringArray

            Name of input visibility file default: none Example:
            vis='['src2.ms','ngc5921.ms','ngc315.ms']

Example

.. container:: param

   .. container:: parameters2

      concatvis : string

   Name of visibility file that will contain the concatenated data
   default: none Example: concatvis='outvis.ms' Note: if this file exits
   on disk then the input files are added to this file. Otherwise the
   new file contains the concatenated data. Be careful here when
   concatenating to an existing file.

Example

.. container:: param

   .. container:: parameters2

      freqtol : undefined

   Frequency shift tolerance for considering data as the same spwid. The
   number of channels must also be the same. Default: '' == 1 Hz
   Example: freqtol='10MHz' will not combine spwid unless they are
   within 10 MHz. Note: This option is useful to combine spectral
   windows with very slight frequency differences caused by Doppler
   tracking, for example.

Example

.. container:: param

   .. container:: parameters2

      dirtol : undefined

   Direction shift tolerance for considering data as the same field
   Default: '' == 1 mas (milliarcsec) Example: dirtol='1arcsec' will not
   combine data for a field unless their phase center differ by less
   than 1 arcsec. Note: If the field names are different in the input
   data sets, the name in the output data set will be the first relevant
   data set in the list.

Example

.. container:: param

   .. container:: parameters2

      respectname : bool = False

   If true, fields with a different name are not merged even if their
   direction agrees (within dirtol) Default: False

Example

.. container:: param

   .. container:: parameters2

      timesort : bool = False

   If true, sort by TIME in ascending order Default: False (data in
   order as read in) Example: timesort=True Note: There is no constraint
   on data that is simultaneously observed for more than one field; for
   example multi-source correlation of VLBA data.

Example

.. container:: param

   .. container:: parameters2

      copypointing : bool = True

   Make a proper copy of the POINTING subtable Default:True (can be time
   consuming!) If False, the result is an empty POINTING table.

Example

.. container:: param

   .. container:: parameters2

      visweightscale : doubleArray

   List of the weight scaling factors to be applied to the individual
   MSs Default: [] (empty list) - no scaling The weights of the
   individual MSs will be scaled in the concatenated output MS by the
   factors in this list. SIGMA will be scaled by 1/sqrt(factor). Useful
   for handling heterogeneous arrays. Use plotms to inspect the "Wt"
   column as a reference for determining the scaling factors. Example:
   [1.,3.,3.] - scale the weights of the second and third MS by a factor
   3 and the SIGMA column of these MS by a factor 1/sqrt(3).

Example

.. container:: param

   .. container:: parameters2

      forcesingleephemfield : undefined

   Make sure that there is only one joint ephemeris for every field in
   this list Default: '' (standard treatment of all ephemeris fields) By
   default, concat will only merge two ephemeris fields if the first
   ephemeris covers the time range of the second. Otherwise, two
   separate fields with separate ephemerides are placed in the output
   MS. In order to override this behaviour and make concat merge the
   non-overlapping or only partially overlapping input ephemerides, the
   name or id of the field in question needs to be placed into the list
   in parameter 'forcesingleephemfield'. Example: ['Neptune'] - will
   make sure that there is only one joint ephemeris for field Neptune in
   the output MS

Example

.. container:: section
   :name: viewlet-below-content-body
