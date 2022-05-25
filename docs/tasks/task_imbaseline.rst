
.. _Description:

Description
   This is the task to do image-based baseline subtraction for single-dish data. 
   If a user needs to reduce the noise in input data before baseline subtraction, the task can smooth the direction plane and/or spectral axis of input data.
   
   **Direction plane smoothing** performs a Fourier-based convolution to smooth the direction plane of input data using a user-specified smoothing kernel. The parameter *dirkernel* could be specified *gaussian*, *boxcar*, and *image*, they are the same as parameter *kernel* of the task `imsmooth <./casatasks.analysis.imsmooth.html>`__. Also the usage of parameters related *dirkernel* is the same as in `imsmooth <./casatasks.analysis.imsmooth.html>`__.
   
   **Spectral axis smoothing** performs smoothing along the spectral axis using a user-specified smoothing kernel. The parameter *spkernel* could be specified *gaussian*, *boxcar*, they are the same as parameter *kernel* of the task `sdsmooth <./casatasks.single.sdsmooth.html>`__. Also the usage of parameters related *spkernel* is the same as in `sdsmooth <./casatasks.single.sdsmooth.html>`__.

   **Baseline subtraction** does fitting and/or subtracting a baseline from single-dish spectra in input data. The parameter *blfunc* could be specified *poly*, *chebyshev*, *cspline*, *sinusoid*, *variable*, and it is the same role as the parameter *blfunc* of the task `sdbaseline <casatasks.single.sdbaseline.html>`__. Also the usage of parameters related *blfunc* is the same as in `sdbaseline <casatasks.single.sdbaseline.html>`__.

.. _Examples:

Examples
   task examples

.. _Development:

Development
   No additional development details

