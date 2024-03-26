sdgridold -- ASAP SD task [DEPRECATED]: SD gridding task -- single dish task
=======================================

Description
---------------------------------------

### DEPRECATION WARNING #################################################
This task will be removed in CASA 5.1.
The functionality of this task with MeasurementSet format is replicated
with sdimaging.
#########################################################################

Task sdgridold performs spatial gridding according to the user 
specification of spatial grid, convolution function, etc.
For grid configuration, the task supplements necessary information 
by referring input data if any of gridding parameter ('npix', 
'cell', or 'center') is not specified by the user. If 'center' is 
default value (empty string), central position of the grid will be 
set to the center of observed area, i.e. x=0.5*(xmax+xmin), 
y=0.5*(ymax+ymin). If either 'cell' or 'npix' is set, unspecified 
one will be calculated from the others. In that case, total extent of 
the grid will be set to cover all observed position. If neither 'cell' 
nor 'npix' is set, cell size will be set to 1.0 arcmin and number of 
pixel will be calculated based on that cell size.
Currently, only J2000 frame is supported.
  


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - infiles
     - :code:`numpy.array( [  ] )`
     - 
   * - antenna
     - :code:`int(-1)`
     - 
   * - spw
     - :code:`'-1'`
     - 
   * - scan
     - :code:`''`
     - 
   * - pol
     - :code:`''`
     - 
   * - gridfunction
     - :code:`'BOX'`
     - gridding function for imaging [\'box\',\'sf\',\'pb\',\'gauss\', or \'gjinc\']
   * - convsupport
     - :code:`int(-1)`
     - 
   * - truncate
     - :code:`int(-1)`
     - 
   * - gwidth
     - :code:`int(-1)`
     - 
   * - jwidth
     - :code:`int(-1)`
     - 
   * - weight
     - :code:`'UNIFORM'`
     - weight type [\'uniform\',\'tint\',\'tsys\', or \'tintsys\']
   * - clipminmax
     - :code:`False`
     - 
   * - outfile
     - :code:`''`
     - 
   * - overwrite
     - :code:`False`
     - 
   * - npix
     - :code:`int(-1)`
     - 
   * - cell
     - :code:`''`
     - 
   * - center
     - :code:`''`
     - 
   * - plot
     - :code:`False`
     - 


Parameter Explanations
=======================================



infiles
---------------------------------------

:code:`numpy.array( [  ] )`

a list of names of input SD datasets


antenna
---------------------------------------

:code:`int(-1)`

select an antenna name or ID, e.g. \'PM03\' (only effective for MS input)


spw
---------------------------------------

:code:`'-1'`

select data by IF IDs (spectral windows), e.g. \'3,5,7\' (\'\'=all)


scan
---------------------------------------

:code:`''`

select data by scan numbers, e.g. \'21~23\' (\'\'=all)


pol
---------------------------------------

:code:`''`

select data by polarization IDs, e.g. \'0,1\' (\'\'=all)


gridfunction
---------------------------------------

:code:`'BOX'`

gridding function for imaging


convsupport
---------------------------------------

:code:`int(-1)`

truncate of convolution kernel


truncate
---------------------------------------

:code:`int(-1)`

truncation radius of convolution kernel


gwidth
---------------------------------------

:code:`int(-1)`

HWHM for gaussian


jwidth
---------------------------------------

:code:`int(-1)`

c-parameter for jinc function


weight
---------------------------------------

:code:`'UNIFORM'`

weight type


clipminmax
---------------------------------------

:code:`False`

clip minimum and maximum values during gridding


outfile
---------------------------------------

:code:`''`

name of output file


overwrite
---------------------------------------

:code:`False`

overwrite the output file if already exists [True, False]


npix
---------------------------------------

:code:`int(-1)`

number of pixels in x and y, symmetric for single value


cell
---------------------------------------

:code:`''`

x and y cell size. default unit arcsec


center
---------------------------------------

:code:`''`

Image center


plot
---------------------------------------

:code:`False`

Plot result or not




