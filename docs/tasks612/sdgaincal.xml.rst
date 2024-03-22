sdgaincal -- MS SD gain calibration task -- single dish task
=======================================

Description
---------------------------------------


  


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
     - name of input SD dataset (must be MS)
   * - calmode
     - :code:`'doublecircle'`
     - gain calibration mode ("doublecircle")
   * - radius
     - :code:`''`
     - radius of central region to be used for calibration
   * - smooth
     - :code:`True`
     - smooth data or not
   * - antenna
     - :code:`''`
     - select data by antenna name or ID, e.g. "PM03"
   * - field
     - :code:`''`
     - select data by field IDs and names, e.g. "3C2*" ("" = all)
   * - spw
     - :code:`''`
     - select data by spw IDs (spectral windows), e.g., "3,5,7" ("" = all)
   * - scan
     - :code:`''`
     - select data by scan numbers, e.g. "21~23" (""=all)
   * - intent
     - :code:`''`
     - select data by observation intent, e.g. "OBSERVE_TARGET#ON_SOURCE" (""=all)
   * - applytable
     - :code:`''`
     - (List of) sky and/or tsys tables for pre-application
   * - interp
     - :code:`''`
     - Interp type in time[,freq], per gaintable. default==linear,linear
   * - spwmap
     - :code:`[ ]`
     - Spectral window mappings to form for applytable(s)
   * - outfile
     - :code:`''`
     - name of output caltable
   * - overwrite
     - :code:`False`
     - overwrite the output file if already exists [True, False]


Parameter Explanations
=======================================



infile
---------------------------------------

:code:`''`

name of input SD dataset (must be MS)


calmode
---------------------------------------

:code:`'doublecircle'`

gain calibration mode


radius
---------------------------------------

:code:`''`

radius of central region to be used for calibration


smooth
---------------------------------------

:code:`True`

smooth data or not


antenna
---------------------------------------

:code:`''`

select data by antenna name or ID, e.g. "PM03"


field
---------------------------------------

:code:`''`

select data by field IDs and names, e.g. "3C2*" ("" = all)


spw
---------------------------------------

:code:`''`

select data by spw IDs (spectral windows), e.g., "3,5,7" ("" = all)


scan
---------------------------------------

:code:`''`

select data by scan numbers, e.g. "21~23" (""=all)


intent
---------------------------------------

:code:`''`

select data by observation intent, e.g. "OBSERVE_TARGET#ON_SOURCE" (""=all)


applytable
---------------------------------------

:code:`''`

(List of) sky and/or tsys tables for pre-application


interp
---------------------------------------

:code:`''`

Interp type in time[,freq], per gaintable. default==linear,linear


spwmap
---------------------------------------

:code:`[ ]`

Spectral window mappings to form for applytable(s)
                     Only used if callib=False
                     default: [] (apply solutions from each calibration spw to
                     the same MS spw only)
                     Any available calibration spw can be mechanically mapped to any 
                      MS spw. 
                     Examples:
                        spwmap=[0,0,1,1] means apply calibration 
                          from cal spw = 0 to MS spw 0,1 and cal spw 1 to MS spws 2,3.
                        spwmap=[[0,0,1,1],[0,1,0,1]] (use a list of lists for multiple
                          applytables)
    


outfile
---------------------------------------

:code:`''`

name of output caltable


overwrite
---------------------------------------

:code:`False`

overwrite the output file if already exists




