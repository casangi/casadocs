#
# stub function definition file for docstring parsing
#

def importfitsidi(fitsidifile, vis='', constobsid=False, scanreindexgap_s=0., specframe='GEO'):
    r"""
Convert a FITS-IDI file to a CASA visibility data set

Parameters
   - **fitsidifile** (stringArray) - Name(s) of input FITS-IDI file(s)
   - **vis** (string='') - Name of output visibility file
   - **constobsid** (bool=False) - If True, give constant obs ID==0 to the data from all input fitsidi files (False = separate obs id for each file)
   - **scanreindexgap_s** (double=0.) - Min time gap (seconds) between integrations to start a new scan
   - **specframe** (string='GEO') - Spectral reference frame for all spectral windows in the output MS


Description
      .. rubric:: Summary
         :name: summary

      The **importfitsidi** task converts FITS files in Interferometry
      Data Interchange (IDI) format to CASA MeasurementSets.

      It permits CASA users to process visibility data provided in the
      FITS-IDI standard `[1] <#cit1>`__. If several files are given,
      they will be concatenated into one MS.

      For data correlated with the DiFX correlator (such as the VLBA
      correlator), importfitsidi will apply the necessary digital
      corrections for antennas using 1-bit or 2-bit sampling.
      Corrections are not applied for other correlators.

      .. note:: **WARNING:** because digital corrections are applied for data
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
         :name: parameter-descriptions

      .. rubric:: *fitsidifile*
         :name: fitsidifile

      Name(s) of input FITS-IDI file(s). No default.  If more than one
      input file is specified, they will be filled into a single MS.

      .. rubric:: *vis*
         :name: vis

      Name of output visibility file (MS). No default.

      .. rubric:: *constobsid*
         :name: constobsid

      Controls the conversion with respect to the observation IDs. If
      True, a constant obs id == 0 is given to the data from all input
      FITS-IDI files. If False, separate observations IDs are given for
      each input file. Default = False.

      .. rubric:: *scanreindexgap_s*
         :name: scanreindexgap_s

      Controls the conversion with respect to the division into scans.
      If *scanreindexgap_s > 0.*, a new scan is started (on a
      per-antenna basis) whenever the gap between two integrations is
      larger than the given value (in seconds), whenever a new field
      starts, or whenever the ARRAY_ID changes. The default = 0, which
      results in no reindexing.

      .. rubric:: *specframe*
         :name: specframe

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

    """
    pass
