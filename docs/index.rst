Common Astronomy Software Applications
======================================

`CASA <https://casa.nrao.edu/../>`__, the *Common Astronomy
Software Applications*, is the primary data processing software
for the Atacama Large Millimeter/submillimeter Array
(`ALMA <https://public.nrao.edu/telescopes/alma/>`__) and Karl G.
Jansky Very Large Array
(`VLA <https://public.nrao.edu/venue/the-very-large-array/>`__),
and is often used also for other radio telescopes.

**6.5.2 Release**

CASA 6.5.2 can now be `downloaded <https://casa.nrao.edu/casa_obtaining.shtml>`__ for general use. CASA 6.5.2 is available either as a downloadable tar-file, or through pip-wheel installation, which gives flexibility to integrate CASA into a customized Python environment.

**Highlights:**

- deconvolve: new task for image-domain deconvolution.
- uvcontsub: new implementation, old uvcontsub task deprecated.
- fringefit: support added for 'uvrange' parameter.
- tclean: new iteration control parameter 'nmajor'.
- sdimaging: new parameter 'enablecache' for improved performance.
- mstransform: parameter 'douvcontsub' deprecated.
- flagdata: mode='shadow' now uses the uvw values from the UVW column.
- tclean/tsdimaging: improved runtime performance of ephemeris imaging.
- simulator tool: new parameter 'simint' in sm.settrop() to control time granularity, down to 0.1s.
- ImageAnalysis tool: new string 'mbret' parameter added to 'image.restoringbeam()'.
- casalog tool: new method 'getOrigin()' implemented to retrieve origin of messages.

For more details on these and other new features, see the CASA 6.5.2 `Release Notes <https://casadocs.readthedocs.io/en/v6.5.2/notebooks/introduction.html>`__.

   
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
