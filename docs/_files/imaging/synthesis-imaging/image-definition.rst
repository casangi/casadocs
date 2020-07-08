.. container::
   :name: viewlet-above-content-title

Types of images
===============

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Ways to set up images (Cube vs MFS, single field, outliers, facets,
   Stokes planes ) and select data

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      The visibility data can be selected in many ways and imaged
      separately (e.g. one spectral window, one field, one channel).
      Data selection can also be done in the image-domain where the same
      data are used to create multiple image planes or multiple images
      (e.g. Stokes I,Q,U,V, or Taylor-polynomial coefficients or
      multiple-facets or outlier fields).

      Parameters for data selection and image definition together define
      the following options.

      +-------------------+-------------------------------------------------+
      | Data Selection    | Imaging Definition                              |
      +===================+=================================================+
      | Spectral Axis     | Cube (multiple channels)  or  MFS (single       |
      |                   | wideband channel) or MT-MFS (multi-term         |
      |                   | wideband images)                                |
      +-------------------+-------------------------------------------------+
      | Polarization axis | Stokes Planes ( I, IV, IQUV, pseudoI, RR, LL,   |
      |                   | XX, YY, etc )                                   |
      +-------------------+-------------------------------------------------+
      | Sky Coordinates   | Image shape, cell size, phasecenter, with or    |
      |                   | without outlier fields                          |
      +-------------------+-------------------------------------------------+
      | Data Selection    | One pointing  vs  multiple pointings for a      |
      |                   | mosaic, data from multiple MeasurementSets,     |
      |                   | etc.                                            |
      +-------------------+-------------------------------------------------+

      For the most part, the above axes are independent of each other
      and logical (and useful) combinations of them are allowed. For
      example, spectral cubes or wideband multi-term images can have
      outlier fields and/or mosaics. An example of a prohibited
      combination is the use of facets along with mosaics or
      a-projection as their algorithmic requirements contradict each
      other.

       

      .. rubric:: Types of Images
         :name: types-of-images-1

      This section illustrates the mapping from visibility data to
      gridded visibilities and then to the image domain for different
      image shape and type options.

       

      .. rubric:: Spectral Cubes :
         :name: spectral-cubes

      During gridding, N Data channels are binned onto M image channels
      using several optional interpolation schemes and doppler
      corrections to transform the data into the LSRK reference frame.
      When data from multiple channels are mapped to a single image
      channel, multi-frequency-synthesis gridding is performed within
      each image channel. More details are explained on the `Spectral
      Line
      Imaging <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/spectral-line-imaging>`__
      page. As can be seen from the diagram, parallelization for cube
      imaging can be naturally done by partitioning data and image
      planes by frequency for both major and minor cycles.

       

      |image1|

       

      .. rubric:: Continuum Images
         :name: continuum-images

      Wideband imaging involves mapping data from a wide range of
      frequency channels onto a single image channel.

      .. rubric:: Multi Frequency Synthesis (MFS) - Single Wideband
         Image
         :name: multi-frequency-synthesis-mfs---single-wideband-image

      Data from all selected data channels are mapped to a single
      broadband uv-grid using appropriate uvw coordinates, and then
      imaged. This is accessed via the " *specmode='mfs'* " option in
      the **tclean** task. Since there is only one uv grid and image,
      parallelization for continuum imagng is done only for the major
      cycle via data partitioning.

      |image2|

       

      .. rubric:: Multi-Term Multi Frequency Synthesis (MTMFS) - Taylor
         Coefficient Images
         :name: multi-term-multi-frequency-synthesis-mtmfs---taylor-coefficient-images

      An improvement to standard MFS that accounts for changes in
      spectral index as a function of sky position is available that
      uses Taylor weighted averages of data from all frequencies
      accumulated onto NTerms uv-grids before imaging. These
      Taylor-weighted residual images form the input for the minor cycle
      of the Multi-Term MFS deconvolution algorithm which performs a
      linear least squares fit (see `Deconvolution
      Algorithms <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/deconvolution-algorithms>`__
      section for more information) during deconvolution to obtain
      Taylor Coefficients per component (to represent sky spectra as
      polynomials in :math:`I` vs :math:`\nu`). This option is accessed
      via " *specmode='mfs'* and *deconvolver*\ ='mtmfs', *nterms=2.* "
      For the same data size as standard MFS (*nterms=1*), Multi-Term
      MFS will have :math:`N_t` times the gridding cost and number of
      images stored in memory.  Parallelization is again done only for
      the major cycle via data partitioning.

       |image3|

       

      .. rubric:: Polarization Planes
         :name: polarization-planes

      Data in the correlation basis are gridded onto separate planes per
      correlation, imaged, and then transformed into the Stokes basis. A
      special case for single plane Stokes I is implemented where data
      from both parallel hands are gridded onto a single uv-grid (to
      save memory). The point spread function is always taken from the
      Stokes I gridded weights. Images can be made for all Stokes
      parameters and correlation pairs (or all combinations possible
      with the selected data). This is an image-partitioning, where the
      same data are used to construct the different imaging products.
      Currently, if any correlation is flagged, all correlations for
      that datum are considered as flagged. An exception is the
      '*pseudoI*' option which allows Stokes I images to include data
      for which either of the parallel hand data are unflagged.

       

      |image4|  

      .. rubric:: Multiple Fields
         :name: multiple-fields

      A very large field of view can sometimes be imaged as a main field
      plus a series of (typically) smaller outlier fields. Imaging of
      fields with relatively few bright outlier sources can benefit from
      the overal reduction in image size that this option provides. 
      Instead of gridding the visibilities data onto a giant uv-grid,
      they are gridded onto multiple smaller images. Each sub-image is
      then deconvolved via separate minor cycles and their model images
      combined to predict model visibiliitles to subtract from the data
      in the next major cycle. The user must specify different phase
      reference centers for each image field.

      Different image shapes and gridding and deconvolution algorithms
      can be chosen for the different outlier fields. For example, one
      could apply single-plane wideband imaging on the main field, but
      employ multi-term MFS for an outlier field to account for
      artificial spectral index due to the wideband primary beam at its
      location. One can also combine MFS and Cube shapes for different
      outlier fields, or choose to run Multi-Scale CLEAN on the main
      field and Hogbom CLEAN on a bright compact outlier.    

      Overlapping fields are supported when possible (i.e. when the
      image types are similar enough across outliers) by always picking
      the "last" instance of that source in the list of outlier images
      in the order specified by the user. This convention implies that
      sources in the overlapping area are blanked in the "earlier" model
      images, such that those sources are not subtracted during the
      major cycles that clean those images.

       

      |image5|

       

      .. rubric:: Multiple Facets
         :name: multiple-facets

      Faceted imaging is one way of handling the w-term effect. A list
      of facet-centers is used to grid the data separately onto multiple
      adjacent sub-images. The sub images are typically simply subsets
      of a single large image so that the deconvolution can be performed
      as a joint image and a single model image is formed. The PSF to be
      used for deconvolution is picked from the first facet. The list of
      phase reference centers for all facets is automatically generated
      from user input of the number of facets (per side) that the image
      is to be divided into.

       

      |image6|

       

       

      .. rubric:: Mosaics
         :name: mosaics

      Data from multiple pointings can be combined to form a single
      large image. The combination can be done either before/during
      imaging or after deconvolution and reconstruction.

      .. rubric:: Stitched Mosaic
         :name: stitched-mosaic

      Data from multiple pointings are imaged and deconvolved
      separately, with the final output images being combined using a
      primary beam model as a weight. This is achieved by running the
      imaging task (**tclean**) separately per pointing, and combining
      them later on using the tool **im.linearmosaic**\ ().

       |image7|

       

      .. rubric:: Joint Mosaic
         :name: joint-mosaic

      Data taken with multiple pointings (and/or phase-reference
      centres) can be combined during imaging by selecting data from all
      fields together (multiple field-ids), and specifying only one
      output image name and one phase-reference center. If mosaic mode
      is enabled (*gridder='mosaic'* or *'awproject'*) attention is paid
      to the pointing centers of each data-fieldID during gridding.
      Primary-beam models are internally used during gridding (to
      effectively weight the images that each pointing would produce
      during a combination) and one single image is passed on to the
      deconvolution modules. 

       

      |image8|

       

       

