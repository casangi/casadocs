#
# stub function definition file for docstring parsing
#

def calstat(caltable, axis='amplitude', datacolumn='gain', useflags=True):
    r"""
Displays statistical information on a calibration table

Parameters
   - caltable_ (string) - Name of input calibration table
   - axis_ (string='amplitude') - Which values to use

      .. raw:: html

         <details><summary><i> axis = amp </i></summary>

      - datacolumn_ (string='gain') - Which data column to use

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> axis = amplitude </i></summary>

      - datacolumn_ (string='gain') - Which data column to use

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> axis = phase </i></summary>

      - datacolumn_ (string='gain') - Which data column to use

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> axis = real </i></summary>

      - datacolumn_ (string='gain') - Which data column to use

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> axis = imag </i></summary>

      - datacolumn_ (string='gain') - Which data column to use

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> axis = imaginary </i></summary>

      - datacolumn_ (string='gain') - Which data column to use

      .. raw:: html

         </details>
   - useflags_ (bool=True) - Take flagging into account? (not implemented)


Description
   .. rubric:: Summary
      

   The **calstat** task returns statistical information about a
   column in a calibration table. The following values are computed:
   mean value, sum of values, sum of squared values, median, median
   absolute deviation, quartile, minimum, maximum, variance, standard
   deviation, root mean square. The results are printed in the CASA
   logger. The statistics info can also be captured as a python
   dictionary return variable. See the examples.

   At this time, it is not possible to apply selection to the
   caltable.

   .. warning:: NB: The *useflags* parameter is not yet implemented.




Details
   Explanation of each parameter

.. _caltable:

   .. rubric:: caltable

   | Name of input calibration table
   |                      Default: ''
   | 
   |                         Example: vis='ggtau.1mm.amp.gcal'

.. _axis:

   .. rubric:: axis

   | Which data to analyze.
   |                      Default: 'amplitude'
   |                      Options: 'amp', 'amplitude', 'phase', 'real',
   |                      'imag', 'imaginary'. Also, the name of any real
   |                      valued MS column can be given, e.g. TIME,
   |                      POLY_COEFF_AMP, REF_ANT, ANTENNA1, FLAG, ...
   | 
   |                      Note: the phase of a complex number is in
   |                      radians in the range [-pi; pi].

.. _datacolumn:

   .. rubric:: datacolumn

   | Which data column to use if axis is 'amp', 'amplitude', 'phase', 'real', 'imag' or 'imaginary'.
   |                      Default: 'gain'

.. _useflags:

   .. rubric:: useflags

   | Take flagging into account? (not implemented, this
   | parameter  has no effect!)
   |                      Default: False
   |                     
   |                      If useflags=False, flagged values are included in
   |                      the statistics. 
   |                      If useflags=True, any flagged values are not used
   |                      in the statistics.


    """
    pass
