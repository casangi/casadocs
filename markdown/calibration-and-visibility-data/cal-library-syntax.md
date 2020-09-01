

# Cal Library Syntax 

How to use Cal Library

The \"Cal Library\" is a new means of expressing calibration application instructions.  It has nominally been available in **applycal** and the calibration solve tasks since CASA 4.1, via the *docallib=True* parameter, as an alternative to the traditional parameters (e.g., *gaintable*, etc.)  that most users continue to use.  As of CASA 4.5, we have deployed use of the Cal Library for *on-the-fly* calibration in **plotms** and **mstransform**.  In CASA 4.5, our intent is to demonstrate the Cal Library and begin familiarizing users with it.  The capabilities remain limited in some ways, and new features, additional flexibility, and broader deployment in more tasks will be offered in later releases.This page describes basic use of the Cal Library.

<div class="alert alert-warning">
Please note the section on current (CASA 4.5, 4.6, 4.7, 5.\*) limitations.
</div>

# Basic Cal Library usage

The Cal Library is a means of specifying calibration instructions in an ascii file, rather than via the traditional *gaintable/gainfield/interp/spwmap/calwt* parameters that often become clumsy when many caltables are involved, and which have rather limited flexibility.  Instead of specifying the traditional parameters, the file name is specified in the *callib* parameter in **applycal** or **plotms** (in **applycal** one must also specifiy *docallib=True*).  For example, to correct an MS called *my.ms*, with a Cal Library file called *mycal.txt*:

```
applycal(vis='my.ms',docallib=True,callib='mycal.txt')
```

In a Cal Library file, each row expresses the calibration apply instructions for a particular caltable and (optionally) a specific selection of data in the MS to which it is to be applied.For example, if *mycal.txt* contains:

```
# mycal.txt cal library file
caltable='cal.G' tinterp='linear' calwt=True
```

this will arrange a caltable called *cal.G* to be applied (with no detailed selection) to all MS data with linear interpolation in time, and with the weights also calibrated.  It corresponds to these settings for the traditional parameters in **applycal**:

```
applycal(vis='my.ms',gaintable='cal.G',gainfield='',interp='linear',
         spwmap=[],calwt=True)
```

If a bandpass table, *cal.B*, is also available for application, one might use the following Cal Library file:

```
# mycal.txt cal library file
caltable='cal.G' tinterp='linear' calwt=True
caltable='cal.B' finterp='linear' calwt=False
```

This example arranges the same instructions for *cal.G*, and adds a bandpass table that will be interpolated linearly in frequency (the default for time-dependent interpolation is linear, if the bandpass table contains more than one time sample), without weight calibration.  The corresponding form with the traditional parameters is:

```
applycal(vis='my.ms',gaintable=['cal.G','cal.B'], gainfield=['',''],
         interp=['linear','linear,linear'],
         spwmap=[],calwt=[True,False])
```

In general, the Cal LIbrary file should be easier to read and manage than the traditional parameters as the number of specified caltables grows.A more complicated example, involving non-trivial *spwmap* as well as field selection (*fldmap*) in the caltable:

```
# mycal.txt cal library file
caltable='cal.G' tinterp='linear' fldmap='nearest' spwmap=[0,1,1,3] calwt=True
caltable='cal.B' finterp='linear' fldmap='3' spwmap=[0,0,0,0] calwt=False
```

