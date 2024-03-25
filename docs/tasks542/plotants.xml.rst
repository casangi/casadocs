plotants -- Plot the antenna distribution in the local reference frame: -- visualization, calibration task
=======================================

Description
---------------------------------------

       The location of the antennas in the MS will be plotted with
       X-toward local east; Y-toward local north.
	


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
   * - figfile
     - :code:`''`
     - 
   * - antindex
     - :code:`False`
     - 
   * - logpos
     - :code:`False`
     - 
   * - exclude
     - :code:`''`
     - 
   * - checkbaselines
     - :code:`False`
     - 
   * - title
     - :code:`''`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file (MS)


figfile
---------------------------------------

:code:`''`

Save the plotted figure to this file


antindex
---------------------------------------

:code:`False`

Label antennas with name and antenna ID


logpos
---------------------------------------

:code:`False`

Whether to plot logarithmic positions


exclude
---------------------------------------

:code:`''`

Antenna name/id selection to exclude from plot


checkbaselines
---------------------------------------

:code:`False`

Whether to check baselines in the main table.


title
---------------------------------------

:code:`''`

Title for the plot




