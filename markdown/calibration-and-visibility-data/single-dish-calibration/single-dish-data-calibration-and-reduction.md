

# Calibration & Reduction 

Reduction details and method

## Single-dish data calibration and reduction

Generally, the calibration of ALMA single-dish data requires essentially only two steps - the application of the $T_{sys}$ calibration, and the application of the \"sky\" calibration (i.e. OFF). With just these steps, the product is $T_A^*$ in units of Kelvin. While the steps are described in detail here, an example of the full single-dish calibration process can be found in the [M100 Band 3 Single Dish CASAguide](https://casaguides.nrao.edu/index.php/M100_Band3_SingleDish_4.3).

In the following description, we refer to data in the ALMA-native format of ASDM (ALMA Science Data Model) with a variable name *asdm*, while we refer to the CASA-native format of MeasurementSet with a variable name *sd_ms*. In the case of single-dish data, the MeasurementSet data are not formally *visibilities*, since they are simply auto-correlations.

1.  **importasdm**: Import the ASDM
2.  **listobs** - List observation parameters
3.  **flagdata** and **flagcmd** - A priori flagging
4.  **gencal**, **applycal**, and **sdcal**- Generate and apply the $T_{sys}$ and sky calibration tables
5.  **flagdata** - Do initial flagging
6.  **applycal** -  Calibrate the data into Kelvins
7.  **sdbaseline** - Subtract the baseline

**1. Import of the ASDM: *ImportASDM***

Import of ASDM data and conversion into the MeasurementSet format is achieved via the **importasdm** task. The task settings are a little different to those used when importing interferometer ASDMs. For instance, *bdfflags=False* will de-select application of the BDF format flags, which are of no consequence in the normal reduction process, and *with_pointing_correction=True* will directly apply the *measured* pointing direction (in Azimuth and Elevation) to the data, rather than the *commanded* pointing positions. For example:

```
importasdm(asdm, asis='Antenna Station Receiver Source CalAtmosphere CalWVR CorrelatorMode SBSummary', bdfflags=False, process_caldevice=False, with_pointing_correction=True)
```

 

**2. List observations parameters: *listobs* **

**listobs** works for single dish observations in the same way as for interferometry, and will detail the calibration scans.  It identifies pointing, $T_{sys}$, and target scans, the science target and OFF scans and their cadence, the correlator frequencies and configuration, and the antennas used in the observations. Unique to the single-dish data is the \#OFF_SOURCE intent. This task is used to identify which spectral windows are used for $T_{sys}$ observations.  This information is critical for those who wish to build their own calibrations.

```
listobs(sd_ms)
```

produces feedback in the logger (or optionally, to a file) from which we can determine which spectral windows are $T_{sys}$ observations and which are science observations.

