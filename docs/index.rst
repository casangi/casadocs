Common Astronomy Software Applications
======================================

`CASA <https://casa.nrao.edu/../>`__, the *Common Astronomy
Software Applications*, is the primary data processing software
for the Atacama Large Millimeter/submillimeter Array
(`ALMA <https://public.nrao.edu/telescopes/alma/>`__) and Karl G.
Jansky Very Large Array
(`VLA <https://public.nrao.edu/venue/the-very-large-array/>`__),
and is often used also for other radio telescopes.

**6.6.3 Release**

CASA 6.6.3 can now be `downloaded <https://casa.nrao.edu/casa_obtaining.shtml>`__ for general use. CASA 6.6.3 is available either as a downloadable tar-file, or through pip-wheel installation, which gives flexibility to integrate CASA into a customized Python environment.

**Highlights:**

- Google Colab: Pip-wheels for Python 3.10 (Google Colab) are now available and compatible with matplotlib.
- getephemtable: new task to retrieve JPL-Horizons ephemeris data. 
- getcalmodvla: new task to to retrieve flux calibrator brightness distributions and create component lists.
- gencal: new parameter ant_pos_time to limit period for which antenna position corrections are included. 
- tec_maps: now consistent with new file-naming convention on remote CDDIS server.
- tclean: algorithmic improvements to the ASP deconvolver for large spread of spatial scales.
- tclean/sdintimaging: now sorts input list of MSes in chronological order.
- tclean/sdintimaging: now checks for mismatches in column states when given multiple input MSs. 
- simulator: simutil now performs case sensitive comparisons for ‘known observatories’.
- plotms: correlation selection now supports standard Stokes parameters and polarization quantities.

In addition, a number of bugs were fixed.
   
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
