.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Regions in the Viewer
=====================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Using CASA CRTF Regions in the Viewer

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

       

      .. rubric:: Regions and the Region Manager
         :name: regions-and-the-region-manager

       

      --------------

      .. figure:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/casa_cookbook073.png/@@images/971b6a45-de35-4fd7-aa57-66d698ea9527.png
         :alt: casa_cookbook073.png
         :figclass: image-inline

      --------------

      CASA regions are following the CASA 'crtf' standard as described
      in
      § `D <https://casa.nrao.edu/docs/cookbook/casa_cookbook015.html#chapter%3Aregionformat>`__.
      CASA regions can be used in all applications, including **tclean**
      and `Image Analysis
      Tasks <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis>`__.

      .. container:: info-box

         **NOTE:** The CASA image analysis tasks will determine how a
         region is projected on a pixel image. The current CASA
         definition is that when the center of a pixel is inside the
         region, the full pixel is considered to be included in the
         region.  If the center of the pixel is outside the region, the
         full pixel will be excluded. Note that the CASA viewer behavior
         is not entirely consistent and for rectangles it assumes
         that *any* fractional pixel coverage will include the entire
         pixel. For other supported shapes (ellipses and polygons),
         however, ithe viewer adheres to the 'center of pixel'
         definition, consistent with the image analysis tools and
         tasks. 

         For purely single-pixel work regions may not necessarily be the
         best choice and alternate methods may be preferable to using
         regions, eg. **ia.topixel**, **ia.toworld**, **ia.pixelvalue**.

      .. container:: alert-box

         **ALERT:** Some region file specifications are not recognized
         by the viewer, the viewer only supports rectangles (box),
         ellipses, and polygons.

      .. container:: info-box

         **NOTE**: A leading ’ann’ (short for annotation) to a region
         definition indicates that it is for visual overlay purposes
         only.

      .. container:: info-box

         **NOTE**: Whereas the region format is supported by all the
         data processing tasks, some aspects of the viewer
         implementation are still limited to rectangles, ellipses, and
         some markers. Full support for all region types is progressing
         with each CASA release.

      Once one or more regions are created, the Region Manager Panel
      becomes active (see `Region Manager <#FigRegionManager>`__). Like
      the Position Tracking and Animator Panels, this can be docked or
      detached from the main viewer display. It contains several tabs
      that can be used to adjust, analyze, and save or load regions.

      .. container:: info-box

         **NOTE**: Moving the mouse into a region will bring it into
         focus for the Spectral Profile or Histogram tools.

       

      .. rubric:: Region Creation, Selection, and Deletion
         :name: region-creation-selection-and-deletion

      Within the display area, you can draw regions or select positions
      using the mouse. Regions can be created with the buttons marked as
      'R' in the mouse tool bar, which can be found on the top-left
      (second row of buttons) in the `Viewer Display
      Panel <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/viewer-basics>`__.
      The viewer currently supports creation of rectangles, ellipses,
      polygons, and the point. As usual, a mouse button can be assigned
      to each button as indicated by the small black square in each
      button (marking the left, middle, or right mouse button). An
      example is shown in `Region Selection <#FigRegionSelection>`__.

      Regions can be selected by SHIFT+click, de-selected by pressing
      SHIFT+click again. The bottom of the Region Manager Panel features
      a slider to switch between regions in the image. Regions can be
      removed by hovering over and pressing ESC or by pressing the
      buttons to the right side of the slider where the first button
      (trash can icon) deletes all regions and the far right button (red
      circle with a white X) deletes the region that is currently
      displayed in the panel.

      --------------

      .. figure:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/casa_cookbook074.png/@@images/15c17c9c-dcae-4309-b667-5ab800747909.png
         :alt: casa_cookbook074.png
         :figclass: image-inline

      --------------

      Once regions are selected, they will feature little, skeletal
      squares in the corners of their boundary boxes. Selected regions
      can be moved by dragging with the mouse button and manually
      resized by grabbing the corners as handles. If more than one
      region is selected, all selected regions move together.

      The Rectangle Region drawing tool currently enables the full
      functionality of the various Region Manager tabs (see below) as
      well as:

      -  Region statistics reporting for images via double clicking
         (also shown in the Statistics tab of the Region Manager),
      -  Defining a region to be averaged for the spectral profile tool
         (accessed via the Tools:Spectral Profile drop down menu or
         "Open the Spectrum Profiler" icon),
      -  Flagging of MeasurementSets. Note that the Rectangle Region
         tool’s mouse button must also be double-clicked to confirm an
         MS flagging edit.
      -  Selecting Clean regions interactively
         (§ `5.3.5 <https://casa.nrao.edu/docs/cookbook/casa_cookbook006.html#section%3Aim.clean.interactive>`__)

      The Polygon Region and Ellipse Region drawing have the same uses,
      except that polygon region flagging of a MeasurementSet is not
      supported.

       

      .. rubric:: Region Positioning
         :name: region-positioning

      --------------

      .. figure:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/casa_cookbook075.png/@@images/9aabef94-1b25-4e1e-9f60-ece2cc6460b9.png
         :alt: casa_cookbook075.png
         :figclass: image-inline

         TypeFigure 
         IDregio editting
         Caption Region Editing: The Properties tab in the Region
         Manager can be used to manually adjust the location, width, and
         display style of the selected region.

      --------------

      With at least one region drawn, the Region Manager becomes active.
      Using the Properties tab, one can manually adjust the position,
      annotation, and display style of the region. The entries labeled
      "frames" set which planes of the image cube the region persists
      through (regions can have a depth associated with them and will
      only appear in the frames listed in this range). One can manually
      adjust the width and height and the center of the box in the
      chosen units. The 'selected' check box is an alternative way to
      the SHIFT+click to select a region. The 'annotation' checkbox will
      place the "ann" string in front of the region ASCII output –
      annotation regions are not be used for processing in, e.g. data
      analysis tasks. In the line and text tabs, one can set the style
      with which the region is displayed, the associated text, and the
      position and style of that text.

      .. container:: info-box

         **NOTE**: Updating the position of a region will update the
         spectral profile shown if the Spectral Profile tool is open and
         the histogram if the Histogram tool is open. The views are
         linked. Dragging a region or adjusting it manually with the
         Properties tab is a good way to explore an image.

       

      .. rubric:: Region Statistics
         :name: region-statistics

      --------------

      .. figure:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/casa_cookbook076.png/@@images/e5fcd597-6574-4e26-b958-40c81b14c12f.png
         :alt: casa_cookbook076.png
         :figclass: image-inline

      --------------

      One of the most useful features of defining a region is the
      ability to extract statistics characterizing the intensity
      distribution inside the region. You can see these in the
      Statistics tab of the of the Region Manager Panel (see `Region
      Statistics <#FigRegionStatistics>`__). This displays statistics
      for the current region in the current plane of the current image.
      When more than a single region is drawn, you can select them one
      by one and the Region Panel will update the statistics to reflect
      the currently selected region. All values are updated on the fly
      when the region is dragged across the image.

      A similar functionality can be achieved by double clicking inside
      of a region. This will send statistics information for this region
      in all registered images to the terminal, looking something like
      this:

      .. container:: casa-output-box

         | (IRC10216.36GHzcont.image) image
         |           Stokes         Velocity            Frame         
           Doppler        Frequency
         |                I -2.99447e+11km/s             LSRK           
           RADIO      3.63499e+10
         |   BrightnessUnit         BeamArea            
           Npts              Sum             Flux
         |          Jy/beam          36.2521            27547    
           1.087686e-01     3.000336e-03
         |             Mean              Rms          Std dev         
           Minimum          Maximum
         |     3.948473e-06     3.723835e-04     3.723693e-04   
           -1.045624e-03     9.968892e-03

      Listed parameters are Stokes, and the displayed channel Velocity
      with the associated Frame, Doppler and Frequency value. Sum, Mean,
      Rms, Std Deviation, Minimum, and Maximum value refer to those in
      the selected region and has the units as specified in
      BrightnessUnit. Npts is the number of pixels in the region, and
      BeamArea the beam size in pixels. FluxDensity is in Jy if the
      image is in Jy/beam. This is an easy way to copy and paste the
      statistical data to a program outside of CASA for further use.

      Taking the RMS of the signal-free portion of an image or cube is a
      good way to estimate the noise. Contrasting this number with the
      maximum of the image gives an estimate of the dynamic range of the
      image. The FluxDensity measurement gives a way to use the viewer
      to do very basic photometry.

       

      .. rubric:: Saving and Loading Regions
         :name: saving-and-loading-regions

      --------------

      .. figure:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/casa_cookbook077.png/@@images/d9419747-9bd9-4e33-abec-28e632c3faec.png
         :alt: casa_cookbook077.png
         :figclass: image-inline

      --------------

      The File tab in the Region Manager allows one to save or load
      selected regions, either individually or en masse. You can choose
      between CASA and DS9 region format. The default is a CASA region
      file (saved with a '.crtf' suffix, see
      § `D <https://casa.nrao.edu/docs/cookbook/casa_cookbook015.html#chapter%3Aregionformat>`__).
      The DS9 format does not offer the full flexibility and cannot
      capture Stokes and spectral axes. DS9 regions will only be usable
      as annotations in the viewer, they cannot be used for data
      processing in other CASA tasks. When saving regions, one can
      choose to save only the current region, all regions that were
      selected with SHIFT+click, or all regions that are visible on the
      screen.

      .. container:: info-box

         **NOTE**: The load functionality for this tab will only become
         available once at least one region exists. To load a region
         when no regions exist, use the `Region Manager <#viewerData>`__
         window.

       

       

      .. rubric:: The Region Fit
         :name: the-region-fit

      The Viewer can attempt to fit a two-dimensional Gaussian to the
      emission distribution inside the currently selected region. To
      attempt the fit, go to the Fit tab of the Region Manager and click
      the 'gaussfit' button in the bottom left of the panel. You can
      choose whether or not to fit a sky level (e.g., to account for a
      finite background, either astronomical, sky, or instrumental).
      After fitting the distribution, the Fit panel shows the results of
      the fit, the center, major and minor axis, and position angle of
      the Gaussian fit in pixels (I) and in world coordinates (W, RA and
      Dec). The detailed results of the fit will also appear in the
      terminal window, including a flag showing whether the fit
      converged.

       

      .. rubric:: The Region Histogram
         :name: the-region-histogram

      --------------

      .. figure:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization/casa_cookbook078.png/@@images/2c6f68de-4257-474f-988e-9148ac700bf1.png
         :alt: casa_cookbook078.png
         :figclass: image-inline

      .. container::

         +-----------------------------------+-----------------------------------+
         | Type                              | Figure                            |
         +-----------------------------------+-----------------------------------+
         | ID                                | Histogram                         |
         +-----------------------------------+-----------------------------------+
         | Caption                           | Histogram Tab: The histogram tab  |
         |                                   | in the Region Manager. Right      |
         |                                   | click to zoom. Hit SHIFT + Right  |
         |                                   | Click to adjust the details of    |
         |                                   | the histogram display.            |
         |                                   |                                   |
         |                                   | .. container::                    |
         |                                   |                                   |
         |                                   |                                   |
         +-----------------------------------+-----------------------------------+

         The viewer will automatically derive a histogram of the pixel
         values inside the selected region. This can be viewed using the
         Histogram tab of the of the Region Manager Panel. This is a
         pared down version of the full Histogram Tool. You can
         manipulate the details of the histogram plot by:

         1. Using the Right Click to zoom - either to the full range, a
            selected percentile, or a range that you have graphically
            selected by dragging the mouse.
         2. Hitting SHIFT + Right Click to open the histogram options.
            This lets you toggle between a logarithmic and linear
            y-axis, choose between a line, outline, or filled histogram,
            and adjust the number of bins.

         The histogram will update as you change the plane of the cube
         or shift between regions.

.. container:: section
   :name: viewlet-below-content-body
