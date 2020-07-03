.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Flag using flagcmd
==================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Flag the visibility data set or calibration table based on a
   specified list of flagging commands

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. container:: info-box

         Info: We recommend using task flagdata as the preferable and
         safer way for flagging based on the visitibilites inspection
         and for many other capabilities. The option to import XML files
         with online flag in flagcmd has largely become obsolete with
         the deprecation of importevla, because the recommended
         importasdm task cannot copy the actual XML tables from the
         original SDM to the newly created MS (it can only apply the
         online flags directly, or write them into ascii tables).

      The task flagcmdwill flag the visibility data set or calibration
      table based on a specified set of flagging commands using a
      flagging syntax. These commands can be input from
      the\ *FLAG_CMD*\ table within the MS,from an ascii file, or from
      input python strings. Input can also be from an XML table within a
      VLA SDM, but given that importasdm does not copy XML files (and
      importevla is deprecated), the Flag.xml, Antenna.xml and
      SpectralWindow.xml tables must first be copied manually into the
      top-level MS directory for use by flagcmd (not the recommended
      approach). Facilities for manipulation, listing, or plotting of
      these flags are also provided.

      When doing any flagging with flagcmd it is wise to use the
      flagbackup=True parameter to save the current flags into a
      .flagversions file. See flagmanager for more details about this.

      .. container:: alert-box

         Alert: The FLAG_CMD sub-table is meant only for meta-data
         selections such as online flags. Using it to save other
         parameters (from modes such as clip, quack, shadow, etc)
         is possible but carries a risk that in future releases these
         parameters maybe renamed or changed their default values. There
         will be no automaticway to rename any parameter that changes in
         the future.

      .. container:: alert-box

         Alert: There is no way to guarantee that a command from the
         COMMAND column has been applied or not to the MS, even if the
         APPLIED column is set to True. If you use other ways to flag
         such as interactive flagging in plotms, the FLAG_CMD will not
         be updated! Use at your own risk!

      The inputs to flagcmdare:

      .. container:: casa-input-box

         | #  flagcmd :: Flagging task based on batches of flag-commands
         | vis                 =      ''          #  Name of MS file or
           calibration table to flag
         | inpmode             =      'table'     #  Input mode for flag
           commands(table/list/xml)
         | inpfile             =      ''          #  Source of flag
           commands
         | tablerows           =      []          #  Rows of inpfile to
           read
         | reason              =      'any'       #  Select by REASON
           types
         | useapplied          =      False       #  Select commands
           whose rows
         |                                        #  have APPLIED column
           set to True
         | action              =      'apply'     #  Action to perform
           in MS and/or in inpfile
         |                                        # 
           (apply/unapply/list/plot/clear/extract)
         | flagbackup          =      True        #  Automatically
           backup the
         |                                        #  FLAG column before
           execution
         | savepars            =      False       #  Save flag commands
           to the MS or to a file

       

      The default input mode is inpmode=’table’ which directs the task
      to input flag commands from the FLAG_CMD internal MS table. Other
      options include list and xml, explained below.

      The default operation mode isaction=’apply’directing the task to
      apply relevant flagging commands to the MS data main table.
      Otheroptions include 'unapply', 'list', 'plot', 'clear', and
      'extract', explained below.

      Seethe Flagging Command Syntax section below for more detail.

      .. container:: alert-box

         Alert: It is possible to flag calibration tables using flagcmd,
         although we recommend using the flagdatatask for this in most
         cases.

      When using flagcmdto flag calibration tables, only
      theapplyandlistactions are supported. Because calibration tables
      do not have a FLAG_CMD sub-table, the defaultinpmode=’table’can
      only be used if an MS is given in theinpfileparameter so that
      flags from the MS are applied to the calibration table directly.
      Otherwise, the flag commands must be given usinginpmode=’list’,
      either from a file or from a list of strings.

       

      --------------

      .. rubric:: Input modesinpmode:
         :name: input-modes-inpmode

      Theinpmodeparameter selects options for the input mode for the
      flagging commands.

      Availableinpmodeoptions are:

      -  ’table’— input from MS table
      -  ’list’— input from ASCII file or from a list of strings
      -  ’xml’— input from XML table (largely obsolete with the
         deprecation of importevla in CASA 5.4)

      .. rubric::  
         :name: section
         :class: subsubsection

      .. rubric:: Input mode inpmode=\ *’table’*
         :name: sec194
         :class: subsubsection

       The default input mode isinpmode=’table’which directs the task to
      input flag commands from a\ *FLAG_CMD*\ MS table. This has the
      sub-parameters:

      .. container:: casa-input-box

         | inpmode        =      'table'      #  Input mode for flag
           commands(table/list/xml)
         | inpfile        =      ''           #  Source of flag commands
         | tablerows      =      []           #  Rows of inpfile to read
         | reason         =      'any'        #  Select by REASON types
         | useapplied     =      False        #  Select commands whose
           rows
         |                                    #  have APPLIED column set
           to
         |                                    #   True

      Ifinpfile = ''then it will look for the\ *FLAG_CMD*\ table in the
      MS given byvis. You can use this sub-parameter to tell the task to
      read the FLAG_CMD table from another MS and apply then to the MS
      given in vis.

      Thetablerowssub-parameter is a simple Python list of the row
      numbers of the table to consider in processing flags. The default
      is all rows. Currently it only takes fully-enumerated integer
      lists. Use the Python range function to generate ranges,

      .. container:: terminal-box

         tablerows = range(0,30) + range(50,55)

         #Do not use strings such as ’0~29,50~54’

      Theuseappliedsub-parameter toggles whether only flag commands
      marked as not having been applied are considered (the default), or
      to allow (re)processing using all commands.

      Thereasonsub-parameter selects the\ *reason*\ type to process. The
      default’any’means all commands.

      .. container:: info-box

         Info: what is within the string is literally matched, e.g.
         reason=’’ matches only blank reasons, and reason =
         ’FOCUS_ERROR,SUBREFLECTOR_ERROR’ matches this compound reason
         string only. To flag by either of these reasons alone, run
         flagcmd twice, once with reason='FOCUS_ERROR', and then with
         the other reason.

      One use case is to read the flag commands from the FLAG_CMD of an
      MS and apply them to a calibration table given in the
      parametervis. Example:

      .. container:: casa-input-box

         flagcmd(vis='cal-X54.B1',
         inpmode='table',inpfile='uid___A002_X2a5c2f_X54.ms',
         action='apply')

      .. rubric:: Input mode inpmode=\ *’list’*
         :name: input-mode-inpmodelist
         :class: subsubsection

      See flagdata help for syntax.

      This mode allows one to give a list of strings with flagging
      commands, the name of a file or a list of filenames that contains
      these commands equivalent to themode=’list’inflagdata. E.g. a
      file\ *flags.txt*\ that contains

      .. container:: casa-input-box

         | scan='1~3' mode='manual'
         | mode='clip' clipminmax=[0,2] correlation='ABS_XX'
           clipoutside=False
         | spw='9' mode='tfcrop' correlation='ABS_YY' ntime=51.0
         | mode='extend' extendpols=True

      can be used via

      .. container:: casa-input-box

         flagcmd(vis='some.ms',inpmode='list',inpfile='flags.txt')

      A list of input files can also be given:

      .. container:: casa-input-box

         flagcmd(vis='some.ms',inpmode='list',inpfile=['flags.txt,'userflags.txt'])

       

      Alternatively, the individual flagging commands can be directly
      provided in the call itself such as:

      .. container:: casa-input-box

         | inpfile=["scan='1~3' mode='manual'",
         |          "mode='clip' clipminmax=[0,2] correlation='ABS_XX'
           clipoutside=False",
         |          "spw='9' mode='tfcrop' correlation='ABS_YY'
           ntime=51.0",
         |          "mode='extend' extendpols=True"]

      .. rubric::  
         :name: section-1

      .. rubric:: Input mode inpmode=’xml’
         :name: input-mode-inpmodexml

      .. container:: alert-box

         Alert: With the deprecation of importevla, XML files can no
         longer be imported directly from the original SDM into the
         newly created MS, but only by manually copying the Flag.xml,
         Antenna.xml and SpectralWindow.xml tables into the top-level MS
         directory (not the recommended approach). Also, the XML mode is
         not available for cal tables, therefore it will not work for
         ALMA MSs. However, task importasdm with process_flags=True will
         copy the flags from the XML files directly to the FLAG_CMD
         sub-table, see importasdm help for options. This is the
         recommend way of dealing with the online flags.

      The input modeinpmode=’xml’tells the task to input flag commands
      from XML SDM files, which contain the online flags. When set this
      opens the sub-parameters:

      .. container:: casa-input-box

         | inpmode        =      'xml'        #  Input mode for flag
           commands(table/list/xml)
         | tbuff          =      0.0          #  Time buffer (sec) to
           pad flags
         | ants           =      ''           #  Allowed flag antenna
           names to select by
         | reason         =      'any'        #  Select by REASON types

      This mode will look for files calledFlag.xml, Antenna.xmland
      optionallySpectralWindow.xmlinside the MS directory specified
      undervis.

      .. container:: info-box

         Info: You can only apply the flags from an XML file. It is not
         possible to unapply them. For that, transfer the flags to the
         FLAG_CMD table using action='list', then unapply them.

       

      Thetbuffsub-parameter sets a padding buffer (in seconds) to the
      begin and end times of the online flags in the XML file. The
      online flag time buffertbuffis specified in seconds, but in fact
      should be keyed to the intrinsic online integration time to allow
      for events (like slewing) that occur within an integration period.
      This is particularly true for JVLA data, where atbuffvalue
      of0.5×to1.5×the integration time is needed. For example, if data
      were taken with 1-second integrations, then at
      leasttbuff=0.5should be used, likewisetbuff=5for 10-second
      integrations. 

      .. container:: info-box

         Info: For JVLA data you should use 1.5× (e.g. tbuff=15 for
         10-second integrations) for data taken in early 2011 or before
         due to a timing error. We do not yet know what ALMA data will
         need for padding (if any).

      Theantssub-parameter selects the antennas from which online flags
      will be selected (default is all antennas). For
      example,ants=’ea01’is a valid choice for JVLA data.

      Thereasonsub-parameter selects by theREASONfield in
      theFlag.xmlfile. The default’any’means all commands. Note
      thatreason=”would only select flags who have a blankREASONfield
      entry.

      .. rubric::  
         :name: section-2
         :class: subsection

      --------------

      .. rubric:: Operation typesaction
         :name: sec197
         :class: subsection

       Theactionselects options for operating on the selected flags and
      possibly the data.

      Availableactionoptions are:

      -  ’apply’— apply flag commands to data
      -  ’unapply’— unapply flags in data
      -  ’list’— list and/or save flag commands
      -  ’plot’— plot flag commands
      -  ’clear’— clear rows fromFLAG_CMDtable
      -  ’extract’— extract internal flag dictionary

      .. rubric:: Apply flagsaction=’apply’
         :name: sec198
         :class: subsubsection

      The default operation mode isaction=’apply’directing the task to
      apply relevant flagging commands to the vis data main table.

      .. container:: casa-input-box

         | action         =       'apply'     #  Action to perform in MS
           and/or in inpfile
         |                                    #  
           (apply/unapply/list/plot/clear/extract)
         | flagbackup     =       True        #  Automatically backup
           the
         |                                         # FLAG column before
           execution

      Theflagbackupparameter toggles whether a new copy of the
      MSFLAGcolumn is written to the.flagversionsbackup directory for
      that MS before the requested flagging operation.

      .. rubric::  
         :name: section-3
         :class: subsubsection

      .. rubric:: Unapply flagsaction=’unapply’
         :name: sec199
         :class: subsubsection

      Theunapplyoption allows unflagging of data based on the selected
      flag commands. This choice opens the sub-parameters:

      .. container:: casa-input-box

         | action = 'unapply' # Action to perform in MS and/or in
           inpfile
         | # (apply/unapply/list/plot/clear/extract)
         | flagbackup = True # Automatically backup the
         | # FLAG column before execution

      As inaction=’apply’, it is possible to make a backup to
      the\*.flagversionsfile by usingflagbackup=True.

       

      .. rubric:: List and save flagsaction=’list’
         :name: sec200
         :class: subsubsection

      The’list’option will give a listing of the flagging commands. This
      choice opens the sub-parameters:

      .. container:: casa-input-box

         | action = 'list' # Action to perform in MS and/or in inpfile
         | # (apply/unapply/list/plot/clear/extract)
         | savepars = True # Save flag commands to the MS or to a file
         | outfile = '' # Name of output file to save commands
         | overwrite = True # Overwrite an existing file to save the
           flag commands

      This action lists the commands on the screen without applying
      them. One can save the flagging script to an file specified in
      theoutfileparameter whensavepars=True. Ifoutfileis empty, it will
      save the commands to a new row in the MS FLAG_CMD table given
      invis.

      The format of the listing output depends on the source of the
      flagging commands. A set of flagging commands specified
      throughinpmode=’list’will be listed directly. The flagging
      commands extracted throughinpmode=’table’will reflect the columns
      in the table:'Row', 'Timerange', 'Reason', 'Type', 'Applied',
      'Lev', 'Sev', 'Command' while commands frominpmode=’xml’will be
      shown with the SDM XML table fields:'Key', 'FlagID', 'Antenna',
      'Reason', 'Timerange'

      .. rubric:: Plot flagsaction=’plot’
         :name: sec201
         :class: subsubsection

      The’plot’option will produce a graphical plot of flags of time
      versus antenna. This choice opens the sub-parameters:

      .. container:: casa-input-box

         | action = 'plot' # Action to perform in MS and/or in inpfile
         | # (apply/unapply/list/plot/clear/extract)
         | plotfile = '' # Name of output file to save plot

      This is only useful for MS. flagcmd is most often used to plot the
      VLA or ALMA flags generated online using impmode='table' or 'xml'
      and provided in a FLAG_CMD or Flags.xml table. Using these tables,
      only the standard on-line REASONs are recognised. These include
      'FOCUS','SUBREFLECTOR', 'OFF SOURCE', 'NOT IN SUBARRAY' for the
      VLA and 'Calibration_device_(ACD)_is_not_in_the_correct_position',
      'Mount_is_off_source', 'FrontEnd_LO_Amps_not_optimized'
      'Power_levels_are_being_optimized.', 'The_WCA_is_not_locked.' for
      ALMA

      If theplotfilesub-parameter is non-blank, then a plotfile will be
      made with that name instead of appearing in a matplotlib plotter
      window on the users workstation. There are additional parameters
      that control the shape of the output file, such as dimensions, and
      resolution.

      .. container:: alert-box

         | Alert: The plotted enumerations are currently only those
           known to be allowed for JVLA online flags as of 15 April
           2011, and include:
         | 'FOCUS', 'SUBREFLECTOR', 'OFF SOURCE', 'NOT IN SUBARRAY' with
           all others being plotted as ’Other\ ’.

      .. rubric:: Clear flagsaction=’clear’
         :name: sec202
         :class: subsubsection

      This is only useful for MS, using inpmode="table".
      The’clear’action will delete selected rows from theFLAG_CMDMS
      table. This choice opens the sub-parameters:

      .. container:: casa-input-box

         | action = 'clear' # Action to perform in MS and/or in inpfile
         | # (apply/unapply/list/plot/clear/extract)
         | clearall = False # Delete all rows from FLAG_CMD
         | rowlist = [] # FLAG_CMD rows to clearThis box is intended for
           CASA Inputs. Insert your text here.

      Therowlistsub-parameter is a simple Python list of the row numbers
      of the table to consider in processing flags. The default is a
      blank list which indicates the desire to clear all rows. Currently
      it only takes fully-enumerated integer lists. Use the Python range
      function to generate ranges,

      .. container:: terminal-box

         | tablerows = range(0,30) + range(50,55)
         | #Do not use strings such as ’0~29,50~54’

      In either case, ifclearall=Falsethen nothing will happen by
      default as a safeguard. Ifclearall=True, then a blank list will
      direct the deletion of the selected rows from the table.

      .. container:: alert-box

         Alert: Use this option with care. You can easily mess up the
         FLAG_CMD table.

      .. rubric:: Extract Flag Commandsaction=’extract’
         :name: sec203
         :class: subsubsection

      This will return the requested flags (depending on inpmode) as a
      Python dictionary.

      .. container:: casa-input-box

         | action = 'extract' # Action to perform in MS and/or in
           inpfile
         | # (apply/unapply/list/plot/clear/extract)

      The dictionary can be saved to a variable such as shown below. If
      a variable is not set, only the first 1000 flags will be printed
      to the terminal:

      .. container:: casa-input-box

         myflagd = flagcmd(vis=msfile,useapplied=True,action='extract')

      An example of the dictionary returned by action='extract' is given
      below:

      .. container:: casa-output-box

         | {0: {'antenna': 'PM04&&*',
         |   'applied': False,
         |   'command': 'antenna=PM04&&\*
           timerange=2013/04/28/04:35:58.217~2013/04/28/04:35:58.468 ',
         |   'id': '662',
         |   'interval': 0.0,
         |   'level': 0,
         |   'mode': '',
         |   'reason': 'ACD_motors_are_not_in_position.',
         |   'severity': 0,
         |   'time': 0.0,
         |   'timerange':
           '2013/04/28/04:35:58.217~2013/04/28/04:35:58.468',
         |   'type': ''},
         |  1: {'antenna': 'CM03&&*',
         |   'applied': False,
         |   'command': 'antenna=CM03&&\*
           timerange=2013/04/28/04:35:58.196~2013/04/28/04:35:58.503 ',
         |   'id': '663',
         |   'interval': 0.0,
         |   'level': 0,
         |   'mode': '',
         |   'reason': 'ACD_motors_are_not_in_position.',
         |   'severity': 0,
         |   'time': 0.0,
         |   'timerange':
           '2013/04/28/04:35:58.196~2013/04/28/04:35:58.503',
         |   'type': ''}}

      .. rubric::  
         :name: section-4
         :class: subsection

      --------------

      .. rubric:: Flagging command syntax
         :name: sec204
         :class: subsection

      A flagging command syntax has been devised to populate
      theCOMMANDcolumn of the\ *FLAG_CMD*\ table and to direct the
      operation of the flagcmdtask.

      The syntax is the same used in flagdata\ ,so please check"help
      flagdata"  for more updated info.

      Commands are a string (which may contain internal "strings")
      consisting ofKEY=VALUEpairs separated by whitespace (see examples
      below).

      .. container:: alert-box

         Alert: There should be no whitespace between KEY=VALUE or
         within each KEY or VALUE, since the simple parser first breaks
         command lines on whitespace, then on "=".

      The key is the name of a parameter and the value is the value of
      that parameter. The parameter data types enforced in flagdata are
      the same used in these flag commands. As an example, the parameter
      clipminmax accepts only a list of double values in flagdata and
      should have the same type when given in a flag command list, e.g.
      mode='clip' clipminmax=[0.1,10.2]

      Each key should only appear once on a given command line/string

      There is an implicit"mode"for each command, with the default
      being’manual’if not given.

      Comment lines can start with ’#’ and will be ignored.

      1. .. rubric:: Data selection parameters (used by all flagging
            modes)
            :name: data-selection-parameters-used-by-all-flagging-modes

         .. container:: casa-input-box

            | antenna=''
            | spw=''
            | correlation=''
            | field=''
            | scan=''
            | feed=''
            | array=''
            | timerange=''
            | uvrange=''
            | intent=''
            | observation=''

         .. container:: info-box

            Info: a command consisting only of meta-data selection
            key-value pairs is a basic "manual" operation, i.e. flag the
            data meeting the selection

      2. .. rubric:: Modes with default values for relevant parameters
            (for further details, refer to the task flagdata)
            :name: modes-with-default-values-for-relevant-parameters-for-further-details-refer-to-the-task-flagdata

         a. .. rubric:: Modemanual
               :name: mode-manual

            .. container:: casa-input-box

               autocorr=False

         b. .. rubric:: Modeclip
               :name: mode-clip

            .. container:: casa-input-box

               | datacolumn='DATA'
               | clipminmax=[]
               | clipoutside=True
               | channelavg=False
               | clipzeros=False
               | timeavg=False
               | timebin=''

         c. .. rubric:: Modeshadow
               :name: mode-shadow

            .. container:: casa-input-box

               | tolerance=0.0
               | addantenna=''

         d. .. rubric:: Modequack
               :name: mode-quack

            .. container:: casa-input-box

               | quackinterval=0.0
               | quackmode='beg'
               | quackincrement=False

         e. .. rubric:: Modeelevation
               :name: mode-elevation

            .. container:: casa-input-box

               | lowerlimit=0.0
               | upperlimit=90.0

         f. .. rubric:: Modetfcrop
               :name: mode-tfcrop

            .. container:: casa-input-box

               | ntime='scan'
               | combinescans=False
               | datacolumn='DATA'
               | timecutoff=4.0
               | freqcutoff=3.0
               | timefit='line'
               | freqfit='poly'
               | maxnpieces=7
               | flagdimension='freqtime'
               | usewindowstats='none'
               | halfwin=1
               | extendflags=True
               | channelavg=False
               | chanbin=1
               | timeavg=False
               | timebin='0s'

         g. .. rubric:: Modeextend
               :name: mode-extend

            .. container:: casa-input-box

               | ntime='scan'
               | combinescans=False
               | extendpols=True
               | growtime=50.0
               | growfreq=50.0
               | growaround=False
               | flagneartime=False
               | flagnearfreq=False

         h. .. rubric:: Moderflag
               :name: mode-rflag

            .. container:: casa-input-box

               | ntime='scan'
               | combinescans=False
               | datacolumn='DATA'
               | winsize=3
               | timedev=''
               | freqdev=''
               | timedevscale=5.0
               | freqdevscale=5.0
               | spectralmax=1000000.0
               | spectralmin=0.0
               | extendflags=True
               | channelavg=False
               | chanbin=1
               | timeavg=False
               | timebin='0s'

         i. .. rubric:: Modeantint
               :name: mode-antint

            .. container:: casa-input-box

               | minchanfrac=0.6
               | verbose=False

         j. .. rubric:: Modeunflag
               :name: mode-unflag

            .. container::

               This mode does not have any sub-parameters.

      3. .. rubric:: Typical example of a list with flag commands
            :name: typical-example-of-a-list-with-flag-commands

         .. container:: casa-input-box

            | spw='0,1'
              antenna='ea1,ea10'
              autocorr=True
            | mode='clip'
              clipzeros=True
              datacolumn='DATA'
            | mode='summary'
              name='Initial_flags'

      4. .. rubric:: Basic elaboration options for online and interface
            use
            :name: basic-elaboration-options-for-online-and-interface-use

         .. container:: casa-input-box

            | id='' # flag ID tag (not necessary)
            | reason='' # reason string for flag
            | flagtime='' # a timestamp for when this flag was generated
              (for
            | user history use)

         .. container:: info-box

            | Info: there is no flagtime column in FLAG_CMD at this
              time, but we will propose to add this as an optional
              column
            | Info: These are currently ignored and not used

      5. .. rubric:: Extended elaboration options for online and
            interface use Note: these areFLAG_CMDcolumns, but their use
            is not clear but included here for compatibility and future
            expansion
            :name: extended-elaboration-options-for-online-and-interface-use-note-these-are-flag_cmd-columns-but-their-use-is-not-clear-but-included-here-for-compatibility-and-future-expansion

         .. container:: casa-input-box

            | level=N # flagging "level" for flags with same reason
            | severity=N # Severity code for the flag, on a scale of
              0-10 in order
            | of increasing severity; user specific

.. container:: section
   :name: viewlet-below-content-body
