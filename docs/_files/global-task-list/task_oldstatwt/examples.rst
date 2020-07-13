Examples
========

.. container:: documentDescription description

   task examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      To run **oldstatwt** on all targets in an MS and estimate the
      scatter using the standard deviation (not the RMS):

      .. container:: casa-input-box

         oldstatwt(vis='example.ms', dorms=False, intent='*TARGET*',
         datacolumn='corrected', minsamp=2)

       

.. container:: section
   :name: viewlet-below-content-body
