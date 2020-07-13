Examples
========

.. container:: documentDescription description

   tool msmetadata examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. container:: casa-input-box

         | # attach tool to an MS
         | msmd.open("3C273XC1.MS")
         | # get the number of spectral windows
         | nspw = msmd.nspw()
         | # free up resources used by the attached tool
         | msmd.done()

      We open the tool by querying the MS for its metadata. We then get
      the number of spectral windows in the dataset and close the tool.

       

      .. container:: casa-input-box

         | # attach tool to an MS
         | msmd.open("3C273XC1.MS")
         | # get the diameter of the antenna named 'VB2'
         | diameter = msmd.antennadiameter()
         | # free up resources used by the attached tool
         | msmd.done()

      We open the tool by querying the MS for its metadata. We then get
      the diameter of antenna 'VB2' and close the tool.

       

      .. container:: casa-input-box

         | # attach tool to an MS
         | msmd.open("3C273XC1.MS")
         | # get the on-source integration time
         | exposure_time = msmd.effexposuretime()
         | # free up resources used by the attached tool
         | msmd.done()

      We open the tool by querying the MS for its metadata. We then get
      the on-source integration time and close the tool.

       

      .. container:: casa-input-box

         | # attach tool to an MS
         | msmd.open("3C273XC1.MS")
         | # get the field names in the MS
         | fieldnames = msmd.fieldnames()
         | # free up resources used by the attached tool
         | msmd.done()

      We open the tool by querying the MS for its metadata. We then get
      the field names fromm the MS and close the tool.

.. container:: section
   :name: viewlet-below-content-body
