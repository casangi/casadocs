Common Astronomy Software Applications
======================================

`CASA <https://casa.nrao.edu/../>`__, the *Common Astronomy
Software Applications*, is the primary data processing software
for the Atacama Large Millimeter/submillimeter Array
(`ALMA <https://public.nrao.edu/telescopes/alma/>`__) and Karl G.
Jansky Very Large Array
(`VLA <https://public.nrao.edu/venue/the-very-large-array/>`__),
and is often used also for other radio telescopes.

**6.7.0 Release**

CASA 6.7.0 can now be `downloaded <https://casa.nrao.edu/casa_obtaining.shtml>`__ for general use. CASA 6.7.0 is available either as a downloadable tar-file, or through pip-wheel installation, which gives flexibility to integrate CASA into a customized Python environment.

**Highlights:**

- Intel Macs: CASA 6.7.0 no longer runs on Mac OS Intel x86 machines.
- CASA Viewer: the CASA Viewer is no longer packaged with Mac OS.
- sdimaging: task sdimaging is deprecated (use tsdimaging instead).
- tclean: new (experimental) gridder option ‘awp2’ (refactor of awproject).
- gencal: added support for the output of task getantposalma.
- fringefit: updated support of corrcomb=’stokes’ (formerly ‘all’) and corrcomb=’parallel’.
- phaseshift: added multi-field specification of the phasecenter parameter.
- sdimaging/tsdimaging: proper derivation of weight values for Stokes I. 
- plotbandpass: upgraded to support band-to-band calibration.
- plotbandpass: plotting of hsd_skycal solutions.
- plotbandpass: more robust identification of unique solution timestamps.
- smoothcal: improvements to smoothing of fringefit solutions.
- msmd.almaspws: identifies ALMA FDM spectral windows with heavy online channel averaging.
- tclean: GPU-enabled gridding option has been added for the VLASS project (this is not yet supported for general-purpose use).

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
   changelog
