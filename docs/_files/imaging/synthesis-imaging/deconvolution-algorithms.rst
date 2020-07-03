.. container::
   :name: viewlet-above-content-title

Deconvolution Algorithms
========================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Minor cycle algorithms (Hogbom, Clark, Multi-Scale, Multi-Term)

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Deconvolution refers to the process of reconstructing a model of
      the sky brightness distribution, given a dirty/residual image and
      the point-spread-function of the instrument. This process is
      called a deconvolution because under certain conditions, the
      dirty/residual image can be written as the result of a convolution
      of the true sky brightness and the PSF of the instrument.
      Deconvolution forms the minor cycle of iterative image
      reconstruction in CASA.

      |image1|

      +---------+-----------------------------------------------------------+
      | Type    | Figure                                                    |
      +---------+-----------------------------------------------------------+
      | ID      | FigConvolution.png                                        |
      +---------+-----------------------------------------------------------+
      | Caption | The observed image (left) is the result of a convolution  |
      |         | of the PSF (middle) and the true sky brightness           |
      |         | distribution (right).                                     |
      +---------+-----------------------------------------------------------+

      The image reconstruction framework is based on Cotton-Schwab
      major/minor cycles `[1] <#cit>`__. Within this system, the minor
      cycle algorithm operates largely in the image domain starting with
      a PSF and a residual image (i.e. the gradient of chi-square or the
      right hand side of the normal equations). The output is an
      incremental model image that defines the 'step' taken during the
      chi-square minimization process. In the next major cycle, the
      contribution of this model image is subtracted out of the list of
      visibilities and the result is regridded and transformed to
      produce a new residual image. This approach allows for a practical
      trade-off between the efficiency of operating in the image domain
      (or simply with gridded visibilities) and the accuracy that comes
      from returning to the ungridded list of visibilities after every
      'step'. It also allows for minor cycle algorithms that have their
      own internal optimization schemes (i.e. they need not be strict
      chi-square minimizations) with their own control parameters. Note
      that any minor cycle algorithm that can operate on gridded
      visibilities can fit into this framework. The inputs to the minor
      cycle algorithm are the residual image, psf and perhaps a starting
      model. Outputs are a model image.

       

      .. container:: content

         .. rubric:: CLEAN Algorithm
            :name: title0

         The CLEAN algorithm forms the basis for most deconvolution
         algorithms used in radio interferometry. The peak of the
         residual image gives the location and strength of a potential
         point source. The effect of the PSF is removed by subtracting a
         scaled PSF from the residual image at the location of each
         point source, and updating the model. Many such iterations of
         finding peaks and subtracting PSFs form the minor cycle.

         There are several variants of the CLEAN algorithm. Some operate
         with a delta function sky model and others with a multi-scale
         sky model. In all cases, the the sky brightness is
         parameterized in a sparse basis such that in practice, the
         minor cycle algorithm needs only to search for the location and
         amplitude of peaks. This makes it efficient. For example,
         fields of compact sources are best represented by delta
         function locations and amplitudes. Extended emission is modeled
         as a linear combination of components of different scale sizes
         and transformed into a multi-scale basis where again, delta
         functions are all that are required to mark the location and
         amplitude of blobs of different sizes. Multi-term algorithms
         for wideband imaging model the sky brightness and its spectrum
         simultaneously, using coefficients of a Taylor polynomial as a
         sparse representation of a smooth spectrum. In this case, the
         location of each (multi-scale) component is chosen via a search
         and the values of the Taylor coefficients for that component
         are solved for via a direct linear least squares calculation.

          

      .. container:: content

         .. rubric:: Hogbom
            :name: title1

         Hogbom CLEAN `[2] <#cit>`__ operates with a point-source model
         of the sky brightness distribution. The minor cycle searches
         for the location and amplitude of components and then subtracts
         a scaled and shifted version of the full PSF to update the
         residual image for each point source. This algorithm is
         efficient in that delta functions are optimal for fields of
         compact sources, but susceptible to errors due to inappropriate
         choices of imaging weights, especially if the PSF has high
         sidelobes. It uses the full PSF during its update step to
         ensure that the next residual is as accurate as possible, but
         this can get compute intensive.  

         In its original form, the Hogbom algorithm operated just once
         in the image domain without new residuals being computed via a
         major cycle. In our CASA Imager implementation, it is treated
         as a minor cycle where one periodically does major cycles as
         well (to guard against minor cycle evolution that is not
         strictly constrained by the ungridded visibilities).

         Since Hogbom CLEAN uses only delta functions, it is most
         appropriate for fields of isolated point sources. It will incur
         errors when imaging extended emission and this is typically
         seen as a mottled appearance of smooth structure and the
         presence of correlated residuals.

          

      .. container:: content

         .. rubric:: Clark
            :name: title2

         Clark CLEAN `[3] <#cit>`__ also operates only in the
         image-domain, and uses a point-source model. There are two main
         differences from the Hogbom algorithm. The first is that it
         does its residual image updates using only a small patch of the
         PSF. This is an approximation that will result in a significant
         speed-up in the minor cycle, but could introduce errors in the
         image model if there are bright sources spread over a wide
         field-of-view where the flux estimate at a given location is
         affected by sidelobes from far-out sources. The second
         difference is designed to compensate for the above. The
         iterations are stopped when the brightest peak in the residual
         image is below the first sidelobe level of the brightest source
         in the initial residual image and the residual image is
         re-computed by subtracting the sources and their responses in
         the gridded Fourier domain (to eliminate aliasing errors).
         Image domain peak finding and approximate subtractions resume
         again. These two stages are iterated between until the chosen
         minor cycle exit criteria are satisfied (to trigger the next
         true major cycle that operates on ungridded visibilities).

         Since Clark CLEAN also uses only delta function, it is similar
         in behavior to Hogbom. The main difference is that the minor
         cycle is expected to be much faster (for large images) because
         only a small fraction of the PSF is used for image-domain
         updates. Typically, errors due to such a truncation are
         controlled by transitioning to a uv-subtraction or a major
         cycle when the peak residual reaches the level of the highest
         sidelobe for the strongest feature.

         For polarization imaging, Clark searches for the peak in

         $I^2 + Q^2 + U^2 + V^2$

         $I^2 + Q^2 + U^2 + V^2$

          

         .. rubric:: Clarkstokes
            :name: clarkstokes

         In the '*clarkstokes*' algorithm, the Clark psf is used, but
         for polarization imaging the Stokes planes are cleaned
         sequentially for components instead of jointly as in '*clark*'.
         This means that this is the same as 'clark' for Stokes I
         imaging only. This option can also be combined with
         *imagermode='csclean'*.

          

      .. container:: content

         .. rubric:: Multi-Scale
            :name: title3

         Cornwell-Holdaway Multi-Scale CLEAN (CH-MSCLEAN) `[4] <#cit>`__
         is a scale-sensitive deconvolution algorithm designed for
         images with complicated spatial structure. It parameterizes the
         image into a collection of inverted tapered paraboloids. The
         minor cycle iterations use a matched-filtering technique to
         measure the location, amplitude and scale of the dominant flux
         component in each iteration, and take into account the
         non-orthogonality of the scale basis functions while performing
         updates. In other words, the minor cycle iterations consider
         all scales together and model components are chosen in the
         order of decreasing integrated flux.

         MS-CLEAN can be formulated as a chi-square minimization applied
         to a sky model that parameterizes the sky brightness as a
         linear combination of flux components of different scale sizes.
         The figure below illustrates how a source with multi-scale
         features is represented by two scale sizes (for example) and
         how the problem reduces to one of finding the location and
         amplitudes of delta function components (something for which a
         CLEAN based approach is optimal). The top left and bottom left
         images show flux components of two different scale sizes. The
         images in the middle column show sets of delta functions that
         mark the locations and amplitudes of the flux components for
         each scale. The image on the far right is the sum of the
         convolutions of the first two columns of images. 

         |image2|

         +---------+-----------------------------------------------------------+
         | Type    | Figure                                                    |
         +---------+-----------------------------------------------------------+
         | ID      | fig_msmodel.png                                           |
         +---------+-----------------------------------------------------------+
         | Caption | A pictorial representation of how a source with structure |
         |         | at multiple spatial scales is modeled in MS-CLEAN.        |
         +---------+-----------------------------------------------------------+

      .. rubric:: Choosing 'scales'
         :name: choosing-scales

      In practice, the user must specify a set of scale sizes for the
      algorithm to use (in units of the number of pixels). As of now,
      this can be done only manually with the user making guesses of
      what the appropriate scale sizes are. This figure illustrates how
      the scales can be chosen, for a given structure on the sky. 

      |image3|

      +---------+-----------------------------------------------------------+
      | Type    | Figure                                                    |
      +---------+-----------------------------------------------------------+
      | ID      | fig_multiscale_example.png                                |
      +---------+-----------------------------------------------------------+
      | Caption | An example set of multiscale 'scale sizes' to choose for  |
      |         | a given source structure.                                 |
      +---------+-----------------------------------------------------------+

      It is recommended that a '0' scale always be included to model
      unresolved sources. Beyond that, scale sizes should approximately
      follow the sizes of dominant structures in the image. For
      structure with very bright and sharp edges, a series of nearby
      scale sizes works best, often in conjunction with a mask. The
      largest scale size should be less than or equal to the smaller
      dimension of large scale features. One must also take care to
      avoid scale sizes that correspond to the unmeasured short spacings
      in the central region of uv space, as the reconstruction on these
      scales will see no constraints from the data and can result in
      arbitrary values (or divergence). For mosaics of extended
      emission, it is sometimes possible to use large scale sizes in the
      minor cycle if there are enough connected structures across
      pointings, but since there still is no actual short spacing uv
      data to constrain those scales, they should be used with caution.
      A reasonable starting point for setting the scales (assuming the
      cell size samples the mainlobe of the psf by a factor of ~5) is
      *scales=[0,5,15]*.

      .. container:: content

         .. rubric:: Scale Bias
            :name: scale-bias

         By default, the optimal choice of scale per iteration is that
         which produces the maximum principal solution (assuming
         independent scales). Given this normalization, all scales
         supplied via the *scales* parameter are treated equally.

         In addition to this base normalization, a *smallscalebias*
         parameter may be used to bias the solution towards smaller or
         larger scales. This is especially useful when very large scale
         emission is coupled with weak compact features. The peak from
         each scale's smoothed residual is multiplied by ( 1 -
         *smallscalebias* \* scale/maxscale ) to increase or decrease
         the amplitude relative to other scales, before the scale with
         the largest peak is chosen.

         *smallscalebias=0.0* (default) implies equal weight to all
         scales (as per the natural normalization that comes with the
         principal solution). Increasing it from 0.0 to 1.0 biases the
         reconstruction towards smaller scales in the supplied range.
         Decreasing it from 0.0 to -1.0 biases it towards larger scales
         in the supplied range.  It can be useful to experiment with
         MS-clean in *interactive=True* mode. If you notice that bright
         regions of emission are overcleaned in the first few major
         cycles (i.e. negative regions will appear in the residual
         image), it suggests that too much cleaning is happening on the
         largest scales and it can help to increase the
         *smallscalebias*. Additionally, it is often necessary to clean
         comparatively deeply to reap the full benefit of a multi-scale
         CLEAN.  Note also that scale bias (*smallscalebias*) is a
         fine-tuning tool that will be useful only if the list of
         supplied scale sizes is also appropriate to the structure being
         deconvolved; before turning to smallscalebias, it is advisable
         to first ensure that the *scales* parameter is set to
         reasonable values.

         .. container:: info-box

            **NOTE**: An improved *smallscalebias* paramater was
            implemented in CASA 5.6 for both MultiScale and MTMFS
            deconvolution algorithms. Details can be found in `this CASA
            memo <https://casa.nrao.edu/casadocs-devel/stable/memo-series/casa-memos/casa_memo9_ms_mtmfs_clean.pdf>`__.

         .. rubric::  
            :name: section

         .. rubric:: Multi-Resolution CLEAN
            :name: multi-resolution-clean

         A related approach, called Multi-Resolution CLEAN is available
         in AIPS (and not in CASA). It is very similar to MS-CLEAN,
         although it operates on one scale size at a time. It smoothes
         the residual image and PSF by a particular scale size, and runs
         the minor cycle only on that scale. It switches scales after
         the next major cycle. This algorithm uses a different
         scale-based normalization (compared to MS-CLEAN) and has its
         own *scalebias* parameter which has its own formula. 

          

      .. container:: content

         .. rubric:: Multi-Term (with Multi-Scale)
            :name: title4

         Multi-Scale Multi-Frequency synthesis (MSMFS) `[5] <#cit>`__ is
         a wide-band imaging algorithm that models the wide-band sky
         brightness distribution as a collection of inverted, tapered
         paraboloids of different scale sizes, whose amplitudes follow a
         polynomial in frequency. A linear-least squares approach is
         used along with standard clean-type iterations to solve for
         best-fit spectral and spatial parameters. A point-source
         version of this algorithm can be run by specifying only one
         scale size corresponding to a delta-function.

         |image4|

         +---------+-----------------------------------------------------------+
         | Type    | Figure                                                    |
         +---------+-----------------------------------------------------------+
         | ID      | figconvolutionmt.png                                      |
         +---------+-----------------------------------------------------------+
         | Caption | A 2x2 system of equations to represent the fitting of a   |
         |         | 2-term Taylor polynomial (Note that this is only a        |
         |         | representative diagram using the same images shaded       |
         |         | differently). In reality, the Hessian matrix contains     |
         |         | different spectral PSFs.                                  |
         +---------+-----------------------------------------------------------+

         The figure illustrates the set of normal equations that are to
         be solved in the image domain. What is usually a single
         convolution is now a joint convolution operator. The images on
         the left represent Taylor-weighted residual images, the 2x2
         matrix contains spectral PSFs (the instruments' responses to
         spectra given by different Taylor functions), and the model
         images on the right represent Taylor coefficients per
         component. (Note : This figure only illustrates the structure
         of the system of equations.)

         More details about the algorithm and how to choose parameters
         such as the number of Taylor coefficients (nterms) and the
         reference frequency (reffreq) are given in the `Wideband
         Imaging <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/wide-band-imaging>`__
         section. 

      .. container:: content

          

      .. container:: content

         Multiple Scales as part of the MTMFS algorithm are treated in
         the same way as MS-Clean (above), with the *scales* and 
         *smallscalebias* parameters available for choosing a range of
         scales and fine-tuning which ones get preference during
         reconstruction.

      .. container:: content

         .. container:: content

            .. rubric::  
               :name: section-1

            .. rubric:: Restoration
               :name: title5

            .. rubric:: Standard Restoration
               :name: standard-restoration

            The final list of flux components (or an image containing
            just the component delta functions) is restored by smoothing
            it with a Gaussian that matches the resolution of the main
            lobe of the PSF and adding back the residual image. This
            step is done in order to compensate for the unphysical
            nature of CLEAN based component images that include delta
            functions, and to include residual flux (especially for
            extended emission) that was not picked up as part of the
            model image. The need for restoration varies depending on
            the choice of algorithm but since all our CLEAN-based
            approaches include delta functions (with or without
            multi-scale components), this restoration step is always
            applied.

             

            .. rubric:: Multi-term restoration
               :name: multi-term-restoration

            Multi-term (wideband) restoration is a bit different from
            standard restoration in that it also modifies the residuals
            that are added to the smoothed model. Residuals are
            converted from Taylor-weighted averages of the residual data
            into Taylor coefficient space such that they represent the
            'next higher order term' being imaged (a standard way of
            represent error). Practical implications of this are a
            higher than expected rms in the zero-th order image because
            the higher order terms being fitted have more reconstruction
            error and are not strictly linearly independent from the
            zero-th order term. In the outputs of the Multi-Term
            algorithm, the restored images contain these modified
            residuals, whereas the residual images contain the
            unmodified residuals which conform to what astronomers
            typically mean by 'residual' images. More details about the
            algorithm are provided in the `Wideband
            Imaging <https://casa.nrao.edu/casadocs-devel/stable/wide-band-imaging>`__
            section.

             

         .. container:: content

            .. rubric:: Clean Bias
               :name: title6

            Clean bias, an effect noticed for decades by users of the
            CLEAN algorithm, is a systematic shift of reconstructed peak
            intensities to lower than expected values. This is usually
            seen in deep imaging runs with large numbers of
            closely-spaced weak sources, and when the PSF has sidelobes
            above the 0.1 level. The use of masks or clean boxes to
            constrain the search space alleviates the problem. A PSF
            with lower sidelobes (for example the PSF from MFS imaging
            as compared to a single channel PSF) can also prevent this
            type of flux bias with the CLEAN algorithm and more
            importantly it does so without having to invoke complicated
            masking procedures.

            The clean bias effect can be explained by considering that
            the CLEAN algorithm is an L1-norm basis-pursuit method that
            is optimized for sparse signals that can be described with a
            minimal number of basis functions. For astronomical images
            this implies well-separated point sources whose properties
            can be described by single basis functions (one pixel each)
            and whose central peaks are minimally affected by PSF
            sidelobes from neighbouring sources. In a crowded field of
            point sources, especially with a PSF with high sidelobes,
            the CLEAN algorithm is more error-prone in the low SNR
            regime. A systematic lowering of source brightness can be
            explained by the algorithm constructing many artificial
            source components from the sidelobes of real sources.

             

         .. container:: content

            .. rubric:: Other Algorithms
               :name: title7

            There are other options that are present in our code base,
            but not used much, could be experimental, coming in the near
            future, or simply untested. Information on how to add
            external algorithms is given below.

            .. rubric:: MEM
               :name: mem

            This algorithm models the sky brightness distribution as a
            collection of point-sources and uses a prior image along
            with an entropy-based penalty function to bias the solution
            of pixel amplitudes. The Maximum Entropy method (MEM)
            `[6] <#cit>`__ `[7] <#cit>`__ is a pixel-based deconvolution
            algorithm that performs a rigorously-constrained
            optimization in a basis of pixel amplitudes. MEM uses the
            Bayesian formulation of chi-square minimization, and applies
            a penalty function based on relative image entropy. This
            choice of penalty function biases the estimate of the true
            sky brightness towards a known prior image. If a flat image
            is chosen as the prior, the solution is biased towards being
            smooth, and produces a more realistic reconstruction of
            extended emission. Positivity and emptiness constraints can
            be applied on the image pixels via a penalty function.

            The MEM implementation in CASA's imager is unstable, and is
            unlikely to get attention as there are better methods
            available now. Please use multi-scale CLEAN instead.

            .. rubric:: ASP
               :name: asp

            The Adaptive Scale Pixel (ASP) `[8] <#cit>`__ deconvolution
            algorithm parameterizes the sky brightness distribution into
            a collection of Gaussians and does a formal constrained
            optimization on their parameters. In the major cycle,
            visibilities are predicted analytically with high accuracy.
            In the minor cycle, the location of a flux component is
            chosen from the peak residual, and the parameters of the
            largest Gaussian that fits the image at that location are
            found. The total number of flux-components is also updated
            as the iterations proceed.

            This algorithm is currently not available in CASA, but is on
            the mid-term implementation plan. 

             

            .. rubric:: Comparison between deconvolution algorithms :
               One example
               :name: comparison-between-deconvolution-algorithms-one-example

            Due to the fact that the uv-sampling is always incomplete,
            the result of a reconstruction algorithm can vary depending
            on the choice of sky model and the type of algorithm and
            constraints used. This figure shows a comparison between
            point-source CLEAN, MS-CLEAN, MEM and the ASP algorithms.

            In the figure below, the top row of panels show the
            component images that illustrate the different sky models
            being used. The middle row of panels shows restored images
            (used for the science). It should be noted that they are all
            different from each other and that they are all valid
            images. The main difference appears to be the achievable
            angular resolution. The bottom panels show residual images
            (gradient of chi-square) which radio astronomers typically
            use to judge whether all the signal in the data has been
            modeled or not. These images show how well the different
            methods handle extended emission. For example, CLEAN results
            in significant correlated flux in the residuals. MEM does
            better but the error pattern has significant structure
            outside the source too. MS-CLEAN has lower residuals than
            the two previous methods but has a characteristic pattern
            arising from using a fixed set of scale sizes to model
            complicated spatial structure. The ASP method shows much
            more noise-like residuals owing to the fact that at each
            iteration it finds best-fit components. Most more recent
            algorithms derived using compressed-sensing theory are
            reported (in the literature) to produce results similar to
            the ASP algorithm, as they all also perform fits to
            parameterized basis functions.

             

            |image5| 

            +---------+-----------------------------------------------------------+
            | Type    | Figure                                                    |
            +---------+-----------------------------------------------------------+
            | ID      | Create a short, unique name                               |
            +---------+-----------------------------------------------------------+
            | Caption | A comparison between point-source CLEAN, MS-CLEAN, MEM    |
            |         | and the ASP algorithms.                                   |
            +---------+-----------------------------------------------------------+

             

         .. container:: content

            .. rubric:: Adding Other Deconvolution algorithms
               :name: title8

            External deconvolution algorithms can be connected to our
            imaging framework in order to access our data I/O and
            gridding routines (with parallelization) and avail of the
            option of operating within major/minor cycle loops instead
            of as stand-alone methods that don’t often connect to the
            data. The only pre-requisite is that the algorithm is able
            to operate in the image domain on a residual image and a
            PSF, and produce a model image as output. 

            It should be noted that although many recently developed
            compressed-sensing algorithms do not explicitly make this
            uv-domain and image-domain distinction, their practical
            implementations do, and in some cases it is possible to
            frame the algorithm within a major/minor cycle structure
            (with residual visibilities being computed as 'data -
            model'). Another way of saying this is that our software can
            be used to implement the data->image and image->data
            transforms, while implementing an external reconstruction
            algorithm. The only exceptions are algorithms that require
            the gridding of something other than 'data - model' and
            which cannot be implemented as linear combinations in the
            image domain.

            Attempts by external algorithm developers to connect to our
            framework are welcome, as are suggestions for improving this
            interface to be more usable.

            .. rubric:: Task Interface
               :name: task-interface

            **tclean** can be used in 'only major cycle' mode by setting
            *niter=0*. If *calcres=False*, *calcpsf=False* are set, then
            **tclean** can be also used to start directly with minor
            cycle algorithms that pick up .residual and .psf images from
            disk.

            .. rubric:: Tool interface
               :name: tool-interface

            Python scripts can use our PySynthesisImager library to
            access each operational step of the **tclean** task, and to
            add or delete steps as necessary. Examples are given in the
            **tclean** task documentation (at the end of the examples
            page).

            .. rubric:: Within C++
               :name: within-c

            For C++ programmers, it is possible to connect a new
            deconvolution algorithm by deriving from SDAlgorithmBase and
            implementing three main routines (initialization, cleanup,
            and a 'takeOneStep' method that does the series of minor
            cycle iterations).

             

            =============== ======================
            Citation Number 1
            Citation Text   Schwab and Cotton 1983
            =============== ======================

            =============== ===========
            Citation Number 2
            Citation Text   Hogbom 1974
            =============== ===========

            =============== ==========
            Citation Number 3
            Citation Text   Clark 1980
            =============== ==========

            =============== =============
            Citation Number 4
            Citation Text   Cornwell 2008
            =============== =============

            =============== ===================
            Citation Number 5
            Citation Text   Rau & Cornwell 2011
            =============== ===================

             

            =============== =======================
            Citation Number 6
            Citation Text   Cornwell and Evans 1985
            =============== =======================

             

            =============== ===========================
            Citation Number 7
            Citation Text   Narayan and Nityananda 1986
            =============== ===========================

            =============== ===========================
            Citation Number 8
            Citation Text   Bhatnagar and Cornwell 2004
            =============== ===========================

             

.. container:: section
   :name: viewlet-below-content-body

.. |image1| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/figconvolution.png/@@images/678d55be-6de3-4c58-b314-2744cc11e05e.png
   :class: image-inline
.. |image2| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/fig_msmodel.png/@@images/ff0dd105-ef87-49df-b2f6-3097b3731a99.png
   :class: image-inline
   :width: 660px
   :height: 323px
.. |image3| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/fig_multiscale_example.png/@@images/f46fa222-9423-4daf-8bc9-8b32f6360914.png
   :class: image-inline
.. |image4| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/figconvolutionmt.png/@@images/686f7143-68de-47b8-b087-d0cda21ac9a7.png
   :class: image-inline
.. |image5| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/fig_deconv_compare-1.png/@@images/e2b5a5f7-30db-491e-b629-72aae623f90b.png
   :class: image-inline
   :width: 514px
   :height: 355px
