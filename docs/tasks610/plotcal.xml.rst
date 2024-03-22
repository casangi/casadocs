plotcal -- An all-purpose plotter for calibration results -- visualization, calibration task
=======================================

Description
---------------------------------------

An all-purpose plotter for calibration results.  The values for all
calibration solutions (G, T, GSPLINE, B, BPOLY, D) can be displayed
for a variety of polarization combinations and calibrations.  The
solutions may be iterated through antennas/spw/fields during one execution.

    


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - caltable
     - :code:`''`
     - 
   * - xaxis
     - :code:`''`
     - 
   * - yaxis
     - :code:`''`
     - 
   * - poln
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
   * - timerange
     - :code:`''`
     - 
   * - subplot
     - :code:`int(111)`
     - 
   * - overplot
     - :code:`False`
     - 
   * - clearpanel
     - :code:`'Auto'`
     - 
   * - iteration
     - :code:`''`
     - 
   * - plotrange
     - :code:`numpy.array( [  ] )`
     - 
   * - showflags
     - :code:`False`
     - 
   * - plotsymbol
     - :code:`'o'`
     - 
   * - plotcolor
     - :code:`'blue'`
     - 
   * - markersize
     - :code:`float(5.0)`
     - 
   * - fontsize
     - :code:`float(10.0)`
     - 
   * - showgui
     - :code:`True`
     - 
   * - figfile
     - :code:`''`
     - 


Parameter Explanations
=======================================



caltable
---------------------------------------

:code:`''`

Name of input calibration table


xaxis
---------------------------------------

:code:`''`

Value to plot along x axis (time,chan,freq, antenna,antenna1,antenna2,scan, amp,phase,real,imag,snr, tsys,delay,rate,disp,spgain)


yaxis
---------------------------------------

:code:`''`

Value to plot along y axis (amp,phase,real,imag,snr, antenna,antenna1,antenna2,scan, tsys,delay,rate,disp,spgain,tec)


poln
---------------------------------------

:code:`''`

Antenna polarization to plot (RL,R,L,XY,X,Y,/)


field
---------------------------------------

:code:`''`

field names or index of calibrators: \'\'==>all


antenna
---------------------------------------

:code:`''`

antenna/baselines: \'\'==>all, antenna = \'3,VA04\'


spw
---------------------------------------

:code:`''`

spectral window:channels: \'\'==>all, spw=\'1:5~57\'


timerange
---------------------------------------

:code:`''`

time range: \'\'==>all


subplot
---------------------------------------

:code:`int(111)`

Panel number on display screen (yxn)


overplot
---------------------------------------

:code:`False`

Overplot solutions on existing display


clearpanel
---------------------------------------

:code:`'Auto'`

Specify if old plots are cleared or not (ignore)


iteration
---------------------------------------

:code:`''`

Iterate plots on antenna,time,spw,field


plotrange
---------------------------------------

:code:`numpy.array( [  ] )`

plot axes ranges: [xmin,xmax,ymin,ymax]


showflags
---------------------------------------

:code:`False`

If true, show flagged solutions


plotsymbol
---------------------------------------

:code:`'o'`

pylab plot symbol


plotcolor
---------------------------------------

:code:`'blue'`

initial plotting color


markersize
---------------------------------------

:code:`float(5.0)`

Size of plotted marks


fontsize
---------------------------------------

:code:`float(10.0)`

Font size for labels


showgui
---------------------------------------

:code:`True`

Show plot on gui


figfile
---------------------------------------

:code:`''`

\'\'= no plot hardcopy, otherwise supply name




