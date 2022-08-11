

.. _Returns:

   out (dict) - names of plot files for action='plot', internal
   flagging dictionary for action='extract'


.. _Description:

Description
   The **flagcmd** task will flag the visibility data or the
   calibration table based on several batch-operations using flag
   commands. There is an extensive and detailed description of this
   task on the `Data Examination and Editing
   chapter <../../notebooks/data_examination.ipynb>`__.
   
   Flag commands follow the mode and parameter names from the
   **flagdata** task. Please refer to the **flagdata** task for a
   detailed explanation.
   
   The **flagcmd** task will flag data based on the commands input on
   *inpmode* such as:
   
   -  'table' = input from FLAG_CMD table in MS
   -  'list' = input from text file or list of strings given in
      *inpfile*
   -  'xml' = input from Flag.xml in the MS given by *vis* (largely
      obsolete with the deprecation of importevla in CASA 5.4)
   
   .. warning:: **WARNING:** The option to import XML files with online flag in
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
      `"importasdm" <../../api/casatasks.rst>`__
      and `"importing
      uv-data" <../../notebooks/visibilities_import_export.ipynb#UV-Data-Import>`__.
   
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
   
   .. note:: **NOTE on flagging calibration tables:**
   
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
   

.. _Examples:

Examples
   More examples of using the flagcmd task can be found
   `here <../../notebooks/data_examination.ipynb#Flag-using-flagcmd>`__.
   
   .. rubric:: Use *inpmode='table'*

   Use *action='list'* first to see what is in the MS before doing
   anything else.
   
   ::
   
      flagcmd(vis='example.ms', inpmode='table', action='list')
   
   Apply the flags stored in the FLAG_CMD table in the MS. This is
   the default setup of **flagcmd**. Note that when a flag command is
   applied, the corresponding APPLIED column cell will be updated to
   True.
   
   ::
   
      flagcmd(vis='example.ms', inpmode='table', action='apply',
              useapplied=False)
   
   To re-apply the flags stored in the FLAG_CMD table in the MS.
   
   ::
   
      flagcmd(vis='example.ms', inpmode='table', action='apply',
              useapplied=True)
   
   To save flag commands from one MS to another without applying
   them. Flag commands will be copied from "other.ms" to the
   FLAG_CMD of "example.ms".
   
   ::
   
      flagcmd(vis='example.ms', inpmode='table', inpfile='other.ms',
              action='list')
   
   To save flag commands from a file into the MS without applying.
   
   ::
   
      flagcmd(vis='example.ms', inpmode='list', inpfile='flags.txt',
              action='list')
   
   Select only certain rows from the FLAG_CMD table. Currently this
   must be a list of individual row numbers (0-based).
   
   ::
   
      flagcmd(vis='example.ms', inpmode='table', action='apply',
              useapplied=False, tablerows=[0,1,2,3,10,11])
   
      flagcmd(vis='example.ms', inpmode='table', action='apply',
              useapplied=False, tablerows=range(29))
   
   .. note:: **NOTE**: The *useapplied=True/False* parameter is important if
      you are going to (re)apply flags marked as APPLIED True in
      FLAG_CMD. It is common to have a "failed" flagging operation
      mark the flags as already applied and then they don't show up
      when you re-run (e.g. in 'list').  Set *useapplied=True* so
      that it will use these anyway.
   
   To apply the flag commands from an MS to a calibration table,
   recall that *inpmode='table'* can only be used if an MS is given
   in the inpfile parameter, so that flags from the MS are applied to
   the cal table.
   
   ::
   
      flagcmd(vis='mycaltable', inpmode='table',
              inpfile='example.ms', action='apply')
   
   .. rubric::        
      Use *inpmode='xml'*

   List the online flags stored in the Flag.xml file of a VLA MS. 
   
   ::
   
      flagcmd(vis='example.ms', inpmode='xml', action='list')
   
   Directly apply the online flags stored in the Flag.xml file in
   the MS, set *inpmode='xml'* and desired buffer.
   
   ::
   
      flagcmd(vis='example.ms', inpmode='xml', action='apply',
              tbuff=1.0)
   
   Apply the flags using a specific set of reasons (a comma separated
   list).
   
   ::
   
      flagcmd(vis='example.ms', inpmode='xml', action='apply',
              reason='FOCUS_ERROR,SUBREFLECTOR_ERROR')
   
   .. note:: **NOTE**: The online flag time buffer *tbuff* is specified
      in seconds, but in fact should be keyed to the intrinsic online
      integration time. This is particularly true for EVLA data, were
      a *tbuff* value of 0.5x to 1.5x the integration time is needed
      (currently you should use 1.5x for data taken in early 2011 or
      before).

   .. rubric:: Use *inpmode='list'*
   
   Apply the flags given in an ASCII file such as the one below,
   which will be saved in a file called "myflags.txt":
   
   ::
   
      antenna='ea01' timerange='00:00:00~01:00:00'
      antenna='ea11' timerange='00:00:00~03:00:00' spw='0~4'
      mode='clip' clipminmax=[0,5] correlation='ABS_ALL'
      mode='quack' quackmode='end' quackinterval=1.0
      mode='shadow' antenna='ea01,ea02,ea03'
   
   ::
   
      flagcmd(vis='example.ms',inpmode='list',inpfile='myflags.txt')
   
   Or the flag commands can be given in the interface of the task,
   using a Python list.
   
   ::
   
      flagcmd(vis='example.ms',inpmode='list',inpfile=["mode='shadow'", "mode='clip'
              clipminmax=[0,5] correlation='ABS_ALL'", "mode='quack'
              quackmode='end' quackinterval=1.0",
              "antenna='ea01' timerange='00:00:00~01:00:00'",
              "antenna='ea11' timerange='00:00:00~03:00:00' spw='0~4'"])

.. _Development:

Development
   No additional development details