In this case, solutions from *cal.G* will be selected based on directional proximity (*\'nearest\'*) for each MS field via the *fldmap* parameter, and spw 2 will be calibrated by spw 1 solutions.  For *cal.B*, solutions from field id 3 will be selected exclusively from the caltable, with spw 0 calibrating all MS spws (of which there are apparently 4).  The corresponding settings for the traditional parameters is as follows:

```
applycal(vis='my.ms',gaintable=['cal.G','cal.B'], gainfield=['nearest','3'],
         interp=['linear','linear,linear'],
         spwmap=[[0,1,1,3],[0,0,0,0]],calwt=[True,False])
```

Comment lines may be included in the cal library file by starting a line with the $#$ character.  (Partial line comments are *not* supported, as yet.)  Existing cal library lines can be turned off (for experimentation purposes) by making those lines comments with $#$.

# More advanced Cal Library Usage

The real power of the Cal Library arises from the ability to specify calibration instructions for a caltable *per MS selection*.  This enables consolidating what would be multiple **applycal** executions using the traditional parameters into a single execution.  Extending the example from above, if the MS field *\'cal\'* should be calibrated by *cal.G* with *\'nearest\'* interpolation in time, and the field *\'sci\'* with *\'linear\'* interpolation in time, the following Cal Library file will achieve this:

```
# mycal.txt cal library file
caltable='cal.G' field='cal' tinterp='nearest' fldmap='nearest' spwmap=[0,1,1,3] calwt=True
caltable='cal.G' field='sci' tinterp='linear' fldmap='nearest' spwmap=[0,1,1,3] calwt=True
caltable='cal.B' finterp='linear' fldmap='3' spwmap=[0,0,0,0] calwt=False
```

Note that the algorithm for selecting solutions from the caltable (*fldmap=\'nearest\'*, which may resolve differently for the two MS fields) hasn\'t been changed, but it could be.  In fact, any of the calibration parameters can be adjusted per MS selection, except *calwt*, which if set to *True* for any MS selection, will be forced to *True* for all (to maintain weight consistency within the MS).  MS selection by spw, intent, and obs id can also be used (see the glossary below).The pair of **applycal** executions corresponding to this Cal Library would be:

```
applycal(vis='my.ms',field='cal',gaintable=['cal.G','cal.B'], gainfield=['nearest','3'],
         interp=['nearest','linear,linear'], spwmap=[[0,1,1,3],[0,0,0,0]],calwt=[True,False])

applycal(vis='my.ms',field='sci',gaintable=['cal.G','cal.B'], gainfield=['nearest','3'],
         interp=['linear','linear,linear'], spwmap=[[0,1,1,3],[0,0,0,0]],calwt=[True,False])
```

When there are many fields to which to apply carefully-selected calibration, *fldmap=\'nearest\'* may not properly select the correct calibrator fields for each target field.  In this case, the index list style form of *fldmap* (like *spwmap*) can be used (where field ids 1,4,6 are calibators, and 2,5,7 are the corresponding science fields):

```
# mycal.txt cal library file
caltable='cal.G' field='1,2,3,4,5,6,7' tinterp='nearest' fldmap=[0,1,1,3,4,4,6,6] spwmap=[0,1,1,3] calwt=True
caltable='cal.B' finterp='linear' fldmap='3' spwmap=[0,0,0,0] calwt=False
```

In this example, field 1 will calibrate itself and field 2.  Similarly, 4 will calibrate itself and 5, and 6 will calibrate itself and 7.   The bandpass calibrator (3) has been included, too, calibrating itself.  Field indices are specified in the *field* and *fldmap* parameters here, for clarity.   While field names can be used in *field*, the *fldmap* parameter, which in this form is an indexing list, can only interpret indices (note that field 0 is also explicitly included in the *fldmap* to preserve the integrity of the indexing). 

If multiple calibrators are required for each individual science fields, use the string selection form of *fldmap*, and specify separate entries for each science field:

```
# mycal.txt cal library file
caltable='cal.G' field='1,3,4,6,8,9,10' tinterp='nearest' fldmap='nearest' spwmap=[0,1,1,3] calwt=True
caltable='cal.G' field='2' tinterp='linear' fldmap='1,8' spwmap=[0,1,1,3] calwt=True
caltable='cal.G' field='5' tinterp='linear' fldmap='4,9' spwmap=[0,1,1,3] calwt=True
caltable='cal.G' field='7' tinterp='linear' fldmap='6,10' spwmap=[0,1,1,3] calwt=True
caltable='cal.B' finterp='linear' fldmap='3' spwmap=[0,0,0,0] calwt=False
```

The additional calibrators for science fields 2, 5, and 7 are 8, 9, and 10, respectively.  The first entry for *cal.G* accounts for all calibrators (including field 3, the bandpass calibrator), using *fldmap=\'nearest\'* to ensure they are each calibrated solely by themselves.  Then, in separate entries, fields 1 and 8 are selected for field 2, fields 4 and 9 are selected for field 5, and fields 6 and 10 are selecterd for field 7.   When using the string selection style in *fldmap*, field names can be used, if desired.

 

### Exclusivity

Since the Cal Library permits MS-selection-specific calibration specifications, it is even possible to specify different caltables for different MS selections, and take advantage of an implicit *exclusivity* property of the Cal Library.  In the above example, the G calibration for the *\'cal\'* and *\'sci\'* fields may come from different caltables, *\'cal.Gcal\'* and *\'cal.Gsci\',* respectiveily (these caltables may have been solved with different solution intervals, for example).  We would specify the Cal Library as follows:

```
# mycal.txt cal library file
caltable='cal.Gcal' field='cal' tinterp='nearest' fldmap='nearest' spwmap=[0,1,1,3] calwt=True
caltable='cal.Gsci' field='sci' tinterp='linear' fldmap='nearest' spwmap=[0,1,1,3] calwt=True
caltable='cal.B' finterp='linear' fldmap='3' spwmap=[0,0,0,0] calwt=False
```

In this case, the *cal.B* table would be applied to both fields as before, but *cal.Gcal* would only be applied to field *\'cal\'* and *cal.Gsci* would only be applied to field *\'sci\'*.   Both tables would ignore data from the field they weren\'t intended for.   The corresponding pair of **applycal** calls would be executed as follows:

```
applycal(vis='my.ms',field='cal',gaintable=['cal.Gcal','cal.B'], gainfield=['nearest','3'],
         interp=['nearest','linear,linear'], spwmap=[[0,1,1,3],[0,0,0,0]],calwt=[True,False])

applycal(vis='my.ms',field='sci',gaintable=['cal.Gsci','cal.B'], gainfield=['nearest','3'],
         interp=['linear','linear,linear'], spwmap=[[0,1,1,3],[0,0,0,0]],calwt=[True,False])
```

<div class="alert alert-warning">
NB: The Cal Libaray exclusivity property described here only works in CASA version 5.3 and later.  In prior versions, the Cal Library system implicitly assumed that all caltables specifed in the Cal Library were nominally intended for all data selections and would have as much MS-selection-specificty as needed explicitly included.   In that case, missing explicit specifications would result in an error message indicating that the Cal Library was missing an explicit MS-selection-specific entry.
</div>

 

# General Rules (current, as of CASA 4.5, 4.6, 4.7, 5.\*)

-    Each non-comment line in the Cal Library file must contain a valid (existing) caltable name
-    Blank lines (i.e., containing whitespace only) will be ignored
-    All parameters (see glossary below) are name/value pairs using an equals sign, delimited with spaces (no commas!)
-   Only those parameters (see glossary) for which non-default values are required need be specified
-   Each set of coordinated instructions must occur on a single line (there is no line continuation operator, as yet)
-   If detailed MS selection is used, care must be exercised to ensure it is mutually exclusive over all MS rows for the same caltable; there is currently no internal checking for redundancy, and only the last calibration instructions for a particular MS selection will be invoked
-   Full-line comments are supported by inserting the $#$ character as the first non-whitespace character in the line.  This mechanism can be used to turn off ordinary cal library lines.
-   When quoted items within a selection string are used, e.g. field=\'\"B0007+106; J0010+109\",GRB021004\', the string must have double quotation marks enclosing single quotation marks or single quotation marks enclosing double quotation marks.  Parsing will fail with a syntax error if the enclosed marks match the outer marks.  Note: the enclosed quotation marks are not needed; field=\'B0007+106; J0010+109,GRB021004\' would work, with the field names separated by commas.

### Limitations

-   Application of parallactic angle corrections is not yet supported within the Cal Library file (this only affects use in plotms, where there is no parang parameter)
-   Some parametrized calibration tables (*BPOLY*, *GSPLINE*) are not yet supported

 

# Conversion from Existing applycal Scripts

To convert exiting **applycal** commands, a simple experimental function, **applycaltocallib** is available.  To access it, type (within CASA):

```
from callibrary import applycaltocallib
```

Then, chose a filename for the cal library file, and supply existing settings for **applycal** parameters (*field*, *spw*, *intent*, *gaintable*, *gainfield*, *interp*, *spwmap*, *calwt*) to the **applycaltocallib** function:

```
callibfile='mycallib.txt'
applycaltocallib(filename=callibfile,append=False,
                 field,spw,intent,gaintable,gainfield,
                 interp,spwmap,calwt)
```

If *append=False*, the specified *filename* will be overwritten, if it already exists.  If *append=True*, new entries will be appended to the existing *filename*.  Only parameters with non-trivial **applycal** settings need be included.  In general, if *gaintable* is a python list, it is best if *gainfield*, *interp*, *spwmap*, and *calwt* (where non-trivially set) are also lists.For example, if your conventional script contains the following **applycal** executions (duplicated from above):

```
applycal(vis='my.ms',field='cal',
         gaintable=['cal.G','cal.B'], gainfield=['nearest','3'],
         interp=['nearest','linear,linear'],
         spwmap=[[0,1,1,3],[0,0,0,0]],
         calwt=[True,False])
applycal(vis='my.ms',field='sci',
         gaintable=['cal.G','cal.B'], gainfield=['nearest','3'],
         interp=['linear','linear,linear'],
         spwmap=[[0,1,1,3],[0,0,0,0]],
         calwt=[True,False])
```

\...these can be edited to **applycaltocallib** executions as:

```
callibfile='mycallib.txt'
applycaltocallib(filename='mycallib.txt',append=False,
                 field='cal',
                 gaintable=['cal.G','cal.B'], gainfield=['nearest','3'],
                 interp=['nearest','linear,linear'],
                 spwmap=[[0,1,1,3],[0,0,0,0]],
                 calwt=[True,False])
applycaltocallib(filename='mycallib.txt',append=True,
                 field='sci',
                 gaintable=['cal.G','cal.B'],
                 gainfield=['nearest','3'],
                 interp=['linear','linear,linear'],
                 spwmap=[[0,1,1,3],[0,0,0,0]],
                 calwt=[True,False])
```

After running them, *mycallib.txt* will contain:

```
caltable='cal.B' calwt=False field='cal' tinterp='linear' finterp='linear' fldmap='3' spwmap=[0, 0, 0, 0]
caltable='cal.G' calwt=True field='cal' tinterp='nearest' fldmap='nearest' spwmap=[0, 1, 1, 3]
caltable='cal.B' calwt=False field='sci' tinterp='linear' finterp='linear' fldmap='3' spwmap=[0, 0, 0, 0]
caltable='cal.G' calwt=True field='sci' tinterp='linear' fldmap='nearest' spwmap=[0, 1, 1, 3]
```

Note that the *cal.B* table is specified separately for the *\'cal\'* and *\'sci\'* fields with otherwise the same parameters; thus, those two lines could be manually consolidated to a single line with unified field selection, yielding:

```
caltable='cal.B' calwt=False field='cal,sci' tinterp='linear' finterp='linear' fldmap='3' spwmap=[0, 0, 0, 0]
caltable='cal.G' calwt=True field='cal' tinterp='nearest' fldmap='nearest' spwmap=[0, 1, 1, 3]
caltable='cal.G' calwt=True field='sci' tinterp='linear' fldmap='nearest' spwmap=[0, 1, 1, 3]
```

The field selection for the first row could be removed entirely if *cal.B* will be used uniformly for all fields in the MS (equivalently, *field=\'\'*).  This sort of row consolidation is optional, but it may have useful memory efficiency benefits when running **applycal**, and so is recommended.The **applycaltocallib** function should be considered experimental and used with care, and the resulting file examined thoroughly for correctness, since this function will not do any internal duplication checking or other sanity checks.  All other current constraints and limitations on cal libraries (as noted above) will apply.

 

# Glossary

This is a list of recognized Cal Library parameters.  For each, the default is indicated.  Additional parameters enhancing flexibility will be added in CASA 4.5 and later.

#### General

-   *caltable* \-\-- the name of the caltable for which the instructions on the current line apply; no default; required

#### MS Selection

Use these parameters to implement calibration instructions specific to particular MS selections (using standard MS Selection syntax, except where noted):

-   *field* \-\-- the MS field selection for which the calibration instructions on the current line apply; default=*\'\'* (all fields)
-   *spw* \-\-- the MS spw selection for which the calibration instructions on the current line apply; default=*\'\'* (all spws) Note that channel selection will be ignored, since the Cal Library does not support variety in calibration application at channel granularity.
-   *intent* \-\-- the MS intent selection for which the calibration instructions on the current line apply; default=*\'\'* (all intents)
-   *obs* \-\-- the MS observation id selection for which the calibration instructions on the current line apply; default=*\'\'* (all obs ids)

####  Interpolation/application

-   *tinterp* \-\-- the time-dependent interpolation mode; default=*\'linear\'* options: *\'linear\'*, *\'nearest\'*
-   *finterp* \-\-- the chan-dependent interpolation mode (only relevant for channelized caltables); default=\'linear\' options: *\'nearest\', \'linear\', \'cubic\', \'spline\'*
-   *calwt* \-\-- weight calibration; default=*True*  options: *True*, *False*

#### Calibration mapping

The following *\*map* parameters enable selection on the caltable.  For each *\*map* parameter, the basic specification is an ordered list indicating the caltable selection indices intended for each MS index on that axis.  E.g., *spwmap=\[0,1,1,3\]* means MS spws 0,1,3 will each be be calibrated by the same spw index from the caltable, and MS spw 2 will be calibrated by cal spw 1.  The *\*map* parameters support other short-hand options as well, as indicated below.  For defaults, \"index identity\" means that each MS index will be calibrated by the corresponding caltable index, and \"no explicit mapping\" means that no filter will be applied to that axis, and all available solutions on the axis will be included.

-   *spwmap* \-\-- spectral window mapping; default=index identity
-   *fldmap* \-\-- field mapping; default=*\[\]* (no explicit mapping); additional options: *\'nearest\'* or a string indicating field selection on the caltable (same as traditional *gainfield* options)
-   *antmap* \-\-- antenna id mapping; default=index identity
-   *obsmap* \-\-- obs id mapping; default=*\[\]* (no explicit mapping)

 

 

 

 

 

