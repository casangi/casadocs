Common Astronomy Software Applications
======================================

`CASA <https://casa.nrao.edu/../>`__, the *Common Astronomy
Software Applications*, is the primary data processing software
for the Atacama Large Millimeter/submillimeter Array
(`ALMA <https://public.nrao.edu/telescopes/alma/>`__) and Karl G.
Jansky Very Large Array
(`VLA <https://public.nrao.edu/venue/the-very-large-array/>`__),
and is often used also for other radio telescopes.

**6.5.6 Release**

CASA 6.5.6 can now be `downloaded <https://casa.nrao.edu/casa_obtaining.shtml>`__ for general use. CASA 6.5.6 is available either as a downloadable tar-file, or through pip-wheel installation, which gives flexibility to integrate CASA into a customized Python environment.

**Highlights:**

- msuvbin: new experimental task to save a measurement set as a UV grid. 
- fringefit: allows the use of the cal library to apply pre-calibration. 
- simobserve: support for component lists having higher order spectral terms. 
- table tool: new table tool method tb.getcoliter(), for iterator access to casacore tables.
- applycal: handles calibration tables with fewer SPWs than the MS they are being applied to. 
- infrastructure: the CASA6 build system has been refactored to improve modularity within the code base, to better streamline dependency management, and to support future development and deployment requirements. The 6.5.6 release marks the start of production packages with the new build system.

In addition, a number of bugs were fixed, including (but not limited to):

- gencal: fixed jyperk caltype not handling polarization dependent Jy/K conversion properly. 
- tclean: fixed cube imaging with perchanweightdensity, and size of psf for specmode=’mfs’. 
- xml-casa (rmtables): fixed bug that disabled automatic parameter type coercion. 
- imsmooth: fixed adding the correct beam to output image metadata.
- tclean: fixed model saving control when a list of MSes is specified. 
- plotbandpass: fixed missing information when plotting single dish caltables.
- imbaseline/sdbaseline/sdcal: fixed problem where libsakura that caused a crash.

For more details on these and other new features, see the CASA 6.5.6 `Release Notes <https://casadocs.readthedocs.io/en/v6.5.6/notebooks/introduction.html>`__.

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