```python
Spectral Windows: (25 unique spectral windows and 2 unique polarization setups)
SpwID Name #Chans Frame Ch0(MHz) ChanWid(kHz) TotBW(kHz) CtrFreq(MHz) BBC Num Corrs

  0  BB_1#SQLD                                       1   TOPO  195994.575   2000000.000   2000000.0 195994.5750        1  XX  YY
  1  BB_2#SQLD                                       1   TOPO  197932.075   2000000.000   2000000.0 197932.0750        2  XX  YY
  2  BB_3#SQLD                                       1   TOPO  207994.575   2000000.000   2000000.0 207994.5750        3  XX  YY
  3  BB_4#SQLD                                       1   TOPO  209994.575   2000000.000   2000000.0 209994.5750        4  XX  YY
  4  WVR#NOMINAL                                     4   TOPO  184550.000   1500000.000   7500000.0 187550.0000        0  XX
  5  X436890472#ALMA_RB_05#BB_1#SW-01#FULL_RES     128   TOPO  196986.763    -15625.000   2000000.0 195994.5750        1  XX  YY
  6  X436890472#ALMA_RB_05#BB_1#SW-01#CH_AVG         1   TOPO  195978.950   1796875.000   1796875.0 195978.9500        1  XX  YY
  7  X436890472#ALMA_RB_05#BB_2#SW-01#FULL_RES     128   TOPO  198924.263    -15625.000   2000000.0 197932.0750        2  XX  YY
  8  X436890472#ALMA_RB_05#BB_2#SW-01#CH_AVG         1   TOPO  197916.450   1796875.000   1796875.0 197916.4500        2  XX  YY
  9  X436890472#ALMA_RB_05#BB_3#SW-01#FULL_RES     128   TOPO  207002.388     15625.000   2000000.0 207994.5750        3  XX  YY
  10 X436890472#ALMA_RB_05#BB_3#SW-01#CH_AVG         1   TOPO  207978.950   1796875.000   1796875.0 207978.9500        3  XX  YY
  11 X436890472#ALMA_RB_05#BB_4#SW-01#FULL_RES     128   TOPO  209002.388     15625.000   2000000.0 209994.5750        4  XX  YY
  12 X436890472#ALMA_RB_05#BB_4#SW-01#CH_AVG         1   TOPO  209978.950   1796875.000   1796875.0 209978.9500        4  XX  YY
  13 BB_1#SQLD                                       1   TOPO  183375.638   2000000.000   2000000.0 183375.6378        1  XX  YY
  14 BB_2#SQLD                                       1   TOPO  181427.463   2000000.000   2000000.0 181427.4627        2  XX  YY
  15 BB_3#SQLD                                       1   TOPO  169374.840   2000000.000   2000000.0 169374.8404        3  XX  YY
  16 BB_4#SQLD                                       1   TOPO  170917.638   2000000.000   2000000.0 170917.6378        4  XX  YY
  17 X1857092512#ALMA_RB_05#BB_1#SW-01#FULL_RES   4096   TOPO  183162.808       122.070    500000.0 183412.7471        1  XX  YY
  18 X1857092512#ALMA_RB_05#BB_1#SW-01#CH_AVG        1   TOPO  183412.686    500000.000    500000.0 183412.6861        1  XX  YY
  19 X1857092512#ALMA_RB_05#BB_2#SW-01#FULL_RES   4096   TOPO  181177.524       122.070    500000.0 181427.4627        2  XX  YY
  20 X1857092512#ALMA_RB_05#BB_2#SW-01#CH_AVG        1   TOPO  181427.402    500000.000    500000.0 181427.4017        2  XX  YY
  21 X1857092512#ALMA_RB_05#BB_3#SW-01#FULL_RES   4096   TOPO  169587.670   -122.070    500000.0 169337.7310        3  XX  YY
  22 X1857092512#ALMA_RB_05#BB_3#SW-01#CH_AVG        1   TOPO  169337.670    500000.000    500000.0 169337.6700        3  XX  YY
  23 X1857092512#ALMA_RB_05#BB_4#SW-01#FULL_RES   4096   TOPO  171158.788   -122.070    500000.0 170908.8487        4  XX  YY
  24 X1857092512#ALMA_RB_05#BB_4#SW-01#CH_AVG        1   TOPO  170908.788    500000.000    500000.0 170908.7877        4  XX  YY
```

From this output, we see the science spectral windows are 17, 19, 21 and 23, and have 4096 channels, while the $T_{sys}$ spectral windows at 5, 7, 9 and 11 have 128 channels.

 

**3. A priori flagging: *flagcmd/flagdata***

**flagcmd** works the same way on single-dish data as for interferometry. In this case, invoking it here applies flagging, by default, from the FLAG_CMD file within the MeasurementSet.

```
flagcmd(vis = 'uid___A002_Xb978c3_X5c4b.ms', inpmode = 'table', useapplied = True, action = 'apply')
```

**flagdata** is used at this point to remove problematic data. Conventionally, 5% of the edges of the bands are removed, as these parts of the band are significantly and detrimentally affected by the low-sensitivity edges of the filter passband. In principle, they can be retained in the cases where spectral lines of interest fall in that area, though the sensitivity losses are significant.

Users should examine their spectra using **plotms**, and ensure any atmospheric lines are properly accounted for. This is particularly true for Band 5 which has a strong atmospheric absorption line at $\sim$183 GHz. There is no real way to remove the signature of the atmospheric lines in position-switched data, since the elevations of the ON (science target) and OFF (sky-calibration position) are almost always different, and therefore have different air masses. The most effective approach in this case is to complete the normal calibrations as described here, then apply a judiciously-selected bandpass correction polynomial and spectral window channel range, as described by the **sdbaseline** step below.

```
flagdata(vis=vis, mode='manual', spw='17:0~119;3960~4079,19:0~119;3960~4079,21:0~119;3960~4079,23:0~119;3960~4079', action='apply', flagbackup=True)
```

