Examples
========

.. container:: documentDescription description

   task examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      This example was taken from the simulation CASAguide located
      `here <https://casaguides.nrao.edu/index.php/Simulation_Guide_Component_Lists_(CASA_5.1)>`__.

      .. container:: casa-input-box

         | default("simanalyze")
         | project = "FITS_list"
         | vis="FITS_list.alma.cycle5.1.ms"
         | imsize = [256,256]
         | imdirection = "J2000 10h00m00.0s -30d00m00.0s"
         | cell = '0.1arcsec'
         | niter = 5000
         | threshold = '10.0mJy/beam'
         | analyze = True
         | simanalyze()

       

.. container:: section
   :name: viewlet-below-content-body
