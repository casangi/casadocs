plotprofilemap -- Makes profile map. -- visualization task
=======================================

Description
---------------------------------------

  The plotprofilemap makes spectral profile map from specified image. 
  The task accepts both CASA image and FITS cube as an input.
  


Parameters
---------------------------------------
.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   * - Parameter
     - Default
     - Description
   * - imagename
     - :code:`''`
     - Input image name (CASA image or FITS)
   * - figfile
     - :code:`''`
     - Output figure name
   * - overwrite
     - :code:`False`
     - Overwrite existing figfile
   * - transparent
     - :code:`False`
     - Output transparent figure
   * - pol
     - :code:`int(0)`
     - Polarization component to be plotted
   * - spectralaxis
     - :code:`''`
     - Type of spectral axis
   * - restfreq
     - :code:`''`
     - Rest frequency
   * - plotrange
     - :code:`''`
     - Spectral axis range to plot
   * - title
     - :code:`''`
     - Title of the plot
   * - linecolor
     - :code:`'b'`
     - Line color
   * - linestyle
     - :code:`'-'`
     - Line style
   * - linewidth
     - :code:`float(0.2)`
     - Line width in points
   * - separatepanel
     - :code:`True`
     - Separate plots
   * - plotmasked
     - :code:`'empty'`
     - Masked data handling
   * - maskedcolor
     - :code:`'gray'`
     - Line color for masked data
   * - showaxislabel
     - :code:`False`
     - Show axis labels on the bottom left panel
   * - showtick
     - :code:`False`
     - Show axis ticks
   * - showticklabel
     - :code:`False`
     - Show axis tick labels on the bottom left panel
   * - figsize
     - :code:`''`
     - Size of the figure
   * - numpanels
     - :code:`''`
     - Number of panels


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Input image name (CASA image or FITS)


figfile
---------------------------------------

:code:`''`

Output figure name


overwrite
---------------------------------------

:code:`False`

Overwrite existing figfile


transparent
---------------------------------------

:code:`False`

Output transparent figure


pol
---------------------------------------

:code:`int(0)`

Polarization component to be plotted


spectralaxis
---------------------------------------

:code:`''`

Type of spectral axis


restfreq
---------------------------------------

:code:`''`

Rest frequency


plotrange
---------------------------------------

:code:`''`

Spectral axis range to plot


title
---------------------------------------

:code:`''`

Title of the plot


linecolor
---------------------------------------

:code:`'b'`

Line color


linestyle
---------------------------------------

:code:`'-'`

Line style


linewidth
---------------------------------------

:code:`float(0.2)`

Line width in points


separatepanel
---------------------------------------

:code:`True`

Separate plots


plotmasked
---------------------------------------

:code:`'empty'`

Masked data handling


maskedcolor
---------------------------------------

:code:`'gray'`

Line color for masked data


showaxislabel
---------------------------------------

:code:`False`

Show axis labels on the bottom left panel


showtick
---------------------------------------

:code:`False`

Show axis ticks


showticklabel
---------------------------------------

:code:`False`

Show axis tick labels on the bottom left panel


figsize
---------------------------------------

:code:`''`

Size of the figure


numpanels
---------------------------------------

:code:`''`

Number of panels




