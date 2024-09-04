Common Astronomy Software Applications
======================================

`CASA <https://casa.nrao.edu/../>`__, the *Common Astronomy
Software Applications*, is the primary data processing software
for the Atacama Large Millimeter/submillimeter Array
(`ALMA <https://public.nrao.edu/telescopes/alma/>`__) and Karl G.
Jansky Very Large Array
(`VLA <https://public.nrao.edu/venue/the-very-large-array/>`__),
and is often used also for other radio telescopes.

**6.6.5 Release**

CASA 6.6.5 can now be `downloaded <https://casa.nrao.edu/casa_obtaining.shtml>`__ for general use. CASA 6.6.5 is available either as a downloadable tar-file, or through pip-wheel installation, which gives flexibility to integrate CASA into a customized Python environment.

**Highlights:**

- Mac OS: the CASA Viewer is no longer packaged with Mac OS.
- wvrgcal: re-written to be compatible with python3.10.
- gencal: new caltype=’eop’ for creating EOP (Earth Orientation Parameter) correction tables.
- gencal: new caltype=‘swpwts’ to use ‘swpow’ mode without temperature conversion factors.
- sdbaseline: per spectrum sinusoid fitting for baseline subtraction.
- sdimaging/tsdimaging: new parameter ‘interpolation’ to specify spectral interpolation rules.
- setjy: will now exclusively use casaconfig to find the required data tables.
- plotms: calibration table interface added in parameters and GUI.
- CASA Docs: new CASA Memo 13 - a guide towards achieving scalable parallelization for imaging large cubes.
- CASA Docs: updated Community Examples on wideband primary beam corrections and custom primary beam models.

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
