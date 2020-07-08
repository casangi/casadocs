.. container::
   :name: viewlet-above-content-title

sdcal
=====

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Single-dish data calibration

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      | Task **sdcal** implements a single-dish data calibration scheme
        similar to that of interferometry, i.e., generate calibration
        tables (caltables) and apply them. Available calibration modes
        (*calmode*) are 'ps', 'otfraster', and 'otf' for sky (reference)
        calibration; and 'tsys' for Tsys\ :math:`T_{\rm sys}`
        calibration. Caltables can be applied to the data with
        *calmode*\ ='apply'. Each mode generates a caltable except for
        *calmode*\ ='apply'. A combination of mode keywords is also
        supported, e.g., *calmode*\ ='ps,tsys,apply' to calibrate sky
        and Tsys\ :math:`T_{\rm sys}` on-the-fly. Calibration is
        available even for fast-moving sources like the Moon (see the
        note relating to the 'otf' mode below).
      | The calibration mode must be set in accordance with the
        observing mode of the data. The modes are as follows: 

      -  'ps': position switching (including OTF) with explicit
         reference (OFF) spectra
      -  'otfraster': raster OTF scan without explicit OFFs
      -  'otf': non-raster OTF scan without explicit OFFs

      | Thus, if the data contains explicit reference spectra, 'ps'
        should be used. Otherwise, 'otfraster' or 'otf' should be used.
      | In 'otfraster' and 'otf' modes, specific edge regions of the
        observation pattern are automatically marked as reference (OFF)
        spectra.
      | These specific regions are:

      -  in 'otfraster' mode: regions near the beginning and end of the
         raster scan lines.
      -  in 'otf' mode: regions near the periphery of the observation
         pattern.

      .. container:: info-box

         **NOTE**: Although the 'otfraster' mode is designed for OTF
         observations without explicit OFF spectra, it should work even
         if explicit reference spectra exist. In that case, the OFF
         spectra are ignored and spectra identified by an edge marker
         are used as the reference.

      .. container:: info-box

         **NOTE**: Detection of periphery scans in 'otf' mode is
         available for "ephemeris" sources, e.g., the Sun and Moon.
         Often, antennas will track these ephemeris sources so that the
         target source is always at the map center. For such
         observations, a periphery search is done in the source frame of
         the ephemeris source, so the observing target maintains its
         position in the map. For calibration in the 'otf' mode, higher
         order pointing interpolation has been implemented to get the
         pointing direction for each spectral data more appropriately.

      Apart from the way reference spectra are selected, the procedure
      to derive calibrated spectra is the same for all modes. Selected
      (or preset) OFF integrations contiguous in time are identified,
      averaged in each segment, and then interpolated to timestamps for
      ON integrations. Effectively, it means that OFF integrations are
      averaged by each OFF spectrum for 'ps' mode, and averaged by
      either ends of each raster row for 'otfraster' mode. Spectra are
      calibrated by:

      TsysON−OFFOFF\ :math:`T_{\rm sys}  \frac{ ON - OFF } { OFF }`.

      .. container:: info-box

         **NOTE**: If *outfile* is unset and *calmode* doesn't include
         "apply", a default names of calibration tables are generated
         based on the *infile* and a predefined suffix  ('_sky' for sky,
         '_tsys' for Tsys\ :math:`T_{\rm sys}`).

       

       

.. container:: section
   :name: viewlet-below-content-body


.. toctree::
   :hidden:
   :maxdepth: 3

   task_sdcal/about
   task_sdcal/parameters
   task_sdcal/changelog
   task_sdcal/examples
   task_sdcal/developer