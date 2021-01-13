
.. _Description:

Description
   The task sdatmcor provides the capability of offline correction of
   residual atmospheric features in the calibrated single-dish spectra
   which result from the difference of elevation angle between ON_SOURCE
   and OFF_SOURCE measurements.

   The correction factor is derived from the atmosphere model based on
   the atmospheric properties (temperature, pressure, etc.) measured
   during the observation. The model is constructed by the atmosphere
   (at) tool.

   Only data selected by data selection parameters are corrected and
   written to the outfile. For spw, two selection parameters, *spw* and
   *outputspw*, are available. The former specifies the data to be
   corrected while the latter corresponds to the spw for output.
   In practice, intersection of *spw* and *outputspw* is corrected.
   For example, when `spw='19,23'` and `outputspw='19'`, spw 23 is not
   corrected because data for spw 23 is not written to outfile so
   that the correction is not meaningful.

   Note that *outfile* will have the data column DATA regardless of
   what data column exists in *infile*.



   .. rubric:: References


   | Sawada, T. et al., 2021, submitted to PASP



.. _Examples:

Examples
   task examples

   .. rubric::   Example 1

   The simplest example that processes all the data.

   ::

      sdatmcor(infile='sd_data.ms', datacolumn='float_data', outfile='sd_data.atmcor.ms',
      overwrite=True)


   .. rubric::   Example 2

   This example applies correction only to spw 23 but outputs all the data. Other spws are
   included in outfile but are not corrected.

   ::

      sdatmcor(infile='sd_data.ms', datacolumn='float_data', outfile='sd_data.atmcor.ms',
      spw='23', overwrite=True)


   .. rubric::   Example 3

   This example applies correction only to spw 23 and output only spw 23. Note that the
   only difference from Example 2 is that *outputspw* is set instead of *spw*.

   ::

      sdatmcor(infile='sd_data.ms', datacolumn='float_data', outfile='sd_data.atmcor.ms',
      outputspw='23', overwrite=True)


   .. rubric::   Example 4 (not practical)

   This example applies correction to spw 19 and 23 and output only spw 23. In this case,
   correction was applied only to spw 23 because spw 19 is not supposed to be included in
   *outfile*.

   ::

      sdatmcor(infile='sd_data.ms', datacolumn='float_data', outfile='sd_data.atmcor.ms',
      spw='19,23', outputspw='23', overwrite=True)


   .. rubric::   Example 5

   This example specifies scaling factor for the correction. The scaling factor can be
   single float value, dictionary of the key-value pair of spw id and the float value
   (e.g. *gainfactor={'23': 50.0, '25': 45.0}*), or name of the caltable that stores
   scaling factor (e.g. *gainfactor='caltablename.tbl'*). Float value is set in this
   example.

   ::

      sdatmcor(infile='sd_data.ms', datacolumn='float_data', outfile='sd_data.atmcor.ms',
      outputspw='23', gainfactor=50.0, overwrite=True)


   .. rubric::   Example 6

   This example shows how to customize atmospheric model.

   ::

      sdatmcor(infile='sd_data.ms', datacolumn='float_data', outfile='sd_data.atmcor.ms',
      outputspw='23', overwrite=True
      atmtype=1, dtem_dh='-5.7K/km', h0='2010m',
      atmdetail=True,
      altitude='5.1km', temperature='290K', pressure='700hPa', humidity=30, pwv='0.1cm',
      dp='10hPa', dpm=1.2, layerboundaries='800m,1.5km', layertemperature='250K,200K')



.. _Development:

Development
   task developer info

