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




    """
    pass
