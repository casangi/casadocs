.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Masks for Deconvolution
=======================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Descriptions of mask types and how to create them

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      For the most careful imaging, you will want to restrict the region
      over which you allow CLEAN components to be found by using a mask.
      This mask is generally referred to as a clean mask.

      .. rubric:: Creating a **clean** mask:
         :name: creating-a-clean-mask

      There are several different ways to specify a clean mask,
      including:

      #. A text-based region. The `CASA region text
         format <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/region-file-format>`__
         can be used to define clean regions either by specifying the
         region directly in the **tclean** command or by using an ASCII
         text file containing the specifications. You can use the viewer
         to save a region formatted according to the CRTF specification.
         To do this, an image must already exist to serve as a reference
         or template to create the mask image or the region.
      #. An image consisting of only 1 (valid) and 0 (invalid) pixel
         values. Such images can be generated or modified using tasks
         such as **makemask**. The mask has to have the same shape
         (number of pixels, velocity, and Stokes planes) as the output
         image. An exception are single velocity and/or single Stokes
         plane masks. They will be expanded to cover all velocity and/or
         Stokes planes of the output cube. 
      #. An automatically generated mask. There are several experimental
         algorithms available in **tclean** for automatically masking
         emission during the deconvolution cycle. See the `automasking
         section <#automasking>`__ below for more details (does not work
         in the old **clean** task).
      #. A mask created by **tclean** while interactively cleaning using
         the viewer. You can combine this method with the options above
         to create an initial clean mask and modify it
         interactively. Please be aware that when running tclean
         interactively, the viewer is accessible during a major cycle,
         and the mask can be inadvertently by changed during the active
         clean cycle, although the new mask is not registered until the
         next major cycle. Also note that interactive **tclean** only
         works when a region or mask is selected in the CASA Viewer. If
         the entire image should be cleaned, please draw a box around
         the entire image. There is a known bug that when a region is
         first selected, and then de-selected to produce an empty mask
         (filled with zeros), the CASA Viewer that runs interactive
         tclean will still allow you to proceed, and tclean will detect
         an empty mask and stop. Please always mark a region/mask to
         continue interactive tclean, and do not forget to double-click
         inside the green contours to select the region.

      However they are created, the masks are all converted (as
      necessary) and stored as CASA images consisting of the pixel
      values of 1 and 0. When mask files are read in and have undefined
      values, these values are treated as 1s by CASA. Mixed types of
      masks can be specified in the **tclean** task. 

      .. container:: info-box

         In CASA, the term, 'mask' for an image is used in two different
         contexts. One is used for CASA images/image analysis is a T/F
         mask (pixel mask), which can be embedded in the parent CASA
         image.  The 'mask' used in imaging normally refers to a 1/0
         image, which is directly used to define deconvolution region(s)
         (or set a 'clean mask') in the **tclean** task.

      .. rubric:: Automasking
         :name: automasking

      The **tclean** task has an option to generate clean masks
      automatically during the deconvolution process by applying flux
      density thresholds to the residual image. Currently
       "auto-multithresh" is the automasking algorithm available
      in **tclean**. Previously available experimental alogrithms,
      *"*\ auto-thresh" and "auto-thresh2" were removed in CASA 5.4. The
      "auto-multithresh" algorithm can be selected via the *usemask*
      parameter. For this algorithm, the mask will be updated at
      the beginning of a minor cycle based on the current residual
      image. The algorithm uses multiple thresholds based on the noise
      and sidelobe levels in the residual image to determine what
      emission to mask. It also have functionality to remove ("prune")
      small mask regions that are unlikely to be real astronomical
      emission. A more detailed description of the algorithm are given
      below and in `[1] <#cit>`__ .

      .. rubric:: *"*\ auto-multithresh"
         :name: auto-multithresh

      This algorithm is intended to mimic what an experienced user would
      do when manually masking images while interactively cleaning. The
      parameters *sidelobethreshold* and *noisethreshold* control the
      initial masking of the image. The *sidelobethreshold* indicates
      the minimum sidelobe level that should be masked, while the
      *noisethreshold*  indicates the minimum signal-to-noise value that
      should be masked. The threshold used for masking is the greater of
      the two values calculated for each minor cycle based on the rms
      noise and sidelobe levels in the current residual image. 

      Regions smaller than a user-specified fraction of the beam can be
      removed, or "pruned", from the mask. The size of the region is
      defined as the number of contiguous pixels in the region. The
      figure below shows an example of the pruning process.

      | 
      | |image1|

      +---------+-----------------------------------------------------------+
      | Type    | Figure                                                    |
      +---------+-----------------------------------------------------------+
      | ID      | masks-for-deconvolution-fig-prune                         |
      +---------+-----------------------------------------------------------+
      | Caption | Figure 1 - An example of the pruning process. The image   |
      |         | on the left shows the original threshold mask, while the  |
      |         | image on the right shows the resulting mask after all     |
      |         | regions smaller than a user-specified fraction of the     |
      |         | beam area have been removed.                              |
      +---------+-----------------------------------------------------------+

      | 
      | The resulting masks are all convolved with a Gaussian that is a
        multiple of the synthesized beam size, which is controlled by
        the parameter *smoothfactor*. Only values above some fraction of
        the smoothed Gaussian peak are retained, which is defined via
        the *cutthreshold* parameter. Note that *cutthreshold* is
        defined as a fraction of the smoothed Gaussian peak, not as an
        absolute value. This procedure ensures that sources are not
        masked too tightly, i.e., there is a margin between the emission
        and the mask.  Note that *smoothfactor* and *cutthreshold* are
        related. A large *smoothfactor* and high *cutthreshold* can give
        a similar region to a lower *smoothfactor* but lower
        *cutthreshold*. Note that setting the cuttreshold too
        high (>~0.2) will tend to remove faint regions. 

      |An image showing a threshold mask, a smoothed threshold image,
      and the final smoothed threshold mask created by cutting above
      particular fraction of the peak threshold..|

      +---------+-----------------------------------------------------------+
      | Type    | Figure                                                    |
      +---------+-----------------------------------------------------------+
      | ID      | masks-for-deconvolution-fig-smooth-and-cut                |
      +---------+-----------------------------------------------------------+
      | Caption | Figure 2 - An example of the process used to ensure that  |
      |         | sources are not masked too tightly. The left hand image   |
      |         | shows the initial threshold mask. The middle image shows  |
      |         | the threshold mask convolved with a Gaussian. The right   |
      |         | image shows the final threshold mask where only emission  |
      |         | above some fraction of the peak in the smoothed mask is   |
      |         | retained. The final mask is larger than the original      |
      |         | threshold mask and better encapsulates the emission.      |
      +---------+-----------------------------------------------------------+

      The initial threshold mask can be expanded down to lower
      signal-to-noise via binary dilation. This feature is particularly
      useful when there is significant faint extended emission. The
      *lownoisethreshold* parameter is used to create a mask of the low
      signal-to-noise emission, which we refer to as the constraint
      mask. Th previous total positive mask is expanded (or grown) via
      an operation known as binary dilation, which expands each mask
      region using a structuring element (also known as a kernel).
      Currently the structuring element is fixed with a 3x3 matrix with
      the diagonal element being 0. We use a constraint mask based on a
      low signal-to-noise threshold to limit the expansion of the mask
      to regions within the *lownoisethreshold*. Only the regions in the
      constraint mask that touch the previous mask are retained in the
      final constraint mask. Then the final constraint mask is pruned,
      smoothed, and cut using the same method as the initial threshold
      mask. 

      The sub-parameter *growiterations* gives a maximum number of
      iterations used to "grow" the previous masking into the low
      signal-to-noise mask, which can speed up masking of large cubes at
      the expense of possibly undermasking extended emission. The
      sub-parameter *dogrowprune* can be used to turn off pruning for
      the constraint mask, which also may also speed up this process.

      |image2|

      +---------+-----------------------------------------------------------+
      | Type    | Figure                                                    |
      +---------+-----------------------------------------------------------+
      | ID      | masks-for-deconvolution-fig-grow                          |
      +---------+-----------------------------------------------------------+
      | Caption | Figure 3 - An example of how the masks are expanded into  |
      |         | low signal-to-noise regions. The top row shows the binary |
      |         | dilation process. Left: The low signal-to-noise threshold |
      |         | mask used as a constraint mask. Middle: The final mask    |
      |         | from the previous clean cycle. Right: The result of       |
      |         | binary dilating the mask from the previous clean major    |
      |         | cycle into the constraint mask. The bottom left           |
      |         | image shows the binary dilated mask multiplied by the     |
      |         | constraint mask to pick out only those regions in the     |
      |         | constraint mask associated with the previous clean mask.  |
      |         | The bottom middle image shows the final pruned, smoothed, |
      |         | and cut mask.                                             |
      +---------+-----------------------------------------------------------+

      There is also an experimental absorption masking feature
      controlled by the sub-parameter *negativethreshold*, which has an
      analogous definition to *noisethreshold*. This feature assumes
      that the data has been continuum subtracted. Absorption masking
      can be turned off by setting the *negativethreshold* vaue to 0
      (the default). Note that the negative and positive threshold masks
      are tracked separately and that the negative mask is not pruned or
      expanded into lower signal-to-noise regions.

      Finally, all the masks (initial threshold mask, negative mask, low
      noise threshold mask) are added together with the mask from the
      previous major cycle to form the final mask.

      All the operations described above, including obtaining image
      statistics, are done per spectral plane for spectral line imaging.
      If a channel is masked using the noise threshold and the resulting
      final mask is zero, then future auto-masking iterations will skip
      that channel. The *minpercentchange* parameter is an experimental
      parameter that controls whether future masks are calculated for a
      particular channel if the mask changes by less than n% after major
      cycle where the cyclethreshold is equal to the threshold for the
      clean. In general, we recommend *minpercentchange* to be set to
      -1.0 (turned off).

      The *verbose* parameter records information to the log on whether
      a channel is included in the masking, the image noise and peak,
      the threshold used and it's value, the number of regions found in
      the initial mask and how many were pruned, the number of region
      found in the low noise threshold mask and how many of those are
      pruned, and the number of pixels in the negative mask. This
      information is helpful for optimizing parameters for different
      imaging cases as well as general debugging.

      .. rubric:: Algorithm In Detail
         :name: algorithm-in-detail

      #. Calculate threshold values based on the input parameters.

         a. sidelobeThresholdValue = sidelobeThreshold \* sidelobeLevel
            \* peak in residual image
         b. noiseThresholdValue =  noiseThreshold \* rms in residual
            image
         c. lowNoiseThresholdValue = lowNoiseThreshold \* rms in
            residual image
         d. negativeThresholdValue = negativeThreshold \* rms in
            residual image

      #. Create the threshold mask.

         a. maskThreshold =
            max(sidelobeThresholdValue,noiseThresholdValue)
         b. Create threshold mask by masking all emission greater than
            maskThreshold.
         c. Prune regions smaller than minBeamFrac times the beam area
            from threshold mask.
         d. Smooth the mask image by smoothFactor \* (beam size).
         e. Mask everything above cutThreshold \* the peak in the
            smoothed mask image.

      #. Expand the mask to low signal-to-noise.

         a. lowMaskThreshold =
            max(sidelobeThresholdValue,lowNoiseThresholdValue)
         b. Create constraintMask by masking all emission greater
            than lowMaskThreshold.
         c. Use binary dilation expand the previous clean cycle mask
            into the constraintMask.
         d. Create the low S/N mask by retaining only the regions in the
            constraintMask that are connected to the previous clean
            cycle mask.
         e. Prune [can turn this off with *dogrowprune*\ =False], cut,
            and smooth the low S/N mask the same way as was done for the
            threshold mask.

      #. Mask the absorption (experimental)

         a. If negativethreshold >0.0:

            #. negativeMaskThreshold =  -  max(negativeThresholdValue,
               sidelobeThresholdValue)
            #. mask negative pixels with values <=
               negativeThresholdValue
            #. Cut and smooth the absorption mask the same way as was
               done for the threshold mask.

      #. Add the threshold mask, the low S/N mask, the absorption mask,
         and the mask from previous clean cycle together.

       

      .. rubric:: Noise Estimation 
         :name: noise-estimation

      Prior to CASA 5.5, "auto-multithresh" estimated the noise per
      channel using the median absolute deviation (MAD), scaled to match
      a Gaussian distribution. This noise estimate is computationally
      fast, but may be less accurate for cases where the emission covers
      a large fraction (nominally 50%) of the field of view. In CASA
      5.5, a new noise estimate was introduced, which uses a more
      complex and computationally expensive noise estimate. This
      estimate may yield more accurate estimates of the noise in the
      case where emission covers a significant fraction of the field of
      view. The procedure is as follows. If there is no mask,
      remove pixels from the noise distribution via Chauvenet's
      criterion `[2] <#cit>`__  `[3] <#cit>`__ and then estimate the
      noise using the remaining pixels via the median absolute
      deviation. If there is a mask, then calculate the noise from the
      pixels outside the clean mask and inside the primary beam mask,
      which we refer to as the masked MAD. All MAD values are scaled to
      match a Gaussian distribution.

      The parameter fastnoise is set to True by default. 

      .. rubric:: Polarization Data
         :name: polarization-data

      As of CASA 5.6, auto-multithresh now functions with polarization
      data. It applies the same algorithms to the Stokes QUV images as
      used for the Stokes I image. This means that the full masking
      process is applied to the positive emission (including the prune
      and grow steps), but that the masking of the negative emission
      only includes the initial threshold mask (no prune or grow).

      .. rubric:: A Note on Input Parameters
         :name: a-note-on-input-parameters

      The default "auto-multithresh" parameters have been optimized for
      the ALMA 12m array in its more compact configurations. The
      parameters may need to be modified for other input cases, e.g.,
      ALMA 12m long baseline data, ALMA 7m array data, and  VLA data.
      The main parameters to explore are *noisethreshold*,
      *sidelobethreshold*, *lownoisethreshold*, *minbeamfrac*, and
      *negativethreshold* (if you have absorption). We do not recommend
      changing the *cutthreshold* and *smoothfactor* parameters from
      their default values. The *dogrowprune* and *growiterations*
      parameters are primarily used to improve the speed of the
      algorithm for large cubes.

       

       

      +-----------------+---------------------------------------------------+
      | Citation Number | 1                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Kepley et al. 2020, Publications of the           |
      |                 | Astronomical Society of the Pacific, 132, 024505  |
      +-----------------+---------------------------------------------------+

       

      =============== ===================================================
      Citation Number 2
      Citation Text    Peirce, B. 1852, The Astronomical Journal, 2, 161.
      =============== ===================================================

      .. container::

         +-----------------------------------+-----------------------------------+
         | Citation Number                   | 3                                 |
         +-----------------------------------+-----------------------------------+
         | Citation Text                     | .. container::                    |
         |                                   |                                   |
         |                                   |    Chauvenet, W. A Manual of      |
         |                                   |    Spherical and Practical        |
         |                                   |    Astronomy, Volume II (London,  |
         |                                   |    UK: Dover; reprinted in 1960   |
         |                                   |    based on fifth revised and     |
         |                                   |    corrected edition 1891),       |
         |                                   |    558–566                        |
         +-----------------------------------+-----------------------------------+

         | 

.. container:: section
   :name: viewlet-below-content-body

.. |image1| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/prune_figure-3.png/@@images/60c65f22-24eb-4130-839e-113f69d9a734.png
   :class: image-inline
.. |An image showing a threshold mask, a smoothed threshold image, and the final smoothed threshold mask created by cutting above particular fraction of the peak threshold..| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/smooth_and_cut.png/@@images/7a47f556-6879-4d32-8112-ff7da03d9c7b.png
   :class: image-inline
.. |image2| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/grow_mask-1.png/@@images/6cb496d8-7f7e-4e0e-9c01-c6ccdee17111.png
   :class: image-inline
