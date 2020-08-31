#
# stub function definition file for docstring parsing
#

def imstat(imagename, axes='-1', region='', box='', chans='', stokes='', listit=True, verbose=True, mask='', stretch=False, logfile='', append=True, algorithm='classic', fence=-1, center='mean', lside=True, zscore=-1, maxiter=-1, clmethod='auto', niter=3):
    r"""
Displays statistical information from an image or image region

Parameters
   - **imagename** (string) - Name of the input image
   - **axes** (variant) - List of axes to evaluate statistics over. Default is all axes.
   - **region** (string) - Region selection. Default is to use the full image.
   - **box** (string) - Rectangular region(s) to select in direction plane. Default is to use the entire direction plane.
   - **chans** (string) - Channels to use. Default is to use all channels.
   - **stokes** (string) - Stokes planes to use. Default is to use all Stokes planes.
   - **listit** (bool) - Print stats and bounding box to logger?
   - **verbose** (bool) - Print additional messages to logger?
   - **mask** (string) - Mask to use. Default is none.
   - **logfile** (string) - Name of file to write fit results.
   - **algorithm** (string) - Algorithm to use. Supported values are "biweight", "chauvenet", "classic", "fit-half", and "hinges-fences". Minimum match is supported.

Subparameters
   .. raw:: html

      <details><summary><i> mask != '' </i></summary>

   - **stretch** (bool=False) - Stretch the mask if necessary and possible? 

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> logfile != '' </i></summary>

   - **append** (bool=True) - If logfile exists, append to it if True or overwrite it if False

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> algorithm = classic </i></summary>

   - **clmethod** (string=auto) - Method to use for calculating classical statistics. Supported methods are "auto", "tiled", and "framework". Ignored if algorithm is not "classic".

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> algorithm = hinges-fences </i></summary>

   - **fence** (double=-1) - Fence value for hinges-fences. A negative value means use the entire data set (ie default to the "classic" algorithm). Ignored if algorithm is not "hinges-fences".

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> algorithm = fit-half </i></summary>

   - **center** (string=mean) - Center to use for fit-half. Valid choices are "mean", "median", and "zero". Ignored if algorithm is not "fit-half".
   - **lside** (bool=True) - For fit-half, use values <= center for real data if True? If False, use values >= center as real data. Ignored if algorithm is not "fit-half".

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> algorithm = chauvenet </i></summary>

   - **zscore** (double=-1) - For chauvenet, this is the target maximum number of standard deviations data may have to be included. If negative, use Chauvenet"s criterion. Ignored if algorithm is not "chauvenet".
   - **maxiter** (int=-1) - For chauvenet, this is the maximum number of iterations to attempt. Iterating will stop when either this limit is reached, or the zscore criterion is met. If negative, iterate until the zscore criterion is met. Ignored if algorithm is not "chauvenet".

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> algorithm = biweight </i></summary>

   - **niter** (int=3) - For biweight, this is the maximum number of iterations to attempt. Iterating will stop when either this limit is reached, or the zscore criterion is met. If negative, do a fast, simple computation (see description). Ignored if the algorithm is not "biweight".

   .. raw:: html

      </details>


Description
      Many parameters are determined from the specified region of an
      image. The region can be specified by a set of `rectangular pixel
      coordinates, the channel ranges and the
      Stokes <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/image-selection-parameters>`__ or
      a `region
      file <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/region-files>`__.

      .. note:: **Alert:** When both the *region* parameter and any of
         *box*/*chans*/*stokes* are specified simultaneously, the task
         may perform unwanted selections, so this should be avoided. See
         this chapter on `region
         files <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/region-files>`__
         for more information.

      For directed output, run as:

      .. note:: myoutput=imstat()

      General procedure:

      .. note:: | #Specify inputs, then
         | myoutput=imstat()
         | #or specify inputs directly in calling sequence to task
         | myoutput=imstat(imagename='image.im', etc)
         | myoutput['KEYS'] #will contain the result associated with any
           of the keys given below

      +-----------------------------------+-----------------------------------+
      | KEYS                              | DESCRIPTION                       |
      +-----------------------------------+-----------------------------------+
      | blc                               | absolute PIXEL coordinate of the  |
      |                                   | bottom left corner of the         |
      |                                   | bounding box surrounding the      |
      |                                   | selected region                   |
      +-----------------------------------+-----------------------------------+
      | blcf                              | Same as blc, but uses WORLD       |
      |                                   | coordinates instead of pixels     |
      +-----------------------------------+-----------------------------------+
      | trc                               | the absolute PIXEL coordinate of  |
      |                                   | the top right corner of the       |
      |                                   | bounding box surrounding the      |
      |                                   | selected region                   |
      +-----------------------------------+-----------------------------------+
      | trcf                              | Same as trc, but uses WORLD       |
      |                                   | coordinates instead of pixels     |
      +-----------------------------------+-----------------------------------+
      | flux                              | the flux or flux density. See     |
      |                                   | below for details.                |
      +-----------------------------------+-----------------------------------+
      | npts                              | the number of unmasked points     |
      |                                   | used                              |
      +-----------------------------------+-----------------------------------+
      | max                               | the maximum pixel value           |
      +-----------------------------------+-----------------------------------+
      | min                               | minimum pixel value               |
      +-----------------------------------+-----------------------------------+
      | maxpos                            | absolute PIXEL coordinate of      |
      |                                   | maximum pixel value               |
      +-----------------------------------+-----------------------------------+
      | maxposf                           | Same as maxpos, but uses WORLD    |
      |                                   | coordinates instead of pixels     |
      +-----------------------------------+-----------------------------------+
      | minpos                            | absolute pixel coordinate of      |
      |                                   | minimum pixel value               |
      +-----------------------------------+-----------------------------------+
      | minposf                           | Same as minpos, but uses WORLD    |
      |                                   | coordinates instead of pixels     |
      +-----------------------------------+-----------------------------------+
      | sum                               | the sum of the pixel              |
      |                                   | values: :math:`\sum I_i`         |
      +-----------------------------------+-----------------------------------+
      | sumsq                             | the sum of the squares of the     |
      |                                   | pixel values: :math:`\sum I_i^2` |
      +-----------------------------------+-----------------------------------+
      | mean                              | the mean of pixel                 |
      |                                   | values                            |
      |                                   | : :math:`\bar{I} = \sum I_i / n` |
      +-----------------------------------+-----------------------------------+
      | sigma                             | the standard deviation about the  |
      |                                   | mean: :math:`\sigma^2            |
      |                                   | = (\sum I_i - \bar{I})^2 / (n-1)` |
      +-----------------------------------+-----------------------------------+
      | rms                               | the root mean                     |
      |                                   | square                            |
      |                                   | : :math:`\sqrt {\sum I_i^2 / n}` |
      +-----------------------------------+-----------------------------------+
      | median                            | the median pixel value            |
      +-----------------------------------+-----------------------------------+
      | medabsdevmed                      | the median of the absolute        |
      |                                   | deviations from the median        |
      +-----------------------------------+-----------------------------------+
      | quartile                          | the inner-quartile range. Find    |
      |                                   | the points which are 25% largest  |
      |                                   | and 75% largest (the median is    |
      |                                   | 50% largest).                     |
      +-----------------------------------+-----------------------------------+
      | q1                                | the first quartile                |
      +-----------------------------------+-----------------------------------+
      | q3                                | the third quartile                |
      +-----------------------------------+-----------------------------------+

       

      .. rubric:: CURSOR AXES
         :name: cursor-axes

      | The *axes* parameter allows one to set the cursor axes over
        which statistics are computed. For example, consider a
        3-dimensional image for which *axes=[0,2]*. The statistics would
        be computed for each XZ (axes 0 and 2) plane in the image. One
        could then examine those statistics as a function of the Y (axis
        1) axis.
      | Each statistic is stored in an array in its own field in the
        returned dictionary. The dimensionality of these arrays is equal
        to the number of axes over which the statistics were not
        evaluated (called the display axes). For example, if the input
        image has four axes, and *axes=[0]*, the output statistic arrays
        will have three dimensions. If *axes=[0, 1]*, the output
        statistic arrays will have two dimensions.
      | The shape of the output arrays when axes has a positive number
        of elements is based on the region selection. If there is no
        region selection, the shape of the statistic arrays is just the
        shape of the image along the display (non-cursor) axes. For
        example, if the input image has dimensions of 300x400x4x80 (RA x
        Dec x Stokes x Freq) and *axes=[0, 1]*, in the absence of a
        region selection, the shape of the output statistic arrays will
        be 4x80. If there is a region selection, the shape of the output
        statistic arrays will be determined by the number of planes
        along the display axes chosen in the region selection. For
        example, continuing with our example, if *axes=[0,1]*,
        *chans="5~15;30~70"*, and *stokes="IV"*, the output statistic
        arrays will have shapes of 2x52. Only the selected planes will
        be displayed in the logger output if *verbose=True*.
      | In the case where the image has a pixel mask, and/or the *mask*
        parameter is specified, and because of this specification a
        plane is entirely masked, this element is included in the
        statistic arrays (usually with a value of 0). It is not included
        in the logger output if *verbose=True*. One can exclude such
        elements from computations on the output arrays by using the
        numpy.extract() method. For example, to compute the minimum rms
        value, not including any fully masked planes, one could use

      .. note:: | stats = imstat(...)
         | rmsmin = numpy.min(numpy.extract(stats['npts']>0,
           stats['rms']))

      Thus in the computation of rmsmin, only the rms elements are
      considered which have associated values of 'npts' that are greater
      than zero.

       

      .. rubric:: ALGORITHMS
         :name: algorithms

      Several types of statistical algorithms are supported:

      .. rubric:: CLASSIC
         :name: classic

      This is the familiar algorithm, in which all unmasked pixels are
      used. One may choose one of two methods, which vary only by
      performance, for computing classic statistics via the *clmethod*
      parameter. The "tiled" method is the old method and is fastest in
      cases where there are a large number of individual sets of
      statistics to be computed and a small number of data points per
      set. This can occur when one sets the *axes* parameter, which
      causes several individual sets of statistics to be computed. The
      "framework" method uses the new statistics framework to compute
      statistics. This method is fastest in the regime where one has a
      small number of individual sets of statistics to calculate, and
      each set has a large number of points. For example, this method is
      fastest when computing statistics over an entire image in one go
      (no *axes* specified). A third option, "auto", chooses which
      method to use by predicting which be faster based on the number of
      pixels in the image and the choice of the *axes* parameter.

      .. rubric:: FIT-HALF
         :name: fit-half

      This algorithm calculates statistics on a dataset created from
      real and virtual pixel values. The real values are determined by
      the input parameters *center* and *lside*. The parameter *center*
      tells the algorithm where the center value of the combined
      real+virtual dataset should be. Options are the mean or the median
      of the input image's pixel values, or at zero. The *lside*
      parameter tells the algorithm on which side of center the real
      pixel values are located. True indicates that the real pixel
      values to be used are ≤ center. False indicates the real pixel
      values to be used are ≥ center. The virtual part of the dataset is
      then created by reflecting all the real values through the center
      value, to create a perfectly symmetric dataset composed of a real
      and a virtual component. Statistics are then calculated on this
      resultant dataset. These two parameters are ignored if algorithm
      is not "FIT-HALF". Because the maximum value is virtual if *lside*
      is True and the minimum value is virtual if *lside* is False, the
      value of the maximum position (if *lside=True*) or minimum
      position (if *lside=False*) is not reported in the returned
      record.

      .. rubric:: HINGES-FENCES
         :name: hinges-fences

      This algorithm calculates statistics by including data in a range
      between :math:`Q1 - f*D` and :math:`Q3 + f*D`, inclusive, where Q1
      is the first quartile of the distribution of unmasked data,
      subject to any specified pixel ranges, Q3 is the third quartile,
      :math:`D = Q3 - Q1` (the inner quartile range), and f is the
      user-specified fence factor. Negative values of f indicate that
      the full distribution is to be used (i.e., the classic algorithm
      is used). Sufficiently large values of f will also be equivalent
      to using the "CLASSIC" algorithm. For f = 0, only data in the
      inner quartile range is used for computing statistics. The value
      of fence is silently ignored if algorithm is not "HINGES-FENCES".

      .. rubric:: CHAUVENET
         :name: chauvenet

      The idea behind this algorithm is to eliminate outliers based on a
      maximum *z-score* parameter value. A *z-score* is the number of
      standard deviations a point is from the mean of a distribution.
      This method thus is meant to be used for (nearly) normal
      distributions. In general, this is an iterative process, with
      successive iterations discarding additional outliers as the
      remaining points become closer to forming a normal distribution.
      Iterating stops when no additional points lie beyond the specified
      *z-score* value, or, if *z-score* is negative, when Chauvenet's
      criterion is met (see below). The parameter *maxiter* can be set
      to a non-negative value to prematurely abort this iterative
      process. When *verbose=T*, the "N-iter" column in the table that
      is logged represents the number of iterations that were executed.

      Chauvenet's criterion allows the target *z-score* to decrease as
      the number of points in the distribution decreases on subsequent
      iterations. Essentially, the criterion is that the probability of
      having one point in a normal distribution at a maximum *z-score*
      of z :sub:`max` must be at least 0.5. z :sub:`max` is therefore
      a function of (only) the number of points in the distribution and
      is given by

      npts = 0.5/erfc(z :sub:`max`/:math:`\sqrt{2}`)

      where erfc() is the complementary error function. As iterating
      proceeds, the number of remaining points decreases as outliers are
      discarded, and so z :sub:`max` likewise decreases. Convergence
      occurs when all remaining points fall within a *z-score* of
      z :sub:`max`. Below is an illustrative table of z :sub:`max`
      values and their corresponding npts values. For example, it is
      likely that there will be a 5-sigma "noise bump" in a perfectly
      noisy image with one million independent elements.

      ====== ===============
      z max **npts**
      1.0    1
      1.5    3
      2.0    10
      2.5    40
      3.0    185
      3.5    1,074
      4.0    7,893
      4.5    73,579
      5.0    872,138
      5.5    13,165,126
      6.0    253,398,672
      6.5    6,225,098,696
      7.0    195,341,107,722
      ====== ===============

      .. rubric:: BIWEIGHT
         :name: biweight

      The biweight is a robust method to determine the center and width
      of a distribution. It uses the median and median absolute
      deviation to effectively downweight points in the distribution
      that are more than 4 standard deviations from the center of the
      distribution and then computes center (i.e., "location") and the
      width (i.e., "scale") of the distribution. These quantities are
      analogous to the mean and the standard deviation for a standard
      normal distribution. Our implementation is based on the equations
      in Beers 1990  `[1] <#cit1>`__ and Iglewicz 1983 `[2] <#cit2>`__ .

      The data weights in this algorithm are

      .. math:: w_i = (1 - u_i^2)

      | where :math:`u_i` is defined as
      | 

        .. math:: u_i = \frac{ x_i - c_{bi} } { c s_{bi} }  

           

      | The variable :math:`x_i` is the data values, :math:`c_{bi}` is
        the biweight location, :math:`s_{bi}` is the biweight scale, and
        :math:`c` is a constant. We adopt a value for :math:`c` of 6,
        which gives zero weight to observations more than 4 standard
        deviations from the median. For the initial computation of the
        :math:`u_i` values, :math:`c_{bi}` is set equal to the median of
        the distribution and :math:`s_{bi}` is set equal to the
        normalized MAD (median of the absolute deviation about the
        median), assuming a Gaussian distribution. This value is the MAD
        multiplied by 1.4826, i.e., the value of the probit function at
        0.75.
      |      
      | The location, :math:`c_{bi}`, is then computed from

      .. math:: c_{bi} = \frac{ \sum_{w_i > 0} x_i  w_i^2 } { \sum_{w_i > 0} w_i^2  }   

      where only values of :math:`u_i` which satisfy :math:`|u_i| < 1`
      (:math:`w_i >0`) are included in the sums. Note that the weights
      are zero, not undefined, for points beyond 4 sigma.

      The scale value is computed using

      .. math:: s_{bi}^2 = \frac{ n \sum_{w_i > 0} (x_i - c_{bi})^2 w_i^4} {p \max(1,p-1)}

      where

      .. math:: p = | \sum_{w_i > 0} w_i (5w_i - 4) | 

      Again, the above sum includes only data for which
      :math:` | u_i |  < 1` (:math:`w_i >0`). The variable n is the
      number of points for the entire distribution, since points beyond
      4 standard deviations are downweights, not removed.

      | The algorithm proceeds as follows.
      |     1. Compute initial :math:`u_i` values (and hence :math:`w_i`
        values) from the above equation, setting :math:`c_{bi}` equal to
        the median of the distribution and :math:`s_{bi}` equal to the
        normalized MAD.
      |     2. Compute the initial value of the scale using the
        :math:`w_i` values computed in step 1 using the equation for
        :math:`s_{bi}`.
      |     3. Recompute :math:`u_i` and :math:`w_i` values using the
        most recent previous scale and location values.
      |     4. Compute the location using the :math:`u_i` and
        :math:`w_i` values from step 3 and the equation for
        :math:`c_{bi}`.
      |     5. Recompute :math:`u_i` and :math:`w_i` values using the
        most recent previous scale and location values.
      |     6. Compute the new scale value using the the :math:`u_i` and
        :math:`w_i` values computed in step 5 and the value of the
        location computed in step 4.
      |     7. Steps 3 - 6 are repeated until convergence occurs or the
        maximum number of iterations (specified in the *niter*
        parameter) is reached. The convergence criterion is given by

              

      .. math:: | (s_{bi} - s_{bi,prev})/s_{bi,prev} | < 0.03  \sqrt{ \frac{0.5}{n - 1}}

             where :math:`s_{bi,prev}` is the value of the scale
      computed in the previous iteration.

      In the special case where *niter* is specified to be negative, the
      scale and location will be computed directly with no iteration.

      |     1. Compute :math:`u_i` and :math:`w_i` values using the
        median for the location and the normalized MAD as the scale.
      |     2. Compute the location and scale (which can be carried out
        simultaneously) using the :math:`u_i` and :math:`w_i` values
        computed in step 1. The value of the location used in the scale
        computation is just the median.

      The only keys present in the returned dictionary are 'mean'
      (location), 'sigma' (scale), 'npts', 'min', and 'max' to maximize
      speed. The last three represent the values using the entire
      distribution. Note that the biweight algorithm does not support
      computation of quantile-like values (median, medabsdevmed, q1, q3,
      and iqr), so setting *robust=True* will cause a warning message to
      be logged regarding that, and the computation will proceed. If you
      want to compute these quantities in addition those values
      calculated here, re-run **imstat** with selecting another
      algorithm.

       

      .. rubric:: NOTES ON FLUX DENSITIES AND FLUXES
         :name: notes-on-flux-densities-and-fluxes

      .. note:: | Explanation of terminology:
         | The terms "intensity" or "brightness" refer to quantities
           with a unit such as Jy/beam or Kelvin (K).
         | The term "flux density" refers to quantities with a unit such
           as Janskys (Jy). This is dimensionally equivalent to
           W/m**2/Hz.
         | The term "flux" refers to a flux density integrated over the
           spectral or velocity axis, such as Jy*km/s or Jy*Hz. These
           are dimensionally equivalent to W/m**2.

      Fluxes and flux densities are not computed if any of the following
      conditions is met:

      #. The image does not have a direction coordinate
      #. The image does not have a intensity-like brightness unit.
         Examples of such units are Jy/beam (in which case the image
         must also have a beam) and Kelvin (K)
      #. There are no direction axes in the cursor axes that are used
      #. If the (specified region of the) image has a non-degenerate
         spectral axis, and the image has a tabular spectral axis (axis
         with varying increments) `[a] <#fna>`__
      #. Any axis that is not a direction nor a spectral axis that is
         included in the cursor axes is not degenerate within in
         specified region

      In cases where none of the above conditions is met, the flux
      density(ies) (intensities integrated over direction planes) will
      be computed if any of the following conditions is met:

      #. The image has no spectral coordinate
      #. The cursor axes do not include the spectral axis
      #. The spectral axis in the chosen region is degenerate

      In the case where there is a non-degenerate spectral axis that is
      included in the cursor axes, the flux (flux density integrated
      over spectral planes) will be computed. In this case, the spectral
      portion of the flux unit will be the velocity unit of the spectral
      coordinate if it has one (e.g., if the brightness unit is Jy/beam
      and the velocity unit is km/s, the flux will have units of Jy
      km/s). If not, the spectral portion of the flux unit will be the
      frequency unit of the spectral axis (e.g., if the brightness unit
      is K and the frequency unit is Hz, the resulting flux unit will be
      K arcsec :sup:`2` Hz).

      In both cases of flux density or flux being computed, the
      resulting numerical value is assigned to the "flux" key in the
      output dictionary.

      If the image has units of Jy/beam, the flux density is just the
      mean intensity multiplied by the number of beam areas included in
      the region. The beam area is defined as the volume of the
      elliptical Gaussian defined by the synthesized beam, divided by
      the maximum of that function, which is equivalent to

      :math:`\frac {π}{4 ln(2)} * FWHM_{major} * FWHM_{minor}`

      where ln() is the natural logarithm and :math:`FWHM_{major}` and
      :math:`FWHM_{minor}` are the major and minor full width at half
      maximum (FWHM) axes of the beam, respectively.

       

      .. rubric:: Task-specific Parameters Summary
         :name: task-specific-parameters-summary

      .. rubric:: *axes*
         :name: axes

      Cursor axes over which to evaluate statistics.

      .. rubric:: *listit*
         :name: listit

      Print stats and bounding box to logger?

      .. rubric:: *verbose*
         :name: verbose

      Print additional, possibly useful, messages to logger?

      .. rubric:: *logfile*
         :name: logfile

      Name of file to write fit results.

      .. rubric:: *append*
         :name: append

      If logfile exists, append to it if True or overwrite it if False.

      .. rubric:: *algorithm*
         :name: algorithm

      Algorithm to use. Supported values are "biweight", "chauvenet",
      "classic", "fit-half", and "hinges-fences". Minimum match is
      supported.

      .. rubric:: *fence*
         :name: fence

      Fence value for hinges-fences. A negative value means use the
      entire data set (ie default to the "classic" algorithm). Ignored
      if algorithm is not "hinges-fences".

      .. rubric:: *center*
         :name: center

      Center to use for fit-half. Valid choices are "mean", "median",
      and "zero". Ignored if algorithm is not "fit-half".

      .. rubric:: *lside*
         :name: lside

      For fit-half, use values <= center for real data if True? If
      False, use values >= center as real data. Ignored if algorithm is
      not "fit-half".

      .. rubric:: *zscore*
         :name: zscore

      For chauvenet, this is the target maximum number of standard
      deviations data may have to be included. If negative, use 
      Chauvenet's criterion. Ignored if algorithm is not "chauvenet".

      .. rubric:: *maxiter*
         :name: maxiter

      For chauvenet, this is the maximum number of iterations to
      attempt. Iterating will stop when either this limit is reached, or
      the zscore criterion is met. If negative, iterate until the zscore
      criterion is met. Ignored if algorithm is not "chauvenet".

      .. rubric:: *clmethod*
         :name: clmethod

      Method to use for calculating classical statistics. Supported
      methods are "auto", "tiled", and "framework". Ignored if algorithm
      is not "classic".

      .. rubric:: *niter*
         :name: niter

      For biweight, this is the maximum number of iterations to attempt.
      Iterating will stop when either this limit is reached, or the
      convergence criterion is met. If negative, do a fast, simple
      computation (see description). Ignored if the algorithm is not
      "biweight".



      =============== =============================
      Footnote Number a
      Footnote Text   May be removed in the future.
      =============== =============================


   Bibliography
         :sup:`1. Beers, T., Flynn, K., and Gebhardt, K. 1990. AJ, 100,
         1, 32.` `<#ref-cit1>`__

         :sup:`2. Iglewicz, Boris. 1983. “Robust Scale Estimators and
         Confidence Intervals for Location” in Understanding Robust and
         Exploratory Data Analysis, eds. Hoaglin, David; Mosteller,
         Frederick; and Tukey, John W., John Wiley and Sons,
         Inc.` `<#ref-cit2>`__


         Footnote(s)

         :sup:`a. May be removed in the future.` `<#refa>`__

    """
    pass
