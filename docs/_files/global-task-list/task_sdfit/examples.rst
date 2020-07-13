Examples
========

.. container:: documentDescription description

   Example usage of sdfit.

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      This example is to fit two Gaussian (default) components to all
      integrations in scan 4, polarization 'XX' only, and write the
      output to a file.  The output (sdfitout) is a python dictionary.

      .. container:: casa-input-box

         sdfitout=sdfit(infile=mymeasurement_set,datacolumn='data',scan='4',outfile='sdfit.log',overwrite=T,nfit=[2],pol='XX')

      An Example of output file:

      .. container:: casa-output-box

         | #SCAN   TIME            ANT     BEAM    SPW     POL    
           Function        P0              P1              P2
         | 4       4873839081.0780 2       0       6       0      
           gauss0          2.58050537      15.00975037     3.89437151  
              
         | 4       4873839081.0780 2       0       6       0      
           gauss1          0.72443587      61.37811279     8.87286472

      In this example, only a spectrum is selected in an MS. Each row of
      the output file stores the results of fitting a line in the
      spectrum. The columns P0, P1, and P2, store the peak, channel
      index of line center, and full-width-half-maximum (FWHM,
      in channels), respectively.

      The task returns a dictionary of fit results which stores the
      number of lines, 'nfit', and the fit of each line, i.e., the line
      center, 'cent', the full-width-half-maximum, 'fwhm', and peak,
      'peak'. Each value except for 'nfit' is a list of 2 entries [fit
      value, error].

      .. container:: casa-input-box

         sdfitout

      .. container:: casa-output-box

         Out[**1**]: 

         | {'cent': [[[15.00975037, 0.04713312], [61.37811279,
           0.25342196]]],
         |  'fwhm': [[[3.89437151, 0.11099002], [8.87286472,
           0.59676313]]],
         |  'nfit': [2],
         |  'peak': [[[2.58050537, 0.06369157], [0.72443587,
           0.04219575]]]}

       To obtain the peak of the second line in the first spectrum from
      the dictionary,

      .. container:: casa-input-box

         sdfitout['peak'][0][1]

      .. container:: casa-output-box

         Out[**2**]: [0.72443587, 0.04219575]

      The first entry is the fitted value and the second one is the
      error on the fitted value.

      To fit three lines in a region:

      .. container:: casa-input-box

          sdfitout=sdfit(infile=mymeasurement_set,fitmode='list',nfit=[3])

      To fit two lines in two regions:

      .. container:: casa-input-box

          sdfitout=sdfit(infile=mymeasurement_set,fitmode='list',nfit=[2,2])

      To automatically fit any lines with S/N > 2, averaging over four
      channels (i.e. smoothing), and requiring lines to be at least 10
      channels wide, while excluding channels 0:1000 from beginning and
      500:end from the end of the spectrum:

      .. container:: casa-input-box

         sdfitout=sdfit(infile=mymeasurement_set,fitmode='auto',
         edge=[1000,500],avg_limit='4', thresh='2',minwidth='10') 

      This example directs the output to a file, mysd.fit :

      .. container:: casa-input-box

         sdfitout=sdfit(infile=mymeasurement_set,outfile='mysd.fit')

      | 
      |  

.. container:: section
   :name: viewlet-below-content-body
