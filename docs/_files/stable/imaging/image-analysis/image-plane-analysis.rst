.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Image Plane Analysis
====================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Source Fitting and Smoothing

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Image-plane Component Fitting (**imfit**)
         :name: image-plane-component-fitting-imfit

      The inputs are:

      .. container:: casa-input-box

         | #  imfit :: Fit one or more elliptical Gaussian components on
           an image region(s)
         | imagename           =         ''        #  Name of the input
           image
         | box                 =         ''        #  Specify one or
           more box regions for the fit.
         | region              =         ''        #  Region. 
         | chans               =         ''        #  Spectral channels
           on which to perform fit. 
         | stokes              =         ''        #  Stokes parameter
           to fit. If blank, first stokes plane is
         |                                         #   used.
         | mask                =         ''        #  Mask to use.
           Default is none.
         | includepix          =         []        #  Range of pixel
           values to include for fitting.
         | excludepix          =         []        #  Range of pixel
           values to exclude for fitting.
         | residual            =         ''        #  Name of output
           residual image.
         | model               =         ''        #  Name of output
           model image.
         | estimates           =         ''        #  Name of file
           containing initial estimates of component
         |                                         #   parameters.
         | logfile             =         ''        #  Name of file to
           write fit results.
         | newestimates        =         ''        #  File to write fit
           results which can be used as initial
         |                                         #   estimates for
           next run.
         | complist            =         ''        #  Name of output
           component list table.
         | dooff               =      False        #  Also fit a zero
           level offset? Default is False
         | rms                 =         -1        #  RMS to use in
           calculation of uncertainties. Numeric or
         |                                         #   valid quantity
           (record or string). If numeric, it is
         |                                         #   given units of
           the input image. If quantity, units must
         |                                         #   conform to image
           units. If not positive, the rms of the
         |                                         #   residual image,
           in the region of the fit, is used.
         | noisefwhm           =         ''        #  Noise correlation
           beam FWHM. If numeric value,
         |                                         #   interpreted as
           pixel widths. If quantity (dictionary,
         |                                         #   string), it must
           have angular units.

      **imfit** will return (as a Python dictionary) the results of the
      fit, but the results can also be written into a component list
      table or a logfile.

      .. container:: info-box

         **NOTE**: To fit more than a single component, you must provide
         starting estimates for each component via the *estimates* file.
         See ‘‘\ *help imfit’*\ ’ for more details on this. A noise
         estimate will be calculated automatically or can be provided
         through the *rms* and *noisefwhm* keywords.

       

      .. rubric:: Examples for **imfit**
         :name: examples-for-imfit

      .. container:: casa-input-box

         | # First fit only a single component at a time
         | # This is OK since the components are well-separated and not
           blended
         | # Box around component A
         | xfit_A_res =
           imfit('b1608.demo.clean2.image',box='121,121,136,136',
         |                   
           newestimates='b1608.demo.clean2.newestimate')
         | # Now extract the fit part of the return value
         | xfit_A = xfit_A_res['results']['component0']
         | #xfit_A
         | #  Out[7]:
         | #{'flux': {'error': array([  6.73398035e-05,  
           0.00000000e+00,   0.00000000e+00,
         | #         0.00000000e+00]),
         | #          'polarisation': 'Stokes',
         | #          'unit': 'Jy',
         | #          'value': array([ 0.01753742,  0.        , 
           0.        ,  0.        ])},
         | # 'label': '',
         | # 'shape': {'direction': {'error': {'latitude': {'unit':
           'arcsec',
         | #                                                'value':
           0.00041154866279462775},
         | #                                   'longitude': {'unit':
           'arcsec',
         | #                                                 'value':
           0.00046695916589535109}},
         | #                         'm0': {'unit': 'rad', 'value':
           -2.0541102061078207},       NOTE: 'm0' and 'm1' are the
           coordinates of peak/controid
         | #                         'm1': {'unit': 'rad', 'value':
           1.1439131060384089},        NOTE: 'm0' and 'm1' are the
           coordinates of peak/controid
         | #                         'refer': 'J2000',
         | #                         'type': 'direction'},
         | #           'majoraxis': {'unit': 'arcsec', 'value':
           0.29100166137741568},
         | #           'majoraxiserror': {'unit': 'arcsec',
         | #                              'value':
           0.0011186420613222663},
         | #           'minoraxis': {'unit': 'arcsec', 'value':
           0.24738110059830495},
         | #           'minoraxiserror': {'unit': 'arcsec',
         | #                              'value':
           0.0013431999725066338},
         | #           'positionangle': {'unit': 'deg', 'value':
           19.369249322401796},
         | #           'positionangleerror': {'unit': 'rad',
         | #                                  'value':
           0.016663189295782171},
         | #           'type': 'Gaussian'},
         | # 'spectrum': {'frequency': {'m0': {'unit': 'GHz', 'value':
           1.0},
         | #                            'refer': 'LSRK',
         | #                            'type': 'frequency'},
         | #              'type': 'Constant'}}
         | # Now the other components
         | xfit_B_res =
           imfit('b1608.demo.clean2.image',box='108,114,120,126',
         |                   
           newestimates='b1608.demo.clean2.newestimate',append=True)
         | xfit_B = xfit_B_res['results']['component0']
         | xfit_C_res=
           imfit('b1608.demo.clean2.image',box='108,84,120,96')
         | xfit_C = xfit_C_res['results']['component0']
         | xfit_D_res =
           imfit('b1608.demo.clean2.image',box='144,98,157,110')
         | xfit_D = xfit_D_res['results']['component0']
         | print ""
         | print "Imfit Results:"
         | print "--------------"
         | print "A  Flux = %6.4f Bmaj = %6.4f" %
           (xfit_A['flux']['value'][0],xfit_A['shape']['majoraxis']['value'])
         | print "B  Flux = %6.4f Bmaj = %6.4f" %
           (xfit_B['flux']['value'][0],xfit_B['shape']['majoraxis']['value'])
         | print "C  Flux = %6.4f Bmaj = %6.4f" %
           (xfit_C['flux']['value'][0],xfit_C['shape']['majoraxis']['value'])
         | print "D  Flux = %6.4f Bmaj = %6.4f" %
           (xfit_D['flux']['value'][0],xfit_D['shape']['majoraxis']['value'])
         | print ""

      Now try fitting four components together. For this we will have to
      provide an estimate file. We will use the clean beam for the
      estimate of the component sizes:

      .. container:: casa-input-box

         | estfile=open('b1608.demo.clean2.estimate','w')
         | print >>estfile,'# peak, x, y, bmaj, bmin, bpa'
         | print >>estfile,'0.017, 128, 129, 0.293arcsec, 0.238arcsec,
           21.7deg'
         | print >>estfile,'0.008, 113, 120, 0.293arcsec, 0.238arcsec,
           21.7deg'
         | print >>estfile,'0.008, 113,  90, 0.293arcsec, 0.238arcsec,
           21.7deg'
         | print >>estfile,'0.002, 151, 104, 0.293arcsec, 0.238arcsec,
           21.7deg'
         | estfile.close()

      Then, this can be used in **imfit**:

      .. container:: casa-input-box

         | fit_all_res = imfit('b1608.demo.clean2.image',
         |                      estimates='b1608.demo.clean2.estimate',
         |                     
           logfile='b1608.demo.clean2.imfitall.log',
         |                     
           newestimates='b1608.demo.clean2.newestimate',
         |                     
           box='121,121,136,136,108,114,120,126,108,84,120,96,144,98,157,110')
         | # Now extract the fit part of the return values
         | xfit_allA = xfit_all_res['results']['component0']
         | xfit_allB = xfit_all_res['results']['component1']
         | xfit_allC = xfit_all_res['results']['component2']
         | xfit_allD = xfit_all_res['results']['component3']

      These results are almost identical to those from the individual
      fits. You can see a nicer printout of the fit results in the
      logfile.

       

      .. rubric:: 2-dimensional Smoothing; Image Convolution (imsmooth)
         :name: dimensional-smoothing-image-convolution-imsmooth

      A data cube can be smoothed across spatial dimensions with
      **imsmooth**. The inputs are:

      .. container:: casa-input-box

         | #  imsmooth :: Smooth an image or portion of an image
         | imagename           =         ''        #  Name of the input
           image. Must be
         |                                         #   specified.
         | kernel              =    'gauss'        #  Type of kernel to
           use. Acceptable values
         |                                         #   are 'b', 'box',
           or 'boxcar' for a
         |                                         #   boxcar kernel,
           'g', 'gauss', or
         |                                         #   'gaussian' for a
           gaussian kernel, 'c',
         |                                         #   'common', or
           'commonbeam' to use the
         |                                         #   common beam of an
           image with multiple
         |                                         #   beams as the
           gaussian to which to
         |                                         #   convolve all the
           planes, 'i' or 'image'
         |                                         #   to use an image
           as the kernel.
         |      beam           =         ''        #  Alternate way of
           describing a Gaussian.
         |                                         #   If specified,
           must be a dictionary with
         |                                         #   keys 'major',
           'minor', and 'pa' (or
         |                                         #   'positionangle').
           Do not specify beam
         |                                         #   if specifying
           major, minor, and pa.
         |                                         #   Example: Example:
           {'major': '5arcsec',
         |                                         #   'minor':
           '2arcsec', 'pa': '20deg'}.
         |      targetres      =      False        #  If gaussian
           kernel, specified parameters
         |                                         #   are to be
           resolution of output image
         |                                         #   (True) or
           parameters of gaussian to
         |                                         #   convolve with
           input image (False).
         |      major          =         ''        #  Major axis for the
           kernels. Standard
         |                                         #   quantity
           representation. Must be
         |                                         #   specified for
           kernel='boxcar'. Example:
         |                                         #   '4arcsec'.
         |      minor          =         ''        #  Minor axis.
           Standard quantity
         |                                         #   representation.
           Must be specified for
         |                                         #   kernel='boxcar'.
           Example: '2arcsec'.
         |      pa             =         ''        #  Position angle
           used only for gaussian
         |                                         #   kernel. Standard
           quantity
         |                                         #   representation.
           Example: '40deg'.
         | region              =         ''        #  Region selection.
           See Default is to use the full
         |                                         #   image.
         | box                 =         ''        #  Rectangular region
           to select in
         |                                         #   direction plane.
           Default is to use the entire
         |                                         #   direction plane.
         | chans               =         ''        #  Channels to use.
           Default is to use all
         |                                         #   channels.
         | stokes              =         ''        #  Stokes planes to
           use.  Default is to
         |                                         #   use all Stokes
           planes.
         | mask                =         ''        #  Mask to use.
           Default
         |                                         #   is none.
         | outfile             =         ''        #  Output image name.
           Must be specified.
         | overwrite           =      False        #  Overwrite
           (unprompted) pre-existing
         |                                         #   output file?

      | where the cube/image imagename will be convolved with a kernel
        defined in the *kernel* keyword. Kernels '*gauss'* and
        '*boxcar'* need the major and minor axes sizes as input, the
        Gaussian kernel smoothing also requires a position angle. By
        default, the kernel size defines the kernel itself, i.e. the
        data will be smoothed with this *kernel*. If the *targetres*
        parameter for Gaussian kernels is set to '*True'*, major and
        minor axes will be those from the output resolution, and the
        kernel will be adjusted for each plane to arrive at the final
        resolution. The ’commonbeam’ kernel is to be used when the beam
        shape is different as a function of frequency. This option will
        then smooth all planes to a single beam, defined by the largest
        beam in the cube. With the '*image'* kernel, one can specify an
        image that will serve as the convolution kernel. A scale factor
        can be applied, which defaults to flux conservation where units
        are Jy/beam or Jy/beam.km/s. For all other units, like K, the
        output will be scaled by the inverse of the convolution kernel.
        e.g., in the extreme case of a flat distribution the values
        before and after smoothing will be the same.
      | Examples:
      | 1) Smoothing with a Gaussian kernel 20” by 10”

      .. container:: casa-input-box

         imsmooth( imagename='my.image', kernel='gauss',
         major='20arcsec', minor='10arcsec',targetres=T)

      2) Smoothing using pixel coordinates and a boxcar kernel.

      .. container:: casa-input-box

         imsmooth( imagename='new.image', major='20pix', minor='10pix',
         kernel='boxcar')

      .. rubric::  
         :name: section

       

.. container:: section
   :name: viewlet-below-content-body
