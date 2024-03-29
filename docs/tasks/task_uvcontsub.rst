

.. _Returns:

Returns
   gof (dict) - goodness of fit statistics grouped by field, scan,
   SPW, polarization and real/imaginary part


.. _Description:

Description
   .. note:: The task **uvcontsub** has been updated. It does not yet
      support combining spws for fitting. If you need this
      functionality please use uvcontsub_old.
   
   .. note:: Strictly speaking, the continuum fitted produced by this
      task is only a good representation of the continuum at the phase
      center. Residuals may be visible for sources far away and one
      may wish to try the following for improved results: a) shifting
      the phase center of the data to the location of the continuum
      source, uv continuum subtracting, and then shifting the data
      back or b) try **imcontsub** in the image domain.

   This task can perform continuum fitting and subtraction in the uv
   domain.

   The function estimates the continuum emission by fitting
   polynomials to the real and imaginary parts of the data. The
   spectral windows and channels on which the fitting is calculated
   can be specified using the parameter *fitspec*. The resulting fit
   represents a model of the continuum in all channels. The fitted
   continuum spectrum is subtracted from all channels selected in
   *spw*, and the result (intended as line emission only) is produced
   in an output MeasurementSet. Polynomial models are fitted and
   subtracted per integration, per baseline, per correlation. Note
   that because the real and imaginary parts are fitted separately,
   the fitted model amplitude has the functional form of
   sqrt(<*polynomial of order fitorder* * 2>) which, in general, is
   not a polynomial.

   The function returns a dictionary with goodness of fit metrics,
   grouped by field, scan, SPW, polarization, and real and imaginary
   part. The goodness of fit metric included in the dictionary is the
   chi-squared values as calculated and minimized by the fitting
   algorithms. The fields *count* found in the dictionary give the
   number of polynomials fitted for every group (one individual
   polynomial fit for every data row and polarization, and real and
   imaginary parts). Simple statistics (average, minimum, and maximum)
   of the goodness of fit values for every field/scan/SPW/polarization
   group are given in the dictionary, see examples section.

   The input MeasurementSet is not modified (is only read). The data
   column from the input MeasurementSet that is read can be selected
   using the *datacolumn* parameter. The continuum subtracted data are
   written into the DATA column of the output MS. Optionally, and to
   support inspection of results and debugging, the fitted model data
   can be written into the MODEL column of the output MS, using the
   parameter *writemodel*. When selection parameters (field, spw,
   scan, etc.) are used, the output MS includes only the data selected
   via those selection parameters. Note that uvcontsub takes as input
   the DATA column by default unless the user sets a different value
   for *datacolumn*. This behavior is different from older uvcontsub
   tasks where the CORRECTED data column is taken as input if
   available, otherwise falling back to DATA.

   The fitting method and polynomial order are chosen via the
   parameters *fitmethod* and *fitorder*. It is also possible to use
   different polynomial orders for different fields and SPWs when
   *fitspec* takes the form of a dictionary. The line-free channels
   are given in the *fitspec* parameter. In it simplest form, it is a
   single line-free channel specification string that applies to all
   fields. It can also be a dictionary, with different line-free
   channel specifications and polynomial order for different fields
   and SPWs. This is to be able to produce an output MeasurementSet
   with multiple sources and/or fields in one single call. The per-SPW
   line-free channels are specified using the spw:channel notation,
   see the `MS selection syntax
   <../../notebooks/visibility_data_selection.ipynb>`__.

   In addition to the *fitspec* parameter, the channelized data flags
   and data weights also influence how the channels will be used for
   the purpose of fitting the continuum. Channels that are flagged are
   effectively excluded for the purpose of fitting (equivalent to
   excluding them from fitspec). The channel weights, adjusted for
   example using the statwt task, also influence how relevant
   different channels will be for the fitting, in a more gradual
   way.

   For more details on how continuum subtraction is performed in the
   uv domain, use of flags and weights, fitting methods, goodness of
   fit, etc. see `UV Continuum Subtraction
   <../../notebooks/uv_manipulation.ipynb#UV-Continuum-Subtraction>`__.


.. _Examples:

