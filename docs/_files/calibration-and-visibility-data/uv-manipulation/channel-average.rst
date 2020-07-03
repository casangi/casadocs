.. container::
   :name: viewlet-above-content-title

Channel average
===============

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Channel averaging highlights using mstransform and split

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Both **mstransform** & **split** support averaging data by
      frequency channel.  In **split** the amount of channel averaging
      (if any) is set by top-level parameter *width*.

      .. container:: casa-input-box

         width  = 1     # Number of channels to average to form one
         output channel

      In **mstransform** this capability is accessed by
      specifying *chanaverage=True* and setting the resulting
      sub-parameter *chanbin*, as shown here:  

      .. container:: casa-input-box

         | chanaverage = True      # Average data in channels.
         | chanbin     = 1         # Width (bin) of input channels to
           average to form an output channel.

      Some new features of split / mstransform relative to the old
      implementation of split are as follows

      -  Whereas the old version of split performed a flat average
         taking into account only the *FLAG* column, **mstransform** /
         **split** use both *FLAG* and spectral weights (when present),
         resulting in a weighted average. To be specific
         *WEIGHT_SPECTRUM* is used when averaging *CORRECTED_DATA*, and
         *SIGMA_SPECTRUM* is used when averaging the *DATA* column.
      -  Also **mstransform** / **split** are able to transform the
         input *WEIGHT/SIGMA_SPECTRUM* according to the rules of error
         propagation that apply to a weighted average, which result in
         an output weight equals to the sum of the input weights. For a
         detailed reference see, *Data Reduction and Error Analysis*
         `[1] <#cit>`__.
      -  Both **mstransform** / **split** drop the last output channel
         bin when there are not enough contributors to fully populate
         it. For instance, if the input SPW has 128 channels and
         *chanbin* is 10, the resulting averaged SPW would have 12
         channels and not 13 channels.

      The chanbin parameter can be either a scalar or a vector. In the
      former case, the same chanbin is applied to all the spectral
      windows. In the second case, each element of the chanbin vector
      will apply to the selected spectral windows. Obviously the size of
      the chanbin vector and the number of selected spectral windows
      have to match.

      .. container:: alert-box

         If spw combination and channel average are used together
         (combinespws=True, chanaverage = True), the chanbin parameter
         can only be a scalar. This is due to the fact that channel
         average applies to the already spw combined MS, which contains
         one single spw.

      =============== ================================================
      Citation Number 1
      Citation Text   Bevington & Robinson, 3rd Ed., McGraw Hill, 2003
      =============== ================================================

.. container:: section
   :name: viewlet-below-content-body
