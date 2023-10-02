Common Astronomy Software Applications
======================================

`CASA <https://casa.nrao.edu/../>`__, the *Common Astronomy
Software Applications*, is the primary data processing software
for the Atacama Large Millimeter/submillimeter Array
(`ALMA <https://public.nrao.edu/telescopes/alma/>`__) and Karl G.
Jansky Very Large Array
(`VLA <https://public.nrao.edu/venue/the-very-large-array/>`__),
and is often used also for other radio telescopes.

**6.5.4 Release**

CASA 6.5.4 can now be `downloaded <https://casa.nrao.edu/casa_obtaining.shtml>`__ for general use. CASA 6.5.4 is based on CASA 6.5.3, and the downloadable tar-file includes the pipelines for ALMA Cycle 10. 

**Highlights:**

- applycal: handles calibration tables that have fewer SPWs than the MS they are being applied to 
- simobserve: edited the lower frequency edge of ALMA Band 1 to be 50 GHz.
- casadata: added alma cycle 10 configuration files.
- gencal: a bug was fixed where VLA antenna position offsets were not taken into account.
- plotbandpass: a bug was fixed to display missing information when plotting single dish caltables.
- plotms: a bug was fixed for autoscaling point size with colorization.

For more details on these and other new features, see the CASA 6.5.4 `Release Notes <https://casadocs.readthedocs.io/en/v6.5.4/notebooks/introduction.html>`__.

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
