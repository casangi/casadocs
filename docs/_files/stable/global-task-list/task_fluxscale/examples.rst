.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Examples
========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task examples

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Given a *'G'* table, *'cal.G'*, containing solutions for a flux
      density calibrator, 3C286, and for two fields with unknown flux
      densities (*0234+285* and *0323+022*):

      .. container:: casa-input-box

         | fluxscale(vis='data.ms',
         |           caltable='cal.G',                  # Select input
           table
         |           fluxtable= 'cal.Gflx',             # Write scaled
           solutions to cal.Gflx
         |           incremental=True,                  # Generate an
           incremental output table
         |           reference='3C286',                 # 3C286 = flux
           calibrator
         |           transfer='0234+258, 0323+022')     # Select
           calibrators to scale

      The output table, *cal.Gflx*, contains per-field, per-spw scaling
      factors alone to be used along with the input gain table *cal.G*
      in subsequent operations, e.g., **applycal**. If
      *incremental=False* had been used, the output *fluxtable* should
      be used in place of the input *caltable* in subsequent operations.

       

      If transfer of the flux density scale among spws is required, use
      *refspwmap.* For example:

      .. container:: casa-input-box

         | fluxscale(vis='data.ms',
         |           caltable='cal.G',                  # Select input
           table
         |           fluxtable= 'cal.Gflx',             # Write scaled
           solutions to cal.Gflx
         |           reference='3C286',                 # 3C286 = flux
           calibrator
         |           transfer='0234+258,0323+022'       # Select
           calibrators to scale
         |           refspwmap=[0,0,0])                 # Use spwid 0
           scaling for spwids 1 & 2

      will use the *reference* field gain amplitudes from spw=0 to scale
      the *transfer* field gain amplitudes in spws 0, 1 & 2.

       

      If the flux density calibrator is resolved, and an adequate model
      is not available, use *antenna* and *uvrange* selection in gaincal
      to limit the gain solutions to baselines satisfying the
      point-source assumption. For example, solve for the flux density
      calibrator (3C286) only, with limited data:

      .. container:: casa-input-box

         | gaincal(vis='data.ms',
         |         caltable='cal.G',        # write solutions to cal.G
         |         field='3C286'            # Select the flux density
           calibrator
         |         selectdata=True,         # Expand other selectors
         |         antenna='0~7',           #  antennas 0-7,
         |         uvrange='0~15klambda',   #  limit uvrange to
           0-15klambda
         |         solint=90)               # on 90s timescale

      Then solve for the other (presumably point-like) calibrators using
      all antennas and baselines, and append to the same *caltable*:

      .. container:: casa-input-box

         | gaincal(vis='data.ms',
         |         caltable='cal.G',           # write solutions to
           cal.G
         |         field='0234+258,0323+022',  # point-like calibrators
           with unknown f.d.
         |         solint=90,
         |         append=True)                   # append to the same
           table

      Finally, run **fluxscale** on the aggregate *caltable*:

      .. container:: casa-input-box

         | fluxscale(vis='data.ms',
         |           caltable='cal.G',      # Input table with unscaled
           cal solutions
         |           fluxtable='cal.Gflx',  # Write scaled solutions to
           cal.Gflx
         |           reference='3C286',     # Use 3c286 as ref with
           limited uvrange
         |           transfer='0234+285,0323+022')   # Transfer scaling

.. container:: section
   :name: viewlet-below-content-body
