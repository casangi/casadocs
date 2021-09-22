Common Astronomy Software Applications
======================================

`CASA <https://casa.nrao.edu/../>`__, the *Common Astronomy
Software Applications*, is the primary data processing software
for the Atacama Large Millimeter/submillimeter Array
(`ALMA <https://public.nrao.edu/telescopes/alma/>`__) and Karl G.
Jansky Very Large Array
(`VLA <https://public.nrao.edu/venue/the-very-large-array/>`__),
and is often used also for other radio telescopes.

**6.2.1 Release**

CASA 6.2.1 can now be `downloaded <https://casa.nrao.edu/casa_obtaining.shtml>`__ for general use. CASA 6.2.1 is based on the prior 6.2.0 release and includes the **Pipeline** software package for `ALMA <https://almascience.nrao.edu/processing/science-pipeline>`__ and `VLA <https://science.nrao.edu/facilities/vla/data-processing/pipeline>`__ operations. CASA 6.2.1 is available either as a downloadable tar-file, or through pip-wheel installation, which gives flexibility to integrate CASA into a customized Python environment.

**New Features:**

- CASA 6: inclusion of remaining tasks, including interactive flagdata GUI
- tclean: refactor of cube imaging (reliability, flexibility, peformance)
- tclean: new option 'briggsbwtaper' and improved 'briggs' weighting
- tclean: improved algorithm for fitting the PSF 
- tclean: updates to multiscale imaging to account for channel-dependence of the PSF
- sdatmcor: new task for atmospheric correction of single dish data
- sdbaseline: new parameters 'updateweight' and 'sigmavalue'
- accor: support of the new parameter 'corrdepflags'
- gencal: GAIN_CURVE subtable (caltype='gc') made available
- plotms: improvements on avaraging, channel selection, and Mueller/Jones tables
- simalma: updates to produce the expected output
- listobs: extended output MS metadata
- tec_maps: porting of 'tec_maps' script for ionospheric calibration in CASA 6
- Consistency in error handling among tasks
- Updates to the model for Mars.
- Fixes to a number of bugs.

For more details on these and other new features, see the CASA 6.2.1 (`Release Notes <https://casadocs.readthedocs.io/en/v6.2.1/notebooks/introduction.html>`__).

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
   api
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
