Common Astronomy Software Applications
======================================

`CASA <https://casa.nrao.edu/../>`__, the *Common Astronomy
Software Applications*, is the primary data processing software
for the Atacama Large Millimeter/submillimeter Array
(`ALMA <https://public.nrao.edu/telescopes/alma/>`__) and Karl G.
Jansky Very Large Array
(`VLA <https://public.nrao.edu/venue/the-very-large-array/>`__),
and is often used also for other radio telescopes.

**6.5.3 Release**

CASA 6.5.3 can now be `downloaded <https://casa.nrao.edu/casa_obtaining.shtml>`__ for general use. CASA 6.5.3 is available either as a downloadable tar-file, or through pip-wheel installation, which gives flexibility to integrate CASA into a customized Python environment.

**Highlights:**

- modular CASA: separate python wheels for casafeather, casabrowser and casalogger GUIs.
- setjy: updated VLA flux calibrator model images at C, X and Ka bands.
- tclean: corrected the math implemented for the uvtaper weighting scheme.
- tclean: increased MPI records, and new parameter fullsummary to avoid issues with large cubes.
- tclean/tsdimaging: performance improvement of ~10-16%.
- simulator: now works with primary beams and a component list with spectral structure.
- gaincal/bandpass: return a dictionary reporting on results.
   
For more details on these and other new features, see the CASA 6.5.3 `Release Notes <https://casadocs.readthedocs.io/en/v6.5.3/notebooks/introduction.html>`__.

CASA is being developed by an international consortium of scientists and software engineers based at the National Radio Astronomical Observatory (NRAO), the European Southern Observatory (ESO), the National Astronomical Observatory of Japan (NAOJ), and the Joint Institute for VLBI European Research Infrastructure Consortium (JIV-ERIC), under the guidance of NRAO.
   
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
   notebooks/citing-casa
   changelog
