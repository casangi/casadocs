#
# stub function definition file for docstring parsing
#

def importasdm(asdm, vis='', createmms=False, separationaxis='auto', numsubms='auto', corr_mode='all', srt='all', time_sampling='all', ocorr_mode='ca', compression=False, lazy=False, asis='', wvr_corrected_data='no', scans='', ignore_time=False, process_syspower=True, process_caldevice=True, process_pointing=True, process_flags=True, tbuff=0.0, applyflags=False, savecmds=False, outfile='', flagbackup=True, verbose=False, overwrite=False, showversion=False, useversion='v3', bdfflags=False, with_pointing_correction=False, convert_ephem2geo=True, polyephem_tabtimestep=0.):
    r"""
Convert an ALMA Science Data Model observation into a CASA visibility file (MS)

Parameters
   - **asdm** (string) - Name of input asdm directory (on disk) [1]_
   - **vis** (string='') - Root name of the ms to be created. Note the .ms is NOT added [2]_
   - **createmms** (bool=False) - Create a Multi-MS output [3]_

      .. raw:: html

         <details><summary><i> createmms = True </i></summary>

      - **separationaxis** (string='auto') - Axis to do parallelization across (scan, spw, baseline, auto) [4]_
      - **numsubms** ({string, int}='auto') - The number of SubMSs to create (auto or any number) [5]_

      .. raw:: html

         </details>
   - **corr_mode** (string='all') - Specifies the correlation mode to be considered on input. A quoted string containing a sequence of ao, co, ac,or all separated by whitespaces is expected [6]_
   - **srt** (string='all') - Specifies the spectral resolution type to be considered on input. A quoted string containing a sequence of fr, ca, bw, or all separated by whitespaces is expected [7]_
   - **time_sampling** (string='all') - Specifies the time sampling (INTEGRATION and/or SUBINTEGRATION)  to be considered on input. A quoted string containing a sequence of i, si, or all separated by whitespaces is expected [8]_
   - **ocorr_mode** (string='ca') - Output data for correlation mode AUTO_ONLY (ao) or CROSS_ONLY (co) or CROSS_AND_AUTO (ca) [9]_
   - **compression** (bool=False) - Flag for turning on data compression [10]_
   - **lazy** (bool=False) - Make the MS DATA column read the ASDM Binary data directly (faster import, smaller MS) [11]_
   - **asis** (string='') - Creates verbatim copies of the ASDMtables in the ouput measurement set. Value given must be a string of table names separated by spaces; A * wildcard is allowed. [12]_
   - **wvr_corrected_data** (string='no') - Specifies which values are considerd in the SDM binary data to fill the DATA column in the MAIN table of the MS; yes for corrected, no for uncorrected, both for corrected and uncorrected (resulting in two MSs) [13]_
   - **scans** (string='') - Processes only the specified scans.  A scan specification consists in an exec bock index followed by the : character, followed by a comma separated list of scan indexes or scan index ranges. (e.g. 0:1;1:2~6,8;2:,3:24~30) [14]_
   - **ignore_time** (bool=False) - All the rows of the tables Feed, History, Pointing, Source, SysCal, CalDevice, SysPower, and Weather are processed independently of the time range of the selected exec block / scan. [15]_
   - **process_syspower** (bool=True) - Process the SysPower table? [16]_
   - **process_caldevice** (bool=True) - Process the CalDevice table? [17]_
   - **process_pointing** (bool=True) - Process the Pointing table? [18]_
   - **process_flags** (bool=True) - Create online flags in the FLAG_CMD sub-table? [19]_

      .. raw:: html

         <details><summary><i> process_flags = True </i></summary>

      - **tbuff** (double=0.0) - Time padding buffer (seconds) [20]_
      - **applyflags** (bool=False) - Apply the flags to the MS. [21]_
      - **savecmds** (bool=False) - Save flag commands to an ASCII file [22]_
      - **outfile** ({string, stringArray}='') - Name of ASCII file to save flag commands [23]_

      .. raw:: html

         </details>
   - **flagbackup** (bool=True) - Back up flag column before applying flags. [24]_
   - **verbose** (bool=False) - Output lots of information while the filler is working [25]_
   - **overwrite** (bool=False) - Over write an existing MS(s) [26]_
   - **showversion** (bool=False) - Report the version of asdm2MS being used [27]_
   - **useversion** (string='v3') - Version of asdm2MS to be used (v3 default, should work for all data) [28]_
   - **bdfflags** (bool=False) - Set the MS FLAG column according to the ASDM _binary_ flags [29]_
   - **with_pointing_correction** (bool=False) - Add (ASDM::Pointing::encoder - ASDM::Pointing::pointingDirection) to the value to be written in MS::Pointing::direction [30]_
   - **convert_ephem2geo** (bool=True) - if True, convert any attached ephemerides to the GEO reference frame (time-spacing not changed) [31]_
   - **polyephem_tabtimestep** (double=0.) - Timestep (days) for the tabulation of polynomial ephemerides. A value <= 0 disables tabulation. [32]_







Details
   Explanation of each parameter

.. [1] 
   **asdm** (string)
      | Name of input ASDM file (directory)
      |                      Default: none
      | 
      |                         Example: asdm='ExecBlock3'
.. [2] 
   **vis** (string='')
      | Root ms name. 
      |                      Default: none
      | 
      |                      Note that a prefix (.ms) is NOT appended to this
      |                      name.
.. [3] 
   **createmms** (bool=False)
      | Create a Multi-MS partitioned according to the given
      | separation axis.
      |                      Default: False
      |                      Options: False|True
      | 
      |                      For more detailed documentation on partition,
      |                      Multi-MS and the MPI use in CASA, please see CASA
      |                      Docs (https://casa.nrao.edu/casadocs/).
.. [4] 
   **separationaxis** (string='auto')
      | Axis to do parallelization across
      |                      Default: 'auto'
      |                      Options: 'scan', 'spw', 'baseline', 'auto'
      | 
      |                      * auto: will partition per scan/spw to obtain
      |                        optimal load balancing with the following
      |                        criteria:    
      |                        1 - Maximize the scan/spw/field distribution
      |                        across sub-MSs
      |                        2 - Generate sub-MSs with similar size
      |                      * 'scan' or 'spw': will partition the MS into
      |                        scan or spw. The individual sub-MSs may not be
      |                        balanced with respect to the number of rows.
      |                      * 'baseline': mostly useful for Single-Dish
      |                        data. This axis will partition the MS based on
      |                        the available baselines. If the user wants only
      |                        auto-correlations, use the
      |                        ocorr_mode='ao'. Note that if numsubms='auto',
      |                        partition will try to create as many subMSs as
      |                        the number of available servers in the
      |                        cluster. If the user wants to have one subMS
      |                        for each baseline, set the numsubms parameter
      |                        to a number higher than the number of baselines
      |                        to achieve this.
.. [5] 
   **numsubms** ({string, int}='auto')
      | The number of sub-MSs to create in the Multi-Ms.
      |                      Default: 'auto'
      |                      Options: any integer number (example: numsubms=4)
      | 
      |                      The default 'auto' is to partition using the
      |                      number of available servers given when launching
      |                      CASA. If the task is unable to determine the
      |                      number of running servers, or the user did not
      |                      start CASA using mpicasa, numsubms will use 8 as
      |                      the default.
      | 
      |                         Example: Launch CASA with 5 engines, where 4
      |                         of them will be used to create the MMS (the
      |                         first engine is used as the MPIClient):
      |                         mpicasa -n 5 casa --nogui --log2term
      |                         CASA> importasdm('uid__A1', createmms=True)
.. [6] 
   **corr_mode** (string='all')
      | Correlation mode to be considered on input.
      |                      Default: 'all'
      |                      Options: ao, co, ac, or all
.. [7] 
   **srt** (string='all')
      | Spectral resolution type.
      |                      Default: 'all'
      |                      Options: fr, ca, bw, or all
.. [8] 
   **time_sampling** (string='all')
      | Specifies the time sampling (INTEGRATION and/or
      | SUBINTEGRATION) to be considered on input. 
      |                      Default: 'all'
      |                      Options: i, si, or all
      | 
      |                      A quoted string containing a sequence of i, si,
      |                      or all separated by whitespaces is expected
.. [9] 
   **ocorr_mode** (string='ca')
      | Output data for correlation mode AUTO_ONLY (ao) or
      | CROSS_ONLY (co) or CROSS_AND_AUTO (ca)
      |                      Default: 'ca'
      |                      Options: ao, co, ca
.. [10] 
   **compression** (bool=False)
      | Produce compressed columns in the resulting measurement
      | set.
      |                      Default: False
      |                      Options: False|True
.. [11] 
   **lazy** (bool=False)
      | Make the MS DATA column read the ASDM Binary data
      | directly (faster import, smaller MS).
      |                      Default: False
      |                      Options: False|True
      | 
      |                      Instead of writing a copy of the visibilities
      |                      into a standard DATA column, lazy=True will make
      |                      importasdm only write a lookup-table such that
      |                      later access to the DATA column will read the
      |                      ASDM binary visibility data directly. This
      |                      requires that the ASDM not be removed from its
      |                      location as long the the DATA column is
      |                      needed. Use method ms.asdmref() to query and
      |                      manipulate the reference to the ASDM.
      | 
      |                      lazy=True will save ca. 50% disk space and
      |                      accelerate the DATA column access by
      |                      ca. 10%. lazy=True will only work when there is
      |                      visibility data in the ASDM, not with pure
      |                      radiometer data.
.. [12] 
   **asis** (string='')
      | Creates verbatim copies of the ASDM tables in the output
      | measurement set.
      |                      Default: none
      | 
      |                      The value given to this option must be a list of
      |                      table names separated by space characters; the
      |                      wildcard character '*' is  allowed in table
      |                      names.
.. [13] 
   **wvr_corrected_data** (string='no')
      | Specifies which values are considerd in the ASDM binary
      | data to fill the DATA column in the MAIN table of the MS.
      |                      Default: no
      |                      Options: no|yes|both
      | 
      |                      * no: uncorrected data
      |                      * yes: corrected data
      |                      * both: for corrected and uncorrected data. Note
      |                        if both is selected, two measurement sets are
      |                        created, one with uncorrected data and the
      |                        other with corrected data (which name is
      |                        suffixed by '-wvr-corrected')
.. [14] 
   **scans** (string='')
      | Processes only the scans specified in the option's value.
      |                      Default: none (all scans)
      | 
      |                      This value is a semicolon separated list of scan
      |                      specifications. A scan specification consists in
      |                      an exec bock index  followed by the character ':'
      |                      followed by a comma separated list of scan
      |                      indexes or scan index ranges. A scan index is
      |                      relative to the exec block it belongs to. Scan
      |                      indexes are  1-based while exec blocks's are
      |                      0-based. 
      | 
      |                         Examples: 
      |                         '0:1' 
      |                         '2:2~6' 
      |                         '0:1;1:2~6,8;2:,3:24~30'
      |                         '1,2' 
      |                         '3:' alone will be interpreted as 'all the
      |                         scans of the exec block#3'. An scan index or a
      |                         scan index range not preceded by an exec block
      |                         index will be interpreted as 'all the scans
      |                         with such indexes in all the exec blocks'.
.. [15] 
   **ignore_time** (bool=False)
      | All the rows of the tables Feed, History, Pointing,
      | Source, SysCal, CalDevice, SysPower, and Weather are processed
      | independently of the time range of the selected exec block / scan.
      |                      Default: False
      |                      Options: False|True
.. [16] 
   **process_syspower** (bool=True)
      | The SysPower table is processed if and only if this
      | parameter is set to true.
      |                      Default: True
      |                      Options: True|False
.. [17] 
   **process_caldevice** (bool=True)
      | The CalDevice table is processed if and only if this
      | parameter is set to true.
      |                      Default: True
      |                      Options: True|False
.. [18] 
   **process_pointing** (bool=True)
      | The Pointing table is processed if and only if this
      | parameter is set to true. 
      |                      Default: True
      |                      Options: True|False
      | 
      |                      If set to False, the POINTING table is empty in
      |                      the resulting MS
.. [19] 
   **process_flags** (bool=True)
      | Create online flags based on the Flag.xml, Antenna.xml
      | and SpectralWindow.xml files and copy them to the FLAG_CMD sub-table
      | of the MS.
      |                      Default: True
      |                      Options: True|False
      | 
      |                      The flags will NOT be applied unless  the
      |                      parameter applyflags is set to True. Optionally,
      |                      the flags can also be saved to an external ASCII
      |                      file if savecmds is set to True.
.. [20] 
   **tbuff** (double=0.0)
      | Time padding buffer (seconds)
      |                      Subparameter of process_flags=True
      |                      Default: 0.0
      | 
      |                      NOTE: this time is in seconds. You should
      |                      currently set the value of tbuff to be 1.5x the
      |                      correlator integration time if greater than 1
      |                      second. For example, if the SDM has integrations
      |                      of 3 seconds, set tbuff=4.5.  Likewise, set
      |                      tbuff=15.0 for 10-sec integrations.
.. [21] 
   **applyflags** (bool=False)
      | Apply the online flags to the MS.
      |                      Subparameter of process_flags=True
      |                      Default: False
      |                      Options: False|True
.. [22] 
   **savecmds** (bool=False)
      | Save the flag commands to an ASCII file given by the
      | parameter outfile. 
      |                      Subparameter of process_flags=True
      |                      Default: False
      |                      Options: False|True
.. [23] 
   **outfile** ({string, stringArray}='')
      | Filename or list of filenames where to save the online
      | flag commands.
      |                      Subparameter of process_flags=True
      |                      Default: '' (it will save on a filename composed
      |                      from the MS name(s).) E.g., for vis='uid_A02.ms',
      |                      the outfile will be 'uid_A02_cmd.txt'.
.. [24] 
   **flagbackup** (bool=True)
      | Back up flag column before applying flags.
      |                      Default: True
      |                      Options: True|False
.. [25] 
   **verbose** (bool=False)
      | Produce log output as asdm2MS is being run
      |                      Default: False
      |                      Options: False|True
.. [26] 
   **overwrite** (bool=False)
      | Over write an existing MS(s) or MS(s), if the option
      | wvr_corrected_data='both'
      |                      Default: False  (do not overwrite)
      |                      Options: False|True
      | 
      |                      NOTE: the overwrite parameter affects all the
      |                      output of the task. If any of the following
      |                      exist, it will not overwrite them. MS(s),
      |                      .flagversions, online flag files. When set to
      |                      True, it will overwrite the MS, .flagversions and
      |                      online flag file.
.. [27] 
   **showversion** (bool=False)
      | Report the version of asdm2MS being used
      |                      Default: False
      |                      Options: False|True
.. [28] 
   **useversion** (string='v3')
      | Version of asdm2MS to be used
      |                      Default: 'v3' (should work for all data)
.. [29] 
   **bdfflags** (bool=False)
      | Set the MS FLAG column according to the ASDM _binary_
      | flags
      |                      Default: False
      |                      Options: False|True
.. [30] 
   **with_pointing_correction** (bool=False)
      | Add (ASDM::Pointing::encoder -
      | ASDM::Pointing::pointingDirection) to the value to be written in
      | MS::Pointing::direction
      |                      Default: False
      |                      Options: False|True
.. [31] 
   **convert_ephem2geo** (bool=True)
      | if True, convert any attached ephemerides to the GEO
      | reference frame (time-spacing not changed)
      |                      Default: True
      |                      Options: True|False
      | 
      |                      ALMA uses ephemerides with observer location
      |                      equal to the ALMA site. For later processing of
      |                      the radial velocity information in, e.g. cvel,  a
      |                      geocentric ephemeris is needed. Setting this
      |                      option to True will perform the conversion of
      |                      positions and velocities on all attached
      |                      ephemerides in the imported MS. This will neither
      |                      change the time-spacing nor the duration of the
      |                      ephemeris. No interpolation in time is done.
.. [32] 
   **polyephem_tabtimestep** (double=0.)
      | Timestep (days) for the tabulation of polynomial
      | ephemerides. A value less than or equal to 0 disables tabulation.
      |                      Default: 0
      | 
      |                      Presently, VLA data can contain polynomial
      |                      ephemerides. ALMA data uses tabulated values.

    """
    pass
