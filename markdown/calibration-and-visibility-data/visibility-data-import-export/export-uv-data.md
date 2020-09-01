

# MeasurementSet Export 

Convert a MeasurementSet to UVFITS

## Export using exportuvfits

The **exportuvfits** task will take a MS and write it out in UVFITS format. The defaults are:

```
#  exportuvfits :: Convert a CASA visibility data set to a UVFITS file:
vis                 =         ''        #  Name of input visibility file
fitsfile            =         ''        #  Name of output UV FITS file
datacolumn          = 'corrected'       #  Visibility file data column
field               =         ''        #  Select field using field id(s) or field name(s)
spw                 =         ''        #  Select spectral window/channels
antenna             =         ''        #  Select data based on antenna/baseline
timerange           =         ''        #  Select data based on time range
avgchan             =          1        #  Channel averaging width (value > 1 indicates averaging)
writesyscal         =      False        #  Write GC and TY tables, (Not yet available)
multisource         =       True        #  Write in multi-source format
combinespw          =       True        #  Export the spectral windows as IFs
     padwithflags   =       True        #  Fill in missing data with flags to fit IFs

writestation        =       True        #  Write station name instead of antenna name
overwrite           =      False        #  Overwrite output file if it exists?
```

For example:

```
exportuvfits(vis='ngc5921.split.ms',
fitsfile='NGC5921.split.fits',
multisource=False)
```

 

The MS selection parameters *field, spw, antenna*, and *timerange* follow the [standard selection syntax](https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset).

The *datacolumn* parameter chooses which data-containing column of the MS is to be written out to the UV FITS file. Choices are: '*data*', '*corrected*', and '*model*'.

There are a number of special parameters that control what is written out. These are mostly here for compatibility with AIPS.

The *writesyscal* parameter toggles whether GC and TY extension tables are written. These are important for VLBA data, and for JVLA data.

<div class="alert alert-warning">
**ALERT:** The *writesyscal* option is not yet available.
</div>

The *multisource* parameter determines whether the UV FITS file is a multi-source file or a single-source file, if you have a single-source MS or choose only a single source. Note: the difference between a single-source and multi-source UVFITS file here is whether it has a source (SU) table and the source ID in the random parameters. Some programs (e.g. difmap) only accept single-source files. If you select more than one source in fields, then the *multisource* parameter will be overridden to be *True* regardless.

The *combinespw* parameter allows, if some conditions are met, exporting of all spectral windows (SpW) as a set of \"IF\"s in a single \"FREQID\" setup instead of giving each SpW its own FREQID in the FITS file. In this context an IF (Intermediate Frequency) is a specialization of an SpW, where each IF in a UV FITS file must have the same number of channels and polarizations, each channel must have the same width, and each IF must be present (even if flagged) throughout the entire observation. If these conditions are not met the data must be exported using multiple FREQIDs, the UV FITS equivalent of a general SpW. This matters since many (sub)programs will work with multiple IFs, but not multiple FREQIDs. For example, a UV FITS file with multiple FREQIDs can be read by AIPS, but you may find that you have to separate the FREQIDs with SPLIT before you can do very much with them. Therefore *combinespw* should be *True* if possible. Typically MSes where each band was observed simultaneously can be exported with *combinespw=True*. MSes where the tuning changed with time, e.g. 10 minutes at 4.8 GHz followed by 15 minutes at 8.4 GHz, should be exported to multiple UV FITS files using *spw* to select one tuning (set of simultaneous SpWs) per file.

The *writestation* parameter toggles the writing of the station name instead of antenna name.

