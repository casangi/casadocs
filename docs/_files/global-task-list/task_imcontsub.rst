imcontsub
=========

.. container:: documentDescription description

   imcontsub task: Estimates and subtracts continuum emission from an
   image cube

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      For each direction pixel in an image (or a subset selected by
      *region* and/or *box*), this task estimates the continuum by
      fitting a polynomial to one or more subsets of the channels. In
      most cases, the user should choose the subset(s) of channels to be
      free of spectral lines. The continuum estimate is saved in
      *contfile* and subtracted from the image (or its subset) to make a
      spectral line estimate, which is saved in *linefile*.

      While imcontsub offers users the option to save the continuum
      estimate as a (multi-channel) dataset, the optimal way to create a
      continuum image is by using the multi-frequency synthesis (MFS)
      option in **tclean**.

      Note that fitting the continuum and subtracting it from a spectral
      line data set can also be done in the *(u,v)*-domain using the
      task **uvcontsub**.

       

      .. rubric:: Task-specific Parameter Descriptions
         :name: task-specific-parameter-descriptions

      .. rubric:: *linefile*
         :name: linefile

      Name of image to which to save the result of subtracting the
      computed continuum from the input image.

      .. rubric:: *contfile*
         :name: contfile

      The computed continuum image.

      .. rubric:: *fitorder*
         :name: fitorder

      Order of polynomial to fit to the specified spectral channels to
      determine the continuum.

      .. rubric:: *chans*
         :name: chans

      Spectral channels to use for fitting a polynomial to determine
      continuum.

.. container:: section
   :name: viewlet-below-content-body

.. toctree::
   :hidden:
   :maxdepth: 3

   task_imcontsub/parameters
   task_imcontsub/changelog
   task_imcontsub/examples
