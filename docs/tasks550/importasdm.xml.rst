importasdm -- Convert an ALMA Science Data Model observation into a CASA visibility file (MS) -- import/export task
=======================================

Description
---------------------------------------

Convert an ALMA Science Data Model observation into a CASA visibility
file (MS)



Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - asdm
     - :code:`''`
     - Name of input asdm directory (on disk)
   * - vis
     - :code:`''`
     - Root name of the ms to be created. Note the .ms is NOT added
   * - createmms
     - :code:`False`
     - Create a Multi-MS output
   * - separationaxis
     - :code:`'auto'`
     - Axis to do parallelization across (scan, spw, baseline, auto)
   * - numsubms
     - :code:`'auto'`
     - The number of SubMSs to create (auto or any number)
   * - corr_mode
     - :code:`'all'`
     - Specifies the correlation mode to be considered on input. A quoted string containing a sequence of ao, co, ac,or all separated by whitespaces is expected
   * - srt
     - :code:`'all'`
     - Specifies the spectral resolution type to be considered on input. A quoted string containing a sequence of fr, ca, bw, or all separated by whitespaces is expected
   * - time_sampling
     - :code:`'all'`
     - Specifies the time sampling (INTEGRATION and/or SUBINTEGRATION)  to be considered on input. A quoted string containing a sequence of i, si, or all separated by whitespaces is expected
   * - ocorr_mode
     - :code:`'ca'`
     - Output data for correlation mode AUTO_ONLY (ao) or CROSS_ONLY (co) or CROSS_AND_AUTO (ca)
   * - compression
     - :code:`False`
     - Flag for turning on data compression
   * - lazy
     - :code:`False`
     - Make the MS DATA column read the ASDM Binary data directly (faster import, smaller MS)
   * - asis
     - :code:`''`
     - Creates verbatim copies of the ASDMtables in the ouput measurement set. Value given must be a string of table names separated by spaces; A * wildcard is allowed.
   * - wvr_corrected_data
     - :code:`'no'`
     - Specifies which values are considerd in the SDM binary data to fill the DATA column in the MAIN table of the MS; yes for corrected, no for uncorrected, both for corrected and uncorrected (resulting in two MSs)
   * - scans
     - :code:`''`
     - Processes only the specified scans.  A scan specification consists in an exec bock index followed by the : character, followed by a comma separated list of scan indexes or scan index ranges. (e.g. 0:1;1:2~6,8;2:,3:24~30)
   * - ignore_time
     - :code:`False`
     - All the rows of the tables Feed, History, Pointing, Source, SysCal, CalDevice, SysPower, and Weather are processed independently of the time range of the selected exec block / scan.
   * - process_syspower
     - :code:`True`
     - Process the SysPower table?
   * - process_caldevice
     - :code:`True`
     - Process the CalDevice table?
   * - process_pointing
     - :code:`True`
     - Process the Pointing table?
   * - process_flags
     - :code:`True`
     - Create online flags in the FLAG_CMD sub-table?
   * - tbuff
     - :code:`float(0.0)`
     - Time padding buffer (seconds)
   * - applyflags
     - :code:`False`
     - Apply the flags to the MS.
   * - savecmds
     - :code:`False`
     - Save flag commands to an ASCII file
   * - outfile
     - :code:`''`
     - Name of ASCII file to save flag commands
   * - flagbackup
     - :code:`True`
     - Back up flag column before applying flags.
   * - verbose
     - :code:`False`
     - Output lots of information while the filler is working
   * - overwrite
     - :code:`False`
     - Over write an existing MS(s)
   * - showversion
     - :code:`False`
     - Report the version of asdm2MS being used
   * - useversion
     - :code:`'v3'`
     - Version of asdm2MS to be used (v3 default, should work for all data)
   * - bdfflags
     - :code:`False`
     - Set the MS FLAG column according to the ASDM _binary_ flags
   * - with_pointing_correction
     - :code:`False`
     - Add (ASDM::Pointing::encoder - ASDM::Pointing::pointingDirection) to the value to be written in MS::Pointing::direction
   * - remove_ref_undef
     - :code:`False`
     - If set to True then apply fixspwbackport on the resulting MS(es).
   * - convert_ephem2geo
     - :code:`True`
     - if True, convert any attached ephemerides to the GEO reference frame (time-spacing not changed)
   * - polyephem_tabtimestep
     - :code:`float(0.)`
     - Timestep (days) for the tabulation of polynomial ephemerides. A value <= 0 disables tabulation.


Parameter Explanations
=======================================



asdm
---------------------------------------

:code:`''`

Name of input ASDM file (directory)
                     Default: none

                        Example: asdm='ExecBlock3'



vis
---------------------------------------

:code:`''`

Root ms name. 
                     Default: none

                     Note that a prefix (.ms) is NOT appended to this
		     name.



createmms
---------------------------------------

:code:`False`

