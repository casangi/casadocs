
.. _Description:

Description
   This is the task to do image-based baseline subtraction for single-dish data. *imbaseline* is based on `sdbaseline <casatasks.single.sdbaseline.html>`__. *sdbaseline* fits/subtracts a baseline in data of Measurement Set format, but *imbaseline* does in CASA Image format. The computing processes of fitting/subtracting are common in both tasks, and the options of *imbaseline* are the subset of them of *sdbaseline*.
   
   If a user needs to reduce the noise in input data before baseline subtraction, the task can smooth the direction plane and/or spectral axis of input data. These features are based on `imsmooth <./casatasks.analysis.imsmooth.html>`__ and `sdsmooth <./casatasks.single.sdsmooth.html>`__.
   
   **Direction plane smoothing** performs a Fourier-based convolution to smooth the direction plane of input data using a user-specified smoothing kernel. The parameter *dirkernel* could be specified *gaussian*, *boxcar*, and *image*, they are the same as parameter *kernel* of the task `imsmooth <./casatasks.analysis.imsmooth.html>`__. Also the usage of parameters related *dirkernel* is the same as in `imsmooth <./casatasks.analysis.imsmooth.html>`__.
   
   **Spectral axis smoothing** performs smoothing along the spectral axis using a user-specified smoothing kernel. The parameter *spkernel* could be specified *gaussian*, *boxcar*, they are the same as parameter *kernel* of the task `sdsmooth <./casatasks.single.sdsmooth.html>`__. Also the usage of parameters related *spkernel* is the same as in `sdsmooth <./casatasks.single.sdsmooth.html>`__.

   **Baseline fitting/subtraction** does fitting and/or subtracting a baseline from single-dish spectra in input data. The parameter *blfunc* could be specified *poly*, *chebyshev*, *cspline*, *sinusoid*, *variable*, and it is the same role as the parameter *blfunc* of the task `sdbaseline <casatasks.single.sdbaseline.html>`__. Also the usage of parameters related *blfunc* is the same as in `sdbaseline <casatasks.single.sdbaseline.html>`__.
   
   Note: The format of the file specified by 'bloutput' is CSV format.

.. _Examples:

Example
   **Example 1**
   
   This is one of the simplest example. It is fitting and subtracting a sinusoidal baseline. There are no parameters about smoothing, so any smoothing processes don't run.
   ::
   
      imbaseline( imagename='my_image.im',
                  linefile='output.im',
                  blfunc='sinusoid' )
   
   **Example 2**
   
   This example shows the direction plane smoothing and fitting/subtracting. The parameters *major*, *minor*, *pa* must be specified when the value *dirkernel* is *gaussian*.
   ::
   
      imbaseline( imagename='my_image.im',
                  linefile='output.im',
                  blfunc='sinusoid',
                  dirkernel='gaussian',
                  major='20arcsec',
                  minor='10arcsec',
                  pa='0deg' ) 
   
   **Example 3**
   
   This is an example of the spectral plane smoothing and fitting/subtracting.
   ::
   
      imbaseline( imagename='my_image.im',
                  linefile='output.im',
                  spkernel='boxcar',
                  kwidth=5 )
   
   
.. _Development:

Development
   No additional development details

