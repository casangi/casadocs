Common Astronomy Software Applications
======================================

`CASA <https://casa.nrao.edu/../>`__, the *Common Astronomy
Software Applications*, is the primary data processing software
for the Atacama Large Millimeter/submillimeter Array
(`ALMA <https://public.nrao.edu/telescopes/alma/>`__) and Karl G.
Jansky Very Large Array
(`VLA <https://public.nrao.edu/venue/the-very-large-array/>`__),
and is often used also for other radio telescopes.

**6.4.4 Release**

CASA 6.4.4 can now be `downloaded <https://casa.nrao.edu/casa_obtaining.shtml>`__ for general use. CASA 6.4.4 is available either as a downloadable tar-file, or through pip-wheel installation, which gives flexibility to integrate CASA into a customized Python environment.

**Highlights:**

- tclean: a new experimental deconvolution algorithm “Adaptive Scale Pixel” has been added to tclean. 
- tclean: new/unknown observatory names can now trigger the generation of Airy disk primary beams. 
- plotms: improvements for changing the phasecenter on-the-fly, which now relies on absolute (rather than relative) position. 
- plotms: colorization now assigns a color for each point based on unique values in a list, to ensure that the colors vary (e.g., for spw in ALMA spectral scans) 
- ft: The componentlist tool and task ft now support models with spectral curvature. 
- fft: the tool method ia.fft() now handles brightness units properly.
- ALMA array configuration files for Cycle-9 were added to the CASA data repository. 
- almahelpers.py was removed from the almatasks package, because its functions are duplicates of those that can be found in casarecipes. 

For more details on these and other new features, see the CASA 6.4.4 `Release Notes <https://casadocs.readthedocs.io/en/v6.4.4/notebooks/introduction.html>`__.
   
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
