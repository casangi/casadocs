

# Solve for Calibration 

How to solve for various calibration terms from the data itself

The **gaincal**, **bandpass**, **polcal**, and **blcal** tasks actually solve for the unknown calibration parameters from the visibility data obtained on calibrator sources, placing the results in a calibration table. They take as input an MS, and a number of parameters that specify any prior calibration tables to pre-apply before computing the solution, as well as parameters controlling the exact properties of the solving process.

We first discuss the parameters that are in common between many of the calibration tasks.  Subsequent sub-sections will discuss the use of each of these solving task in more detail.

 

# Common Calibration Solver Parameters

There are a number of parameters that are in common between the calibration solver tasks.

### Input/output

The input MeasurementSet and output calibration table are controlled by the following parameters:

```
vis          =         ''   #Name of input visibility file
caltable     =         ''   #Name of output calibration table
```

The MS name is specified in *vis*. If it is highlighted red in the inputs then it does not exist, and the task will not execute. Check the name and path in this case.

The output table name is specified in *caltable*. Be sure to give a unique name to the output table, or be careful. If the table exists, then what happens next will depend on the task and the values of other parameters. The task may not execute giving a warning that the table already exists, or will go ahead and overwrite the solutions in that table, or append them. Be careful.

### Data selection

Data selection is controlled by the following parameters:

```
field        =         ''   #field names or index of calibrators: ''==>all
spw          =         ''   #spectral window:channels: ''==>all
intent       =         ''   #Select observing intent
selectdata   =      False   #Other data selection parameters
```

Field and spectral window selection are so often used, that we have made these standard parameters, *field* and *spw* respectively.  Additionally, *intent* is also included as a standard parameter to enable selection by the scan intents that were specified when the observations were set up and executed. They typically describe what was intended with a specific scan, i.e. a flux or phase calibration, a bandpass, a pointing, an observation of your target, or something else or a combination. The format for the scan intents of your observations are listed in the logger when you run listobs. Minimum matching with wildcards will work, like \*BANDPASS\*.  This is especially useful when multiple intents are attached to scans.  Finally, observation is an identifier to distinguish between different observing runs, mainly used for ALMA.

The selectdata parameter expands, revealing a range of other selection sub-parameters:

```
selectdata          =       True        #data selection parameters
     timerange      =         ''        #time range (blank for all)
     uvrange        =         ''        #uv range (blank for all)
     antenna        =         ''        #antenna/baselines (blank for all)
     scan           =         ''        #scan numbers (blank for all)
     correlation    =         ''        #correlations (blank for all)
     array          =         ''        #(sub)array numbers (blank for all)
     observation    =         ''        #Select by observation ID(s)
     msselect       =         ''        #MS selection (blank for all)
```

Note that if *selectdata=False* these parameters are not used when the task is executed, even if set non-trivially.

Among the most common *selectdata=True* parameters to use is uvrange, which can be used to exclude longer baselines if the calibrator is resolved, or short baselines if the calibrator contains extended flux not accounted for in the model.  The rest of these parameters may be set according to information and values available in the listobs output.  Note that all parameters are specified as strings, even if the values to be specified are numbers.  See the section on [MS Selection](https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset) for more details on the powerful syntax available for selecting data.

### Prior calibration

Calibration tables that have already been determined can be arranged for apply before solving for the new table using the following parameters:

```
docallib        =  False        #Use traditional cal apply parameters
     gaintable  =     []        #Gain calibration table(s) to apply on the fly
     gainfield  =     []        #Select a subset of calibrators from gaintable(s)
     interp     =     []        #Interpolation mode (in time) to use for each gaintable
     spwmap     =     []        #Spectral windows combinations to form for gaintable(s)
```

The *docallib* parameter is a toggle that can be used to select specification of prior calibration using the new \"cal library\" mechanism (*docallib=True*) which is described in greater detail [here.](https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/cal-library-syntax)

When *docalib=False*, the traditional CASA calibration apply sub-parameters will be used, as listed above.

#### ***gaintable***

The *gaintable* parameter takes a string or list of strings giving the names of one or more calibration tables to arrange for application. For example:

```
   gaintable = ['ngc5921.bcal','ngc5921.gcal']
```

specifies two tables, in this case bandpass and gain calibration tables respectively.