Create a Multi-MS partitioned according to the given
separation axis.
                     Default: False
                     Options: False|True

                     For more detailed documentation on partition,
		     Multi-MS and the MPI use in CASA, please see CASA
		     Docs (https://casa.nrao.edu/casadocs/).



separationaxis
---------------------------------------

:code:`'auto'`

Axis to do parallelization across
                     Default: 'auto'
                     Options: 'scan', 'spw', 'baseline', 'auto'

                     * auto: will partition per scan/spw to obtain
		       optimal load balancing with the following
		       criteria:    
                       1 - Maximize the scan/spw/field distribution
		       across sub-MSs
                       2 - Generate sub-MSs with similar size
                     * 'scan' or 'spw': will partition the MS into
		       scan or spw. The individual sub-MSs may not be
		       balanced with respect to the number of rows.
                     * 'baseline': mostly useful for Single-Dish
		       data. This axis will partition the MS based on
		       the available baselines. If the user wants only
		       auto-correlations, use the
		       ocorr_mode='ao'. Note that if numsubms='auto',
		       partition will try to create as many subMSs as
		       the number of available servers in the
		       cluster. If the user wants to have one subMS
		       for each baseline, set the numsubms parameter
		       to a number higher than the number of baselines
		       to achieve this. 



numsubms
---------------------------------------

:code:`'auto'`

The number of sub-MSs to create in the Multi-Ms.
                     Default: 'auto'
                     Options: any integer number (example: numsubms=4)

                     The default 'auto' is to partition using the
		     number of available servers given when launching
		     CASA. If the task is unable to determine the
		     number of running servers, or the user did not
		     start CASA using mpicasa, numsubms will use 8 as
		     the default.

                        Example: Launch CASA with 5 engines, where 4
			of them will be used to create the MMS (the
			first engine is used as the MPIClient):
                        mpicasa -n 5 casa --nogui --log2term
                        CASA> importasdm('uid__A1', createmms=True)



corr_mode
---------------------------------------

:code:`'all'`

Correlation mode to be considered on input.
                     Default: 'all'
                     Options: ao, co, ac, or all



srt
---------------------------------------

:code:`'all'`

Spectral resolution type.
                     Default: 'all'
                     Options: fr, ca, bw, or all



time_sampling
---------------------------------------

:code:`'all'`

Specifies the time sampling (INTEGRATION and/or
SUBINTEGRATION) to be considered on input. 
                     Default: 'all'
                     Options: i, si, or all

                     A quoted string containing a sequence of i, si,
		     or all separated by whitespaces is expected



ocorr_mode
---------------------------------------

:code:`'ca'`

Output data for correlation mode AUTO_ONLY (ao) or
CROSS_ONLY (co) or CROSS_AND_AUTO (ca)
                     Default: 'ca'
                     Options: ao, co, ca



compression
---------------------------------------

:code:`False`

Produce compressed columns in the resulting measurement
set.
                     Default: False
                     Options: False|True



lazy
---------------------------------------

:code:`False`

Make the MS DATA column read the ASDM Binary data
directly (faster import, smaller MS).
                     Default: False
                     Options: False|True

                     Instead of writing a copy of the visibilities
		     into a standard DATA column, lazy=True will make
		     importasdm only write a lookup-table such that
		     later access to the DATA column will read the
		     ASDM binary visibility data directly. This
		     requires that the ASDM not be removed from its
		     location as long the the DATA column is
		     needed. Use method ms.asdmref() to query and
		     manipulate the reference to the ASDM.

                     lazy=True will save ca. 50% disk space and
		     accelerate the DATA column access by
		     ca. 10%. lazy=True will only work when there is
		     visibility data in the ASDM, not with pure
		     radiometer data.



asis
---------------------------------------

:code:`''`

Creates verbatim copies of the ASDM tables in the output
measurement set.
                     Default: none

                     The value given to this option must be a list of
		     table names separated by space characters; the
		     wildcard character '*' is  allowed in table
		     names.



wvr_corrected_data
---------------------------------------

:code:`'no'`

Specifies which values are considerd in the ASDM binary
data to fill the DATA column in the MAIN table of the MS.
                     Default: no
                     Options: no|yes|both

                     * no: uncorrected data
                     * yes: corrected data
                     * both: for corrected and uncorrected data. Note
		       if both is selected, two measurement sets are
		       created, one with uncorrected data and the
		       other with corrected data (which name is
		       suffixed by '-wvr-corrected')



scans
---------------------------------------

:code:`''`

Processes only the scans specified in the option's value.
                     Default: none (all scans)

                     This value is a semicolon separated list of scan
		     specifications. A scan specification consists in
		     an exec bock index  followed by the character ':'
		     followed by a comma separated list of scan
		     indexes or scan index ranges. A scan index is
		     relative to the exec block it belongs to. Scan
		     indexes are  1-based while exec blocks's are
		     0-based. 

                        Examples: 
                        '0:1' 
                        '2:2~6' 
                        '0:1;1:2~6,8;2:,3:24~30'
                        '1,2' 
                        '3:' alone will be interpreted as 'all the
			scans of the exec block#3'. An scan index or a
			scan index range not preceded by an exec block
			index will be interpreted as 'all the scans
			with such indexes in all the exec blocks'.  



ignore_time
---------------------------------------

:code:`False`

All the rows of the tables Feed, History, Pointing,
Source, SysCal, CalDevice, SysPower, and Weather are processed
independently of the time range of the selected exec block / scan.
                     Default: False
                     Options: False|True



process_syspower
---------------------------------------

:code:`True`

 The SysPower table is processed if and only if this
parameter is set to true.
                     Default: True
                     Options: True|False



process_caldevice
---------------------------------------

:code:`True`

The CalDevice table is processed if and only if this
parameter is set to true.
                     Default: True
                     Options: True|False



process_pointing
---------------------------------------

:code:`True`

The Pointing table is processed if and only if this
parameter is set to true. 
                     Default: True
                     Options: True|False

                     If set to False, the POINTING table is empty in
		     the resulting MS



process_flags
---------------------------------------

:code:`True`

Create online flags based on the Flag.xml, Antenna.xml
and SpectralWindow.xml files and copy them to the FLAG_CMD sub-table
of the MS.
                     Default: True
                     Options: True|False

                     The flags will NOT be applied unless  the
		     parameter applyflags is set to True. Optionally,
		     the flags can also be saved to an external ASCII
		     file if savecmds is set to True.



tbuff
---------------------------------------

:code:`float(0.0)`

Time padding buffer (seconds)
                     Subparameter of process_flags=True
                     Default: 0.0

                     NOTE: this time is in seconds. You should
		     currently set the value of tbuff to be 1.5x the
		     correlator integration time if greater than 1
		     second. For example, if the SDM has integrations
		     of 3 seconds, set tbuff=4.5.  Likewise, set
		     tbuff=15.0 for 10-sec integrations.



applyflags
---------------------------------------

:code:`False`

Apply the online flags to the MS.
                     Subparameter of process_flags=True
                     Default: False
                     Options: False|True



savecmds
---------------------------------------

:code:`False`

Save the flag commands to an ASCII file given by the
parameter outfile. 
                     Subparameter of process_flags=True
                     Default: False
                     Options: False|True



outfile
---------------------------------------

:code:`''`

Filename or list of filenames where to save the online
flag commands.
                     Subparameter of process_flags=True
                     Default: '' (it will save on a filename composed
		     from the MS name(s).) E.g., for vis='uid_A02.ms',
		     the outfile will be 'uid_A02_cmd.txt'.



flagbackup
---------------------------------------

:code:`True`

Back up flag column before applying flags.
                     Default: True
                     Options: True|False



verbose
---------------------------------------

:code:`False`

Produce log output as asdm2MS is being run
                     Default: False
                     Options: False|True



overwrite
---------------------------------------

:code:`False`

Over write an existing MS(s) or MS(s), if the option
wvr_corrected_data='both'
                     Default: False  (do not overwrite)
                     Options: False|True

                     NOTE: the overwrite parameter affects all the
		     output of the task. If any of the following
		     exist, it will not overwrite them. MS(s),
		     .flagversions, online flag files. When set to
		     True, it will overwrite the MS, .flagversions and
		     online flag file.    



showversion
---------------------------------------

:code:`False`

Report the version of asdm2MS being used
                     Default: False
                     Options: False|True



useversion
---------------------------------------

:code:`'v3'`

Version of asdm2MS to be used
                     Default: 'v3' (should work for all data)



bdfflags
---------------------------------------

:code:`False`

Set the MS FLAG column according to the ASDM _binary_
flags
                     Default: False
                     Options: False|True



with_pointing_correction
---------------------------------------

:code:`False`

Add (ASDM::Pointing::encoder -
ASDM::Pointing::pointingDirection) to the value to be written in
MS::Pointing::direction
                     Default: False
                     Options: False|True



remove_ref_undef
---------------------------------------

:code:`False`

If set to True then apply fixspwbackport on the resulting
MS(es).
                     Default: False
                     Options: False|True



convert_ephem2geo
---------------------------------------

:code:`True`

if True, convert any attached ephemerides to the GEO
reference frame (time-spacing not changed)
                     Default: True
                     Options: True|False

                     ALMA uses ephemerides with observer location
		     equal to the ALMA site. For later processing of
		     the radial velocity information in, e.g. cvel,  a
		     geocentric ephemeris is needed. Setting this
		     option to True will perform the conversion of
		     positions and velocities on all attached
		     ephemerides in the imported MS. This will neither
		     change the time-spacing nor the duration of the
		     ephemeris. No interpolation in time is done.



polyephem_tabtimestep
---------------------------------------

:code:`float(0.)`

Timestep (days) for the tabulation of polynomial
ephemerides. A value less than or equal to 0 disables tabulation.
                     Default: 0

                     Presently, VLA data can contain polynomial
		     ephemerides. ALMA data uses tabulated values.





