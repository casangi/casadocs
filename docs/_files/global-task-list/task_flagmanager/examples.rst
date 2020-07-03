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

      .. rubric:: Examples of using **flagmanager** to manipulate the
         flag versions of a MeasurementSet
         :name: examples-of-using-flagmanager-to-manipulate-the-flag-versions-of-a-measurementset

      First save the flags from a MS using **flagdata**

      .. container:: casa-input-box

         flagdata('my.ms', mode='manual', autocorr=True,
         flagbackup=True)

      List the existing flag versions of the above MS

      .. container:: casa-input-box

         flagmanager('my.ms', mode='list')

      The output of the above command can be seen below. Note that the
      first flag versions is called 'Original", which was saved at
      import time using **importasdm**. The second entry called
      'flagdata_1' is the flag versions from the above manual flagging.

      .. container:: casa-output-box

         2018-04-23 18:47:19 INFO flagmanager::agentflagger:: + MS :
         /Users/casadir/work/my.ms

         2018-04-23 18:47:19 INFO flagmanager::agentflagger:: main :
         working copy in main table

         2018-04-23 18:47:19 INFO flagmanager::agentflagger:: Original :
         Original flags at import into CASA

         2018-04-23 18:47:19 INFO flagmanager::agentflagger:: flagdata_1
         : Flags autosave on 2018-04-23 20:47:14

      A captured Python dictionary returns the same content but is
      machine readable: 

      .. container:: casa-input-box

         myflaglist = flagmanager('myvis.ms', mode='list')

      .. container:: casa-output-box

         {0:{'name': 'Original', 'comment': 'Original flags at import
         into CASA'}, 1:{'name': 'flagdata_1', 'comment': 'Flags
         autosave on 2018-04-23 20:47:14'}}

       

      Rename the flag version to a more meaningful name

      .. container:: casa-input-box

         flagmanager('my.ms', mode='rename', oldname='flagdata_1',
         versionname='autocorr', comment='Flags from autocorrelation')

      Restore the original flags to the MS

      .. container:: casa-input-box

         flagmanager('my.ms', mode='restore', versionname='Original')

       

       

       

.. container:: section
   :name: viewlet-below-content-body
