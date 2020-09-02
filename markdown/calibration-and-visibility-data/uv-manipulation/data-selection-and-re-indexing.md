

# Select/Reindex UV-data 

Notes on visibility selection and reindexing

**mstransform** / **split** are able to create a new MS with a specific data selection, for instance splitting a science target. The new MS contains only the selected data and also the subtables are re-generated to contain only the metadata matching the data selection. The details about pure split operation are described in the **split** task documentation.

Keywords relevant to data selection are as follows:

```
CASA <1>: inp mstransform
--------> inp(mstransform)

vis                 =         ''        #Name of input MeasurementSet or Multi-MS.
outputvis           =         ''        #Name of output MeasurementSet or Multi-MS.
tileshape           =        [0]        #List with 1 or 3 elements giving the
                                           tile shape of the disk data columns.
field               =         ''        #Select field using ID(s) or name(s).
spw                 =         ''        #Select spectral window/channels.
scan                =         ''        #Select data by scan numbers.
antenna             =         ''        #Select data based on antenna/baseline.
correlation         =         ''        #Correlation: '' ==> all, correlation='XX,YY'.
timerange           =         ''        #Select data by time range.
intent              =         ''        #Select data by scan intent.
array               =         ''        #Select (sub)array(s) by array ID number.
uvrange             =         ''        #Select data by baseline length.
observation         =         ''        #Select by observation ID(s).
feed                =         ''        #Multi-feed numbers: Not yet implemented.
datacolumn          = 'corrected'       #Which data column(s) to process.
keepflags           =       True        #Keep *completely flagged rows* or
                                           drop them from the output.
usewtspectrum       =      False        #Create a WEIGHT_SPECTRUM column in the output MS.
```

 

New features related to data selection and re-indexing provided by **mstransform** / **split** (but not in **oldsplit**) are the following:

-   Spectral weight initialization: **mstransform** can initialize the output *WEIGHT* and *SIGMA_SPECTRUM* columns by specifying *usewtspectrum = True*. The details about spectral weights initialization are described in section
-   Tile shape specification for the data columns: **mstransform** also allows to specify a custom default tile shape for the output data columns, namely a list of 3 elements specifying the number of correlations, channels and rows to be contained in each tile, for instance *tileshape = \[4,128,351\]* would specify a tile with shape (4 correlations)x(128 channels)x(351 rows). This can be used to optimize the access pattern of subsequent tasks, for instance imaging tasks.
-   Support for SPWs with different sets of correlation products: **mstransform** / **split** are both able to work when a given SPW is associated with several correlation products (like in some EVLA correlation setups). This is transparent for the user and simply works by using the spw data selection parameter normally. It also works in conjunction with the polarization parameter, so for instance if a given MS has separated RR and LL data associated with spw 0 the following data selection would work flawlessly: *spw = '0' correlation = 'LL'*
-   Support for multiple channel selection: Both **mstransform** / **split** are also capable of working with multiple channel selection. This support also goes transparently for the user, by simply following the SPW syntax as described in the [Visibility Data Selection](https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset) chapter. For example *spw = '4,7:4\~59,8:4\~13;18\~594' * which means \"select all channels in spectral window four, channels 4 through 59 inclusive in spectral window seven; also select spectral window 8, channels 4 through 13 and 18 through 594, also inclusive.\". See more examples of spectral window selections in the split [examples](https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_split/examples) chapter.

 

