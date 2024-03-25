calstat -- Displays statistical information on a calibration table -- calibration task
=======================================

Description
---------------------------------------

This task returns statistical information about a column in a
calibration table. The following values are computed: mean value, sum
of values, sum of squared values, median, median absolute deviation,
quartile, minimum, maximum, variance, standard deviation, root mean
square.



Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - caltable
     - :code:`''`
     - Name of input calibration table
   * - axis
     - :code:`'amplitude'`
     - Which values to use
   * - datacolumn
     - :code:`'gain'`
     - Which data column to use
   * - useflags
     - :code:`True`
     - Take flagging into account? (not implemented)
   * - xstat
     - :code:`[ ]`
     - 


Parameter Explanations
=======================================



caltable
---------------------------------------

:code:`''`

Name of input calibration table
                     Default: ''

                        Example: vis='ggtau.1mm.amp.gcal'



axis
---------------------------------------

:code:`'amplitude'`

Which data to analyze.
                     Default: 'amplitude'
                     Options: 'amp', 'amplitude', 'phase', 'real',
                     'imag', 'imaginary'. Also, the name of any real
                     valued MS column can be given, e.g. TIME,
                     POLY_COEFF_AMP, REF_ANT, ANTENNA1, FLAG, ...

                     Note: the phase of a complex number is in
                     radians in the range [-pi; pi].



datacolumn
---------------------------------------

:code:`'gain'`

Which data column to use if axis is 'amp', 'amplitude', 'phase', 'real', 'imag' or 'imaginary'.
                     Default: 'gain'



useflags
---------------------------------------

:code:`True`

Take flagging into account? (not implemented, this
parameter  has no effect!)
                     Default: False
                    
                     If useflags=False, flagged values are included in
                     the statistics. 
                     If useflags=True, any flagged values are not used
                     in the statistics.



xstat
---------------------------------------

:code:`[ ]`

Statistical information for the calibration table




