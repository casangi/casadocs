#
# stub function definition file for docstring parsing
#

def imfit(imagename, box='', region='', chans='', stokes='', mask='', includepix=[''], excludepix=[''], residual='', model='', estimates='', logfile='', append=True, newestimates='', complist='', overwrite=False, dooff=False, offset=0.0, fixoffset=False, stretch=False, rms='-1', noisefwhm='', summary=''):
    r"""
Fit one or more elliptical Gaussian components on an image region(s)

Parameters
   - **imagename** (string) - Name of the input image
   - **box** (string='') - Rectangular region(s) to select in direction plane. Default is to use the entire direction plane.
   - **region** (variant='') - Region selection. Default is to use the full image.
   - **chans** (variant='') - Channels to use. Default is to use all channels.
   - **stokes** (string='') - Stokes planes to use. Default is to use first Stokes plane.
   - **mask** (string='') - Mask to use. Default is none.
   - **includepix** (intArray=['']) - Range of pixel values to include for fitting.
   - **excludepix** (intArray=['']) - Range of pixel values to exclude for fitting.
   - **residual** (string='') - Name of output residual image.
   - **model** (string='') - Name of output model image.
   - **estimates** (string='') - Name of file containing initial estimates of component parameters.
   - **logfile** (string='') - Name of file to write fit results.
   - **newestimates** (string='') - File to write fit results which can be used as initial estimates for next run.
   - **complist** (string='') - Name of output component list table.
   - **dooff** (bool=False) - Also fit a zero level offset? Default is False
   - **rms** ({int, double, record, string}='-1') - RMS to use in calculation of uncertainties. Numeric or valid quantity (record or string). If numeric, it is given units of the input image. If quantity, units must conform to image units. If not positive, the rms of the residual image, in the region of the fit, is used.
   - **noisefwhm** ({int, double, record, string}='') - Noise correlation beam FWHM. If numeric value, interpreted as pixel widths. If quantity (dictionary, string), it must have angular units.
   - **summary** (string='') - File name to which to write table of fit parameters.


Description
      .. rubric:: OVERVIEW
         :name: overview

      This application is used to fit one or more two dimensional
      Gaussians to sources in an image as well as an optional zero-level
      offset. Fitting is limited to a single polarization but can be
      performed over several contiguous spectral channels. If the image
      has a clean beam, the report and returned dictionary will contain
      both the convolved and the deconvolved fit results. For examples
      and explanation of the dictionary, see the `Image Plane
      Analysis <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/image-plane-analysis>`__
      pages.

       

      When dooff is False, the method returns a dictionary with keys
      named 'converged', 'pixelsperarcsec', 'results', and
      'deconvolved'. The value of 'converged' is a boolean array which
      indicates if the fit converged on a channel by channel basis. The
      value of 'pixelsperarcsec' is a two element double array with the
      absolute values of the direction coordinate pixel increments
      (longitude-like and latitude-like coordinate, respectively) in
      arcsec. The value of 'results' is a dictionary representing a
      component list reflecting the fit results. In the case of an image
      containing beam information, the sizes and position angles in the
      'results' dictionary are those of the source(s) convolved with the
      restoring beam, while the same parameters in the 'deconvolved'
      dictionary represent the source sizes deconvolved from the beam.
      In the case where the image does not contain a beam, 'deconvolved'
      will be absent. Both the 'results' and 'deconvolved' dictionaries
      can be read into a component list tool (default tool is named cl)
      using the fromrecord() method for easier inspection using tool
      methods, eg

      .. note:: cl.fromrecord(res['results'])

       

      although this only works if the flux density units are conformant
      with Jy.

      There are also values in each component subdictionary not used by
      **cl.fromrecord()** but meant to supply additional information.
      There is a 'peak' subdictionary for each component that provides
      the peak intensity of the component. It is present for both
      'results' and 'deconvolved' components. There is also a 'sum'
      subdictionary for each component indicating the simple sum of
      pixel values in the the original image enclosed by the fitted
      ellipse. There is a 'channel' entry in the 'spectrum'
      subdictionary which provides the zero-based channel number in the
      input image for which the solution applies. In addtion, if the
      image has a beam(s), then there will be a 'beam' subdictionary
      associated with each component in both the 'results' and
      'deconvolved' dictionaries. This subdictionary will have three
      keys: '*beamarcsec*' will be a subdictionary giving the beam
      dimensions in arcsec, '*beampixels*' will have the value of the
      beam area expressed in pixels, and '*beamster*' will have the
      value of the beam area expressed in steradians. Also, if the image
      has a beam(s), in the component level dictionaries will be an
      'ispoint' entry with an associated boolean value describing if the
      component is consistent with a point source. Each component level
      dictionary will have a 'pixelcoords' entry which has the value of
      a two element numeric array which provides the direction pixel
      coordinates of the fitted position.

      If *dooff* is True, in addition to the specified number of
      Gaussians, a zero level offset will also be fit. The initial
      estimate for this offset is specified using the *offset*
      parameter. Units are assumed to be the same as the image
      brightness units. The zero level offset can be held constant
      during the fit by specifying *fixoffset=True*. In the case of
      *dooff=True*, the returned dictionary contains two additional
      keys, '*zerooff*' and '*zeroofferr*', which are both dictionaries
      containing '*unit*' and '*value*' keys. The values associated with
      the '*value*' keys are arrays containing the fitted zero level
      offset value and its error, respectively, for each channel. In
      cases where the fit did not converge, these values are set to NaN.
      The value associated with '*unit*' is just the image brightness
      unit.

      The region can either be specified by a *box(es)* or a *region*.
      Ranges of pixel values can be included or excluded from the fit.
      If specified using the *box* parameter, multiple boxes can be
      given using the format *box* ="blcx1, blcy1, trcx1, trcy1, blcx2,
      blcy2, trcx2, trcy2, ... , blcxN, blcyN, trcxN, trcyN" where N is
      the number of boxes. In this case, the union of the specified
      boxes will be used.

      The default behavior of imfit is to fit a single Gaussian
      component. If a multiple-Gaussian fit is desired, the user must
      specify initial estimates via a text file (see below for details).
      If no estimate file is specified, imfit will attempt to guess the
      initial parameters and fit a single Gaussian to the union of
      specified boxes/regions. Users who wish to perform individual fits
      to separate regions should run imfit multiple times, specifying a
      single input box/region each time.

      If specified, the *residual* and/or *model* images for successful
      fits will be written.

      The user has the option of writing the result of the fit to a log
      file, and has the option of either appending to or overwriting an
      existing file.

      The user has the option of writing the (convolved) parameters of a
      successful fit to a file which can be fed back to **imfit** as the
      new estimates file for a subsequent run.

      The user has the option of writing the fit results in tabular
      format to a file whose name is specified using the *summary*
      parameter.

      If specified and positive, the value of *rms* is used to calculate
      the parameter uncertainties, otherwise, the rms in the selected
      region in the relevant channel is used for these calculations.

      The *noisefwhm* parameter represents the noise-correlation beam
      FWHM. If specified as a quantity, it should have angular units. If
      specified as a numerical value, it is set equal to that number of
      pixels. If specified and greater than or equal to the pixel size,
      it is used to calculate parameter uncertainties using the
      correlated noise equations (see below). If it is specified but
      less than a pixel width, the uncorrelated noise equations (see
      below) are used to compute the parameter uncertainties. If it is
      not specified and the image has a restoring beam(s), the
      correlated noise equations are used to compute parameter
      uncertainties using the geometric mean of the relevant beam major
      and minor axes as the noise-correlation beam FWHM. If *noisefwhm*
      is not specified and the image does not have a restoring beam,
      then the uncorrelated noise equations are used to compute the
      parameter uncertainties.

      .. rubric:: SUPPORTED UNITS
         :name: supported-units

      Currently only images with brightness units conformant with
      Jy/beam, Jy/beam km/s, and K are fully supported for fitting. If
      your image has some other base brightness unit, that unit will be
      assumed to be equivalent to Jy/pixel and results will be
      calculated accordingly. In particular, the flux density (reported
      as Integrated Flux in the logger and associated with the "flux"
      key in the returned component subdictionary(ies)) for such a case
      represents the sum of pixel values.

      Note also that converting the returned results subdictionary to a
      component list via **cl.fromrecord()** currently only works
      properly if the flux density units in the results dictionary are
      conformant with Jy. If you need to be able to run
      **cl.fromrecord()** on the resulting dictionary you can first
      modify the flux density units by hand to be (some prefix)Jy and
      then run cl.fromrecord() on that dictionary, bearing in mind your
      unit conversion.

      If the input image has units of K, the flux density of components
      will be reported in units of [prefix]K*rad*rad, where prefix is an
      SI prefix used so that the numerical value is between 1 and 1000.
      To convert to units of K*beam, determine the area of the
      appropriate beam, which is given by

      .. math:: \begin{equation} \frac{\pi}{4 \rm{ln} 2} \, b_{\rm maj} \,b_{\rm min} \end{equation}

      where :math:` b_{\rm maj}` and :math:`b_{\rm min}` are the major
      and minor axes of the beam, and convert to steradians (=rad*rad).
      This value is included in the beam portion of the component
      subdictionary (key '*beamster*'). Then divide the numerical value
      of the logged flux density by the beam area in steradians. So, for
      example

      .. note:: | # run on an image with K brightness units
         | res = imfit(...)
         | # get the I flux density in K*beam of component 0
         | comp = res['results']['component0']
         | flux_density_kbeam =
           comp['flux']['value'][0]/comp['beam']['beamster']

       

      .. rubric:: FITTING OVER MULTIPLE CHANNELS
         :name: fitting-over-multiple-channels

      For fitting over multiple channels, the result of the previous
      successful fit is used as the estimate for the next channel. The
      number of Gaussians fit cannot be varied on a channel by channel
      basis. Thus the variation of source structure should be reasonably
      smooth in frequency to produce reliable fit results.

      .. rubric:: MASK SPECIFICATION
         :name: mask-specification

      `Mask <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/image-masks>`__
      specification can be done using an `LEL
      expression <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/lattice-expression-language-lel/lattice-expression-language>`__.
      For example

      .. note:: mask = "myimage>5"

      will use only pixels with values greater than 5.

      .. rubric:: INCLUDING AND EXCLUDING PIXELS
         :name: including-and-excluding-pixels

      Pixels can be included or excluded from the fit based on their
      values using these parameters. Note that specifying both is not
      permitted and will cause an error. If specified, both take an
      array of two numeric values.

      .. rubric:: ESTIMATES
         :name: estimates

      Initial estimates of fit parameters (peak intensity, peak x pixel
      coordinate, peak y pixel coordinate, major axis, minor axis,
      position angle) may be specified via an estimates text file. Each
      line of this file should contain a set of parameters for a single
      Gaussian. Optionally, some of these parameters can be fixed during
      the fit. The format of each line is

      peak intensity, peak x-pixel value, peak y-pixel value, major
      axis, minor axis, position angle, fixed

      | The fixed parameter is optional. The peak intensity is assumed
        to be in the same units as the image pixel values (eg Jy/beam).
        The peak coordinates are specified in pixel coordinates. The
        major and minor axes and the position angle are the convolved
        parameters if the image has been convolved with a clean beam and
        are specified as quantities. The fixed parameter is optional and
        is a string. It may contain any combination of the following
        characters 'f' (peak intensity), 'x' (peak x position), 'y'
        (peak y position), 'a' (major axis), 'b' (axial ratio, R =
        (major axis FWHM)/(minor axis FWHM)), 'p' (position angle).
        **NOTE: One cannot hold the minor axis fixed without holding the
        major axis fixed.** If the major axis is not fixed, specifying
        'b' in the fixed string will hold the axial ratio fixed during
        the fit.

      In addition, lines in the file starting with a # are considered
      comments.

      An example of such a file is:

      ::

         # peak intensity must be in map units
         120, 150, 110, 23.5arcsec, 18.9arcsec, 120deg
         90, 60, 200, 46arcsec, 23arcsec, 140deg, fxp

      This is a file which specifies that two Gaussians are to be
      simultaneously fit, and for the second Gaussian the specified peak
      intensity, x position, and position angle are to be held fixed
      during the fit.

      .. rubric:: ERROR ESTIMATES
         :name: error-estimates

       

      Error estimates are based on the work of  Condon (1997)  `[1]
      . <#cit1%20.>`__

       

        Key assumptions made are:

      -  The given model (elliptical Gaussian, or elliptical Gaussian
         plus constant offset) is an adequate representation of the data
      -  An accurate estimate of the pixel noise is provided or can be
         derived (see above). For the case of correlated noise (e.g., a
         CLEAN map), the fit region should contain many "beams" or an
         independent value of rms should be provided.
      -  The signal-to-noise ratio (SNR) of the Gaussian component is
         large. This is necessary because a Taylor series is used to
         linearize the problem. Condon (1997) states that the fractional
         bias in the fitted amplitude due to this assumption is of order
         1/S :sup:`2`, where S is the overall SNR of the Gaussian with
         respect to the given data set (defined more precisely below).
         For a 5 sigma "detection" of the Gaussian, this is a 4% effect.
      -  All (or practically all) of the flux in the component being fit
         falls within the selected region.

      If a constant offset term is simultaneously fit and not fixed, the
      region of interest should be even larger. The derivations of the
      expressions summarized in this note assume an effectively infinite
      region.

      Two sets of equations are used to calculate the parameter
      uncertainties, based on if the noise is correlated or
      uncorrelated. The rules governing which set of equations are used
      have been described above in the description of the *noisefwhm*
      parameter.

      In the case of uncorrelated noise, the equations used are

      .. math:: \begin{equation} \frac{\sigma(A)}{A} = \frac{\sigma(I)}{I} = \frac{\sigma(\theta_M)}{\theta_M} = \frac{\sigma(\theta_m)}{\theta_m} = \sqrt{8ln2} \frac{\sigma(x_0)}{\theta_M} = \sqrt{8ln2}\frac{\sigma(y_0)}{\theta_m} = \frac{\sigma(\phi)}{\sqrt{2}}(\frac{\theta_M^2-\theta_m^2}{\theta_M\theta_m}) = \frac{\sqrt{2}}{\rho}\end{equation}

      where :math:`\sigma(z)` is the uncertainty associated with
      parameter :math:`z`, :math:`A` is the peak intensity, :math:`I` is
      the flux density, :math:`\theta_M` and :math:`\theta_m` are the
      FWHM major and minor axes, :math:`\phi` is the position angle of
      the component, :math:`x_0` and :math:`y_0` are the direction
      uncertainties of the component measured along the major and minor
      axes; the resulting uncertainties measured along the principle
      axes of the image direction coordinate are calculated by
      propagation of errors using the 2D rotation matrix which enacts
      the rotation through the position angle plus 90 degrees.
      :math:`\rho` is the overall signal to noise ratio of the
      component, which, for the uncorrelated noise case, is given by

      .. math:: \begin{equation} \rho = \frac{A}{h\mu}\sqrt{\frac{\pi\theta_M\theta_m}{8ln2}} \end{equation}

      where :math:`h` is the pixel width of the direction coordinate and
      :math:`\mu` is the rms noise (see the discussion above for the
      rules governing how the value of :math:`\mu` is determined).

      For the correlated noise case, the same equations are used to
      determine the uncertainties as in the uncorrelated noise case,
      except for the uncertainty in :math:`I` (see below). However,
      :math:`\rho` is given by

      .. math:: \begin{equation} \rho = \frac{A}{\mu}\frac{\sqrt{\theta_M\theta_m}}{2\theta_N}\left(1 + \left(\frac{\theta_N}{\theta_M}\right)^2\right)^{\alpha_M/2}\left(1 + \left(\frac{\theta_N}{\theta_m}\right)^2\right)^{\alpha_m/2} \end{equation}

      where :math:`\theta_N` is the noise-correlation beam FWHM (see
      discussion of the *noisefwhm* parameter for rules governing how
      this value is determined). Variables :math:`\alpha_M` and
      :math:`\alpha_m` depend on which uncertainty is being calculated.
      For :math:`\sigma(A)`, :math:`\alpha_M` = :math:`\alpha_m` = 3/2.
      For :math:`\sigma_M` and :math:`x_0`, :math:`\alpha_M` = 5/2 and
      :math:`\alpha_m` = 1/2. For :math:`\theta_m`, :math:`y_0`, and
      :math:`\phi`, :math:`\alpha_M` = 1/2 and :math:`\alpha_m` = 5/2.
      :math:`\sigma(I)` is calculated in the correlated noise case
      according to

      .. math:: \begin{equation} \frac{\sigma(I)}{I} = \sqrt{ \left(\frac{\sigma(A)}{A}\right)^2 + \left(\frac{\theta_N^2}{\theta_M\theta_m}\right)\left[\left(\frac{\sigma(\theta_M)}{\theta_M}\right)^2 + \left(\frac{\sigma(\theta_m)}{\theta_m}\right)^2 \right] } \end{equation}

      Note well the following caveats:

      -  Fixing Gaussian component parameters will tend to cause the
         parameter uncertainties reported for free parameters to be
         overestimated.
      -  Fitting a zero level offset that is not fixed will tend to
         cause the reported parameter uncertainties to be slightly
         underestimated.
      -  The parameter uncertainties will be inaccurate at low SNR (a
         ~10% for SNR = 3).
      -  If the fitted region is not considerably larger than the
         largest component that is fit, parameter uncertainties may be
         mis-estimated.
      -  An accurate rms noise measurement, :math:`\mu`, for the region
         in question must be supplied. Alternatively, a sufficiently
         large signal-free region must be present in the selected region
         (at least about 25 noise beams in area) to auto-derive such an
         estimate.
      -  If the image noise is not statistically independent from pixel
         to pixel, a reasonably accurate noise correlation scale,
         :math:`\theta` :math:`_N`, must be provided. If the noise
         correlation function is not approximately Gaussian, the
         correlation length can be estimated using

      .. math:: \begin{equation} \theta_N = \sqrt{ \frac{2 \ln (2)}{\pi} } \, \frac{  \iint C(x,y) \mathrm{d}x \mathrm{d}y} { \sqrt{ \iint C(x,y)^2 \mathrm{d}x \mathrm{d}y}   } \end{equation}

      where C(x,y) is the associated noise-smoothing function.

      -  If fitted model components have significant spatial overlap,
         the parameter uncertainties are likely to be mis-estimated
         (i.e., correlations between the parameters of separate
         components are not accounted for).
      -  If the image being analyzed is an interferometric image with
         poor uv sampling, the parameter uncertainties may be
         significantly underestimated.

      The deconvolved size and position angle errors are computed by
      taking the maximum of the absolute values of the differences of
      the best fit deconvolved value of the given parameter and the
      deconvolved size of the eight possible combinations of (FWHM major
      axis +/- major axis error), (FWHM minor axis +/- minor axis
      error), and (position angle +/- position angle error). If the
      source cannot be deconvolved from the beam (if the best fit
      convolved source size cannot be deconvolved from the beam), upper
      limits on the deconvolved source size are reported, if possible.
      These limits simply come from the maximum major and minor axes of
      the deconvolved Gaussians taken from trying all eight of the
      aforementioned combinations. In the case none of these
      combinations produces a deconvolved size, no upper limit is
      reported.

       

      .. rubric:: Task-specific Parameter Descriptions
         :name: task-specific-parameter-descriptions

      .. rubric:: *includepix*
         :name: includepix

      Two element array giving the range of pixel values to include in
      the fit. Only one range of pixel values may be specified in
      includepix or excludepix.

      .. rubric:: *excludepix*
         :name: excludepix

      Two element array giving the range of pixel values to exclude in
      the fit. Only one range of pixel values may be specified in
      includepix or excludepix.

      .. rubric:: *residual*
         :name: residual

      Name of output residual image. Empty string indicates that the
      residual image should not be written.

      .. rubric:: *model*
         :name: model

      Name of output model image. Empty string indicates that the model
      image should not be written.

      .. rubric:: *estimates*
         :name: estimates-1

      Name of the text file that contains the initial parameter
      estimates. See the above description describing the format for
      such a file. An empty string indicates that the application should
      automatically determine initial parameter estimates. If it is
      desired that more than one Gaussian be fit simultaneously, an
      estimates file must be specified.

      .. rubric:: *logfile*
         :name: logfile

      Name of output file to which to write results. If set to the empty
      string, no logfile is written, although the results can still be
      obtained from the logger output.

      .. rubric:: *append*
         :name: append

      If True, append results to the specified logfile if it already
      exists. If False, overwrite an existing logfile if it already
      exists.

      .. rubric:: *newestimates*
         :name: newestimates

      Name of file to which to write the results of the fit in an
      estimates file format, so that the written file can be used as the
      estimates file on subsequent runs. The empty string means do not
      write such a file.

      .. rubric:: *complist*
         :name: complist

      Name of the component list table to which to write the fitted
      model. The empty string indicates that a component list table
      should not be written.

      .. rubric:: *overwrite*
         :name: overwrite

      Indicates if an existing component list table should be
      overwritten. If False and a component list table of the name
      specified by the complist parameter already exists, an exception
      will be thrown.

      .. rubric:: *dooff*
         :name: dooff

      Indicates if a constant zero-level offset should also be
      simultaneously fit.

      .. rubric:: *offset*
         :name: offset

      Initial estimate for the zero level offset, in the same units as
      the values in the image.

      .. rubric:: *fixoffset*
         :name: fixoffset

      Indicates if the specified zero-level offset should be held fixed
      during the fit.

      .. rubric:: *rms*
         :name: rms

      RMS to use in calculation of uncertainties. Numeric or valid
      quantity (record or string). If numeric, it is given units of the
      input image. If quantity, units must conform to image units. If
      not positive, the rms of the residual image, in the region of the
      fit, is used. See the above discussion for more details.

      .. rubric:: *noisefwhm*
         :name: noisefwhm

      Noise correlation beam FWHM. If numeric value, interpreted as
      pixel widths. If quantity (dictionary, string), it must have
      angular units. See the above discussion for more details.

      .. rubric:: *summary*
         :name: summary

      Name of file to which to write a plain text table summary of the
      fit parameters. The empty string indicates that such a file should
      not be written.


   Bibliography
         :sup:`1. Condon
         (1997) ` http://adsabs.harvard.edu/abs/1997PASP..109..166C `<#ref-cit1>`__

    """
    pass
