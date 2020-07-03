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

   task blcal examples

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

       

      In this example, we solve for constant (*solint='inf'*)
      frequency-independent (*freqdep=False*) baseline-based solutions
      relative to ordinary gain, bandpass, and gaincurve calibration:

      .. container:: casa-input-box

         | blcal(vis='data.ms',
         |       caltable='cal.M',                        # Output table
           name
         |       field='2',                               # A field with
           a very good model
         |       solint='inf',                            # single
           solution per baseline, spw
         |       gaintable=['cal.B','cal.gc','cal.G90s'], # all prior
           cal
         |       freqdep=False)                           #
           frequency-independent solution

       

       

       

       

.. container:: section
   :name: viewlet-below-content-body
