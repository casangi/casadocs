Examples
========

.. container:: documentDescription description

   task examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      To concatenate the two MeasurementSets 'ngc5921.ms' and 'src2.ms'
      into a file named 'out.mms':

      .. container:: casa-input-box

         virtualconcat(vis=['src2.ms','ngc5921.ms'],
         concatvis='out.mms')

      The original 'ngc5921.ms' and 'src2.ms' are gone. The output data
      'out.mms' is a Multi-MS. As most of the data is only moved, not
      copied, this is faster and subsequent tasks can run in parallel on
      the Sub-MSs of 'out.mms'.

       

      To concatenate the two MeasurementSets 'ngc5921.ms' and 'src2.ms'
      into a file named 'out.mms', but keeping the original
      MeasurementSets:

      .. container:: casa-input-box

         virtualconcat(vis=['src2.ms','ngc5921.ms'],
         concatvis='out.mms', keepcopy=True)

      Compared to the first example, this consumes more disk space and
      time for the copy.    

      .. container:: info-box

         NOTE: Run flagmanager to save flags in the concatvis.

       

.. container:: section
   :name: viewlet-below-content-body
