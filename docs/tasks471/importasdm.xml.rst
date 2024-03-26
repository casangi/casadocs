importasdm -- Convert an ALMA Science Data Model observation into a CASA visibility file (MS) -- import/export task
=======================================

Description
---------------------------------------



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
     - 
   * - vis
     - :code:`''`
     - 
   * - createmms
     - :code:`False`
     - 
   * - separationaxis
     - :code:`'auto'`
     - 
   * - numsubms
     - :code:`'auto'`
     - 
   * - corr_mode
     - :code:`'all'`
     - 
   * - srt
     - :code:`'all'`
     - 
   * - time_sampling
     - :code:`'all'`
     - 
   * - ocorr_mode
     - :code:`'ca'`
     - 
   * - compression
     - :code:`False`
     - 
   * - lazy
     - :code:`False`
     - 
   * - asis
     - :code:`''`
     - 
   * - wvr_corrected_data
     - :code:`'no'`
     - 
   * - scans
     - :code:`''`
     - 
   * - ignore_time
     - :code:`False`
     - 
   * - process_syspower
     - :code:`True`
     - 
   * - process_caldevice
     - :code:`True`
     - 
   * - process_pointing
     - :code:`True`
     - 
   * - process_flags
     - :code:`True`
     - 
   * - tbuff
     - :code:`float(0.0)`
     - 
   * - applyflags
     - :code:`False`
     - 
   * - savecmds
     - :code:`False`
     - 
   * - outfile
     - :code:`''`
     - 
   * - flagbackup
     - :code:`True`
     - 
   * - verbose
     - :code:`False`
     - 
   * - overwrite
     - :code:`False`
     - 
   * - showversion
     - :code:`False`
     - 
   * - useversion
     - :code:`'v3'`
     - 
   * - bdfflags
     - :code:`False`
     - 
   * - with_pointing_correction
     - :code:`False`
     - 
   * - remove_ref_undef
     - :code:`False`
     - 
   * - convert_ephem2geo
     - :code:`True`
     - 
   * - polyephem_tabtimestep
     - :code:`float(0.)`
     - 


Parameter Explanations
=======================================



asdm
---------------------------------------

:code:`''`

Name of input asdm directory (on disk)


vis
---------------------------------------

:code:`''`

Root name of the ms to be created. Note the .ms is NOT added 


createmms
---------------------------------------

:code:`False`

Create a multi-MS output


separationaxis
---------------------------------------

:code:`'auto'`

Axis to do parallelization across(scan, spw, baseline, auto)


numsubms
---------------------------------------

:code:`'auto'`

The number of SubMSs to create (auto or any number)


corr_mode
---------------------------------------

:code:`'all'`

specifies the correlation mode to be considered on input. A quoted string containing a sequence of ao, co, ac,or all separated by whitespaces is expected


srt
---------------------------------------

:code:`'all'`

specifies the spectral resolution type to be considered on input. A quoted string containing a sequence of fr, ca, bw, or all separated by whitespaces is expected


time_sampling
---------------------------------------

:code:`'all'`

specifies the time sampling (INTEGRATION and/or SUBINTEGRATION)  to be considered on input. A quoted string containing a sequence of i, si, or all separated by whitespaces is expected


ocorr_mode
---------------------------------------

:code:`'ca'`

output data for correlation mode AUTO_ONLY (ao) or CROSS_ONLY (co) or CROSS_AND_AUTO (ca)


compression
---------------------------------------

:code:`False`

Flag for turning on data compression


lazy
---------------------------------------

:code:`False`

Make the MS DATA column read the ASDM Binary data directly (faster import, smaller MS)


asis
---------------------------------------

:code:`''`

Creates verbatim copies of the ASDMtables in the ouput measurement set.  Value given must be a string of table names separated by spaces; A * wildcard is allowed.


wvr_corrected_data
---------------------------------------

:code:`'no'`

Specifies which values are considerd in the SDM binary data to fill the DATA column in the MAIN table of the MS. Expected values for this option are: no, for uncorrected data (default), yes, for the corrected data, and both, for for corrected and uncorrected data. Note if both is selected two measurement sets are created, one with uncorrected data and the other with corrected data.  


scans
---------------------------------------

:code:`''`

processes only the specified scans. This value is a semicolon separated list of scan specifications. A scan specification consists in an exec bock index followed by the : character;  followed by a comma separated list of scan indexes or scan index ranges. A scan index is relative to the exec block it belongs to. Scan indexes are 1-based while exec blocks are 0-based. "0:1" or "2:2~6" or "0:1,1:2~6,8;2:,3:24~30" "1,2" are valid values for the option. "3:" alone will be interpreted as, all the scans of the exec block#3.  An scan index or a scan index range not preceded by an exec block index will be interpreted as, all the scans with such indexes in all the exec blocks.  By default all the scans are considered. 


ignore_time
---------------------------------------

:code:`False`

All the rows of the tables Feed, History, Pointing, Source, SysCal, CalDevice, SysPower, and Weather are processed independently of the time range of the selected exec block / scan.


process_syspower
---------------------------------------

:code:`True`

 The SysPower table is processed if and only if this parameter is set to true.


process_caldevice
---------------------------------------

:code:`True`

The CalDevice table is processed if and only if this parameter is set to true.


process_pointing
---------------------------------------

:code:`True`

The Pointing table is processed if and only if this parameter is set to true. If set to False, the POINTING table is empty in the resulting MS


process_flags
---------------------------------------

:code:`True`

Create online flags in the FLAG_CMD sub-table.


tbuff
---------------------------------------

:code:`float(0.0)`

 Time padding buffer (seconds)


applyflags
---------------------------------------

:code:`False`

Apply the flags to the MS.


savecmds
---------------------------------------

:code:`False`

Save flag commands to an ASCII file


outfile
---------------------------------------

:code:`''`

Name of ASCII file to save flag commands


flagbackup
---------------------------------------

:code:`True`

Back up flag column before applying flags.


verbose
---------------------------------------

:code:`False`

Output lots of information while the filler is working


overwrite
---------------------------------------

:code:`False`

Over write an existing MS(s)


showversion
---------------------------------------

:code:`False`

Report the version of asdm2MS being used


useversion
---------------------------------------

:code:`'v3'`

Version of asdm2MS to be used (\'v3\' (default, should work for all data))


bdfflags
---------------------------------------

:code:`False`

Set the MS FLAG column according to the ASDM _binary_ flags


with_pointing_correction
---------------------------------------

:code:`False`

 add (ASDM::Pointing::encoder - ASDM::Pointing::pointingDirection) to the value to be written in MS::Pointing::direction


remove_ref_undef
---------------------------------------

:code:`False`

if set to True then apply fixspwbackport on the resulting MS(es).


convert_ephem2geo
---------------------------------------

:code:`True`

if True, convert any attached ephemerides to the GEO reference frame (time-spacing not changed)


polyephem_tabtimestep
---------------------------------------

:code:`float(0.)`

Timestep (days) for the tabulation of polynomial ephemerides. A value <= 0 disables tabulation.




