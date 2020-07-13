Examples
========

.. container:: documentDescription description

   task examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric::   Example 1
         :name: example-1

      This is one of the simplest examples. To fit and remove a
      Chebyshev polynomial function (default is 5th order) from the data
      'sd_data.ms', using only spectral window 0, and fitting channels
      100-800 and 1200-2000 (to avoid, for example, band-pass roll off
      at the edges, and perhaps an emission line that might occur over
      channels 800-1200).

      .. container:: casa-input-box

         sdbaseline(infile='sd_data.ms',
         spw='0:100~800;1200~2000',blfunc='chebyshev',outfile='sd_data.ms.bl',overwrite
         =True)  

      .. rubric::  Example 2
         :name: example-2

      This example shows fitting and subtracting a sinusoidal baseline.
      To fit and remove a sinusoid from the data 'sd_data.ms', using
      spectral window 0 and scan number 0. Wave numbers of sinusoids are
      set autmatically in the fft method. 

      .. container:: casa-input-box

         sdbaseline(infile='sd_data.ms',spw='0',scan='0',blfunc='sinusoid',applyfft=True,fftmethod='fft',outfile='sd_data.ms.bl',overwrite=True) 

      .. rubric::  Example 3
         :name: example-3

      In this example, the user specifies different fitting parameters
      per spectrum, using blfunc='variable' and specifying the fit
      parameters using a text file.

      .. container:: casa-input-box

         sdbaseline(infile='sd_data.ms',blfunc='variable',blparam='blparam.txt',outfile='sd_data.ms.bl',overwrite
         =True)

       Here is the text file "blparam.txt" used in the above example.

      .. container:: info-box

         #row,pol,mask,clipniter,clipthresh,use_linefinder,thresh,Ledge,Redge,avg_limit,blfunc,order,npiece,nwave

         0,0,100~750;1250~1900,0,3.,false,0.,0,0,0,chebyshev,2,0,[]

         0,1,,0,3.,false,0.,0,0,0,chebyshev,0,0,[]

         1,0,0~500;1500~2000,0,3.,false,0.,0,0,0,poly,1,0,[] 

       

       

.. container:: section
   :name: viewlet-below-content-body
