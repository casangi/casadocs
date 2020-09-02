

# Types of images 

Ways to set up images (Cube vs MFS, single field, outliers, facets, Stokes planes ) and select data

The visibility data can be selected in many ways and imaged separately (e.g. one spectral window, one field, one channel). Data selection can also be done in the image-domain where the same data are used to create multiple image planes or multiple images (e.g. Stokes I,Q,U,V, or Taylor-polynomial coefficients or multiple-facets or outlier fields).

Parameters for data selection and image definition together define the following options.

    Data Selection                                             Imaging Definition
  ------------------- ----------------------------------------------------------------------------------------------------
     Spectral Axis     Cube (multiple channels)  or  MFS (single wideband channel) or MT-MFS (multi-term wideband images)
   Polarization axis                      Stokes Planes ( I, IV, IQUV, pseudoI, RR, LL, XX, YY, etc )
    Sky Coordinates                   Image shape, cell size, phasecenter, with or without outlier fields
    Data Selection        One pointing  vs  multiple pointings for a mosaic, data from multiple MeasurementSets, etc.

For the most part, the above axes are independent of each other and logical (and useful) combinations of them are allowed. For example, spectral cubes or wideband multi-term images can have outlier fields and/or mosaics. An example of a prohibited combination is the use of facets along with mosaics or a-projection as their algorithmic requirements contradict each other.

 

# Types of Images

This section illustrates the mapping from visibility data to gridded visibilities and then to the image domain for different image shape and type options.

 

## Spectral Cubes :

During gridding, N Data channels are binned onto M image channels using several optional interpolation schemes and doppler corrections to transform the data into the LSRK reference frame. When data from multiple channels are mapped to a single image channel, multi-frequency-synthesis gridding is performed within each image channel. More details are explained on the [Spectral Line Imaging](https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/spectral-line-imaging) page. As can be seen from the diagram, parallelization for cube imaging can be naturally done by partitioning data and image planes by frequency for both major and minor cycles.

 

![7712e396f0309a7d9309a77cfa8fc6fc2f8a0be9](media/7712e396f0309a7d9309a77cfa8fc6fc2f8a0be9.png){.image-inline width="460" height="257"}

 

## Continuum Images

Wideband imaging involves mapping data from a wide range of frequency channels onto a single image channel.

### Multi Frequency Synthesis (MFS) - Single Wideband Image

Data from all selected data channels are mapped to a single broadband uv-grid using appropriate uvw coordinates, and then imaged. This is accessed via the \" *specmode=\'mfs\'* \" option in the **tclean** task. Since there is only one uv grid and image, parallelization for continuum imagng is done only for the major cycle via data partitioning.

![51885b785409ea1448f61c399eb82e53f0a54729](media/51885b785409ea1448f61c399eb82e53f0a54729.png){.image-inline width="429" height="216"}

 

### Multi-Term Multi Frequency Synthesis (MTMFS) - Taylor Coefficient Images

An improvement to standard MFS that accounts for changes in spectral index as a function of sky position is available that uses Taylor weighted averages of data from all frequencies accumulated onto NTerms uv-grids before imaging. These Taylor-weighted residual images form the input for the minor cycle of the Multi-Term MFS deconvolution algorithm which performs a linear least squares fit (see [Deconvolution Algorithms](https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/deconvolution-algorithms) section for more information) during deconvolution to obtain Taylor Coefficients per component (to represent sky spectra as polynomials in $I$ vs $\nu$). This option is accessed via \" *specmode=\'mfs\'* and *deconvolver*=\'mtmfs\', *nterms=2.* \" For the same data size as standard MFS (*nterms=1*), Multi-Term MFS will have $N_t$ times the gridding cost and number of images stored in memory.  Parallelization is again done only for the major cycle via data partitioning.

 ![f068a79a636e070fea341be6847ccefc61b1c6d5](media/f068a79a636e070fea341be6847ccefc61b1c6d5.png){.image-inline width="447" height="285"}

 

## Polarization Planes

