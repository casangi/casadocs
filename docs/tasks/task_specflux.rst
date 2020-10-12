

.. _Description:

Description
   specflux task: Report spectral profile and calculate spectral flux
   over a user specified region
   
   .. warning:: **Note**: **specflux** is currently an experimental task. 
   
   **specflux** retrieves details of a multi-channel image spectrum
   which has been integrated over a given region (or the entire image
   by default). One may specify which function to use to combine the
   pixel values within the region using the *function* parameter.
   Supported values are 'flux density', 'mean', 'median', and 'sum'.
   Minimal match is supported. **specflux** also calculates
   spectrally integrated flux (brightness) values. 
   
   The task uses the brightness units that are specified in the image
   header (e.g., Jy/beam or K). When 'flux density' is calculated,
   the resulting spectra are in units of Jy for cube units of Jy/beam
   and :math:`K*arcsec^2` for cube units of K. 
   
   The spectral integral that **specflux** calculates is the sum of
   the spectrum multiplied by the channel width. The units are
   updated accordingly. 
   
   If the units are :math:`K*arcsec^2`, multiply the reported value
   by :math:`2.3504\times10^{-8}\times d^2`, where :math:`d` is in
   pc, to convert from units of :math:`K*arcsec^2` to units of
   :math:`K*pc^2`.
   
   If provided, *major* and *minor* will be used to compute the beam
   size, and hence the per channel flux densities (if *function="flux
   density"*), overriding the input image beam information (if
   present).
   
   .. note:: **NOTE**: When it is not possible to compute the spectral flux
      (e.g., in the case where the brightness units are Jy/beam but
      the image has no synthesized beam and none is provided to the
      task), then the application will fail.
   
   The output of **specflux** is written to the CASA logger and an
   ASCII file if *logfile* is specified. 
   
    
   
   .. rubric:: Parameter descriptions
      
   
   .. rubric:: *imagename*
      
   
   Name of the input image (CASA, FITS or MIRIAD images are
   accepted). 
   
   .. rubric:: *region*
      
   
   Region selection, using a `CASA region
   file <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/region-files>`__.
   Default is the entire image. 
   
   .. rubric:: *box*
      
   
   `Rectangular spatial
   selection <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/image-selection-parameters>`__,
   if no region file is supplied. Default is the entire image.
   
   .. rubric:: *chans*
      
   
   `Spectral/channel
   selection <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/image-selection-parameters>`__,
   if no region file is supplied. Default is the entire channel
   range. 
   
   .. rubric:: *stokes*
      
   
   `Stokes
   selection <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/image-selection-parameters>`__,
   if no region file is supplied. Default are all Stokes planes. 
   
   .. rubric:: *mask*
      
   
   An `image
   mask <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/image-masks>`__
   file. Default is not to use a mask.  
   
   .. rubric:: *stretch*
      
   
   If the image mask is a single plane and not a cube of the same
   dimension as the input data cube, *stretch* can by set to True to
   extend the mask to all planes. (Default: False)
   
   .. rubric:: *function*
      
   
   Aggregate function to use for computing per channel values.
   Supported values are 'flux density', 'mean', 'median', 'sum'.
   Minimal match is supported. *
   *
   
   .. rubric:: *unit*
      
   
   Unit to use for the spectral flux calculation. Must be conformant
   with a typical spectral axis unit. Velocity units may only be used
   if the spectral coordinate has a rest frequency and if it is
   :math:`> 0`.
   
   .. rubric:: *major*
      
   
   Major axis of overriding restoring beam. If specified, it must be
   a valid quantity (e.g., "4arcsec").
   
   .. rubric:: *minor*
      
   
   Minor axis of overriding restoring beam. If specified, it must be
   a valid quantity (e.g., "3arcsec").
   
   .. rubric:: *logfile*
      
   
   File which to write details. Default is to not write to a file.
   
   .. rubric:: *overwrite*
      
   
   Overwrite exisitng *logfile* file if it exists. (Default: False)
   

.. _Examples:

