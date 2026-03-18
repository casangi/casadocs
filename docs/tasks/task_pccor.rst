.. _Description:

Description
   Generate Pulse Cal CORrections (**pccor**) for VLBA data

   **pccor** produces time resolved phase and delay corrections for
   VLBA data by analysing the phases in the PHASE_CAL table inside a
   VLBA MS. Delay corrections are estimated from the highest and
   lowest frequency tones within each SPW which leads to cycle
   ambiguities. Cycle ambiguities are dealt with by comparing the PC
   delay correction over a selected time range and/or scan with a
   reference fringe fit delay solution over the same time range
   obtained with a better spectral leverage. The reference fringe fit
   table can be produced by an internal **pccor** call to
   **fringefit** or can be provided by an expert user as input.

   When pulse cal data is completely missing for an antenna and/or
   spectral window **pccor** does not flag that data, it simply throws
   a warning and outputs the frige fit solution as the **pccor**
   solution for that antenna and/or spectral window.  When pulse cal
   data is missing during the selected time range for the fringe fit
   solution a warning is thrown indicating that this is the case,
   which the user may go around by selecting another fringe fit time
   range. Lastly in the case that pulse cal data is missing for the
   reference antenna during the fringe fit time range for a spectral
   window, no solutions will be produced for that spectral window, if
   all selected spectral windows have missing pulse cal data for the
   reference antenna an error/exception is thrown.

.. _Examples:

Examples
   Example of a pccor call using a scan to select a time range:

   ::
      
      pccor(
          vis='my_vlba_data.ms',
          pccor_caltable='my_vlba_data.ms.pccor',
          refant='LA',
          scan='15'
      )

   Example of a pccor call using a time range directly:

   ::
      
      pccor(
          vis='my_vlba_data.ms',
          pccor_caltable='my_vlba_data.ms.pccor',
          refant='LA',
          timerange='21:36:00~21:37:00'
      )

   Example of a pccor call with spectral window selection and MK
   antenna exclusion:

   ::
   
      pccor(
          vis='my_vlba_data.ms',
          pccor_caltable='my_vlba_data.ms.pccor',
          refant='LA',
          timerange='2011/09/16/21:36:00~21:37:00',
          spw='0,1,2',
          antenna='!MK'
      )

   Lastly an example of a pccor call where the user provides a
   reference frige fit cal table.

   ::
      
      pccor(
          vis='my_vlba_data.ms',
          pccor_caltable='my_vlba_data.ms.pccor',
          refant='LA',
          timerange='2011/09/16/21:36:00~21:37:00',
          ff_table='my_previous_ref_fringefit.mpc'
      )

.. _Development:

Development
   No additional development details
