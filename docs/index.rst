Common Astronomy Software Applications
======================================

`CASA <https://casa.nrao.edu/../>`__, the *Common Astronomy
Software Applications*, is the primary data processing software
for the Atacama Large Millimeter/submillimeter Array
(`ALMA <https://public.nrao.edu/telescopes/alma/>`__) and Karl G.
Jansky Very Large Array
(`VLA <https://public.nrao.edu/telescopes/vla/>`__),
and is often used also for other radio telescopes.

**6.7.7 Release**

CASA 6.7.7 can now be `downloaded <https://casa.nrao.edu/casa_obtaining.shtml>`__ for general use. CASA 6.7.7 is available either as a downloadable tar-file (Linux), a downloadable DMG (MacOS) or through pip-wheel installation, which gives flexibility to integrate CASA into a customized Python environment.

**Highlights:**

- zenithdelaycal: new task to calibrate the Zenith delay and clock difference (AIPS/DELZN).
- tclean: new parameter fracbw to set fractional bandwidth for briggsbwtaper.
- tclean: negative pblimit now removes image mask for standard wproject gridders.
- tclean: improved flux consistency between gridders for small fields of view.
- tclean: optimization of automasking algorithm.
- importasdm: new experimental parameter use_durations to set EXPOSURE column in MS.
- getantposalma: new default for 'auto' search with updated URL.
- casaconfig: updated URL for ASTRON measures data.

In addition, a large number of bugs were fixed.

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
   notebooks/contact
   changelog