Examples
   task examples
   
   **Example 1:**
   
   Write a spectrum of the cube "my.im" to the file "my.log". A
   rectangular box is selected in pixel units, in addition to a mask
   calculated by the `LEL
   expression <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/lattice-expression-language-lel/lattice-expression-language>`__
   defining all pixel values larger than zero. 
   
   ::
   
      specflux(imagename="my.im", box="10,10,45,50", mask="my.im>=0",
      unit="km/s", logfile="my.log", overwrite=True)
   
   The units of the cube are in Jy/beam (*function="flux density"*).
   The CASA output looks like this:
   
   ::
   
      | 2018-04-23 21:28:31 INFO specflux
        ##########################################
      | 2018-04-23 21:28:31 INFO specflux ##### Begin Task: specflux
        #####
      | 2018-04-23 21:28:31 INFO specflux
        specflux(imagename="IRC10216_HC3N.cube_r0.5.image",region="",box="",chans="",stokes="",
      | 2018-04-23 21:28:31 INFO specflux
        mask="",stretch=False,function="flux
        density",unit="km/s",major="",
      | 2018-04-23 21:28:31 INFO specflux
        minor="",logfile="",overwrite=False)
      | 2018-04-23 21:28:31 INFO specflux No directional region
        specified. Using full positional plane.
      | 2018-04-23 21:28:31 INFO specflux Using all spectral
        channels.
      | 2018-04-23 21:28:31 INFO specflux Using polarizations ALL
      | 2018-04-23 21:28:31 INFO specflux Selected bounding box : 
      | 2018-04-23 21:28:31 INFO specflux [0, 0, 0, 0] to [299, 299,
        0, 53] (09:48:01.492, +13.15.40.658, I, 3.63986e+10Hz to
        09:47:53.299, +13.17.40.258, I, 3.6392e+10Hz)
      | 2018-04-23 21:28:31 INFO specflux Selected bounding box : 
      | 2018-04-23 21:28:31 INFO specflux [0, 0, 0, 0] to [299, 299,
        0, 53] (09:48:01.492, +13.15.40.658, I, 3.63986e+10Hz to
        09:47:53.299, +13.17.40.258, I, 3.6392e+10Hz)
      | 2018-04-23 21:28:31 INFO specflux Selected bounding box : 
      | 2018-04-23 21:28:31 INFO specflux [0, 0, 0, 0] to [299, 299,
        0, 53] (09:48:01.492, +13.15.40.658, I, 3.63986e+10Hz to
        09:47:53.299, +13.17.40.258, I, 3.6392e+10Hz)
      | 2018-04-23 21:28:31 INFO specflux Selected bounding box : 
      | 2018-04-23 21:28:31 INFO specflux [0, 0, 0, 0] to [299, 299,
        0, 53] (09:48:01.492, +13.15.40.658, I, 3.63986e+10Hz to
        09:47:53.299, +13.17.40.258, I, 3.6392e+10Hz)
      | 2018-04-23 21:28:31 INFO specflux Selected bounding box : 
      | 2018-04-23 21:28:31 INFO specflux [0, 0, 0, 0] to [299, 299,
        0, 53] (09:48:01.492, +13.15.40.658, I, 3.63986e+10Hz to
        09:47:53.299, +13.17.40.258, I, 3.6392e+10Hz)
      | 2018-04-23 21:28:31 INFO specflux Selected bounding box : 
      | 2018-04-23 21:28:31 INFO specflux [0, 0, 0, 0] to [299, 299,
        0, 53] (09:48:01.492, +13.15.40.658, I, 3.63986e+10Hz to
        09:47:53.299, +13.17.40.258, I, 3.6392e+10Hz)
      | 2018-04-23 21:28:31 INFO specflux #
        IRC10216_HC3N.cube_r0.5.image, region=
      | 2018-04-23 21:28:31 INFO specflux # beam size: 5.8131035724
        arcsec2, 36.3318973275 pixels
      | 2018-04-23 21:28:31 INFO specflux # Total flux: 42.4303952205
        Jy.km/s
      | 2018-04-23 21:28:31 INFO specflux # Channel
        number_of_unmasked_pixels frequency_(MHz) Velocity_(km/s)
        Flux_density_(Jy)
      | 2018-04-23 21:28:31 INFO specflux 0 90000 36398.605111
        -51.770979 1.288319e-02
      | 2018-04-23 21:28:31 INFO specflux 1 90000 36398.480096
        -50.741311 1.763681e-02
      | 2018-04-23 21:28:31 INFO specflux 2 90000 36398.355081
        -49.711639 -4.651636e-03
      | 2018-04-23 21:28:31 INFO specflux 3 90000 36398.230067
        -48.681963 -2.611289e-03
      | 2018-04-23 21:28:31 INFO specflux 4 90000 36398.105052
        -47.652284 4.760521e-03
      | 2018-04-23 21:28:31 INFO specflux 5 90000 36397.980038
        -46.622601 2.035849e-03
      | 2018-04-23 21:28:31 INFO specflux 6 90000 36397.855023
        -45.592915 -4.315952e-03
      | 2018-04-23 21:28:31 INFO specflux 7 90000 36397.730008
        -44.563226 -1.664018e-02
      | 2018-04-23 21:28:31 INFO specflux 8 90000 36397.604994
        -43.533532 1.474457e-02
      | 2018-04-23 21:28:31 INFO specflux 9 90000 36397.479979
        -42.503835 -1.682229e-04
      | 2018-04-23 21:28:31 INFO specflux 10 90000 36397.354965
        -41.474135 1.795171e-01
      | 2018-04-23 21:28:31 INFO specflux 11 90000 36397.229950
        -40.444431 1.029375e+00
      | 2018-04-23 21:28:31 INFO specflux 12 90000 36397.104935
        -39.414724 1.830073e+00
      | 2018-04-23 21:28:31 INFO specflux 13 90000 36396.979921
        -38.385013 2.226224e+00
      | 2018-04-23 21:28:31 INFO specflux 14 90000 36396.854906
        -37.355298 2.335040e+00
      | 2018-04-23 21:28:31 INFO specflux 15 90000 36396.729892
        -36.325580 2.192430e+00
      | 2018-04-23 21:28:31 INFO specflux 16 90000 36396.604877
        -35.295859 1.910963e+00
      | 2018-04-23 21:28:31 INFO specflux 17 90000 36396.479862
        -34.266134 1.605489e+00
      | 2018-04-23 21:28:31 INFO specflux 18 90000 36396.354848
        -33.236405 1.445156e+00
      | 2018-04-23 21:28:31 INFO specflux 19 90000 36396.229833
        -32.206673 1.232498e+00
      | 2018-04-23 21:28:31 INFO specflux 20 90000 36396.104819
        -31.176937 1.016602e+00
      | 2018-04-23 21:28:31 INFO specflux 21 90000 36395.979804
        -30.147198 8.716491e-01
      | 2018-04-23 21:28:31 INFO specflux 22 90000 36395.854789
        -29.117455 8.204997e-01
      | 2018-04-23 21:28:31 INFO specflux 23 90000 36395.729775
        -28.087709 8.065589e-01
      | 2018-04-23 21:28:31 INFO specflux 24 90000 36395.604760
        -27.057959 7.171811e-01
      | 2018-04-23 21:28:31 INFO specflux 25 90000 36395.479746
        -26.028205 6.755083e-01
      | 2018-04-23 21:28:31 INFO specflux 26 90000 36395.354731
        -24.998448 6.621807e-01
      | 2018-04-23 21:28:31 INFO specflux 27 90000 36395.229716
        -23.968688 6.800027e-01
      | 2018-04-23 21:28:31 INFO specflux 28 90000 36395.104702
        -22.938924 7.596419e-01
      | 2018-04-23 21:28:31 INFO specflux 29 90000 36394.979687
        -21.909156 8.898271e-01
      | 2018-04-23 21:28:31 INFO specflux 30 90000 36394.854673
        -20.879385 1.004381e+00
      | 2018-04-23 21:28:31 INFO specflux 31 90000 36394.729658
        -19.849611 1.108837e+00
      | 2018-04-23 21:28:31 INFO specflux 32 90000 36394.604643
        -18.819832 1.380175e+00
      | 2018-04-23 21:28:31 INFO specflux 33 90000 36394.479629
        -17.790051 1.794887e+00
      | 2018-04-23 21:28:31 INFO specflux 34 90000 36394.354614
        -16.760265 2.042901e+00
      | 2018-04-23 21:28:31 INFO specflux 35 90000 36394.229600
        -15.730477 2.504406e+00
      | 2018-04-23 21:28:31 INFO specflux 36 90000 36394.104585
        -14.700684 2.789486e+00
      | 2018-04-23 21:28:31 INFO specflux 37 90000 36393.979570
        -13.670888 2.820036e+00
      | 2018-04-23 21:28:31 INFO specflux 38 90000 36393.854556
        -12.641089 1.624858e+00
      | 2018-04-23 21:28:31 INFO specflux 39 90000 36393.729541
        -11.611286 2.082959e-01
      | 2018-04-23 21:28:31 INFO specflux 40 90000 36393.604527
        -10.581480 -2.755634e-02
      | 2018-04-23 21:28:31 INFO specflux 41 90000 36393.479512
        -9.551670 -1.471130e-03
      | 2018-04-23 21:28:31 INFO specflux 42 90000 36393.354497
        -8.521856 6.336133e-03
      | 2018-04-23 21:28:31 INFO specflux 43 90000 36393.229483
        -7.492039 -2.073986e-03
      | 2018-04-23 21:28:31 INFO specflux 44 90000 36393.104468
        -6.462218 -1.695162e-02
      | 2018-04-23 21:28:31 INFO specflux 45 90000 36392.979454
        -5.432394 -1.015228e-02
      | 2018-04-23 21:28:31 INFO specflux 46 90000 36392.854439
        -4.402566 2.214961e-02
      | 2018-04-23 21:28:31 INFO specflux 47 90000 36392.729424
        -3.372735 -2.795951e-04
      | 2018-04-23 21:28:31 INFO specflux 48 90000 36392.604410
        -2.342900 2.829185e-03
      | 2018-04-23 21:28:31 INFO specflux 49 90000 36392.479395
        -1.313062 4.695695e-02
      | 2018-04-23 21:28:31 INFO specflux 50 90000 36392.354381
        -0.283220 1.790321e-02
      | 2018-04-23 21:28:31 INFO specflux 51 90000 36392.229366
        0.746625 -2.175977e-02
      | 2018-04-23 21:28:31 INFO specflux 52 90000 36392.104351
        1.776474 0.000000e+00
      | 2018-04-23 21:28:31 INFO specflux 53 90000 36391.979337
        2.806327 0.000000e+00
      | 2018-04-23 21:28:31 INFO specflux ##### End Task: specflux
        #####
      | 2018-04-23 21:28:31 INFO specflux
        ##########################################
   
    
   
   **Example 2: **
   
   Write a spectrum of the cube "myimage.im" to the file
   "integrated_line_flux.log". A CASA region "myregion.crtf" is
   specified, in addition to a channel range (channels 15 to 25). We
   also override the cube beam parameters for the calculation by new
   values of 11 and 22 arcseconds. 
   
   ::
   
      specflux(imagename="myimage.image", region="myregion.crtf",
      chans="15~25", unit="km/s", major="11arcsec", minor="22arcsec",
      logfile="integrated_line_flux.log", overwrite=True) 
   
   The units are in K (*function="flux density"*). The CASA output
   looks like this: 
   
   ::
   
      | 2018-04-23 21:28:18 INFO specflux
        ##########################################
      | 2018-04-23 21:28:18 INFO specflux ##### Begin Task: specflux
        #####
      | 2018-04-23 21:28:18 INFO specflux
        specflux(imagename="IRC10216_HC3N.cube_r0.5.image-testK",region="",box="",chans="",stokes="",
      | 2018-04-23 21:28:18 INFO specflux
        mask="",stretch=False,function="flux
        density",unit="km/s",major="",
      | 2018-04-23 21:28:18 INFO specflux
        minor="",logfile="",overwrite=False)
      | 2018-04-23 21:28:18 INFO specflux No directional region
        specified. Using full positional plane.
      | 2018-04-23 21:28:18 INFO specflux Using all spectral
        channels.
      | 2018-04-23 21:28:18 INFO specflux Using polarizations ALL
      | 2018-04-23 21:28:18 INFO specflux Selected bounding box :
      | 2018-04-23 21:28:18 INFO specflux [0, 0, 0, 0] to [299, 299,
        0, 53] (09:48:01.492, +13.15.40.658, I, 3.63986e+10Hz to
        09:47:53.299, +13.17.40.258, I, 3.6392e+10Hz)
      | 2018-04-23 21:28:18 INFO specflux Selected bounding box :
      | 2018-04-23 21:28:18 INFO specflux [0, 0, 0, 0] to [299, 299,
        0, 53] (09:48:01.492, +13.15.40.658, I, 3.63986e+10Hz to
        09:47:53.299, +13.17.40.258, I, 3.6392e+10Hz)
      | 2018-04-23 21:28:18 INFO specflux Selected bounding box :
      | 2018-04-23 21:28:18 INFO specflux [0, 0, 0, 0] to [299, 299,
        0, 53] (09:48:01.492, +13.15.40.658, I, 3.63986e+10Hz to
        09:47:53.299, +13.17.40.258, I, 3.6392e+10Hz)
      | 2018-04-23 21:28:18 INFO specflux Selected bounding box :
      | 2018-04-23 21:28:18 INFO specflux [0, 0, 0, 0] to [299, 299,
        0, 53] (09:48:01.492, +13.15.40.658, I, 3.63986e+10Hz to
        09:47:53.299, +13.17.40.258, I, 3.6392e+10Hz)
      | 2018-04-23 21:28:18 INFO specflux Selected bounding box :
      | 2018-04-23 21:28:18 INFO specflux [0, 0, 0, 0] to [299, 299,
        0, 53] (09:48:01.492, +13.15.40.658, I, 3.63986e+10Hz to
        09:47:53.299, +13.17.40.258, I, 3.6392e+10Hz)
      | 2018-04-23 21:28:18 INFO specflux Selected bounding box :
      | 2018-04-23 21:28:18 INFO specflux [0, 0, 0, 0] to [299, 299,
        0, 53] (09:48:01.492, +13.15.40.658, I, 3.63986e+10Hz to
        09:47:53.299, +13.17.40.258, I, 3.6392e+10Hz)
      | 2018-04-23 21:28:18 INFO specflux #
        IRC10216_HC3N.cube_r0.5.image-testK, region=
      | 2018-04-23 21:28:18 INFO specflux # beam size: 5.8131035724
        arcsec2, 36.3318973275 pixels
      | 2018-04-23 21:28:18 INFO specflux # Total flux: 246.652283987
        K.arcsec2.km/s
      | 2018-04-23 21:28:18 INFO specflux # Channel
        number_of_unmasked_pixels frequency_(MHz) Velocity_(km/s)
        Flux_density_(K.arcsec2)
      | 2018-04-23 21:28:18 INFO specflux 0 90000 36398.605111
        -51.770979 7.489131e-02
      | 2018-04-23 21:28:18 INFO specflux 1 90000 36398.480096
        -50.741311 1.025246e-01
      | 2018-04-23 21:28:18 INFO specflux 2 90000 36398.355081
        -49.711639 -2.704044e-02
      | 2018-04-23 21:28:18 INFO specflux 3 90000 36398.230067
        -48.681963 -1.517969e-02
      | 2018-04-23 21:28:18 INFO specflux 4 90000 36398.105052
        -47.652284 2.767340e-02
      | 2018-04-23 21:28:18 INFO specflux 5 90000 36397.980038
        -46.622601 1.183460e-02
      | 2018-04-23 21:28:18 INFO specflux 6 90000 36397.855023
        -45.592915 -2.508908e-02
      | 2018-04-23 21:28:18 INFO specflux 7 90000 36397.730008
        -44.563226 -9.673109e-02
      | 2018-04-23 21:28:18 INFO specflux 8 90000 36397.604994
        -43.533532 8.571171e-02
      | 2018-04-23 21:28:18 INFO specflux 9 90000 36397.479979
        -42.503835 -9.778974e-04
      | 2018-04-23 21:28:18 INFO specflux 10 90000 36397.354965
        -41.474135 1.043551e+00
      | 2018-04-23 21:28:18 INFO specflux 11 90000 36397.229950
        -40.444431 5.983861e+00
      | 2018-04-23 21:28:18 INFO specflux 12 90000 36397.104935
        -39.414724 1.063841e+01
      | 2018-04-23 21:28:18 INFO specflux 13 90000 36396.979921
        -38.385013 1.294127e+01
      | 2018-04-23 21:28:18 INFO specflux 14 90000 36396.854906
        -37.355298 1.357383e+01
      | 2018-04-23 21:28:18 INFO specflux 15 90000 36396.729892
        -36.325580 1.274482e+01
      | 2018-04-23 21:28:18 INFO specflux 16 90000 36396.604877
        -35.295859 1.110862e+01
      | 2018-04-23 21:28:18 INFO specflux 17 90000 36396.479862
        -34.266134 9.332870e+00
      | 2018-04-23 21:28:18 INFO specflux 18 90000 36396.354848
        -33.236405 8.400842e+00
      | 2018-04-23 21:28:18 INFO specflux 19 90000 36396.229833
        -32.206673 7.164641e+00
      | 2018-04-23 21:28:18 INFO specflux 20 90000 36396.104819
        -31.176937 5.909610e+00
      | 2018-04-23 21:28:18 INFO specflux 21 90000 36395.979804
        -30.147198 5.066987e+00
      | 2018-04-23 21:28:18 INFO specflux 22 90000 36395.854789
        -29.117455 4.769650e+00
      | 2018-04-23 21:28:18 INFO specflux 23 90000 36395.729775
        -28.087709 4.688611e+00
      | 2018-04-23 21:28:18 INFO specflux 24 90000 36395.604760
        -27.057959 4.169048e+00
      | 2018-04-23 21:28:18 INFO specflux 25 90000 36395.479746
        -26.028205 3.926800e+00
      | 2018-04-23 21:28:18 INFO specflux 26 90000 36395.354731
        -24.998448 3.849325e+00
      | 2018-04-23 21:28:18 INFO specflux 27 90000 36395.229716
        -23.968688 3.952926e+00
      | 2018-04-23 21:28:18 INFO specflux 28 90000 36395.104702
        -22.938924 4.415877e+00
      | 2018-04-23 21:28:18 INFO specflux 29 90000 36394.979687
        -21.909156 5.172657e+00
      | 2018-04-23 21:28:18 INFO specflux 30 90000 36394.854673
        -20.879385 5.838572e+00
      | 2018-04-23 21:28:18 INFO specflux 31 90000 36394.729658
        -19.849611 6.445786e+00
      | 2018-04-23 21:28:18 INFO specflux 32 90000 36394.604643
        -18.819832 8.023103e+00
      | 2018-04-23 21:28:18 INFO specflux 33 90000 36394.479629
        -17.790051 1.043386e+01
      | 2018-04-23 21:28:18 INFO specflux 34 90000 36394.354614
        -16.760265 1.187559e+01
      | 2018-04-23 21:28:18 INFO specflux 35 90000 36394.229600
        -15.730477 1.455837e+01
      | 2018-04-23 21:28:18 INFO specflux 36 90000 36394.104585
        -14.700684 1.621557e+01
      | 2018-04-23 21:28:18 INFO specflux 37 90000 36393.979570
        -13.670888 1.639316e+01
      | 2018-04-23 21:28:18 INFO specflux 38 90000 36393.854556
        -12.641089 9.445470e+00
      | 2018-04-23 21:28:18 INFO specflux 39 90000 36393.729541
        -11.611286 1.210846e+00
      | 2018-04-23 21:28:18 INFO specflux 40 90000 36393.604527
        -10.581480 -1.601879e-01
      | 2018-04-23 21:28:18 INFO specflux 41 90000 36393.479512
        -9.551670 -8.551833e-03
      | 2018-04-23 21:28:18 INFO specflux 42 90000 36393.354497
        -8.521856 3.683259e-02
      | 2018-04-23 21:28:18 INFO specflux 43 90000 36393.229483
        -7.492039 -1.205630e-02
      | 2018-04-23 21:28:18 INFO specflux 44 90000 36393.104468
        -6.462218 -9.854151e-02
      | 2018-04-23 21:28:18 INFO specflux 45 90000 36392.979454
        -5.432394 -5.901627e-02
      | 2018-04-23 21:28:18 INFO specflux 46 90000 36392.854439
        -4.402566 1.287580e-01
      | 2018-04-23 21:28:18 INFO specflux 47 90000 36392.729424
        -3.372735 -1.625315e-03
      | 2018-04-23 21:28:18 INFO specflux 48 90000 36392.604410
        -2.342900 1.644635e-02
      | 2018-04-23 21:28:18 INFO specflux 49 90000 36392.479395
        -1.313062 2.729656e-01
      | 2018-04-23 21:28:18 INFO specflux 50 90000 36392.354381
        -0.283220 1.040732e-01
      | 2018-04-23 21:28:18 INFO specflux 51 90000 36392.229366
        0.746625 -1.264918e-01
      | 2018-04-23 21:28:18 INFO specflux 52 90000 36392.104351
        1.776474 0.000000e+00
      | 2018-04-23 21:28:18 INFO specflux 53 90000 36391.979337
        2.806327 0.000000e+00
      | 2018-04-23 21:28:18 INFO specflux ##### End Task: specflux
        #####
      | 2018-04-23 21:28:18 INFO specflux
        ##########################################
   

.. _Development:

Development
   task developer
   
   --CASA Developer--
   
   