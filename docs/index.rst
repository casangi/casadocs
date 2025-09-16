Common Astronomy Software Applications
======================================

`CASA <https://casa.nrao.edu/../>`__, the *Common Astronomy
Software Applications*, is the primary data processing software
for the Atacama Large Millimeter/submillimeter Array
(`ALMA <https://public.nrao.edu/telescopes/alma/>`__) and Karl G.
Jansky Very Large Array
(`VLA <https://public.nrao.edu/venue/the-very-large-array/>`__),
and is often used also for other radio telescopes.

**6.6.6 Release**

CASA 6.6.6 can now be `downloaded <https://casa.nrao.edu/casa_obtaining.shtml>`__ for general use. CASA 6.6.6 is based on CASA 6.6.5, and the downloadable tar-file includes the pipeline for ALMA Cycle 12 and the VLA. 

**Highlights:**

- phaseshift: added multi-field specification of the phasecenter parameter. 
- gencal: added support for the output of task getantposalma. 
- simalma: ALMA Cycle-12 configurations files were added.
- tsdimaging/sdimaging: weight value for Stokes I properly derived from linear/circular correlations. 
- getantposalma: default value of snr changed to the one used by the web service.
- plotbandpass: support of band-to-band calibration.
- plotbandpass: plotting of hsd_skycal solutions.
- plotbandpass: added features similar of the corresponding analysisUtils version.

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
