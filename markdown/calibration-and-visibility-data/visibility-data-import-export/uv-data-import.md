

# UV Data Import 

Converting Telescope UV Data to a MeasurementSet

There are a number of tasks available to bring data in various forms into CASA as a MeasurementSet:

-   ALMA and VLA Science Data Model format via **importasdm** and **importevla**
-   historic VLA Archive format data via **importvla**
-   ATCA Data via **importatca**
-   MIRIAD Data from various telescopes via **importmiriad**
-   GMRT Data via **importgmrt**
-   UVFITS format can be imported into and exported from CASA (**importuvfits**, **importfitsidi**, and **exportuvfits**)


## ALMA and VLA Filling of Science Data Model (ASDM) data 

The ALMA and JVLA projects have agreed upon a common archival science data model (ASDM; sometimes also called SDM) format, and have jointly developed the software to fill this data into CASA. In the ASDM format, the bulk of the data is contained in large binary data format (BDF) tables, with the meta-data and ancillary information in XML tables. This is structured as a directory, like the MS, and was designed to be similar to the MS to facilitate conversion.

The content of an ASDM can be listed with the task **asdmsummary**:

```
#asdmsummary :: Summarized description of an ASDM dataset.
asdm = '' #Name of input ASDM directory
```

with an output that contains the list and positions of the antennas, followed by the metadata of each scan like observation time, source name, frequency and polarization setup:

