.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Procedure SD Imaging
====================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   The procedure for single-dish image generation and data gridding in
   CASA

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      CASA uses the
      `sdimaging <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_sdimaging>`__
      task to grid a single-dish image or cube. While the steps are
      described in detail here, an example of the full single-dish
      calibration and imaging processes can be found in the `M100 Band 3
      Single Dish
      CASAguide <https://casaguides.nrao.edu/index.php/M100_Band3_SingleDish_4.3>`__.

      .. rubric:: Default operation
         :name: default-operation

      The **sdimaging** task can determine and populate almost all the
      gridding parameters by default.  Simply invoking **sdimaging**
      with the single-dish MeasurementSet and output file name will
      work. This will produce a single, potentially very large cube
      having as many channels as necessary to span the entire spectral
      range, with a spectral resolution equal to that of the
      observation.

      .. container:: casa-input-box

         sdimaging(infiles=sd_ms+'.bl',outfile=imagename)

      The default parameter choices for imaging are selected as follows:
      the image pixel size is 1/3 the primary beam, the primary beam
      itself is computed based on the standard $\frac{\lambda}{D}$, with
      some empirically-validated tapering applied. The image dimensions
      are determined by the spatial extent of the mapped area in the
      observation, and by default, all channels and all spectral windows
      are imaged, along with all antennas and all polarizations.

      .. rubric:: Customized operation
         :name: customized-operation

      Of course, users can tune their data products by specifying the
      image size and dimensions, the frequency/velocity characteristics,
      the gridding and data filtering and smoothing parameters, and so
      on. The defaults for **sdimaging** for image resolution (i.e.
      cellsize in arcsec) is determined from the rest frequency of the
      0th spectral window so that there are three pixel elements across
      the beam, the beam being calculated with
      $b\times\frac{\lambda}{D}$.  See information here about tapering:
      `PrimaryBeamArcsec <https://safe.nrao.edu/wiki/bin/view/ALMA/PrimaryBeamArcsec>`__.
      The image extent is computed by default so that the sampled area
      is completely encompassed in a single rectangle, and the pixel
      dimension follows naturally from maxsize/cellsize. The default
      image center (the somewhat inappropriately-named *phasecenter*
      parameter) is computed simply as the center of that region.

      These parameters can be left to be determined by **sdimaging**, or
      they can be determined using CASA tools.

       

      .. rubric:: Image dimensions and pixel interval
         :name: image-dimensions-and-pixel-interval

      The image extent can be explicitly determined using
      **aU.getTPSampling**:

      .. container:: casa-input-box

         xSampling, ySampling, maxsize = aU.getTPSampling(refvis,
         showplot=True)

      which returns an image output showing the scans, their sky angles,
      and positions in RA-Dec, as shown here:

      |image1|

      Note that **getTPSampling** MUST operate on the original
      MeasurementSet (i.e. one that is not split or subselected).
      **getTPSampling** also yields the sampling rates in the x and y
      (i.e. azimuth and elevation) axes, as well as the maximum size of
      the image, in arcseconds.

      The beam size used by **sdimaging** is determined using the
      **aU.primaryBeamArcsec** task, though this can also be invoked by
      the user and used to compute, for example, a cellsize and image
      size. The default for **aU.primaryBeamArcsec** corresponds to a
      12m antenna with normal tapering. Setting
      the *fwhmfactor* modifies the beam taper (see discussion in
      `PrimaryBeamArcsec <https://safe.nrao.edu/wiki/bin/view/ALMA/PrimaryBeamArcsec>`__).

      .. container:: casa-input-box

         freq=115.27e+9
         fwhmfactor=1.13
         diameter=12
         theorybeam = aU.primaryBeamArcsec(frequency=freq*1e-9,
         fwhmfactor=fwhmfactor, diameter=diameter)
         cell = theorybeam/9.0
         imsize = int(round(maxsize/cell)*2)

      The center of the image can be modified using the *phasecenter*
      parameter. Single-dish images actually have many phase centers, so
      the name is somewhat misleading. However it is preserved here for
      consistency with the interferometer terminology. In the context of
      single-dish data, *phasecenter* refers only to coordinates that
      will align with the center of the image, and this can be in J2000
      or Az/El, e.g.

      .. container:: casa-input-box

         phasecenter='J2000 12h22m54.9 +15d49m15'

       

      .. rubric:: Frequency and/or velocity axis
         :name: frequency-andor-velocity-axis

      The default rest frequency is the mean frequency of the first
      spectral window (i.e. that having the lowest spectral window ID).
      Of course it can instead be set by the user, or a different
      spectral window frequency can be used, extracted from the data
      using **msmd** tools:

      .. container:: casa-input-box

         | msmd.open(vislist[0])
         | freq = msmd.meanfreq(spw)
         | msmd.close()
         | print "SPW %d: %.3f GHz" % (spw, freq*1e-9)

      The third axis of the image cube can be specified using the
      *veltype* and *outframe* parameters. Many spectral-line observers
      will prefer to change these so the output has a velocity axis in
      the radio convention as follows:

      .. container:: casa-input-box

         | veltype='radio',
         | outframe='lsrk',

      and the rest frequency can be specified with:

      .. container:: casa-input-box

         restfreq='115.271204GHz'

      The velocity extent of the image cube can be specified by
      selecting a spectral window (via the *spw* parameter), the channel
      range (via the *nchan* and *start* parameters), and the
      frequency/velocity resolution (via the *width* parameter). For
      example:

      .. container:: casa-input-box

         | nchan=70,
         | mode='velocity',
         | start='1400km/s',
         | width='5km/s',

      .. rubric:: 
         Gridding parameters
         :name: gridding-parameters

      The gridding kernel defaults to a box shape, but it can be
      specified as a spherical ('SF'), Primary beam ('PB'),
      Gaussian ('GAUSS') or Gaussian*Jinc (GJINC). The recommended
      setting for ALMA data is a spherical ('SF') kernel.
      The *convsupport* parameter defines the cut-off radius for 'SF' in
      units of pixels, defaulting to 3 pixels.  However, the recommended
      value for ALMA data is convsupport=6 (see
      `sdimaging <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_sdimaging>`__
      and Mangum et al. 2007 `[1] <#cit>`__ for more details on these
      parameters).

      The parameter *stokes* specifies the stokes product. At present,
      the weighting for stokes I is computed consistently with
      historical usage: I=XX/2+YY/2.  While this is mathematically
      consistent with the computation of stokes I, it is an incorrect
      treatment since the computation necessarily must incorporate the
      contributions from Q and U. Ordinarily, these terms cancel out
      from the computation of stokes I, but their error parameters must
      be incorporated, and historically, this is not respected. 

      CASA development is seeking to make the computation of the weights
      consistent with a proper computation of stokes I, and this is done
      in **sdfit**, but it is not yet completed for **sdimaging. **
      However, to emphasize, while the current implementation of
      computation for stokes I by **sdimaging** is consistent with
      convention, the convention is formally incorrect.

       

      .. rubric:: Example script
         :name: example-script

      Fully specified, a call to **sdimaging** might look like the
      following:

      .. container:: casa-input-box

         | sdimaging(infiles=sd_ms+'.bl',
         |     field='M42',
         |     spw='%s'%(spw),
         |     nchan=70,
         |     mode='velocity',
         |     start='1400km/s',
         |     width='5km/s',
         |     veltype='radio',
         |     outframe='lsrk',
         |     restfreq='%sGHz'%(freq/1e+9),
         |     gridfunction='SF',
         |     convsupport=6,
         |     stokes='I',
         |     phasecenter='J2000 12h22m54.9 +15d49m15',
         |     ephemsrcname='',
         |     imsize=imsize,
         |     cell='%sarcsec'%(cell),
         |     overwrite=True,
         |     outfile=imagename)

      The products here are the image data, returned in the variable
      'imagename', and also a map of weights: <imagename>.weight. The
      weights indicate the robustness of the gridded data on a per-pixel
      basis, and are important when performing further computations and
      analysis with the image products.

      +-----------------+---------------------------------------------------+
      | Citation Number | 1                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Mangum, et al. 2007, A&A, 474, 679-687            |
      |                 | (`ADS <http://www.aan                             |
      |                 | da.org/articles/aa/pdf/2007/41/aa7811-07.pdf>`__) |
      +-----------------+---------------------------------------------------+

       

.. container:: section
   :name: viewlet-below-content-body

.. |image1| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/single-dish-imaging/95b1aeee-fd40-4a05-87fe-a4170a8b403e.png/@@images/e51fb1c5-fe54-457a-9ffb-9ec7e539a015.png
   :class: image-inline