.. container:: section
   :name: viewlet-below-content-body

.. |image1| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/figcube-1.png/@@images/728971c9-7e21-4e6c-8d0e-a6eb994d2281.png
   :class: image-inline
   :width: 460px
   :height: 257px
.. |image2| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/figcontinuum.png/@@images/7992efaf-23bb-49fd-9c7f-0934bada7ae6.png
   :class: image-inline
   :width: 429px
   :height: 216px
.. |image3| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/figcontinuummt.png/@@images/2da5c34e-7fca-4772-9d23-f00492b64ee4.png
   :class: image-inline
   :width: 447px
   :height: 285px
.. |image4| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/figstokes.png/@@images/9f2e7ca5-8b0b-446a-9b03-1befb8bf75c3.png
   :class: image-inline
   :width: 515px
   :height: 271px
.. |image5| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/figmultifield.png/@@images/73776a23-1bd0-4751-b1f2-42fa2b731a3d.png
   :class: image-inline
   :width: 479px
   :height: 249px
.. |image6| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/figfacets.png/@@images/609348cd-81e1-4c9a-a6a4-304d8573ba32.png
   :class: image-inline
   :width: 513px
   :height: 272px
.. |image7| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/figmosaicstitched-1.png/@@images/febd1763-839e-4c6a-beab-7db00f7eb30c.png
   :class: image-inline
   :width: 467px
   :height: 226px
.. |image8| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/figmosaicjoint-2.png/@@images/b895ac50-6d95-49f7-b7c6-4ea34e7ca674.png
   :class: image-inline
   :width: 448px
   :height: 218px
