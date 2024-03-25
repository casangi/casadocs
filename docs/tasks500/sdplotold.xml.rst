sdplotold -- ASAP SD task [DEPRECATED]: plot spectra -- single dish task
=======================================

Description
---------------------------------------

### DEPRECATION WARNING #################################################
This task will be removed in CASA 5.1.
To a very great extent, the functionality of this task with MeasurementSet
format is replicated with plotms.
#########################################################################

Task sdplotold displays single-dish spectra, total power,
or pointing direction of input data.
It assumes that the spectra have been calibrated.
It does allow selection of scans, spectral windows, polarizations, 
and some time and channel averaging/smoothing options also, but 
does not write out this data.

This task adds an additional toolbar to Matplotlib plotter. 
See the cookbook for details of its capability.
  


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - infile
     - :code:`''`
     - 
   * - antenna
     - :code:`int(0)`
     - 
   * - fluxunit
     - :code:`''`
     - 
   * - telescopeparam
     - :code:`''`
     - 
   * - specunit
     - :code:`''`
     - units for spectral axis [\'\',\'channel\',\'km/s\',\'GHz\',\'MHz\',\'kHz\', or \'Hz\']
   * - restfreq
     - :code:`''`
     - 
   * - frame
     - :code:`''`
     - 
   * - doppler
     - :code:`''`
     - 
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - scan
     - :code:`''`
     - 
   * - pol
     - :code:`''`
     - 
   * - beam
     - :code:`''`
     - 
   * - rastermode
     - :code:`'row'`
     - 
   * - raster
     - :code:`''`
     - 
   * - timeaverage
     - :code:`False`
     - 
   * - tweight
     - :code:`'tintsys'`
     - weighting for time averaging [\'tintsys\', \'tsys\', \'tint\', \'var\', or \'median\']
   * - scanaverage
     - :code:`False`
     - 
   * - polaverage
     - :code:`False`
     - 
   * - pweight
     - :code:`'tsys'`
     - weighting for polarization averaging [\'tsys\' or \'var\']
   * - kernel
     - :code:`''`
     - type of spectral smoothing [\'hanning\',\'gaussian\', or \'boxcar\'] (\'\'=no smoothing)
   * - kwidth
     - :code:`int(5)`
     - 
   * - plottype
     - :code:`'spectra'`
     - type of plot [\'spectra\',\'totalpower\',\'azel\',\'pointing\', or \'grid\']
   * - stack
     - :code:`'p'`
     - setting of plot overlay [\'b\'(beam), \'i\'(spw), \'p\'(pol), \'r\'(row), \'s\'(scan), \'t\'(time or src type)]
   * - panel
     - :code:`'i'`
     - multple panel setting [\'b\'(beam), \'i\'(spw), \'p\'(pol), \'r\'(row), \'s\'(scan), \'t\'(time)]
   * - flrange
     - :code:`numpy.array( [  ] )`
     - 
   * - sprange
     - :code:`numpy.array( [  ] )`
     - 
   * - linecat
     - :code:`'none'`
     - 
   * - linedop
     - :code:`float(0.0)`
     - 
   * - subplot
     - :code:`int(-1)`
     - 
   * - colormap
     - :code:`'none'`
     - 
   * - linestyles
     - :code:`'none'`
     - 
   * - linewidth
     - :code:`[ ]`
     - 
   * - histogram
     - :code:`False`
     - 
   * - center
     - :code:`''`
     - 
   * - cell
     - :code:`numpy.array( [  ] )`
     - 
   * - scanpattern
     - :code:`False`
     - 
   * - header
     - :code:`True`
     - 
   * - headsize
     - :code:`int(9)`
     - 
   * - plotstyle
     - :code:`False`
     - 
   * - margin
     - :code:`numpy.array( [  ] )`
     - 
   * - legendloc
     - :code:`int(1)`
     - 
   * - outfile
     - :code:`''`
     - 
   * - overwrite
     - :code:`False`
     - 


Parameter Explanations
=======================================



infile
---------------------------------------

:code:`''`

name of input SD dataset


antenna
---------------------------------------

:code:`int(0)`

select an antenna name or ID, e.g. \'PM03\' (only effective for MS input)


fluxunit
---------------------------------------

:code:`''`

units of the flux (\'\'=current)


telescopeparam
---------------------------------------

:code:`''`

parameters of telescope for flux conversion (see examples in help)


specunit
---------------------------------------

:code:`''`

units for spectral axis


restfreq
---------------------------------------

:code:`''`

rest frequency (default unit: Hz)


frame
---------------------------------------

:code:`''`

frequency reference frame (\'\'=current)


doppler
---------------------------------------

:code:`''`

doppler convention (\'\'=current). Effective only when spw selection is in velocity unit


field
---------------------------------------

:code:`''`

select data by field IDs and names, e.g. \'3C2*\' (\'\'=all)


spw
---------------------------------------

:code:`''`

select data by IF IDs (spectral windows), e.g. \'3,5,7\' (\'\'=all)


scan
---------------------------------------

:code:`''`

select data by scan numbers, e.g. \'21~23\' (\'\'=all)


pol
---------------------------------------

:code:`''`

select data by polarization IDs, e.g. \'0,1\' (\'\'=all)


beam
---------------------------------------

:code:`''`

select data by beam IDs, e.g. \'0,1\' (\'\'=all)


rastermode
---------------------------------------

:code:`'row'`

mode of raster selection [\'row\', \'raster\']


raster
---------------------------------------

:code:`''`

select data by raster scan row or map iteration e.g. \'0~2\' (\'\'=all)


timeaverage
---------------------------------------

:code:`False`

average spectra over time [True, False] (see examples in help)


tweight
---------------------------------------

:code:`'tintsys'`

weighting for time averaging


scanaverage
---------------------------------------

:code:`False`

average spectra within a scan number [True, False] (see examples in help)


polaverage
---------------------------------------

:code:`False`

average spectra over polarizations [True, False]


pweight
---------------------------------------

:code:`'tsys'`

weighting for polarization averaging


kernel
---------------------------------------

:code:`''`

type of spectral smoothing


kwidth
---------------------------------------

:code:`int(5)`

width of spectral kernel in channels


plottype
---------------------------------------

:code:`'spectra'`

type of plot


stack
---------------------------------------

:code:`'p'`

code for stacking on single plot for spectral plotting


panel
---------------------------------------

:code:`'i'`

code for splitting into multiple panels for spectral plotting


flrange
---------------------------------------

:code:`numpy.array( [  ] )`

range for flux axis of plot for spectral plotting


sprange
---------------------------------------

:code:`numpy.array( [  ] )`

range for spectral axis of plot


linecat
---------------------------------------

:code:`'none'`

control for line catalog plotting for spectral plotting


linedop
---------------------------------------

:code:`float(0.0)`

doppler offset for line catalog plotting (spectral plotting)


subplot
---------------------------------------

:code:`int(-1)`

number of subplots (row and column)


colormap
---------------------------------------

:code:`'none'`

the colours to be used for plot lines


linestyles
---------------------------------------

:code:`'none'`

the linestyles to be used for plot lines


linewidth
---------------------------------------

:code:`[ ]`

width of plotted lines


histogram
---------------------------------------

:code:`False`

plot histogram


center
---------------------------------------

:code:`''`

the central direction of gridding. (default: map center)


cell
---------------------------------------

:code:`numpy.array( [  ] )`

x and y cell size, e.g., ["1arcmin","1arcmin"]. (default map extent/subplot number)


scanpattern
---------------------------------------

:code:`False`

plot scan patterns.


header
---------------------------------------

:code:`True`

print header information on the plot


headsize
---------------------------------------

:code:`int(9)`

header fontsize


plotstyle
---------------------------------------

:code:`False`

customize plot settings


margin
---------------------------------------

:code:`numpy.array( [  ] )`

subplot margins in figure coordinate


legendloc
---------------------------------------

:code:`int(1)`

legend location


outfile
---------------------------------------

:code:`''`

file name for hardcopy output


overwrite
---------------------------------------

:code:`False`

overwrite the output file if already exists




