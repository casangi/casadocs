#
# stub function definition file for docstring parsing
#

def spxfit(imagename='', box='', region='', chans='', stokes='', axis=-1, mask='', minpts=1, multifit=False, spxtype='plp', spxest=[''], spxfix=[''], div='0', spxsol='', spxerr='', model='', residual='', wantreturn=True, stretch=False, logresults=True, logfile='', append=True, sigma='', outsigma=''):
    r"""
Fit a 1-dimensional model(s) to an image(s) or region for determination of spectral index.

Parameters
   - imagename_ (variant='') - Name of the input image(s)
   - box_ (string='') - Rectangular region to select in direction plane. Default is to use the entire direction plane.
   - region_ (string='') - Region selection. Default is to use the full image.
   - chans_ (string='') - Channels to use. Default is to use all channels.
   - stokes_ (string='') - Stokes planes to use. Default is to use all Stokes planes.
   - axis_ (int=-1) - The profile axis. Default: use the spectral axis if one exists, axis 0 otherwise (<0).
   - mask_ (string='') - Mask to use. Default is none.

      .. raw:: html

         <details><summary><i> mask != '' </i></summary>

      - stretch_ (bool=False) - Stretch the mask if necessary and possible? 

      .. raw:: html

         </details>
   - minpts_ (int=1) - Minimum number of unmasked points necessary to attempt fit.
   - multifit_ (bool=False) - If true, fit a profile along the desired axis at each pixel in the specified region. If false, average the non-fit axis pixels and do a single fit to that average profile. Default False.

      .. raw:: html

         <details><summary><i> multifit = True </i></summary>

      - spxsol_ (string='') - Name of the spectral index function coefficient solution image to write.
      - spxerr_ (string='') - Name of the spectral index function coefficient error image to write.
      - model_ (string='') - Name of model image. Default: do not write the model image ("").
      - residual_ (string='') - Name of residual image. Default: do not write the residual image ("").

      .. raw:: html

         </details>
   - spxtype_ (string='plp') - Type of function to fit. "plp" = power logarithmic polynomial, "ltp" = logarithmic transformed polynomial.
   - spxest_ (doubleArray=['']) - REQUIRED. Initial estimates as array of numerical values for the spectral index function coefficients. eg [1.5, -0.8] if fitting a plp function thought to be close to 1.5*(x/div)**(-0.8) or [0.4055, -0.8] if fitting an lpt function thought to be close to ln(1.5) - 0.8*ln(x/div).
   - spxfix_ (boolArray=['']) - Fix the corresponding spectral index function coefficients during the fit. True means hold fixed.
   - div_ (variant='0') - Divisor (numerical value or quantity) to use in the logarithmic terms of the plp or ltp function. 0 means calculate a useful value on the fly.
   - wantreturn_ (bool=True) - Should a record summarizing the results be returned?
   - logresults_ (bool=True) - Output results to logger?
   - logfile_ (string='') - File in which to log results. Default is not to write a logfile.

      .. raw:: html

         <details><summary><i> logfile != '' </i></summary>

      - append_ (bool=True) - Append results to logfile? Logfile must be specified. Default is to append. False means overwrite existing file if it exists.

      .. raw:: html

         </details>
   - sigma_ ({string, stringArray, doubleArray, intArray}='') - Standard deviation array or image name(s).

      .. raw:: html

         <details><summary><i> sigma != '' </i></summary>

      - outsigma_ (string='') - Name of output image used for standard deviation. Ignored if sigma is empty.

      .. raw:: html

         </details>


Description
   This task fits a power logarithmic polynomial or a logarithmic
   tranformed polynomial to one-dimensional profiles for
   determination of spectral indices.

   This application performs a non-linear, least squares fits using
   the Levenberg-Marquardt algorithm of either a power logarithmic
   polynomial or a logarithmic tranformed polynomial to pixel values
   along a specified axis of an image or images. A description of the
   fitting algorithm may be found in AIPS++ Note 224 `[1] <#cit1>`__
   and in Numerical Recipes `[2] <#cit2>`__. These functions are most
   often used for fitting the spectral index and higher order terms
   of a spectrum. A power logarithmic polynomial (plp) has the form

   y = c :sub:`0` \*(x/div) :sup:`[c 1 + c 2 \*ln(x/div) +
   c 3 \*ln(x/div)` :math:`^2` + ... +
   c :sub:`n` \*ln(x/div) :math:`^{(n-1)}`]

   In the case of fitting a spectral index, which is traditionally
   represented as :math:`\alpha`, the :math:`\alpha` is equal to
   c :sub:`1`.

   A logarithmic transformed polynomial (ltp) is simply the result of
   this equation after taking the natural log of both sides so that
   it has the form

   ln(y) = c :sub:`0` + c :sub:`1` \*ln(x/div) +
   c :sub:`2` \*ln(x/div) :sup:`2` + ... +
   c :sub:`n` \*ln(x/div) :sup:`n`

   Because the logarithm of the ordinate values must be taken before
   fitting a logarithmic transformed polynomial, all non-positive
   pixel values are effectively masked for the purposes of fitting.

   The coefficients of the two forms are equal to each other except
   that c :sub:`0` in the second equation is equal to
   ln(c :sub:`0`) of the first.

   In both cases, div is a numerical value used to scale abscissa
   values so they are closer to unity when they are sent to the
   fitter. This generally improves the probability that the fit will
   converge. This parameter may be specified via the *div* parameter.
   A value of 0 (the default) indicates that the application should
   determine a reasonable value for div, which is determined via

   div = 10 :math:`int[log_{10}\sqrt{min(x)*max(x)}]`

   where min(x) and max(x) are the minimum and maximum abscissa
   values, respectively.

   The number of values specified in the *spxest* array indicate the
   number of coefficients for which to solve. If *multifit=True*, the
   values provided in the *spxest* array are used as initial
   estimates at every pixel. So, for example, if S(:math:`\nu`) is
   proportional to :math:`\nu^{\alpha}` and you expect alpha to be
   near -0.8 and the value of S(:math:`\nu`) is 1.5 at 10 :math:`^9`
   Hz and your image(s) have spectral units of Hz, you would specify
   *spxest=[1.5, -0.8]* and *div=1e9* when fitting a plp function, or
   *spxest=[0.405, -0.8]* and *div=1e9* if fitting an ltp function
   close to ln(1.5) - 0.8*ln(x/div).

   .. rubric:: 
      A CAUTIONARY NOTE
      

   Note that the likelihood of getting a reliable solution increases
   with the number of good data points as well as the goodness of the
   initial estimate. It is possible that the first solution found
   might not be the best one, and so, if a solution is found, it is
   recommended that the fit be repeated using the solution of the
   previous fit as the initial estimate for the new fit. This process
   should be repeated until the solutions from one fit to the next
   differ only insignificantly. The convergent solution is very
   likely the best solution.

   .. rubric:: AXIS
      

   The *axis* parameter indicates on which axis profiles should be
   fit; a negative value indicates the spectral axis should be used,
   or if one does not exist, that the zeroth axis should be used.

   .. rubric:: MINIMUM NUMBER OF PIXELS
      

   The *minpts* parameter indicates the minimum number of unmasked
   pixels that must be present in order for a fit to be attempted.
   When *multifit=True*, positions with too few good points will be
   masked in any output images.

   .. rubric:: ONE FIT OF REGION AVERAGE OR PIXEL BY PIXEL FIT
      

   The *multifit* parameter indicates if profiles should be fit at
   each pixel in the selected region (true), or if the profiles in
   that region should be averaged and the fit done to that average
   profile (false).

   .. rubric:: FUNCTION TYPE
      

   Which function to fit is specified in the *spxtype* parameter.
   Only two values (case insensitive) are supported. A value of "plp"
   indicates that a power logarithmic polynomial should be fit. A
   value of "ltp" indicates a logarithmic transformed polynomial
   should be fit.

   .. rubric:: INCLUDING STANDARD DEVIATIONS OF PIXEL VALUES
      

   If the standard deviations of the pixel values in the input image
   are known and they vary in the image (e.g. they are higher for
   pixels near the edge of the band), they can be included in the
   *sigma* parameter. This parameter takes either an array or an
   image name. The array or image must have one of three shapes:

   #. the shape of the input image,
   #. the same dimensions as the input image with the lengths of all
      axes being one except for the fit axis which must have length
      corresponding to its length in the input image, or
   #. be one dimensional with lenght equal the the length of the fit
      axis in the input image.

   In cases 2 and 3, the array or pixels in sigma will be replicated
   such that the image that is ultimately used is the same shape as
   the input image. The values of sigma must be non-negative. It is
   only the relative values that are important. A value of 0 means
   that pixel should not be used in the fit. Other than that, if
   pixel A has a higher standard deviation than pixel B, then pixel A
   is noisier than pixel B and will receive a lower weight when the
   fit is done. The weight of a pixel is the usual

   weight = :math:`\frac{1}{\sigma^2}`

   In the case of *multifit=F*, the sigma values at each pixel along
   the fit axis in the hyperplane perpendicular to the fit axis which
   includes that pixel are averaged and the resultant averaged
   standard deviation spectrum is the one used in the fit.
   Internally, sigma values are normalized such that the maximum
   value is 1. This mitigates a known overflow issue.

   One can write the normalized standard deviation image used in the
   fit by specifying its name in *outsigma*. This image can then be
   used as sigma for subsequent runs.

   .. rubric:: RETURNED DICTIONARY STRUCTURE
      

   The returned dictionary has a (necessarily) complex structure.
   First, there are keys "xUnit" and "yUnit" whose values are the
   abscissa unit and the ordinate unit described by simple strings.
   Next there are arrays giving a broad overview of the fit quality.
   These arrays have the shape of the specified region collapsed
   along the fit axis with the axis corresponding to the fit axis
   having length of 1:

   | ATTEMPTED: a boolean array indicating which fits were attempted
     (e.g. if too few unmasked points, a fit will not be attempted).
   | CONVERGED: a boolean array indicating which fits converged.
     False if the fit was not attempted.
   | VALID: a boolean array indicating which solutions fall within
     the specified valid ranges of parameter space (any solution for
     which a value or error is NaN is automatically marked as
     invalid)
   | NITER: an int array indicating the number of iterations for each
     profile, <0 if the fit did not converge
   | DIRECTION: a string array containing the world direction
     coordinate for each profile

   There is a "type" array having number of dimensions equal to the
   number of dimensions in the above arrays plus one. The shape of
   the first n-1 dimensions is the same as the shape of the above
   arrays. The length of the last dimension is equal to the number of
   components fit. The values of this array are all "POWER
   LOGARITHMIC POLYNOMIAL" or "LOGARITHMIC TRANSFORMED POLYNOMIAL",
   depending on which type function was fit.

   There will be a subdictionary accessible via the "plp" or "ltp"
   key (depending on which type of function was fit) which will have
   subkeys "solution" and "error" which will each have an array of
   values. Each of these arrays will have one more dimension than the
   overview arrays described above. The shape of the first n-1
   dimensions will be the same as the shape of the overview arrays
   described above, while the final dimension will have length equal
   to the number of parameters that were fit. Along this axis will be
   the corresponding fit result or associated error (depending on the
   array's associated key) of the fit. In cases where the fit was not
   attempted or did not converge, a value of NAN will be present.

   .. rubric:: OUTPUT IMAGES
      

   In addition to the returned dictionary, optionally one or more of
   any combination of output images can be written. The model and
   residual parameters indicate the names of the model and residual
   images to be written; empty values indicate that these images
   should not be written.

   The parameters *spxsol* and *spxerr* are the names of the solution
   and error images to write, respectively. In cases where more than
   one coefficient are fit, the image names will be appended with an
   underscore followed by the relevant coefficient number ("_0",
   "_1", etc). These images contain the arrays for the associated
   parameter solutions or errors described in previous sections.
   Pixels for which fits were not attempted, did not converge, or
   converged but have values of NaN (not a number) or INF (infinity)
   will be masked as bad.

   .. rubric:: LPT vs PLP
      

   Ultimately, the choice of which functional form to use in
   determining the spectral index is up to the user and should be
   based on the scientific goals. However, below is a summary of one
   user's experience and preferences as an example:

   If the weights are known or can be determined from the images
   (e.g. the source-free image rms and a fractional calibration
   error) then a weighted fit using the non-linear (power-law) model
   is preferred. An unweighted fit using the non-linear model will,
   in general, give far too much leverage to large flux values.

   If the weights are unknown or will not be considered by the
   fitting algorithm, then the log-transformed polynomial model is
   preferred. However, this does not work well in low signal-to-noise
   regions. A conservative mask could be created such that only high
   S/N areas are fit, but this could hinder many science objectives.



   

   .. rubric:: Task specific parameters summary
      

   .. rubric:: *axis*
      

   The profile axis. Default (<0): use the spectral axis if one
   exists, axis 0 otherwise.

   .. rubric:: *minpts*
      

   Minimum number of unmasked points necessary to attempt fit.

   .. rubric:: *multifit*
      

   If true, fit a profile along the desired axis at each pixel in the
   specified region. If false, average the non-fit axis pixels and do
   a single fit to that average profile. Default False.

   .. rubric:: *spxtype*
      

   Type of function to fit. "plp" = power logarithmic polynomial,
   "ltp" = logarithmic transformed polynomial.

   .. rubric:: *spxest*
      

   REQUIRED. Initial estimates as array of numerical values for the
   spectral index function coefficients. eg [1.5, -0.8] if fitting a
   plp function thought to be close to 1.5*(x/div)**(-0.8) or
   [0.4055, -0.8] if fitting an lpt function thought to be close to
   ln(1.5) - 0.8*ln(x/div).

   *spxfix*

   Fix the corresponding spectral index function coefficients during
   the fit. True means hold fixed.

   .. rubric:: *div*
      

   Divisor (numerical value or quantity) to use in the logarithmic
   terms of the plp or ltp function. 0 means calculate a useful value
   on the fly.

   .. rubric:: *spxsol*
      

   Name of the spectral index function coefficient solution image to
   write.

   .. rubric:: *spxerr*
      

   Name of the spectral index function coefficient error image to
   write.

   .. rubric:: *model*
      

   Name of model image. Default (""): do not write the model image.

   .. rubric:: *residual*
      

   Name of residual image. Default (""): do not write the residual
   image.

   .. rubric:: *wantreturn*
      

   Should a record summarizing the results be returned?

   .. rubric:: *logresults*
      

   Output results to logger?

   .. rubric:: *logfile*
      

   File in which to log results. Default is not to write a logfile.

   .. rubric:: *append*
      

   Append results to logfile? Logfile must be specified. Default is
   to append. False means overwrite existing file if it exists.

   .. rubric:: *sigma*
      

   Standard deviation array or image name(s).

   .. rubric:: *outsigma*
      

   Name of output image used for standard deviation. Ignored if sigma
   is empty.


   Bibliography
      :sup:`1. Brouw, Wim, 1999
      (` `Web <http://www.astron.nl/casacore/trunk/casacore/doc/notes/224.html>`__ :sup:`)` `<#ref-cit1>`__

      :sup:`2. W.H. Press et al. 1988, Cambridge University Press
      (` `PDF <http://www2.units.it/ipl/students_area/imm2/files/Numerical_Recipes.pdf>`__ :sup:`)` `<#ref-cit2>`__


.. _imagename:

imagename (variant='')
   | Name of the input image(s)

.. _box:

box (string='')
   | Rectangular region to select in direction plane. Default is to use the entire direction plane.

.. _region:

region (string='')
   | Region selection. Default is to use the full image.

.. _chans:

chans (string='')
   | Channels to use. Default is to use all channels.

.. _stokes:

stokes (string='')
   | Stokes planes to use. Default is to use all Stokes planes.

.. _axis:

axis (int=-1)
   | The profile axis. Default: use the spectral axis if one exists, axis 0 otherwise (<0).

.. _mask:

mask (string='')
   | Mask to use. Default is none.

.. _minpts:

minpts (int=1)
   | Minimum number of unmasked points necessary to attempt fit.

.. _multifit:

multifit (bool=False)
   | If true, fit a profile along the desired axis at each pixel in the specified region. If false, average the non-fit axis pixels and do a single fit to that average profile. Default False.

.. _spxtype:

spxtype (string='plp')
   | Type of function to fit. "plp" = power logarithmic polynomial, "ltp" = logarithmic transformed polynomial.

.. _spxest:

spxest (doubleArray=[''])
   | REQUIRED. Initial estimates as array of numerical values for the spectral index function coefficients. eg [1.5, -0.8] if fitting a plp function thought to be close to 1.5*(x/div)**(-0.8) or [0.4055, -0.8] if fitting an lpt function thought to be close to ln(1.5) - 0.8*ln(x/div).

.. _spxfix:

spxfix (boolArray=[''])
   | Fix the corresponding spectral index function coefficients during the fit. True means hold fixed.

.. _div:

div (variant='0')
   | Divisor (numerical value or quantity) to use in the logarithmic terms of the plp or ltp function. 0 means calculate a useful value on the fly.

.. _spxsol:

spxsol (string='')
   | Name of the spectral index function coefficient solution image to write.

.. _spxerr:

spxerr (string='')
   | Name of the spectral index function coefficient error image to write.

.. _model:

model (string='')
   | Name of model image. Default: do not write the model image ("").

.. _residual:

residual (string='')
   | Name of residual image. Default: do not write the residual image ("").

.. _wantreturn:

wantreturn (bool=True)
   | Should a record summarizing the results be returned?

.. _stretch:

stretch (bool=False)
   | Stretch the mask if necessary and possible?

.. _logresults:

logresults (bool=True)
   | Output results to logger?

.. _logfile:

logfile (string='')
   | File in which to log results. Default is not to write a logfile.

.. _append:

append (bool=True)
   | Append results to logfile? Logfile must be specified. Default is to append. False means overwrite existing file if it exists.

.. _sigma:

sigma ({string, stringArray, doubleArray, intArray}='')
   | Standard deviation array or image name(s).

.. _outsigma:

outsigma (string='')
   | Name of output image used for standard deviation. Ignored if sigma is empty.


    """
    pass
