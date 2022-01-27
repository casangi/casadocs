Common Astronomy Software Applications
======================================

`CASA <https://casa.nrao.edu/../>`__, the *Common Astronomy
Software Applications*, is the primary data processing software
for the Atacama Large Millimeter/submillimeter Array
(`ALMA <https://public.nrao.edu/telescopes/alma/>`__) and Karl G.
Jansky Very Large Array
(`VLA <https://public.nrao.edu/venue/the-very-large-array/>`__),
and is often used also for other radio telescopes.

**6.4.3 Release**

CASA 6.4.3 can now be (`downloaded <https://casa.nrao.edu/casa_obtaining.shtml>`__) for general use. CASA 6.4.3 is available either as a downloadable tar-file, or through pip-wheel installation, which gives flexibility to integrate CASA into a customized Python environment.

**Highlights:**

- gencal: a new caltype parameter 'jyperk' is now available.
- tclean: mixed polarization setups can now be handled in imaging.
- flagdata: improvements were made regarding input checks, executing complex commands, and flagging with time or channel averaging.
- importasdm/exportasdm: parameters 'showversion' and 'useversion' were deprecated and removed from the task-code and sdm tool.
- a number of bugs were fixed.

For more details on these and other new features, see the CASA 6.4.3 (`Release Notes <https://casadocs.readthedocs.io/en/v6.4.3/notebooks/introduction.html>`__).
   
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
