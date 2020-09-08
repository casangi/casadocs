#
# stub function definition file for docstring parsing
#

def plotweather(vis, seasonal_weight=0.5, doPlot=True, plotName=''):
    r"""
Plot elements of the weather table; estimate opacity.

Parameters
   - vis_ (string) - MS name
   - seasonal_weight_ (double=0.5) - weight of the seasonal model
   - doPlot_ (bool=True) - set this to True to create a plot
   - plotName_ (string='') - (Optional) the name of the plot file


Description
   This task is intended for VLA use only. Plots elements of the
   weather table; estimates opacity.

   Generates opacity estimates from both the weather data and a
   seasonal model.By default the returned opacity is the mean of
   these predictions, but this can be adjusted with seasonal_weight.
   Please note that theopacity determined in this manner is only a
   rough estimatewhich could propagate to an error when
   bootstrapping the flux density.

   These methods and models are described in detail in `EVLA Memo
   143 <https://library.nrao.edu/public/memos/evla/EVLAM_143.pdf>`__ , `VLA
   Test Memo
   232 <https://library.nrao.edu/public/memos/vla/test/VLAT_232.pdf>`__ , `VLA
   Scientific Memo
   176 <https://library.nrao.edu/public/memos/vla/sci/VLAS_176.pdf>`__ ,
   and references therein.

   Saves the plot to the following default file:MS name +
   .plotweather.png. Custom plot filenames must end in one of: .png,
   .pdf, .ps, .eps or .svg

   If run as a function, will return the mean zenith opacity per
   spectral window.

   The wind direction is defined as the direction where the wind is
   coming from (the arrow points into the wind), with north atthe
   top and counterclockwise through west, south, and east.




Details
   Explanation of each parameter

.. _vis:

   .. rubric:: vis

   | MS name

.. _seasonal_weight:

   .. rubric:: seasonal_weight

   | weight of the seasonal model

.. _doPlot:

   .. rubric:: doPlot

   | set this to True to create a plot

.. _plotName:

   .. rubric:: plotName

   | (Optional) the name of the plot file


    """
    pass