```python
Input ASDM dataset : TDEM0008.sb3373760.eb3580330.55661.22790537037
========================================================================================
ASDM dataset :TDEM0008.sb3373760.eb3580330.55661.22790537037
========================================================================================

Exec Block : ExecBlock_0
Telescope : JVLA
Configuration name : B
Observer name : Dr. Juergen Ott
The exec block started on 2011-04-10T05:28:13.200000000 and ended on 2011-04-10T10:27:12.300000256

27 antennas have been used in this exec block.
        Id     Name         Make Station    Diameter         X              Y             Z
     Antenna_0  ea01    UNDEFINED   W36        25    -1606841.96   -5042279.689    3551913.017
     Antenna_1  ea02    UNDEFINED   E20        25     -1599340.8   -5043150.965    3554065.219
     Antenna_2  ea03    UNDEFINED   E36        25   -1596127.728   -5045193.751    3552652.421
     Antenna_3  ea04    UNDEFINED   W28        25   -1604865.649    -5042190.04    3552962.365
     Antenna_4  ea05    UNDEFINED   W08        25   -1601614.091   -5042001.653    3554652.509
     Antenna_5  ea06    UNDEFINED   N24        25    -1600930.06   -5040316.397    3557330.397
     Antenna_6  ea07    UNDEFINED   E32        25   -1597053.116   -5044604.687    3553058.987
     Antenna_7  ea08    UNDEFINED   N28        25   -1600863.684   -5039885.318    3557965.319
     Antenna_8  ea09    UNDEFINED   E24        25    -1598663.09   -5043581.392    3553767.029
     Antenna_9  ea10    UNDEFINED   N32        25   -1600781.039   -5039347.456    3558761.542
     Antenna_10  ea11    UNDEFINED   E04        25    -1601068.79    -5042051.91    3554824.835
     Antenna_11  ea12    UNDEFINED   E08        25   -1600801.926   -5042219.366    3554706.448
     Antenna_12  ea14    UNDEFINED   W12        25   -1602044.903   -5042025.824    3554427.832
     Antenna_13  ea15    UNDEFINED   W24        25   -1604008.742   -5042135.828    3553403.707
     Antenna_14  ea16    UNDEFINED   N12        25   -1601110.052   -5041488.079    3555597.439
     Antenna_15  ea17    UNDEFINED   W32        25   -1605808.656   -5042230.082    3552459.202
     Antenna_16  ea18    UNDEFINED   N16        25   -1601061.961    -5041175.88    3556058.022
     Antenna_17  ea19    UNDEFINED   W04        25   -1601315.893    -5041985.32    3554808.305
     Antenna_18  ea20    UNDEFINED   N36        25   -1600690.606   -5038758.734    3559632.061
     Antenna_19  ea21    UNDEFINED   E12        25    -1600416.51    -5042462.45    3554536.041
     Antenna_20  ea22    UNDEFINED   N04        25   -1601173.979   -5041902.658    3554987.518
     Antenna_21  ea23    UNDEFINED   E16        25   -1599926.104   -5042772.967    3554319.789
     Antenna_22  ea24    UNDEFINED   W16        25   -1602592.854   -5042054.997      3554140.7
     Antenna_23  ea25    UNDEFINED   N20        25   -1601004.709   -5040802.809    3556610.133
     Antenna_24  ea26    UNDEFINED   W20        25   -1603249.685   -5042091.404    3553797.803
     Antenna_25  ea27    UNDEFINED   E28        25   -1597899.903   -5044068.676    3553432.445
     Antenna_26  ea28    UNDEFINED   N08        25    -1601147.94   -5041733.837    3555235.956

Number of scans in this exec Block : 234

scan #1 from 2011-04-10T05:28:13.200000000 to 2011-04-10T05:33:35.500000256
        Intents : OBSERVE_TARGET
        Sources : 1331+305=3C286
        Subscan #1 from 2011-04-10T05:28:13.200000000 to 2011-04-10T05:33:35.500000256
                Intent : UNSPECIFIED
                Number of integrations : 322

                 Binary data in uid:///evla/bdf/1302413292901
                 Number of integrations : 322
                 Time sampling : INTEGRATION
                 Correlation Mode : CROSS_AND_AUTO
                 Spectral resolution type : FULL_RESOLUTION
                 Atmospheric phase correction : AP_UNCORRECTED
                 SpectralWindow_0 : numChan = 256, frame = TOPO,
                 firstChan = 8484000000, chandWidth = 125000 x Polarization_0 : corr = RR,LL

scan #2 from 2011-04-10T05:33:35.500000256 to 2011-04-10T05:35:35.200000000
        Intents : OBSERVE_TARGET
        Sources : 1331+305=3C286
        Subscan #1 from 2011-04-10T05:33:35.500000256 to 2011-04-10T05:35:35.200000000
                Intent : UNSPECIFIED
                Number of integrations : 119

                 Binary data in uid:///evla/bdf/1302413293280
                 Number of integrations : 119
                 Time sampling : INTEGRATION
                 Correlation Mode : CROSS_AND_AUTO
                 Spectral resolution type : FULL_RESOLUTION
                 Atmospheric phase correction : AP_UNCORRECTED
                 SpectralWindow_0 : numChan = 256, frame = TOPO,
                 firstChan = 8484000000, chandWidth = 125000 x Polarization_0 : corr = RR,LL

scan #3 from 2011-04-10T05:35:35.200000000 to 2011-04-10T05:36:34.999999488
        Intents : OBSERVE_TARGET
        Sources : 1331+305=3C286
        Subscan #1 from 2011-04-10T05:35:35.200000000 to 2011-04-10T05:36:34.999999488
...
```

The **importasdm** task will fill SDM1.2 and SDM1.3 format data into a CASA visibility data set (MS). ALMA data was recorded in SDM1.2 format from October 2009 until May 2011. Since May 2011, ALMA is using the SDM 1.3 format. In particular all science data from cycle 0 onwards is in SDM1.3. The JVLA also started using SDM1.2 in October 2009 and continues to use this format. **importasdm** can read all of the above formats. The parameter *useversion* can be used to enable the options *process_syspower*, *process_caldevice*, and *process_pointing*.

The default inputs of **importasdm** are:

