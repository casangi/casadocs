#
# stub function definition file for docstring parsing
#

def flagcmd(vis, inpmode='table', inpfile='', tablerows=[''], reason='any', useapplied=False, tbuff=0.0, ants='', action='apply', flagbackup=True, clearall=False, rowlist=[''], plotfile='', savepars=False, outfile='', overwrite=True):
    r"""
Flagging task based on batches of flag-commands

Parameters
   - vis_ (string) - Name of MS file or calibration table to flag
   - inpmode_ (string='table') - Input mode for flag commands(table/list/xml)

      .. raw:: html

         <details><summary><i> inpmode = table </i></summary>

      - inpfile_ ({string, stringArray}='') - Source of flag commands
      - tablerows_ (intArray=['']) - Rows of inpfile to read
      - reason_ ({string, stringArray}='any') - Select by REASON types
      - useapplied_ (bool=False) - Select commands whose rows have APPLIED column set to True

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> inpmode = list </i></summary>

      - inpfile_ ({string, stringArray}='') - Source of flag commands
      - reason_ ({string, stringArray}='any') - Select by REASON types

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> inpmode = xml </i></summary>

      - tbuff_ (double=0.0) - Time buffer (sec) to pad flags
      - ants_ (string='') - Allowed flag antenna names to select by
      - reason_ ({string, stringArray}='any') - Select by REASON types

      .. raw:: html

         </details>
   - action_ (string='apply') - Action to perform in MS and/or in inpfile (apply/unapply/list/plot/clear/extract)

      .. raw:: html

         <details><summary><i> action = apply </i></summary>

      - flagbackup_ (bool=True) - Automatically backup the FLAG column before execution

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> action = unapply </i></summary>

      - flagbackup_ (bool=True) - Automatically backup the FLAG column before execution

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> action = plot </i></summary>

      - plotfile_ (string='') - Name of output file to save plot

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> action = clear </i></summary>

      - clearall_ (bool=False) - Delete all rows from FLAG_CMD
      - rowlist_ (intArray=['']) - FLAG_CMD rows to clear

      .. raw:: html

         </details>
   - savepars_ (bool=False) - Save flag commands to the MS or file

      .. raw:: html

         <details><summary><i> savepars = True </i></summary>

      - outfile_ (string='') - Name of output file to save commands
      - overwrite_ (bool=True) - Overwrite an existing file to save the flag commands

      .. raw:: html

         </details>


Description
   The **flagcmd** task will flag the visibility data or the
   calibration table based onseveral batch-operations using flag
   commands. There is an extensive and detailed description of this
   task on the `Data Examination and Editing
   chapter <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing>`__.

   Flag commands follow the mode and parameter names from the
   **flagdata** task. Please refer tothe **flagdata** task for a
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




Details
   Explanation of each parameter

.. _vis:

   .. rubric:: vis

   | Name of input visibility file or calibration table.
   |                      default: '' (none) 
   | 
   |                         example: vis='uid___A002_X2a5c2f_X54.ms'

.. _inpmode:

   .. rubric:: inpmode

   | Input mode for flag commands(table/list/xml)
   |                      options: 'table','list','xml'
   |                      default: 'table' (the input commands from
   |                      FLAG_CMD table of the MS)
   | 
   |                      inpmode='xml' inputs online flags from Flag.xml
   |                      file in the MS. This mode has become largely
   |                      obsolete with the deprecation of the importevla
   |                      task (see the flagcmd task pages in CASA Docs for
   |                      more information). This mode will not work for
   |                      ALMA MS or cal tables.
   | 
   |                      NOTE: You can only apply the flags from a list or
   |                      xml; you will not be able to unapply
   |                      them. Transfer the flag commands to the FLAG_CMD
   |                      table if you want to unapply the flags (see
   |                      'inpfile' description below).

.. _inpfile:

   .. rubric:: inpfile

   | Source of flag commands. Subparameter of
   | inpmode='table/list'.
   |                      Path to MS containing FLAG_CMD (table), or name
   |                      of an ASCII file, list of files or a list of
   |                      Python strings to apply to MS or cal table
   |                      (list). 
   |                      options: [] with flag commands or [] with
   |                      filenames or '' with a filename. (String values
   |                      must contain quotes around them or the parser
   |                      will not work.)
   |                      default: '' (read from FLAG_CMD table in the MS
   |                      specified via 'vis')
   | 
   |                      Main use is to read flags from internal FLAG_CMD,
   |                      but one use case is to read the flag commands
   |                      from an MS given in inpfile and apply them to
   |                      another MS or cal table given in vis.

.. _tablerows:

   .. rubric:: tablerows

   | List of rows of the FLAG_CMD table to read. Subparameter
   | of inpmode='table/list'.
   |                      default: [] (read all rows)
   | 
   |                         example: [0,1,2,10]
   | 
   |                      NOTE: currently only takes integer lists, not
   |                      parseable strings with ranges.  Use the Python
   |                      range function to generate ranges, e.g. tablerows
   |                      = range(0,30) + range(50,55) instead of
   |                      '0~29,50~54' for now.

.. _reason:

   .. rubric:: reason

   | Select flag commands based on REASON(s). Subparameter of
   | inpmode.
   |                      default: 'any' (all flags regardless of reason)
   | 
   |                         Examples: 
   |                         reason='FOCUS_ERROR'
   |                         reason=['FOCUS_ERROR','SUBREFLECTOR_ERROR']
   | 
   |                      If inpfile is a list of files, the reasons given
   |                      in this parameter will apply to all the files.
   | 
   |                      NOTE: what is within the string is literally
   |                      matched, e.g. reason='' matches only blank
   |                      reasons, and reason
   |                      ='FOCUS_ERROR,SUBREFLECTOR_ERROR' matches this
   |                      compound reason string only

.. _useapplied:

   .. rubric:: useapplied

   | Select commands whose rows have APPLIED column set to
   | True. Subparameter of inpmode='table'.
   |                      options: True,False
   |                      default: False   
   | 
   |                      If useapplied=True it will read in both applied
   |                      and unapplied flags.
   | 
   |                      IMPORTANT: The APPLIED column is set to True
   |                      after a flag command is applied to the MS. In
   |                      order to re-apply the same flag command, this
   |                      parameter should be set to True.

.. _tbuff:

   .. rubric:: tbuff

   | Time buffer (sec) to pad flags. Subparameter of
   | inpmode='xml'.
   |                      default: 0.0

.. _ants:

   .. rubric:: ants

   | Allowed flag antenna names to select by. Subparameter of
   | inpmode='xml'.

.. _action:

   .. rubric:: action

   | Action to perform in MS and/or in inpfile
   |                      options: apply/unapply/list/plot/clear/extract
   |                      default: 'apply'
   |                    
   |                         Examples:
   |                         -- action='apply': This operation will apply
   |                         the commands chosen by inpmode. If
   |                         inpmode='table' and inpfile='' then the
   |                         APPLIED column in FLAG_CMD will be set to
   |                         True.
   |                         -- action='unapply': unapply flags in MS. (Not
   |                         available for cal tables). This operation will
   |                         unapply the commands chosen by inpmode='table'
   |                         ONLY. After unapplying the commands, the task
   |                         will update the APPLIED column to False.
   |                         -- action='list': list and/or save flag
   |                         commands. This operation will list the
   |                         commands chosen by inpmode on the screen and
   |                         save them to the MS or to a file without
   |                         applying. It will save the commands to outfile
   |                         if the parameter savepars is set to True. If
   |                         outfile is None, it will save the commands to
   |                         the MS given in 'vis'.
   |                         -- action='plot': plot flags (ant
   |                         vs. time). (Not available for cal
   |                         tables). This operation will plot the flags
   |                         chosen by inpmode to a matplotlib gui or to a
   |                         file.  These will be sorted by antenna
   |                         vs. time.  Most useful for showing the online
   |                         flags.
   |                         -- action='clear': clear flags from FLAG_CMD
   |                         in the MS. (Not available for cal tables) This
   |                         operation will delete the selected flag rows
   |                         from the internal FLAG_CMD table of the MS.
   |                         -- action='extract': extract internal flag
   |                         dictionary. (Not available for cal tables)
   |                         This option will return the internal flagging
   |                         dictionary to python. There is no extant
   |                         description of the format of this dictionary,
   |                         as it is an internal device used by the
   |                         flagcmd task. This action is provided for the
   |                         convenience of advanced users.
   | 
   |                     WARNING: choosing this action='clear' will
   |                     disregard anything you set in inpmode and will
   |                     always work on the FLAG_CMD table in vis. This can
   |                     be used to totally delete rows from the FLAG_CMD
   |                     table, when setting clearall=True.

.. _flagbackup:

   .. rubric:: flagbackup

   | Automatically backup the FLAG column before
   | execution. Subparameter of action='apply/unapply'.
   |                      options: True,False
   |                      default: True

.. _clearall:

   .. rubric:: clearall

   | Delete all rows from FLAG_CMD. Subparameter of
   | action='clear'.
   |                      default: False (will not clear)

.. _rowlist:

   .. rubric:: rowlist

   | FLAG_CMD rows to clear. Subparameter of action='clear'.
   |                      default: [] (all flags in table)
   |                
   |                         example: [0,1,2,10]
   | 
   |                      WARNING: this can be dangerous, and you must set
   |                      clearall=True  to use this!!! This will delete
   |                      the specified rows from the internal FLAG_CMD
   |                      table for vis regardless of what mode is set to
   |                      (useful for when you import from xml or file),
   |                      and decide to redo it). This action will NOT
   |                      unapply the commands.
   | 
   |                      NOTE: currently only takes integer lists, not
   |                      parseable strings with ranges.  Use the Python
   |                      range function to generate ranges, e.g. rowlist =
   |                      range(0,30) + range(50,55) instead of
   |                      '0~29,50~54' for now.

.. _plotfile:

   .. rubric:: plotfile

   | Name of output file to save plot
   |                      default: '' (plot to matplotlib window)
   | 
   |                      WARNING: will only reliably plot individual flags
   |                      per antenna and timerange (e.g. direct from xml)

.. _savepars:

   .. rubric:: savepars

   | Save the flag commands to the FLAG_CMD table of the MS or
   | to an output text file.
   |                      options: True/False     
   |                      default: False

.. _outfile:

   .. rubric:: outfile

   | Name of output file to save commands. Subparameter of
   | savepars=True.
   |                      default: ' '; it will save the commands in the
   |                      FLAG_CMD table of the MS.
   | 
   |                         example: outfile='flags.txt' will save the
   |                         parameters in a text file.

.. _overwrite:

   .. rubric:: overwrite

   | Overwrite an existing file given in 'outfile' to save the
   | flag commands. Subparameter of savepars=True.
   |                      options: True/False
   |                      default: True; it will remove the existing file
   |                      given in 'outfile' and save the current flag
   |                      commands to a new file with the same name. When
   |                      set to False, the task will exit with an error
   |                      message if the file exist.


    """
    pass
