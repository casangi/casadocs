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

       

      In the following example, antenna-based gain amplitude corrections
      for all spws, antennas, and polarizations will be multiplied by 3.
      When applied to visibility data, this correction will produce a
      corrected visibility that is (1/3*1/3) less than the uncorrected
      visibility.

      .. container:: casa-input-box

         | gencal(vis='test.ms',caltable='test.G',caltype='amp',
         |        spw='',antenna='',pol='',
         |        parameter=[3])

       

      In the following example, gain phase corrections for antennas ea03
      and ea04 will be adjusted (additive) by 45 and 120 degrees
      (respectively), for all spws and polarizations. When these phases
      are applied to visibility data, the visibility phases will
      decrease or increase by the specified amount where the selected
      antennas occur first or second (respectively) in each baseline.
      E.g., the phase of baseline ea03&ea04 will change by (-45+120) = +
      75 degrees. Baseline ea01&ea03's phase will change by +45 degrees;
      baseline ea04&ea05's phase will change by -120 degrees. The same
      phase sign convention is used for delay and antenna position
      corrections.

      .. container:: casa-input-box

         | gencal(vis='test.ms',caltable='test.G',caltype='ph',
         |        spw='',antenna='ea03,ea04',pol='',
         |        parameter=[45,120])

       

      Gain phase corrections for antennas ea05 and ea06 will be adjusted
      (additive) by 63 and -34 degrees (respectively), in R only, for
      all spws

      .. container:: casa-input-box

         | gencal(vis='test.ms',caltable='test.G',caltype='ph',
         |        spw='',antenna='ea05,ea06',pol='R',
         |        parameter=[63,-34])

       

      Gain phase corrections in all spws will be adjusted for antenna
      ea09 by 14 deg in R and -23 deg in L, and for antenna ea10 by -130
      deg in R and 145 deg in L.

      .. container:: casa-input-box

         | gencal(vis='test.ms',caltable='test.G',caltype='ph',
         |        spw='',antenna='ea09,ea10',pol='R,L',
         |        parameter=[14,-23,-130,145])

       

      Gain phases corrections in both polarizations will be adjusted for
      antenna ea09 by 14 deg in spw 2 and -23 deg in spw 3, and for
      antenna ea10 by -130 deg in spw 2 and 145 deg in spw 3.

      .. container:: casa-input-box

         | gencal(vis='test.ms',caltable='test.G',caltype='ph',
         |        spw='2,3',antenna='ea09,ea10',pol='',
         |        parameter=[14,-23,-130,145])

       

      Delay corrections in both polarizations will be adjusted for
      antenna ea09 by 14 nsec in spw 2 and -23 nsec in spw 3, and for
      antenna ea10 by -130 nsec in spw 2 and 145 nsec in spw 3. See the
      above example for *caltype='ph'* for details of the sign
      convention adopted when applying delay corrections.

      .. container:: casa-input-box

         | gencal(vis='test.ms',caltable='test.G',caltype='sbd',
         |        spw='2,3',antenna='ea09,ea10',pol='',
         |        parameter=[14,-23,-130,145])

       

      \**\* Currently Karl G. Jansky VLA observations only \***  Antenna
      position corrections will be retrieved automatically over internet
      to generate the caltable with *antenna=''*.

      .. container:: casa-input-box

         gencal(vis='test.ms',caltable='test.G',caltype='antpos',antenna='')

       

      Antenna position corrections in meters (in ITRF) for antenna ea09
      (dBx=0.01, dBy=0.02, dBz=0.03) and for antenna ea10 (dBx=-0.03,
      dBy=-0.01, dBz=-0.02). See the above example for *caltype='ph'*
      for details of the sign convention adopted when applying 'antpos'
      corrections.

      .. container:: casa-input-box

         | gencal(vis='test.ms',caltable='test.G',caltype='antpos',
         |        antenna='ea09,ea10',
         |        parameter=[0.01,0.02,0.03, -0.03,-0.01,-0.02])

       

      Antenna position corrections (in the traditional VLA-centric
      frame) will be introduced in meters for antenna ea09 (dBx=0.01,
      dBy=0.02, dBz=0.03) and for antenna ea10 (dBx=-0.03, dBy=-0.01,
      dBz=-0.02).  These offsets will be rotated to the ITRF frame
      before storing them in the caltable. See the above example for
      *caltype='ph'* for details of the sign convention adopted when
      applying antpos corrections.

      .. container:: casa-input-box

         | gencal(vis='test.ms',caltable='test.G',caltype='antposvla',
         |        antenna='ea09,ea10',
         |        parameter=[0.01,0.02,0.03, -0.03,-0.01,-0.02])

       

.. container:: section
   :name: viewlet-below-content-body
