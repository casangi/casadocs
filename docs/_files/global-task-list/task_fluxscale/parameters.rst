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

               vis : string

            Name of input visibility file Default: none Example:
            vis='ngc5921.ms'

Example

.. container:: param

   .. container:: parameters2

      caltable : string

   Name of input calibration table Default: none Example:
   caltable='ngc5921.gcal'. This cal table was obtained from task
   gaincal.=

Example

.. container:: param

   .. container:: parameters2

      fluxtable : string

   Name of output, flux-scaled calibration table (required) Default:
   none Example: fluxtable='ngc5921.gcal2' The gains in this table have
   been adjusted by the derived flux density each calibrator. The
   MODEL_DATA column has NOT been updated for the flux density of the
   calibrator. Use setjy to do this if it is a point source.

Example

.. container:: param

   .. container:: parameters2

      reference : stringArray

   Reference field name(s) (transfer flux scale FROM) Default: none
   Example: reference='1328+307' The names of the fields with a known
   flux densities or visibilities that have been placed in the MODEL
   column by setjy or ft for a model not in the CASA system. The syntax
   is similar to field. Hence field index or names can be used.

Example

.. container:: param

   .. container:: parameters2

      transfer : stringArray

   Transfer field name(s) (transfer flux scale TO) Default: '' (all
   sources in caltable that are not specified as reference sources. Do
   not include unknown target sources) The names of the fields with
   unknown flux densities. These should be point-like calibrator sources
   The syntax is similar to field. Hence source index or names can be
   used. Examples: transfer='1445+099, 3C84'; transfer = '0,4' NOTE: All
   fields in reference and transfer must have solutions in the caltable.

Example

.. container:: param

   .. container:: parameters2

      listfile : string

   Name of listfile that contains the fit information. Default: '' (no
   fit listfile will be created) The list file contains the flux
   density, flux density error, S/N, and number of solutions (all
   antennas and feeds) for each spectral window. NOTE: The nominal
   spectral window frequencies will be included in the future.

Example

.. container:: param

   .. container:: parameters2

      append : bool = False

   Append fluxscaled solutions to the fluxtable? Default: False (the
   fluxtable must not exist) Options: False|True

Example

.. container:: param

   .. container:: parameters2

      refspwmap : intArray = -1

   Vector of spectral windows enabling scaling across spectral windows
   Default: [-1] (none) Example with 4 spectral windows: If the
   reference fields were observed only in spw=1 and 3, and the transfer
   fields were observed in all 4 spws (0,1,2,3), specify
   refspwmap=[1,1,3,3]. This will ensure that transfer fields observed
   in spws 0,1,2,3 will be referenced to reference field solutions only
   in spw 1 or 3.

Example

.. container:: param

   .. container:: parameters2

      gainthreshold : double = -1.0

   Threshold in the input gain solutions to be used in fractional
   deviation from median values. Default: -1 (no threshold) Example:
   gainthreshold=0.15 (only used the gain solutions within 15%
   (inclusive) of the median gain value (per field and per spw).

Example

.. container:: param

   .. container:: parameters2

      antenna : string

   Select data based on antenna/baseline Subparameter of antenna
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

   Select data based on time range Subparameter of antenna Default = ''
   (all) Examples: timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
   (Note: if YYYY/MM/DD is missing date defaults to first day in data
   set.) timerange='09:14:0~09:54:0' picks 40 min on first day
   timerange= '25:00:00~27:30:00' picks 1 hr to 3 hr 30min on NEXT day
   timerange='09:44:00' pick data within one integration of time
   timerange='>10:24:00' data after this time

Example

.. container:: param

   .. container:: parameters2

      scan : string

   Scan number range Subparameter of antenna Default: '' = all

Example

.. container:: param

   .. container:: parameters2

      incremental : bool = False

   Create an incremental caltable containing only gain correction
   factors ( flux density= 1/(gain correction factor)**2)? Default:
   False Options: False|True Example: incremental=True (output a
   caltable containing flux scale factors.) NOTE: If you use the
   incremental option, note that BOTH this incremental fluxscale table
   AND an amplitude vs. time table should be supplied in applycal.

Example

.. container:: param

   .. container:: parameters2

      fitorder : int = 1

   Polynomial order of the spectral fitting for valid flux densities
   Default: 1 It falls back to a lower fitorder if there are not enough
   solutions to fit with the requested fitorder.

Example

.. container:: param

   .. container:: parameters2

      display : bool = False

   Display statistics and/or spectral fitting results. Default: False
   Options: False|True Currently only a histogram of the correction
   factors to derive the final flux density for each spectral window
   will be plotted.

Example

.. container:: param

   .. container:: parameters2

      fluxd : undefined = {}

   Dictionary containing the transfer fluxes and their errors.

Example

.. container:: section
   :name: viewlet-below-content-body
