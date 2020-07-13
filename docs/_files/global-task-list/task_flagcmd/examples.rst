Examples
========

.. container:: documentDescription description

   task examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      More examples of using the flagcmd task can be found
      `here <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing/flagging-based-on-a-list-of-commands-flagcmd>`__.

      .. rubric:: Use *inpmode='table'*
         :name: use-inpmodetable

      Use *action='list'* first to see what is in the MS before doing
      anything else.

      .. container:: casa-input-box

         flagcmd(vis='example.ms', inpmode='table', action='list')

      Apply the flags stored in the FLAG_CMD table in the MS. This is
      the default setup of **flagcmd**. Note that when a flag command is
      applied, the corresponding APPLIED column cell will be updated to
      True.

      .. container:: casa-input-box

         flagcmd(vis='example.ms', inpmode='table', action='apply',
         useapplied=False)

      To re-apply the flags stored in the FLAG_CMD table in the MS.

      .. container:: casa-input-box

         flagcmd(vis='example.ms', inpmode='table', action='apply',
         useapplied=True)

      To save flag commands from one MS to another without applying
      them. Flag commands will be copied from "other.ms" to the
      FLAG_CMD of "example.ms".

      .. container:: casa-input-box

         flagcmd(vis='example.ms', inpmode='table', inpfile='other.ms',
         action='list')

      To save flag commands from a file into the MS without applying.

      .. container:: casa-input-box

         flagcmd(vis='example.ms', inpmode='list', inpfile='flags.txt',
         action='list')

      Select only certain rows from the FLAG_CMD table. Currently this
      must be a list of individual row numbers (0-based).

      .. container:: casa-input-box

         flagcmd(vis='example.ms', inpmode='table', action='apply',
         useapplied=False, tablerows=[0,1,2,3,10,11])

         flagcmd(vis='example.ms', inpmode='table', action='apply',
         useapplied=False, tablerows=range(29))

      .. container:: info-box

         **NOTE**: The *useapplied=True/False* parameter is important if
         you are going to (re)apply flags marked as APPLIED True in
         FLAG_CMD. It is common to have a "failed" flagging operation
         mark the flags as already applied and then they don't show up
         when you re-run (e.g. in 'list').  Set *useapplied=True* so
         that it will use these anyway.

      To apply the flag commands from an MS to a calibration table,
      recall that *inpmode='table'* can only be used if an MS is given
      in the inpfile parameter, so that flags from the MS are applied to
      the cal table.

      .. container:: casa-input-box

         flagcmd(vis='mycaltable', inpmode='table',
         inpfile='example.ms', action='apply')

      .. rubric::        
         Use *inpmode='xml'*
         :name: use-inpmodexml

      List the online flags stored in the Flag.xml file of a VLA MS. 

      .. container:: casa-input-box

         flagcmd(vis='example.ms', inpmode='xml', action='list')

      Directly apply the online flags stored in the Flag.xml file in
      the MS, set *inpmode='xml'* and desired buffer.

      .. container:: casa-input-box

         flagcmd(vis='example.ms', inpmode='xml', action='apply',
         tbuff=1.0)

      Apply the flags using a specific set of reasons (a comma separated
      list).

      .. container:: casa-input-box

         flagcmd(vis='example.ms', inpmode='xml', action='apply',
         reason='FOCUS_ERROR,SUBREFLECTOR_ERROR')

      .. container:: info-box

         **NOTE**: The online flag time buffer *tbuff* is specified
         in seconds, but in fact should be keyed to the intrinsic online
         integration time. This is particularly true for EVLA data, were
         a *tbuff* value of 0.5x to 1.5x the integration time is needed
         (currently you should use 1.5x for data taken in early 2011 or
         before).

       

      .. rubric:: Use *inpmode='list'*
         :name: use-inpmodelist

      Apply the flags given in an ASCII file such as the one below,
      which will be saved in a file called "myflags.txt":

      ::

         antenna='ea01' timerange='00:00:00~01:00:00'
         antenna='ea11' timerange='00:00:00~03:00:00' spw='0~4'
         mode='clip' clipminmax=[0,5] correlation='ABS_ALL'
         mode='quack' quackmode='end' quackinterval=1.0
         mode='shadow' antenna='ea01,ea02,ea03'

      .. container:: casa-input-box

         flagcmd(vis='example.ms',inpmode='list',inpfile='myflags.txt')

      Or the flag commands can be given in the interface of the task,
      using a Python list.

      .. container:: casa-input-box

         | flagcmd(vis='example.ms',inpmode='list',inpfile=["mode='shadow'",
         |                                                "mode='clip'
           clipminmax=[0,5] correlation='ABS_ALL'",
         |                                                "mode='quack'
           quackmode='end' quackinterval=1.0",
         |                                              
            "antenna='ea01' timerange='00:00:00~01:00:00'",
         |                                              
            "antenna='ea11' timerange='00:00:00~03:00:00' spw='0~4'"])

       

.. container:: section
   :name: viewlet-below-content-body
