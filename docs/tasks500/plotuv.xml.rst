plotuv -- Plot the baseline distribution -- visualization,information task
=======================================

Description
---------------------------------------

      Plots the selected baselines of vis one field at a time, in kilowavelengths.
    


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - vis
     - :code:`''`
     - 
   * - field
     - :code:`''`
     - 
   * - antenna
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - observation
     - :code:`''`
     - 
   * - array
     - :code:`''`
     - 
   * - maxnpts
     - :code:`int(100000)`
     - 
   * - colors
     - :code:`numpy.array( [ 'r','y','g','b' ] )`
     - 
   * - symb
     - :code:`','`
     - 
   * - ncycles
     - :code:`int(1)`
     - 
   * - figfile
     - :code:`''`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file (MS)


field
---------------------------------------

:code:`''`

Select field using ID(s) or name(s)


antenna
---------------------------------------

:code:`''`

Select data based on antenna/baseline


spw
---------------------------------------

:code:`''`

Select spectral window/channels


observation
---------------------------------------

:code:`''`

Select by observation ID(s)


array
---------------------------------------

:code:`''`

Select (sub)array(s) by array ID number


maxnpts
---------------------------------------

:code:`int(100000)`

Maximum number of points per plot.


colors
---------------------------------------

:code:`numpy.array( [ 'r','y','g','b' ] )`

a list of matplotlib color codes


symb
---------------------------------------

:code:`','`

A matplotlib plot symbol code


ncycles
---------------------------------------

:code:`int(1)`

How many times to cycle through colors per plot.


figfile
---------------------------------------

:code:`''`

Save the plotted figure(s) using this name




