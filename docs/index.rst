Common Astronomy Software Applications
======================================

`CASA <https://casa.nrao.edu/../>`__, the *Common Astronomy
Software Applications*, is the primary data processing software
for the Atacama Large Millimeter/submillimeter Array
(`ALMA <https://public.nrao.edu/telescopes/alma/>`__) and Karl G.
Jansky Very Large Array
(`VLA <https://public.nrao.edu/venue/the-very-large-array/>`__),
and is often used also for other radio telescopes.

**6.4.0 Release**

CASA 6.4.0 can now be (`downloaded <https://casa.nrao.edu/casa_obtaining.shtml>`__) for general use. CASA 6.4.0 is available either as a downloadable tar-file, or through pip-wheel installation, which gives flexibility to integrate CASA into a customized Python environment.

**Highlights:**

- OS Support: CASA now supports RedHat 8, and Mac OS with Python 3.8, for both monolithic and modular versions. Note the Linux tarballs with different Python versions will extract to the same directory name.
- plotcal/plotms: Funtionality for plotcal has been migrated to plotms, and plotcal was deprecated.
- plotms: calibration table averaging with channel selection is now supported.
- fringefit: memory usage of fringefit has been reduced, allowing larger datasets to be processed.
- imhead: updated to display microsecond precision.
- caltables: the storage of frequency meta information in caltables improved, making certain frequency-dependent calibration solutions more accurate.
- sdintimaging: now adds information to the history of produced images
- T+dT timerange selection improved in accuracy.

For more details on these and other new features, see the CASA 6.4.0 (`Release Notes <https://casadocs.readthedocs.io/en/v6.4.0/notebooks/introduction.html>`__).
   
CASA is developed by an international consortium of scientists
based at the National Radio Astronomical Observatory (NRAO), the
European Southern Observatory (ESO), the National Astronomical
Observatory of Japan (NAOJ), the Academia Sinica Institute of
Astronomy and Astrophysics (ASIAA), CSIRO Astronomy and Space
Science (CSIRO/CASS), and the Netherlands Institute for Radio
Astronomy (ASTRON), under the guidance of NRAO.
   
.. toctree::
   :hidden:
   :maxdepth: 3

   notebooks/introduction
   genindex
   api
   Task List <api/casatasks>
   notebooks/usingcasa
   notebooks/casa-fundamentals
   notebooks/external-data
   calibration
   imaging
   notebooks/carta
   notebooks/pipeline
   notebooks/simulation
   notebooks/parallel-processing
   notebooks/memo-series
   examples/index
   changelog