The *gainfield*, *interp*, and *spwmap* parameters key off *gaintable*, taking single values or lists, with an entries for each corresponding table in specified in *gaintable*.  The caltables can be listed in *gaintable* in any order, without affecting the order in which they are applied to the data (for consistency, this is controlled internally according to the [Measurement Equation](https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals/the-measurement-equation-calibration) framework).  If non-trivial settings are required for only a subset of the tables listed in *gaintable*, it can be convenient to specify these tables first in *gaintable*, include their qualifying settings first in the other paramters, and omit specifications for those tables not needing qualification (sensible defaults will be used for these).

#### ***gainfield***

The *gainfield* parameter specifies which field(s) from each respective *gaintable* to select for apply. This is a list, with each entry a string. The default for an entry means to use all in that table. For example, use

```
   gaintable = ['ngc5921.bcal', 'ngc5921.gcal']
   gainfield = [ '1331+305',    '1331+305,1445+099']
```

to specify selection of *1331+305* from *ngc5921.bcal* and fields *1331+305* and *1445+099* from *ngc5921.gcal*.  Selection of this sort is only needed if avoiding other fields in these caltables is necessary.  The field selection used here is the general MS Selection syntax.

In addition, *gainfield* supports a special value:

```
   gainfield = [ 'nearest' ]
```

which selects the calibrator that is the spatially closest (in sky coordinates) to each of the selected MS fields specified in the *field* data selection parameter.  Note that the nearest calibrator field is evaluated once per execution and is never dependent on time, spw or any other data meta-axis.  This can be useful for running tasks with a number of different sources to be calibrated in a single run, and when this simple proximity notion is applicable.   Note that the [cal library](https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/cal-library-syntax) mechanism provides increased flexibility in this area.

#### ***interp***

The *interp* parameter chooses the interpolation scheme to be used when pre-applying the solution in the tables. Interpolation in both time and frequency (for channel-dependent calibrations) are supported. The choices are currently \'*nearest\'* and \'*linear\'* for time-dependent interpolation, and \'*nearest\'*, \'*linear\'*, \'*cubic\'*, and \'*spline\'* for frequency-dependent interpolation.  Frequency-dependent interpolation is only relevant for channel-dependent calibration tables (like bandpass) that are undersampled in frequency relative to the data.

-   *\'nearest\'  * just picks the entry nearest in time or freq to the visibility in question
-   \'*linear*\'     calibrates each datum with calibration phases and amplitudes linearly interpolated from neighboring values in time or frequency. In the case of phase, this mode will assume that phase never jumps more than 180 degrees between neighboring points, and so phase changes exceeding this between calibration solutions cannot be corrected for.  Also, solutions will not be extrapolated arbitrarily in time or frequency for data before the first solution or after the last solution; such data will be calibrated using nearest to avoid unreasonable extrapolations.
-   \'*cubic*\'   (frequency axis only) forms a 3rd-order polynomial that passes through the nearest 4 calibration samples (separately in phase and amplitude)
-   \'*spline*\'   (frequency axis only) forms a cubic spline that passes through the nearest 4 calibration samples (separately in phase and amplitude)

The time-dependent interp options can be appended with *\'PD\'* to enable a \"phase delay\" correction per spw for non-channel-dependent calibration type.  For example: \'*linearPD*\'.  This will adjust the time-dependent phase by the ratio of the data frequency and solution frequency and effect a time-dependent delay-like calibration over spws, and is most useful when distributing a single-spw\'s solution (e.g.., as might be generated by *combine=\'spw\'* in **gaincal**) over many data spws, and when the the residual being calibrated is non-dispersively delay-like.

The time-dependent interp options can also be appended with *\'perobs\'* to enforce observation Id boundaries in the interpolation.

The frequency-dependent interp options can be appended with \'flag\' to enforce channel-dependent flagging by flagged bandpass channels (i.e., \'*nearestflag*\', \'*linearflag*\', \'*cubicflag*\', and \'*splineflag*\', rather than to automatically fill such channels in with interpolation (which is the default).

For each *gaintable*, specify the interpolation style in quotes, with the frequency-dependent interpolation style specified after a comma, if relevant.  For example:

```
   gaintable = ['ngc5921.bcal',  'ngc5921.gcal']
   gainfield = ['1331+305',      ['1331+305','1445+099'] ]
   interp =    ['linear,spline', 'linear']
```

uses linear interpolation on the time axis for both cal tables, and a cubic spline for interpolation of the frequency axis in the bandpass table.

#### ***spwmap***

The *spwmap* parameter is used to redistribute the calibration available in a caltable flexibly among spectral windows, thereby permitting correction of some spectral windows using calibration derived from others.   The *spwmap* parameter takes a list or a list of lists of integers, with one list of integers for every caltable specified in *gaintable*.  Each list is indexed by the MS spectral window ids, and the values indicate the calibration spectral windows to use for each MS spectral window.  I.e., for each MS spw, *i*, the calibration spw *j* will be *j=spwmap\[i\]*. 

