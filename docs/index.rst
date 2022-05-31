Common Astronomy Software Applications
======================================

`CASA <https://casa.nrao.edu/../>`__, the *Common Astronomy
Software Applications*, is the primary data processing software
for the Atacama Large Millimeter/submillimeter Array
(`ALMA <https://public.nrao.edu/telescopes/alma/>`__) and Karl G.
Jansky Very Large Array
(`VLA <https://public.nrao.edu/venue/the-very-large-array/>`__),
and is often used also for other radio telescopes.

**6.5.0 Release**

CASA 6.5.0 can now be `downloaded <https://casa.nrao.edu/casa_obtaining.shtml>`__ for general use. CASA 6.5.0 is available either as a downloadable tar-file, or through pip-wheel installation, which gives flexibility to integrate CASA into a customized Python environment.

**Highlights:**

- imbaseline: a new task imbaseline was added for image-based baseline subtraction for single-dish data.
- corrbit(): a new method corrbit() was implemented in the msmetadata tool for returning the value in SPECTRAL_WINDOW:: SDM_CORR_BIT column.
- setjy: the parameter 'modimage' was removed and parameter 'model' should be used instead.
- plotms: support was added for additional axes of calibration tables.
- tclean: the return dictionary now includes additional information about the minor cycles.
- Mac OS 12: a bug was fixed which prevented the Mac OS 11 / Python 3.6 package to open on Mac OS 12.

For more details on these and other new features, see the CASA 6.5.0 `Release Notes <https://casadocs.readthedocs.io/en/v6.5.0/notebooks/introduction.html>`__.
   
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
