.. _Description:

Description
   .. note:: **uvcontsub2021** is a new task expected to eventually
      replace the tasks **uvcontsub** and **uvcontsub3**, as well as
      the **douvcontsub** feature of **mstransform**.
   
   This task can perform continuum fitting and subtraction in the uv
   domain.

   The function estimates the continuum emission by fitting polynomials to
   the real and imaginary parts of the data. The spectral windows and
   channels on which the fitting is calculated can be selected using
   the parameter *fitspw*. The resulting fit represents a model of the
   continuum in all channels. The fitted continuum spectrum is
   subtracted from all channels selected in *spw*, and the result
   (intended as line emission only) is produced in an output
   MeasurementSet. Polynomial models are fitted and subtracted per
   integration, per baseline, correlation.

   The function returns a dictionary with goodness of fit metrics,
   grouped by field, scan, SPW, polarization, and real and imaginary
   part. The dictionary includes chi-square values as calculated and
   minimized by the fitting algorithms. [NOTE/TODO: details to be
   finalized, see discussion in development documents].

   The input MeasurementSet is not modified (is only read). The data
   column from the input MeasurementSet that is read can be selected
   using the *datacolumn* parameter. The continuum subtracted data are
   written into the DATA column of the output MS. Optionally, and to
   support inspection of results and debugging, the fitted model data
   can be written into the MODEL column of the output MS, using the
   parameter *writemodel*.

   The fitting method and polynomial order are selected via the
   parameters *fitmethod* and *fitorder*. The line-free channels are
   given in the *fitspw* parameter. In it simplest form, it is a
   line-free channel specification string that applies to all
   fields. It can also take a list of line-free channel
   specifications, with an item per field or group or fields. This is
   to be able to produce an output MeasurementSet with multiple
   sources and/or fields in one single call. The per-SPW line-free
   channels are specified using the spw:channel notation, see the `MS
   selection syntax
   <../../notebooks/visibility_data_selection.ipynb>`__.

   In addition to the *fitspw* parameter, the channelized data flags
   and data weights also influence how the channels will be used for
   the purpose of fitting the continuum. Channels that are flagged are
   effectively excluded for the purpose of fitting (equivalent to
   excluding them from fitspw). The channel weights, adjusted for
   example using the statwt task, also influence how relevant
   different channels will be for the fitting, in a more gradual
   way. See `UV Continuum Subtraction
   <../../notebooks/uv_manipulation.ipynb#UV-Continuum-Subtraction>`__
   for more details.

..
    Notes taken from the pages of uvcontsub(1) and uvcontsub3:

   .. note:: Strictly speaking, the continuum fitted produced by this
      task is only a good representation of the continuum at the phase
      center. Residuals may be visible for sources far away and one
      may try **imcontsub** in the image domain for improved results.

   .. note:: values of *fitorder* > 1 should be used with care. Higher
      order polynomials are more flexible, and may overfit and absorb
      line emission. They also tend to go wild at the edges of
      *fitspw*,

   .. note:: Because the continuum model is necessarily a smoothed
      fit, images made with it are liable to have their field of view
      reduced in some strange way. Images of the continuum should be
      made by simply excluding the line channels (and probably
      averaging the remaining ones) in **tclean**.

.. _Examples:

Examples
   **Example 1:**

   Subtract the continuum of channels 10~100 and 300~350 in spw 0
   (assuming that the line is in channels 101~299). Note that we also
   exclude edge channels, e.g. the first 9 channels. We use a
   fitorder of 0 (default):

   .. code-block:: python

      uvcontsub2021(vis='input_ms.ms', outputvis='vis_line.ms', fitspw='0:10~100;300~350')

   **Example 2:**

   Subtract the continuum of channels 10~100 and 300~350 in spw 0,
   with fit order of 1. This example is very similar to the previous
   one but we just increase the order of the polynomials
   fitted:

   .. code-block:: python

      uvcontsub2021(vis='input_ms.ms', outputvis='vis_line.ms', fitorder=1, fitspw='0:10~100;300~350')

   **Example 3:**

   Our input MS has two fields. We use one call to uvcontsub to make a
   1 field MS for the first field, and a second call to make a 1 field
   MS for the second field of the input MS: to make the second field
   MS. The *fitspw* is not specified which implies that all channels
   are used for fitting purposes in all the SPWs:

   .. code-block:: python

      uvcontsub2021(vis='input_ms.ms', outputvis='field0_line.ms', field=0)
      uvcontsub2021(vis='input_ms.ms', outputvis='field1_line.ms', field=1)

   **Example 4:**

   Alternative to previous example, give fitspw as array and produce
   an output MS with 2 fields:

   .. code-block:: python
   
      uvcontsub2021(vis='input_ms.ms', outputvis='vis_line.ms', fitspw=[['0', '0:10~100;300~350'], ['1', '0:20~90;200~350']])

   **Example 5:**

   To ease analysis of the fitted model, we produce an output MS with
   the continuum subtracted data in the DATA column, and the fitted
   model in the MODEL column:

   .. code-block:: python
   
      uvcontsub2021(vis='input_ms.ms', outputvis='vis_line.ms', writemodel=True)


   Placeholder (work in progress) paragraph about numerical
   characterization. This will link to a Jupyter notebook with demo
   scripts. The notebook will be available online, hosted on `Google
   Colab
   <https://colab.research.google.com/github/casangi/casadocs/blob/master/docs/notebooks/>`_,
   where the demo scripts can be run from the browser (or retrieved to
   be run locally). The notebook will characterize the correctness of
   the results produced by uvcontsub based on simulated data. The
   scripts contained in the notebook can also be used to run
   experiments with the task, see the task **phaseshift** for an
   example.

.. _Development:

Development
   This version of uvcontsub is defined to satisfy the operational
   requirements of the pipelines and SRDP, as best as they could be
   identified throughout 2021. Additional features (or use modes) can
   be considered:

   - Channel selections in *fitspw* are supported in the native frame
     of the input MeasurementSet. The suggestion is that frame
     conversions, when needed, be handled in separate (helper)
     functions rather than embedded in the task.

   - SPW combination, related to the *combine* parameter of the tasks
     **uvcontsub(1)** and **uvcontsub3**.

   - Phase shifting related features and parameters (see task
     **phaseshift**).

   - Some CASA tasks have a parameter **excludechans** that inverts
     the channel specification of fitspw (the channels given in fitswp
     are excluded from the fitting instead of included). This
     functionality would be provided separately in a helper function.

   - It is expected that additional tests and support will be needed
     as future work once higher order polynomials and robust fitting
     are tried out, as well as phasecenter shifts, etc. New
     simulations might be needed.
