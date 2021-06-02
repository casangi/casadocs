

.. _Description:

Description
   The spectral moment distributions at each pixel are
   determined. The main control of the calculation is given by the
   parameter *moments*:
   
   -  moments = -1 - mean value of the spectrum
   -  moments =  0 - integrated value of the spectrum
   -  moments =  1 - intensity weighted coordinate; traditionally
      used to get "velocity fields"
   -  moments =  2 - intensity weighted dispersion of the coordinate;
      traditionally used to get "velocity dispersion"
   -  moments =  3 - median value of the spectrum
   -  moments =  4 - median coordinate
   -  moments =  5 - standard deviation about the mean of the
      spectrum
   -  moments =  6 - root mean square of the spectrum
   -  moments =  7 - absolute mean deviation of the spectrum
   -  moments =  8 - maximum value of the spectrum
   -  moments =  9 - coordinate of the maximum value of the spectrum
   -  moments = 10 - minimum value of the spectrum
   -  moments = 11 - coordinate of the minimum value of the spectrum
   
   The default value of *outfile* is the input image name appended by
   an auto-determined suffix.
   
   If *stretch=True* and if the number of mask dimensions is less
   than or equal to the number of image dimensions and some axes in
   the mask are degenerate while the corresponding axes in the image
   are not, the mask will be stetched in the degenerate axis
   dimensions. For example, if the input image has shape [100, 200,
   10] and the input mask has shape [100, 200, 1] and *stretch=True*,
   the mask will be stretched along the third dimension to shape
   [100, 200, 10]. However if the mask is shape [100, 200, 2],
   stretching is not possible and an error will result.
   
   If an image has multiple per-channel beams and the moment axis is
   equal to the spectral axis, each channel will be convolved with a
   beam that has a minimum area necessary to contain each of the
   image beams, ie, it is the minimum area common beam to which all
   the beams in the image can be convolved.
    
   
   .. rubric:: Task-specific parameter summary

   *moments*
   
   List of moments to compute. See above for details.
   
   *axis*
   
   Axis along which to compute the specified moments.
   
   *includepix*

   Range of pixel values to include in the computation. A range can
   only be given for one of includepix or excludepix.
   
   *excludepix*
   
   Range of pixel values to exclude in the computation. A range can
   only be given for one of includepix or excludepix.
   

.. _Examples:

Examples
   Example for creating the "moment 1" map, a map of the
   intensity-weighted mean spectral axis value, which is often used
   for finding velocity fields:
   
   ::
   
      immoments(axis='spec', imagename='myimage', moments=[1],
                outfile='velocityfields')
   
   Example for finding the spectral mean, -1 moment, on a specified
   region of the image as defined by the *box* and *stokes*
   parameters:
   
   ::
   
      taskname='immoments'
      default()
      imagename = 'myimage'
      moments = [-1]
      axis = 'spec'
      stokes = 'I'
      box = '55,12,97,32'
      go
   
   Example using a box
   
   ::
   
      immoments('clean.image', axis='spec', box="40,40,120,120",
                outfile='mom_withmask.im')
   
   Example using a CRTF elliptical region with specified axis lengths
   and a position angle of 30 degrees.
   
   ::
   
      immoments('clean.image', axis='spec',
                region="ellipse[[00:00:13.47460, +000.02.20.3571],
                [10arcsec,15arcsec], 30deg]", outfile='mom_withmask.im')
   
   Example using a mask created with a second file to select the data
   used to calculate the 0-moment, integrated values. In this case,
   the mask is from the calibrated.im file and all values that have a
   value greater than 0.5 will be positive in the mask:
   
   ::
   
      immoments('clean.image', axis='spec',
                mask='"calibrated.im">0.5', outfile='mom_withmask.im')
   

.. _Development:

Development
   No additional development details

