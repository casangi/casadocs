.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Visibility Data Selection
=========================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   How to select visibility data

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Once in MS form, subsets of the data can be operated on using the
      tasks and tools. In CASA, there are three common data selection
      parameters used in the various tasks: field\ , \ spw\ ,
      and \ selectdata. In addition, the selectdata\  parameter, if set
      to \ True, will open up a number of other sub-parameters for
      selection. The selection operation is unified across all the
      tasks. The available \ *selectdata*\  parameters may not be the
      same in all tasks. But if present, the same parameters mean the
      same thing and behave in the same manner when used in any task.

      For example:

      .. container:: casa-input-box

         field = ''         # field names or index of calibrators
         ''==>all
         spw = ''           # spectral window:channels: ''==>all
         selectdata = False # Other data selection parameters

      versus

      .. container:: casa-input-box

         field = ''         # field names or index of calibrators
         ''==>all
         spw = ''           # spectral window:channels: ''==>all
         selectdata = True  # Other data selection parameters
         timerange = ''     # time range: ''==>all
         uvrange = ''       # uv range''=all
         antenna = ''       # antenna/baselines: ''==>all
         scan = ''          # scan numbers
         msselect = ''      # Optional data selection (Specialized. but
         see help)

      The following are the general syntax rules and descriptions of the
      individual selection parameters of particular interest for the
      tasks.

       

      .. container:: info-box

         Info: The full documentation of the MeasurementSet data
         selection syntax can be found on the\ `CASAcore
         documentation <https://casacore.github.io/casacore-notes/>`__\  page,
         document 263 "\ `Measurement Selection
         Syntax <https://casacore.github.io/casacore-notes/263.html>`__\ "
         (see also\ `CASA Memo
         1 <https://casa.nrao.edu/casadocs-devel/stable/memo-series/casa-memos/casa_memo3_msselection_bhatnagar.pdf>`__\ ).
         Links to relevant subsections are provided in the subsections
         below.

      .. rubric::  
         :name: section
         :class: subsection

      .. rubric:: General selection syntax
         :name: sec121
         :class: subsection

      Most of the selections are effected through the use of selection
      strings. This sub-section describes the general rules used in
      constructing and parsing these strings. Note that some selections
      are done through the use of numbers or lists. There are also
      parameter-specific rules that are described under each parameter.

      All lists of basic selection specification-units are comma
      separated lists and can be of any length. White-spaces before and
      after the commas (e.g. \ ’3C286, 3C48, 3C84’\ ) are ignored, while
      white-space within sub-strings is treated as part of the
      sub-string (e.g.\  \ ’3C286, VIRGO A, 3C84’\ ). In some cases,
      spaces need to be quoted, e.g. "’spw 1’" (note the double quote
      around the single quotes).

      All integers can be of any length (in terms of characters)
      composed of the characters 0–9. Floating point numbers can be in
      the standard format (\ DIGIT.DIGIT\ , \ DIGIT.\ , or \ .DIGIT\ )
      or in the mantissa-exponent format (e.g. \ 1.4e9\ ). Places where
      only integers make sense (e.g. IDs), if a floating point number is
      given, only the integer part is used (it is truncated).

      Range of numbers (integers or real numbers) can be given in the
      format 'N0~N1'. For integerranges, it is expanded into a list of
      integers starting from \ N0\  (inclusive) to \ N1\  (inclusive).
      For real numbers, it is used to select all values present for the
      appropriate parameter in the MeasurementSet
      between \ N0\  and \ N1\  (including the boundaries). Note that
      the \ ``'~'``\  (tilde) character is used rather than the more
      obvious ’\ -\ ’ in order to accommodate hyphens in strings and
      minus signs in numbers.

      Wherever appropriate, units can be specified. The units are used
      to convert the values given to the units used in the
      MeasurementSet. For ranges, the unit is specified only once (at
      the end) and applies to both the range boundaries.

       

      .. rubric:: String Matching
         :name: sec122
         :class: subsubsection

      String matching can be done in three ways. Any component of a
      comma separated list that cannot be parsed as a number, a number
      range, or a physical quantity is treated as a regular expression
      or a literal string. If the string does not contain the
      characters \ ’*’, ’{’, ’}’\  \ or \ ’?’, it is treated as a
      literal string and used for exact matching. If any of the above
      mentioned characters are part of the string, they are used as a
      regular expression. As a result, for most cases, the user does not
      need to supply any special delimiters for literal strings
      and/orregular expressions. For example:

      .. container:: casa-input-box

         field = '3'    # match field ID 3 and not select field named
         "3C286".

         | field = '3*'   # used as a pattern and matched against field
           names. If
         |                # names like "3C84", "3C286", "3020+2207" are
           found,
         |                # all will match. Field ID 3 will not be
           selected
         |                # (unless of course one of the above mentioned
           field
         |                # names also correspond to field ID 3!).

         field = '30*'  # will match only with "3020+2207" in above set.

      However if it is required that the string be matched exclusively
      as a regular expression, it can be supplied within a pair
      of ’/’\  as delimiters (e.g. \ ’/.+BAND.+/’\ ). A string enclosed
      within double quotes (\ ’"’\ ) is used exclusively for pattern
      matching (patterns are a simplified form of regular expressions -
      used in most UNIX commands for string matching). Patterns are
      internally converted to equivalent regular expressions before
      matching. See the Unix command "info regex", or
      visit \ http://www.regular-expressions.info\ , for details of
      regular expressions and patterns.

      Strings can include any character except the following:

      .. container:: terminal-box

         ',' ';' '"' '/' NEWLINE

      (since these are part of the selection syntax). Strings that do
      not contain any of the characters used to construct regular
      expressions or patterns are used for exact matches. Although it is
      highly discouraged to have name in the MS containing the above
      mentioned reserved characters, if one does choose to include the
      reserved characters as parts of names etc., those names can only
      be matched against quoted strings (since regular expression and
      patterns are a super-set of literal strings – i.e., a literal
      string is also a valid regular expression).

      This leaves \ ’"’, ’*’, ’{’, ’}’\  or \ ’?’\  \ as the list of
      printable character that cannot be part of a name (i.e., a name
      containing this character can never be matched in a MSSelection
      expression). These will be treated as pattern-matching even inside
      double double quotes (\ ’" "’\ ). There is currently no escape
      mechanism (e.g. via a backslash).

      Some examples of strings, regular expressions, and patterns:

      -  The string ’LBAND’\  \ will be used as a literal string for
         exact match. It will match only the exact string \ LBAND\ .
      -  The wildcarded string \ ’*BAND*’\  will be used as a string
         pattern for matching. This will match any string which has the
         sub-string \ BAND\  in it.
      -  The string \ ’"*BAND*"’\  will also be used as a string
         pattern, matching any string which has the
         sub-string \ BAND\  in it.
      -  The string \ ’/.+BAND.+/’\  will be used as a regular
         expression. This will also match any string which as the
         sub-string \ BAND\  in it. (the \ .+\  regex operator has the
         same meaning as the \ \*\  \ wildcard operator of patterns).

      .. rubric::  
         :name: section-1
         :class: subsection

      .. rubric:: The \ field\  Parameter
         :name: sec123
         :class: subsection

      The \ field\  parameter is a string that specifies which field
      names or ids will be processed in the task or tool. The field
      selection expression consists of comma separated list of field
      specifications inside the string.

      Field specifications can be literal field names, regular
      expressions or patterns (see above). Those fields for which the
      entry in the NAME column of the FIELD\  MS sub-table match the
      literal field name/regular expression/pattern are selected. If a
      field name/regular expression/pattern fails to match any field
      name, the given name/regular expression/pattern are matched
      against the field code. If still no field is selected, an
      exception is thrown.

      Field specifications can also be given by their integer IDs. IDs
      can be a single or a range of IDs. Field ID selection can also be
      done as a boolean expression. For a field specification of the
      form \ ’>ID’\ , all field IDs greater than ID are selected.
      Similarly for \ ’<ID’\  all field IDs less than the ID are
      selected.

      For example, if the MS has the following observations:

      .. container:: casa-output-box

         MS summary:
         ==========
         FIELDID SPWID NChan Pol NRows Source Name
         ---------------------------------------------------------------
         0 0 127 RR 10260 0530+135
         1 0 127 RR 779139 05582+16320
         2 0 127 RR 296190 05309+13319
         3 0 127 RR 58266 0319+415
         4 0 127 RR 32994 1331+305
         5 1 1 RR,RL,LL,RR 23166 KTIP

      one might select

      .. container:: casa-input-box

         field = '0~2,KTIP'  # FIELDID 0,1,2 and field name KTIP
         field = '0530+135' # field 0530+135
         field = '05*'          # fields
         0530+135,05582+16320,05309+13319 

      .. rubric::   
         :name: section-2
         :class: subsection

      .. container:: info-box

         `Field
         Selection <http://casacore.github.io/casacore-notes/263.html#x1-190004>`__
         - Expression for selection data along frequency axis (CASAcore
         docs)

       

      .. rubric:: The spw Parameter
         :name: the-spw-parameter

      The \ spw\  parameter is a string that indicates the specific
      spectral windows and the channels within them to be used in
      subsequent processing. Spectral window selection (\ ’SPWSEL’\ )
      can be given as a spectral window integer ID, a list of integer
      IDs, a spectral window name specified as a literal string (for
      exact match) or a regular expression or pattern.

      The specification can be via frequency ranges or by indexes. A
      range of frequencies are used to select all spectral windows which
      contain channels within the given range. Frequencies can be
      specified with an optional unit — the default unit being \ Hz\ .
      Other common choices for radio and mm/sub-mm data
      are \ kHz, MHz\ , and \ GHz\ . You will get the entire spectral
      windows, not just the channels in the specified range. You will
      need to do channel selection (see below) to do that.

      The spw can also be selected via comparison for integer IDs. For
      example, \ ’>ID’\  \ will select all spectral windows with ID
      greater than the specified value, while \ ’<ID’\  \ will select
      those with ID lesser than the specified value.

      Spectral window selection using strings follows the standard
      rules: 

      .. container:: casa-input-box

         spw = '1'                      # SPWID 1
         spw = '1,3,5'                # SPWID 1,3,5
         spw = '0~3'                  # SPWID 0,1,2,3
         spw = '0~3,5'               # SPWID 0,1,2,3 and 5
         spw = '<3,5'                 # SPWID 0,1,2,3 and 5
         spw = '*'                      # All spectral windows
         spw = '1412~1415MHz' #Spectral windows containing 1412-1415MHz.

      In some cases, the spectral windows may allow specification by
      name. For example, 

      .. container:: casa-input-box

         spw = '3mmUSB, 3mmLSB'      # choose by names (if
         available)might be meaningful for the dataset in question.

      Note that the order in which multiple spws are given may be
      important for other parameters. For example, the \ mode =
      ’channel’\  in \ clean\  uses the first \ spw\  as the origin for
      the channelization of the resulting image cube.

       

      .. rubric:: Channel selection inthe \ *spw*\  parameter
         :name: sec125
         :class: subsubsection

      Channel selection can be included in the spw string in the
      form \ ’SPWSEL:CHANSEL’\  where \ CHANSEL\  is the channel
      selector. In the end, the spectral selection within a given
      spectral window comes down to the selection of specific channels.
      We provide a number of shorthand selection options for this.
      These \ *CHANSEL*\  options include:

      -  Channel ranges: 'START~STOP'\ *  *
      -  Frequency ranges: 'FSTART~FSTOP' 
      -  Channel striding/stepping: 'START~STOP^STEP' or
         'FSTART~FSTOP^FSTEP'

      The most common selection is via channel ranges 'START~STOP' or
      frequency ranges 'FSTART~FSTOP':

      .. container:: casa-input-box

         | spw = '0:13~53'        # spw 0, channels 13-53, inclusive
         | spw = '0:1413~1414MHz' # spw 0, 1413-1414MHz section only

      All ranges are inclusive, with the channel given by, or containing
      the frequency given by, START\  and \ STOP\  plus all channels
      between included in the selection. You can also select the
      spectral window via frequency ranges 'FSTART~FSTOP', as described
      above: 

      .. container:: casa-input-box

         spw = '1413~1414MHz:1413~1414MHz' # channels falling within
         1413~1414MHz
         spw = '*:1413~1414MHz'                      # does the same
         thing

      You can also specify multiple spectral window or channel ranges,
      e.g. 

      .. container:: casa-input-box

         spw = '2:16, 3:32~34' # spw 2, channel 16 plus spw 3 channels
         32-34
         spw = '2:1~3;57~63'   # spw 2, channels 1-3 and 57-63
         spw = '1~3:10~20'     # spw 1-3, channels 10-20
         spw = '*:4~56'        # all spw, channels 4-56

      Note the use of the wildcard in the last example.

      A step can be also be included using '^STEP' \ as a postfix:

      .. container:: casa-input-box

         spw = '0:10~100^2'        # chans 10,12,14,...,100 of spw 0
         spw = ':^4'               # chans 0,4,8,... of all spw
         spw = ':100~150GHz^10GHz' # closest chans to 100,110,...,150GHz

      A step in frequency will pick the channel in which that frequency
      falls, or the nearest channel.

      .. rubric::  
         :name: section-3
         :class: subsection

      .. container:: info-box

         `Frequency
         Selection <http://casacore.github.io/casacore-notes/263.html#x1-230006>`__
         - Expression for selection along the frequency axis (CASAcore
         docs)

      .. rubric:: The selectdata Parameters
         :name: the-selectdata-parameters

      The \ selectdata\  parameter, if set to True (default), will
      expand the inputs to include a number of sub-parameters, given
      below and in the individual task descriptions (if different).
      If \ selectdata = False\ , then the sub-parameters are treated as
      blank for selection by the task.

      The common \ selectdata\  expanded sub-parameters are:

      .. rubric::  
         :name: section-4
         :class: subsubsection

      .. rubric:: The \ antenna\  Parameter
         :name: sec127
         :class: subsubsection

      The \ antenna\  selection string is a semi-colon (\ ’;’\ )
      separated list of baseline specifications. A baseline
      specification is of the form:

      -  ’ANT1’\  — Select all baselines including the antenna(s)
         specified by the selector \ ANT1\ .

      -  ’ANT1&’\  — Select only baselines between the antennas
         specified by the selector \ ANT1\ .

      -  ’ANT1&ANT2’\  — Select only the cross-correlation baselines
         between the antennas specified by selector \ ANT1\  and
         antennas specified by selector \ ANT2\ . Thus \ ’ANT1&’\  is an
         abbreviation for \ ’ANT1&ANT1’\ .

      -  ’ANT1&&ANT2’\  — Select only auto-correlation and
         cross-correlation baselines between antennas specified by the
         selectors \ ANT1\  and \ ANT2\ . Note that this is what the
         default \ antenna=’’\  \ gives you.

      -  ’ANT1&&&’\  — Select only autocorrelations specified by the
         selector \ ANT1\ .

      The selectors \ ANT1\  and \ ANT2\  are comma-separated lists of
      antenna integer-IDs or literal antenna names, patterns, or regular
      expressions. The \ ANT\  strings are parsed and converted to a
      list of antenna integer-IDs or IDs of antennas whose name match
      the given names/pattern/regular expression. Baselines
      corresponding to all combinations of the elements in lists on
      either side of ampersand are selected.

      Integer IDs can be specified as single values or a range of
      integers. When items of the list are parsed as literal strings or
      regular expressions or patterns. All antenna names that match the
      given string (exact match)/regular expression/pattern are
      selected.

       

      .. container:: alert-box

         ALERT: Just for antenna selection, a user supplied integer (or
         integer list) is converted to a string and matched against the
         antenna name. If that fails, the normal logic of using an
         integer as an integer and matching it with antenna index is
         done. Note that currently there is no method for specifying a
         pure index (e.g. a number that will not first be checked
         against the name).

       

      The comma is used only as a separator for the list of antenna
      specifications. The list of baselines specifications is a
      semi-colon separated list, e.g.

      .. container:: casa-input-box

         antenna = '1~3 & 4~6 ; 10&11'

      will select baselines between antennas 1,2,3 and
      4,5,6\ (’1&4’, ’1&5’, …, ’3&6’\ ) plus baseline \ ’10&11’\ .

      The wildcard operator (\ *’*’*\ ) will be the most often used
      pattern. To make it easy to use, the wildcard (and only this
      operator) can be used without enclosing it in quotes. For example,
      the selection

      .. container:: casa-input-box

         antenna = 'VA*'

      will match all antenna names which have ’VA’\  \ as the first 2
      characters in the name (irrespective of what follows after these
      characters).

      There is also a negation operator “\ !\ ” that can be used to
      de-select antennas or baselines.

      Some examples:

      .. container:: casa-input-box

         antenna=''           # shows blank autocorr pages
         antenna='*&*'        # does not show the autocorrs
         antenna='*&&*'       # show both auto and cross-cor (default)
         antenna='*&&&'       # shows only autocorrs
          
         antenna='5&*'        # shows non-auto baselines with AN 5
         antenna='5,6&&&'     # AN 5 and 6 autocor
         antenna='5&&&;6&*'   # AN 5 autocor plus cross-cors to AN 6
         antenna='5,6,7&'     # all baselines in common between antennas
         5, 6, and 7
         antenna='!5'         # baselines not involving AN 5

      Antenna numbers as names: Needless to say, naming antennas such
      that the names can also be parsed as a valid token of the syntax
      is a bad idea. Nevertheless, antenna names that contain any of the
      reserved characters and/or can be parsed as integers or integer
      ranges can still be used by enclosing the antenna names in double
      quotes (' "ANT" '). E.g. the string

      .. container:: casa-input-box

         antenna = '10~15,21,VA22'

      will expand into an antenna ID list 10,11,12,13,14,15,21,22
      (assuming the index of the antenna named ’VA22’\  is 22). If,
      however, the antenna with ID index 50 is named \ ’21’\ , then the
      string

      .. container:: casa-input-box

         antenna = '10~15,21,VA22'

      will expand into an antenna ID list of
      10,11,12,13,14,15,50,22. Keep in mind that numbers are FIRST
      matched against names, and only against indices if that matching
      fails. There is currently no way to force a selection to use the
      index, and if there an antenna with that name it will select that.

      Read elsewhere (e.g. info regex under Unix) for details of regular
      expression and patterns.

      .. rubric:: 
         Antenna stations 
         :name: antenna-stations

      Instead of antenna names, the antenna station names are also
      accepted by the selection syntax., e.g. ’N15’ for the JVLA.

       

      .. rubric:: ANT@STATION selection syntax 
         :name: antstation-selection-syntax

      Sometimes, data from multiple array configurations are stored in a
      single MS. But some antennas may have been moved during
      reconfiguration and the\  \ ’ANT@STATION’\  syntax can distinguish
      between them. ’\ ANT\ ’ is the antenna name or index
      and ’\ STATION\ ’ is the antenna station name, e.g., ’EA12@W03’
      selects antenna EA012 but only at times when it is positioned on
      station W03. Wildcards are accepted, e.g. ’EA12@*’ selects all
      visibilities from antenna EA12, and ’*@W03’ would select all
      antennas that are located on station ’\ W03\ ’ during any
      observations included in the MS.

      .. container:: info-box

         `Antenna/Baseline
         Selection <http://casacore.github.io/casacore-notes/263.html#x1-100003>`__\ \  \ -
         Expression for selection along baseline/antenna aixs (CASAcore
         docs)

       

      .. rubric:: The \ *scan*\  Parameter 
         :name: sec128
         :class: subsubsection

      The \ scan\  parameter selects the scan ID numbers of the data.
      There is currently no naming convention for scans. The scan ID is
      filled into the MS depending on how the data was obtained, so use
      this with care.

      Examples:

      .. container:: casa-input-box

         scan = '3'          # scan number 3.
         scan = '1~8'      # scan numbers 1 through 8, inclusive
         scan = '1,2,4,6'  # scans 1,2,4,6
         scan = '<9'        # scans <9 (1-8)NOTE: ALMA and VLA/JVLA
         number scans starting with 1 and not 0. You can see what the
         numbering is in your MS using the listobs task
         with verbose=True.

       

      .. container:: info-box

         `Scan/Sub-array
         Selection <http://casacore.github.io/casacore-notes/263.html#x1-350009>`__
         - Expression for selection based on scan or sub-array indices
         (CASAcore docs)

       

      .. rubric:: The \ timerange\  Parameter
         :name: sec129
         :class: subsubsection

       The time strings in the following (T0\ , \ T1\  and \ dT\ ) can
      be specified as \ YYYY/MM/DD/HH:MM:SS.FF\ . The time fields
      (i.e., \ YYYY\ , \ MM\ , \ DD\ , \ HH\ , \ MM\ , \ SS\  and \ FF\ ),
      starting from left to right, may be omitted and they will be
      replaced by context sensitive defaults as explained below.

      Some examples:

       

      timerange='T0~T1': Select all time stamps from T0\  to \ T1. For
      example:

      .. container:: casa-input-box

         timerange = '2007/10/09/00:40:00 ~ 2007/10/09/03:30:00'

      Note that fields missing in T0\  are replaced by the fields in the
      time stamp of the first valid row in the MS. For example,

      .. container:: casa-input-box

         timerange = '09/00:40:00 ~ 09/03:30:00'

      where the\  YY/MM/\  part of the selection has been defaulted to
      the start of the MS.

      Fields missing in \ T1\ , such as the date part of the string, are
      replaced by the corresponding fields of \ T0\  (after its defaults
      are set). For example:

      .. container:: casa-input-box

         timerange = '2007/10/09/22:40:00 ~ 03:30:00'

      does the same thing as above.

       

      timerange='T0':  Select all time stamps that are within an
      integration time of T0\ . For example:

      .. container:: casa-input-box

         timerange = '2007/10/09/23:41:00'

      Integration time is determined from the first valid row (more
      rigorously, an average integration time should be computed).
      Default settings for the missing fields of \ T0 are as in the
      first example.

       

      timerange='T0+dT': Select all time stamps starting from T0 and
      endingwith time stamp \ *T0+dT*\ . For example:

      .. container:: casa-input-box

         timerange = '23:41:00+01:00:00'

      picks an hour-long chunk of time.

      Defaults of T0\  are set as usual. Defaults for \ dT\  are set
      from the time corresponding to MJD=0. Thus, \ dT is a
      specification of length of time from the assumed nominal "start of
      time".

       

      timerange='>T0': Select all times greater than \ *T0*\ . For
      example:

      .. container:: casa-input-box

         timerange = '>2007/10/09/23:41:00'
         timerange = '>23:41:00'                   # Same thing without
         day specification

      Default settings for *T0* are as above.

      timerange='<T1': Select all times less than \ *T1*\ . For example:

      .. container:: casa-input-box

         timerange = '<2007/10/09/23:41:00'

      Default settingsfor \ *T1*\  are as above.

       

      An ultra-conservative selection might be:

      .. container:: casa-input-box

         timerange = '1960/01/01/00:00:00~2020/12/31/23:59:59'

      which would choose all possible data!

       

      .. container:: info-box

         `Time
         Selection <http://casacore.github.io/casacore-notes/263.html#x1-80002>`__\ **-
         Expression for selection data along time axisTime Selection
         (CASAcore docs) **

       

      .. rubric:: The uvrange Parameter
         :name: sec130
         :class: subsubsection

       Rows in the MS can also be selected based on the uv-distance or
      physical baseline length that the visibilities in each row
      correspond to. This \ *uvrange*\  can be specified in various
      formats.

      The basic building block of uv-distance specification is a valid
      number with optional units in the format N[UNIT] (the unit in
      square brackets is optional). We refer to this basic buildingblock
      as UVDIST\ . The default unit is meter. Units of length (such
      as \ ’m’\  \ and \ ’km’\ ) select physical baseline distances
      (independent of wavelength). The other allowed units are in
      wavelengths (such as \ ’lambda’, ’klambda’\  and \ ’Mlambda’\  and
      are true uv-plane radii

      $$UVDIST=\sqrt{u^2+v^2}$$

       

      If only a single UVDIST\  is specified, all rows, the uv-distance
      of which exactly matches the given \ UVDIST\ , are selected.

      UVDIST\  can be specified as a range in the format
      'N0~N1[UNIT]' (where \ N0\  and \ N1\  are valid numbers). All
      rows corresponding to uv-distance
      between \ N0\  and \ N1\  (inclusive) when converted the specified
      units are selected.

      UVDIST\  can also be selected via comparison operators. When
      specified in the format \ ’>UVDIST’\ , all visibilities with
      uv-distances greater than the given \ UVDIST\  are selected.
      Likewise, when specified in the format \ ’<UVDIST’\ , all rows
      with uv-distances less than the given \ UVDIST\  are selected.

      Any number of above mentioned uv-distance specifications can be
      given as a comma-separated list.

      Examples:

      .. container:: casa-input-box

         uvrange = '100~200km'                              # an annulus
         in physical baseline length
         uvrange = '24~35Mlambda, 40~45Mlambda' # two annuli in units of
         mega-wavelengths
         uvrange = '< 45klambda'                             # less than
         45 kilolambda
         uvrange = '> 0lambda'                                # greater
         than zero length (no auto-corrs)
         uvrange = '100km'                                      #
         baselines of length 100km
         uvrange = '100klambda'                              # uv-radius
         100 kilolambda

      .. container:: info-box

         `UV-distance
         Selection <http://casacore.github.io/casacore-notes/263.html#x1-210005>`__
         - Expression for selection based on uv-distance (CASAcore docs)

      .. rubric:: 
         The \ correlation\  Parameter
         :name: sec131
         :class: subsubsection

      The \ correlation\  parameter will select between different
      correlation products. They can be either the correlation ID or
      values such as ’XX’, ’YY’, ’XY’, ’YX’, ’RR’, ’LL’, ’RL’, ’LR’.

       

      .. container:: info-box

         `Polarization
         Selection <http://casacore.github.io/casacore-notes/263.html#x1-310007>`__\ -
         Expression for selection along the polarization axis (CASAcore
         docs) 

      .. rubric:: 
         The \ intent\  Parameter
         :name: sec132
         :class: subsubsection

      intent\  is the scan intent that was specified when the
      observations were set up. They typically describe what was
      intended with a specific scan, i.e. a flux or phase calibration, a
      bandpass, a pointing, an observation of your target, or something
      else or a combination. The format for the scan intents of your
      observations are listed in the logger when you run listobs.
      Minimum matching with wildcards will work, like ’*BANDPASS*’. This
      is especially useful when multiple intents are attached to scans.

       

      .. container:: info-box

         `'Scan Intent' based
         selection <http://casacore.github.io/casacore-notes/263.html#x1-320008>`__\  -
         Selection by intent (CASAcore docs)

        

      .. rubric:: The \ observation\  Parameter
         :name: sec133
         :class: subsubsection

      The \ observation\  parameter can select between different
      observation IDs. They will be assigned to parts of a combined data
      set during a run of concat. Each input MS will receive its own
      observation id in the process.

       

      .. rubric:: The \ feed\  Parameter
         :name: sec134
         :class: subsubsection

      The \ *feed*\  parameter can select between different feeds, e.g.
      for different feeds in a single dish multibeam array.

       

      .. rubric:: The \ msselect\  Parameter
         :name: sec135
         :class: subsubsection

      More complicated selections within the MS structure are possible
      using the Table Query Language (TaQL). This is accessed through
      the msselect\  parameter.

      Note that the TaQL syntax does not follow the rules given in
      above for our other selection strings. TaQL is explained in more
      detail in CASAcore NOTE 199 —\ \ `Table Query
      Language <https://casacore.github.io/casacore-notes/199.html>`__\ \ .
      The specific columns of the MS are given in the most recent\ \ `MS
      specification
      document <https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals/measurement-set>`__\ \ .

      Most selection can be carried out using the other selection
      parameters. However, these are merely shortcuts to the underlying
      TaQL selection. For example, field and spectral window selection
      can be done using msselect rather than through field or spw:

      .. container:: casa-input-box

         | msselect='FIELD_ID == 0'                  # Field id 0 only
         | msselect='FIELD_ID <= 1'                  # Field id 0 and 1
         | msselect='FIELD_ID IN [1,2]'              # Field id 1 and 2
         | msselect='FIELD_ID==0 && DATA_DESC_ID==3' # Field id 0 in spw
           id 3 only

      .. container:: alert-box

         ALERT: The \ msselect\  style parameters will be phased out of
         the tasks. TaQL selection will still be available in the
         Toolkit. 

       

      This page describes the syntax for the various expressions for
      selecting data from the MeasurementSet, implemented in the
      MSSelection module of CASACore. All expressions consist of a comma
      or semi-colon separated list of speciﬁcations.  The MSSelection
      module can also be used for other tables that follow the general
      data base design of the MeasurementSet. The CASA CalTables is an
      example which also uses the MSSelection module for selection.The
      most up to date document will always be on the `CASACore GitHub
      Repository <http://casacore.github.io/casacore-notes/263.html>`__.
      The content in this page is derived from this `GitHub
      snapshot <https://github.com/casacore/casacore-notes/tree/92c6d74cb32592980224b0707884823c5623088f/263.dir>`__.

      .. container:: info-box

         `Using MSSelection expressions in
         TaQL <http://casacore.github.io/casacore-notes/263.html#x1-3700010>`__
         - MSSelection expressions can also be used in pure-TaQL
         expressions (CASAcore docs)

      .. rubric::  
         :name: section-5
         :class: sectionHead

.. container:: section
   :name: viewlet-below-content-body
