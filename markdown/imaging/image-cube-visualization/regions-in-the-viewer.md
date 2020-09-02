

# Regions in the Viewer 

Using CASA CRTF Regions in the Viewer

 

## Regions and the Region Manager

 

------------------------------------------------------------------------

![b0a36b1085af0c104e3d638b0a2d23ee2a5b74d9](media/b0a36b1085af0c104e3d638b0a2d23ee2a5b74d9.png){.image-inline}

------------------------------------------------------------------------

CASA regions are following the CASA \'crtf\' standard as described in § [D](https://casa.nrao.edu/docs/cookbook/casa_cookbook015.html#chapter%3Aregionformat). CASA regions can be used in all applications, including **tclean** and [Image Analysis Tasks](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis).

<div class="alert alert-info">
**NOTE:** The CASA image analysis tasks will determine how a region is projected on a pixel image. The current CASA definition is that when the center of a pixel is inside the region, the full pixel is considered to be included in the region.  If the center of the pixel is outside the region, the full pixel will be excluded. Note that the CASA viewer behavior is not entirely consistent and for rectangles it assumes that *any* fractional pixel coverage will include the entire pixel. For other supported shapes (ellipses and polygons), however, ithe viewer adheres to the 'center of pixel' definition, consistent with the image analysis tools and tasks. 

For purely single-pixel work regions may not necessarily be the best choice and alternate methods may be preferable to using regions, eg. **ia.topixel**, **ia.toworld**, **ia.pixelvalue**.
</div>

<div class="alert alert-warning">
**ALERT:** Some region file specifications are not recognized by the viewer, the viewer only supports rectangles (box), ellipses, and polygons.
</div>

<div class="alert alert-info">
**NOTE**: A leading 'ann' (short for annotation) to a region definition indicates that it is for visual overlay purposes only.
</div>

<div class="alert alert-info">
**NOTE**: Whereas the region format is supported by all the data processing tasks, some aspects of the viewer implementation are still limited to rectangles, ellipses, and some markers. Full support for all region types is progressing with each CASA release.
</div>

Once one or more regions are created, the Region Manager Panel becomes active (see [Region Manager](#FigRegionManager)). Like the Position Tracking and Animator Panels, this can be docked or detached from the main viewer display. It contains several tabs that can be used to adjust, analyze, and save or load regions.

<div class="alert alert-info">
**NOTE**: Moving the mouse into a region will bring it into focus for the Spectral Profile or Histogram tools.
</div>

 

### Region Creation, Selection, and Deletion

Within the display area, you can draw regions or select positions using the mouse. Regions can be created with the buttons marked as \'R\' in the mouse tool bar, which can be found on the top-left (second row of buttons) in the [Viewer Display Panel](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/viewer-basics). The viewer currently supports creation of rectangles, ellipses, polygons, and the point. As usual, a mouse button can be assigned to each button as indicated by the small black square in each button (marking the left, middle, or right mouse button). An example is shown in [Region Selection](#FigRegionSelection).

Regions can be selected by SHIFT+click, de-selected by pressing SHIFT+click again. The bottom of the Region Manager Panel features a slider to switch between regions in the image. Regions can be removed by hovering over and pressing ESC or by pressing the buttons to the right side of the slider where the first button (trash can icon) deletes all regions and the far right button (red circle with a white X) deletes the region that is currently displayed in the panel.

------------------------------------------------------------------------

![9978959045808465057ed10e8fa21f4bbfeb7aa5](media/9978959045808465057ed10e8fa21f4bbfeb7aa5.png){.image-inline}

------------------------------------------------------------------------

Once regions are selected, they will feature little, skeletal squares in the corners of their boundary boxes. Selected regions can be moved by dragging with the mouse button and manually resized by grabbing the corners as handles. If more than one region is selected, all selected regions move together.

The Rectangle Region drawing tool currently enables the full functionality of the various Region Manager tabs (see below) as well as:

-   Region statistics reporting for images via double clicking (also shown in the Statistics tab of the Region Manager),
-   Defining a region to be averaged for the spectral profile tool (accessed via the Tools:Spectral Profile drop down menu or \"Open the Spectrum Profiler\" icon),
-   Flagging of MeasurementSets. Note that the Rectangle Region tool's mouse button must also be double-clicked to confirm an MS flagging edit.
-   Selecting Clean regions interactively (§ [5.3.5](https://casa.nrao.edu/docs/cookbook/casa_cookbook006.html#section%3Aim.clean.interactive))

The Polygon Region and Ellipse Region drawing have the same uses, except that polygon region flagging of a MeasurementSet is not supported.

 

### Region Positioning

------------------------------------------------------------------------

![f9d2972c79da5e3b12e60dc426b81baace780aae](media/f9d2972c79da5e3b12e60dc426b81baace780aae.png){.image-inline}

------------------------------------------------------------------------

The File tab in the Region Manager allows one to save or load selected regions, either individually or en masse. You can choose between CASA and DS9 region format. The default is a CASA region file (saved with a \'.crtf\' suffix, see § [D](https://casa.nrao.edu/docs/cookbook/casa_cookbook015.html#chapter%3Aregionformat)). The DS9 format does not offer the full flexibility and cannot capture Stokes and spectral axes. DS9 regions will only be usable as annotations in the viewer, they cannot be used for data processing in other CASA tasks. When saving regions, one can choose to save only the current region, all regions that were selected with SHIFT+click, or all regions that are visible on the screen.

<div class="alert alert-info">
**NOTE**: The load functionality for this tab will only become available once at least one region exists. To load a region when no regions exist, use the [Region Manager](#viewerData) window.
</div>

 

 

### The Region Fit

The Viewer can attempt to fit a two-dimensional Gaussian to the emission distribution inside the currently selected region. To attempt the fit, go to the Fit tab of the Region Manager and click the \'gaussfit\' button in the bottom left of the panel. You can choose whether or not to fit a sky level (e.g., to account for a finite background, either astronomical, sky, or instrumental). After fitting the distribution, the Fit panel shows the results of the fit, the center, major and minor axis, and position angle of the Gaussian fit in pixels (I) and in world coordinates (W, RA and Dec). The detailed results of the fit will also appear in the terminal window, including a flag showing whether the fit converged.

 

### The Region Histogram

------------------------------------------------------------------------

![71a8870c7e27d8e4226ab388d473c1f3cba13373](media/71a8870c7e27d8e4226ab388d473c1f3cba13373.png){.image-inline}

<div>

<table class="caption-table"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="text-align: left;">Type</td><td>Figure </td></tr><tr class="even"><td style="text-align: left;">ID</td><td>Histogram</td></tr><tr class="odd"><td style="text-align: left;">Caption</td><td>Histogram Tab: The histogram tab in the Region Manager. Right click to zoom. Hit SHIFT + Right Click to adjust the details of the histogram display.<div> </div></td></tr></tbody></table>

The viewer will automatically derive a histogram of the pixel values inside the selected region. This can be viewed using the Histogram tab of the of the Region Manager Panel. This is a pared down version of the full Histogram Tool. You can manipulate the details of the histogram plot by:

1.  Using the Right Click to zoom - either to the full range, a selected percentile, or a range that you have graphically selected by dragging the mouse.
2.  Hitting SHIFT + Right Click to open the histogram options. This lets you toggle between a logarithmic and linear y-axis, choose between a line, outline, or filled histogram, and adjust the number of bins.

The histogram will update as you change the plane of the cube or shift between regions.

</div>

