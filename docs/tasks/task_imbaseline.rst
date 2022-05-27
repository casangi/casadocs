
.. _Description:

Description
   `imbaseline <./casatasks.analysis.imbaseline.html>`__ is a task to do image-based baseline subtraction for single-dish data. This task is based on `sdbaseline <casatasks.single.sdbaseline.html>`__. Input file format of `sdbaseline <casatasks.single.sdbaseline.html>`__ is Measurement Set, while CASA Image format is used for the input of `imbaseline <./casatasks.analysis.imbaseline.html>`__. The computing processes of fitting and subtracting are common in both tasks, and the options of `imbaseline <./casatasks.analysis.imbaseline.html>`__ consist of subset of `sdbaseline <casatasks.single.sdbaseline.html>`__.
   
   If users need to reduce the noise in input data before baseline subtraction, `imbaseline <./casatasks.analysis.imbaseline.html>`__ can make smoothing in the spatial plane and/or spectral axis setting parameters of *dirkernel* and *spkernel*, respectively. These features are based on `imsmooth <./casatasks.analysis.imsmooth.html>`__ and `sdsmooth <./casatasks.single.sdsmooth.html>`__, respectively.
   
   **Spatial plane smoothing** performs a Fourier-based convolution to smooth the spatial plane of input data using a user-specified smoothing kernel. The parameter *dirkernel* can be specified as *gaussian*, *boxcar*, or *image*. They are same parameters *kernel* of the task `imsmooth <./casatasks.analysis.imsmooth.html>`__. Usage of parameters related *dirkernel* is same as those used in `imsmooth <./casatasks.analysis.imsmooth.html>`__.
   
   **Spectral axis smoothing** can be performed using a user-specified smoothing kernel. The parameter *spkernel* can be specified as *gaussian* or *boxcar*. They are same parameters *kernel* of the task `sdsmooth <./casatasks.single.sdsmooth.html>`__. Usage of parameters related *spkernel* is same as those used in `sdsmooth <./casatasks.single.sdsmooth.html>`__.

   **Baseline fitting and subtraction** can be performed with specifying a parameter *blfunc* either *poly*, *chebyshev*, *cspline*, *sinusoid*, or *variable*. The parameter *maskmode* can be specified as *list* or *auto*. Usage of parameters related *blfunc* and *maskmode* are same as those used in `sdbaseline <casatasks.single.sdbaseline.html>`__.
   
Note 
   * The format of the file specified by *bloutput* should be CSV format when using `imbaseline <./casatasks.analysis.imbaseline.html>`__.
   * If the parameter *output_cont* sets *True*, the output continuum image is saved by subtracting an output image from an input image. The file will be named as *imagename* + "*.cont*".

.. _Examples:

Example
   **Example 1**
   
   This is one of the simplest examples fitting baselines using the sinusoidal function and subtracting. No smoothing processes are applied.
   ::
   
      imbaseline(imagename='my_image.im',
                 linefile='output.im',
                 blfunc='sinusoid')
   
   **Example 2**
   
   Following example shows baseline fitting and subtracting smoothing with the spatial plane. Parameters such as *major*, *minor*, and *pa*, should be specified when *dirkernel='gaussian'*. 
   ::
   
      imbaseline(imagename='my_image.im',
                 linefile='output.im',
                 blfunc='sinusoid',
                 dirkernel='gaussian',
                 major='20arcsec',
                 minor='10arcsec',
                 pa='0deg') 
   
   **Example 3**
   
   Following examples shows baseline fitting and subtracting smoothing with the spectral axis. 
   ::
   
      imbaseline(imagename='my_image.im',
                 linefile='output.im',
                 spkernel='boxcar',
                 kwidth=5)
   
   
.. _Development:

Development
   No additional development details

