sdflag -- ASAP SD spectral spectral/row flagging task -- single dish task
=======================================

Description
---------------------------------------

Task sdflag performs either interactive or non-interactive channel/row 
based flagging on spectra. 

Currently, there are three ways of non-interactive flagging available: 
(1) channel or row based flagging by selecting spectra by field,
    lists of scan numbers, IF numbers, and polarization idices in
    mode='manual',
(2) channel based flagging by specifying a range of spectral values in
    mode='clip', and 
(3) row based flagging by specifying a list of row numbers in 
    mode='rowid'. Note this is an EXPERT mode since it might not be
    straight forward for general users to select data by row IDs in
    scantable.

In mode='manual', the channel based flagging are invoked when spw
parameter contains channel range selection. Otherwise, the whole
channels are flagged for the selected spectra. Note channel range
selection by spw parameter has effect only in mode='manual'.

Interactive flagging is available when mode='interactive'. 
The available ways of interactive flagging include: 
(1) row based flagging by selecting 'panel' and (2) channel
based flagging by selecting 'region's of channels on Flag plotter. 
See the cookbook for details of how to select channel regions and spectra
on the plotter.

NOTE the task sdflag only modifies flag information, FLAGROW and FLAGTRA, 
in the input scantable. This task keeps all records in input dataset. 
Data selection parameters are used for selecting data to modify flag
information.

If plotlevel>=1, the task asks you if you really apply the 
flags before it is actually written to the data with a plot 
indicating flagged regions.

WARNING for overwrite option:
Be sure 'outform' is the same as data format of input file when you
overwrite it. The default value of the option 'overwrite'
is True in this task, thereby the current dataset (infile) is 
overwritten unless a different file name is set to outfile. 
There is a known issue in overwriting infile. If 'outform' differs to the
data format of infile, the data is overwritten with the new data format 
(specified by 'outform') and the data in the original format will be lost.




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
   * - mode
     - :code:`'manual'`
     - mode of data selection and flag operation [\'manual\', \'clip\', \'interactive\', \'rowid\'(expert)]
   * - unflag
     - :code:`False`
     - 
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - timerange
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
   * - restfreq
     - :code:`''`
     - 
   * - frame
     - :code:`''`
     - frequency reference frame [\'LSRK\', \'TOPO\', \'LSRD\', \'BARY\', \'GALACTO\', \'LGROUP\', or \'CMB\'] (\'\'=current) Effective only when spw selection is in velocity or frequency unit.
   * - doppler
     - :code:`''`
     - doppler convention [\'RADIO\', \'OPTICAL\', \'Z\', \'BETA\', or \'GAMMA\'] (\'\'=current).  Effective only when spw selection is in velocity unit.
   * - clipminmax
     - :code:`numpy.array( [  ] )`
     - 
   * - clipoutside
     - :code:`True`
     - 
   * - showflagged
     - :code:`False`
     - 
   * - row
     - :code:`''`
     - 
   * - rasterrow
     - :code:`''`
     - 
   * - outfile
     - :code:`''`
     - 
   * - outform
     - :code:`'ASAP'`
     - output file format [\'ASAP\', \'MS2\', \'ASCII\', or \'SDFITS\'] (See a WARNING in help)
   * - overwrite
     - :code:`True`
     - overwrite the output file if already exists [True, False] (See a WARNING in help)
   * - plotlevel
     - :code:`int(0)`
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

select an antenna name or ID, e.g, \'PM03\' (only effective for MS input)


mode
---------------------------------------

:code:`'manual'`

mode of data selection and flag operation


unflag
---------------------------------------

:code:`False`

unflag selected data (False: flag, True: unflag)


field
---------------------------------------

:code:`''`

select data by field IDs and names, e.g. \'3C2*\' (\'\' = all)


spw
---------------------------------------

:code:`''`

select data by IF IDs (spectral windows), e.g., \'3,5,7\' (\'\' = all)


timerange
---------------------------------------

:code:`''`

select data by time range, e.g, \'09:14:0~09:54:0\' (\'\' = all) (see examples in help)


scan
---------------------------------------

:code:`''`

select data by scan numbers, e.g, \'21~23\' (\'\' = all)


pol
---------------------------------------

:code:`''`

select data by polarization IDs, e.g, \'0,1\' (\'\' = all)


beam
---------------------------------------

:code:`''`

select data by beam IDs, e.g, \'0,1\' (\'\' = all)


restfreq
---------------------------------------

:code:`''`

the rest frequency, \'1.41GHz\' (default unit: Hz). Effective only when spw selection is in velocity unit. (see examples in help) 


frame
---------------------------------------

:code:`''`

frequency reference frame (\'\'=current) Effective only when spw selection is in velocity or frequency unit.


doppler
---------------------------------------

:code:`''`

doppler convention (\'\'=current). Effective only when spw selection is in velocity unit.


clipminmax
---------------------------------------

:code:`numpy.array( [  ] )`

range of data that will NOT be flagged


clipoutside
---------------------------------------

:code:`True`

clip outside the range, or within it


showflagged
---------------------------------------

:code:`False`

show flagged data (in gray) on plots


row
---------------------------------------

:code:`''`

select data by row IDs to apply row-based flagging/unflagging (e.g., \'0,3,5\')


rasterrow
---------------------------------------

:code:`''`

select data by raster rows (e.g., \'0,3,5\')


outfile
---------------------------------------

:code:`''`

name of output file (See a WARNING in help)


outform
---------------------------------------

:code:`'ASAP'`

output file format (See a WARNING in help)


overwrite
---------------------------------------

:code:`True`

overwrite the output file if already exists (See a WARNING in help)


plotlevel
---------------------------------------

:code:`int(0)`

control for plotting of results (see examples in help)