The default for *spwmap* (an empty list per *gaintable*) means that MS spectral windows will be calibrated by solutions identified with the same index in the calibration table (i.e., by themselves, typically).  Explicit specification of the default would be *spwmap=\[0,1,2,3\]*, for an MS with four spectral windows.   Less trivially, for a caltable containing solutions derived from and labelled as spectral windows 0 and 1, these two cal spectral windows can be mapped to any of the MS spectral windows.  E.g., (for a single *gaintable*):

```
   spwmap=[0,1,1,0]                #apply from cal spw=0 to MS spws 0,3 and from cal spw 1 to MS spws 1,2
```

For multiple gaintables, use a lists of lists (one spwmap list per gaintable), e.g.,

```
   gaintable = ['ngc5921.bcal',  'ngc5921.gcal']
   gainfield = ['1331+305',      ['1331+305','1445+099'] ]
   interp =    ['linear,spline', 'linear']
   spwmap =    [ [0,1,1,0],      [2,3,2,3] ]
```

which will use bandpass spws 0 and 1 for MS spws (0,3), and (1,2), respectively, and gain spws 2 and 3 for MS spws (0,2) and (1,3), respectively.

Any spectral window mapping is mechanically valid, including using specific calibration spectral windows for more than one different MS spectral window (as above) and using alternate calibration even for spectral windows for which calibration is nominally available, as long as the mapped calibration spectral windows have calibration solutions available in the caltable.  If a mapped calibration spectral window is absent from the caltable (and not merely flagged), an exception will occur.

The scientific meaningfulness of a non-trivial spwmap specification is the responsibility of the user; no internal checks are performed to attempt the scientific validity of the mapping.  Usually, *spwmap* is used to distribute calibration such as Tsys, which may be measured in a wide low-resolution spectral window, to narrow high-resolution spectral windows that fall within the wide one.  It is also used to distribute calibration derived from a **gaincal** solve which was performed using *combine=\'spw\'* (e.g., for increased SNR) to each of the spectral windows (and perhaps others) aggregated in the solve; in this case, it may be useful to consider using the *\'PD\'* (\"phase delay\") interpolation option described above, to account for the frequency ratios between each of the individual MS spectral windows and the aggregated calibration spectral window. 

#### Absolute vs. Relative frequency in frequency-dependent interpolation

<div>

By default, frequency-dependent solutions are interpolated for application in absolute sky frequency units.  Thus, it is usually necessary to obtain **bandpass** solutions that cover the frequencies of all spectral windows that must be corrected.   In this context, it is mechanically valid to use *spwmap* to transfer a **bandpass** solution from a wide, low-resolution spectral window to a narrow, higher-resolution spectral window that falls within the wide one in sky frequency space.   On the other hand, if adequate data for a **bandpass** solution is unavailable for a specific spectral window, e.g., due to contamination by line emission or absorption (such as HI), or because of flagging, **bandpass** solutions from other spectral windows (i.e., at different sky frequencies) can be applied using *spwmap*.   In this case, it is also necessary to add *\'rel*\' to the frequency interpolation string in the *interp* parameter, as this will force the interpolation to be calculated in relative frequency units.  Specifically, the center frequency of the **bandpass** solution will be registered with the absolute center frequency of each of the MS spectral windows to which it is applied, thereby enabling relative frequency registration.  The quality of such calibration transfer will depend, of course, on the uniformity of the hardware parameters and properties determining the bandpass shapes in the observing system\--this is often appropriate over relatively narrow bandwidths in digital observing systems, as long as the setups are sufficiently similar (same sideband, same total spectral window bandwidth, etc., though note that the channelization need not be the same).  Traditionally (e.g., at the VLA, for HI observations), **bandpass** solutions for this kind of calibration transfer have be solved by combining spectral windows on either side of the target spectral window (see the task documentation for [**bandpass**](https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_bandpass) for more information on solving with *combine=\'spw\'*).

</div>

<div>

 

</div>

<div>

For example, to apply a bandpass solution from spectral window 0 (in a **bandpass** table called ngc5921.bcal) to MS spectral windows 0,1,2,3 with linear interpolation calculated in relative frequency units (and with frequency-dependent flagging respected):

</div>

<div>

```
   gaintable = ['ngc5921.bcal']
   interp =    ['nearest,linearflagrel']
   spwmap =    [ [0,0,0,0] ]
```

