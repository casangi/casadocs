Common Astronomy Software Applications
======================================

`CASA <https://casa.nrao.edu/../>`__, the *Common Astronomy
Software Applications*, is the primary data processing software
for the Atacama Large Millimeter/submillimeter Array
(`ALMA <https://public.nrao.edu/telescopes/alma/>`__) and Karl G.
Jansky Very Large Array
(`VLA <https://public.nrao.edu/telescopes/vla/>`__),
and is often used also for other radio telescopes.

**6.7.2 Release**

CASA 6.7.2 can now be `downloaded <https://casa.nrao.edu/casa_obtaining.shtml>`__ for general use. CASA 6.7.2 is available either as a downloadable tar-file, or through pip-wheel installation, which gives flexibility to integrate CASA into a customized Python environment.

**Highlights:**

- iclean: new interactive clean widget 
- msuvbinflag: new experimental task to flag outliers in the UV plane.
- appendantab: new task for appending *antab* files to an MS.
- hanningsmooth: new parameter *smooth_spw* for selecting spws to smooth.
- sdbaseline: added applying of sinusoid fitting parameters using baseline table.
- fringefit: added functionality to combine channels across spectral windows. 
- feather/sdintimaging: support added for per-plane beams in feather. 
- importfitsidi: now labels source positions in the ICRS reference frame (VLBI).
- atmosphere: ATM (atmosphere) library updated to ALMA Cycle 12. 
- casaconfig: new options and updates available. 
- import/export: “Beam Waveguide” antennas (ALT-AZ+BWG-R / ALT-AZ+BWG-L mount types) now experimentally supported.
- config files: the configuration files for ngVLA version Rev.F and ALMA Cycle 12 have been added.

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