Examples
   **Example 1:**

   Subtract the continuum of channels 10~100 and 300~350 in spw 0
   (assuming that the line is in channels 101~299). Note that we also
   exclude edge channels, e.g. the first 9 channels. We use a
   fitorder of 0 (default):

   .. code-block:: python

      result = uvcontsub(vis='input_ms.ms', outputvis='vis_line.ms', fitspec='0:10~100;300~350')
      # result has contents as in the following example (excerpt):
      result
      {'description': 'summary of data fitting results in uv-continuum subtraction',
       'goodness_of_fit': {'field': {'0': {'scan': {'1': {'spw': {'0': {'polarization':
       {'0': {'chi_squared': {'average': {'imag': 1.05,
                                           'real': 0.964},
                              'max': {'imag': 1.11,
                                      'real': 1.08},
                               'min': {'imag': 1.02,
                                       'real': 0.74}},
              'count': 40},
        '1': {'chi_squared': {'average': {'imag': 1.05,
                                          'real': 1.04},
                              'max': {'imag': 1.06,
                                      'real': 1.15},
                              'min': {'imag': 0.992,
                                      'real': 0.954}},
              'count': 40}}}}}}}}}
      }

   **Example 2:**

   Subtract the continuum of channels 10~100 and 300~350 in spw 0,
   with fit order of 1. This example is very similar to the previous
   one but we just increase the order of the polynomials
   fitted:

   .. code-block:: python

      uvcontsub(vis='input_ms.ms', outputvis='vis_line.ms', fitorder=1, fitspec='0:10~100;300~350')

   **Example 3:**

   Our input MS has two fields. We use one call to uvcontsub to make a
   single field MS for the first field, and then a second call to make
   a single field MS for the second field of the input MS:

   .. code-block:: python

      uvcontsub(vis='input_ms.ms', outputvis='field0_line.ms', field=0, fitspec='0:10~100;300~350', fitorder=0)
      uvcontsub(vis='input_ms.ms', outputvis='field1_line.ms', field=1, fitspec='0:20~90;200~350', fitorder=1)

   **Example 4:**

   Alternative to previous example, give fitspec as dictionary and produce
   an output MS with 2 fields:

   .. code-block:: python

      spec = {'0': {'19': {'chan': '10~100;300~350', 'fitorder': 0}}}, {'1': {'19': {'chan': '20~90;200~350', 'fitorder': 1}}}
      uvcontsub(vis='input_ms.ms', outputvis='vis_line.ms', fitspec=spec)

   **Example 5:**

   To ease analysis of the fitted model, we produce an output MS with
   the continuum subtracted data in the DATA column, and the fitted
   model in the MODEL column. In contrast to the examples above,
   *fitspec* is not specified which implies that all channels are used
   for fitting purposes in all the SPWs:

   .. code-block:: python
   
      uvcontsub(vis='input_ms.ms', outputvis='vis_line.ms', writemodel=True)

   **Example notebook**

   Examples of simulated MeasurementSets that can be used to evaluate
   uvcontsub are included in this `Jupyter notebook
   <../../notebooks/simulations_uvcontsub_ALMA.ipynb>`__ with demo
   scripts. The notebook is available on `Google Colab
   <https://colab.research.google.com/github/casangi/casadocs/blob/master/docs/notebooks/simulations_uvcontsub_ALMA.ipynb>`_,
   where the demo scripts can be run from the browser (or retrieved to
   be run locally). The verification tests of this task include
   numerical tests based on simulated data from the notebook. These
   numerical verification tests check the accuracy of the continuum
   fits produced by uvcontsub. For example, for polynomials of known
   coefficients, for order 0, 1, and 2, added artificially to the
   visibilities, the accuracy of the fitted polynomials is better than
   10e-5 (measured as relative residual values through all channels
   and rows). For a polynomial of order 0, with added Gaussian random
   noise and continuum SNR of ~3.5, the relative residuals are of the
   order of 1% (~3% for the 75th percentile). The scripts included in
   the notebook can also be used to further characterize the behavior
   of the task for different data properties, and to run other
   experiments with the task.

.. _Development:

Development
   This version of uvcontsub is defined to satisfy the operational
   requirements of the pipelines and SRDP, as best as they could be
   identified throughout 2021. Additional features (or use modes) can
   be considered:

   - Channel specifications in *fitspec* are supported in the native
     frame of the input MeasurementSet. The suggestion is that frame
     conversions, when needed, be handled in separate (helper)
     functions rather than embedded in the task.

   - SPW combination, related to the *combine* parameter of the task
     **uvcontsub_old**.

   - Phase shifting related features and parameters (see task
     **phaseshift**).

   - Some CASA tasks have a parameter **excludechans** that inverts
     the channel specification of fitspec (the channels given in fitswp
     are excluded from the fitting instead of included). This
     functionality would be provided separately in a helper function.

   - It is expected that additional tests and support will be needed
     as future work once higher order polynomials and robust fitting
     are tried out, as well as phasecenter shifts, etc. New
     simulations might be needed.
