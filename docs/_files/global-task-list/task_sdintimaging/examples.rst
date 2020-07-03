.. container::
   :name: viewlet-above-content-title

Examples
========

.. container::
   :name: viewlet-below-content-title

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      To run sdintimaging with automatic SD-PSF generation, n-sigma
      stopping thresholds, a pb-based mask at the 0.3 gain level, and no
      other deconvolution masks (interactive=False).  Use the helper
      function shown below to extract frequency information from the sd
      cube to supply as input to sdintimaging.  Note that the sdimage
      cube must contain per-plane restoring beams.

      .. container:: casa-input-box

         from sdint_helper import \*
         sdintlib = SDINT_helper()
         sdintlib.setup_cube_params(sdcube='M100_TP')
            Output : Shape of SD cube : [90 90  1 70]
            Coordinate ordering : ['Direction', 'Direction', 'Stokes',
            'Spectral']
            nchan = 70
            start = 114732899312.0Hz
            width = -1922516.74324Hz
            Found 70 per-plane restoring beams#
            (For specmode='mfs' in sdintimaging, please remember to set
            'reffreq' to a value within the freq range of the cube)
            Returned Dict : {'nchan': 70, 'start': '114732899312.0Hz',
            'width': '-1922516.74324Hz'}

         sdintimaging(usedata="sdint", sdimage="../M100_TP",
         sdpsf="",sdgain=3.0, dishdia=12.0, vis="../M100_12m_7m",
         imagename="try_sdint_niter5k", imsize=1000, cell="0.5arcsec",
         phasecenter="J2000 12h22m54.936s +15d48m51.848s", stokes="I",
         specmode="cube", reffreq="", nchan=70,
         start="114732899312.0Hz", width="-1922516.74324Hz",
         outframe="LSRK", veltype="radio", restfreq="115.271201800GHz",
         interpolation="linear", chanchunks=1,
         perchanweightdensity=True, gridder="mosaic", mosweight=True,
         pblimit=0.2, deconvolver="multiscale", scales=[0, 5, 10, 15,
         20], smallscalebias=0.0, pbcor=False, weighting="briggs",
         robust=0.5, niter=5000, gain=0.1, threshold=0.0, nsigma=3.0,
         interactive=False, usemask="user", mask="", pbmask=0.3)

      For test-results using these parameters, and for additional
      test-results, see the CASA Docs chapter page on `Joint Single Dish
      and Interferometeric Image
      Reconstruction <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-combination/joint-sd-and-interferometer-image-reconstruction>`__.

       

       

.. container:: section
   :name: viewlet-below-content-body
