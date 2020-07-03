.. container::
   :name: viewlet-above-content-title

Observing Modes
===============

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   ALMA modes for observing: PS, OTF, and OTF-raster

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. container:: content5

         At present, ALMA single dish observing has three modes: PS
         (position switched), OTF (on the fly), and OTF-raster
         (Rasterized on the fly). These have slightly different
         observation/scanning patterns, and also have differences in the
         cadence and position of the OFF measurements.

         In the case of the PS mode, the OFF position is specified by
         the PI before the observations.  The OFF positions have a
         specific and periodic cadence and should, where possible, be at
         approximately the same azimuth as the observations of the
         science target. Note that PS mode observations can include
         mapping observations, and this is actually the general mode for
         ALMA single-dish observations.

         For OTF-raster, the telescope scans the observing target,
         including some additional length on either side of the target. 
         The reference data are interpolated from the OFF positions at
         the edge of the scans. It is assumed that the bandpass profile
         varies slowly as a function of scan position. This mode yields
         a slightly better calibration than position switching, since
         the variation in the air mass is typically more consistent
         between the OFF data and the target.  At present, ALMA uses
         OTF-raster mode to calibrate observations of the amplitude
         (i.e. Jy-to-K) calibrators.

         For OTF mode, the observations are not rasterized.  The
         scanning pattern for OTF observations can take several forms. 
         Solar observations, for example, use a double-circle scan. In
         this case the entire periphery of the observed region is
         identified as an OFF measurement.  The OTF-raster mode, on the
         other hand, uses the first and last points of the raster rows
         as the OFF. A mean bandpass is formed from the OFF
         measurements, interpolated in time, and applied to any
         measurements not identified as OFF.  For OTF and OTF-raster,
         specific OFF posiotions are not explicitly nominated prior to
         the observations. 

          

      .. container:: content5

          

.. container:: section
   :name: viewlet-below-content-body