```
#importasdm :: Convert an ALMA Science Data Model observation into a
CASA visibility file (MS) or single-dish data format (Scantable)
asdm                =         ''        #Name of input asdm directory (on
                                        #disk)
vis                 =         ''        #Root name of the MS to be created.
                                        #Note the .ms is NOT added
createmms           =      False        #Create a multi-MS output
singledish          =      False        #Set true to output single-dish data
                                        #format
corr_mode           =      'all'        #specifies the correlation mode to be
                                        #considered on input. A quoted string
                                        #containing a sequence of ao, co,
                                        #ac,or all separated by whitespaces
                                        #is expected
srt                 =      'all'        #specifies the spectral resolution
                                        #type to be considered on input. A
                                        #quoted string containing a sequence
                                        #of fr, ca, bw, or all separated by
                                        #whitespaces is expected
time_sampling       =      'all'        #specifies the time sampling
                                        #(INTEGRATION and/or SUBINTEGRATION)
                                        #to be considered on input. A quoted
                                        #string containing a sequence of i,
                                        #si, or all separated by whitespaces
                                        #is expected
ocorr_mode          =       'ca'        #output data for correlation mode
                                        #AUTO_ONLY (ao) or CROSS_ONLY (co) or
                                        #CROSS_AND_AUTO (ca)
compression         =      False        #Flag for turning on data compression
lazy                =      False        #Make the MS DATA column read the ASDM
                                        #Binary data directly (faster import,
                                        #smaller MS)
asis                =         ''        #Creates verbatim copies of the
                                        #ASDMtables in the ouput MeasurementSet.
                                        #Value given must be a string
                                        #of table names separated by spaces;
                                        #A * wildcard is allowed.
wvr_corrected_data  =       'no'        #Specifies which values are considerd
                                        #in the SDM binary data to fill the
                                        #DATA column in the MAIN table of the
                                        #MS. Expected values for this option
                                        #are: no, for uncorrected data
                                        #(default), yes, for the corrected
                                        #data, and both, for for corrected
                                        #and uncorrected data. Note if both
                                        #is selected two MeasurementSets are
                                        #created, one with uncorrected data
                                        #and the other with corrected data.
scans               =         ''        #processes only the specified scans.
                                        #This value is a semicolon separated
                                        #list of scan specifications. A scan
                                        #specification consists of an exec
                                        #block index followed by the :
                                        #character;  followed by a comma
                                        #separated list of scan indexes or
                                        #scan index ranges. A scan index is
                                        #relative to the exec block it
                                        #belongs to. Scan indexes are 1-based
                                        #while exec blocks are 0-based. "0:1"
                                        #or "2:2~6" or
                                        #"0:1,1:2~6,8;2:,3:24~30" "1,2" are
                                        #valid values for the option. "3:"
                                        #alone will be interpreted as, all
                                        #the scans of the exec block#3.  An
                                        #scan index or a scan index range not
                                        #preceded by an exec block index will
                                        #be interpreted as, all the scans
                                        #with such indexes in all the exec
                                        #blocks.  By default all the scans
                                        #are considered.
ignore_time         =      False        #All the rows of the tables Feed,
                                        #History, Pointing, Source, SysCal,
                                        #CalDevice, SysPower, and Weather are
                                        #processed independently of the time
                                        #range of the selected exec block /
                                        #scan.
process_syspower    =       True        #The SysPower table is processed if
                                        #and only if this parameter is set to
                                        #true.
process_caldevice   =       True        #The CalDevice table is processed if
                                        #and only if this parameter is set to
                                        #true.
process_pointing    =       True        #The Pointing table is processed if
                                        #and only if this parameter is set to
                                        #true. If set to False, the POINTING
                                        #table is empty in the resulting MS
process_flags       =       True        #Create online flags in the FLAG_CMD
                                        #sub-table.
     tbuff          =        0.0        #Time padding buffer (seconds)
     applyflags     =      False        #Apply the flags to the MS.
     savecmds       =      False        #Save flag commands to an ASCII file
     outfile        =         ''        #Name of ASCII file to save flag
                                        #commands

flagbackup          =       True        #Back up flag column before applying
                                        #flags.
verbose             =      False        #Output lots of information while the
                                        #filler is working
overwrite           =      False        #Over write an existing MS(s)
showversion         =      False        #Report the version of asdm2MS being
                                        #used
useversion          =       'v3'        #Version of asdm2MS to be used ('v3'
                                        #(default, should work for all data))
bdfflags            =      False        #Set the MS FLAG column according to
                                        #the ASDM _binary_ flags
with_pointing_correction =      False   #add (ASDM::Pointing::encoder -
                                        #ASDM::Pointing::pointingDirection)
                                        #to the value to be written in
                                        #MS::Pointing::direction
convert_ephem2geo   =       True        #if True, convert any attached
                                        #ephemerides to the GEO reference
                                        #frame (time-spacing not changed)
```

