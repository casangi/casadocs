Examples
========

.. container:: documentDescription description

   task examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      More information on **uvmodelfit** can be found
      `here <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/uv-manipulation/fitting-gaussians-to-visibilities>`__.

      Example:

      .. container:: casa-input-box

         | # Note: It's best to channel average the data if there are
           many channels before running a modelfit
         | split('ngc5921.ms','1445+099_avg.ms',
           datacolumn='corrected',field='1445*',width='63')
         |  

         | # Initial guess is that it's close to the phase center and
           has a flux of 2.0 (a priori we know it's 2.47)
         | uvmodelfit('1445+099_avg.ms', # use averaged data
         |            niter=5, # Do 5 iterations
         |            comptype='P', # P=Point source, G=Gaussian, D=Disk
         |            sourcepar=[2.0,.1,.1], # Source parameters for a
           point source
         |            spw='0',  
         |            outfile='gcal.cl') # Output component list file

.. container:: section
   :name: viewlet-below-content-body
