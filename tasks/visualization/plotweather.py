#
# stub function definition file for docstring parsing
#

def plotweather(vis, seasonal_weight=0.5, doPlot=True, plotName=''):
    """
Plot elements of the weather table; estimate opacity.

Parameters
----------
vis : string
   MS name
seasonal_weight : double
   weight of the seasonal model
doPlot : bool
   set this to True to create a plot
plotName : string
   (Optional) the name of the plot file

Other Parameters
----------

Notes
-----





   task description



      This task is intended for VLA use only. Plots elements of the
      weather table; estimates opacity.

      Generates opacity estimates from both the weather data and a
      seasonal model.By default the returned opacity is the mean of
      these predictions, but this can be adjusted with seasonal_weight.
      Please note that the opacity determined in this manner is only a
      rough estimate which could propagate to an error when
      bootstrapping the flux density.

      These methods and models are described in detail in `EVLA Memo
      143 <https://library.nrao.edu/public/memos/evla/EVLAM_143.pdf>`__ , `VLA
      Test Memo
      232 <https://library.nrao.edu/public/memos/vla/test/VLAT_232.pdf>`__ , `VLA
      Scientific Memo
      176 <https://library.nrao.edu/public/memos/vla/sci/VLAS_176.pdf>`__ ,
      and references therein.

      Saves the plot to the following default file: MS name +
      .plotweather.png. Custom plot filenames must end in one of: .png,
      .pdf, .ps, .eps or .svg

      If run as a function, will return the mean zenith opacity per
      spectral window.

      The wind direction is defined as the direction where the wind is
      coming from (the arrow points into the wind), with north at the
      top and counterclockwise through west, south, and east.

    """
    pass
