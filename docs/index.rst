Common Astronomy Software Applications
======================================

`CASA <https://casa.nrao.edu/../>`__, the *Common Astronomy
Software Applications*, is the primary data processing software
for the Atacama Large Millimeter/submillimeter Array
(`ALMA <https://public.nrao.edu/telescopes/alma/>`__) and Karl G.
Jansky Very Large Array
(`VLA <https://public.nrao.edu/venue/the-very-large-array/>`__),
and is often used also for other radio telescopes.

**6.5.5 Release**

CASA 6.5.5 can now be `downloaded <https://casa.nrao.edu/casa_obtaining.shtml>`__ for general use. CASA 6.5.5 is available either as a downloadable tar-file, or through pip-wheel installation, which gives flexibility to integrate CASA into a customized Python environment.

**Highlights:**

- fringefit: allows combined solving of correlations via the corrcomb parameter.
- fringefit: new functionality with concatspws or combine=‘spw’.
- tclean: enabled more stable cube imaging with the awproject gridder 
- plotms: exports text data with more sufficient precision. 
- setjy: will catch an unreasonable input spectral index value. 
- msmetadata tool: includes ALMA-specific methods rxbands() and subwindows().
- applycal: now has per-scan interpolation.

In addition, a number of bugs were fixed, including (but not limited to):

- tclean: numerical fixes with the w-term correction within awproject.
- tclean: not recognizing the observatory name.
- gencal: not always taking antenna position offsets properly into account.
- sdfit/importasap: invalid memory access.
- an MPI issue with Ubuntu.

Casacore was also updated from Aug 2022 - Mar 2023.

For more details on these and other new features, see the CASA 6.5.5 `Release Notes <https://casadocs.readthedocs.io/en/v6.5.5/notebooks/introduction.html>`__.

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
