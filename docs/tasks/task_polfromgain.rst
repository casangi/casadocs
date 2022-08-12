

.. _Returns:

Returns
   frac_stokes (dict) - fractional Stokes results, indexed by field
   and SPW


.. _Description:

Description
   .. warning:: This task is considered "experimental" in CASA 5.5.  Improvements are expected in CASA 5.6 (e.g., sensitivity to the ionosphere), 
      and more testing experience will enable better advice for users.
      

The polfromgain task permits extracting point-source calibrator linear polarization estimates from time- (and thus parallactic angle-) dependent 
gaintype='G' (gaincal) solutions obtained from observations in the linear basis where no linear polarization model was supplied.  Since the linear 
basis parallel hands, XX and YY, are proportional to (I+Qp) and (1-Qp), respectively (where Qp = Qcos2p + Usin2p, and p is the time-depedent 
parallactic angle), the polarization-dependent (gaintype='G') gains, Gx and Gy, obtained by gaincal on a point-like calibrator will absorb the 
time-dependent polarization information if the correct polarized model has not been supplied.  This task extracts reasonably accurate fractional Q 
and U estimates from the ratio of the square of the gain ratio Gx/Gy.   The Q,U estimates will be performed per spectral window, and the task 
returns a python dictionary containing the fractional Stokes vector for each available spw, along with a spectral window average.  Optionally, a 
new gain caltable containing gains corrected for the polarization signature, may be generated.
 
As of CASA 5.5, polfromgain cannot yet account for ionospheric faraday rotation embedded within the Gx, Gy gains.  (Note that such gains cannot be 
solved for relative to ionospheric faraday rotation without prior knowledge of the calibrator linear polarization.)
 
The polfromgain task can and will not give sensible results for gain calibration tables solved in the circular basis.
 
.. rubric:: Task-specific parameters

*vis*
The Measurement Set corresponding to the specified gain table.  This is used to extract some geometry information not stored in the gain table. 

*tablein*
The input gain table, containing 'G' solutions with significant time/parallactic angle-dependence, and solved using an unpolarized model.   If 
the gain table has been obtained using an accurate polarized model, pofromgain should yield Q=U~=0.0.   

*caltable*
If specified, polfromgain will generate a new calibration table that has had the Q,U signature removed from the input gains. 

*paoffset*
If a non-zero value is specified, the estimated calibrator polarization will be rotated by this amount.  This may be useful if the feed orientation 
is not correctly stored in the MS.  This option should be used with great care since downstream calibration operations will behave differently.


.. _Examples:

Examples
   To derive Q,U estimates from gaintable 'gaintable.gcal' (gaintype='G' in task gaincal), based on a point-source calibrator from the MS 'inputvis.ms' that has significant time/parallactic angle-dependence but no linear polarization model supplied during calibration, and to create a new gain caltable 'optional_newtable.gcal' that contains gains corrected for the polarization signature:
   
   ::
   
      polfromgain(vis='inputvis.ms', tablein='gaintable.gcal', caltable='optional_newtable.gcal')

   
   
.. _Development:

Development
   No additional development details
