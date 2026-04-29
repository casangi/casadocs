Common Astronomy Software Applications
======================================

`CASA <https://casa.nrao.edu/../>`__, the *Common Astronomy
Software Applications*, is the primary data processing software
for the Atacama Large Millimeter/submillimeter Array
(`ALMA <https://public.nrao.edu/telescopes/alma/>`__) and Karl G.
Jansky Very Large Array
(`VLA <https://public.nrao.edu/telescopes/vla/>`__),
and is often used also for other radio telescopes.

**6.7.5 Release**

CASA 6.7.5 can now be `downloaded <https://casa.nrao.edu/casa_obtaining.shtml>`__ for general use. CASA 6.7.5 is available either as a downloadable tar-file, or through pip-wheel installation, which gives flexibility to integrate CASA into a customized Python environment.

**Highlights:**

- MacOS 26: support for MacOS 26 was added.
- pccor: new task for pulse delay calibration.
- ft: extended list of data selection parameters.
- fringefit: performance has been improved with speedup of FFT stage.
- sdcal: generates fully flagged calibration solution when OFF_SOURCE data are invalid.
- importasdm: added support for additional optional ASDM columns.

In addition, a large number of bugs were fixed.
   
CASA is being developed by an international consortium of scientists and software engineers based at the National Radio Astronomical Observatory (NRAO), the European Southern Observatory (ESO), the National Astronomical Observatory of Japan (NAOJ), and the Joint Institute for VLBI European Research Infrastructure Consortium (JIVE), under the guidance of NRAO.
   
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
