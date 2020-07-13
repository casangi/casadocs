Parameters
==========

.. container:: documentDescription description

   task parameters

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               fitsidifile : stringArray

            Name(s) of input FITS-IDI file(s) Default: none (must be
            supplied) Examples: fitsidifile='3C273XC1.IDI'
            fitsidifile=['3C273XC1.IDI1','3C273XC1.IDI2']

Example

.. container:: param

   .. container:: parameters2

      vis : string

   Name of output visibility file Default: none Example:
   outputvis='3C273XC1.ms'

Example

.. container:: param

   .. container:: parameters2

      constobsid : bool = False

   If True, give constant obs ID==0 to the data from all input fitsidi
   files (False = separate obs id for each file) Default: False (new obs
   id for each input file) Options: False|True

Example

.. container:: param

   .. container:: parameters2

      scanreindexgap_s : double = 0.

   Min time gap (seconds) between integrations to start a new scan
   Default: 0. (no reindexing) If > 0., a new scan is started whenever
   the gap between two integrations is > the given value (seconds) or
   when a new field starts or when the ARRAY_ID changes.

Example

.. container:: param

   .. container:: parameters2

      specframe : string = GEO

   This frame will be used to set the spectral reference frame for all
   spectral windows in the output MS Default: GEO (geocentric) Options:
   GEO|TOPO|LSRK|BARY NOTE: if specframe is set to TOPO, the reference
   location will be taken from the Observatories table in the CASA data
   repository for the given name of the observatory. You can edit that
   table and add new rows.

Example

.. container:: section
   :name: viewlet-below-content-body