</div>

<div>

 

</div>

<div>

When selecting channels for a **bandpass** solution that will be applied using *\'rel\'*, it is important to recognize that the selected channels will be centered on each of the \_absolute\_ centers of the MS spectral windows to which it will be applied.   An asymmetric channel selection for the **bandpass** solve will cause an undesirable shift in the relative registration on apply.   Avoid this by using symmetrical channel selection (or none) for the **bandpass** solve.
</div>

<div>

Also note that if relative frequency interpolation is required but *\'rel\'* is not used in *interp*, the interpolation mechanism currently assumes you want absolute frequency interpolation.  If there is no overlap in absolute frequency, the result will be nearest (in channel) interpolation such that the calibration edge channel closest to the visibility data will be used to calibrate that data.  

</div>

<div>

 

</div>

<div>

Finally, please note that relative frequency interpolation is not yet available via the cal library.

</div>

<div>

 

</div>

### Parallactic angle

The *parang* parameter turns on the application of the antenna-based parallactic angle correction (P) in the Measurement Equation. This is necessary for polarization calibration and imaging, or for cases where the parallactic angles are different for geographically spaced antennas and it is desired that the ordinary calibration solves not absorb the inter-antenna parallactic angle phase. When dealing with only the parallel-hand data (e.g. RR, LL, XX, YY), and an unpolarized calibrator model for a co-located array (e.g. the VLA or ALMA), you can set *parang=False* and save some computational effort. Otherwise, set *parang=True* to apply this correction, especially if you are doing polarimetry.

### Solving parameters

The parameters controlling common aspects of the solving process itself are:

```
solint              =      'inf'        #Solution interval: egs. 'inf', '60s' (see help)
combine             =     'scan'        #Data axes which to combine for solve (obs, scan,
                                        #spw, and/or field)
preavg              =       -1.0        #Pre-averaging interval (sec) (rarely needed)
refant              =         ''        #Reference antenna name(s)
minblperant         =          4        #Minimum baselines _per antenna_ required for solve
minsnr              =        3.0        #Reject solutions below this SNR
solnorm             =      False        #Normalize solution amplitudes post-solve.
corrdepflags        =      False        #Respect correlation-dependent flags
```

The time and frequency (if relevant) solution interval is specified in *solint*. Optionally a frequency interval for each solution can be added after a comma, e.g. *solint=\'60s,300Hz\'*. Time units are in seconds unless specified differently. Frequency units can be either \'*ch*\' or \'*Hz*\' and only make sense for bandpass or frequency dependent polarization calibration.  On the time axis, the special value \'inf\' specifies an infinite solution interval encompassing the entire dataset, while \'int\' specifies a solution every integration.  Omitting the frequency-dependent solution interval will yield per-sample solutions on this axis.  You can use time quanta in the string, e.g. *solint=\'1min\'* and *solint=\'60s\'* both specify solution intervals of one minute. Note that \'*m*\' is a unit of distance (meters); \'*min*\' must be used to specify minutes. The *solint* parameter interacts with *combine* to determine whether the solutions cross scan, field, or other meta-data boundaries.

The parameter controlling the scope of each solution is *combine*. For the default, *combine=\'\'*, solutions will break at *obs*, *scan*, *field*, and *spw* boundaries. Specification of any of these in *combine* will extend the solutions over the specified boundaries (up to the solint). For example, *combine=\'spw\'* will combine spectral windows together for solving, while *combine=\'scan\'* will cross scans, and *combine=\'obs,scan\'* will use data across different observation IDs and scans (usually, obs Ids consist of many scans, so it is not meaningful to combine obs Ids without also combining scans). Thus, to do scan-based solutions (single solution for each scan, per spw, field, etc.), set

```
   solint = 'inf'
   combine = ''
```

To obtain a single solution (per spw, per field) for an entire observation id (or the whole MS, if there is only one obsid), use:

```
   solint = 'inf'
   combine = 'scan'
```

You can specify multiple choices for combination by separating the axes with commas, e.g.:

```
   combine = 'scan,spw'
```

<div class="alert alert-warning">
Care should be exercised when using *combine='spw'* in cases where multiple groups of concurrent spectral windows are observed as a function of time. Currently, only one aggregate spectral window can be generated in a single calibration solve execution, and the meta-information for this spectral window is calculated from all selected MS spectral windows. To avoid incorrect calibration meta-information, each spectral window group should be calibrated independently (also without using *append=True*). Additional flexibility in this area will be supported in a future version.
</div>

