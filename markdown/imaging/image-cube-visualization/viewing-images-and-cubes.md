

# Viewing Images and Cubes 

Details on viewing images and cubes

# Viewing Images

There are several options for viewing an image. These are seen at the right of the Load Data - Viewer panel described in [Initial Viewer Panels](#initial-viewer-panels) after selecting an image. They are:

-   raster image --- a greyscale or color image,
-   contour map --- contours of intensity as a line plot,
-   vector map --- vectors (as in polarization) as a line plot,
-   marker map --- a line plot with symbols to mark positions.

The raster image is the default image display, and is what you get if you invoke the viewer with an image file and no other options. In this case, you will need to use the Open menu to bring up the Load Data panel to choose a different display.

This page discusses raster images and contour maps in detail; for an example of how to use a vector map, see the 3C286 Polarization CASAguide [here](https://casaguides.nrao.edu/index.php/3C286_Band6Pol_Imaging_for_CASA_4.3).

## Initial Viewer Panels {#viewerRasterMap}

When the viewer is started, two dialogs appear. One is the Data Manager which presents two panels.

### Data Manager

The left panel shows the files that the viewer can load while the right panel shows some statistics about the file that is selected.

![e4b6e0a334c21c09b02abeac82d22632d050643f](media/e4b6e0a334c21c09b02abeac82d22632d050643f.jpg)

The other panel is the Viewer Display Panel.

### Viewer Display Panel

This panel is the main panel used to interact with the viewer. 

![1fa6b6a876aad22dcb6fc8c360d20fc4a67784ce](media/1fa6b6a876aad22dcb6fc8c360d20fc4a67784ce.jpg)

The image is shown on the left and image information is shown on the right. The Cursors panel displays information about the pixel at the current cursor location (as the cursor is moved around the image).

### Animators Panel

The Animators panel allows the planes on the image cube to be displayed. This can be done by either single-stepping plane by plane or playing the planes of the image cube like a movie. The buttons are: 

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><img src="markdown/_media/2c6505666e66f7864551526a4671489e0113c673.png" title="Anim0_ToStart.png" class="image-left" /><br />
<br />
</td><td>move to the first image plane</td></tr><tr class="even"><td><img src="markdown/_media/1664330a16c2db796b734e094af3ea123c7f28e0.png" title="Anim1_RevStep.png" class="image-left" /></td><td>move back one image plane</td></tr><tr class="odd"><td><img src="markdown/_media/031fffc236c0d843392d428addac247288f0e11f.png" title="Anim2_Rev.png" class="image-left" /></td><td>play image cube in reverse</td></tr><tr class="even"><td><img src="markdown/_media/b855a1ed3836bbd79eac65b341755ec44597e88d.png" title="Anim3_Stop.png" class="image-left" /></td><td>stop playing the movie</td></tr><tr class="odd"><td><img src="markdown/_media/9778c0eb8de97fd56c1d9be55c904c1f5cabc235.png" title="Anim4_Play.png" class="image-left" /></td><td>play image cube as a movie</td></tr><tr class="even"><td><img src="markdown/_media/41a79bc85908fd3d50836936c795b9577b4dd0b7.png" title="Anim5_FwdStep.png" class="image-left" /></td><td>move forward one image plane</td></tr><tr class="odd"><td><img src="markdown/_media/b0fa85965496a6f8fbfbc38fdec6046466f4bdc8.png" title="Anim6_ToEnd.png" class="image-left" /></td><td><p>move to the last image plane</p></td></tr></tbody></table>

In addition, to these controls for moving through the image cube, there are two other areas of animation control:

  ------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![85424f67f54248c57c56336ea81bd66cf6fda3ac](media/85424f67f54248c57c56336ea81bd66cf6fda3ac.jpg)   the rate indicates how how fast the movie should be played in terms of frames, and the second entry box (here with a zero) is for going to a particular plane of the image cube (enter a number and hit return) \[Jump doesn\'t seem to do anything\]
  ![9b03ad5ef24dbda549937b824a99bf4094af4343](media/9b03ad5ef24dbda549937b824a99bf4094af4343.jpg)   the slider of this control allows for moving through the image cube as the slider is moved. The dialogs at the ends of the slider allows for setting the start and end points for the movie (which can be less than or equal to zero and the number of planes in the cube)
  ------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Button Tools

These tools are designed for use with a three-button mouse. The row of boxes below the icon indicates which mouse button to which the tool is currently bound. For example, the last three icons in this table indicate that these tools are bound to the first, second, and third buttons respectively:

  ------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![ea7304b3410f36a9dccb3226349b77a36d11a998](media/ea7304b3410f36a9dccb3226349b77a36d11a998.png)          zoom: select this tool (by clicking on this icon and pressing one of the three buttons), then click and drag out a rectangle, then double click inside the rectangle to zoom in
  ![ec32ba3d365abd638f28eab5223ff43191f45c76](media/ec32ba3d365abd638f28eab5223ff43191f45c76.png)             panning: select this tool, then if the image is zoomed in, click and drag within the image to move the image
  ![ff0fc891b68739126b6757a6f2711f3e298bf37c](media/ff0fc891b68739126b6757a6f2711f3e298bf37c.png)       adjust color map: select this tool, then click and drag within the image to adjust the color map
  ![30ae0891708bab0f984a47332160c32eb5a19c74](media/30ae0891708bab0f984a47332160c32eb5a19c74.png)   contrast: select this tool, then click and drag within the image
  ![fcdf48b33278a7339b429ba55d5ca04bb3200639](media/fcdf48b33278a7339b429ba55d5ca04bb3200639.png)           point region: select this tool, then place a point on the image, the regions panel corresponding to the dot you placed will have statistics an information about the selected point
  ![9f482145a9d4db935ea3ab16d49ee44d1641700c](media/9f482145a9d4db935ea3ab16d49ee44d1641700c.png)       rectangular region: select this tool, then click and drag out a rectangle in the image and the regions panel corresponding to this region will have information about the rectangular region; double clicking in the region will display the statistics in to terminal window
  ![41ce877a9905c5c1496a99b09183e2095fcca245](media/41ce877a9905c5c1496a99b09183e2095fcca245.png)        eliptical region: select this tool, then click and drag out an ellipse, the regions panel corresponding to this region will have information about the eliptical region; double clicking in the region will display the statistics in the terminal window
  ![954637995892613204657cc0f5b51c865f12a077](media/954637995892613204657cc0f5b51c865f12a077.png)       polygon region: select this tool, then click multiple times within the image to mark out a region (one click at a time), double clicking when you have marked all of the points that denote the polygon, the regions panel corresponding to this region will have information about this region; double clicking in the region will display statistics for this region in the terminal window
  ![fdc2fd7995dbfd26ce5939da376bdbe40e2caac4](media/fdc2fd7995dbfd26ce5939da376bdbe40e2caac4.png)         polyline region: select this tool, then click multiple times within the image to mark out a multi-segment line, the region panel for this region will display statistics about the region
  ![731bad1ac19871bd8ce249ad527d8dd85589763e](media/731bad1ac19871bd8ce249ad527d8dd85589763e.png)            ruler: select this tool, click and drag in the image to get a display of distance along two axes
  ![c19dae88d0d5f8fc261291f1d0c2df6344b4a35e](media/c19dae88d0d5f8fc261291f1d0c2df6344b4a35e.png)           pv diagram: select this tool, click and drag within the image to create  a to be used to create a position/velocity diagram (the diagram is created from the region panel corresponding to the P/V line that you\'ve drawn)
  ------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

These tools create regions that can be used to provide information about a portion of an image.

### Regions

Regions are created with the region [Button Tools](#button-tools). For a region to be created, the Region panel (displayed on the left side of the Viewer Display Panel) must be open. If you do not see the Regions panel, it can be included in the Display Panel by selecting the Regions check box in the View menu:

![4a9aebf37ad6a0a09105e2438ffd0ba508e4734f](media/4a9aebf37ad6a0a09105e2438ffd0ba508e4734f.jpg)

Once the Regions dialog is in view Regions can be created and information about the regions can be viewed. For example, here one region (black rectangle) has been created and region statistics is displayed:

![f8acac9ee8c014d5338db58636ffffe4c8a181b0](media/f8acac9ee8c014d5338db58636ffffe4c8a181b0.jpg)

Note that in the statistics window, the brightness units are specified and the beam area is defined as the volume of the elliptical Gaussian $\frac{Π}{4ln(2)} * FWHM_{major} * FWHM_{minor}$, where ln() is the natural logarithm and $FWHM_{major}$ and $FWHM_{minor}$ are the major and minor FWHM axes of the beam, respectively. The flux density is the mean intensity multiplied by the number of beams included in the selected region.

### Region Statistics {#region-statistics style="text-align: center;"}

If more than one region has been created, the scroll bar can be used to move from the information about one region to the next or the cursor (in the image panel) can be used to move from one region to the next and the region information will be updated as the cursor moves from region to region. Here are three regions, showing histograms for the regions:

![cfc4f812ec08c5e86f6ffac0c67aabfc4c03d72a](media/cfc4f812ec08c5e86f6ffac0c67aabfc4c03d72a.jpg)

### Region Histogram {#region-histogram style="text-align: center;"}

The region which corresponds to the histogram that is shown has the corner adjustment cubes drawn.

Any regions that are created using these tools can be removed by moving the cursor over the region you would like to remove and once that region is highlighted press the escape key. Regions can also be deleted from the region panel that corresponds to the region you would like to remove.

## Viewing a Raster Map

A raster map of an image shows pixel intensities in a two-dimensional cross-section of gridded data with colors selected from a colormap according to a scaling that can be specified by the user. Starting the casaviewer with an image as a raster map will look something like the example in [Initial Viewer Panels](#initial-viewer-panels). Once loaded, the data display can be adjusted by the user through the Data Display Options panel, which appears when you choose the Data: Adjust Data Display menu or use the wrench icon from the Main Toolbar. The Data Display Options window is shown in the right panel of [Initial Viewer Panels](#initial-viewer-panels). It consists of a tab for each image or MS loaded, under which are a cascading series of expandable categories. For an image, these are:

-   display axes
-   hidden axes
-   basic settings
-   position tracking
-   axis labels
-   axis label properties
-   beam ellipse
-   color wedge

The basic settings category is expanded by default. To expand a category to show its options, click on it with the left mouse button.

 

### Data Display Options --- Display and Hidden Axes

In this category the physical axes (i.e. Right Ascension, Declination, Velocity, Stokes) to be displayed can be selected and assigned to the x, y, and z axes of the display. The z axis will be the axis scrolled across by the channel bar in the Animators Panel. If your image has a fourth axis (typically Stokes), then one of the axes will need to be hidden and not used in viewing. Which axis is hidden can be controlled by a slider within the hidden axes drop-down.

 

### Data Display Options --- Basic Settings

This roll-up is open by default showing some commonly-used parameters that alter the way the image is displayed. The most frequently used of these changes how the intensity value of a pixel maps to a color on the screen. An example of this part of the panel is shown in [Mapping Intensity to Color](#FigColorMapping).

------------------------------------------------------------------------

![d2baca80c73d185c1ca04583ccba36710108d3d5](media/d2baca80c73d185c1ca04583ccba36710108d3d5.png)

------------------------------------------------------------------------

<div>

The options available are:

</div>

-   basic settings: *aspect ratio*

    This option controls the horizontal-vertical size ratio of data pixels on screen. \"Fixed world\" (the default) means that the *aspect ratio* of the pixels is set according to the coordinate system of the image (i.e., true to the projected sky). \"Fixed lattice\" means that data pixels will always be square on the screen. Selecting \"flexible\" allows the map to stretch independently in each direction to fill as much of the display area as possible.

-   basic settings: *pixel treatment*

    This option controls the precise alignment of the edge of the current \"zoom window\" with the data lattice. \"Edge\" (the default) means that whole data pixels are always drawn, even on the edges of the display. For most purposes, \"edge\" is recommended. \"center\" means that data pixels on the edge of the display are drawn only from their centers inwards.

    <div class="alert alert-info">
    **NOTE**: A data pixel's center is considered its \"definitive\" position, and corresponds to a whole number in \"data pixel\" or \"lattice\" coordinates.
    </div>

-   basic settings: *resampling mode*

    This setting controls how the data are resampled to the resolution of the screen. \"Nearest\" (the default) means that screen pixels are colored according to the intensity of the nearest data point, so that each data pixel is shown in a single color. \"Bilinear\" applies a bilinear interpolation between data pixels to produce smoother looking images when data pixels are large on the screen. \"Bicubic\" applies an even higher-order (and somewhat slower) interpolation.

-   basic settings: *data range*

    You can use the entry box provided to set the minimum and maximum data values mapped to the available range of colors as a list \[min, max\]. For very high dynamic range images, you will probably want to enter a max less than the data maximum in order to see detail in lower brightness-level pixels.

    <div class="alert alert-info">
    **NOTE**: By default you edit the scaling of a single image at once and can click between the tabs at the top of the Data Display Options window to manipulate different windows. By checking the Global Color Settings box at the bottom of this window, you will manipulate the scaling for all images at once. This can be very useful, for example, when attempting a detailed comparison between multiple reductions of the same data.
    </div>

-   basic settings: *scaling power cycles*

    This option allows logarithmic scaling of data values to colormap cells, which can be very helpful in the case of very high dynamic range. The color for a data value is determined as follows:

    1.  The value is clipped to lie within the data range \[min, max\] specified above.
    2.  This clipped value is mapped to a new value depending on the selected scaling power cycles in the following way:
        -   If the scaling power cycles is set to 0 (the default), the program considers a linear range from \[min, max\] and scales this directly onto the set of available colors.
        -   For positive scaling values, the data value (after clipping on \[min, max\] is scaled linearly to lie between 0 and p (where p is the value chosen) and 10 is raised to this power, yielding a value in the range 1 to 10^p^. That value is scaled linearly to the set of available colors.
        -   For negative scaling values, the data value (after clipping on \[min, max\]) is scaled linearly to lie between 1 and 10^\|p\|^, where p is the power chosen. The base 10 logarithm is taken of this re-scaled data value, yielding a value in the range 0 to abs(p). That value is scaled linearly to the set of available colors. Thus the data is treated as if it had p decades of range, with an equal number of colors assigned to each decade.
    3.  The color corresponding to a number in final range is determined by the selected colormap and its \"fiddling\" (shift/slope) and brightness/contrast settings (see Mouse Toolbar, above). Adding a color wedge to your image can help clarify the effect of the various color controls.

    See [Scaling Power Cycles](#FigScalingPowerCycles) for sample curves.

------------------------------------------------------------------------

![71082fec54dd80acd580c40814ca9ad304ba7097](media/71082fec54dd80acd580c40814ca9ad304ba7097.png)

------------------------------------------------------------------------

In practice, you will often manipulate the data range bringing the max down in high dynamic range images, raising the minimum to the near the noise level when using non-zero scaling cycles. It is also common to use negative power cycles when considering high dynamic range images --- this lets you bring out the faint features around the bright peaks.

-   basic settings: *colormap*

    You can select from a variety of colormaps here. Hot Metal, Rainbow and Greyscale colormaps are the ones most commonly used.

 

### Graphical Specification of the Intensity Scale

A histogram icon next to the Data Range entry in the Data Display Options window opens the Image Color Mapping window, which allows visualization and graphical manipulation of the mapping of intensity to color. The window at the left shows a histogram of the data with a gray range showing the data range. You can use this window to select the data range graphically (with the mouse), manually (by typing into the Min and Max entry windows), or as a percentile of the data. On the right, you can select the scaling power cycles and see a visualization of the transfer function mapping intensity (x-axis) to color (y-axis).

The functionality here follows the other histogram tools, with the Display tab used to change the histogram plotting parameters. It will often be useful to use a logarithmic scaling of the y-axis and filled histograms when manipulating the color table.

 

### Data Display Options --- Other Settings

Many of the other settings on the Data Display Options panel for raster images are self-explanatory such as those which affect beam ellipse drawing (only available if your image provides beam data), or the form of the axis labeling and position tracking information. You can also give your image a color wedge, a key to the current mapping from data values to colors.

 

### Viewer Canvas Manager --- Panels, Margins, and Backgrounds

------------------------------------------------------------------------

![bdbf6ab7cf4f4553813d0b9ef67c336d6ca7956d](media/bdbf6ab7cf4f4553813d0b9ef67c336d6ca7956d.png)

------------------------------------------------------------------------

 The display area can also be manipulated from the Viewer Canvas Manager window. Use the wrench icon with a \"P\" (or the \"Display Panel\" menu) to show this window, which allows you to manipulate the infrastructure of the main display panel. You can set:

-   Margins - specify the spacing for the left, right, top, and bottom margins
-   Number of panels - specify the number of panels in x and y and the spacing between those panels.
-   Background Color - white or black (more choices to come)

[Multi-Panel Display](#FigMultiPanel) illustrates a multi-panel display along with the Viewer Canvas Manager settings which created it.

<div>

 
## Viewing a Contour Map

Viewing a contour image is similar to viewing a raster map. A contour map shows lines of equal data value for the selected plane of gridded data (see [Viewing a Contour Map](#FigContourView)). Contour maps are particularly useful for overlaying on raster images so that two different measurements of the same part of the sky can be shown simultaneously (see [Overlay Contours on a Raster Map](#viewerContourOverlay)).

Several basic settings options control the contour levels used:

-   The contours themselves are specified by a list in the box *Relative Contour Levels*. These are defined relative to the two other parameters:
-   The *Base Contour Level* sets the zero level for the relative contour list corresponds to in units of intensity in the image.
-   The *Unit Contour Level* sets what 1 in the relative contour list corresponds to in units of intensity in the image.

Additionally, you have the option to manipulate the thickness and color of the image and to have either positive or negative contours appear dashed.

------------------------------------------------------------------------

![65b29709d5005d1f999a3482263d05da8effaea4](media/65b29709d5005d1f999a3482263d05da8effaea4.png)

------------------------------------------------------------------------

For example, the following settings:

       Relative Contour Levels = [0.2, 0.4, 0.6, 0.8]
       Base Contour Level = 0.0
       Unit Contour Level = <image max>

would map the maximum of the image to 1 in the relative contour levels and the base contour level to zero. So the contours will show 20%, 40%, 60%, and 80% of the peak.

Another approach is to set the unit contour to 1, so that the contours are given in intensity units (usually Jy/beam). So this setup:

       Relative Contour Levels = [0.010, 0.0.020, 0.040, 0.080, 0.160, 0.320]
       Base Contour Level = 0.0
       Unit Contour Level = 1.0

would create contours starting at 10 mJy/beam and doubling every contour.

Another useful approach is to set contours in units of the rms noise level of the image, which can be worked out from a signal free region. Then a setup like this:

       Relative Contour Levels = [-3,3,5,10,15,20]
       Base Contour Level = 0.0
       Unit Contour Level = <image rms>

Would indicate significance of the features in the image. The first two contours show emission at ± 3-sigma and so on. You can get the image rms using the [imstat task](https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_imstat) or using the [Region Statistics](#region-statistics) on a region of the image .

Not all images are of intensity, for example a moment-1 image ([immoments task](https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_immoments)) has units of velocity. In this case, absolute contours (like the last two examples) will work fine, but by default the viewer will set fractional contours but refer to the min and max of the image:

       Relative Contour Levels = [0.2, 0.4, 0.6, 0.8]
       Base Contour Level = <image min>
       Unit Contour Level = <image max>

Here we have contours spaced evenly from min to max, and this is what you get by default if you load a non-intensity image (like the moment-1 image). See [Overlaying a Contour Map](#FigContourOverlay) for an example of this.

 

### Overlay Contours on a Raster Map

Contours of either a second data set or the same data set can be used for comparison or to enhance visualization of the data. The Data Display Options Panel will have multiple tabs (switch between them at the top of the window) that allow you to adjust each overlay individually.

<div class="alert alert-info">
**NOTE**: Axis labeling is controlled by the first-registered image overlay that has labeling turned on (whether raster or contour), so make label adjustments within that tab.
</div>

To add a Contour overlay, open the Load Data panel (Use the Data menu or click on the folder icon), select the data set and click on contour map. See [Overlaying a Contour Map](#FigContourOverlay) for an example using NGC5921.

------------------------------------------------------------------------

![f37c9cebb709797c6c3f7326d397cc7d38cb3038](media/f37c9cebb709797c6c3f7326d397cc7d38cb3038.png)

 

### Creating a Position/Velocity Diagram

With an image cube loaded, it is possible to create a position/velocity diagram using the P/V Button Tool (see [Initial Viewer Panels](#initial-viewer-panels)). The first step in creating a P/V diagram is to select the tool with the mouse button to which you would like to bind the tool:

![e33db1e64044bac99a712e5e56c84163c63b8a7c](media/e33db1e64044bac99a712e5e56c84163c63b8a7c.jpg)

Here we have bound the P/V button tool to the first mouse button. At this point, we can drag out a P/V line, by clicking and dragging on the image:

![258d6b45ebcda4acc8293fb0be9714b062e5cb6d](media/258d6b45ebcda4acc8293fb0be9714b062e5cb6d.jpg)

 

After creating the P/V line, it will appear with two circles on each end. These circles can be used to adjust the line by clicking within the circle and dragging:

![0b9e0d612e604fad380a7cc40a443547806e1d81](media/0b9e0d612e604fad380a7cc40a443547806e1d81.jpg)

After the P/V line is properly in place, the final P/V diagram can be created from the P/V Regions panel. It is just a matter of generating the P/V diagram with the Generate P/V button:

![13f7ffec391f0f9340b6d1feb8b1c7889a12e69e](media/13f7ffec391f0f9340b6d1feb8b1c7889a12e69e.jpg)

The generation of the P/V diagram may take some time, but then the final diagram is displayed:

![a66c61bd7ca3a4de494cacda916c4075803c6fa7](media/a66c61bd7ca3a4de494cacda916c4075803c6fa7.jpg)

 

 

 

 

 

 

 

 

</div>

