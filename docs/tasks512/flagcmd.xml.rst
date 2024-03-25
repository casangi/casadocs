flagcmd -- Flagging task based on batches of flag-commands -- data editing task
=======================================

Description
---------------------------------------

    The flagcmd task allows several batch-operations using flag commands.

    Flag commands follow the mode and parameter names from the flagdata task
    (also explained below).  The available modes are: manual, clip, shadow, quack, 
    elevation,  tfcrop, rflag and extend. The summary mode is not supported
    in this task. Use the flagdata task for that.

    The flagcmd task will flag data based on the commands input on inpmode :
        table = input from FLAG_CMD table in MS
        list  = input from text file or list of strings given in inpfile
        xml   = input from Flag.xml in the MS given by vis

    Batch operations include : apply/unapply/list/plot/clear/extract

    IMPORTANT: The FLAG_CMD sub-table is meant only for meta-data selections such as online flags.
       Using it to save other parameters (from modes such as clip, quack, shadow, etc) is
       possible but carries a risk that in future releases these parameters maybe renamed
       or changed their default values. Use it at your own risk! There will be no automatic
       way to rename any parameter that changes in the future.
    
       There is no way to guarantee that a command from the COMMAND column has been
       applied or not to the MS, even if the APPLIED column is set to True. If you
       use other ways to flag such as interactive flagging in plotms, the FLAG_CMD
       will not be updated! Use at your own risk.
               
    NOTE on flagging calibration tables.
    -----------------------------------
    
    It is possible to flag cal tables using this task, although we recommend using the flagdata
    task for this.
    
    When using this task to flag cal tables, only the 'apply' and 'list' actions are supported. 
    Because cal tables do not have a FLAG_CMD sub-table, the default inpmode='table' can only 
    be used if an MS is given in the 'inpfile' parameter so that flags from the MS are applied to 
    the cal table. Otherwise, the flag commands must be given using inpmode='list', either from a 
    file(s) or from a list of strings. See below for more information about these parameters. 
    Data selection for calibration tables is limited to field, scan, antenna, time, spw and
    observation. If the calibration table was created before CASA 4.1, this task will create 
    a dummy OBSERVATION column and OBSERVATION sub-table in the input calibration table to
    adapt it to the new cal table format.
        
        


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - vis
     - :code:`''`
     - 
   * - inpmode
     - :code:`'table'`
     - 
   * - inpfile
     - :code:`''`
     - 
   * - tablerows
     - :code:`numpy.array( [  ] )`
     - 
   * - reason
     - :code:`'any'`
     - 
   * - useapplied
     - :code:`False`
     - 
   * - tbuff
     - :code:`float(0.0)`
     - 
   * - ants
     - :code:`''`
     - 
   * - action
     - :code:`'apply'`
     - 
   * - flagbackup
     - :code:`True`
     - 
   * - clearall
     - :code:`False`
     - 
   * - rowlist
     - :code:`numpy.array( [  ] )`
     - 
   * - plotfile
     - :code:`''`
     - 
   * - savepars
     - :code:`False`
     - 
   * - outfile
     - :code:`''`
     - 
   * - overwrite
     - :code:`True`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of MS file or calibration table to flag


inpmode
---------------------------------------

:code:`'table'`

Input mode for flag commands(table/list/xml)


inpfile
---------------------------------------

:code:`''`

Source of flag commands


tablerows
---------------------------------------

:code:`numpy.array( [  ] )`

Rows of inpfile to read


reason
---------------------------------------

:code:`'any'`

Select by REASON types


useapplied
---------------------------------------

:code:`False`

Select commands whose rows have APPLIED column set to True


tbuff
---------------------------------------

:code:`float(0.0)`

Time buffer (sec) to pad flags


ants
---------------------------------------

:code:`''`

Allowed flag antenna names to select by


action
---------------------------------------

:code:`'apply'`

Action to perform in MS and/or in inpfile (apply/unapply/list/plot/clear/extract)


flagbackup
---------------------------------------

:code:`True`

Automatically backup the FLAG column before execution


clearall
---------------------------------------

:code:`False`

Delete all rows from FLAG_CMD


rowlist
---------------------------------------

:code:`numpy.array( [  ] )`

FLAG_CMD rows to clear


plotfile
---------------------------------------

:code:`''`

Name of output file to save plot


savepars
---------------------------------------

:code:`False`

Save flag commands to the MS or to a file


outfile
---------------------------------------

:code:`''`

Name of output file to save commands


overwrite
---------------------------------------

:code:`True`

Overwrite an existing file to save the flag commands




