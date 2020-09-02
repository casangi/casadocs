Common Astronomy Software Applications
======================================
   

   `CASA <https://casa.nrao.edu/../>`__, the*Common Astronomy
   Software Applications*, is the primary data processing software
   for the Atacama Large Millimeter/submillimeter Array
   (`ALMA <https://public.nrao.edu/telescopes/alma/>`__) and Karl G.
   Jansky Very Large Array
   (`VLA <https://public.nrao.edu/venue/the-very-large-array/>`__),
   and is often used also for other radio telescopes.

   CASA 5.7/6.1 can now be
   `downloaded <https://casa.nrao.edu/../casa_obtaining.shtml>`__ for
   general use. CASA 5.7 is based on Python 2, while CASA 6.1 is
   based on Python 3, but both contain the same functionality. CASA
   6.1 is available either as a downloadable tar-file (much like CASA
   5.7), or through `pip-wheel
   installation <https://casa.nrao.edu/casadocs-devel/stable/usingcasa/obtaining-and-installing>`__,
   which gives flexibility to integrate CASA into a customized Python
   environment.

   The CASA 5.7/6.1 release builds on CASA 5.6, but has the following
   main new features:

   .. rubric:: New Features
      

   -  A new task sdintimaging is available for jont deconvolution of
      Single Dish and Interfermeter data.
   -  A new task sdtimeaverage is available for averaging single-dish
      spectral data over specified time.
   -  A new single-dish spectral imaging mode, 'cubesource', is
      available in the task tsdimaging.
   -  A new parameter corrdepflags has been added to the gaincal,
      bandpass, and fringefit tasks to permit more control of
      flagging subsets of correlations.
   -  The fringefit task now includes support for dispersive delays.
   -  The CASA simulator now uses tclean instead of clean.
   -  The ability to correct for heterogeneous antenna pointing
      offsets stored in the POINTING sub-table of the MS has been
      added totclean(gridder='awproject').
   -  statwt now includes weighting each visibility by its exposure
      time, and also improved in the way the timebin parameter is
      interpreted when its value is an integer.
   -  the imsmooth task has been made consistency with the rest of
      CASA in terms of masking
   -  simobserve now reads and populates antenna names rather than
      assigning numbers, which makes comparing simulated and real
      data easier.
   -  The fldmap parameter within the cal library will now support
      multiple fields
   -  `CARTA <https://casa.nrao.edu/casadocs-devel/stable/imaging/carta>`__ v.1.3
      with limited features is now available for users who wish to
      visualize their data outside the CASA Viewer.
   -  VLA P-band models have been made available in CASA forseveral
      standard calibrators.
   -  Ephemeris tables for Solar System objects have been extended in
      time
   -  An "execfile" python shortcut has been added to the (Python 3
      based) CASA 6 environment for backwards compatibility with ALMA
      scriptForPI.py restore scripts.

   For more details and other implementations, please see the CASA
   5.7/6.1 `Release
   Notes <https://casa.nrao.edu/casadocs-devel/stable/introduction/release-notes-610>`__.

   

   *CASA is developed by an international consortium of scientists
   based at the National Radio Astronomical Observatory (NRAO), the
   European Southern Observatory (ESO), the National Astronomical
   Observatory of Japan (NAOJ), the Academia Sinica Institute of
   Astronomy and Astrophysics (ASIAA), CSIRO Astronomy and Space
   Science (CSIRO/CASS), and the Netherlands Institute for Radio
   Astronomy (ASTRON), under the guidance of NRAO.*

.. toctree::
   :hidden:
   :maxdepth: 3

   notebooks/introduction
   notebooks/usingcasa
   notebooks/casa-fundamentals
   notebooks/external-data
   notebooks/calibration-and-visibility-data
   notebooks/imaging
   notebooks/pipeline
   notebooks/simulation
   task_api
   tool_api
   notebooks/parallel-processing
   notebooks/memo-series
   notebooks/casa-development-team
