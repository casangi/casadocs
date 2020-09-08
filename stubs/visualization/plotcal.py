#
# stub function definition file for docstring parsing
#

def plotcal(caltable, xaxis='', yaxis='', poln='', field='', antenna='', spw='', timerange='', subplot=111, overplot=False, clearpanel='Auto', iteration='', plotrange=[
            ], showflags=False, plotsymbol='o', plotcolor='blue', markersize=5.0, fontsize=10.0, showgui=True, figfile=''):
    r"""
An all-purpose plotter for calibration results 

Parameters
   - caltable_ (string) - 
   - xaxis_ (string='') - 
   - yaxis_ (string='') - 
   - poln_ (string='') - 
   - field_ (string='') - 
   - antenna_ (string='') - 
   - spw_ (string='') - 
   - timerange_ (string='') - 
   - subplot_ (int=111) - 
   - overplot_ (bool=False) - 
   - clearpanel_ (string='Auto') - 
   - iteration_ (string='') - 
   - plotrange_ (doubleArray=[
            ]) - 
   - showflags_ (bool=False) - 
   - plotsymbol_ (string='o') - 
   - plotcolor_ (string='blue') - 
   - markersize_ (double=5.0) - 
   - fontsize_ (double=10.0) - 
   - showgui_ (bool=True) - 
   - figfile_ (string='') - 


Description
   .. rubric:: Most of the functionality of plotcal is now
      implemented in plotms.
      

   We recommend the use of plotms for plotting calibration tables,
   except for certain VLBI cases that still need plotcal. Plotcal
   will be deprecated in the near future.

   

   The **plotcal** task is available for examining solutions of all
   of the basic solvable types.

   .. warning:: **Alert:** Currently, **plotcal** needs to know the MS from
      which caltable was derived to get indexing information. It does
      this using the name stored inside the table, which does not
      include the full path, but assumes the MS is in the *current
      working directory*. Thus if you are using a MS in a directory
      other than the current one, it will not find it. You need to
      change directories using *cd* in IPython (or *os.chdir()*
      inside a script) to the MS location. If the MS is not found,
      **plotcal** wil plot solutions, but ignore any specified
      selection.

   .. rubric:: Parameter descriptions
      

   .. rubric:: *caltable*
      

   Specify the name of the calibration table to be plotted as a
   string in *caltable*.

   

   .. rubric:: Axis choices: *xaxis, yaxis*
      

   Specify the axes to be plotted in *xaxis* and *yaxis*. The
   possible choices are listed in the Parameters section.

   

   .. rubric:: General selection: *field, spw, antenna, timerange*
      

   The **plotcal** task uses the same selection syntax as the solving
   tasks for these parameters. See
   `here <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__
   for more information.

   

   .. rubric:: Polarization selection: *poln*
      

   The *poln* parameter determines what polarization or combination
   of polarizations is being plotted. Choosing *poln='RL'* plots both
   R and L polarizations on the same plot. The respective XY options
   do equivalent things. The *poln='/'* option plots amplitude ratios
   or phase differences between whatever polarizations are in the MS
   (R and L or X and Y).

   

   .. rubric:: Plot control: *subplot, iteration, overplot,
      plotrange*
      

   The *subplot* parameter is particularly helpful in making
   multi-panel plots. The format is *subplot=yxn* where *yxn* is an
   integer with digit *y* representing the number of plots in the
   y-axis, digit *x* the number of panels along the x-axis, and digit
   *n* giving the location of the plot in the panel array (where n =
   1, ..., xy, in order upper left to right, then down).

   The *iteration* parameter allows you to select an identifier to
   iterate over when producing multi-page or multi-panel plots. The
   choices for *iteration* are: *'antenna', 'time', 'spw', 'field'*.
   For example, if per-antenna solution plots are desired, use
   *iteration='antenna'*. You can then use *subplot* to specify the
   number of plots to appear on each page. In this case, set the n to
   1 in *subplot=yxn*. Use the Next button on the **plotcal** window
   to advance to the next set of plots. Note that *iteration* can
   take more than one choice (as a single string containing a
   comma-separated list of the options). When specifying multiple
   iteration axes, the iteration order will be fixed (independent of
   the order specified in the iteration string). The iteration
   order (slowest to fastest) is
   *iteration='antenna,time,field,spw'*.

   The *overplot* parameter may be used to plot more than one
   execution of **plotcal** on the same plot surface. If
   *overplot=T*, and the specified plot axes are consistent, any
   existing plot will not be cleared before plotting. It can useful
   to use the *plotsymbol* parameter to change the plot symbols for
   different **plotcal** runs using *overplot*, so that the different
   solutions are distinguishable.

   The range of the two axes can be specified in the *plotrange*
   parameter, as a list of real numbers in the following order:

   ::

      plotrange=[xmin,xmax,ymin,ymax]

   If the both values for either axis are zeros, the plot range on
   that axis will be set automatically.

   .. rubric:: Symbol control: *plotsymbol, plotcolor, markersize,
      fontsize*
      

   Symbol type, color, and size, as well as fontsize for labels can
   be set with these parameters, which are adopted from the general
   matplotlib interface.

   .. rubric:: Plot files: *showgui, figfile*
      

   If *showgui=True*, an interactive plot window will be generated to
   show the plot. If a filename is specified in *figfile,* a plot
   file will be generated. The format of the plotfile is indicated
   by a specified suffix on the filename; supported formats include
   emf, eps, pdf, png, ps, raw, rgba, svg, svgz.




Details
   Explanation of each parameter

.. _caltable:

   .. rubric:: caltable

   | Name of input calibration table

.. _xaxis:

   .. rubric:: xaxis

   | Value to plot along x axis (time,chan,freq, antenna,antenna1,antenna2,scan, amp,phase,real,imag,snr, tsys,delay,rate,disp,spgain)

.. _yaxis:

   .. rubric:: yaxis

   | Value to plot along y axis (amp,phase,real,imag,snr, antenna,antenna1,antenna2,scan, tsys,delay,rate,disp,spgain,tec)

.. _poln:

   .. rubric:: poln

   | Antenna polarization to plot (RL,R,L,XY,X,Y,/)

.. _field:

   .. rubric:: field

   | field names or index of calibrators: \'\'==>all

.. _antenna:

   .. rubric:: antenna

   | antenna/baselines: \'\'==>all, antenna = \'3,VA04\'

.. _spw:

   .. rubric:: spw

   | spectral window:channels: \'\'==>all, spw=\'1:5~57\'

.. _timerange:

   .. rubric:: timerange

   | time range: \'\'==>all

.. _subplot:

   .. rubric:: subplot

   | Panel number on display screen (yxn)

.. _overplot:

   .. rubric:: overplot

   | Overplot solutions on existing display

.. _clearpanel:

   .. rubric:: clearpanel

   | Specify if old plots are cleared or not (ignore)

.. _iteration:

   .. rubric:: iteration

   | Iterate plots on antenna,time,spw,field

.. _plotrange:

   .. rubric:: plotrange

   | plot axes ranges: [xmin,xmax,ymin,ymax]

.. _showflags:

   .. rubric:: showflags

   | If true, show flagged solutions

.. _plotsymbol:

   .. rubric:: plotsymbol

   | pylab plot symbol

.. _plotcolor:

   .. rubric:: plotcolor

   | initial plotting color

.. _markersize:

   .. rubric:: markersize

   | Size of plotted marks

.. _fontsize:

   .. rubric:: fontsize

   | Font size for labels

.. _showgui:

   .. rubric:: showgui

   | Show plot on gui

.. _figfile:

   .. rubric:: figfile

   | \'\'= no plot hardcopy, otherwise supply name


    """
    pass
