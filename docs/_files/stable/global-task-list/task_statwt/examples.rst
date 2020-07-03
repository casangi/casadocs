.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Examples
========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task examples

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Update the weights of a MS as in the **statwt** task. All channels
      in a SPW will receive equal weight:

      .. container:: casa-input-box

         statwt("my.ms")

       

      Update the weights of a MS, using a calculation that disregards
      visibilities in spectral window 2 between channels 7 and 16. All
      channels in a SPW will receive equal weight, even those
      disregarded in the calculation:

      .. container:: casa-input-box

         statwt("my.ms", fitspw='2:7~16’, excludechans=True)

       

      Update the weights of a MS using an algorithm robust to outliers.
      All channels in a SPW will receive equal weight:

      .. container:: casa-input-box

         statwt("my.ms", statalg='chauvenet')

       

      Update the weights of a MS using time binning of 300s. All
      channels in a SPW will receive equal weight, and all times within
      a *timebin* will receive equal weight:

      .. container:: casa-input-box

         statwt("my.ms", timebin="300s")

       

      Update the weights of a MS using time binning of 10 integrations.
      Each channel and integration will receive a unique weight. The
      weight calculation will consider all visibilities within the time
      bin:

      .. container:: casa-input-box

         statwt("my.ms", timebin=10, slidetimebin=True, chanbin=1)

       

      Calculate, but do not update the weights of spectral window 3 of a
      MS. Return statistics which summarize the calculated weights as a
      dictionary:

      .. container:: casa-input-box

         weight_stats = statwt("my.ms", preview=True, spw='3')

       

.. container:: section
   :name: viewlet-below-content-body