Data in the correlation basis are gridded onto separate planes per correlation, imaged, and then transformed into the Stokes basis. A special case for single plane Stokes I is implemented where data from both parallel hands are gridded onto a single uv-grid (to save memory). The point spread function is always taken from the Stokes I gridded weights. Images can be made for all Stokes parameters and correlation pairs (or all combinations possible with the selected data). This is an image-partitioning, where the same data are used to construct the different imaging products. Currently, if any correlation is flagged, all correlations for that datum are considered as flagged. An exception is the \'*pseudoI*\' option which allows Stokes I images to include data for which either of the parallel hand data are unflagged.

 

![2505ddafc4936705143e6210e997ffee48acf231](media/2505ddafc4936705143e6210e997ffee48acf231.png){.image-inline width="515" height="271"}  

## Multiple Fields

A very large field of view can sometimes be imaged as a main field plus a series of (typically) smaller outlier fields. Imaging of fields with relatively few bright outlier sources can benefit from the overal reduction in image size that this option provides.  Instead of gridding the visibilities data onto a giant uv-grid, they are gridded onto multiple smaller images. Each sub-image is then deconvolved via separate minor cycles and their model images combined to predict model visibiliitles to subtract from the data in the next major cycle. The user must specify different phase reference centers for each image field.

Different image shapes and gridding and deconvolution algorithms can be chosen for the different outlier fields. For example, one could apply single-plane wideband imaging on the main field, but employ multi-term MFS for an outlier field to account for artificial spectral index due to the wideband primary beam at its location. One can also combine MFS and Cube shapes for different outlier fields, or choose to run Multi-Scale CLEAN on the main field and Hogbom CLEAN on a bright compact outlier.    

Overlapping fields are supported when possible (i.e. when the image types are similar enough across outliers) by always picking the \"last\" instance of that source in the list of outlier images in the order specified by the user. This convention implies that sources in the overlapping area are blanked in the \"earlier\" model images, such that those sources are not subtracted during the major cycles that clean those images.

 

![5c981ca63d45b330b41ebcd4e67b4607d47d47a5](media/5c981ca63d45b330b41ebcd4e67b4607d47d47a5.png){.image-inline width="479" height="249"}

 

## Multiple Facets

Faceted imaging is one way of handling the w-term effect. A list of facet-centers is used to grid the data separately onto multiple adjacent sub-images. The sub images are typically simply subsets of a single large image so that the deconvolution can be performed as a joint image and a single model image is formed. The PSF to be used for deconvolution is picked from the first facet. The list of phase reference centers for all facets is automatically generated from user input of the number of facets (per side) that the image is to be divided into.

 

![08fa4167833923aa5e120ade2d66c24de84c3a4a](media/08fa4167833923aa5e120ade2d66c24de84c3a4a.png){.image-inline width="513" height="272"}

 

 

# Mosaics

Data from multiple pointings can be combined to form a single large image. The combination can be done either before/during imaging or after deconvolution and reconstruction.

## Stitched Mosaic

Data from multiple pointings are imaged and deconvolved separately, with the final output images being combined using a primary beam model as a weight. This is achieved by running the imaging task (**tclean**) separately per pointing, and combining them later on using the tool **im.linearmosaic**().

 ![64ef9fbb940c0eefc34e96c18d0ac726f56ee982](media/64ef9fbb940c0eefc34e96c18d0ac726f56ee982.png){.image-inline width="467" height="226"}

 

## Joint Mosaic

Data taken with multiple pointings (and/or phase-reference centres) can be combined during imaging by selecting data from all fields together (multiple field-ids), and specifying only one output image name and one phase-reference center. If mosaic mode is enabled (*gridder=\'mosaic\'* or *\'awproject\'*) attention is paid to the pointing centers of each data-fieldID during gridding. Primary-beam models are internally used during gridding (to effectively weight the images that each pointing would produce during a combination) and one single image is passed on to the deconvolution modules. 

 

![0886eddf2dfd68343993dca5b5c02affe00ccc54](media/0886eddf2dfd68343993dca5b5c02affe00ccc54.png){.image-inline width="448" height="218"}

 

 

