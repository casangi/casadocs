.. container::
   :name: viewlet-above-content-title

Image Analysis in the Viewer
============================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Analysis Tools that are available in the Viewer

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: The Brightness Profile Tool
         :name: the-brightness-profile-tool

      The viewer allows the user to draw multiple line segments using
      the "Polyline drawing" button, and this feature can be used to
      display one-dimensional brightness profiles of images, such as
      shown in the `Spatial Profile Tool <#FigSlicerTool>`__. After
      double-clicking the last line segment, the 'Regions' dock will
      then display a preview of the slice in the Spatial Profile tab and
      the full "Spatial Profile Tool" can be launched from there by
      clicking the "Spatial Profile Tool" button. This "Spatial Profile
      Tool" panel allows one to select the interpolation method to
      connect the pixels, and a number count for the sampled pixels in
      between markers. 'Automatic' will show all pixels. The x-axis of
      the display can be either the distance along the slice or the X
      and Y coordinate projections (e.g. along RA and DEC). All segments
      are also listed at the bottom with their start and end
      coordinates, the distance and the position angles of each slice
      segment. The color tool can be used to give each segment a
      separate color.

      --------------

       

      .. figure:: ../../../../docs/cookbook/casa_cookbook090.png
         :alt: TypeFigure 
         IDCreate a short, unique name
         CaptionSpatial Profile Tool: The Spatial Profile tool shows the
         brightness distribution along line segments of an image.

         TypeFigure 
         IDCreate a short, unique name
         CaptionSpatial Profile Tool: The Spatial Profile tool shows the
         brightness distribution along line segments of an image.

      --------------

       

      .. rubric:: The Histogram Tool
         :name: the-histogram-tool

       

      --------------

      .. figure:: ../../../../docs/cookbook/casa_cookbook092.png
         :alt: TypeFigure
         IDCreate a short, unique name
         CaptionHistogram Tool: The Histogram tool can be accessed from
         the Main Toolbar or the Tools drop down menu. Details of the
         display and included pixels can be manipulated via the menus
         along the top of the window. The right hand panel allows one to
         attempt to fit a distribution to the histogram.

         TypeFigure
         IDCreate a short, unique name
         CaptionHistogram Tool: The Histogram tool can be accessed from
         the Main Toolbar or the Tools drop down menu. Details of the
         display and included pixels can be manipulated via the menus
         along the top of the window. The right hand panel allows one to
         attempt to fit a distribution to the histogram.

      --------------

      .. container::

         CASA can calculate and visualize a histogram of pixel values
         inside a region of interest. To examine this histogram, select
         Histogram from the Tools drop-down menu or the 'Histogram' icon
         in the Main Toolbar (looks like a comb). This opens the full
         Histogram Tool; more limited versions are accessible from the
         Region Manager Panel, the graphical color table manipulation
         tool, and the Collapse/Moments tool.

         The resulting Histogram Tool should look something like
         `Histogram Tool <#FigHistogramTool>`__. The menus along the top
         (or the corresponding mouse clicks) allow one to:

         -  Zoom to the full range, a selected percentile, or a
            graphical range.
         -  Change the display of the histogram to show a log axis,
            display as either a line plot, an outline, or a filled
            histogram. Change the number of bins in the histogram, or
            clear the plot (to start over).
         -  Configure what data are fed into the histogram. You can use
            this menu to tell the histogram to track the channel
            currently selected in the main Viewer Display Panel (click
            the "Track Channel" box) or to integrate across some range
            of channels (defaulting to the whole image). You can also
            switch the 2-D footprint used between the whole Image, the
            Selected Region, and All Regions.
         -  Save (via the disk icon) an image of the histogram to a
            graphical file on disk.

         The Histogram Tool also allows you to fit the distribution
         using either a Gaussian or a Poisson distribution, for example
         to estimate the noise in the image (a Gaussian will be a good
         choice to describe the noise in most radio data cubes). You can
         specify initial estimates or let the program generate initial
         guesses. The fit is then overplotted on the histogram (colors
         can be adjusted by clicking the color wheel icon in the
         toolbar) and details of the fit are printed to the text window
         below the fit button.

      .. container::

          
         .. rubric:: The Two-Dimensional Fitting Tool
            :name: the-two-dimensional-fitting-tool

          

         --------------

         .. figure:: ../../../../docs/cookbook/casa_cookbook093.png
            :alt: TypeFigure 
            IDCreate a short, unique name
            CaptionTwo-Dimensional Fitting Tool: The interface to the
            two dimensional fitting tool (accessed via Tools:Fit...or
            the blue circles icon in the Main Toolbar). The interface
            allows you to specify and automatically generate (Find
            Sources) initial estimates, to specify the range of pixel
            values to be included in the fit, and to specify the output
            (log file, residual image, and visualization). Click Fit to
            start the fit.

            TypeFigure 
            IDCreate a short, unique name
            CaptionTwo-Dimensional Fitting Tool: The interface to the
            two dimensional fitting tool (accessed via Tools:Fit...or
            the blue circles icon in the Main Toolbar). The interface
            allows you to specify and automatically generate (Find
            Sources) initial estimates, to specify the range of pixel
            values to be included in the fit, and to specify the output
            (log file, residual image, and visualization). Click Fit to
            start the fit.

         --------------

          

         CASA can fit two-dimensional Gaussians to an intensity
         distribution, and the Two-Dimensional Fitting Tool in the
         Viewer exposes this functionality interactively. This tool,
         accessed by the 'blue circles' icon in the Main Toolbar or the
         Tools:Fit menu item, has an interface like that shown in
         `Two-Dimensional Fitting Tool <#FigTwoDFitting>`__. The
         interface exposes several options:

         1. You can select whether to fit only the selected region or
            the whole image plane and specify which channel of the cube
            you want to operate on.

            .. container:: info-box

               **NOTE**: The two dimensional fitter only operates on a
               single channel at a time.

         2. Initial Estimates: The box in the top left corner allows the
            user to specify initial estimates by feeding in a file. The
            easiest way to make an appropriate file is to edit an
            existing one. Even easier, you can use the Find Sources
            button to automatically generate a temporary file of initial
            estimates.
         3. Pixel Range: You can choose to only include a certain range
            of pixel intensity values in the fit. For example, you might
            choose to only fit Gaussians to pixels a few times above the
            measured noise level. You can use the Specify Graphically
            button to bring up an interactive histogram of the region (a
            reduced functionality version of the full Histogram Tool).
         4. Output: You can choose to save the output of the fit as a
            file to the specified directory and to subtract the fit from
            the image and to subtract the fit from the original,
            creating a Residual Image that gets stored as a CASA image
            and automatically loaded into the viewer. This gives a way
            to tell how well your fit describes the total emission.
         5. Visualization: You can toggle whether the fit is displayed
            on the viewer or not and change the color of the marker.

         Click Fit to start the fit. If the fit does not converge, try
         improving your initial estimates and fitting again.

.. container:: section
   :name: viewlet-below-content-body
