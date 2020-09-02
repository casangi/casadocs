

# Combine MeasurementSets 

Concatenating multiple datasets (concat and virtualconcat)

Once you have your data in the form of CASA MeasurementSets, you can go ahead and process your data using the editing, calibration, and imaging tasks. In some cases, you will most efficiently operate on single MS for a particular session (such as calibration). Some tasks can take multiple MeasurementSets as input. For others, it is easiest to combine your multiple data files into one.

If you need to combine multiple datasets, you can use the **concat** task. The default inputs are:

```
#concat :: Concatenate several visibility data sets.
vis                     =   ['']    #Name of input visibility files to be concatenated
concatvis               =    ''     #Name of output visibility file
freqtol                 =    ''     #Frequency shift tolerance for considering data as the same spwid
dirtol                  =    ''     #Direction shift tolerance for considering data as the same field
respectname             =  False    #If true, fields with a different name are not merged even if their direction agrees
timesort                =  False    #If true, sort by TIME in ascending order
copypointing            =   True    #Copy all rows of the POINTING table.
visweightscale          =    []     #List of the weight scaling factors to be applied to the individual MSs
forcesingleephemfield   =    ''     #make sure that there is only one joint ephemeris for every field in this list
```

The *vis* parameter will take the list of MSs to combine. **concat** will presort them in time.

With *visweightscale*, a list of weights can be manually specified for the respective input data sets. They will be applied at the time of the combination. To determine the appropriate weights for this procedure, one can inspect the weights (\'Wt\' and \'WtSp\' axis inputs) of the input datasets in **plotms**. The weights of the individual MSs will be scaled in the concatenated output MS by the factors in this list. SIGMA will be multiplied by 1/sqrt(factor) (i.e. the weights will be multiplied by factor). This capability can be useful for handling heterogeneous arrays, depending on how the weights were intially estimated and set.

The *concatvis* parameter contains the name of the output MS. If this points to an existing file on disk, then the MS in vis will appended to it, otherwise a new MS file is created to contain the concatenated data. Be careful here!

The *timesort* parameter can be used to make sure the output MS is in time order (e.g. if your input MS have concurrent times). This can possibly speed up some subsequent calibration operations.

Furthermore, the parameter *copypointing* can be used to control whether the *POINTING* table will be carried along in the concatenation process or if the output MS should not contain a *POINTING* table. This table is quite large for some data (e.g. ALMA) and is mainly needed for mosaic imaging. If you are certain that you will not need it, you can save time and diskspace by setting *copypointing*=*False*.

For ALMA and VLA data, **importasdm** will fill the correct coordinates from ephemerides data into the *SOURCE* table. And, as stated in the [ephemeris](https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/ephemeris-data) section, **concat** will correctly merge fields which use the same ephemeris.

Using the parameter *forcesingleephemfield,* you can control whether the attached tabulated ephemerides are merged into one. By default, **concat** will only merge two ephemeris fields if the first ephemeris covers the time range of the second. Otherwise, two separate fields with separate ephemerides are placed in the output MS. In order to override this behaviour and make **concat** merge the non-overlapping or only partially overlapping input ephemerides, the name or id of the field in question needs to be placed into the list in parameter *forcesingleephemfield*. Example: *forcesingleephemfield=\'Neptune\'* - will make sure that there is only one joint ephemeris for field Neptune in the output MS.

The parameters *freqtol* and *dirtol* control how close together in frequency and angle on the sky spectral windows or field locations need to be before calling them the same.

<div class="alert alert-warning">
**ALERT:** If multiple frequencies or pointings are combined using *freqtol* or *dirtol*, then the data are not changed (i.e. not rephased to the single phase center). Use of these parameters is intended to be tolerant of small offsets (e.g. planets tracked which move slightly in J2000 over the course of observations, or combining epochs observed with slightly different positions).
</div>

For example:

```
default('concat')
vis = ['n4826_16apr.split.ms','n4826_22apr.split.ms']
concatvis = 'n4826_tboth.ms'
freqtol = '50MHz'
visweightscale=['1','2']
concat()
```

combines the two days in n4826_16apr.split.ms and n4826_22apr.split.ms into a new output MS called n4826_tboth.ms, and the second MS is weighted twice the first one.

<div class="alert alert-warning">
**ALERT:** If you are concatenating MSs which use antennas which were moved between observations, the MS definition does only foresee a unique antenna ID, but not a unique name(!). The moved antenna will appear twice in the antenna list under the same name but on different stations and with two different IDs. The pair ('*NAME@STATION*') will be the unique identifier.
</div>

If you would like to only concatenate the subtables of several MSs, not the bulk visibility data, you can use the task **testconcat** instead of **concat** to save time and diskspace. **testconcat** has the same parameters as **concat**. It produces an output MS with the concatenated subtables and an empty *MAIN* table.

Furthermore, the task **virtualconcat** permits to concatenate MSs into a [multi-MS](https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/the-multi-ms) (MMS) which is much faster as the data is moved into the MMS rather than copied and only some reindexing is done. The bulk data is not rewritten. If you want to keep a copy of the original MSs, set the parameter *keepcopy* of **virtualconcat** to True. The creation of that copy will of course consume some of the time you saved by doing a virtual concatenation. Otherwise **virtualconcat** offers the same functionality as **concat**.

 

