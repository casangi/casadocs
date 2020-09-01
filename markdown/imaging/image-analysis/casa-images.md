

# CASA Images 

Structure of CASA images

CASA images are stored as tables and can be accessed with CASA tasks and tools. For example, images can be visualized with the CASA **viewer **(see \'[Image Cube Visualization](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization)\'), and image metadata can be listed and edited with the **imhead **task. CASA tasks and tools also enable further processing of images, including e.g. the computation of statistics including spectral indices and polarization properties, transformation onto different spatial coordinates, spatial resolutions, and spectral frames, and many other processes (see the following page, '[Dealing with Images](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/dealing-with-images)' for a description of tasks that operate on CASA images).

 

#### Image Headers

Image Headers contain metadata on the observation -- e.g. the observing date, pointing position, object observed, etc., and the resulting image -- e.g. the restoring beam size, image intensity units, spatial coordinate system, spectral parameters, stokes parameters, etc.  Header metadata tells the user what is in the image, and is used by the CASA **viewer** and other tasks to set the data array on the correct spatial and spectral coordinates, assign the intensity values correctly, and otherwise properly handle the data cube. 

Image Headers can be accessed and edited via the **imhead** task and the **msmd** tool.  Header data can also be inspected with the **casabrowser**.  See the page on \'[Image Headers](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/dealing-with-image-headers)\' for further details. 

 

#### Image Axes / Velocity Systems

CASA images typically have the following axis order (python indices are zero-based): Axis 0 = RA, 1 = DEC, 2 = Stokes, 3 = Frequency. The spatial axes can alternately contain GLON/GLAT or other coordinate systems.  The spectral axis of images created in CASA is always in frequency units. In addition, one or more velocity systems can be *added* to relabel the spectral axis. When images are imported into CASA from FITS files rather than generated within CASA itself, the above conventions may not apply. See the page on '[Image Import and Export](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/image-and-image-value-import-and-export)' for further details on importing and exporting FITS files.

The spatial and spectral axes in CASA images can be modified using CASA tasks and tools described in the '[Reformat Images](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/image-reformatting)' page. 

 

#### Image Masks

Internal Image Masks are stored as Boolean True/False cubes within the images themselves. There can be multiple masks stored in each data cube and one of them is defined to be the \'default\' mask. The default mask is the one visible when the image is displayed, e.g. in the **viewer**, and that is applied for operations on images. All masks have labels, such as mask0 etc. and they can be selected by specifying the image name followed by the mask name, separated by a colon. For example, \'mask1\' in \'image.im\' is used when specifying the image as \'image.im:mask1\'. Available masks can be listed with the task **makemask** which can also assign any mask as the default. The same task can also be used to export masks into separate CASA zero/non-zero cubes and to import such cubes as Boolean masks inside images. In addition, **makemask** enables the creation of masks from [image regions](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/region-files).  More information on masks is provided on the \'[Image Masks](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/image-masks)\' and \'[LEL Masks](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/lattice-expression-language-lel/lel-masks)\' CASAdocs pages. 

 

#### CASA Regions

CASA Regions can be specified through simple lists in LEL (e.g. region = 'box\[\[108, 108,\], \[148, 148\]\]') or through CASA Region Text Format (CRTF) files, which are text files that contain one or more regions with specific shapes (e.g. ellipses and rectangles), sizes, and other properties. These files can be used to specify the region of an image in which to operate, and they can easily be modified by the user or converted to CASA image masks (Boolean data cubes) using the **makemask** task. More information on CRTF files is available on the \'[Region Files](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/region-files)\' page.    

