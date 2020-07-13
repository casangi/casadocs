Examples
========

.. container:: documentDescription description

   task examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Run the MTMFS deconvolver to generate wideband Taylor coefficient
      solutions from spectral windows 0, 1 and 2 of a dataset:

      .. container:: casa-input-box

         tclean(vis='xxx.ms', imagename='try', spw='0~3', imsize=200,
         cell='10.0arcsec', deconvolver='mtmfs', nterms=2, niter=20)

       

      Apply wideband PB correction using the middle channel (for
      example, channel number 32) from each spectral window to compute a
      primary beam cube to which Taylor coefficients are fit:

      .. container:: casa-input-box

         widebandpbcor(vis='xxx.ms', imagename='try', nterms=2,
         threshold='0.1Jy', action='pbcor', spwlist=[0,1,2],
         chanlist=[32,32,32], weightlist=[1.0,1.0,1.0])

       

      Use the 'calcalpha' mode to recalculate spectral index with a
      different threshold at which to apply the True/False mask in the
      ouput image:

      .. container:: casa-input-box

         widebandpbcor(vis='xxx.ms', imagename='try', nterms=2,
         threshold='0.05Jy', action='calcalpha')

       

.. container:: section
   :name: viewlet-below-content-body
