#
# stub function definition file for docstring parsing
#

def importvla(archivefiles, vis='', bandname='', frequencytol='150000.0Hz', project='', starttime='', stoptime='', applytsys=True, autocorr=False, antnamescheme='new', keepblanks=False, evlabands=False):
    r"""
Import VLA archive file(s) to a measurement set

Parameters
   - **archivefiles** (stringArray) - Name of input VLA archive file(s)
   - **vis** (string) - Name of output visibility file
   - **bandname** (string) - VLA frequency band name:\'\'=>obtain all bands in the archive file
   - **frequencytol** (string) - Frequency shift to define a unique spectra window (Hz)
   - **project** (string) - Project name: \'\' => all projects in files
   - **starttime** (string) - Start time to search for data
   - **stoptime** (string) - End time to search for data
   - **applytsys** (bool) - Apply nominal sensitivity scaling to data and weights
   - **autocorr** (bool) - Import autocorrelations to MS, if set to True
   - **antnamescheme** (string) - \'old\' or \'new\'; \'VA04\' or \'04\' for VLA ant 4
   - **keepblanks** (bool) - Fill scans with blank (empty) source names (e.g. tipping scans)
   - **evlabands** (bool) - Use updated eVLA frequencies and bandwidths for bands and wavelengths


Description
      Imports an arbitrary number of VLA archive-format data sets into a
      CASA MeasurementSet.

      The task **importvla** reads in VLA data in archive format, as
      downloaded from the VLA data archive. It will handle archival VLA
      data in both old style (before July 2007) and new style (after
      July 2007). It can apply the system temperature (Tsys) to the data
      and to the weights. If more than one band is present, each band
      will be put in the same MeasurementSet but in a separate spectral
      window.

      .. note:: **NOTE**: **importvla** will import the on-line flags (from the
         VLA system) along with the data. Shadowed antennas will also be
         flagged. The flags will be put in the MAIN table and thus
         available to subsequent tasks and tools. If you wish to revert
         to unflagged data, use **flagmanager** to save the flags (if
         you wish), and then use **flagdata** with *mode=’manualflag’*
         and *unflag=True* to toggle off the flags.

       

      .. rubric:: Parameter descriptions
         :name: parameter-descriptions

      .. rubric:: *archivefiles*
         :name: archivefiles

      The parameter *archivefiles* is used to specify the input VLA
      Archive format file names, as can be found in the `NRAO
      Archive <https://archive.nrao.edu>`__. Note that *archivefiles*
      takes a string or list of strings, as there are often multiple
      files for a project in the archive. If the data are located in a
      different directory on disk, then use the full path name to
      specify each archive file. The scaling of VLA data both before and
      after the June 2007 Modcomp-turnoff is fully supported, based on
      the value of *applytsys*.

      .. rubric:: *vis*
         :name: vis

      Name of output visibility file.

      .. rubric:: *bandname*
         :name: bandname

      The **importvla** task allows selection on the frequency band. The
      *bandname* indicates the VLA Frequency band(s) to load, using the
      traditional bandname codes. These are:

      -  ’4’ = 48-96 MHz
      -  ’P’ = 298-345 MHz
      -  ’L’ = 1.15-1.75 GHz
      -  ’C’ = 4.2-5.1 GHz
      -  ’X’ = 6.8-9.6 GHz
      -  ’U’ = 13.5-16.3 GHz
      -  ’K’ = 20.8-25.8 GHz
      -  ’Q’ = 38-51 GHz
      -  ’’ = all bands (default)

      .. note:: **NOTE**: After the transition from the VLA to JVLA, the actual
         frequency ranges covered by the bands have changed, and
         additional bands have been added (namely ’S’ from 1-2 GHz and
         ’Ka’ from 26.4-40 GHz). See the `frequency ranges of the
         JVLA <https://science.nrao.edu/facilities/vla/docs/manuals/oss2017B/performance/vla-frequency-bands-and-tunability>`__
         bands for details.

      .. rubric:: *frequencytol*
         :name: frequencytol

      The *frequencytol* parameter specifies the frequency separation
      tolerated when assigning data to spectral windows. The default is
      *frequencytol='150000.0Hz'*. For Doppler tracked data, where the
      sky frequency changes with time, a *frequencytol* < 10000 Hz may
      produce too many unnecessary spectral windows.

      .. rubric:: *project*
         :name: project

      You can specify a specific project name to import from archive
      files. The default ’’ will import data from all projects in
      file(s) *archivefiles*. For example for VLA Project AL519:

      -  project = 'AL519'    # this will work
      -  project = 'al519'    # this will also work

      .. note:: **NOTE**: project=’AL0519’ will NOT work (even though that is
         what queries to the VLA Archive will print it as).

      .. rubric:: *starttime* and *stoptime*
         :name: starttime-and-stoptime

      You can specify start and stop times for the data, e.g.,
      *starttime='1970/1/31/00:00:00'* and
      *stoptime='2199/1/31/23:59:59'*. The blank defaults will load all
      data fitting other criteria.

      .. rubric:: *applytsys*
         :name: applytsys

      The *applytsys* parameter controls whether the nominal sensitivity
      scaling (based on the measured TSYS, with the weights scaled
      accordingly using the integration time) is applied to the
      visibility amplitudes or not. If True, then it will be scaled so
      as to be the same as AIPS FILLM (i.e., approximately in
      deciJanskys). Note that post-Modcomp data is in raw correlation
      coefficient and will be scaled using the TSYS values, while
      Modcomp-era data had this applied online. In all cases,
      **importvla** will do the correct thing to data and weights based
      on an internal flag in the VLA Archive file, either scaling it or
      unscaling based on your choice for *applytsys*.

      .. note:: **NOTE**: If *applytsys=True* and you see strange behavior in
         data amplitudes, it may be due to erroneous TSYS values from
         the online system. You might want to then fill with
         *applytsys=False* and look at the correlation coefficients to
         see if the behavior is as expected.

      .. rubric:: *autocorr*
         :name: autocorr

      Autocorrelations are written to the MeasurementSet if
      *autocorr=True*. Generally for the VLA, autocorrelation data is
      not useful, and furthermore the imaging routine will try to image
      the autocorrelation data (it assumes it is single dish data) which
      will swamp any real signal. Thus, if you do fill the
      autocorrelations, you will have to flag them before imaging.

      .. rubric:: *antnamescheme*
         :name: antnamescheme

      The *antnamescheme* parameter controls whether **importvla** will
      try to use a naming scheme where JVLA antennas are prefixed with
      EA (e.g., ’EA16’) and old VLA antennas have names prefixed with VA
      (e.g., ’VA11’).

      .. rubric:: *keepblanks*
         :name: keepblanks

      Turns on or off whether **importvla** fills the scans with blank
      (empty) source names (e.g., tipping scans).

      .. rubric:: *evlabands*
         :name: evlabands

      The *evlabands=True* option is provided to allow users to access
      JVLA frequencies outside the standard VLA tunings (e.g., the
      extended C-band above 6 GHz).

      .. note:: **WARNING**: Use of this option for standard VLA data will
         cause unexpected associations, such as X-band data below 8 GHz
         being extracted to C-band (as the JVLA C-band is 4–8 GHz). Use
         with care.

       

       

      .. rubric:: Notes
         :name: notes

      If the output *vis* parameter (MeasurementSet) already exists or
      is an illegal name, the following SEVERE warning is shown.
      (<*archivefiles*> and <*vis*> are those parameter values):

      .. note:: | SEVERE \**\* Error importing <*archivefiles*> to <*vis*>
         | SEVERE Need valid visibility file name (bad name or already
           exists)
         | SEVERE An error occurred running task importvla.

      When **importvla** finishes without writing any rows to the output
      MeasurementSet (because of the data selection resulting from the
      parameter settings or because of problems with the data as
      described below) then this SEVERE error message is shown
      ("*<vis*>" is the value of the *vis* parameter).

      .. note:: | SEVERE \**\* visibility file is empty: <*vis*>
         | SEVERE An error occurred running task importvla.

      This task has not been tested on VLA archive data with revisions
      less than 23. Using **importvla** to import older revisions
      results in the following warning message (the revision level of
      the archive data is shown):

      .. note:: | WARN This function has not been tested on VLA archive data
           with revisions less
         | WARN than 23 & the data in this record has a revision level
           of 5
         | WARN It is very likely that the correlation data will be
           scaled incorrectly

      The *epoch* value is set to zero in archive data for revsions less
      than 10. **importvla** assumes a value of 1950 in that case,
      resuting in the code using a value of B1950_VLA where necessary in
      the output MeasurementSet (mean epoch [1979.9] and ecliptic at
      B1950.0). This warning message is given when that assumption is
      made:

      .. note:: WARN epoch is 0, assuming B1950_VLA

      Records involving unsupported observing modes are skipped by
      **importvla**. If only unsupported observing modes are found no
      rows will be written and the output MeasurementSet will be empty.
      A warning message similar to the following is shown when an
      unsupported observing mode is seen, indicating the mode and a
      short description of that mode.

      .. note:: WARN Unsupported observing mode: IA interferometer pointing
         mode A (IF)

      The polarization information is sometimes impossible for
      **importvla** to determine for some old (early) correlator modes.
      In that case, the task will skip that record. If no other
      correlator modes are found in the data the resulting output
      MeasurementSet will be empty. This is a SEVERE error and may
      indicate that there are other problems with any data that was
      written to the MeasurementSet.

      .. note:: | SEVERE Unable to determine polarization information for some
           or all correlator modes.
         | SEVERE That data can not be filled and the resulting
           visibility file may be empty.

      The folllowing warning appears to be limited to revisions 03 and
      04 and it may indicate other problems wtih the output
      MeasurementSet. The check for this condition is always made
      against the first antenna encountered. All of the antennas that
      are different from that antenna will be shown in a warning
      message.

      .. note:: | WARN The IF transfer switch for antenna VA04 is different
           from the setting for antenna VA01.
         | WARN Correlations involving this antenna may have incorrect
           polarization labelling.

      .. rubric:: Unsupported Observing Modes
         :name: unsupported-observing-modes

      -  "D " : delay center determination mode
      -  "IR" : interferometer reference pointing mode
      -  "I*" : interferomter pointing mode \* (IF). Where \* is one of
         A, B, C, D.
      -  "J*" : JPL mode \* (IF). Where \* is one of A, B, C, D."
      -  "P*" : single dish pointing mode \* (IF). Where \* is one of A,
         B, C, D
      -  "TB" : test back-end and front-end
      -  "TE" : tipping curve
      -  "TF" : test front-end
      -  "VS" : single dish VLBI

    """
    pass