The reference antenna is specified by the *refant* parameter.  Ordinary MS Selection antenna selection syntax is used.  Ideally, use of *refant* is useful to lock the solutions with time, effectively rotating (after solving) the phase of the gain solutions for all antennas such that the reference antennas phase remains constant at zero.  In **gaincal,** it is also possible to select a *refantmode*, either \'*flex*\' or \'*strict*\'.  A list of antennas can be provided to this parameter and, for refantmode=\'flex\', if the first antenna is not present in the solutions (e.g., if it is flagged), the next antenna in the list will be used, etc.   See the documentation for the **rerefant** task for more information.  If the selected antenna drops out, the next antenna specified (or the next nearest antenna) will be substituted for ongoing continuity in time (at its current value) until the refant returns, usually at a new value (not zero), which will be kept fixed thenceforth.  You can also run without a reference antenna, but in this case the solutions will formally float with time; in practice, the first antenna will be approximately constant near zero phase. It is usually prudent to select an antenna near the center of the array that is known to be particularly stable, as any gain jumps or wanders in the *refant* will be transferred to the other antenna solutions. Also, it is best to choose a reference antenna that never drops out, if possible.Setting a *preavg* time will let you average data over periods shorter than the solution interval first before solving on longer timescales.  This is necessary only if the visibility data vary systematically within the solution interval in a manner independent of the solve-for factors (which are, by construction, considered constant within the solution interval), e.g., source linear polarization in **polcal**.  Non-trivial use of *preavg* in such cases will avoid loss of SNR in the averaging within the solution interval. 

The minimum signal-to-noise ratio allowed for an acceptable solution is specified in the *minsnr* parameter. Default is *minsnr=3*.

The *minblperant* parameter sets the minimum number of baselines to other antennas that must be preset for each antenna to be included in a solution. This enables control of the constraints that a solution will require for each antenna. 

The *solnorm* parameter toggles on the option to normalize the solution after the solutions are obtained. The exact effect of this depends upon the type of solution (see **gaincal**, **bandpass**, and **blcal**).  Not all tasks use this parameter.One should be aware when using *solnorm* that if this is done in the last stage of a chain of calibration, then the part of the calibration that is normalized away will be lost. It is best to use this in early stages (for example in a first bandpass calibration) so that later stages (such as final gain calibration) can absorb the lost normalization scaling. It is generally not strictly necessary to use *solnorm=True* at all, but it is sometimes helpful if you want to have a normalized bandpass for example.

The *corrdepflags* parameter controls how visibility vector flags are interpreted. If *corrdepflags=False* (the default), then when any one or more of the correlations in a single visibility vector is flagged (per spw, per baseline, per channel), it treats all available correlations in the single visibility vector as flagged, and therefore it is excluded from the calibration solve. This has been CASA\'s traditional behavior (prior to CASA 5.7), in order to be conservative w.r.t. flags. If instead *corrdepFlags=True* (for CASA 5.7+), correlation-dependent flags will be respected exactly and precisely as set, such that any available unflagged correlations will be used in the solve for calibration factors.  For the tasks currently supporting the *corrdepflags* parameter (*gaincal, bandpass, fringefit*), this means any unflagged parallel-hand correlations will be used in solving, even if one or the other parallel-hand (or either of the cross-hands) is flagged.  Note that the *polcal* task does not support *corrdepflags* since polarization calibration is generally more sensitive to correlation-dependence in the flagging in ways which may be ill-defined for partial flagging; this stricture may be relaxed in future for non-leakage solving modes.  Most notably, this feature permits recovery and calibration of visibilities on baselines to antennas for which one polarization is entirely flagged, either because the antenna did not have that polarization at all (e.g., heterogeneous VLBI, where flagged visibilities are filled for missing correlations on single-polarization antennas), or one polarization was not working properly during the observation. 

### Appending calibration solutions to existing tables

The *append* parameter, if set to *True*, will append the solutions from this run to existing solutions in *caltable*. Of course, this only matters if the table already exists. If *append=False* and the specified caltable exists, it will overwrite it (if the caltable is not open in another process).

<div class="alert alert-warning">
The *append* parameter should be used with care, especially when also using *combine* in non-trivial ways. E.g., calibration solves will currently refuse to append incongruent aggregate spectral windows (e.g., observations with more than one group of concurrent spectral windows) when using *combine='spw'*. This limitation arises from difficulty determining the appropriate spectral window fan-out on apply, and will be relaxed in a future version.
</div>

 

 

