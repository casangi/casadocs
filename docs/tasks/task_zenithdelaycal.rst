.. _Description:

Description
   Estimate the atmospheric zenith delay and clock error

   Given a calibration table with multi-band delays (MBDs), the **zenithdelaycal** task separates the contribution from the atmosphere and the clock using the model:
   
   .. math::
   
        Delay = Clock(t) + Atmo(t) * Airmass(elevation)

   Where Clock(t) and Atmo(t) are polynomials describing the clock and atmosphere, respectively, and Airmass(elevation) is the model used to describe the airmass (selected through the ``atmospheric_delay_model`` argument).
   **zenithdelaycal** finds the polynomials that describe the delay rates.

   In VLBI the correlator assumes a model of the clock error and atmosphere that is not perfect. Residual errors in the clock and atmosphere can be estimated from MBDs spanning a range of elevations. For more background and details on how to setup the observations please see `AIPS memo 110 <https://www.aips.nrao.edu/TEXT/PUBL/AIPSMEM110.PS>`_.

.. _Examples:

Examples
   Example of a zenithdelaycal call using a constant clock error and a linear polynomial for the atmosphere:

   ::

        zenithdelaycal(vis="data.ms",
                       caltable="data.zen",
                       refant="PT",
                       mbdtable="data.mbd",
                       clock_polynomial_order=0,
                       atmospheric_polynomial_order=1)

   Example of a zenithdelaycal call using cuadratic polynomials for both the clock and atmosphere:

   ::

        zenithdelaycal(vis="data.ms",
                       caltable="data.zen",
                       refant="PT",
                       mbdtable="data.mbd",
                       clock_polynomial_order=2,
                       atmospheric_polynomial_order=2)

   Example of a zenithdelaycal call using a secant cubed model for the airmass:

   ::

        zenithdelaycal(vis="data.ms",
                       caltable="data.zen",
                       refant="PT",
                       mbdtable="data.mbd",
                       atmospheric_delay_model="secant cubed")

   Example of a zenithdelaycal call producing output plots:

   ::

        zenithdelaycal(vis="data.ms",
                       caltable="data.zen",
                       refant="PT",
                       mbdtable="data.mbd",
                       plot_delay_solution=True)

   The output plots will be stored in the current working directory as PNGs with the names ``zenithdelaycal_delay_plot_antenna-name.png``, where ``antenna-name`` is replaced by the corresponding antenna name (e.g., "PT", "SC", etc...).

.. _Development:

Development
   No additional development details

