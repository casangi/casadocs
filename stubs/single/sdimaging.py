#
# stub function definition file for docstring parsing
#

def sdimaging(infiles, outfile='', overwrite=False, field='', spw='', antenna='', scan='', intent='OBSERVE_TARGET#ON_SOURCE', mode='channel', nchan=-1, start='0', width='1', veltype='radio', outframe='', gridfunction='BOX', convsupport=-1, truncate='-1', gwidth='-1', jwidth='-1', imsize=[''], cell='', phasecenter='', projection='SIN', ephemsrcname='', pointingcolumn='direction', restfreq='', stokes='', minweight=0.1, brightnessunit='', clipminmax=False):
    r"""
SD task: imaging for total power and spectral data

Parameters
   - **infiles** (stringArray) - a list of names of input SD Measurementsets (only MS is allowed for this task) [1]_
   - **outfile** (string='') - name of output image [2]_
   - **overwrite** (bool=False) - overwrite the output file if already exists [True, False] [3]_
   - **field** ({string, stringArray}='') - select data by field IDs and names, e.g. "3C2*" (""=all) [4]_
   - **spw** ({string, stringArray}='') - select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all) [5]_
   - **antenna** ({string, stringArray}='') - select data by antenna names or IDs, e.g, "PM03" ("" = all antennas) [6]_
   - **scan** ({string, stringArray}='') - select data by scan numbers, e.g. "21~23" (""=all) [7]_
   - **intent** ({string, stringArray}='OBSERVE_TARGET#ON_SOURCE') - select data by observational intent, e.g. "*ON_SOURCE*" (""=all) [8]_
   - **mode** (string='channel') - spectral gridding type ["channel", "frequency", "velocity"] [9]_

      .. raw:: html

         <details><summary><i> mode = channel </i></summary>

      - **nchan** (int=-1) -  number of channels (planes) in output image (-1=all) [10]_
      - **start** ({string, int}='0') - start of output spectral dimension, e.g. "0", "110GHz", "-20km/s" [11]_
      - **width** ({string, int}='1') - width of output spectral channels [12]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = frequency </i></summary>

      - **nchan** (int=-1) -  number of channels (planes) in output image (-1=all) [10]_
      - **start** ({string, int}='0') - start of output spectral dimension, e.g. "0", "110GHz", "-20km/s" [11]_
      - **width** ({string, int}='1') - width of output spectral channels [12]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = velocity </i></summary>

      - **nchan** (int=-1) -  number of channels (planes) in output image (-1=all) [10]_
      - **start** ({string, int}='0') - start of output spectral dimension, e.g. "0", "110GHz", "-20km/s" [11]_
      - **width** ({string, int}='1') - width of output spectral channels [12]_
      - **veltype** (string='radio') - velocity definition ["radio", "optical", "true" or "relativistic"]  [13]_

      .. raw:: html

         </details>
   - **outframe** (string='') - velocity frame of output image ["lsrk", "lsrd", "bary", "geo", "topo", "galacto", "lgroup", "cmb"] (""=current frame or LSRK for multiple-MS inputs)  [14]_
   - **gridfunction** (string='BOX') - gridding function for imaging ["BOX", "SF", "PB", "GAUSS" or "GJINC"] (see description in help) [15]_

      .. raw:: html

         <details><summary><i> gridfunction = SF </i></summary>

      - **convsupport** (int=-1) - convolution support for gridding [16]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> gridfunction = sf </i></summary>

      - **convsupport** (int=-1) - convolution support for gridding [16]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> gridfunction = GAUSS </i></summary>

      - **truncate** ({string, int, double}='-1') - truncation radius for gridding [17]_
      - **gwidth** ({string, int, double}='-1') - HWHM for gaussian [18]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> gridfunction = gauss </i></summary>

      - **truncate** ({string, int, double}='-1') - truncation radius for gridding [17]_
      - **gwidth** ({string, int, double}='-1') - HWHM for gaussian [18]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> gridfunction = GJINC </i></summary>

      - **truncate** ({string, int, double}='-1') - truncation radius for gridding [17]_
      - **gwidth** ({string, int, double}='-1') - HWHM for gaussian [18]_
      - **jwidth** ({string, int, double}='-1') - c-parameter for jinc function [19]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> gridfunction = gjinc </i></summary>

      - **truncate** ({string, int, double}='-1') - truncation radius for gridding [17]_
      - **gwidth** ({string, int, double}='-1') - HWHM for gaussian [18]_
      - **jwidth** ({string, int, double}='-1') - c-parameter for jinc function [19]_

      .. raw:: html

         </details>
   - **imsize** ({intArray, doubleArray}=['']) - x and y image size in pixels, e.g., [64,64]. Single value: same for both spatial axes ([] = number of pixels to cover whole pointings in MSes) [20]_
   - **cell** ({string, stringArray, doubleArray}='') - x and y cell size, (e.g., ["8arcsec","8arcsec"]. default unit arcmin. ("" = 1/3 of FWHM of primary beam) [21]_
   - **phasecenter** (variant='') - image center direction: position or field index, e.g., "J2000 17:30:15.0 -25.30.00.0". ("" = the center of pointing directions in MSes) [22]_
   - **projection** (string='SIN') - map projection type [23]_
   - **ephemsrcname** (string='') - ephemeris source name, e.g. "MARS" [24]_
   - **pointingcolumn** (string='direction') - pointing data column to use ["direction", "target", "pointing_offset", "source_offset" or "encoder"] [25]_
   - **restfreq** ({string, double}='') - rest frequency to assign to image, e.g., "114.5GHz" [26]_
   - **stokes** (string='') - stokes parameters or polarization types to image, e.g. "I", "XX" [27]_
   - **minweight** (double=0.1) - Minimum weight ratio to use [28]_
   - **brightnessunit** (string='') - Overwrite the brightness unit in image (\'\' = respect the unit in MS) [\'K\' or \'Jy/beam\'] [29]_
   - **clipminmax** (bool=False) - Clip minimum and maximum value from each pixel [30]_


Description
   | This task grids/images total power and spectral data according
     to a specified gridding kernel. The input data should be
     calibrated and bandpass corrected (where necessary), and the
     output is a CASA image format dataset, either 2-d, 3-d, or 4-d
     depending on the input parameters.
   | 

   The output image contains up to four axes: two spatial axes,
   frequency, and polarization. By default, the spatial coordinates
   are determined such that the imaged area is covered with a cell
   size equal to 1/3 of the FWHM of the primary beam of antennas in
   the first MS. It is also possible to define the spatial axes of
   the image by specifying the image center direction
   (*phasecenter*), the number of image pixels (*imsize*), and the
   pixel size (*cell*).

   | 
   | The frequency coordinate of the image is defined by three
     parameters: the number of channels (*nchan*), the channel
     number/frequency/velocity of the first channel (*start*), and
     the channel width (*width*). The *start* and *width* parameters
     can be in units of 'channel' (use channel number), 'frequency'
     (e.g., 'GHz'), or 'velocity' (e.g., 'km/s'). By default,
     *nchan*, *start*, and *width* are set so that all selected
     spectral windows are covered with a channel width equal to the
     separation of the first two channels selected.
   | Finally, the polarization axis of the image is determined by the
     *stokes* parameter. For example, *stokes* ='XXYY' produces an
     image cube with each plane containing the image of one of the
     polarizations, while stokes='I' produces a "total intensity", or
     Stokes I image.

   The parameter *gridfunction* sets the gridding function
   (convolution kernel) for imaging. Currently, the task supports
   'BOX' (boxcar), 'SF' (Prolate Spheroidal Wave Function), 'GAUSS'
   (Gaussian), 'GJINC' (Gaussian*Jinc), where Jinc(x) =
   :math:`J_1(π*x/c)/(π*x/c)` with a first order Bessel function J_1,
   and 'PB' (Primary Beam).

   | There are four subparameters for *gridfunction*: *convsupport,
     truncate, gwidth*, and *jwidth*. The *convsupport* parameter is
     an integer specifying the cutoff radius for 'SF' in units of
     pixels. By default (*convsupport* =-1), the cutoff radius is 3
     pixels. The *truncate* parameter is a cutoff radius for 'GAUSS'
     or 'GJINC'. It accepts integer, float, and string values, where
     the string would be a number plus unit. Allowed units include
     'deg', 'arcmin', 'arcsec', and 'pixel'. The default is 'pixel'.
     The default value for *truncate*, which is used when a negative
     radius is set, is 3*HWHM for 'GAUSS', and the radius at the
     first null for 'GJINC'. The *gwidth* is the HWHM of the Gaussian
     for 'GAUSS' and 'GJINC'. The default value is sqrt(log(2))
     pixels for 'GAUSS' and 2.52*sqrt(log(2)) pixels for 'GJINC'. The
     *jwidth* specifies the width of the jinc function (parameter 'c'
     in the definition above). The default is 1.55 pixels. Both
     *gwidth* and *jwidth* allow integer, float, or string values,
     where the string would be a number plus unit. The default
     values for *gwidth* and *jwidth* are taken from Mangum, et al.
     2007 `[1] <#cit1>`__ . The formula for 'GAUSS' and 'GJINC' are
     taken from Table 1 in the paper, and are written as follows
     using *gwidth* and *jwidth*:
   |  GAUSS: :math:`\exp[-\log(2)*(|r|/gwidth)^2]`
   |  GJINC:
     :math:`J_1(π*|r|/jwidth)/(π*|r|/jwidth)* \exp[-\log(2)*(|r|/gwidth)^2]`

   The *imagename* should be unique. Clean will stop with an
   Exception error (e.g. Exception: Unable to open lattice) if
   *imagename* is the same as the *vis* name. 

   | The *ephemsrcname* parameter can be set to specifiy an ephemeris
     for a moving source (solar sytem objects). If the source name
     in the data matches one of the solar system objects known by
     CASA, the imaging realigns the data by shifting the source, so
     that the source appears to be fixed in the image.
   | The *clipminmax* function can clip minimum and maximum value
     from each pixel. This function makes the computed output
     slightly more robust to noise and spurious data. Note the
     benefit of clipping is lost when the number of integrations
     contributing to each gridded pixel is small, or where the
     incidence of spurious data points is approximately equal to or
     greater than the number of beams (in area) encompassed by the
     expected image.

   The *minweight* parameter defines a threshold of weight values to
   mask. The pixels in *outfile* whose weight is smaller than
   *minweight* \*median (*weight*) are masked out. The task also
   creates a weight image with the name outfile.weight.

   The *projection* parameter allows to specify what kind of map
   projection is applied. The default is SIN (slant orthographic)
   projection. Besides that, the task supports CAR (plate carrée),
   TAN (gnomonic), and SFL (Sanson-Flamsteed).

   .. rubric:: Bibliography


   Bibliography
      :sup:`1. Mangum, et al. 2007, A&A, 474,
      679-687` `(A&A) <http://www.aanda.org/articles/aa/pdf/2007/41/aa7811-07.pdf>`__ `<#ref-cit1>`__




Details
   Explanation of each parameter

.. [1] 
   **infiles** (stringArray)
      | a list of names of input SD Measurementsets (only MS is allowed for this task)
.. [2] 
   **outfile** (string='')
      | name of output image
.. [3] 
   **overwrite** (bool=False)
      | overwrite the output file if already exists [True, False]
.. [4] 
   **field** ({string, stringArray}='')
      | select data by field IDs and names, e.g. "3C2*" (""=all)
.. [5] 
   **spw** ({string, stringArray}='')
      | select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all)
.. [6] 
   **antenna** ({string, stringArray}='')
      | select data by antenna names or IDs, e.g, "PM03" ("" = all antennas)
.. [7] 
   **scan** ({string, stringArray}='')
      | select data by scan numbers, e.g. "21~23" (""=all)
.. [8] 
   **intent** ({string, stringArray}='OBSERVE_TARGET#ON_SOURCE')
      | select data by observational intent, e.g. "*ON_SOURCE*" (""=all)
.. [9] 
   **mode** (string='channel')
      | spectral gridding type
.. [10] 
   **nchan** (int=-1)
      | number of channels (planes) in output image (-1=all)
.. [11] 
   **start** ({string, int}='0')
      | start of output spectral dimension, e.g. "0", "110GHz", "-20km/s"
.. [12] 
   **width** ({string, int}='1')
      | width of output spectral channels
.. [13] 
   **veltype** (string='radio')
      | velocity definition
.. [14] 
   **outframe** (string='')
      | velocity frame of output image (""=current frame or LSRK for multiple-MS inputs)
.. [15] 
   **gridfunction** (string='BOX')
      | gridding function for imaging (see description in help)
.. [16] 
   **convsupport** (int=-1)
      | convolution support for gridding
.. [17] 
   **truncate** ({string, int, double}='-1')
      | truncation radius for gridding
.. [18] 
   **gwidth** ({string, int, double}='-1')
      | HWHM for gaussian
.. [19] 
   **jwidth** ({string, int, double}='-1')
      | c-parameter for jinc function
.. [20] 
   **imsize** ({intArray, doubleArray}=[''])
      | x and y image size in pixels, e.g., [64,64]. Single value: same for both spatial axes ([] = number of pixels to cover whole pointings in MSes)
.. [21] 
   **cell** ({string, stringArray, doubleArray}='')
      | x and y cell size, (e.g., ["8arcsec","8arcsec"]. default unit arcmin. ("" = 1/3 of FWHM of primary beam)
.. [22] 
   **phasecenter** (variant='')
      | image center direction: position or field index, e.g., "J2000 17:30:15.0 -25.30.00.0". ("" = the center of pointing directions in MSes)
.. [23] 
   **projection** (string='SIN')
      | map projection type
.. [24] 
   **ephemsrcname** (string='')
      | ephemeris source name, e.g. "MARS"
.. [25] 
   **pointingcolumn** (string='direction')
      | pointing data column to use
.. [26] 
   **restfreq** ({string, double}='')
      | rest frequency to assign to image, e.g., "114.5GHz"
.. [27] 
   **stokes** (string='')
      | stokes parameters or polarization types to image, e.g. "I", "XX"
.. [28] 
   **minweight** (double=0.1)
      | Minimum weight ratio to the median of weight used in weight correction and weight beased masking
.. [29] 
   **brightnessunit** (string='')
      | Overwrite the brightness unit in image (\'\' = respect the unit in MS) [\'K\' or \'Jy/beam\']
.. [30] 
   **clipminmax** (bool=False)
      | Clip minimum and maximum value from each pixel. Note the benefit of clipping is lost when the number of integrations contributing to each gridded pixel is small, or where the incidence of spurious datapoints is approximately or greater than the number of beams (in area) encompassed by expected image.

    """
    pass
