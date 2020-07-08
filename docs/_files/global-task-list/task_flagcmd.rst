.. container::
   :name: viewlet-above-content-title

flagcmd
=======

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task flagcmd description

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      The **flagcmd** task will flag the visibility data or the
      calibration table based on several batch-operations using flag
      commands. There is an extensive and detailed description of this
      task on the `Data Examination and Editing
      chapter <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing>`__.

      Flag commands follow the mode and parameter names from the
      **flagdata** task. Please refer to the **flagdata** task for a
      detailed explanation.

      The **flagcmd** task will flag data based on the commands input on
      *inpmode* such as:

      -  'table' = input from FLAG_CMD table in MS
      -  'list' = input from text file or list of strings given in
         *inpfile*
      -  'xml' = input from Flag.xml in the MS given by *vis* (largely
         obsolete with the deprecation of importevla in CASA 5.4)

      .. container:: alert-box

         **WARNING:** The option to import XML files with online flag in
         flagcmd has largely become obsolete with the deprecation of
         task **importevla** in CASA 5.4, because the recommended
         **importasdm** task cannot copy the actual XML tables from the
         original SDM to the newly created MS (it can only apply the
         online flags directly, or write them into ascii tables). The
         *Flag.xml, Antenna.xml* and *SpectralWindow.xml* tables must
         first be copied manually into the top-level MS directory for
         use by flagcmd (not the recommended approach). Consider the use
         of the recommended task **flagdata** instead, as explained in
         the CASA Docs chapters on
         `"importasdm" <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_importasdm>`__
         and `"importing
         uv-data" <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/visibility-data-import-export/uv-data-import>`__.

         **IMPORTANT**: The FLAG_CMD sub-table is meant only for
         meta-data selections such as online flags. Using it to save
         other parameters (from modes such as clip, quack, shadow, etc)
         is possible but carries a risk that in future releases these
         parameters maybe renamed or changed their default values. Use
         it at your own risk! There will be no automatic way to rename
         any parameter that changes in the future.  

         There is no way to guarantee that a command from the COMMAND
         column has been applied or not to the MS, even if the APPLIED
         column is set to True. If you use other ways to flag such as
         interactive flagging in plotms, the FLAG_CMD will not be
         updated! Use at your own risk.

      .. container:: info-box

         **NOTE on flagging calibration tables:**

         It is possible to flag cal tables using this task, although we
         recommend using the **flagdata** task for this.

         When using this task to flag cal tables, only the 'apply' and
         'list' actions are supported. Because cal tables do not have a
         FLAG_CMD sub-table, the default *inpmode='table'* can only be
         used if an MS is given in the *inpfile* parameter, so that
         flags from the MS are applied to the cal table. Otherwise the
         flag commands must be given using *inpmode='list'*, either from
         a file(s) or from a list of strings. See the parameters tab for
         more information. Data selection for calibration tables is
         limited to field, scan, antenna, time, spw and observation. If
         the calibration table was created before CASA 4.1, this task
         will create a dummy OBSERVATION column and OBSERVATION
         sub-table in the input calibration table to adapt it to the new
         cal table format.

       

.. container:: section
   :name: viewlet-below-content-body


.. toctree::
   :hidden:
   :maxdepth: 3

   task_flagcmd/about
   task_flagcmd/parameters
   task_flagcmd/changelog
   task_flagcmd/examples
   task_flagcmd/developer