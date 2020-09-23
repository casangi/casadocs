

.. _Description:

Description
   

.. _Examples:

Examples
   task examples
   
   ::
   
      | # smoothing with a gaussian kernel 20arseconds by 10
        arseconds
      | imsmooth( imagename='my.image', kernel='gauss',
        major='20arcsec', minor='10arcsec', pa="0deg")
   
   ::
   
      | # the same as before, just a different way of specifying the
        kernel parameters
      | mybeam = {'major': '20arcsec', 'minor': '10arcsec', 'pa':
        '0deg'}
      | imsmooth( imagename='my.image', kernel='gauss', beam=mybeam)
   
   ::
   
      | # Smoothing using pixel coordinates and a boxcar kernel.
      | imsmooth( imagename='new.image', major='20pix',
        minor='10pix', kernel='boxcar')
   
   ::
   

.. _Development:

Development
   task developer
   
   --CASA Developer--
   
   