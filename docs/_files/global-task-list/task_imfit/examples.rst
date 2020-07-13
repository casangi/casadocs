Examples
========

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Here is how one might fit two Gaussians to multiple channels of a
      cube using the fit from the previous channel as the initial
      estimate for the next. It also illustrates how one can specify a
      region in the associated continuum image as the region to use as
      the fit for the channel.

      .. container::

         .. container:: casa-input-box

            | default imfit
            | imagename = "co_cube.im"

            | # specify box around source
            | box = "50,50,100,100"
            | chans = "2~20"
            | # only use pixels with positive values in the fit
            | excludepix = [-1e10,0]
            | # estimates file contains initial parameters for two
              Gaussians in channel 2
            | estimates = "initial_estimates.txt"
            | # append results to the log file for all the channels
            | append = "True"
            | imfit()

.. container:: section
   :name: viewlet-below-content-body
