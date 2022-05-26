
.. _Description:

Description
   *imbaseline* is a task to do image-based baseline subtraction for single-dish data. This task is based on `sdbaseline <casatasks.single.sdbaseline.html>`__. Input file format of *sdbaseline* is Measurement Set, while CASA Image format is used for the input of *imbaseline*. The computing processes of fitting and subtracting are common in both tasks, and the options of *imbaseline* consist of the subset of *sdbaseline*.
   
   If a user needs to reduce the noise in input data before baseline subtraction, the task can smooth the spacial plane and/or spectral plane setting a parameter of *dirkernel* and *spkernel*, respectively. These features are based on `imsmooth <./casatasks.analysis.imsmooth.html>`__ and `sdsmooth <./casatasks.single.sdsmooth.html>`__.
   
   **Direction plane smoothing** performs a Fourier-based convolution to smooth the spacial plane of input data using a user-specified smoothing kernel. The parameter *dirkernel* can be specified *gaussian*, *boxcar*, and *image*, they are same parameters *kernel* of the task `imsmooth <./casatasks.analysis.imsmooth.html>`__. Usage of parameters related *dirkernel* is the same as in `imsmooth <./casatasks.analysis.imsmooth.html>`__.
   
   **Spectral axis smoothing** performs smoothing along the spectral axis using a user-specified smoothing kernel. The parameter *spkernel* can be specified *gaussian*, *boxcar*, they are same parameters *kernel* of the task `sdsmooth <./casatasks.single.sdsmooth.html>`__. Usage of parameters related *spkernel* is same as those in `sdsmooth <./casatasks.single.sdsmooth.html>`__.

   **Baseline fitting/subtraction** does fitting and subtracting a baseline from single-dish spectra in input data. The parameter *blfunc* can be specified *poly*, *chebyshev*, *cspline*, *sinusoid*, *variable*, and the parameter *maskmode* can be specified *auto*, *list*. Usage of parameters related *blfunc* and *maskmode* is same as in `sdbaseline <casatasks.single.sdbaseline.html>`__.
   
Note 
   * The format of the file specified by *bloutput* is CSV format. It cannot be specified format type.
   * If the parameter *output_cont* set *True*, the output continuum image is saved by subtracting an output image from an input image. The file name of it will be named as the input file name *imagename* + "*.cont*".

.. _Examples:

Example
   **Example 1**
   
   This is one of the simplest examples fitting the baseline using the sinusoidal function and subtracting. No smoothing processes are applied.
   ::
   
      imbaseline( imagename='my_image.im',
                  linefile='output.im',
                  blfunc='sinusoid' )
   
   **Example 2**
   
   Following example shows baseline fitting and subtracting smoothing with the spatial plane. Parameters such as *major*, *minor*, *pa*, should be specified when *dirkernel='gaussian'* is specified. 
   ::
   
      imbaseline( imagename='my_image.im',
                  linefile='output.im',
                  blfunc='sinusoid',
                  dirkernel='gaussian',
                  major='20arcsec',
                  minor='10arcsec',
                  pa='0deg' ) 
   
   **Example 3**
   
   Following examples shows baseline fitting and subtracting smoothing with spectral plane. 
   ::
   
      imbaseline( imagename='my_image.im',
                  linefile='output.im',
                  spkernel='boxcar',
                  kwidth=5 )
   
   
.. _Development:

Development
   No additional development details

