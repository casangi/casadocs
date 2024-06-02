Common Astronomy Software Applications
======================================

`CASA <https://casa.nrao.edu/../>`__, the *Common Astronomy
Software Applications*, is the primary data processing software
for the Atacama Large Millimeter/submillimeter Array
(`ALMA <https://public.nrao.edu/telescopes/alma/>`__) and Karl G.
Jansky Very Large Array
(`VLA <https://public.nrao.edu/venue/the-very-large-array/>`__),
and is often used also for other radio telescopes.

**6.6.4 Release**

CASA 6.6.4 can now be `downloaded <https://casa.nrao.edu/casa_obtaining.shtml>`__ for general use. CASA 6.6.4 is available either as a downloadable tar-file, or through pip-wheel installation, which gives flexibility to integrate CASA into a customized Python environment.

**Highlights:**

-  Mac ARM: CASA builds for Mac ARM are now available (but do not include the Viewer).
- CASA config: addition of a new casaconfig package to handle configuration settings.
- polfromgain: new parameter minpacov to specify minimum parallactic coverage threshold.
- tclean: new mtmfs-via-cube imaging mode (specmode='mvc') with accurate wideband primary beam correction.
- getephemtable: posrefsys keyword changed to ICRS; support non-alphanumeric characters.
- setjy: usescratch defaults to True; False no longer allowed with Butler-JPL-Horizons.
- fixplanets: removed functionality to attach JPL-Horizons ephemeris data in MIME format (use getephemtable instead).
- getantposalma: new task to query ALMA antenna position web service and return list of antenna ITRF positions.

In addition, a number of bugs were fixed.

CASA is being developed by an international consortium of scientists and software engineers based at the National Radio Astronomical Observatory (NRAO), the European Southern Observatory (ESO), the National Astronomical Observatory of Japan (NAOJ), and the Joint Institute for VLBI European Research Infrastructure Consortium (JIV-ERIC), under the guidance of NRAO.
   
.. toctree::
   :hidden:
   :maxdepth: 3

   notebooks/introduction
   genindex
   API (tasks, tools, GUIs, etc.)  <api>
   Task List (shortcut) <api/casatasks>
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
   notebooks/frequently-asked-questions
   notebooks/citing-casa
   changelog
