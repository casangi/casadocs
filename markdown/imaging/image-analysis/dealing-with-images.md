

# Dealing with Images 

CASA tasks for image analysis

Image cubes in CASA can be manipulated and analyzed in various ways mainly using tasks with an \'im\' prefix and with the **image** CASA tool. Frequently, the tasks and tools handle CASA, FITS, and MIRIAD images, but we recommend using images in the CASA format. 

In the following pages, useful image analysis tasks are introduced that span import/export tasks, image information, reformatting, mathematical operations, and spatial and spectral fitting. Available image analysis tasks include: 

-   **imhead** --- summarize and manipulate the "header" information in a CASA image
-   **imsubimage** --- Create a (sub)image from a region of the image
-   **imcontsub** --- perform continuum subtraction on a spectral-line image cube
-   **imfit** --- image plane Gaussian component fitting
-   **immath** --- perform mathematical operations on or between images
-   **immoments** --- compute the moments of an image cube
-   **impv** --- generate a position-velocity diagram along a slit
-   **imstat** --- calculate statistics on an image or part of an image
-   **imval** --- extract the data and mask values from a pixel or region of an image
-   **imtrans** --- reorder the axes of an image or cube
-   **imcollapse** --- collapse image along one or more axes by aggregating pixel values along that axis
-   **imregrid** --- regrid an image onto the coordinate system of another image
-   **imreframe** --- change the frame in which the image reports its spectral values
-   **imrebin** --- rebin an image
-   **specsmooth** --- 1-dimensional smooth images in the spectral and angular directions
-   **imsmooth** --- 2-dimensional smooth images in the spectral and angular directions
-   **specfit** --- fit 1-dimensional Gaussians, polynomial, and/or Lorentzians models to an image or image region
-   **specflux** --- Report details of an image spectrum.
-   **plotprofilemap** --- Plot spectra at their position
-   **rmfit** --- Calculation of rotation measures
-   **spxfit** --- Calculation of Spectral Indices and higher order polynomials
-   **makemask** --- image mask handling
-   **slsearch** --- query a subset of the Splatalogue spectral line catalog
-   **splattotable** --- convert a file exported from Splatalogue to a CASA table
-   **importfits** --- import a FITS image into a CASA image format table
-   **exportfits** --- write out an image in FITS format

There are other tasks which are useful during image analysis. These include:

-   **viewer** --- there are useful region statistics and image cube slice and profile capabilities in the viewer

