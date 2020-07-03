.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Viewing Images and Cubes
========================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Details on viewing images and cubes

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Viewing Images
         :name: viewing-images

      There are several options for viewing an image. These are seen at
      the right of the Load Data - Viewer panel described in `Initial
      Viewer Panels <#initial-viewer-panels>`__ after selecting an
      image. They are:

      -  raster image — a greyscale or color image,
      -  contour map — contours of intensity as a line plot,
      -  vector map — vectors (as in polarization) as a line plot,
      -  marker map — a line plot with symbols to mark positions.

      The raster image is the default image display, and is what you get
      if you invoke the viewer with an image file and no other options.
      In this case, you will need to use the Open menu to bring up the
      Load Data panel to choose a different display.

      This page discusses raster images and contour maps in detail; for
      an example of how to use a vector map, see the 3C286 Polarization
      CASAguide
      `here <https://casaguides.nrao.edu/index.php/3C286_Band6Pol_Imaging_for_CASA_4.3>`__.

      .. rubric:: Initial Viewer Panels
         :name: viewerRasterMap

      When the viewer is started, two dialogs appear. One is the Data
      Manager which presents two panels.

      .. rubric:: Data Manager
         :name: data-manager

      The left panel shows the files that the viewer can load while the
      right panel shows some statistics about the file that is selected.

      |image1|

      The other panel is the Viewer Display Panel.

      .. rubric:: Viewer Display Panel
         :name: viewer-display-panel

      This panel is the main panel used to interact with the viewer. 

      |image2|

      | 
      | The image is shown on the left and image information is shown on
        the right. The Cursors panel displays information about the
        pixel at the current cursor location (as the cursor is moved
        around the image).

      .. rubric:: Animators Panel
         :name: animators-panel

      The Animators panel allows the planes on the image cube to be
      displayed. This can be done by either single-stepping plane by
      plane or playing the planes of the image cube like a movie. The
      buttons are: 

      +-----------------------------------+-----------------------------------+
      | |image3|                          | move to the first image plane     |
      +-----------------------------------+-----------------------------------+
      | |image4|                          | move back one image plane         |
      +-----------------------------------+-----------------------------------+
      | |image5|                          | play image cube in reverse        |
      +-----------------------------------+-----------------------------------+
      | |image6|                          | stop playing the movie            |
      +-----------------------------------+-----------------------------------+
      | |image7|                          | play image cube as a movie        |
      +-----------------------------------+-----------------------------------+
      | |image8|                          | move forward one image plane      |
      +-----------------------------------+-----------------------------------+
      | |image9|                          | move to the last image plane      |
      +-----------------------------------+-----------------------------------+

      | 
      | In addition, to these controls for moving through the image
        cube, there are two other areas of animation control:

      +-----------+---------------------------------------------------------+
      | |image14| | the rate indicates how how fast the movie should be     |
      |           | played in terms of frames, and the second entry box     |
      |           | (here with a zero) is for going to a particular plane   |
      |           | of the image cube (enter a number and hit return) [Jump |
      |           | doesn't seem to do anything]                            |
      +-----------+---------------------------------------------------------+
      | |image15| | the slider of this control allows for moving through    |
      |           | the image cube as the slider is moved. The dialogs at   |
      |           | the ends of the slider allows for setting the start and |
      |           | end points for the movie (which can be less than or     |
      |           | equal to zero and the number of planes in the cube)     |
      +-----------+---------------------------------------------------------+

      .. rubric:: Button Tools
         :name: button-tools

      These tools are designed for use with a three-button mouse. The
      row of boxes below the icon indicates which mouse button to which
      the tool is currently bound. For example, the last three icons in
      this table indicate that these tools are bound to the first,
      second, and third buttons respectively:

      +-----------+---------------------------------------------------------+
      | |image38| | zoom: select this tool (by clicking on this icon and    |
      |           | pressing one of the three buttons), then click and drag |
      |           | out a rectangle, then double click inside the rectangle |
      |           | to zoom in                                              |
      +-----------+---------------------------------------------------------+
      | |image39| | panning: select this tool, then if the image is zoomed  |
      |           | in, click and drag within the image to move the image   |
      +-----------+---------------------------------------------------------+
      | |image40| | adjust color map: select this tool, then click and drag |
      |           | within the image to adjust the color map                |
      +-----------+---------------------------------------------------------+
      | |image41| | contrast: select this tool, then click and drag within  |
      |           | the image                                               |
      +-----------+---------------------------------------------------------+
      | |image42| | point region: select this tool, then place a point on   |
      |           | the image, the regions panel corresponding to the dot   |
      |           | you placed will have statistics an information about    |
      |           | the selected point                                      |
      +-----------+---------------------------------------------------------+
      | |image43| | rectangular region: select this tool, then click and    |
      |           | drag out a rectangle in the image and the regions panel |
      |           | corresponding to this region will have information      |
      |           | about the rectangular region; double clicking in the    |
      |           | region will display the statistics in to terminal       |
      |           | window                                                  |
      +-----------+---------------------------------------------------------+
      | |image44| | eliptical region: select this tool, then click and drag |
      |           | out an ellipse, the regions panel corresponding to this |
      |           | region will have information about the eliptical        |
      |           | region; double clicking in the region will display the  |
      |           | statistics in the terminal window                       |
      +-----------+---------------------------------------------------------+
      | |image45| | polygon region: select this tool, then click multiple   |
      |           | times within the image to mark out a region (one click  |
      |           | at a time), double clicking when you have marked all of |
      |           | the points that denote the polygon, the regions panel   |
      |           | corresponding to this region will have information      |
      |           | about this region; double clicking in the region will   |
      |           | display statistics for this region in the terminal      |
      |           | window                                                  |
      +-----------+---------------------------------------------------------+
      | |image46| | polyline region: select this tool, then click multiple  |
      |           | times within the image to mark out a multi-segment      |
      |           | line, the region panel for this region will display     |
      |           | statistics about the region                             |
      +-----------+---------------------------------------------------------+
      | |image47| | ruler: select this tool, click and drag in the image to |
      |           | get a display of distance along two axes                |
      +-----------+---------------------------------------------------------+
      | |image48| | pv diagram: select this tool, click and drag within the |
      |           | image to create  a to be used to create a               |
      |           | position/velocity diagram (the diagram is created from  |
      |           | the region panel corresponding to the P/V line that     |
      |           | you've drawn)                                           |
      +-----------+---------------------------------------------------------+

      These tools create regions that can be used to provide information
      about a portion of an image.

      .. rubric:: Regions
         :name: regions

      Regions are created with the region `Button
      Tools <#button-tools>`__. For a region to be created, the Region
      panel (displayed on the left side of the Viewer Display Panel)
      must be open. If you do not see the Regions panel, it can be
      included in the Display Panel by selecting the Regions check box
      in the View menu:

      |image49|

      Once the Regions dialog is in view Regions can be created and
      information about the regions can be viewed. For example, here one
      region (black rectangle) has been created and region statistics is
      displayed:

      |image50|

      Note that in the statistics window, the brightness units are
      specified and the beam area is defined as the volume of the
      elliptical Gaussian $\frac{Π}{4ln(2)} \* FWHM_{major} \*
      FWHM_{minor}$, where ln() is the natural logarithm and
      $FWHM_{major}$ and $FWHM_{minor}$ are the major and minor FWHM
      axes of the beam, respectively. The flux density is the mean
      intensity multiplied by the number of beams included in the
      selected region.

      .. rubric:: Region Statistics
         :name: region-statistics

      If more than one region has been created, the scroll bar can be
      used to move from the information about one region to the next or
      the cursor (in the image panel) can be used to move from one
      region to the next and the region information will be updated as
      the cursor moves from region to region. Here are three regions,
      showing histograms for the regions:

      |image51|

      .. rubric:: Region Histogram
         :name: region-histogram

      The region which corresponds to the histogram that is shown has
      the corner adjustment cubes drawn.

      Any regions that are created using these tools can be removed by
      moving the cursor over the region you would like to remove and
      once that region is highlighted press the escape key. Regions can
      also be deleted from the region panel that corresponds to the
      region you would like to remove.

      .. rubric:: Viewing a Raster Map
         :name: viewing-a-raster-map

      A raster map of an image shows pixel intensities in a
      two-dimensional cross-section of gridded data with colors selected
      from a colormap according to a scaling that can be specified by
      the user. Starting the casaviewer with an image as a raster map
      will look something like the example in `Initial Viewer
      Panels <#initial-viewer-panels>`__. Once loaded, the data display
      can be adjusted by the user through the Data Display Options
      panel, which appears when you choose the Data: Adjust Data Display
      menu or use the wrench icon from the Main Toolbar. The Data
      Display Options window is shown in the right panel of `Initial
      Viewer Panels <#initial-viewer-panels>`__. It consists of a tab
      for each image or MS loaded, under which are a cascading series of
      expandable categories. For an image, these are:

      -  display axes
      -  hidden axes
      -  basic settings
      -  position tracking
      -  axis labels
      -  axis label properties
      -  beam ellipse
      -  color wedge

      The basic settings category is expanded by default. To expand a
      category to show its options, click on it with the left mouse
      button.

       

      .. rubric:: Data Display Options — Display and Hidden Axes
         :name: data-display-options-display-and-hidden-axes

      In this category the physical axes (i.e. Right Ascension,
      Declination, Velocity, Stokes) to be displayed can be selected and
      assigned to the x, y, and z axes of the display. The z axis will
      be the axis scrolled across by the channel bar in the Animators
      Panel. If your image has a fourth axis (typically Stokes), then
      one of the axes will need to be hidden and not used in viewing.
      Which axis is hidden can be controlled by a slider within the
      hidden axes drop-down.

       

      .. rubric:: Data Display Options — Basic Settings
         :name: data-display-options-basic-settings

      This roll-up is open by default showing some commonly-used
      parameters that alter the way the image is displayed. The most
      frequently used of these changes how the intensity value of a
      pixel maps to a color on the screen. An example of this part of
      the panel is shown in `Mapping Intensity to
      Color <#FigColorMapping>`__.

      --------------

      .. figure:: ../../../../../docs/cookbook/casa_cookbook065.png
         :alt: Mapping Intensity to Color: The basic settings category
         of the Data Display Options panel and the interactive tool for
         setting the mapping from intensity to color.
         :figclass: image-inline
         :width: 315px
         :height: 238px

         Mapping Intensity to Color: The basic settings category of the
         Data Display Options panel and the interactive tool for setting
         the mapping from intensity to color.

      --------------

      .. container::

         The options available are:

      -  basic settings: *aspect ratio*

         This option controls the horizontal-vertical size ratio of data
         pixels on screen. "Fixed world" (the default) means that the
         *aspect ratio* of the pixels is set according to the coordinate
         system of the image (i.e., true to the projected sky). "Fixed
         lattice" means that data pixels will always be square on the
         screen. Selecting "flexible" allows the map to stretch
         independently in each direction to fill as much of the display
         area as possible.

      -  basic settings: *pixel treatment*

         This option controls the precise alignment of the edge of the
         current "zoom window" with the data lattice. "Edge" (the
         default) means that whole data pixels are always drawn, even on
         the edges of the display. For most purposes, "edge" is
         recommended. "center" means that data pixels on the edge of the
         display are drawn only from their centers inwards.

         .. container:: info-box

            **NOTE**: A data pixel’s center is considered its
            "definitive" position, and corresponds to a whole number in
            "data pixel" or "lattice" coordinates.

      -  basic settings: *resampling mode*

         This setting controls how the data are resampled to the
         resolution of the screen. "Nearest" (the default) means that
         screen pixels are colored according to the intensity of the
         nearest data point, so that each data pixel is shown in a
         single color. "Bilinear" applies a bilinear interpolation
         between data pixels to produce smoother looking images when
         data pixels are large on the screen. "Bicubic" applies an even
         higher-order (and somewhat slower) interpolation.

      -  basic settings: *data range*

         You can use the entry box provided to set the minimum and
         maximum data values mapped to the available range of colors as
         a list [min, max]. For very high dynamic range images, you will
         probably want to enter a max less than the data maximum in
         order to see detail in lower brightness-level pixels.

         .. container:: info-box

            **NOTE**: By default you edit the scaling of a single image
            at once and can click between the tabs at the top of the
            Data Display Options window to manipulate different windows.
            By checking the Global Color Settings box at the bottom of
            this window, you will manipulate the scaling for all images
            at once. This can be very useful, for example, when
            attempting a detailed comparison between multiple reductions
            of the same data.

      -  basic settings: *scaling power cycles*

         This option allows logarithmic scaling of data values to
         colormap cells, which can be very helpful in the case of very
         high dynamic range. The color for a data value is determined as
         follows:

         1. The value is clipped to lie within the data range [min, max]
            specified above.
         2. This clipped value is mapped to a new value depending on the
            selected scaling power cycles in the following way:

            -  If the scaling power cycles is set to 0 (the default),
               the program considers a linear range from [min, max] and
               scales this directly onto the set of available colors.
            -  For positive scaling values, the data value (after
               clipping on [min, max] is scaled linearly to lie between
               0 and p (where p is the value chosen) and 10 is raised to
               this power, yielding a value in the range 1 to
               10\ :sup:`p`. That value is scaled linearly to the set of
               available colors.
            -  For negative scaling values, the data value (after
               clipping on [min, max]) is scaled linearly to lie between
               1 and 10\ \|p\|, where p is the power chosen. The base 10
               logarithm is taken of this re-scaled data value, yielding
               a value in the range 0 to abs(p). That value is scaled
               linearly to the set of available colors. Thus the data is
               treated as if it had p decades of range, with an equal
               number of colors assigned to each decade.

         3. The color corresponding to a number in final range is
            determined by the selected colormap and its "fiddling"
            (shift/slope) and brightness/contrast settings (see Mouse
            Toolbar, above). Adding a color wedge to your image can help
            clarify the effect of the various color controls.

         See `Scaling Power Cycles <#FigScalingPowerCycles>`__ for
         sample curves.

      --------------

      .. figure:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/scaling_powers.png/@@images/ec869f54-c03d-486f-b266-01d011aa6e03.png
         :alt: scaling_powers.png
         :figclass: image-inline

         Scaling Power Cycles: Example curves for scaling power cycles.

      --------------

      In practice, you will often manipulate the data range bringing the
      max down in high dynamic range images, raising the minimum to the
      near the noise level when using non-zero scaling cycles. It is
      also common to use negative power cycles when considering high
      dynamic range images — this lets you bring out the faint features
      around the bright peaks.

      -  basic settings: *colormap*

         You can select from a variety of colormaps here. Hot Metal,
         Rainbow and Greyscale colormaps are the ones most commonly
         used.

       

      .. rubric:: Graphical Specification of the Intensity Scale
         :name: graphical-specification-of-the-intensity-scale

      A histogram icon next to the Data Range entry in the Data Display
      Options window opens the Image Color Mapping window, which allows
      visualization and graphical manipulation of the mapping of
      intensity to color. The window at the left shows a histogram of
      the data with a gray range showing the data range. You can use
      this window to select the data range graphically (with the mouse),
      manually (by typing into the Min and Max entry windows), or as a
      percentile of the data. On the right, you can select the scaling
      power cycles and see a visualization of the transfer function
      mapping intensity (x-axis) to color (y-axis).

      The functionality here follows the other histogram tools, with the
      Display tab used to change the histogram plotting parameters. It
      will often be useful to use a logarithmic scaling of the y-axis
      and filled histograms when manipulating the color table.

       

      .. rubric:: Data Display Options — Other Settings
         :name: data-display-options-other-settings

      Many of the other settings on the Data Display Options panel for
      raster images are self-explanatory such as those which affect beam
      ellipse drawing (only available if your image provides beam data),
      or the form of the axis labeling and position tracking
      information. You can also give your image a color wedge, a key to
      the current mapping from data values to colors.

       

      .. rubric:: Viewer Canvas Manager — Panels, Margins, and
         Backgrounds
         :name: viewer-canvas-manager-panels-margins-and-backgrounds

      --------------

      .. figure:: ../../../../../docs/cookbook/casa_cookbook067.png
         :alt: Multi-Panel Display: A multi-panel display set up through
         the Viewer Canvas Manager.
         :figclass: image-inline

         Multi-Panel Display: A multi-panel display set up through the
         Viewer Canvas Manager.

      --------------

       The display area can also be manipulated from the Viewer Canvas
      Manager window. Use the wrench icon with a "P" (or the "Display
      Panel" menu) to show this window, which allows you to manipulate
      the infrastructure of the main display panel. You can set:

      -  Margins - specify the spacing for the left, right, top, and
         bottom margins
      -  Number of panels - specify the number of panels in x and y and
         the spacing between those panels.
      -  Background Color - white or black (more choices to come)

      `Multi-Panel Display <#FigMultiPanel>`__ illustrates a multi-panel
      display along with the Viewer Canvas Manager settings which
      created it.

      .. container::

          
         .. rubric:: Viewing a Contour Map
            :name: viewing-a-contour-map

         Viewing a contour image is similar to viewing a raster map. A
         contour map shows lines of equal data value for the selected
         plane of gridded data (see `Viewing a Contour
         Map <#FigContourView>`__). Contour maps are particularly useful
         for overlaying on raster images so that two different
         measurements of the same part of the sky can be shown
         simultaneously (see `Overlay Contours on a Raster
         Map <#viewerContourOverlay>`__).

         Several basic settings options control the contour levels used:

         -  The contours themselves are specified by a list in the box
            *Relative Contour Levels*. These are defined relative to the
            two other parameters:
         -  The *Base Contour Level* sets the zero level for the
            relative contour list corresponds to in units of intensity
            in the image.
         -  The *Unit Contour Level* sets what 1 in the relative contour
            list corresponds to in units of intensity in the image.

         Additionally, you have the option to manipulate the thickness
         and color of the image and to have either positive or negative
         contours appear dashed.

         --------------

         .. figure:: ../../../../../docs/cookbook/casa_cookbook069.png
            :alt: Viewing a Contour Map: The Viewer Display Panel (top)
            and Data Display Options panel (bottom) after choosing
            contour map from the Load Data panel. The image shown is for
            channel 11 of the NGC5921 cube, selected using the Animators
            tape deck, and zoomed in using the tool bar icon. Note the
            different options in the open basic settings category of the
            Data Display Options panel (as compared to raster image in
            `Initial Viewer Panels <#initial-viewer-panels>`__).
            :figclass: image-inline

            Viewing a Contour Map: The Viewer Display Panel (top) and
            Data Display Options panel (bottom) after choosing contour
            map from the Load Data panel. The image shown is for channel
            11 of the NGC5921 cube, selected using the Animators tape
            deck, and zoomed in using the tool bar icon. Note the
            different options in the open basic settings category of the
            Data Display Options panel (as compared to raster image in
            `Initial Viewer Panels <#initial-viewer-panels>`__).

         --------------

         For example, the following settings:

         ::

               Relative Contour Levels = [0.2, 0.4, 0.6, 0.8]
               Base Contour Level = 0.0
               Unit Contour Level = <image max>

         would map the maximum of the image to 1 in the relative contour
         levels and the base contour level to zero. So the contours will
         show 20%, 40%, 60%, and 80% of the peak.

         Another approach is to set the unit contour to 1, so that the
         contours are given in intensity units (usually Jy/beam). So
         this setup:

         ::

               Relative Contour Levels = [0.010, 0.0.020, 0.040, 0.080, 0.160, 0.320]
               Base Contour Level = 0.0
               Unit Contour Level = 1.0

         would create contours starting at 10 mJy/beam and doubling
         every contour.

         Another useful approach is to set contours in units of the rms
         noise level of the image, which can be worked out from a signal
         free region. Then a setup like this:

         ::

               Relative Contour Levels = [-3,3,5,10,15,20]
               Base Contour Level = 0.0
               Unit Contour Level = <image rms>

         Would indicate significance of the features in the image. The
         first two contours show emission at ± 3-sigma and so on. You
         can get the image rms using the `imstat
         task <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_imstat>`__ or
         using the `Region Statistics <#region-statistics>`__ on a
         region of the image .

         Not all images are of intensity, for example a moment-1 image
         (`immoments
         task <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_immoments>`__)
         has units of velocity. In this case, absolute contours (like
         the last two examples) will work fine, but by default the
         viewer will set fractional contours but refer to the min and
         max of the image:

         ::

               Relative Contour Levels = [0.2, 0.4, 0.6, 0.8]
               Base Contour Level = <image min>
               Unit Contour Level = <image max>

         Here we have contours spaced evenly from min to max, and this
         is what you get by default if you load a non-intensity image
         (like the moment-1 image). See `Overlaying a Contour
         Map <#FigContourOverlay>`__ for an example of this.

          

         .. rubric:: Overlay Contours on a Raster Map
            :name: overlay-contours-on-a-raster-map

         Contours of either a second data set or the same data set can
         be used for comparison or to enhance visualization of the data.
         The Data Display Options Panel will have multiple tabs (switch
         between them at the top of the window) that allow you to adjust
         each overlay individually.

         .. container:: info-box

            **NOTE**: Axis labeling is controlled by the
            first-registered image overlay that has labeling turned on
            (whether raster or contour), so make label adjustments
            within that tab.

         To add a Contour overlay, open the Load Data panel (Use the
         Data menu or click on the folder icon), select the data set and
         click on contour map. See `Overlaying a Contour
         Map <#FigContourOverlay>`__ for an example using NGC5921.

         --------------

         .. figure:: ../../../../../docs/cookbook/casa_cookbook071.png
            :alt: Overlaying a Contour Map: The Viewer Display Panel
            (top) andData Display Options panel (bottom) after
            overlaying a Contour Map of velocity on a Raster Image of
            intensity. The image shown is for the moments of the NGC5921
            cube, zoomed in using the tool bar icon. The tab for the
            contour plot is open in the Data Display Options panel.
            :figclass: image-inline

            Overlaying a Contour Map: The Viewer Display Panel (top)
            andData Display Options panel (bottom) after overlaying a
            Contour Map of velocity on a Raster Image of intensity. The
            image shown is for the moments of the NGC5921 cube, zoomed
            in using the tool bar icon. The tab for the contour plot is
            open in the Data Display Options panel.

          

         .. rubric:: Creating a Position/Velocity Diagram
            :name: creating-a-positionvelocity-diagram

         With an image cube loaded, it is possible to create a
         position/velocity diagram using the P/V Button Tool (see
         `Initial Viewer Panels <#initial-viewer-panels>`__). The first
         step in creating a P/V diagram is to select the tool with the
         mouse button to which you would like to bind the tool:

         |image52|

         Here we have bound the P/V button tool to the first mouse
         button. At this point, we can drag out a P/V line, by clicking
         and dragging on the image:

         |image53|

          

         After creating the P/V line, it will appear with two circles on
         each end. These circles can be used to adjust the line by
         clicking within the circle and dragging:

         |image54|

         After the P/V line is properly in place, the final P/V diagram
         can be created from the P/V Regions panel. It is just a matter
         of generating the P/V diagram with the Generate P/V button:

         |image55|

         The generation of the P/V diagram may take some time, but then
         the final diagram is displayed:

         |image56|

          

          

          

          

          

          

          

          

.. container:: section
   :name: viewlet-below-content-body

.. |image1| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/data-manager.jpeg/@@images/eb696ae9-b84f-42b9-95ac-b17441931778.jpeg
   :class: image-inline
   :width: 479px
   :height: 314px
.. |image2| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/viewer-display-panel.jpeg/@@images/39a94bfa-318a-46ed-aa33-2d0034ac26bb.jpeg
   :class: image-inline
   :width: 477px
   :height: 305px
.. |image3| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/anim0_tostart.png/@@images/b5b0b005-a1cf-4827-9ca7-d9dde2489f7a.png
   :class: image-left
.. |image4| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/anim1_revstep.png/@@images/7ba927f7-2477-4739-a00d-84a439d37d1e.png
   :class: image-left
.. |image5| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/anim2_rev.png/@@images/c1aacd37-c86b-487c-935e-8147d450f004.png
   :class: image-left
.. |image6| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/anim3_stop.png/@@images/72c666e2-6ed6-4393-b712-1ad584207bdc.png
   :class: image-left
.. |image7| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/anim4_play.png/@@images/8acbcc4c-d4f4-4d99-ae0a-e3bf74174226.png
   :class: image-left
.. |image8| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/anim5_fwdstep.png/@@images/40232385-cf7b-4ff0-bc29-538b357bb0ab.png
   :class: image-left
.. |image9| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/anim6_toend.png/@@images/274bc9e3-2ea6-4d06-9a54-e387ffdf5517.png
   :class: image-left
.. |image10| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/movie-controls.jpeg/@@images/95e812ce-0060-40e4-b67a-64c1157465ff.jpeg
   :class: image-left
   :width: 196px
   :height: 25px
.. |image11| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/movie-boundary.jpeg/@@images/9cfa93eb-af4e-4d86-b5cd-4e7c2b52f8ed.jpeg
   :class: image-left
   :width: 316px
   :height: 18px
.. |image12| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/movie-controls.jpeg/@@images/95e812ce-0060-40e4-b67a-64c1157465ff.jpeg
   :class: image-left
   :width: 196px
   :height: 25px
.. |image13| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/movie-boundary.jpeg/@@images/9cfa93eb-af4e-4d86-b5cd-4e7c2b52f8ed.jpeg
   :class: image-left
   :width: 316px
   :height: 18px
.. |image14| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/movie-controls.jpeg/@@images/95e812ce-0060-40e4-b67a-64c1157465ff.jpeg
   :class: image-left
   :width: 196px
   :height: 25px
.. |image15| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/movie-boundary.jpeg/@@images/9cfa93eb-af4e-4d86-b5cd-4e7c2b52f8ed.jpeg
   :class: image-left
   :width: 316px
   :height: 18px
.. |image16| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/magnifyb0.png/@@images/68cb6ff9-81a0-4cc4-bb24-fed6a5bdfb2d.png
   :class: image-left
.. |image17| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/handb0.png/@@images/bf42950a-d14e-4604-9c0e-648f8518ff0a.png
   :class: image-left
.. |image18| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/arrowcrossb0.png/@@images/4fbd998d-5ad8-4254-ac95-94488fdb6ced.png
   :class: image-left
.. |image19| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/brightcontrastb0.png/@@images/088bb800-1dea-44ea-b569-764de7a7e006.png
   :class: image-left
.. |image20| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/symdotb0.png/@@images/868e9c81-34aa-46a4-9be7-47a0e5df6fd5.png
   :class: image-left
.. |image21| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/rectregionb0.png/@@images/855840cc-7b13-49dc-b3d2-e1375db38a19.png
   :class: image-left
.. |image22| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/ellregionb0.png/@@images/7476e41d-71d0-40ab-b4ca-32d1326d8ed1.png
   :class: image-left
.. |image23| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/polyregionb0.png/@@images/2cecc620-d669-4c9f-bc2a-5328bba9f861.png
   :class: image-left
.. |image24| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/polylineb1.png/@@images/0341cc4d-3eda-4317-baa0-9cea16d8f4d4.png
   :class: image-left
.. |image25| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/rulerb2.png/@@images/2885c036-c9db-4ba1-b15d-7838698e3b4e.png
   :class: image-left
.. |image26| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/pvtoolb3.png/@@images/f6424dd6-c059-4372-8753-c920bcb802d4.png
   :class: image-left
.. |image27| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/magnifyb0.png/@@images/68cb6ff9-81a0-4cc4-bb24-fed6a5bdfb2d.png
   :class: image-left
.. |image28| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/handb0.png/@@images/bf42950a-d14e-4604-9c0e-648f8518ff0a.png
   :class: image-left
.. |image29| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/arrowcrossb0.png/@@images/4fbd998d-5ad8-4254-ac95-94488fdb6ced.png
   :class: image-left
.. |image30| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/brightcontrastb0.png/@@images/088bb800-1dea-44ea-b569-764de7a7e006.png
   :class: image-left
.. |image31| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/symdotb0.png/@@images/868e9c81-34aa-46a4-9be7-47a0e5df6fd5.png
   :class: image-left
.. |image32| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/rectregionb0.png/@@images/855840cc-7b13-49dc-b3d2-e1375db38a19.png
   :class: image-left
.. |image33| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/ellregionb0.png/@@images/7476e41d-71d0-40ab-b4ca-32d1326d8ed1.png
   :class: image-left
.. |image34| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/polyregionb0.png/@@images/2cecc620-d669-4c9f-bc2a-5328bba9f861.png
   :class: image-left
.. |image35| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/polylineb1.png/@@images/0341cc4d-3eda-4317-baa0-9cea16d8f4d4.png
   :class: image-left
.. |image36| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/rulerb2.png/@@images/2885c036-c9db-4ba1-b15d-7838698e3b4e.png
   :class: image-left
.. |image37| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/pvtoolb3.png/@@images/f6424dd6-c059-4372-8753-c920bcb802d4.png
   :class: image-left
.. |image38| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/magnifyb0.png/@@images/68cb6ff9-81a0-4cc4-bb24-fed6a5bdfb2d.png
   :class: image-left
.. |image39| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/handb0.png/@@images/bf42950a-d14e-4604-9c0e-648f8518ff0a.png
   :class: image-left
.. |image40| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/arrowcrossb0.png/@@images/4fbd998d-5ad8-4254-ac95-94488fdb6ced.png
   :class: image-left
.. |image41| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/brightcontrastb0.png/@@images/088bb800-1dea-44ea-b569-764de7a7e006.png
   :class: image-left
.. |image42| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/symdotb0.png/@@images/868e9c81-34aa-46a4-9be7-47a0e5df6fd5.png
   :class: image-left
.. |image43| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/rectregionb0.png/@@images/855840cc-7b13-49dc-b3d2-e1375db38a19.png
   :class: image-left
.. |image44| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/ellregionb0.png/@@images/7476e41d-71d0-40ab-b4ca-32d1326d8ed1.png
   :class: image-left
.. |image45| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/polyregionb0.png/@@images/2cecc620-d669-4c9f-bc2a-5328bba9f861.png
   :class: image-left
.. |image46| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/polylineb1.png/@@images/0341cc4d-3eda-4317-baa0-9cea16d8f4d4.png
   :class: image-left
.. |image47| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/rulerb2.png/@@images/2885c036-c9db-4ba1-b15d-7838698e3b4e.png
   :class: image-left
.. |image48| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/pvtoolb3.png/@@images/f6424dd6-c059-4372-8753-c920bcb802d4.png
   :class: image-left
.. |image49| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/viewer-view-menu.jpeg/@@images/22cc99ee-f10b-48d3-8d38-5f1beb6bd5af.jpeg
   :class: image-inline
   :width: 277px
   :height: 132px
.. |image50| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/region-statistics.jpeg/@@images/611c2581-f5b4-4e01-8c9b-64a75487fbe5.jpeg
   :class: image-inline
   :width: 497px
   :height: 248px
.. |image51| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/region-histogram.jpeg/@@images/dd9153e4-7c88-4caa-9c06-430fd0b5fd4f.jpeg
   :class: image-inline
   :width: 464px
   :height: 218px
.. |image52| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/pv-diagram-select-tool.jpeg/@@images/067e549f-88dd-41a1-b6aa-286987c7795e.jpeg
   :class: image-inline
   :width: 326px
   :height: 328px
.. |image53| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/pv-diagram-drag-line.jpeg/@@images/c621178b-011c-4cac-9cf8-265d1efa1519.jpeg
   :class: image-inline
   :width: 316px
   :height: 317px
.. |image54| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/pv-diagram-adjust-circles.jpeg/@@images/637cb0d1-449b-4fea-afce-ad15b50c5bfd.jpeg
   :class: image-inline
   :width: 311px
   :height: 312px
.. |image55| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/pv-diagram-region-panel.jpeg/@@images/5383c6b5-1af9-4261-84c3-ca20c4e46cb6.jpeg
   :class: image-inline
   :width: 538px
   :height: 279px
.. |image56| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/pv-diagram-final-image.jpeg/@@images/bdc6fcaa-3032-4038-8cd7-8b55807b0f6f.jpeg
   :class: image-inline
   :width: 596px
   :height: 365px
