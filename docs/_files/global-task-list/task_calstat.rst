calstat
=======

.. container:: documentDescription description

   displays statistical information on a calibration table

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

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

      .. container:: alert-box

         NB: The *useflags* parameter is not yet implemented.

.. container:: section
   :name: viewlet-below-content-body

.. toctree::
   :hidden:
   :maxdepth: 3

   task_calstat/changelog
   task_calstat/examples
