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

      To import all K-band data from two archival VLA data-sets and
      write them out in a single MeasurementSet, taking into account all
      bands (and placing them in different spectral windows), applying
      the system temperatures and excluding the auto-correlations:

      .. container:: casa-input-box

         importvla(archivefiles=['inputfile1','inputfile2'],
         vis='output.ms', bandname='K', applytsys=True, autocorr=False)

       

.. container:: section
   :name: viewlet-below-content-body
