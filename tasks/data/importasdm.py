#
# stub function definition file for docstring parsing
#

def importasdm(asdm, vis='', createmms=False, separationaxis='auto', numsubms='auto', corr_mode='all', srt='all', time_sampling='all', ocorr_mode='ca', compression=False, lazy=False, asis='', wvr_corrected_data='no', scans='', ignore_time=False, process_syspower=True, process_caldevice=True, process_pointing=True, process_flags=True, tbuff=0.0, applyflags=False, savecmds=False, outfile='', flagbackup=True, verbose=False, overwrite=False, showversion=False, useversion='v3', bdfflags=False, with_pointing_correction=False, convert_ephem2geo=True, polyephem_tabtimestep=0.):
    r"""
Convert an ALMA Science Data Model observation into a CASA visibility file (MS)

Parameters
   - **asdm** (string) - Name of input asdm directory (on disk)
   - **vis** (string='') - Root name of the ms to be created. Note the .ms is NOT added
   - **createmms** (bool=False) - Create a Multi-MS output

      .. raw:: html

         <details><summary><i> createmms = True </i></summary>

      - **separationaxis** (string='auto') - Axis to do parallelization across (scan, spw, baseline, auto)
      - **numsubms** ({string, int}='auto') - The number of SubMSs to create (auto or any number)

      .. raw:: html

         </details>
   - **corr_mode** (string='all') - Specifies the correlation mode to be considered on input. A quoted string containing a sequence of ao, co, ac,or all separated by whitespaces is expected
   - **srt** (string='all') - Specifies the spectral resolution type to be considered on input. A quoted string containing a sequence of fr, ca, bw, or all separated by whitespaces is expected
   - **time_sampling** (string='all') - Specifies the time sampling (INTEGRATION and/or SUBINTEGRATION)  to be considered on input. A quoted string containing a sequence of i, si, or all separated by whitespaces is expected
   - **ocorr_mode** (string='ca') - Output data for correlation mode AUTO_ONLY (ao) or CROSS_ONLY (co) or CROSS_AND_AUTO (ca)
   - **compression** (bool=False) - Flag for turning on data compression
   - **lazy** (bool=False) - Make the MS DATA column read the ASDM Binary data directly (faster import, smaller MS)
   - **asis** (string='') - Creates verbatim copies of the ASDMtables in the ouput measurement set. Value given must be a string of table names separated by spaces; A * wildcard is allowed.
   - **wvr_corrected_data** (string='no') - Specifies which values are considerd in the SDM binary data to fill the DATA column in the MAIN table of the MS; yes for corrected, no for uncorrected, both for corrected and uncorrected (resulting in two MSs)
   - **scans** (string='') - Processes only the specified scans.  A scan specification consists in an exec bock index followed by the : character, followed by a comma separated list of scan indexes or scan index ranges. (e.g. 0:1;1:2~6,8;2:,3:24~30)
   - **ignore_time** (bool=False) - All the rows of the tables Feed, History, Pointing, Source, SysCal, CalDevice, SysPower, and Weather are processed independently of the time range of the selected exec block / scan.
   - **process_syspower** (bool=True) - Process the SysPower table?
   - **process_caldevice** (bool=True) - Process the CalDevice table?
   - **process_pointing** (bool=True) - Process the Pointing table?
   - **process_flags** (bool=True) - Create online flags in the FLAG_CMD sub-table?

      .. raw:: html

         <details><summary><i> process_flags = True </i></summary>

      - **tbuff** (double=0.0) - Time padding buffer (seconds)
      - **applyflags** (bool=False) - Apply the flags to the MS.
      - **savecmds** (bool=False) - Save flag commands to an ASCII file
      - **outfile** ({string, stringArray}='') - Name of ASCII file to save flag commands

      .. raw:: html

         </details>
   - **flagbackup** (bool=True) - Back up flag column before applying flags.
   - **verbose** (bool=False) - Output lots of information while the filler is working
   - **overwrite** (bool=False) - Over write an existing MS(s)
   - **showversion** (bool=False) - Report the version of asdm2MS being used
   - **useversion** (string='v3') - Version of asdm2MS to be used (v3 default, should work for all data)
   - **bdfflags** (bool=False) - Set the MS FLAG column according to the ASDM _binary_ flags
   - **with_pointing_correction** (bool=False) - Add (ASDM::Pointing::encoder - ASDM::Pointing::pointingDirection) to the value to be written in MS::Pointing::direction
   - **convert_ephem2geo** (bool=True) - if True, convert any attached ephemerides to the GEO reference frame (time-spacing not changed)
   - **polyephem_tabtimestep** (double=0.) - Timestep (days) for the tabulation of polynomial ephemerides. A value <= 0 disables tabulation.


Description
      .. note:: NOTE: **importevla** has now been deprecated, and
         **importasdm** combined with **flagdata** should be used to
         import JVLA data, as explained in a dedicated section below.

      .. rubric:: Overview
         :name: overview

      The **importasdm** task will fill SDM1.2 and SDM1.3 format data
      into a CASA visibility data set (MS). The importasdm task supports
      all changes in the ALMA ASDM made since the previous CASA release
      (an up-to-date description of the most recent tables of the SDM
      can be found
      `here <https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals/the-science-data-model>`__).
      ALMA data were recorded in SDM1.2 format from October 2009 until
      May 2011. Since May 2011, ALMA is using the SDM1.3 format. In
      particular, all science data from Cycle 0 onward will be in
      SDM1.3. The JVLA started using SDM1.2 in October 2009, but
      currently also uses SDM1.3. The **importasdm** task can read all
      of the above formats.  For the default parameter settings for
      **importasdm**, see the Examples tab.

      The basic modes of importing data utilizing **importasdm** can be
      set by using various parameters.  For example,

      -  If the parameter *scans* is set, then **importasdm** processes
         only the scans specified in the option’s value. This value is a
         semicolon-separated list of scan specifications. A scan
         specification consists in an execution (exec) block index
         followed by the character ’:’ followed by a comma-separated
         list of scan indices or scan index ranges. A scan index is
         relative to the exec block it belongs to. Scan indices are
         1-based while exec blocks are 0-based. The expressions:

         -  "0:1"
         -  "2:2~6"
         -  "0:1;1:2~6,8;2:,3:24~30"
         -  "1,2"
         -  "3:"

      -  are all valid values for the selection. The "3:" selector will
         be interpreted as ’all the scans of the exec block 3’. A scan
         index or a scan index range not preceded by an exec block index
         will be interpreted as ’all the scans with such indexes in all
         the exec blocks’. By default, all the scans are considered.
      -  When *process_flags=True*, the task will create online flags
         based on the Flag.xml, Antenna.xml and SpectralWindow.xml files
         and copy them to the *FLAG_CMD* sub-table of the MS. The flags
         will NOT be applied unless the parameter *applyflags* is set to
         True. Optionally, the flags can also be saved to an external
         ASCII file if *savecmds* is set to True. The flags can later be
         applied to the MS using task **flagdata** in list mode.
      -  When *bdfflags=True*, the task will apply online flags
         contained in the ASDM BDF data by calling the executable
         bdflags2MS which the user can also do from the OS prompt.
         Setting *bdfflags=True* is recommended for ALMA data.
      -  When *createmms=True*, the task will create a Multi-MS
         partitioned according to the given separation axis. For more
         detailed documentation on partition, Multi-MS, and the MPI use
         in CASA, please see the global task list pages describing
         **partition** and **mstransform**. `The
         Multi-MS <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/the-multi-ms>`__ also
         contains more information on Multi-MS creation. 
      -  When setting the values for *wvr_corrected_data*, the task will
         read the SDM binary data and fill the DATA column in the MAIN
         table of the MS for those ALMA data that have either corrected
         data, uncorrected data or both. Expected values for this option
         are 'no' for the uncorrected data (this is the default), 'yes'
         for the corrected data, and 'both' for corrected and
         uncorrected data. In the latter case, two MeasurementSets are
         created, one containing the uncorrected data and the other
         containing the corrected data; the name of the corrected
         MS will be given a suffix of '-wvr-corrected'. See the relevent
         documentation on the ALMA Science Portal regarding those ALMA
         cycles which provided both corrected and uncorrected data
         streams.

      .. rubric:: Import of JVLA data with importasdm *
         *
         :name: import-of-jvla-data-with-importasdm

      As of CASA 5.4, the task importevla is no longer available to
      import JVLA data. The functionality is replaced by importasdm,
      which is also being used by the VLA pipeline. However, several
      additional steps are required to duplicate the behaviour of
      importevla when using importasdm, involving a difference in
      default parameters and the fact that some of the on-the-go
      flagging cannot be performed by importasdm.

      To mimic the behaviour of importevla, change the following
      parameters in **importasdm** from their default settings:

      -  *ocorr_mode = 'co'* to import cross-correlations only
         (discarding auto-correlations) *
         *
      -  *with_pointing_correction = True* to add pointing
         corrections *
         *
      -  *process_flags = True* (default) to read in the online flags,
         then *applyflags = True* to apply the online flags and/or
         *savecmd = True* to save flag commands to an ascii table **.**
      -  For ephemeris objects: convert_ephem2geo = False

      While online flags can thus be created by leaving the parameter
      *process_flags = True* by default, additional flagging steps need
      to be performed after **importasdm** to flag zero values and
      shadowing of antennas:

      -  **Shadow flags:** use task **flagdata**, with *mode = 'shadow'*
         (and optionally *reason = 'shadow'*). The parameters
         *tolerance* and *addantenna* can be specified in flagdata in
         the same way they were used in importevla. *
         *
      -  **Zero clipping flags:** use task **flagdata**, with *mode =
         'clip',* *correlation = 'ABS_ALL',* and *clipzeros = True* (and
         optionally *reason = 'clip'*) *.* Note that the non-default
         case in importevla where *flagpol = False c* an be replicated
         by setting *correlation="ABS_RR, ABS_LL".*

      Like **importasdm**, the task **flagdata** can also save the
      flagging commands to an ascii table by setting *savepars = True.*
      To NOT apply the flags (*applyflags=False* in importevla) add
      *action='calculate'* to flagdata. You may also chose to add a
      reason using the cmdreason argument, e.g.
      *cmdreason="CLIP_ZERO_ALL".*

      .. note:: **WARNING** *:* The task **flagdata** can only write out the
         flag commands for that invocation of flagdata. The default
         *overwrite=True* must be used to overwrite an existing file. In
         order to save the commands from all 3 possible flagging steps
         (importasdm, zero, and shadow) each step must be saved to a
         separate file, which must then be concatenated into a single
         file to be used to flag the data.

      .. rubric:: Import of ASDM data with option *lazy=True*
         :name: import-of-asdm-data-with-option-lazytrue

      For the parameter *lazy*, if the default value False is chosen,
      **importasdm** will fill the visibilities into a newly created
      DATA column (FLOAT_DATA for total power data) of the MS converting
      them from their binary format in the ASDM to the CASA Table
      format. If *lazy* is set to True, the task will create the
      DATA/FLOAT_DATA column with an ASDM-specific storage manager, the
      (asdmstman), which enables CASA to directly read the binary data
      from the ASDM with on-the-fly conversion. No redundant copy of the
      raw data is created.

      This procedure has the advantage that it saves more than 60% disk
      space and at least in some cases makes the access to the DATA
      column ≥ 10% faster because the data I/O volume is decreased. For
      the same reason, it also accelerates the import itself by ca. a
      factor 2. The acceleration is particularly large in the
      **applycal** task and here particularly on standard SATA disks.
      E.g., if your ASDM has a size of 36 GB, the import with default
      parameters will turn this into an MS of 73 GB size (total disk
      space consumption = 36 GB + 73 GB = 109 GB). With *lazy=True*, the
      imported MS has a size of only 2 GB (total disk space consumption
      = 36 GB + 2 GB = 38 GB). I.e. your total disk space savings are
      ca. 65%. Even when you compare to the case where you delete the
      ASDM after normal import, the solution with lazy import and
      keeping the ASDM will save you ca. 48% disk space (in the example
      above 38 GB compared to 73 GB). The only caveats are the
      following:

      #. You must not delete your ASDM. You can, however, move it but
         you have to update the reference stored in the MS. Symbolic
         links will work. See below on how to use the tool method
         **ms.asdmref** to manipulate the ASDM reference.
      #. The lazily imported DATA/FLOAT_DATA column is read-only. But in
         any normal data reduction, the DATA/FLOAT_DATA column (as
         opposed to CORRECTED DATA) is treated as read-only anyway.

      The lazily imported MS is numerically identical with the
      traditionally imported MS and so are all results derived from the
      MSs. The setting *lazy=True* might be made the default setting in
      future CASA releases. An important additional tool to manipulate
      lazily imported MSs is the method **ms.asdmref** in the MS tool.
      If the MS is imported from an ASDM with option *lazy=True*, the
      DATA/FLOAT_DATA column of the MS is virtual and directly reads the
      visibilities from the ASDM. A reference to the original ASDM is
      stored with the MS. If the ASDM needs to be moved to a different
      path, the reference to it in the MS needs to be updated. This can
      be achieved with **ms.asdmref**. The method takes one argument:
      *abspath*. When called with *abspath* equal to an empty string
      (default), the method just reports the currently set ASDM path or
      an empty string if the ASDM path was not set, i.e. the MS was not
      lazily imported. If you want to move the referenced ASDM to a
      different path, you can set the new absolute path by providing it
      as the value of *abspath* to the method.

      .. note:: | ms.open(’uid___A12345_X678_X910.ms’,False)
         | ms.asdmref(’/home/alma/myanalysis/uid___A12345_X678_X910’)
         | ms.close()

      will set the new location of the referenced ASDM to
      /home/alma/myanalysis/uid___A12345_X678_X910.

      .. note:: **NOTE**: The lazily imported MS can be moved without any
         restrictions independently from the referenced ASDM as long as
         the absolute path to the ASDM remains accessible, even across
         file systems.

    """
    pass