Both steps **flagcmd** and **flagdata** are generally useful, but care should be taken in case the emission lines of interest are being inadvertantly flagged out.

 

**4. Generation of the **$T_{sys}$ and $T_{sky}$ calibration tables: *gencal, sdcal and applycal*

There are two ways to proceed in CASA when computing and applying calibration tables for single dish observations.

1.  Build the $T_{sys}$ calibration tables with **gencal**, build the sky calibration tables with **sdcal,** and apply them with **applycal**
2.  Build and apply both the $T_{sys}$ and sky calibration tables with **sdcal**

The second option is faster, but users familar with the **gencal** and **applycal** tasks may prefer the first option.

In either case, the mapping between the $T_{sys}$ scans and science scans must be determined either by examination of the output of **listobs**, or by running the **sdcal** and specifying the method to be used to obtain the OFF position. Usually ALMA will take position-switched observations via *mode=*\'*ps*\', though other alternatives exist which do not need any OFF positions to be explicitly observed. The OFF can be obtained from the source data itself via *mode=*\'*otfraster*\' or *mode=*\'*off*\'.

 

In the first of the two cases mentioned above (having identified the target spectral windows as 17,19,21 and 23, and using a target identified by the variable name, \"source\") :

```
gencal(vis = sd_ms, caltable = sd_ms+'.tsys', caltype = 'tsys')

sdcal(infile = sd_ms, outfile = sd_ms+'.sky', calmode = 'ps')

from recipes.almahelpers import tsysspwmap
tsysmap = tsysspwmap(vis = sd_ms, tsystable = sd_ms+'.tsys', trim = False)

applycal(vis = sd_ms, applymode = 'calflagstrict', spw = '17,19,21,23', field = source, gaintable = [sd_ms+'.tsys', sd_ms+'.sky'], gainfield = ['nearest', source], spwmap = tsysmap)
```

 

In the second case:

```
sdcal(infile=sd_ms, calmode='ps,tsys,apply')
```

Note that we didn\'t specify the $T_{sys}$ spectral windows in the call to **sdcal. ** For ALMA single-dish data from Cycle 3 onward, this is okay since the $T_{sys}$ and science data share the same spectral window.   Alternatively, the mapping between the $T_{sys}$ and science spectral windows can be explicitly set with *spwmap* and *spw.* In this case, we would use:

```
sdcal(infile=vis, calmode='ps,tsys,apply', spwmap={17:[17], 19:[19], 21:[21],23:[23]}, spw='17,19,21,23')
```

The general structure of *spwmap* is {Tsys spw 0: \[science spw 0\],\....,Tsys spw n: \[science spw n\]} for 0 to n spectral windows.

**gencal** applied at this stage builds (and optionally applies) the $T_{sys}$ calibration tables. These calibrations are an intrinsic part of the ASDM. There are no re-computations applied to the $T_{sys}$ data by CASA. Ultimately, the $T_{sys}$ calibration tables will be applied in the **applycal** step, consistent with the descriptions of calibrations given in the sections above. We point out that the $T_{sys}$ calibrations are a multiplicative factor, so the order of the application of the $T_{sys}$ cal tables relative to the application of the $T_{sky}$ calibrations is immaterial.

**8. Subtracting the baseline: *sdbaseline***

It\'s important at this point to define exactly what is meant by *baseline* in the context of single-dish data. In interferometry, *baseline* refers to the spatial separation of antenna pairs.  For a single dish observation, *baseline* refers to the spectral pattern produced by the atmosphere and instrument. Since single-dish antennas measure total power, not an interference pattern, they are responsive to emission wherever it exists within the single-dish beam or signal path. This signal is dominated by the receiver/correlator/backend sampling function, but has a significant time-varying component usually dominated by atmospheric fluctuations. The power yielded by atmospheric fluctuations are invisible to interferometer observations, as they are in the *near field*, and are therefore generally resolved out from the data.  Note, though, that the atmospheric variability can contaminate interferometric measurements by introducing a decoherence in phase, and such losses in phase are not relevant for single-dish observations.

**sdbaseline** removes a spectral baseline from the data on a per-integration basis. The options here are extensive, and baseline subtraction can be complex when emission is strongly variable throughout the map, or when there are nearby atmospheric absorption features.  But CASA is effective at choosing intelligent defaults with *mode=\'auto\'*. With *mode=\'auto\'*, CASA will examine the brightness variability per integration and determine the most appropriate channel ranges for computing the spectral baseline, based on the mean absolute deviation of the channels. This approach is successful even when applied to spectra crowded heavily with emission lines.  As long as the emission-free parts of the spectrum have statistically significant representation in the data, then the *mode=\'auto\'* will be successful. Baseline corrections employed by CASA are subtracted, and therefore can be applied iteratively, as needed.

**sdbaseline** supports Polynomial, Chebychev and Sinusoid baseline removal. Sinusoidal baselines are determined with a Fourier transform of the spectral data - again, an automatic mode is available, where CASA will determine the most significant Fourier components and remove them, though specific wavenumbers can be explicitly added or removed on top of the automatic operation. Sinusoidal components occur in many single-dish telescopes, and are a typical manifestation of a standing-wave resonation of the main-reflector/subreflector cavity. ALMA has employed scattering cones in the single-dish subreflectors to effectively mitigate the strength of this standing wave. It\'s worth noting that removal of Fourier components should be applied with utmost caution; the result is effectively a convolution of the spectra with a spectral filter, and MUST affect the resulting emission spectra. Users who use this baseline mode should explore and characterize the consequences and subsquent error propagation, in the context of their own data.In this example, we remove a 1st order polynomial from spectral windows 17, 19, 21 & 23, automatically finding and masking out any lines brighter than 5 $\sigma$, and referencing the \"corrected\" (i.e. calibrated) data column.

```
sdbaseline(infile = sd_ms, datacolumn = 'corrected', spw = '17,19,21,23', maskmode = 'auto', thresh = 5.0, avg_limit = 4, blfunc = 'poly', order = 1, outfile = sd_ms+'.cal')
```

 

Note that at this point, the product dataset (sd_ms+\'.cal) has only four spectral windows. These are (if all is going well) the science observations which are $T_{sys}$ and sky calibrated, and are now bandpass-corrected.

 

**9. Convert the Science Target Units from Kelvin to Jansky: *scaleAutocorr***

To convert the units of the single-dish observations from $T_A^*$ (K) into Janskys and to prepare for combination with interferometer data, we need to obtain the empirically-determined Jy-to-K conversion data. These data already take into account any correlator non-linearities and also factor in the various subsystem efficiencies. 

The easiest way to obtain this is simply with a call to a specialized CASA task that obtains the Jy-to-K factors that accesses polynomal fits from ongoing calibration campaign data.

```
jyperk = es.getJyPerK(sd_ms+'.cal')
```

The contents of this variable jyperk is a python dictionary:

```
for ant in jyperk.keys():
for spw in jyperk[ant].keys():
scaleAutocorr(vis=sd_ms+'.cal', scale=jyperk[ant][spw]['mean'], antenna=ant, spw=spw)
```

 

**scaleAutocorr** simply applies the scaling from $T_A^*$ to Jy/beam. The scaling factors are determined empirically, as part of the QA2-level calibrations provided by ALMA. The scaling factors are to be provided to **scaleAutocorr** as a float, but are most conveniently applied in calls that iterate through antenna and spectral window, where the Jy-per-K factors are retained as a list with the format:

 

```python
 jyperk = 

  { antenna01_name { spw0: { 'mean': 44.345, 'n': '', 'std': ''},

              spw1: { 'mean': 44.374, 'n': '', 'std': ''},

              spw2: { 'mean': 44.227, 'n': '', 'std': ''},

              spw3: { 'mean': 44.203, 'n': '', 'std': ''}},

    antenna02_name: { spw0: { 'mean': 44.345, 'n': '', 'std': ''},

              spw1: { 'mean': 44.374, 'n': '', 'std': ''},

              spw2: { 'mean': 44.227, 'n': '', 'std': ''},

              spw3: { 'mean': 44.203, 'n': '', 'std': ''}}}
```

 

which can be iterated and applied to the actual data with the following loop:

```

to_amp_factor = lambda x: 1. / sqrt(x)

 

for ant in jyperk.keys():

   factors=[]

   for spw in jyperk[ant].keys():

      factors.append(jyperk[ant][spw]['mean'])

   gencal(vis=sd_ms, caltable=sd_ms+'.jy2ktbl', caltype='amp', spw=",".join(str(x) for x in jyperk[ant].keys()), parameter=map(to_amp_factor, factors))

   applycal(vis=sd_ms+'.cal', gaintable=sd_ms+'.jy2ktbl')

```

 

 

