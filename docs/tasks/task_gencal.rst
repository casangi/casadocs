

.. _Description:

Description
   The **gencal** task provides a means of specifying antenna-based
   calibration values manually. The values are put in designated
   tables and applied to the data using other tasks (**applycal**,
   **gaincal**, **bandpass**, etc.). Several specialized calibrations
   are also generated with **gencal**.

   .. rubric:: Calibration types: *caltype*
   
   The **gencal** task supports many different calibration types via
   the *caltype* parameter. These are listed here in two groups. Many
   of these options are part of `Preparing for
   Calibration <../../notebooks/synthesis_calibration.ipynb#Preparing-for-Calibration>`__
   and more information about how they work can be found in that
   section.
   
   .. rubric:: Manual *caltype*
   
   The following enable directly specifying calibration factors for
   each specified *pol*, *antenna*, *spw*. Except where noted, each
   expects one real *parameter* value per specified *pol*, *antenna*,
   and *spw*.
   
   -  'amp'= amplitude correction
   -  'ph' = phase correction
   -  'sbd'= single-band delay (phase-frequency slope for each spw)
   -  'mbd'= multi-band delay (phase-frequency slope over all spw)
   -  'opac' = Tropospheric opacity (1 real parameter [in nepers] per
      antenna, spw)
   -  'antpos' = ITRF antenna position corrections (3 real parameters
      [in m] for each antenna; see below)
   -  'antposvla' = VLA-centric antenna position corrections (3 real
      parameters [in m] for each antenna; see below)
   
   .. rubric:: Specialized *caltype*
   
   The following *caltype* options automatically generate caltables
   from ancilliary information found in the MS or elsewhere. The
   *pol, antenna, spw,* and *parameter* options are ignored for
   these.
   
   -  'tsys' = Tsys from the MS.SYSCAL table (ALMA, VLBI)
   -  'swpow' = VLA switched-power gains from MS.SYSPOWER, CALDEVICE
   -  'rq' = VLA requantizer gains \_only\_
   -  'swp/rq' = VLA switched-power gains divided by requantizer gain
   -  'gc' = Gain curve (zenith-angle-dependent gain) (VLA, VLBI)
   -  'eff' = Antenna efficiency (sqrt(K/Jy)) (VLA only)
   -  'gceff' = Gain curve and efficiency (VLA only)
   -  'tecim' = Time-dependent TEC image specified in *infile*
      subparameter
   -  'antpos' = For VLA datasets, automatic lookup of antenna
      position corrections if *antenna=''*
   - 'jyperk' = Jy/K factors via Jy/K database Web API if infile=''
      (ALMA only)
      
   For the VLA, *caltype='gc'* will do auto-lookup the gain curve information.
   For VLBI, gain curve information will be taken from MS.GAIN_CURVE when present
   or from an external table specified by the *infile* subparameter.

   .. rubric:: Specifying calibration values: *pol, antenna, spw, parameter*
   
   Generic calibration values for the "manual *caltype* s" listed
   above should be specified in the *parameter* argument as a list.
   The length of the list must correspond to the net length of the
   specific polarizations, antennas, and spws specified in the *pol*,
   *antenna*, and *spw* selection arguments.  The values specified in
   *parameter* will be duplicated over all members of any selection
   axis that is not explicitly specified (*pol* ='', *spw* =''
   and/or *antenna* ='') E.g., if
   *pol* = *antenna* = *spw* ='', it only makes sense to specify
   a single *parameter* value (or three, for *antpos* and
   *antposvla*), and this will be duplicated for all pols, antennas,
   and spws. If multiple *parameter* values are specified, at least
   one of *pol*, *spw*, or *antenna* must be non-trivial, and the
   number of values in *parameter* must be consistent with the range
   of specified *pol*, *spw*, and/or *antenna*. E.g., if only a
   non-trivial *spw* selection is specified, then the *parameter*
   value list should match the number of spws specified, and these
   values will be duplicated for all polarizations and antennas. If
   more than one of *pol*, *spw*, and *antenna* is non-trivially
   specified, the number of *parameter * values specified should
   match the product of the number specified selection elements. The
   *parameter* values should be sorted by *pol* (fastest), *antenna*,
   and *spw* (slowest). Un-specified elements on non-trivially
   specified axes will be filled with nominal values (i.e., it is not
   necessary to exhaustively specify all elements on any axis or use
   nominal *parameter* values explicitly). **Please consult the
   examples for additional guidance.** There is currently no support
   for time-dependent calibration specfication; in all cases, the
   specified *parameter* values will be assumed constant in time
   (though their impact on the data may be time-dependent, depending
   on the *caltype*).
   
   The same *caltable* can be specified for multiple runs of
   **gencal**, in which case the specified *parameter* values will be
   incorporated cumulatively. E.g., amplitude-like values
   (*caltype='amp'*) multiply and phase-like values ('ph',
   'sbd','mbd','antpos') add. Also, 'amp' and 'ph' calibrations can
   be incorporated into the same *caltable* (in separate cumulative
   runs), but each of the other types require their own unique
   *caltable*. A mechanism for specifying manual corrections via a
   text file will be provided in the future.
   
   The calibration tables generated by **gencal** can be applied to
   the data in all other tasks that accept specified calibration for
   (pre-)application, e.g.,
   `applycal. <../../api/casashell.rst>`__
   **gaincal**, **bandpass**, etc.
   
   Consult the Examples for more information on the many *caltype*
   options in **gencal**.
   
   .. rubric:: Notes on specific *caltype* s
   
   -  'antpos'  For antenna position corrections
      (*caltype='antpos'*), the antenna position offsets are
      specified in the ITRF frame. For the Karl G. Jansky VLA,
      automated lookup of the antenna position corrections is enabled
      when antenna is unspecified (*antenna=''*) for this *caltype*.
      Note that this requires internet connection to access the VLA
      antenna position correction site.
   -  'antposvla'  For (old) pre-upgrade VLA position corrections,
      specify the values in the VLA-centric frame and **gencal** will
      rotate them to ITRF before storing them in the output caltable.
   -  VLA switched power calibration is supported in three modes:
      'swpow' (formerly 'evlagain', a syntax which has been
      deprecated) yields the formal VLA switched power calibration
      which describes voltage gain as sqrt(Pdif/Tcal) (used to
      correct the visibility data) and Tsys as Psum*Tcal/Pdif/2 (used
      to correct the weights). 'swpow' implicitly includes any
      requantizer gain scale and adjustments. 'rq' yields only the
      requantizer voltage gains (Tsys is set to 1.0 to avoid weight
      adjustments). 'swp/rq' yields the ordinary switched power
      voltage gains divided by the requantizer voltage gain (Tsys is
      calculated normally). The 'rq' and 'swp/rq' modes are are
      mainly intended for testing and evaluating the VLA switched
      power systems.
   -  For *caltype='opac'*, only constant (in time) opacities are
      supported via **gencal**.  
   -  For gaincurve and efficiency (*caltype='gc'*, *'gceff'*, or
      *'eff'*), observatory-provided factors are determined per spw
      according to the observing frequencies. These caltypes are currently
      only supported for VLA (including pre-upgrade VLA) and VLBI processing.
      (Appropriate factors for ALMA are TBD.)
   -  'jyperk'  For ALMA Total Power (Single Dish), the task without
      'infile' sub-parameter queries Jy/K DB
      (https://asa.alma.cl/science/jy-kelvins) via internet to obtain
      factors and generate a caltable. Or factors are taken from a 
      file in the local storage specified by the 'infile' sub-parameter
      to generate a caltable.


.. _Examples:

Examples
   In the following example, antenna-based gain amplitude corrections
   for all spws, antennas, and polarizations will be multiplied by 3.
   When applied to visibility data, this correction will produce a
   corrected visibility that is (1/3*1/3) less than the uncorrected
   visibility.
   
   ::
   
      gencal(vis='test.ms',caltable='test.G',caltype='amp',spw='',antenna='',pol='',
             parameter=[3])

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
   
   ::
   
      gencal(vis='test.ms',caltable='test.G',caltype='ph', spw='',antenna='ea03,ea04',pol='',
             parameter=[45,120])
   
   Gain phase corrections for antennas ea05 and ea06 will be adjusted
   (additive) by 63 and -34 degrees (respectively), in R only, for
   all spws
   
   ::
   
      gencal(vis='test.ms',caltable='test.G',caltype='ph',spw='',antenna='ea05,ea06',pol='R',
             parameter=[63,-34])

   
   Gain phase corrections in all spws will be adjusted for antenna
   ea09 by 14 deg in R and -23 deg in L, and for antenna ea10 by -130
   deg in R and 145 deg in L.
   
   ::
   
      gencal(vis='test.ms',caltable='test.G',caltype='ph',spw='',antenna='ea09,ea10',pol='R,L',
             parameter=[14,-23,-130,145])

   Gain phases corrections in both polarizations will be adjusted for
   antenna ea09 by 14 deg in spw 2 and -23 deg in spw 3, and for
   antenna ea10 by -130 deg in spw 2 and 145 deg in spw 3.
   
   ::
   
      gencal(vis='test.ms',caltable='test.G',caltype='ph',spw='2,3',antenna='ea09,ea10',pol='',
             parameter=[14,-23,-130,145])

   
   Delay corrections in both polarizations will be adjusted for
   antenna ea09 by 14 nsec in spw 2 and -23 nsec in spw 3, and for
   antenna ea10 by -130 nsec in spw 2 and 145 nsec in spw 3. See the
   above example for *caltype='ph'* for details of the sign
   convention adopted when applying delay corrections.
   
   ::
   
      gencal(vis='test.ms',caltable='test.G',caltype='sbd',spw='2,3',antenna='ea09,ea10',pol='',
             parameter=[14,-23,-130,145])
   
   Currently Karl G. Jansky VLA observations only Antenna
   position corrections will be retrieved automatically over internet
   to generate the caltable with *antenna=''*.
   
   ::
   
      gencal(vis='test.ms',caltable='test.G',caltype='antpos',antenna='')
   

   Antenna position corrections in meters (in ITRF) for antenna ea09
   (dBx=0.01, dBy=0.02, dBz=0.03) and for antenna ea10 (dBx=-0.03,
   dBy=-0.01, dBz=-0.02). See the above example for *caltype='ph'*
   for details of the sign convention adopted when applying 'antpos'
   corrections.
   
   ::
   
      gencal(vis='test.ms',caltable='test.G',caltype='antpos',antenna='ea09,ea10',
             parameter=[0.01,0.02,0.03, -0.03,-0.01,-0.02])
   

   Antenna position corrections (in the traditional VLA-centric
   frame) will be introduced in meters for antenna ea09 (dBx=0.01,
   dBy=0.02, dBz=0.03) and for antenna ea10 (dBx=-0.03, dBy=-0.01,
   dBz=-0.02).  These offsets will be rotated to the ITRF frame
   before storing them in the caltable. See the above example for
   *caltype='ph'* for details of the sign convention adopted when
   applying antpos corrections.
   
   ::
   
      gencal(vis='test.ms',caltable='test.G',caltype='antposvla',antenna='ea09,ea10',
             parameter=[0.01,0.02,0.03, -0.03,-0.01,-0.02])


.. _Development:

Development
   No additional development details

