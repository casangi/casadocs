.. container::
   :name: viewlet-above-content-title

Description
===========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   importuvfits task: Convert a UVFITS file to a CASA measurement set

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Convert a UVFITS file to a CASA visibility data set.

      This is primarily designed for importing AIPS data into CASA, but
      also works for other UVFITS data (e.g., MIRIAD).

      The current UVFITS specification can be found in `AIPS Memo
      117 <ftp://ftp.aoc.nrao.edu/pub/software/aips/TEXT/PUBL/AIPSMEM117.PS>`__.

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

      .. container:: info-box

         **NOTE**: Don't forget to flag autocorrections using the
         task **flagdata**, *autocorr = true*

.. container:: section
   :name: viewlet-below-content-body
