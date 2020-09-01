

# Plot Antenna Positions 

Plotting antenna positions

This task is a simple plotting interface to produce plots of the antenna positions (taken from the ANTENNA sub-table of the MS). The location of the antennas in the MS will be plotted with X-toward local east, Y-toward local north.

The inputs to **plotants** are:

```
 # plotants :: Plot the antenna distribution in the local reference frame:
vis              =   ''       # Name of input visibility file (MS)
figfile          =   ''       # Save the plotted figure to this file
antindex         =   False    # Label antennas with name and antenna ID
logpos           =   False    # Whether to plot logarithmic positions
exclude          =   ''       # Antenna name/id selection to exclude from plot
checkbaselines   =   False    # Whether to check baselines in the main table.
title            =   ''       # Title for the plot.
showgui          =   True     # Show plot on gui.

```

For most telescopes, the default X/Y plot is in meters.  For VLBA antenna plots, latitude vs. longitude (degrees) is plotted instead.

Supported format extensions for the *figfile* include emf, eps, pdf, png, ps, raw, rgba, svg, and svgz, depending on which python modules are installed on your system. Formats currently available in a downloaded CASA package include all but emf (enhanced metafile).

Each antenna position is labeled with the antenna name. VLBA antenna plots label the positions with \"name @ station\" format, e.g. \"2\@FD\" for the Fort Davis, Texas, antenna. To add the antenna ID to the name, set *antindex=True* as shown in Figure 1.

![0913b01badcfd68e003cece8d0ff8c658c936262](media/0913b01badcfd68e003cece8d0ff8c658c936262.png)

>ALMA antenna positions with *antindex=True*.
  

By default, **plotants** plots the positions of all antennas in the ANTENNA subtable. However, the user has the option to exclude certain antennas with the *exclude* parameter. Its value is a string to select which antennas to exclude, using the same syntax as the antenna parameter in [MeasurementSet selection](https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset). For example, *exclude=\"5\~6\"* would exclude the PM antennas from the plot in Figure 1.

To plot only those antennas which appear in the MAIN table (e.g. after a split, which retains the entire ANTENNA subtable in the dataset), set *checkbaselines=True*. This parameter would have automatically removed antenna 7 (DV10) from the plot in Figure 1, as it does not appear in the main table of this dataset.

To plot logarithmic positions instead of X/Y positions, set *logpos=True* as shown in Figure 2:

![5933a270bc2321a65052a7f5b39f6e0e8b0879d5](media/5933a270bc2321a65052a7f5b39f6e0e8b0879d5.png)

>Antenna positions with *logpos=True*
  

The default title for the plot is \"Antenna Positions for \" the MS name (*vis* argument), as shown in all figures on this page. To set a custom title, set the *title* parameter to the desired string.

# The plotants GUI

By default, the plotants GUI will be shown when the task is used.  If the GUI is not needed, as in scripting mode to produce a *figfile*, set *showgui=False*. When casa flags are set to avoid starting GUI tools or to run without the matplotlib \'tkagg\' backend (*\--nogui, \--pipeline,* or *\--agg*), the plotants GUI will not be shown regardless of the value of the *showgui* parameter.

The antennas will be plotted in a plotter window as shown below. Several tool buttons are available to manipulate and save the plot:

-   The \'Home\' button (leftmost house icon) is used to return to the first, default view after panning or zooming.
-   The \'Forward\' and \'Back\' buttons (left- and right-arrow icons) are used to navigate between previous plot views after pan/zoom actions.
-   The \'Pan/Zoom\' button (crossed blue arrows, fourth icon) is used to drag the plot to a new position by pressing and holding the mouse button.
-   The \'Zoom-to-rectangle\' button (magnifier icon, fifth from left) is used to mark a rectangular region with the mouse in order to zoom in on the plot.
-   The \'Subplot-configuration\' button (sixth icon) can be used to stretch or compress the left, right, top, or bottom of the plot, as well as the ability to reset the plot to the original shape after manipulation before exiting the configuration dialog.
-   The \'Save\' button (rightmost icon) is used to export the plot. A file save dialog is launched to select a location, name, and format (default png) for the file.

![f05dc15d6cf9628b4e2f819d7e5530c7f27d3bd2](media/f05dc15d6cf9628b4e2f819d7e5530c7f27d3bd2.png)

>**plotants** GUI for a VLA dataset with *antindex=True*. Note the tool buttons at the bottom of the window.
  

