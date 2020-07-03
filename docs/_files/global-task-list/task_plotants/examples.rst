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

      Plot antenna positions and make a plot in a ps-file:

      .. container:: casa-input-box

         | # In CASA
         | plotants(vis='ngc5921.ms', figfile='ngc5921ants.ps')

      Plot logarithmic positions of antennas in main table, labeled with
      antenna ID:

      .. container:: casa-input-box

         plotants(vis='ngc5921.ms', antindex=True, logpos=True,
         checkbaselines=True)

      Plot antenna positions but exclude antennas 1, 2, 3, 5, and 7:

      .. container:: casa-input-box

         plotants(vis='ngc5921.ms', exclude='1~3,5,7')

.. container:: section
   :name: viewlet-below-content-body
