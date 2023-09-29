Common Astronomy Software Applications
======================================

`CASA <https://casa.nrao.edu/../>`__, the *Common Astronomy
Software Applications*, is the primary data processing software
for the Atacama Large Millimeter/submillimeter Array
(`ALMA <https://public.nrao.edu/telescopes/alma/>`__) and Karl G.
Jansky Very Large Array
(`VLA <https://public.nrao.edu/venue/the-very-large-array/>`__),
and is often used also for other radio telescopes.

**6.6.0 Release**

CASA 6.6.0 can now be `downloaded <https://casa.nrao.edu/casa_obtaining.shtml>`__ for general use. CASA 6.6.0 is available either as a downloadable tar-file, or through pip-wheel installation, which gives flexibility to integrate CASA into a customized Python environment.

**Highlights:**

- Google Colab: Pip-wheels for Python 3.10 (Google Colab) are now available.
- Installation: test script added to test the CASA installation.
- defintent: new task to modify the scan intents of a measurement set.
- sdimaging: new parameter convertfirst, to reduce the number of direction conversions.
- deconvolve: mtmfs enabled as an algorithm option.
- image tool: fitsheader function added to return FITS header as Python dictionary.
- tclean/deconvolve: return dictionaries added for niter=0 calls.
- plotms: parameter colorizeoverlay added to better specify overlay colors.
- plotms: better specifies values in the legend when coloraxis is set.
- Multiple MS input: clarifications added to the CASA logger on how CASA handles input of multiple MSs.
- telemetry/crash reporter: functionality deprecated

In addition, a number of bugs were fixed.

For more details on these and other new features, see the CASA 6.6.0 `Release Notes <https://casadocs.readthedocs.io/en/v6.6.0/notebooks/introduction.html>`__.

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