If *scans* is set, then **importasdm** processes only the scans specified in the option's value. This value is a semicolon separated list of scan specifications. A scan specification consists of an exec block index followed by the character ':' followed by a comma separated list of scan indexes or scan index ranges. A scan index is relative to the exec block it belongs to. Scan indexes are 1-based while exec blocks are 0-based. The expressions

```
 "0:1"
 "2:2~6"
 "0:1,1:2~6,8;2:,3:24~30"
 "1,2"
 "3:"
```

are all valid values for the [selection](https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset). The \"3:\" selector will be interpreted as 'all the scans of the exec block 3'. A scan index or a scan index range not preceded by an exec block index will be interpreted as 'all the scans with such indexes in all the exec blocks'. By default all the scans are considered.

When *process_flags=True* the task will create online flags based on the Flag.xml, Antenna.xml and SpectralWindow.xml files and copy them to the *FLAG_CMD* sub-table of the MS. The flags will NOT be applied unless the parameter *applyflags* is set to *True*. Optionally, the flags can also be saved to an external ASCII file if savecmds is set to *True*. The flags can later be applied to the MS using task **flagdata** in *list* mode.

When *bdfflags=True* the task will apply online flags contained in the ASDM BDF data by calling the executable bdflags2MS which the user can also do from the OS prompt. This is recommended for ALMA data.

If *singledish=True*, output data format is scantable (single-dish data format) instead of MS. In that case, you must specify name or id of the antenna that you want to obtain data. This can be done by using *antenna* parameter that is defined as a subparameter of *singledish*. For single-dish mode, only auto-correlation data are filled, i.e. *ocorr_mode* is forcibly set to '*ao*'.

