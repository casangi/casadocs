Examples
========

.. container:: documentDescription description

   task examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      For a MeasurementSet 'calibrated.ms', the continuum imaging
      sensitivity using natural weighting for field id 3 and a subset of
      channels in spw 0 can be obtained as follows:

      .. container:: casa-input-box

         | aps=apparentsens(vis='calibrated.ms',
         |                  spw='0:0~30;40~80',
         |                  field='3',
         |                  specmode='mfs',
         |                  cell='0.007arcsec',imsize=[2048, 2048],
         |                  weighting='natural')

          print aps

       

      The returned dictionary is (also reported in logger):

      .. container:: casa-output-box

         {'relToNat': 1.0000000000089664, 'effSens':
         1.0022319615408699e-05}

      Note that the 'relToNat' factor is 1.0.

      For the same MS and selection, but with Briggs weighting:

      .. container:: casa-input-box

         | aps=apparentsens(vis='calibrated.ms',
         |                  spw='0:0~30;40~80',
         |                  field='3',
         |                  specmode='mfs',
         |                  cell='0.007arcsec',imsize=[2048, 2048],
         |                  weighting='briggs',
         |                  robust=0.5)

         print aps

      The returned dictionary is (also reported in logger):

      .. container:: casa-output-box

         {'relToNat': 1.1450564209993626, 'effSens':
         1.1476121428828694e-05}

      Note that Briggs weighting is ~14% less sensitive in this case.

       

       

       

       

       

       

       

       

       

       

       

       

       

       

       

.. container:: section
   :name: viewlet-below-content-body
