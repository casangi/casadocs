#
# stub function definition file for docstring parsing
#

def calstat(caltable, axis='amplitude', datacolumn='gain', useflags=True):
    r"""
Displays statistical information on a calibration table

Parameters
   - **caltable** (string) - Name of input calibration table
   - **axis** (string) - Which values to use
   - **useflags** (bool) - Take flagging into account? (not implemented)

Subparameters
   .. raw:: html

      <details><summary><i> axis = amp </i></summary>

   - **datacolumn** (string=gain) - Which data column to use

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> axis = amplitude </i></summary>

   - **datacolumn** (string=gain) - Which data column to use

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> axis = phase </i></summary>

   - **datacolumn** (string=gain) - Which data column to use

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> axis = real </i></summary>

   - **datacolumn** (string=gain) - Which data column to use

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> axis = imag </i></summary>

   - **datacolumn** (string=gain) - Which data column to use

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> axis = imaginary </i></summary>

   - **datacolumn** (string=gain) - Which data column to use

   .. raw:: html

      </details>


Description
      .. rubric:: Summary
         :name: summary

      The **calstat** task returns statistical information about a
      column in a calibration table. The following values are computed:
      mean value, sum of values, sum of squared values, median, median
      absolute deviation, quartile, minimum, maximum, variance, standard
      deviation, root mean square. The results are printed in the CASA
      logger. The statistics info can also be captured as a python
      dictionary return variable. See the examples.

      At this time, it is not possible to apply selection to the
      caltable.

       

      .. rubric:: Parameters
         :name: parameters

      .. rubric:: *caltable*
         :name: caltable

      Specify the name of the calibration table as a string in
      *caltable*.

      .. rubric:: *axis*
         :name: axis

      Specify the axis upon which to calculate statistics in *axis*. The
      possible values are 'amp' (or 'amplitude'), 'phase', 'real',
      'imag' (or 'imaginary'). Also, the name of any real valued
      CalTable column can be given, e.g. TIME, POLY_COEFF_AMP, REF_ANT,
      ANTENNA1, FLAG, etc.

      .. rubric:: *datacolumn*
         :name: datacolumn

      For *axis='amp'*, *'amplitude'*, *'phase'*, *'real'*, *'imag'*, or
      *'imaginary'* specify the name of the column from which to extract
      the axis values and calculate statistics. E.g., for a 'G' table
      from **gaincal**, use *datacolumn='CPARAM'*.

      .. rubric:: *useflags*
         :name: useflags

      .. note:: NB: The *useflags* parameter is not yet implemented.

    """
    pass
