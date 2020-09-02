

# Spectral Profiler 

Using the Spectral Profile GUI in the Viewer

 

## The Spectral Profile Tool

 

------------------------------------------------------------------------

![f460a73178b5a78ab57f1664858a899137979ef2](media/f460a73178b5a78ab57f1664858a899137979ef2.png){.image-inline}

------------------------------------------------------------------------

<div>

<div class="alert alert-info">
**NOTE**: Make Sure That You Use the Radio Version! This section describes the 'Radio' version of the profiler. To be sure that you have the radio version of the tool selected (this may not be the default), click on the preferences icon (the 'gear' fourth from the left in the Spectral Profile tool) and make sure that the 'Optical' option is not checked. If you are using the Spectral Profile tool in the viewer for the very first time, you will also be prompted for a selection that will subsequently be kept for all future calls unless the preference is changed.
</div>

The Spectral Profile Tool consists of the [Spectral Profile Toolbar](#viewerSpectralProfileToolbar), a [main display area](#viewerSpectralProfile), and two associated tabs: [Spectral-Line Fitting](#viewerSpectralLineFitting) and [Line Overlays](#viewerLineOverlays).

Interaction With the Main Display Panel: For the Spectral Profile tool to work, a region or point must be specified in the main Viewer Display window. Use the mouse tools to specify a point, rectangle, ellipse, or polygon region. Alternatively, load a region file. The Spectral Profile tool will show a spectrum extracted from the region most recently highlight by the mouse in the main Viewer Display Panel. The method of extraction (i.e. mean, median, sum, or flux density) can be specified by the user using a drop down menu below the spectrum in the Spectral Profile window; the method of extraction is mean by default.

The Spectral Profile tool can also feed back to the Main Display Panel. By holding CTRL and right clicking in the spectrum, you will cause the Main Display Panel to jump to display the frequency channel corresponding to the spectral (x) coordinate of the region highlighted in the Spectral Profile tool. Holding CTRL and dragging out a spectral range while holding the right mouse button will queue a movie scrolling through images across that spectral range. You can achieve the same effect with the two-ended-arrow icon towards the right of the toolbar in the Spectral Profile window.

In both the [Spectral-Line Fitting](#viewerSpectralLineFitting) and [Line Overlays](#viewerLineOverlays) tabs, it may be useful to select a range in frequency or velocity. You can do this with the parallel lines-and-arrow icon (see below) or by holding shift, left clicking, and dragging out the range of interest. A shaded gray region should appear indicating your selection.

 

### Spectral Profile Toolbar

------------------------------------------------------------------------

![b70f90030cd7ed87f57699da695279ded944c906](media/b70f90030cd7ed87f57699da695279ded944c906.png)

<div>

>Spectral Profile Toolbar: The toolbar for the Spectral Profile tool allows the user to save the spectrum, print or save the tool as an image, edit preferences (general, tool, legend), apply spectral smoothing, pan or zoom around the spectrum, select a range of interest, jump to a channel, or add a label.
  

The [Spectral Profile Toolbar](#FigSpectralToolbar) is the toolbar along the top of the Spectral Profile window. From left to right, the icons allow the user to:

-   (disk) export the current profile to a FITS or ASCII file
-   (printer) print the main window to a hard copy
-   (writing desk) save the panel as an image (PNG, JPG, PDF, etc.)
-   (gear) set plot preferences
-   (color wheel) set color preferences for the plot
-   (signpost) set legend preferences
-   (triangle) set the spectral smoothing method and kernel width
-   (arrows) pan the spectrum in the indicated direction NOTE: The arrow keys also allow one to pan using the keyboard.
-   (magnifying glass) zoom to the default zoom, in, and out NOTE: the +/- keys allow one to zoom with the keyboard
-   (parallel lines+arrows) drag out a range of interest in the spectrum, for use with fitting or line overlays.
-   (double-ended arrow) jump to a channel in the main viewer (single click) or define a range over which to play a movie in the viewer (with a drag).
    <div class="alert alert-info">
    **NOTE**: You can also jump to a channel with CTRL+Right Click and queue a movie by holding CTRL and dragging out a range while holding the right mouse button.
    </div>
-   (notepad and pencil) Add or edit a label on the plot. Click this icon to enter a mode where you can drag out a box to create a new annotation box or drag the corners of an existing one to resize it. You can edit the contents, color, and font of an existing annotation by right clicking on it and selecting \"Edit Annotation\" in the main Spectral Profile window.

------------------------------------------------------------------------

![3298dfa9eac7bb5c2b721bf9ea8613f647cb6b4c](media/3298dfa9eac7bb5c2b721bf9ea8613f647cb6b4c.png)

------------------------------------------------------------------------

<div>

[Spectral Profile Tool Preferences](#FigSpectralProfilePreferences) shows the setting dialogs accessible from the toolbar. This Preferences dialog opened by the \'gear\' icon allows the user to:

</div>

<div>

-   Toggle automatic scaling the x- and y-ranges of the plot.
-   Toggle the coordinate grid overlay in the background of the plot.
-   Toggle whether registered images other than the current one appear as overlays on the plot.
-   Toggle whether these profiles are plotted relative to the main profile (in development).
-   Toggle the display of tooltips (in development).
-   Toggle the plotting of a top axis.
-   Toggle between a histogram and simple line 

------------------------------------------------------------------------

![b3606599a0ccbeb166c8d7fc12e6fd80a8c7a3ed](media/b3606599a0ccbeb166c8d7fc12e6fd80a8c7a3ed.png)

------------------------------------------------------------------------

The main window shows the spectrum extracted from the active region of the image in the main Display Panel. The spectra from the same region in any other registered images are also plotted if overlays are enabled. Menus along the bottom of the image allow the user to select how the spectrum is displayed. From left to right:

-   The units for the bottom spectral axis.
-   The units for the top spectral axis.
    <div class="alert alert-info">
    **NOTE**: Dual axes are enabled only if a single image is registered and the top axis option is enabled. In general, dual axes are not well-defined for mixed data sets. The exception is that open data cubes with matched frequency/spectral axes will allow dual axes.
    </div>
-   The units for the left intensity or flux axis
    <div class="alert alert-info">
    **NOTE**: The "Fraction of Peak" option allows for easy comparison of data with disparate intensity scales.
    </div>
-   The velocity reference frame used if a velocity axis is chosen for the top or bottom axis.
-   The method used to extract spectrum from the region --- a mean over all pixels in the region, a median, sum, or a sum converting units to get a flux density over the region (Jy).
-   Toggle the calculation and overplotting of error bars calculated from scatter in the data (rmse refers to root mean square error).

In addition to these drop-down menus, the main Spectral Profile window allows the user to do the following using keyboard and mouse inputs:

-   jump the main Display Panel window to a specified channel (CTRL+Right click): hold CTRL and right click in the spectrum. A marker will appear and the main Viewer Display Panel will jump to display that channel.
-   animate the main Display Panel in a movie across a frequency range (CTRL+Right click+drag): hold CTRL, Right click, and drag. The main Viewer Display panel will respond by showing a movie scrolling across the selected spectral channels.
-   zoom the Spectral Profile (+/-, mouse drag): Use the +/- keys to zoom in the same way as the toolbar buttons. Alternatively, press and drag the left mouse button. A yellow box is drawn onto the panel. After releasing the mouse button, the plot will zoom to the selected range.
-   pan the Spectral Profile (arrows): Use the arrow keys to pan the plot.
-   select a spectral range for analysis: hold shift, left click, and drag. A gray area will be swept out in the display. This method can be used to select a range for spectral line fitting or collapsing a data cube (in the Collapse/Moments window).

**NOTE**: If the mouse input to the Spectral Profile browser becomes confused hit the ESC key several times and it will reset.

 

### Spectral-Line Fitting {#spectral-line-fitting 

------------------------------------------------------------------------

![c29793490bd0d5d69c32f5485bc256ff586fd2ab](media/c29793490bd0d5d69c32f5485bc256ff586fd2ab.png)

>Spectral Line Fitting Tab: Using the Spectral Line Fitting Tab (found at the bottom left of the Spectral Profile Tool), the user can fit a combination of a polynomial and multiple Gaussian components. The range to be fit can be specified (gray region) manually or with a shift+click+drag. Initial estimates for each component may be entered by hand or specified via an initial estimates GUI. The results are output to a dialog and text file with the fit overplotted (here in blue) on the spectrum (with the possibility to save it to disk).
  

------------------------------------------------------------------------

![c648346d0ff0181b8a8984116c5357abdaed3bdf](media/c648346d0ff0181b8a8984116c5357abdaed3bdf.png)

>Specifying Initial Gaussian Estimates Graphically and Fitting Output: The top panel shows the graphical specification of initial estimates for Gaussian fitting. Slider bars specify the center, FWHM, and peak intensity for the initial estimate. The bottom panel shows the verbose output of the fitting.
  

The Spectral-Line Fitting tab, shown in [Spectral Line Fitting Tab](#FigSpectralLineFitting) and [Specifying Initial Gaussian Estimates Graphically and Fitting Output](#FigInitialGaussEstimates), allows the user to interactively fit a combination of Gaussian and polynomial profiles to the data shown in the Spectral Line Profile tool. The tool includes a number of options:

-   A drag-down menu labeled \"Curve\" at the top of the panel allows the user to pick which data set to fit.
-   The spectral range to fit can be specified by either holding shift+left click+dragging out a region in the main spectral profile window or by typing it manually into the boxes labeled Min and Max near the top left of the fitting panel.
-   Optionally multiple fits can be carried out once, fitting each spectrum in the region in turn. To enable this, check the \'MultiFit\' box.
-   Optionally a polynomial of the specified order may be fit. To do so, check the \'Polynomial\' fit check box and then specify the desired order.
-   The results may be saved to a text file. This text file should be specified before the fit is carried out. Click \'Save\' and then use the dialog to specify the file name. Note that the fit curve itself becomes a normal spectral profile data set and can be saved to disk using the toolbar (\'disk\' icon) after the fit.
-   One or more Gaussians can be fit, although results are presently most stable for one Gaussian. Specify the number of Gaussians in the box marked \"Gaussian Count\" and then enter initial estimates for the peak, center, and FWHM in the table below. Any of these values can be fixed for any of the Gaussians being fit. Initial estimates can also be manually specified by clicking \"Estimates\". This brings up an additional GUI window (see [Specifying Initial Gaussian Estimates Graphically](#FigInitialGaussEstimates)), where sliders can be used to specify initial estimates for each Gaussian to be fit.
-   For plotting purposes, one may wish to oversample the fit (i.e., plot a smooth Gaussian), you can do so by increasing the Fit Samples/Channel to a high number to finely sample the fit when plotting.

**NOTE**: Currently the tool works well for specifying a single Gaussian. Fitting multiple Gaussian components can become unstable.

 

### Line Overlays {#line-overlays 

------------------------------------------------------------------------

![4d513d4c6000fd2ea90d88b9a7b01d057d90114f](media/4d513d4c6000fd2ea90d88b9a7b01d057d90114f.png)

>Line Overlays Tab: The Line Overlay tab (found at the bottom left of the Spectral Profile Tool) allows users to query the CASA copy of the Splatalogue spectral line database. Enter the redshift of your source (far right of the panel), select an Astronomical Filter from the drop down menu, and use shift+click+drag to select a frequency range (or enter the range manually in the boxes marked Min and Max). The \"Search\" button will bring up a separate \"Search Results\" window, which can in turn be used to graph the candidate lines in the main Spectral Profile window (here CO v=0).
  

Each version of CASA includes a local version of the [Splatalogue](http://www.splatalogue.net) spectral line database and this can be used to identify and overplot spectral transitions. This feature, shown in [Line Overlay Tab](#FigLineOverlayTab), allows the user to search Splatalogue over the range of interest.

To overlay spectral lines:

1.  Select the Line Overlays tab in the Spectral Profiles tab.
2.  If you know it, enter the redshift or velocity of your source in the \"Doppler Shift\" panel. Otherwise, the lines will be overlaid assuming a redshift of 0.
3.  Specify a minimum and maximum frequency range to search, either by typing a range or by holding shift and left click and dragging out a range in the spectrum (you will see a gray box appear). If you don't specify a range, the tool will search over the frequency range of spectrum.
4.  Optionally, you may select an astronomical filter from the list (e.g., commonly used extragalactic lines or lines often found in hot cores, see [Splatalogue](http://www.splatalogue.net) for more information). This is usually a good idea because it pares the potentially very large list of candidate lines to a smaller set of reasonable candidates.
5.  Click \'Search\' and the Spectral Profile will search Splatalogue for a list of Spectral lines that fit the selected Astronomical Filter in the selected frequency range for the selected redshift. A \"Molecular Line Search Results\" dialog box will pop up showing the list of candidate lines.
6.  Highlight one or more of these transitions and click \'Graph Selected Lines\'. A set of vertical markers will appear in the main Spectral Profile window at the appropriate (redshifted) frequencies for the line.

NOTE: You will want to click \'Clear Lines\' between searches, especially if you update the redshift.

 

## The Collapse/Moments Tool {#the-collapsemoments-tool 

 

------------------------------------------------------------------------

![df2fa469ffe23c7fb70cba20c7821a5dfd3da869](media/df2fa469ffe23c7fb70cba20c7821a5dfd3da869.png)

------------------------------------------------------------------------

The CASA Viewer can collapse a data cube into an image, for instance allowing to look at the emission integrated along the z axis or the mean velocity of emission along the line of sight. You can access this functionality via the Collapse/Moments tool (accessed via the Tools drop down menu in the Main Display planel or via the four inward pointing arrows icon in the Main Toolbar) which is shown in [Collapse/Moments Tool](#FigMomentsTool).

The tool uses the same format as the Spectral Profile tool and will show the integrated spectrum of whatever region or point is currently selected in the Main Display Panel. To create a moment map:

1.  Select a range over which to integrate either manually using the left part of the window, by adding an interval and typing in the values into the boxes marked Min and Max or by holding SHIFT + Left Click and dragging out the range of interest.
2.  Pick the set of algorithms (listed in the box labeled \"Moment(s)\") that you will use to collapse the image along the z-axis. Clicking an option toggles that moment method, and the collapse will create a new image for each selected moment. For details on the individual collapse method, see the [immoments](https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_immoments) task for more details on each moment.
3.  The moment may optionally include or exclude pixels within a certain range (for example, you might include only values with signal-to-noise of three or greater when calculating the velocity dispersion). You can enter the values to include or exclude manually in the Thresholding window on the right or you can open a histogram tool to specify this range graphically by clicking Specify Graphically (before this can work, you must click \'Include\' or \'Exclude\').
4.  The results of the collapse can be saved to a file, which consists of a string specifying the specific moment tacked onto a root file name that you can specify using Select Root Output File.
5.  When you are satisfied with your chosen options, press \'Collapse\'.

**NOTE**: Even if you don't save the results of the collapse to a file, you can still save the map later using the Save as\... entry in the Data pull down menu from the Main Viewer Display Panel.

## Interactive Position-Velocity Diagram Creation {#interactive-position-velocity-diagram-creation 

 

------------------------------------------------------------------------

![54c3e56ee2d8faacb841aa44931c419e06cf357e](media/54c3e56ee2d8faacb841aa44931c419e06cf357e.png)

------------------------------------------------------------------------

The route to create position-velocity cuts in the viewer is illustrated in [Position/Velocity Tool](#FigPVCutTool):

1.  Select the \'P/V cut\' tool from the Mouse Toolbar and use it to draw a line across a data cube along the axis you want to visualize.
2.  Open the Region Manager Panel and go to the pV tab. Highlight the cut you just drew. You should see the end point coordinates listed, along with information on the length and position angle of the cut. You can set the averaging width (in pixels) in a window at the bottom of the tab.
3.  When you are satisfied, hit \'Generate P/V\'. This will create a new Main Viewer Display Panel showing the position velocity cut. The axes should be Offset and velocity.

The new image can be saved to disk with the Data:Save as\... option.

</div>

</div>

