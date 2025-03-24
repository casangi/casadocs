

.. _Returns:

Returns
   frac_stokes (dict) - fractional Stokes results, keyed by field
   and SPW (including a SPW-averaged result)


.. _Description:

Description
   .. warning:: This task is considered "experimental" in CASA 6.6. 
      

The polfromgain task permits extracting point-source calibrator linear polarization estimates from time- (and thus parallactic angle-) dependent 
gaintype='G' (gaincal) solutions obtained from observations in the linear basis where no linear polarization model was supplied.  Since the linear 
basis parallel hands, XX and YY, are proportional to (I+Qp) and (1-Qp), respectively (where Qp = Qcos2p + Usin2p, and p is the time-depedent 
parallactic angle), the polarization-dependent (gaintype='G') gains, Gx and Gy, obtained by gaincal on a point-like calibrator will absorb the 
time-dependent polarization information if the correct polarized model has not been supplied.  For geographically small arrays (for which there 
is negligible parallactic angle variation across the array) with linear feeds (e.g., ALMA), this task extracts reasonably accurate fractional Q 
and U estimates from the ratio of the square of the gain ratio Gx/Gy.   If the source is unpolarized, or if the gains were solved using a visibility 
model with the correct Q,U included (and parang=True), polfromgain should return Q=U=0.0 (to within the noise).  The Q,U estimates will be performed 
per spectral window and antenna, and logged, and the task returns a python dictionary containing the fractional Stokes vector for each available 
spw (averaged over antennas), along with an average over all spectral window.  If there are solutions for multiple fields within the suppied gain 
caltable, separate Q and U estimates will be generated for each.  Optionally, by specifying an output caltable, a new gain caltable containing gains corrected for the 
source polarization effects may be generated.

The polfromgain task cannot and will not give sensible results for gain calibration tables solved in the circular basis, and therefore should not
be used for arrays with circularly-polarized feeds, e.g., JVLA (>1 GHz).

As of CASA 6.6, polfromgain cannot yet account for ionospheric faraday rotation embedded within the Gx, Gy gains.  (Note that such gains cannot be 
solved for relative to ionospheric faraday rotation without prior knowledge of the calibrator linear polarization.)
 
.. _Examples:

Example
   To derive Q,U estimates from gaintable 'gaintable.gcal' (gaintype='G' in task gaincal), based on a point-source calibrator from the MS 'inputvis.ms' that has significant time/parallactic angle-dependence but no linear polarization model supplied during calibration, and to create a new gain caltable 'optional_newtable.gcal' that contains gains corrected for the polarization signature (a threshold of 45 degrees of parallactic angle coverage is enforced):
   
   ::
   
      S=polfromgain(vis='inputvis.ms', tablein='gaintable.gcal', caltable='optional_newtable.gcal',minpacov=45)

   The dictionary returned contains the fractional Stokes polarization information estimated by polfromgain:

   ::

      S = {'Field1' : {'Spw0': [1.0, 0.033, 0.015, 0.0],
                       'Spw1': [1.0, 0.035, 0.013, 0.0],
                       'SpwAve' : [1.0, 0.034, 0.014, 0.0]}}

.. _Development:

Development
   No additional development details
