

# Viewer Basics 

An introduction to basic viewer features

# Starting the Viewer

------------------------------------------------------------------------

![08fb3afec0b21c1c8afa30e15b80617972df1d4f](media/08fb3afec0b21c1c8afa30e15b80617972df1d4f.png)

>Initial Viewer Panels: The Viewer Display Panel (left) and the Data Manager Panel (right) for a regular image or data cube.
  

------------------------------------------------------------------------

Within the CASA environment, the viewer task can be used to start the CASA Viewer, displaying an image or MS. The inputs are:

```
#  viewer :: View an image or visibility data set.

infile        =         ''   #   (Optional)  Name of file to visualize.
displaytype   =   'raster'   #   (Optional)  Type of visual rendering
                             #   (raster, contour, vector or marker).
                             #   lel  if an lel expression is given
                             #   for infile (advanced).
```

Examples of starting the CASA Viewer:

```
CASA <1>: viewer()

CASA <2>: viewer('ngc5921.demo.ms')

CASA <3>: viewer('ngc5921.demo.cleanimg.image')

CASA <4>: viewer('ngc5921.demo.cleanimg.image', 'contour')
 
CASA <5>: viewer('"ngc5921.demo.cleanimg.image"^2', 'lel')
```

The first command creates an empty [Viewer Display Panel](#the-viewer-display-panel) and a [Load Data Window](#the-data-manager-panel---saving-and-loading-data).The second command starts the viewer with a loaded MeasurementSet. The third command starts the viewer and opens an image data cube (see [Initial Viewer Panels](#FigInitialViewerPanels)).

Examples four and five make use of the second parameter (displaytype). Example four displays the image as a contour map rather than the default raster map. Example five uses 'Lattice (Image) Expression Language' to display the square of the image data.

Note that the viewer can open FITS files, CASA image files, MeasurementSets, and saved viewer states. The viewer determines the type of file being opened automatically.

For additional scripting options when opening the viewer, see the discussion of the **imview** and **msview** tasks.

 

## Running the Viewer Outside CASA

If you have CASA installed, then the CASA Viewer is available as a stand-alone application called casaviewer. From the operating system prompt, the following commands work the same as the casa task commands given in the previous section:

```
casaviewer &

casaviewer ms_filename &
 
casaviewer image_filename &
 
casaviewer image_filename contour &
 
casaviewer '"image_filename"^2' lel &
```

#  

# The Viewer Display Panel

The CASA Viewer consists of a number of graphical user interface (GUI) windows. The main [Viewer Display Panel](#the-viewer-display-panel) is used for both image and MeasurementSet viewing. It is shown in the left panels of [Initial Viewer Panels](#FigInitialViewerPanels) and [Data Display Options](#the-viewer-display-panel) and appears the same whether an image or MeasurementSet is being displayed.

 

------------------------------------------------------------------------

 

![e8cf3cee163da8e2a22ef120a841581226610667](media/e8cf3cee163da8e2a22ef120a841581226610667.png)

------------------------------------------------------------------------

At the top of the Viewer Display Panel are drop down menus:

-   DATA
    -   Open --- open the [Data Manager](#the-data-manager-panel---saving-and-loading-data) window.
    -   Manage Images --- open the [Image Manager](#image-manager) which contains functionality for managing the image stack.
    -   Adjust Data Display --- open the [Data Display Options](#the-viewer-display-panel) (\'Adjust\') window.
    -   Save as\... --- save/export data to a file.
    -   Print --- print the displayed image.
    -   Save Panel State --- to a 'restore' file (xml format).
    -   Restore Panel State --- from a restore file.
    -   Preferences --- manually edit the viewer configuration.
    -   Close panel--- close this Viewer Display Panel. If this is the last display panel open, this will exit the viewer.
    -   Quit Viewer --- close all display panels and exit.
-   DISPLAY PANEL    -   New Panel--- create a new, empty Viewer Display Panel.
    -   Panel Options --- open the Viewer Canvas Manager (see the [Viewing Images and Cubes](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/viewing-images-and-cubes) page) window to edit margins, the number of panels, and the background.
    -   Save Panel State --- save the current state of the viewer as a file that can later be reloaded.
    -   Restore Panel State --- restore the viewer to a state previously saved as a file.
    -   Print --- print displayed image.
    -   Close Panel --- close this Viewer Display Panel. If this is the last display panel open, this will exit the viewer.
-   TOOLS
    -   Spectral Profile --- open the [Spectral Profile Browser](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/spectral-profiler) window to look at intensity as a function of frequency for part of an image.
    -   Collapse/Moments --- open the [Collapse/Moments](#viewerCollapseMoments) window, which allows you to create new images from a data cube by integrating along the spectral axis.
    -   Histogram --- open the [Histogram](#viewerHistogram) inspection window, which allows you to graphically examine the distribution of pixel values in a data cube.
    -   Fit --- open the [Two-Dimensional Fitting](#viewerSpectralFit) window, which can be used to fit Gaussians to two dimensional intensity distributions.
    -   Interactive Clean --- open a window to look at ongoing interactive clean processes.
-   VIEW
    -   Main Toolbar --- show/hide the top row of icons (see [Main Toolbar (image)](#the-main-toolbar) and [Main Toolbar (usage)](#the-main-toolbar)).
    -   Mouse Toolbar --- show/hide the second row of mouse-button action selection icons (see [Mouse Toolbar (image)](#the-mouse-toolbar) and [Mouse Toolbar (usage)](#the-mouse-toolbar)).
    -   Animators--- show/hide tapedeck control panel attachment to the main [Viewer Display Panel](#the-viewer-display-panel).
    -   Cursors --- show/hide the position tracking attachment to the main [Viewer Display Panel](#the-viewer-display-panel).
    -   Regions --- show/hide the region manager attachment to the main [Viewer Display Panel](#the-viewer-display-panel).

 

## The Main Toolbar

------------------------------------------------------------------------

 

![8b57d404c74488f1107e2ebf839c0f60faeb3c71](media/8b57d404c74488f1107e2ebf839c0f60faeb3c71.png)

>Main Toolbar: The Display Panel's Main Toolbar appears directly below the menus and contains \'shortcut\' buttons for most of the frequently-used menu items.
  

------------------------------------------------------------------------

 

Below the drop down menus is the Main Toolbar (see [Main Toolbar](#the-main-toolbar)). This top row of icons offers fast access to these menu items:

-   FOLDER (Data:Open shortcut) --- open the [Data Manager](#the-data-manager-panel---saving-and-loading-data) window.
-   WRENCH (Data:Adjust shortcut) --- open the [Data Display Options](#the-viewer-display-panel) ('Adjust') window.
-   MANAGE IMAGES (Data: Manage Images shortcut) - open the [Image Manager](#image-manager) window.
-   DELETE (Data:Close shortcut) --- close (unload) the selected data file. The menu expands to the right showing all loaded data.
-   SAVE DATA (Data:Save as) --- save the current data to a file.
-   NEW PANEL (Display Panel:New Panel) --- create a new, empty Viewer Display Panel.
-   PANEL WRENCH (Display Panel:Panel Options) --- open the Viewer Canvas Manager (see the [Viewing Images and Cubes](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/viewing-images-and-cubes) page) window to edit margins, the number of panels, and the background.
-   SAVE PANEL (Display Panel: Save Panel State) --- save panel state to a 'restore' file.
-   RESTORE PANEL (Display Panel: Restore Panel State) --- restore panel state from a restore file.
-   SPECTRAL PROFILE (Tools: Spectral Profile) --- Open the [Spectral Profile](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/spectral-profiler) window to look at intensity as a function of frequency for part of an image.
-   COLLAPSE/MOMENTS (Tools: Collapse/Moments) --- Open the [Collapse/Moments](#viewerCollapseMoments) window, which allows you to create new images from a data cube by integrating along the spectral axis.
-   HISTOGRAM (Tools:Histogram) --- Open the [Histogram](#viewerHistogram) inspection window, which allows you to graphically examine the distribution of pixel values in a data cube.
-   TWO-DIMENSIONAL FITTING (Tools:Fit) -- Open the [Two-Dimensional Fitting](#viewerSpectralFit) window, which can be used to fit Gaussians to two dimensional intensity distributions.
-   PRINT (Display Panel:Print) --- print the current display.
-   MAGNIFIER BOX --- zoom out all the way.
-   MAGNIFIER PLUS --- zoom in (by a factor of 2).
-   MAGNIFIER MINUS --- zoom out (by a factor of 2).     

## The Mouse Toolbar

------------------------------------------------------------------------

 

![aa5ec91c272ee59cd0bef0a8d695ca7872058795](media/aa5ec91c272ee59cd0bef0a8d695ca7872058795.png)

>Mouse Toolbar: The \'Mouse Tool\' Bar allows you to assign how mouse buttons behave in the image display area. Initially, zooming, color adjustment, and rectangular regions are assigned to the left, middle and right mouse buttons, respectively. Click on a tool with a mouse button to assign that tool to that mouse button.
  

------------------------------------------------------------------------

Below the Main Toolbar are eleven Mouse Tool buttons (see [Mouse Toolbar](#the-mouse-toolbar)). These allow you to assign what behavior the three mouse buttons have when clicked in the display area. Clicking a mouse tool icon will \[re-\]assign the mouse button that was clicked to that tool. Black and white squares beneath the icons show which mouse button is currently assigned to which tool.The mouse tools available from the toolbar are:

-   ZOOMING (magnifying glass icon): To zoom into a selected area, press the zoom tool's mouse button (the left button by default) on one corner of the desired rectangle and drag to the desired opposite corner. Once the button is released, the zoom rectangle can still be moved or resized by dragging. To complete the zoom, double-click inside the selected rectangle. If you instead double-click outside the rectangle, you will zoom out.
-   PANNING (hand icon): Press the panning tool's mouse button on a point you wish to move, drag it to the position where you want it moved, and release. Note: The arrow keys, Page Up, Page Down, Home and End keys can also be used to pan through your data any time you are zoomed in. (Click on the main display area first, to be sure the keyboard is 'focused' there).
-   STRETCH-SHIFT COLORMAP FIDDLING (crossed arrows): This is usually the handiest color adjustment; it is assigned to the middle mouse button by default. Hold down the tool\'s mouse button and drag across the display window to adjust the stretch and color. Note that you can also adjust the color table quantitatively inside the [Data Display Options](#viewerRasterMap) window.
-   BRIGHTNESS-CONTRAST COLORMAP FIDDLING (light/dark sun): Another tool to adjust the color stretch.
-   POSITIONING (plus): This tool can place a point marker on the display to select a position. It is used to flag MeasurementSet data or to select an image position for spectral profiles. Click on the desired position with the tool's mouse button to place the point; once placed you can drag it to other locations. You can also place multiple points on the display (e.g. for different spectral profile positions) -- remove them by hovering over and hitting ESC. Double-click is not needed for this tool. See [Viewer Region Positioning](#the-region-manager-panel) for more detail.
-   RECTANGLE, ELLIPSE, and POLYGON REGION DRAWING: The rectangle region tool is assigned to the right mouse button by default. As with the zoom tool, a rectangle region is generated by dragging with the assigned mouse button; the selection is confirmed by double-clicking within the rectangle. An ellipse regions is created by dragging with the assigned mouse button. In the case of an elliptical region, both the elliptical region and its surrounding rectangle are shown on the display. The selection is confirmed by double-clicking within the ellipse. Polygon regions are created by clicking the assigned mouse button at the desired vertices and then clicking the final location twice to finish. Once created, a polygon can be moved by dragging from inside, or reshaped by dragging the handles at the vertices. See [Viewer Region Positioning](#viewerRegionPositioning) for the uses of this tool.
-   POLYLINE DRAWING: A polyline can be created by selecting this tool. It is manipulated similarly to the polygon region tool: create segments by clicking at the desired positions and then double-click to finish the line.
-   DISTANCE TOOL (ruler): After selecting the distance tool by assigning a mouse button to it, distances on the image can conveniently be measured by dragging the mouse with the assigned button pressed. The tool measures the distances along the world coordinate axes and along the hypotenuse. If the units in both axes are \[deg\], the distances are displayed in \[arcsec\].
-   POSITION-VELOCITY DIAGRAM: Use this mouse tool to drag out a position axis that can be used to generate a position velocity diagram in a new viewer panel from the region manager dock.

<div class="alert alert-info">
**NOTE**: The \'escape\' key can be used to cancel any mouse tool operation that was begun but not completed, and to erase a region, point, or other tool showing in the display area.
</div>

 

## The Main Display Area

The Main Display Area lies below the toolbars. This area shows the image or MeasurementSet currently loaded. Clicking the mouse inside the display area allows region or position selection according to the settings in the mouse toolbar.The Display Area may have up to three attached panels: the Animators panel, the Cursors panel, and the Regions panel. These may be displayed or hidden from the \"View\" dropdown menu in the main Viewer Display Panel. If one of these is missing from your viewer, check that it is checked \"on\" in that menu. The panels can also be turned off by clicking the \"X\" in the top right corner, in which case you will need to use the View menu to get them back.By default, the three panels appear attached to the main Viewer Display Panel on the right side of the image. They may be dragged to new positions. Each of the three panels can be attached to the left, top, right, or bottom of the main Viewer Display Panel or they can be entirely undocked and left as free-floating panels.

<div class="alert alert-info">
**NOTE**: Depending on your window manager, windows without focus, including detached panels and tools like the Spectral Profile Browser may sometimes display odd behavior. As a general rule, giving the window focus by clicking on it will correct the issue. If you seem to \"lose\" a detached panel (like the Animators Panel), then click in the main window to get it back.
</div>

<div class="alert alert-info">
**NOTE**: With all three panels turned on (and especially with several images loaded), the Main Display Panel can sometimes shrink to very small sizes as the panels grow. Try detaching the panels to get the main display panel back to a useful size.
</div>

A restart of the viewer will display all docks in the state of a previous viewer session, given that it was closed normally. In addition, the viewer docking can be changed under "Preferences" in the toolbar (for Mac OS: under the "CASA Viewer" tab on the toolbar, for Linux: under "Data"). An example is given in the [Preference Dialog](#FigViewerPreferences) figure below. Each item can be changed and the input box will only allow accepted input formats. A complete restart is required to apply the changes.

------------------------------------------------------------------------

 ![8feaa9fb0d42d24217df66390ab85c79d44fa0bd](media/8feaa9fb0d42d24217df66390ab85c79d44fa0bd.png)

>Preference Dialog: The Preference Dialog can be used to manually change the docking and size of the viewer panel.
  

------------------------------------------------------------------------

###  The Animators Panel

![2cfd77b4f2ced4be1a260718e231ae8110cb6d0d](media/2cfd77b4f2ced4be1a260718e231ae8110cb6d0d.png)

>Animators Panel: The Animators Panel allows you to scroll through the z-axis of a data cube (using the Channels tape deck) or cycle among open Images. The panel can be undocked from the main display panel.
  

------------------------------------------------------------------------

The Animators Panel allows you to scroll through the channels of a data cube and to flip through loaded images. The main features of the panel are the two "tape decks," one labeled \"Channels\" and one labeled \"Images\".

<div class="alert alert-info">
**NOTE**: You will only see the Images tape deck when multiple images are loaded.
</div>

The \"Channels\" tape deck scrolls between planes of an individual image. By default, the channel tape deck scrolls among frequency planes when Right Ascension and Declination are the displayed axes (in this case, frequency is the z-axis). From outside to inside, the buttons cause the display to jump all the way to the beginning/end of the z-axis, cause the viewer to step one plane forward or backward along the z-axis, or start a movie. The limits on the z-axis can be set manually using the windows at the end of the scroll bar. The scroll bar can also be dragged or the user can jump the display to a manually entered plane by entering the plane into the text block.When you have multiple images loaded, the Images tape deck cycles through which is image is being displayed. In the movie mode, it allows you continuously click between images. Functionally, the Images tape deck works similarly to the Channels tape deck, with the ability to step, jump, or continuously scroll through images.

<div class="alert alert-info">
**NOTE**: The check boxes next to the channel and images tabs enable or disable those panels. This doesn't have much effect when the display has only a single panel, but with multiple panels (i.e., several maps at once in the main window) it changes the nature of the display. If the \"Images\" box is checked then interleaved maps from different cubes are displayed. Otherwise a series of maps from a single cube are shown.
</div>

 

## The Cursors Panel {#the-cursors-panel style="text-align: left;"}

------------------------------------------------------------------------

 

![b58deef224d019cae4184041a4e7fd9691bfcaf6](media/b58deef224d019cae4184041a4e7fd9691bfcaf6.png)

>Cursors Panel: The Cursors Panel gives information about the open data cube at the current location of the cursor. Freeze the Cursors Panel using the SPACE bar.
  

------------------------------------------------------------------------

The Cursors Panel (below the Images tape deck in [Initial Viewer Panels](#FigInitialViewerPanels)) shows the intensity, position (e.g., RA and Dec), Stokes, frequency (or velocity), and pixel location for the point currently under the cursor. A separate box appears for each registered image or MeasurementSet and you can see the tracking information for each. Tracking can be \'frozen\' (and unfrozen again) by hitting the space bar when the viewer's focus is on the main display area. (To be sure that the focus is indeed the main display area, first click on the main display area.)

 

### The Region Manager Panel {#the-region-manager-panel style="text-align: left;"}

The Region Manager Panel becomes active when regions are created. It has a large amount of functionality, from display region statistics and histograms to creating position-velocity cuts. We discuss these in [Viewer Regions](#viewerRegions). Like the Animators and Cursors Panels, the Region Manager Panel can be moved relative to the main Viewer Display Panel or entirely undocked.
## Saving and Restoring the Display Panel State {#saving-and-restoring-the-display-panel-state style="text-align: left;"}

You can save the display panel's current state --- meaning the panel settings and the data on display --- or load a saved panel state from disk. To save the display panel state, select Save Panel State from the Display Panel drop-down menu or click the \"Save Display Panel State to File\" icon on the main toolbar (an arrow pointing from a picture to a page, see [Main Toolbar](#the-main-toolbar)). It is advisable but not required to retain the file's \'.rstr\' (\"Restore\") extension.You can restore the display panel to the saved state by loading the saved state from the Data Manager Panel, by selecting Restore Panel State from the Display Panel drop down menu, or by clicking the \"Restore Display Panel State\" icon (just to the right of the \"Save Display Panel State\" icon).It is possible to restore panel states viewing MeasurementSets, images, or panel states that have multiple layers, such as contour plots over raster images. You can also save LEL displays. You can also the save or restore the panel state with no data loaded, which is a convenient way to restore preferred initial settings such as overall panel size.Data Locations: The viewer is fairly forgiving regarding data location when restoring a saved panel state. It will find files located:

-   in the original location recorded in the restore file
-   in the current working directory (where you started the viewer)
-   in the restore file's directory
-   in the original location relative to the restore file

This means that you can generally restore a saved panel state if you move that file together with data files. The exception to this rule is that the process is less forgiving if you save the display of an LEL expression. In this case the files must be in the locations specified in the original LEL expression. If a data file is not found, restore will attempt to proceed but results may not be ideal.Manually Editing Saved Display Panel States: The saved \"Restore\" files are in ascii (xml) format, and manual edits are possible. However, these files are long and complex. Use caution, and back up restore files before editing. If you make a mistake, the viewer may not even recognize the file as a restore file. It is easier and safer to make changes on the display panel and then save the display panel state again.
# The Data Manager Panel --- Saving and Loading Data

------------------------------------------------------------------------

 

![7d4cd267bbb4a3b269e1f22c908e1dc21a017b70](media/7d4cd267bbb4a3b269e1f22c908e1dc21a017b70.png)

>Data Manager Panel: The load tab of the Data Manager panel. This appears if you open the viewer without any infile specified, if you use select Open from the Data drop-down menu, or click the Open (Folder) icon. You can access the save image or save region tabs from this view or by selecting Save as\... from the Data drop down menu. The load tab shows all files in the current directory that can be loaded into the viewer --- images, MS, CASA region files, and Display Panel State files.
  

------------------------------------------------------------------------

The Data Manager Panel is used to interactively load and save images, MeasurementSets, Display Panel States, and regions. An example of the loading tab in this panel is shown in the [Data Manager Panel](#the-data-manager-panel---saving-and-loading-data) figure. This panel appears automatically if you open the viewer without specifying an input file or it can be accessed through the Data:Open menu or Open icon of the Viewer Display Panel.

 

## Loading Data

The load tab of the Data Manager Panel allows you to interactively choose images or MeasurementSets to load into the viewer. The load tab automatically shows you the available images, MeasurementSets, and Display Panel States in the current directory that can be opened by the viewer. When you highlight an image in this view, the tab shows a brief summary of the image: pixel shape, extent of the image on the sky and in frequency/velocity, and restoring beam (if available).Selecting a file will bring up information about that file in the panel on the right of the Data Manager Panel provide options for how to display the data. Images can be displayed as:

1.  raster image
2.  contour map
3.  vector map
4.  marker map

These options area each discussed in [Viewing Images](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/viewing-images-and-cubes).

Additionally, the following data types can be loaded via the Data Manager Panel:slice: a subselection of a data cube can be loaded, the start and end pixel in each spatial, polarization, and spectral dimension can be selected.LEL: Instead of only loading an image from disk, you may ask the viewer to evaluate a 'Lattice Expression Language' (LEL) expression (§ [6.1.4](https://casa.nrao.edu/casadocs-devel/docs/cookbook/casa_cookbook007.html#section%3Aanalysis.pars.lattice)). This can be entered in the box provided after you click the \"LEL\" box. The images used in the LEL expression should have the same coordinates and extents.MeasurementSets: A MeasurementSet can only be displayed as a raster. For MeasurementSets, the load tab offers options for data selection. This will reduce loading and processing times for visibility flagging.Regridding Images on Load: Optionally, you may regrid the velocity axis of an image you wish to load to match the current coordinates grid in the Display Panel. In this case, the viewer will interpolate (using the selected interpolation scheme) the cube on disk to share the same velocity gridding as the loaded coordinates. This can be used, e.g. to overlay contour maps of different spectral lines or to make synchronized movies of multiple cubes. Note that the regridding depends on the rest frequency in the image, which is used to calculate the velocities used in regridding.

 

## Registered vs. Open Datasets

When you load data as described above, it is first opened, and then registered on all existing Display Panels. An open dataset has been prepared in memory from disk. All open datasets will have a tab in the Data Display Options window, whether currently registered or not. When a data set is registered to a Display Panel its coordinates are aligned to the master coordinate image in the panel and it is ready for drawing. If multiple Display Panels are open then a data set may be registered on one Display Panel and not on another. Only those data sets registered on a particular Display Panel show up in its Cursors Panel.Why Register More Than One Image? It is useful to have more than one image registered on a panel if you are displaying a contour image over a raster image (see [Overlay Contours on a Raster Map](#viewerContourOverlay)), to 'blink' between images (see Animators in [Viewer Display Panel](#the-viewer-display-panel)), or to compare images using the Cursors Panel.Unregistering Images: A data set can be registered or unregistered using the Image Manager in the Data drop down menu or the Image Manager icon (third from left). This icon will open the Image Manager window and the checkboxes can be used to register or unregister an image.Closing vs. Unregistering: You can close a data set that is no longer needed using the Close option in the Data drop-down menu, the \"Close\" icon (fourth from left), or right mouse button "Close" selection in the [Image Manager](#image-manager).If you close a dataset, you must reload it from disk (or recreate it if it's an LEL expression, regridded image, moment or something similar) to see it again. If you unregister a dataset, it will draw immediately if you re-register it, with its options as you have previously set them. In general, close unneeded datasets but unregister those that you intend to use again.

 

## Image Manager

The Image Manager is used to define the master coordinate image, the sequence of images (e.g. for blinking), to register and unregister images, close images, change between raster, contour, vector, and marker displays, and to modify the properties of images. The panel can be invoked from the "Manage Images" tool, the third icon from the left (two overlapping squares).An example is shown in [Image Manager](#image-manager) figure. In this case, four images are loaded into the viewer. The sequence of images can be changed by dragging and dropping the images to new positions in the stack. The letter to the left indicates whether the image is a Raster, Contour, Vector, or Marker image. MC marks the coordinate master, in this case the second image. The checkboxes are to change the registration statuses. The Coordinate Master image can be defined by a right mouse click, and selecting the corresponding option. The right mouse menu button also offers options for quick changes between contour and raster images and to close an image.The Options button will open a drop-down box (as shown in [Image Manager](#image-manager) for the first image), in which one can again change between image type, change to a different rest frequency (or "Reset" to the value in the image header), or open the \"Display Options\" panel for that specific image with all the adjustment options explained in [Viewing a Raster Map](#viewerRasterMap) or [Viewing a Contour Map](#viewerContourMap)).

------------------------------------------------------------------------

 

![8974d9863e86c477d90bafedc2635435d5e45fbb](media/8974d9863e86c477d90bafedc2635435d5e45fbb.png)

>Image Manager
  

------------------------------------------------------------------------

 

 

## Saving Data or Regions

------------------------------------------------------------------------

 

![6635be99d7c7c01aecee67542626f14a7a4fab30](media/6635be99d7c7c01aecee67542626f14a7a4fab30.png)

>Save Data Panel: The Save Data panel that appears when selecting the 'Save as\...' (see [Main Toolbar](#FigMainToolbar)).
  

 

------------------------------------------------------------------------

The viewer can create new images by carrying out velocity regridding, evaluating an LEL expression, or collapsing a data cube. You can save these images to disk using the Data Manager Panel. Select Save As under the Data drop-down menu or click the Save As (disk) icon to bring up the Data Manager Panel set to the save tabs. These tabs are shown in the figure above.From the Save Image tab of the Data Manager Panel, you can export images from the viewer to either a CASA image or FITS file on disk. Select the desired file name and click \"Save.\" The Data Manager also allows you to save your current regions to a file, either in the CASA or ds9 format. The left side of the Save Data Panel lists all images that can be exported to disk. To save an image to a file, you can either enter the new filename in the box labeled \'output name:\' followed by the save-button (alternatively the 'Enter'-key), or choose a file name from the right hand side.