The option *createmms* prepares the output file for [parallel processing](https://casa.nrao.edu/casadocs-devel/stable/parallel-processing) and creates a [multi-MS](https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/the-multi-ms).

 

### Specifics on importing Janksy VLA data with importasdm 

As of CASA 5.4, the task importevla is no longer available to import JVLA data, but a lot of its functionality is replaced by importasdm. However, several additional steps are required to duplicate the behaviour of importevla when using importasdm, involving a difference in default parameters and the fact that some of the on-the-go flagging cannot be performed by importasdm.

To mimic the behaviour of importevla, change the following parameters in **importasdm** from their default settings:

-   *ocorr_mode = \'co\'* to import cross-correlations only (discarding auto-correlations)*    *
-   *with_pointing_correction = True* to add pointing corrections*    *
-   *process_flags = True* (default) to read in the online flags, then *applyflags = True* to apply the online flags and/or *savecmd = True* to save flag commands to an ascii table.
-   For ephemeris objects: convert_ephem2geo = False

While online flags can thus be created by leaving the parameter *process_flags = True* by default, additional flagging steps need to be performed after **importasdm** to flag zero values and shadowing of antennas:

-   **Shadow flags:** use task **flagdata**, with *mode = \'shadow\'* (and optionally *reason = \'shadow\'*). The parameters *tolerance* and *addantenna* can be specified in flagdata in the same way they were used in importevla. *    *
-   **Zero clipping flags:** use task **flagdata**, with ***mode = \'clip\',*** *correlation = \'ABS_ALL\',* and *clipzeros = True* (and optionally *reason = \'clip\'*)*.* Note that the non-default case in importevla where *flagpol = False c*an be replicated by setting *correlation=\"ABS_RR, ABS_LL\".*

Like **importasdm**, the task **flagdata** can also save the flagging commands to an ascii table by setting *savepars = True.* To NOT apply the flags (*applyflags=False* in importevla) add *action=\'calculate\'* to flagdata. You may also chose to add a reason using the cmdreason argument, e.g. *cmdreason=\"CLIP_ZERO_ALL\".*

<div class="alert alert-warning">
**WARNING***:* The task **flagdata** can only write out the flag commands for that invocation of flagdata. The default *overwrite=True* must be used to overwrite an existing file. In order to save the commands from all 3 possible flagging steps (importasdm, zero, and shadow) each step must be saved to a separate file, which must then be concatenated into a single file to be used to flag the data.
</div>

 

### Import of ASDM data with option *lazy=True* 

With *lazy=False,* **importasdm** will fill the visibilities into a newly created *DATA* column of the MS converting them from their binary format in the ASDM to the CASA Table format.

If, however, *lazy* is set to *True*, the task will create the *DATA* column with an ALMA data-specific storage manager, the asdmstman, which enables CASA to directly read the binary data from the ASDM with on-the-fly conversion. No redundant copy of the raw data is created.

This procedure has the advantage that it saves more than 60% disk space and at least in some cases makes the access to the *DATA* column ≥ 10% faster because the data I/O volume is decreased. For the same reason, it also accelerates the import itself by ca. a factor 2. The acceleration is particularly large in the **applycal** task and here particularly on standard SATA disks.

E.g., if your ASDM has a size of 36 GB, the import with default parameters will turn this into an MS of 73 GB size (total disk space consumption = 36 GB + 73 GB = 109 GB). With *lazy=True*, the imported MS has a size of only 2 GB (total disk space consumption = 36 GB + 2 GB = 38 GB). I.e. your total disk space savings are ca. 65%. Even when you compare to the case where you delete the ASDM after normal import, the solution with lazy import and keeping the ASDM will save you ca. 48% disk space (in the example above 38 GB compared to 73 GB).

The only caveats are the following:

1.  You must not delete your ASDM. You can, however, move it but you have to update the reference stored in the MS. Symbolic links will work. See below on how to use the tool method **ms.asdmref()** to manipulate the ASDM reference.
2.  The lazily imported *DATA* column is read-only. But in any normal data reduction, the *DATA* column (as opposed to *CORRECTED_DATA*) is treated as read-only anyway.

The lazily imported MS is numerically identical with the traditionally imported MS and so are all results derived from the MSs.

An important additional tool to manipulate lazily imported MSs is the new method **ms.asdmref()** in the **ms** tool. If the MS is imported from an ASDM with option *lazy=True*, the DATA column of the MS is virtual and directly reads the visibilities from the ASDM. A reference to the original ASDM is stored with the MS. If the ASDM needs to be moved to a different path, the reference to it in the MS needs to be updated. This can be achieved with **ms.asdmref()**.

The method takes one argument: *abspath*. When called with *abspath* equal to an empty string (default), the method just reports the currently set ASDM path or an empty string if the ASDM path was not set, i.e. the MS was not lazily imported.

If you want to move the referenced ASDM to a different path, you can set the new absolute path by providing it as the value of *abspath* to the method.

```
 ms.open('uid___A12345_X678_X910.ms',False)
 ms.asdmref('/home/alma/myanalysis/uid___A12345_X678_X910')
 ms.close()
```

will set the new location of the referenced ASDM to /home/alma/myanalysis/uid\_\_\_A12345_X678_X910. Contrary to what one would expect from the parameter name, you can also provide a *relative* path as *abspath*. This path will be interpreted as relative to the location of the MS.

<div>

<div>

<div>

<div class="alert alert-info">

**Info**: the lazily imported MS itself can be moved without any restrictions independently from the referenced ASDM as long as the path to the ASDM remains accessible, even across file systems.

</div>

</div>

</div>

</div>


## VLA: Filling data from archive format (importvla) 

VLA data in archive format (i.e., as downloaded from the historic VLA data archive) are read into CASA from disk using the **importvla** task. The inputs are:

```
#importvla :: import VLA archive file(s) to a MeasurementSet:

archivefiles  =         ''   #Name of input VLA archive file(s)
vis           =         ''   #Name of output visibility file
bandname      =         ''   #VLA frequency band name:''=>obtain all bands in archive files
frequencytol  =   150000.0   #Frequency shift to define a unique spectral window (Hz)
project       =         ''   #Project name:  '' => all projects in file
starttime     =         ''   #start time to search for data
stoptime      =         ''   #end time to search for data
applytsys     =       True   #apply nominal sensitivity scaling to data & weights
autocorr      =      False   #import autocorrelations to ms, if set to True
antnamescheme =      'new'   #'old' or 'new'; 'VA04' or '4' for ant 4
keepblanks    =      False   #Fill scans with empty source names (e.g. tipping scans)?
evlabands     =      False   #Use updated eVLA frequencies and bandwidths
```

The main parameters are *archivefiles* to specify the input VLA Archive format file names, and *vis* to specify the output MS name.

<div class="alert alert-info">
**Info:** The scaling of VLA data both before and after the June 2007 Modcomp-turnoff is fully supported, based on the value of *applytsys*.
</div>

Note that *archivefiles* takes a string or list of strings, as there are often multiple files for a project in the archive.

For example:

```
archivefiles = ['AP314_A950519.xp1','AP314_A950519.xp2']
   vis = 'NGC7538.ms'
```

The **importvla** task allows selection on the frequency band. Suppose that you have 1.3 cm line observations in K-band and you have copied the archive data files AP314_A95019.xp\* to your working directory and started casa. Then,

```
  default('importvla')
   archivefiles = ['AP314_A950519.xp1','AP314_A950519.xp2','AP314_A950519.xp3']
   vis = 'ngc7538.ms'
   bandname = 'K'
   frequencytol = 10e6
   importvla()
```

If the data is located in a different directory on disk, then use the full path name to specify each archive file, e.g.:

```
archivefiles=['/home/rohir2/jmcmulli/ALMATST1/Data/N7538/AP314_A950519.xp1',
     '/home/rohir2/jmcmulli/ALMATST1/Data/N7538/AP314_A950519.xp2',
     '/home/rohir2/jmcmulli/ALMATST1/Data/N7538/AP314_A950519.xp3']
```

<div class="alert alert-info">
**Info:** **importvla** will import the on-line flags (from the VLA system) along with the data. Shadowed antennas will also be flagged. The flags will be put in the *MAIN* table and thus available to subsequent tasks and tools. If you wish to revert to unflagged data, use **flagmanager** to save the flags (if you wish), and then use **flagdata** with *mode='manual'* and *unflag=True* to toggle off the flags.
</div>

 

The other parameters are:

#### Parameter applytsys 

The *applytsys* parameter controls whether the nominal sensitivity scaling (based on the measured *TSYS*, with the weights scaled accordingly using the integration time) is applied to the visibility amplitudes or not. If *True*, then it will be scaled so as to be the same as AIPS **FILLM** (i.e. approximately in deciJanskys). Note that post-Modcomp data is in raw correlation coefficient and will be scaled using the *TSYS* values, while Modcomp-era data had this applied online. In all cases **importvla** will do the correct thing to data and weights based on an internal flag in the VLA Archive file, either scaling it or unscaling based on your choice for *applytsys*.

If *applytsys=True* and you see strange behavior in data amplitudes, it may be due to erroneous *TSYS* values from the online system. You might want to then fill with *applytsys=False* and look at the correlation coefficients to see if the behavior is as expected.

#### Parameter bandname

The *bandname* indicates the VLA Frequency band(s) to load, using the traditional bandname codes. These are:

-   '4' = 48-96 MHz
-   'P' = 298-345 MHz
-   'L' = 1.15-1.75 GHz
-   'C' = 4.2-5.1 GHz
-   'X' = 6.8-9.6 GHz
-   'U' = 13.5-16.3 GHz
-   'K' = 20.8-25.8 GHz
-   'Q' = 38-51 GHz
-   '' = all bands (default)

Note that as the transition from the VLA to JVLA progressed, the actual frequency ranges covered by the bands expanded, and additional bands were added (namely 'S' from 2-4 GHz and 'A' from 26.4-40 GHz).

#### Parameter frequencytol

The *frequencytol* parameter specifies the frequency separation tolerated when assigning data to spectral windows. The default is *frequencytol=150000* (Hz). For Doppler tracked data, where the sky frequency changes with time, a *frequencytol* \< 10000 Hz may produce too many unnecessary spectral windows.

#### Parameter project

You can specify a specific *project* name to import from archive files. The default '' will import data from all projects in file(s) archivefiles.

For example for VLA Project AL519:

```
project = 'AL519'    #this will work
project = 'al519'    #this will also work
```

while *project='AL0519'* will NOT work (even though that is what queries to the VLA Archive will print it as - sorry!).

#### Parameters starttime and stoptime 

You can specify start and stop times for the data, e.g.:

```
starttime = '1970/1/31/00:00:00'
stoptime = '2199/1/31/23:59:59'
```

Note that the blank defaults will load all data fitting other criteria.

#### Parameter autocorr 

Note that autocorrelations are filled into the data set if *autocorr=True*. Generally for the VLA, autocorrelation data is not useful, and furthermore the imaging routine will try to image the autocorrelation data (it assumes it is single dish data) which will swamp any real signal. Thus, if you do fill the autocorrelations, you will have to flag them before imaging.

#### Parameter antnamescheme 

The *antnamescheme* parameter controls whether **importvla** will try to use a naming scheme where JVLA antennas are prefixed with EA (e.g. 'EA16') and old VLA antennas have names prefixed with VA (e.g. 'VA11'). Our method to detect whether an antenna is JVLA is not yet perfected, and thus unless you require this feature, simply use *antnamescheme='old'*.

#### Parameter evlabands 

The *evlabands=True* option is provided to allow users to access JVLA frequencies outside the standard VLA tunings (e.g. the extended C-band above 6 GHz).

<div class="alert alert-warning">
**ALERT:** use of this option for standard VLA data will cause unexpected associations, such as X-band data below 8 GHz being extracted to C-band (as the JVLA C-band is 4--8 GHz). Use with care.
</div>

 

## Import ATCA and CARMA data 

There are several ways to import data from ATCA and CARMA into CASA. The data from these arrays has historically been processed in MIRIAD. For simple cases (single source and frequency) exporting from MIRIAD to UVFITS format and importing using **importuvfits** often works ok, although some fixes to the resulting MeasurementSet may be needed.

The **importmiriad** task reads MIRIAD visibility data and can handle multiple frequencies and sources in the input. Since it does not apply any calibration, make sure to apply it beforehand in MIRIAD.

The **importatca** task reads the ATCA archive format (RPFITS) directly, avoiding the need to go through MIRIAD to load the data. It can handle ATCA data from both the old and new (CABB) correlator.

 

### Import MIRIAD visibilities (importmiriad)

The task **importmiriad** allows one to import visibilities in the MIRIAD data format to be converted to a MS. The task has mainly been tested on data from the ATCA and CARMA telescopes and the inputs are:

```
#importmiriad :: Convert a Miriad visibility file into a CASA MeasurementSet
mirfile             =         ''        #Name of input Miriad visibility file
vis                 =         ''        #Name of output MeasurementSet
tsys                =      False        #Use the Tsys to set the visibility weights
spw                 =      'all'        #Select spectral windows
vel                 =         ''        #Select velocity reference (TOPO,LSRK,LSRD)
linecal             =      False        #(CARMA) Apply line calibration
wide                =      'all'        #(CARMA) Select wide window averages
debug               =          0        #Display increasingly verbose debug messages
```

The *mirfile* parameter specifies a single MIRIAD visibility file which should have any calibration done in MIRIAD already applied to it.

Set the *tsys* parameter to *True* to change the visibility weights from the MIRIAD default (usually the integration time) to the inverse of the noise variance using the recorded system temperature.

The *spw* parameter can be used to select all or some of the simultaneous spectral windows from the input file. Use the default of 'all' for all the data or use e.g., *spw='0,2'* to select the first and third window.

The *vel* parameter can be used to set the output velocity frame reference. For ATCA this defaults to '*TOPO*' and for CARMA it defaults to '*LSRK*'. Only change this if your data comes out with the incorrect velocity.

The *linecal* parameter is only useful for CARMA data and can apply the line calibration if it is stored with the MIRIAD data.

The *wide* parameter is only useful for CARMA data and can select which of the wide-band channels should be loaded.

 

### Import ATCA RPFITS data (importatca) 

The data from the ATCA is available from the archive in files in the RPFITS format. These files can be imported into CASA with the **importatca** task.

```
#importatca :: Import ATCA RPFITS file(s) to a MeasurementSet
files               =['*.C1234']        #Name of input ATCA RPFits file(s)
vis                 = 'c1234.ms'        #Name of output visibility file
                                        #(MeasurementSet)
options             =         ''        #Processing options: birdie, reweight,
                                        #noxycorr, fastmosaic, hires, noac
                                        #(comma separated list)
spw                 =       [-1]        #Specify the spectral windows to use,
                                        #default=all
nscans              =     [0, 0]        #Number of scans to skip followed by
                                        #number of scans to read
lowfreq             =   '0.1GHz'        #Lowest reference frequency to select
highfreq            =   '999GHz'        #Highest reference frequency to select
fields              =       ['']        #List of field names to select
edge                =          8        #Percentage of edge channels to flag.
                                        #For combined zooms, this specifies
                                        #the percentage for a single zoom
                                        #window
```

The files parameter can take a string or a list of strings as input and also allows the use of wildcards as shown in the example above.

For older ATCA continuum data (before the CABB correlator, April 2009) use *options='birdie,reweight'* to suppress internally generated RFI.

The options parameter:

-   *birdie* - (pre-CABB data only) Discard edge channels and channels affected by internal RFI.
-   *reweight* - (pre-CABB data only) Suppress ringing of RFI spikes by reweighting of the lag spectrum
-   *noxycorr* - do not apply the xy phase correction as derived from the switched noise calibration, by default this is applied during loading of the data.
-   *fastmosaic* - use this option if you are loading mosaic data with many pointings and only one or two integrations per pointing. This option changes the tiling of the data to avoid excessive I/O.
-   *hires* - use this option if you have data in time binning mode (as used for pulsars) but you want to make it look like data with very short integration time (no bins).
-   *noac* - discard the auto-correlation data

The *spw* parameter takes a list of integers and can be used to select one or more of the simultaneous frequencies. With CABB there can be up to 34 spectra. The order of the frequency bands in the RPFITS file is: the two continuum bands (0 and 1), followed by the zoom bands for the first frequency and then the zoom bands for the second frequency. Note that this *spw* parameter does not take a string with wildcards. Use *spw=-1* to get all the data.

The *nscans* parameter can be used to select part of a file, e.g., to retrieve a few test scans for a quick look.

The *lowfreq* and *highfreq* parameters select data based on the reference frequency.

The *fields* parameter selects data based on the field/source name.

The *edge* parameter specifies how many edge channels to discard as a percentage of the number of channels in each band. E.g., the default value of 8 will discard 8 channels from the top and bottom of a 2048 channel spectrum.

 

### UVFITS Import 

 

The UVFITS format is not exactly a standard, but is a popular archive and transport format nonetheless. CASA supports UVFITS files written by the AIPS FITTP task, and others.

UVFITS is supported for both import and export.

#### Import using importuvfits 

To import UVFITS format data into CASA, use the **importuvfits** task:

```
#In CASA: inp(importuvfits)
fitsfile            =         ''  #Name of input UVFITS file
vis                 =         ''  #Name of output visibility file (MS)
antnamescheme       =      'old'  #For VLA only; 'new' or 'old'; 'VA04' or '04' for VLA ant 4
```

This is straightforward, since all it does is read in a UVFITS file and convert it as best it can into a MS.

For example:

```
importuvfits(fitsfile='NGC5921.fits',vis='ngc5921.ms')
```

<div class="alert alert-info">
**INFO: **Here is a hint for handling CARMA data loaded into CASA using importuvfits:

tb.open("c0104I/ANTENNA",nomodify=False)
namelist=tb.getcol("NAME").tolist()
for i in range(len(namelist)):
 name = 'CA'+namelist[i]
 print ' Changing '+namelist[i]+' to '+name
 namelist[i]=name
 
tb.putcol("NAME",namelist)
tb.close()
</div>

 

#### Import using importfitsidi 

Some **uvfits** data is written in the FITS-IDI standard. Those files can be imported into CASA with the **importfitsidi** task:

```
#importfitsidi :: Convert a FITS-IDI file to a CASA visibility data set
fitsidifile         =       ['']       #Name(s) of input FITS-IDI file(s)
vis                 =          ''       #Name of output visibility file (MS)
constobsid          =      False        #If True, give constant obs ID==0 to
                                        #the data from all input fitsidi
                                        #files (False = separate obs id for
                                        #each file)
scanreindexgap_s    =        0.0        #min time gap (seconds) between
                                        #integrations to start a new scan
```

The *constobs* parameter can be used to give all visibilities the same observation id of 0. *scanreindexgap_s* controls the gap that defines different scans.

Example:

```
importfitsidi(fitsidifile='NGC1300.fits',vis='NGC1300.ms')
```

