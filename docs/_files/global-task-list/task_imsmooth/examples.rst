Examples
========

.. container:: documentDescription description

   task examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. container:: casa-input-box

         | # smoothing with a gaussian kernel 20arseconds by 10
           arseconds
         | imsmooth( imagename='my.image', kernel='gauss',
           major='20arcsec', minor='10arcsec', pa="0deg")

      .. container:: casa-input-box

         | # the same as before, just a different way of specifying the
           kernel parameters
         | mybeam = {'major': '20arcsec', 'minor': '10arcsec', 'pa':
           '0deg'}
         | imsmooth( imagename='my.image', kernel='gauss', beam=mybeam)

      .. container:: casa-input-box

         | # Smoothing using pixel coordinates and a boxcar kernel.
         | imsmooth( imagename='new.image', major='20pix',
           minor='10pix', kernel='boxcar')

      ::

          

.. container:: section
   :name: viewlet-below-content-body
