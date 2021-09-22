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

CASA 6.2.1 can now be `downloaded <https://casa.nrao.edu/casa_obtaining.shtml>`__ for general use. CASA 6.2.1 includes a pipeline that has been validated for `ALMA <https://almascience.nrao.edu/processing/science-pipeline>`__ and `VLA <https://science.nrao.edu/facilities/vla/data-processing/pipeline>`__ operations. CASA 6.2.1 and its included pipeline is functionally equivalent to CASA 6.2.0, and has the following added fixes and features:

-  Fixed known issue with channel averaging of a caltable in PlotMS. Resolved slow performance and crashes.
-  A significant slow down in flagdata command present in 6.2 (up to 3-4x, specially in 'summary' mode) has now been fixed, bringing CASA 6.2.1 flagdata command to a performance comparable with CASA 6.1.
-  Updated ALMA spw classification algorithm to allow spws with bandwidths of < 2 GHz to be classified as FDM windows, whereas they were classified as TDM windows before change.
-  Fix defects that prevented using the Splatalogue offline database with spectral profile tool in the CASA viewer.
-  Running tclean using a list of ALMA MeasurementSets which exhibit very large Doppler frequency changes between them (i.e., large TOPO offsets in channels) was found to result in crashes due to memory limits being crossed. A fix was implemented to switch to a different mode when such situations might occur (specifically, if the weight density grid is larger than 10% of the cube grid in memory usage). This different mode uses less memory but results in a longer runtime as tclean must make multiple passes through all MSs.



**6.2 New Features:**

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
