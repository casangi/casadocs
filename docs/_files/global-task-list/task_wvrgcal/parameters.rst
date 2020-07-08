.. container::
   :name: viewlet-above-content-title

Parameters
==========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task parameters

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               vis : string

            Name of input visibility file

Example

.. container:: param

   .. container:: parameters2

      caltable : string

   Name of output gain calibration table

Example

.. container:: param

   .. container:: parameters2

      toffset : double = 0

   Time offset (sec) between interferometric and WVR data

Example

.. container:: param

   .. container:: parameters2

      segsource : bool = True

   Do a new coefficient calculation for each source

Example

.. container:: param

   .. container:: parameters2

      sourceflag : stringArray

   Regard the WVR data for these source(s) as bad and do not produce
   corrections for it (requires segsource=True)

Example

.. container:: param

   .. container:: parameters2

      tie : stringArray

   Prioritise tieing the phase of these sources as well as possible
   (requires segsource=True)

Example

.. container:: param

   .. container:: parameters2

      nsol : int = 1

   Number of solutions for phase correction coefficients (nsol>1
   requires segsource=False)

Example

.. container:: param

   .. container:: parameters2

      disperse : bool = False

   Apply correction for dispersion

Example

.. container:: param

   .. container:: parameters2

      wvrflag : stringArray

   Regard the WVR data for these antenna(s) as bad and replace its data
   with interpolated values from neighbouring antennas

Example

.. container:: param

   .. container:: parameters2

      statfield : string

   Compute the statistics (Phase RMS, Disc) on this field only

Example

.. container:: param

   .. container:: parameters2

      statsource : string

   Compute the statistics (Phase RMS, Disc) on this source only

Example

.. container:: param

   .. container:: parameters2

      smooth : string

   Smooth calibration solution on the given timescale

Example

.. container:: param

   .. container:: parameters2

      scale : double = 1.

   Scale the entire phase correction by this factor

Example

.. container:: param

   .. container:: parameters2

      spw : intArray

   List of the spectral window IDs for which solutions should be saved
   into the caltable

Example

.. container:: param

   .. container:: parameters2

      wvrspw : intArray

   List of the spectral window IDs from which the WVR data should be
   taken

Example

.. container:: param

   .. container:: parameters2

      reversespw : string

   Reverse the sign of the correction for the listed SPWs (only needed
   for early ALMA data before Cycle 0)

Example

.. container:: param

   .. container:: parameters2

      cont : bool = False

   Estimate the continuum (e.g., due to clouds) (experimental)

Example

.. container:: param

   .. container:: parameters2

      maxdistm : double = 500.

   maximum distance (m) of an antenna used for interpolation for a
   flagged antenna

Example

.. container:: param

   .. container:: parameters2

      minnumants : int = 2

   minimum number of near antennas (up to 3) required for interpolation

Allowed Value(s)

1 2 3

Example

.. container:: param

   .. container:: parameters2

      mingoodfrac : double = 0.8

   If the fraction of unflagged data for an antenna is below this value
   (0. to 1.), the antenna is flagged.

Example

.. container:: param

   .. container:: parameters2

      usefieldtab : bool = False

   derive the antenna AZ/EL values from the FIELD rather than the
   POINTING table

Example

.. container:: param

   .. container:: parameters2

      refant : stringArray

   use the WVR data from this antenna for calculating the dT/dL
   parameters (can give ranked list)

Example

.. container:: param

   .. container:: parameters2

      offsetstable : string

   (experimental) subtract the temperature offsets in this table from
   the WVR measurements before calculating the phase corrections

Example

.. container:: section
   :name: viewlet-below-content-body
