

.. _Description:

Description
   Convert a FITS-IDI file to a CASA MeasurementSet
   
   .. rubric:: Summary
      
   
   The **importfitsidi** task converts FITS files in Interferometry
   Data Interchange (IDI) format to CASA MeasurementSets.
   
   It permits CASA users to process visibility data provided in the
   FITS-IDI standard `[1] <#cit1>`__. If several files are given,
   they will be concatenated into one MS.
   
   For data correlated with the DiFX correlator (such as the VLBA
   correlator), importfitsidi will apply the necessary digital
   corrections for antennas using 1-bit or 2-bit sampling.
   Corrections are not applied for other correlators.
   
   .. warning:: **WARNING:** because digital corrections are applied for data
      correlated with the the DiFX correlator, this means that
      processing archival data correlated with the VLBA hardware
      correlator should be done with care and may not yield the
      appropriate results.
   
   Visibility weights in the SIGMA and WEIGHT columns of the MS are
   initialized taking into account the correlator weights,
   effectively by scaling the integration time by the correlator
   weight.
   
   The importfitsidi task will import meta-data from the
   SYSTEM_TEMPERATURE and WEATHER tables of the FITS-IDI files, if
   present. For correlators that do not attach these tables, the
   meta-data should be attached to the FITS-IDI files before using
   importfitsidi if amplitude calibraton using T :sub:`sys`
   information or opacity corrections using weather information is
   desired. Meta-data from GAIN_CURVE, PHASE-CAL, FLAG, BASELINE,
   BANDPASS, CALIBRATION and MODEL_COMPS tables is currently ignored.
   
    
   
   .. rubric:: Parameter descriptions
      
   
   .. rubric:: *fitsidifile*
      
   
   Name(s) of input FITS-IDI file(s). No default.  If more than one
   input file is specified, they will be filled into a single MS.
   
   .. rubric:: *vis*
      
   
   Name of output visibility file (MS). No default.
   
   .. rubric:: *constobsid*
      
   
   Controls the conversion with respect to the observation IDs. If
   True, a constant obs id == 0 is given to the data from all input
   FITS-IDI files. If False, separate observations IDs are given for
   each input file. Default = False.
   
   .. rubric:: *scanreindexgap_s*
      
   
   Controls the conversion with respect to the division into scans.
   If *scanreindexgap_s > 0.*, a new scan is started (on a
   per-antenna basis) whenever the gap between two integrations is
   larger than the given value (in seconds), whenever a new field
   starts, or whenever the ARRAY_ID changes. The default = 0, which
   results in no reindexing.
   
   .. rubric:: *specframe*
      
   
   Set the spectral reference frame for all spectral windows in the
   MS.  Default = *'GEO'*.   Other options:  *'TOPO', 'LSRK',
   'BARY'*.  NOTE: If *specframe='TOPO',
   * the reference location will be taken from the Observatories
   table in the CASA data repository for the given name of the
   observatory.
   
   
      Bibliography
   :sup:`1. E. Greisen,` `AIPS
   memo <http://www.aips.nrao.edu/aipsmemo.html>`__ :sup:`114,
   revised version` `<#ref-cit1>`__
   

.. _Examples:

Examples
   task examples
   
   To convert a single observation spread across two FITS-IDI files
   into a single CASA MeasurementSet while treating gaps of 15
   seconds or more as scan boundaries:
   
   ::
   
      importfitsidi(fitsidifile=['N18C1_1.IDI', 'N18C1_2.IDI'],
      vis='n18c1.ms', constobsid=True, scanreindexgap_s=15)
   

.. _Development:

Development
   task developer
   
   --CASA Developer--
   
   