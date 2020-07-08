.. container::
   :name: viewlet-above-content-title

Methods
=======

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task applycal parameters

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-methods

          

         .. container:: param

            constructor **table**

            .. container:: collcontent

               .. container:: methoddesc

                  Use this constructor to construct a table tool inside
                  casapy from the name of a disk file containing a
                  \\casa\\ Table. A new table may also be created from a
                  table descriptor (see tablecreatedesc). When creating
                  a new table, detailed data manager information can be
                  given using the \\texttt{dminfo} argument. This is a
                  record as returned by the getdminfo function. Most of
                  the arguments are rarely used: most of the time,
                  you'll just need to use the tablename, and perhaps
                  nomodify. A table can be shared by multiple processes
                  by using the appropriate locking options. The possible
                  options are: \\\- auto: let the system take care of
                  locking. At regular time intervals these autolocks are
                  released to give other processes the opportunity to
                  access the table. The aipsrc variable
                  \\\\texttt{table.relinquish.reqautolocks.interval}
                  defines the number of seconds between releasing
                  autolocks on tables needed in another process.
                  \\\\texttt{table.relinquish.allautolocks.interval}
                  defines the number of seconds between releasing all
                  autolocks. \\\- autonoread: as auto, but no read
                  locking is needed. This must be used with care,
                  because it means that reading can be done while the
                  table tool is not synchronized with the table file (as
                  is normally done when a lock is acquired). The
                  function \\texttt{resync} can be used to explicitly
                  synchronize the table tool \\\- user: the user takes
                  care by explicit calls to lock and unlock \\\-
                  usernoread: as user and the no readlocking behaviour
                  of autonoread. \\\- permanent: use a permanent lock;
                  the constructor fails when the table is already in use
                  in another process \\\- permanentwait: as above, but
                  wait until the other process releases its lock \\\-
                  default: this is the default option. If the given
                  table is already open, the locking option in use is
                  not changed. Otherwise it reverts to auto. \\\When
                  auto locking is used, it is possible to give a record
                  containing the fields option, interval, and/or
                  maxwait. In this way advanced users have full control
                  over the locking options. In practice this is hardly
                  ever needed. When creating a new table, the endian
                  format in which the data should be stored, can be
                  specified. The possible values are: \\\- big: big
                  endian format (as used on e.g. SUN) \\\- little:
                  little endian format (as used on e.g. PC) \\\- local:
                  use the endian format of the machine being used \\\-
                  aipsrc: use the endian format specified in aipsrc
                  variable table.endianformat (which defaults to big).
                  \\\The default is aipsrc. \\\Note that usually it is
                  best to store data in local endian format, because
                  that requires the least amount of byte swapping.
                  However, if the table must be accessible with AIPS++
                  version 1.7 or before, big endian should be used. When
                  creating a new table, the table will normally reside
                  on disk. It is, however, possible to specify that the
                  table should be held in memory. In such a case the
                  table is process specific, thus cannot be seen by
                  other processes. Note that a memory table uses the
                  MemoryStMan storage manager for all its stored
                  columns, but it is still possible to use virtual
                  columns as well.

               .. container:: methodsection

                  Parameters : None

               .. container:: methodsection

                  Example

               .. container:: methodexam

                  table1:=table("3C273XC1.MS"); table1.browse();

         .. container:: param

            function **fromfits**

            .. container:: collcontent

               .. container:: methoddesc

                  Create a table from binary FITS format. This generates
                  a CASA table from the binary FITS table in the given
                  HDU (header unit) of the FITS file. Note that other
                  FITS formats ({\em e.g.} Image FITS and UVFITS) are
                  read by other means. \\\It is possible to specify the
                  storage manager to use for the table:
                  \\\\texttt{standard} is the default storage manager.
                  \\\\texttt{incremental} is efficient for slowly
                  varying data. \\\\texttt{memort} is for in memory use
                  for e.g to grab given columns via getcol.

               .. container:: methodsection

                  Parameters

               .. container:: parameters2

                  tablename : undefined

               .. container:: methodparmtable

                  Name of table to be created

.. container:: parameters2

   fitsfile : undefined

.. container:: methodparmtable

   Name of FITS file to be read

.. container:: parameters2

   whichhdu : undefined = 1

.. container:: methodparmtable

   Which HDU to read (0-relative to primary HDU i.e. 1 is the smallest
   valid value)

.. container:: parameters2

   storage : undefined = standard

.. container:: methodparmtable

   Storage manager to use (standard or incremental or memory)

Allowed Value(s)

standard incremental memory

.. container:: parameters2

   convention : undefined = none

.. container:: methodparmtable

   Convention to use (sdfits or none)

.. container:: parameters2

   nomodify : undefined = true

.. container:: methodparmtable

   Open Read-only?

.. container:: parameters2

   ack : undefined = true

.. container:: methodparmtable

   Acknowledge creations, etc

.. container:: param

   function **fromascii**

   .. container:: collcontent

      .. container:: methoddesc

         Create a table from an ASCII file. Columnar data as well as
         table and column keywords may be specified. \\\Once the table
         is created from the ASCII data, it is opened in the specified
         mode by the table tool. The table columns are filled from a
         file containing the data values separated by a separator (one
         line per table row). The default separator is a blank. Blanks
         after the separator are ignored. \\\If a non-blank separator is
         used, values can be empty. Such values default to 0, empty
         string, or F depending on the data type. E.g. 1,,2, has 4
         values of which the 2nd and 4th are empty and default to 0.
         Similarly if fewer values are given than needed, the missing
         values get the default value. Either the data format can be
         explicitly specified or it can be found automatically. The
         former gives more control in ambiguous situations. Both scalar
         and array columns can be generated from the ASCII input. The
         format string determines the type and optional shape. In
         automatic mode (\texttt{autoheader=True}) the first line of the
         ASCII data is analyzed to deduce the data types. Only the types
         I, D, and A can be recognized. A number without decimal point
         or exponent is I (integer), otherwise it is D (double). Any
         other string is A (string). Note that a number may contain a
         leading sign (+ or -). The \\texttt{autoshape} argument can be
         used to specify if the input should be stored as multiple
         scalars (the default) or as a single array. In the latter case
         one axis in the shape can be defined as variable length by
         giving it the value 0. It means that the actual array shape in
         a row is determined by the number of values in the
         corresponding input line. Columns get the names
         \\texttt{Column1}, \\texttt{Column2}, etc.. \\\For example:
         \\begin{enumerate} \\item \\texttt{autoshape=[]} (which is the
         default) means that all values are to be stored as scalar
         columns. \\item \\texttt{autoshape=0} means that all values in
         a row are to be stored as a variable length vector. \\item
         \\texttt{autoshape=10} defines a fixed length vector. If an
         input line contains less than 10 values, the vector is filled
         with default values. If more than 10 values, the latter values
         are ignored. \\item \\texttt{autoshape=[5,0]} defines a 2-dim
         array of which the 2nd axis is variable. Note that if an input
         line does not contain a multiple of 5 values, the array is
         filled with default values. \\end{enumerate} If the format of
         the table is explicitly specified, it has to be done either in
         the first two lines of the data file (named by the argument
         filename), or in a separate header file (named by the argument
         headerfile). In both forms, table keywords may also be
         specified before the column definitions. The column names and
         types can be described by two lines: \\begin{enumerate} \\item
         The first line contains the names of the columns. These names
         may be enclosed in quotes (either single or double). \\item The
         second line contains the data type and optionally the shape of
         each column. Valid types are: \\begin{itemize} \\item S for
         Short data \\item I for Integer data \\item R for Real data
         \\item D for Double Precision data \\item X for Complex data
         (Real followed by Imaginary) \\item Z for Complex data
         (Amplitude then Phase) \\item DX for Double Precision Complex
         data (Real followed by Imaginary) \\item DZ for Double
         Precision Complex data (Amplitude then Phase) \\item A for
         ASCII data (a value must be enclosed in single or double quotes
         if it contains whitespace) \\item B for Boolean data (False are
         empty string, 0, or any string starting with F, f, N, or n).
         \\end{itemize} \\end{enumerate} If a column is an array, the
         shape has to be given after the data type without any
         whitespace. E.g. \\texttt{I10} defines an integer vector of
         length 10. \\texttt{A2,5} defines a 2-dim string array with
         shape [2,5]. Note that \\texttt{I} is not the same as
         \\texttt{I1} as the first one defines a scalar and the other
         one a vector with length 1. The last column can have one
         variable length axis denoted by the value 0. It "consumes" the
         remainder of the input line. If the argument headerfile is set
         then the header information is read from that file instead of
         the first lines of the data file. To give a simple example of
         the form where the header information is located at the top of
         the data file: \\begin{verbatim} COLI COLF COLD COLX COLZ COLS
         I R D X Z A 1 1.1 1.11 1.12 1.13 1.14 1.15 Str1 10 11 12 13 14
         15 16 "" \\end{verbatim} Note that a complex number consists of
         2 numbers. \\\Also note that an empty string can be given. Let
         us now give an example of a separate header file that one might
         use to get interferometer data into \\casa: \\begin{verbatim} U
         V W TIME ANT1 ANT2 DATA R R R D I I X1,0 \\end{verbatim} The
         data file would then look like: \\begin{verbatim} 124.011
         54560.0 3477.1 43456789.0990 1 2 4.327 -0.1132 34561.0 45629.3
         3900.5 43456789.0990 1 3 5.398 0.4521 \\end{verbatim} Note that
         the DATA column is defined as a 2-dim array of 1 correlation
         and a variable number of channels, so the actual number of
         channels is determined by the input. In this example both rows
         will have 1 channel (note that a complex value contains 2
         values). Tables may have keywords in addition to the columns.
         The keywords are useful for holding information that is global
         to the entire table (such as author, revision, history, {\em
         etc,}). \\\The keywords in the header definitions must preceed
         the column descriptions. They must be enclosed between a line
         that starts with ".key..." and a line that starts with
         ".endkey..." (where ... can be anything). Between these two
         lines each line should contain the following as listed below. A
         table keywordset and column keywordsets can be specified. The
         latter can be specified by specifying the column name after the
         .keywords string. \\begin{itemize} \\item The keyword name,
         e.g., ANYKEY \\item The datatype and optional shape of the
         keyword (cf. list of valid types above) \\item The value or
         values for the keyword (the keyword may contain a scalar or an
         array of values). e.g., 3.14159 21.78945 \\end{itemize} Thus to
         continue the example above, one might wish to add keywords as
         follows: \\begin{verbatim} .keywords DATE A "97/1/16" REVISION
         D 2.01 AUTHOR A "Tim Cornwell" INSTRUMENT A "VLA" .endkeywords
         .keywords TIME UNIT A "s" .endkeywords U V W TIME ANT1 ANT2
         DATA R R R D I I X1,0 \\end{verbatim} Similarly to the column
         format string, the keyword formats can also contain shape
         information. The only difference is that if no shape is given,
         a keyword can have multiple values (making it a vector). It is
         possible to ignore comment lines in the header and data file by
         giving the \\texttt{commentmarker}. It indicates that lines
         starting with the given marker are ignored. Note that the
         marker can be a regular expression (e.g. texttt{' \*//'} tells
         that lines starting with // and optionally preceeded by blanks
         have to be ignored). With the arguments \\texttt{firstline} and
         \\texttt{lastline} one can specify which lines have to be taken
         from the input file. A negative value means 1 for
         \\texttt{firstline} or end-of-file for \\texttt{lastline}. Note
         that if the headers and data are combined in one file, these
         line arguments apply to the whole file. If headers and data are
         in separate files, these line arguments apply to the data file
         only. Also note that ignored comment lines are counted, thus
         are used to determine which lines are in the line range. The
         number of rows is determined by the number of lines read from
         the data file.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         tablename : undefined

      .. container:: methodparmtable

         Name of table to be created

.. container:: parameters2

   asciifile : undefined

.. container:: methodparmtable

   Name of ASCII file to be read

.. container:: parameters2

   headerfile : undefined

.. container:: methodparmtable

   Name of an optional file defining the format

.. container:: parameters2

   autoheader : undefined = false

.. container:: methodparmtable

   Determine header information automatically

.. container:: parameters2

   autoshape : undefined = -1

.. container:: methodparmtable

   Shape to be used if autoheader=True

.. container:: parameters2

   sep : undefined =

.. container:: methodparmtable

   Value separator

.. container:: parameters2

   commentmarker : undefined

.. container:: methodparmtable

   Regex indicating comment line

.. container:: parameters2

   firstline : undefined = 0

.. container:: methodparmtable

   First line to use

.. container:: parameters2

   lastline : undefined = -1

.. container:: methodparmtable

   Last line to use

.. container:: parameters2

   nomodify : undefined = true

.. container:: methodparmtable

   Open Read-only?

.. container:: parameters2

   columnnames : undefined

.. container:: methodparmtable

   Column Names

.. container:: parameters2

   datatypes : undefined

.. container:: methodparmtable

   Data types

.. container:: param

   function **open**

   .. container:: collcontent

      .. container:: methoddesc

         Opens a disk file containing an existing \\casa\\ Table. Most
         of the time you just need to specify the tablename and perhaps
         nomodify. A table can be shared by multiple processes by using
         the appropriate locking options. The possible options are: \\\-
         auto: let the system take care of locking. At regular time
         intervals these autolocks are released to give other processes
         the opportunity to access the table. \\\- autonoread: as auto,
         but no read locking is needed. This must be used with care,
         because it means that reading can be done while the table tool
         is not synchronized with the table file (as is normally done
         when a lock is acquired). The function \\texttt{resync} can be
         used to explicitly synchronize the table tool \\\- user: the
         user takes care by explicit calls to lock and unlock \\\-
         usernoread: as user and the no readlocking behaviour of
         autonoread. \\\- permanent: use a permanent lock; the
         constructor fails when the table is already in use in another
         process \\\- permanentwait: as above, but wait until the other
         process releases its lock \\\- default: this is the default
         option. If the given table is already open, the locking option
         in use is not changed. Otherwise it reverts to auto. \\\When
         auto locking is used, it is possible to give a record
         containing the fields option, interval, and/or maxwait. In this
         way advanced users have full control over the locking options.
         In practice this is hardly ever needed.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         tablename : undefined

      .. container:: methodparmtable

.. container:: parameters2

   lockoptions : undefined

.. container:: methodparmtable

   locking dictionary to be used : dict keys are 'option', 'interval',
   'maxwait'

.. container:: parameters2

   nomodify : undefined = true

.. container:: methodparmtable

.. container:: methodsection

   Example

.. container:: methodexam

   # First let's make a table for testing def maketesttable(): # Get
   path to CASA home directory by stipping name from '$CASAPATH'
   pathname=os.environ.get("CASAPATH").split()[0] # This is where the
   3C273XC1.fits data should be
   fitsdata=pathname+"/data/demo/3C273XC1.fits" # Remove old table if
   present !rm -rf 3C273XC1.MS ms.fromfits("3C273XC1.MS",fitsdata)
   ms.close() maketesttable() tb.open("3C273XC1.MS") tb.browse()
   tb.close() The first line opens an existing table 3C273XC1.MS, the
   second browses it using the browse function. tb.open("3C273XC1.MS",
   nomodify=False, lockoptions={'option':'user'}) tb.lock();
   tb.addrows(); tb.unlock(); In this example explicit user locking is
   used. The function lock is needed to acquire a (write) lock before
   the addrows is done. Thereafter the lock is released to give other
   processes the chance to operate on the table. \\\Note that releasing
   a lock implies flushing the table, so doing that very often can be
   quite expensive.

.. container:: param

   function **create**

   .. container:: collcontent

      .. container:: methoddesc

         Create a new \\casa\\ Table. Most of the time you just need to
         specify the table's name and a description of its format. A
         table can be shared by multiple processes by using the
         appropriate locking options. The possible options are: \\\-
         auto: let the system take care of locking. At regular time
         intervals these autolocks are released to give other processes
         the opportunity to access the table. \\\- autonoread: as auto,
         but no read locking is needed. This must be used with care,
         because it means that reading can be done while the table tool
         is not synchronized with the table file (as is normally done
         when a lock is acquired). The function \\texttt{resync} can be
         used to explicitly synchronize the table tool \\\- user: the
         user takes care by explicit calls to lock and unlock \\\-
         usernoread: as user and the no readlocking behaviour of
         autonoread. \\\- permanent: use a permanent lock; the
         constructor fails when the table is already in use in another
         process \\\- permanentwait: as above, but wait until the other
         process releases its lock \\\- default: this is the default
         option. If the given table is already open, the locking option
         in use is not changed. Otherwise it reverts to auto. \\\When
         auto locking is used, it is possible to give a record
         containing the fields option, interval, and/or maxwait. In this
         way advanced users have full control over the locking options.
         In practice this is hardly ever needed.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         tablename : undefined

      .. container:: methodparmtable

.. container:: parameters2

   tabledesc : undefined

.. container:: methodparmtable

   description of the table's format

.. container:: parameters2

   lockoptions : undefined = default

.. container:: methodparmtable

   locking to be used

.. container:: parameters2

   endianformat : undefined

.. container:: methodparmtable

.. container:: parameters2

   memtype : undefined

.. container:: methodparmtable

.. container:: parameters2

   nrow : undefined = 0

.. container:: methodparmtable

.. container:: parameters2

   dminfo : undefined

.. container:: methodparmtable

   Data Manager information

.. container:: methodsection

   Example

.. container:: methodexam

   # First let's get sample descriptions of a table and its data
   managers. import os, shutil def
   get_tabledesc_and_dminfo(tabname="3C273XC1.MS"): made_copy = False #
   Fetch new table if tabname not present if not os.path.isdir(tabname):
   # Get path to CASA root directory by stripping name from '$CASAPATH'
   pathname = os.environ.get("CASAPATH").split()[0] # There should be
   some data here fitsdata = pathname + "/data/demo/3C273XC1.fits"
   tabname = "3C273XC1.MS" ms.fromfits(tabname, fitsdata) ms.close()
   made_copy = True tb.open(tabname) tabdesc = tb.getdesc() dminfo =
   tb.getdminfo() print tabname, "has", tb.nrows(), "rows." tb.close() #
   Clean up if made_copy: shutil.rmtree(tabname) return tabdesc, dminfo
   tabdesc, dmi = get_tabledesc_and_dminfo() tabdesc # prints tabdesc
   dmi # prints dmi # You could alter tabdesc and/or dmi at this point.
   # Unnecessary, but just to show there is nothing up my sleeve...
   tb.close() tb.create("myempty.ms", tabdesc, dminfo=dmi) tb.nrows() #
   0L tb.addrows(5) # Add the rows \_before\_ filling the columns.
   tb.putcol('ARRAY_ID', numpy.array([0 for i in range(5)]))
   tb.putcol('ANTENNA1', numpy.array(range(5))) tb.putcol('ANTENNA2',
   numpy.array(range(1,6))) tb.browse() # Still mostly, but not
   completely, empty. tb.close() This creates a CASA table using a
   description of a table and its data managers from an existing MS.

.. container:: param

   function **flush**

   .. container:: collcontent

      .. container:: methoddesc

         Until a flush is performed, the results of all operations are
         not reflected in any change to the disk file. Hence you {\em
         must} do a flush to write the changes to disk.

      .. container:: methodsection

         Parameters : None

.. container:: param

   function **fromASDM**

   .. container:: collcontent

      .. container:: methoddesc

         .keywords DATE A "07/7/23" REVISION D 0 AUTHOR A "Paulo C.
         Cortes" INSTRUMENT A "ALMA" .endkeywords The main function for
         this task is to create a CASA::Table from a XML ASDM Table. The
         classes asdmCasaXMLUtil and asdmCasaSaxHandler are the main
         objects which implement the task. The asdmCasaSaxHandler
         encapsulate all the operations returning a reference to a
         CASA::Table. The class uses xerces-c to parse the XML table and
         creates the CASA::Table. The implementation assumes the
         integrity of the XML data, it not attempting to check whether
         the XML data meets a column format or not. In detail, an
         ArrayString column should agree with the following format: nd
         nx ... data, where nd is the number of dimensions, nx is the
         size of the first dimension (implemented upto a cube, i.e.
         nx,ny,nz), and data is the array itself which should have the
         appropiate number of elements. For example, a VectorString
         column could be: 1 2 "I" "Q" or dimension 1, size 2, and two
         string elements. Due to the lack of data type spefication in
         the XML tables, the column names are hardcoded into the
         asdmCasaSaxHandler based on the ASDM specification (see
         http://aramis.obspm.fr/~alma/ASDM/ASDMEntities/index.html).
         While missing data from a table column will be accepted by the
         task, any new column beyond the specification has to be added
         into the class, also, any change in data types form the
         specificatin will produce a crash, CASA is picky with data
         types integrity. So far, the list of tables included in the
         class is: AlmaCorrelatorMode.xml, Antenna.xml
         ConfigDescription.xml, DataDescription.xml, ExecBlock.xml,
         Feed.xml, Field.xml, Main.xml, Polarization.xml, Processor.xml,
         Receiver.xml, SBSummary.xml, Scan.xml, Source.xml,
         SpectralWindow.xml, State.xml, Station.xml, Subscan.xml,
         SwitchCycle.xml, CalCurve.xml, CalData.xml, CalPhase.xml more
         tables will follow. The usage of fromASDM is simple, it gets
         two string, tablename and xmlfile, where tablename is the
         CASA::Table to be written and xmlfile represents the ASDM XML
         table. To call it do: tb.fromasdm(tablename,xmlfile)

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         tablename : undefined

      .. container:: methodparmtable

         Name of table to be created

.. container:: parameters2

   xmlfile : undefined

.. container:: methodparmtable

   Name of the XML file to be read

.. container:: param

   function **resync**

   .. container:: collcontent

      .. container:: methoddesc

         Acquiring a read or write lock automatically synchronizes the
         internals of the table tool with the actual contents of the
         table files. In this way different processes accessing the same
         table always use the same table data. \\\However, a table can
         be used without read locking. In that case the table tool
         internals are not synchronized automatically. The resync
         function offers a way to do explicit synchronization. It is
         only useful if the table is opened with locking mode
         \\texttt{autonoread} or \\texttt{usernoread}.

      .. container:: methodsection

         Parameters : None

.. container:: param

   function **close**

   .. container:: collcontent

      .. container:: methoddesc

         First a flush is done, then the table is closed inside casapy
         and is no longer available for use.

      .. container:: methodsection

         Parameters : None

.. container:: param

   function **copy**

   .. container:: collcontent

      .. container:: methoddesc

         Copy the table. All subtables are also copied. References to
         another table are preserved. The argument \\texttt{deep}
         determines how a reference table (i.e. the result of a query)
         is copied. By default a file copy is made, thus the resulting
         table still contains references and no actual data. If,
         however, \\texttt{deep=True} is given, a deep copy is made
         which means that the actual data are copied. Also all subtables
         are copied. \\\Normally a plain table is copied by copying the
         files. However, if \\texttt{deep=True} and
         \\texttt{valuecopy=True} are given, a plain table is copied by
         copying all its values and subtables. This is useful to
         reorganize the tables, i.e. to regain file space that is wasted
         by frequent updates to a table. \\\The argument
         \\texttt{dminfo} can be used to specify explicit data manager
         info for the columns in the new plain table. It can be used to
         change, for example, a storage manager from IncrStMan to
         StandardStMan. The \\texttt{dminfo} is a record as returned by
         the getdminfo If \\texttt{dminfo} is a non-empty record, it
         forces \\texttt{valuecopy=True}. The standard operation is make
         the copy to a plain table. It is, however, possible to copy to
         a memory table by giving \\texttt{memorytable=True}. The endian
         format for the newly created table can be specified. This is
         only meaningful if a deep copy is made to a plain table. The
         possible values are: \\\- big: big endian format (as used on
         e.g. SUN) \\\- little: little endian format (as used on e.g.
         PC) \\\- local: use the endian format of the machine being used
         \\\- aipsrc: use the endian format specified in aipsrc variable
         table.endianformat (which defaults to big). \\\The default is
         aipsrc. Normally the \\texttt{copy} function only copies the
         table and does not create a new table tool object. The user can
         do that by opening the newly created table in the standard way.
         However, it is possible to get an object back by using
         \\texttt{returnobject=True}. An object is always returned if
         the copy is made to a memory table.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         newtablename : undefined

      .. container:: methodparmtable

         Name of newtable on disk

.. container:: parameters2

   deep : undefined = false

.. container:: methodparmtable

   Make a deep copy of a reference table?

.. container:: parameters2

   valuecopy : undefined = false

.. container:: methodparmtable

   Make a deep copy of any table?

.. container:: parameters2

   dminfo : undefined

.. container:: methodparmtable

   Data manager info for new table

.. container:: parameters2

   endian : undefined = aipsrc

.. container:: methodparmtable

   Endian format of new table

.. container:: parameters2

   memorytable : undefined = false

.. container:: methodparmtable

   Hold new table in memory?

.. container:: parameters2

   returnobject : undefined = false

.. container:: methodparmtable

   Return a tool object for the new table

.. container:: parameters2

   norows : undefined = false

.. container:: methodparmtable

   Don't copy any rows (useful for copying only the table structure)

.. container:: param

   function **copyrows**

   .. container:: collcontent

      .. container:: methoddesc

         Copy rows from this table to another. By default all rows of
         this table are appended to the output table. It is possible
         though to control which rows are copied. \\\Rows are added to
         the output table as needed. Because no rows can be added to a
         reference table, it is only possible to overwrite existing rows
         in such tables. Only the data of columns existing in both
         tables will be copied. Thus by making a reference table
         consisting of a few columns, it is possible to copy those
         columns only.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         outtable : undefined

      .. container:: methodparmtable

         table object of output table

.. container:: parameters2

   startrowin : undefined = 0

.. container:: methodparmtable

   First row to take from input table

.. container:: parameters2

   startrowout : undefined = -1

.. container:: methodparmtable

   First row to write in output table, -1 (=end)

.. container:: parameters2

   nrow : undefined = -1

.. container:: methodparmtable

   Nr of rows to copy, -1 (=all)

.. container:: methodsection

   Example

.. container:: methodexam

   This example appends rows to the table itself, thus doubles the
   number of rows. tb.open('3C273XC1.MS',nomodify=False)
   tb.copyrows('3C273XC1.MS') tb.close() This example copies 10 rows of
   the selected subset of the MS to the beginning of the output MS. !rm
   -rf in.MS out.MS ms.fromfits('in.MS','3C273XC1.fits') #Make two MSs
   ms.fromfits('out.MS','3C273XC1.fits') #for example ms.close()
   tb.open("in.MS") t1 = tb.query('ANTENNA1==0') tb.close()
   t1.copyrows("out.MS",nrow=10,startrowout=0) t1.close()

.. container:: param

   function **done**

   .. container:: collcontent

      .. container:: methoddesc

         Effectively a synonym for function close.

      .. container:: methodsection

         Parameters : None

.. container:: param

   function **iswritable**

   .. container:: collcontent

      .. container:: methoddesc

         Test if the table is opened for write.

      .. container:: methodsection

         Parameters : None

.. container:: param

   function **endianformat**

   .. container:: collcontent

      .. container:: methoddesc

         Get the endian format used for this table. It returns a string
         with value 'big' or 'little'.

      .. container:: methodsection

         Parameters : None

.. container:: param

   function **lock**

   .. container:: collcontent

      .. container:: methoddesc

         Try to acquire a read or write lock on the table. Nothing will
         be done if the table is already correctly locked by this
         process. It is only needed when user locking is used. When the
         lock is acquired, the internal caches will be synchronized with
         the (possibly changed) contents of the table. \\\It is possible
         to specify the number of attempts to do (1 per second) in case
         the table is locked by another process. The default 0 is trying
         indefinitely.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         write : undefined = true

      .. container:: methodparmtable

         Write lock? (F=read lock)

.. container:: parameters2

   nattempts : undefined = 0

.. container:: methodparmtable

   Nr of attempts

.. container:: param

   function **unlock**

   .. container:: collcontent

      .. container:: methoddesc

         The table is flushed and the lock on the table is released.
         This function is only needed when user locking is used.
         However, it is also possible to use it with auto locking. In
         that case the lock will automatically be re-acquired before the
         next table operation.

      .. container:: methodsection

         Parameters : None

.. container:: param

   function **datachanged**

   .. container:: collcontent

      .. container:: methoddesc

         This function tests if data in the table have changed (by
         another process) since the last call to this function.

      .. container:: methodsection

         Parameters : None

.. container:: param

   function **haslock**

   .. container:: collcontent

      .. container:: methoddesc

         Has this process a read or write lock on the table?

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         write : undefined = true

      .. container:: methodparmtable

         Has it a write lock? (F=read lock)

.. container:: param

   function **lockoptions**

   .. container:: collcontent

      .. container:: methoddesc

         Get the lock options used for this table. It returns a record
         with the fields: option, interval and maxwait. The record can
         be used as the lockoptions argument when opening a table.

      .. container:: methodsection

         Parameters : None

.. container:: param

   function **ismultiused**

   .. container:: collcontent

      .. container:: methoddesc

         Is the table still in use in another process? If so, the table
         cannot be deleted.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         checksubtables : undefined = false

      .. container:: methodparmtable

         check if subtables are multiused?)

.. container:: param

   function **browse**

   .. container:: collcontent

      .. container:: methoddesc

         To start the browser, the environment variable DISPLAY must be
         set.

      .. container:: methodsection

         Parameters : None

.. container:: param

   function **name**

   .. container:: collcontent

      .. container:: methoddesc

         Gives the name of the \\casa\\ table on disk that the table
         tool has open.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         tb.open("3C273XC1.MS") tb.name() # 3C273XC1.MS

.. container:: param

   function **createmultitable**

   .. container:: collcontent

      .. container:: methoddesc

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         outputTableName : undefined

      .. container:: methodparmtable

         name of the concatenated table

.. container:: parameters2

   tables : undefined

.. container:: methodparmtable

   list of the names of the tables to be concatenated

.. container:: parameters2

   subdirname : undefined

.. container:: methodparmtable

   optional name of the subdirectory into which the input tables are
   moved

.. container:: methodsection

   Example

.. container:: methodexam

.. container:: param

   function **toasciifmt**

   .. container:: collcontent

      .. container:: methoddesc

         Write a table into an ASCII format approximately compatible
         with fromascii except that in order to permit variable shaped
         arrays (as they often occur in MSs), array values are output
         enclosed in square brackets. The separator between values can
         be specified and defaults to a blank. Note that columns
         containing invalid data or record type data are ignored and a
         warning is issued. If the argument headerfile is set then the
         header information is written to that file instead of the first
         two lines of the data file.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         asciifile : undefined

      .. container:: methodparmtable

         Name of ASCII file to be written

.. container:: parameters2

   headerfile : undefined

.. container:: methodparmtable

   Name of an optional file defining the format

.. container:: parameters2

   columns : undefined

.. container:: methodparmtable

   Names of columns to be written, default is all

.. container:: parameters2

   sep : undefined

.. container:: methodparmtable

   Value separator, default is one blank

.. container:: methodsection

   Example

.. container:: methodexam

   tb.toasciifmt(asciifile='myfile3.dat', headerfile='myfile3.head',
   columns=['SOURCE_ID', 'NAME', 'PROPER_MOTION'], sep=', ') will
   produce a comma separated ASCII output of the three columns
   'SOURCE_ID', 'NAME', and 'PROPER_MOTION' in file 'myfile3.dat' and a
   format description in 'myfile3.head'.
   tb.toasciifmt(asciifile='myfile.dat') will produce a space separated
   ASCII output of all table columns into file 'myfile.dat' with the
   first two lines containing a format description.

.. container:: param

   function **taql**

   .. container:: collcontent

      .. container:: methoddesc

         This method Expose TaQL to the user. Details on TaQL maybe
         found at http://www.astron.nl/aips++/docs/notes/199

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         taqlcommand : undefined = TaQL expression

      .. container:: methodparmtable

         TaQL expression

.. container:: methodsection

   Example

.. container:: methodexam

   For more information on TaQL see
   http://www.astron.nl/aips++/docs/notes/199

.. container:: param

   function **query**

   .. container:: collcontent

      .. container:: methoddesc

         Make a table from a query applied to the current table. It is
         possible to specify column(s) and/or expressions to sort on and
         to specify the columns to be contained in the output table. See
         the example below. A new "on-the-fly" table tool is returned.
         The new (reference) table can be given a name and will then be
         written to disk. Note that the resulting table is just a
         reference to the original table. One can make a deep copy of
         the query result using the copy function (see example).

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         query : undefined = String

      .. container:: methodparmtable

         Query string

.. container:: parameters2

   name : undefined

.. container:: methodparmtable

   Name of resulting reference table

.. container:: parameters2

   sortlist : undefined

.. container:: methodparmtable

   Sort string (one or more expressions separated by commas)

.. container:: parameters2

   columns : undefined

.. container:: methodparmtable

   List of column names separated by commas

.. container:: parameters2

   style : undefined

.. container:: methodparmtable

   How to handle numeric ranges and order axes

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("3C273XC1.MS") subt=tb.query("OBSERVATION_ID==0",
   sortlist="ARRAY_ID", columns="TIME, DATA, UVW") print subt.ncols() #
   23 tb.close() copyt = subt.copy ("3C273XC1_spw1.MS", True)
   subt.close() copyt.close() From the original table corresponding to
   the disk file 3C273XC1.MS, only rows with OBSERVATION\_ID equal to 0
   are selected and sorted by ARRAY\_ID. Only the columns TIME DATA UVW
   are written. Thereafter a deep copy of the result is made. This table
   query command is equivalent to the Table Query Language (TaQL)
   command SELECT TIME, DATA, UVW FROM 3C273XC1.MS WHERE
   OBSERVATION_ID==0 ORDERBY ARRAY_ID See
   http://www.astron.nl/casacore/trunk/casacore/doc/notes/199.html for
   an explanation of TaQL. If "style" is not blank, "using style \\

.. container:: param

   function **calc**

   .. container:: collcontent

      .. container:: methoddesc

         Get the result from the calculation of an expression on a table
         The expression can be any expression that can be given in the
         WHERE clause of a SELECT expression (thus including
         subqueries). The given expression determines if the result is a
         scalar, a vector, or a record containing arrays. See the
         examples below.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         expr : undefined

      .. container:: methodparmtable

         Expression string

.. container:: parameters2

   prefix : undefined = using style base0, endincl, fortranorder

.. container:: methodparmtable

   TaQL prefix for style and ordering etc ...check TaQL note 199 for
   usage

.. container:: parameters2

   showtaql : undefined = false

.. container:: methodparmtable

   Show the full taql command used

.. container:: methodsection

   Example

.. container:: methodexam

   tb.calc('[select from ngc5921.ms giving [mean(abs(DATA))]]') find the
   mean of the abs of each row of the DATA column of the MeasurementSet
   ngc5921.ms returns a (potentially enormous) record where a field
   contains the value of the expression for the row with that number.
   Note that it returns a record because for each row the expression
   results in an array. It should be clear that this example is useless.
   However, something like this could be useful for a column with (very)
   small arrays. tb.calc('[select from ngc5921.ms.contsub giving
   [ntrue(FLAG)]]') returns for each row the number of flags set. The
   result is a vector, because for each row the expression results in a
   scalar. tb.calc('sum([select from ngc5921.ms.contsub giving
   [ntrue(FLAG)]])') returns the total number of flags set in the table
   (in a single scalar). using subrow array tb.calc('median([select from
   ngc5921.ms where ANTENNA1==3 && ANTENNA2==5 giving
   [abs(DATA[0,31])]])') The above will find the median channel 31 and
   0th pol of the requested baseline formed with antennas 3 and 5. Note
   that the that the default casa order of arrays is fortran order
   ...pol axis is before channel axis tb.calc('median([select from
   ngc5921.ms where ANTENNA1==3 && ANTENNA2==5 giving [abs(DATA[31,
   0])]])', prefix='using style python') Now the same is as the above
   but using the python style of axis ordering access

.. container:: param

   function **selectrows**

   .. container:: collcontent

      .. container:: methoddesc

         Create a (reference) table containing a given subset of rows.
         It is, for instance, useful when a selection is done on another
         table containing the row numbers in the main table. It can be
         useful to apply the casapy function unique to those row
         numbers, otherwise the same row might be included multiple
         times (see example). It is possible to give a name to the
         resulting table. If given, the resulting table is made
         persistent with that table name. Otherwise the table is
         transient and disappears when closed or when casapy exits. The
         rownumbers function returns a vector containing the row number
         in the main table for each row in the selection table. Thus
         given a row number vector \\texttt{rownrs}, the following is
         always true. \\begin{verbatim} rownrs ==
         tb.selectrows(rownrs).rownumbers() \\end{verbatim} However, it
         is not true when selectrows is used on a selection table.
         because \\texttt{rownumbers} does not return the row number in
         that selection table but in the main table. \\\It means that
         one has to take great care when using \\texttt{selectrows} on a
         selection table.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         rownrs : undefined

      .. container:: methodparmtable

         0-based Row Numbers

.. container:: parameters2

   name : undefined

.. container:: methodparmtable

   Name of resulting table

.. container:: methodsection

   Example

.. container:: methodexam

   # EXAMPLE NOT VERIFIED SINCE query IS BROKEN # Do the query on the
   main table. tb.open('SOMENAME') scantable = tb.query(command) # Get
   the column containing the 0-based row numbers in the BACKEND table. #
   Make the row numbers unique. NEED TO REPLACE GLISH unique FUNCTION
   HERE! backrows = unique(scantable.getcol('NS_GBT_BACKEND_ID')) # Form
   the table subset of the BACKEND table containing those rows.
   tb.close() tb.open('SOMENAME/GBT_BACKEND') scanback =
   tb.selectrows(backrows); # Do something with that table. print
   scanback.nrows();

.. container:: param

   function **info**

   .. container:: collcontent

      .. container:: methoddesc

         The info record contains information on the table.

      .. container:: methodsection

         Parameters : None

.. container:: param

   function **putinfo**

   .. container:: collcontent

      .. container:: methoddesc

         The info record contains information on the table. It is
         written by applications, and used to determine what type of
         information is stored in a table.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         value : undefined

      .. container:: methodparmtable

         Info record

.. container:: param

   function **addreadmeline**

   .. container:: collcontent

      .. container:: methoddesc

         A readme line is part of the info record associated with a
         table. It is to inform the user, and is not used by any
         application directly.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         value : undefined

      .. container:: methodparmtable

         readme line

.. container:: param

   function **summary**

   .. container:: collcontent

      .. container:: methoddesc

         A (terse) summary of the table contents is sent to the
         defaultlogger.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         recurse : undefined = false

      .. container:: methodparmtable

         Summarize subtables recursively

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("tcal") tb.summary() # successful nomodify open of table tcal
   : 9 columns, 11 rows # Table summary: tcal # Shape: 9 columns by 11
   rows # Info: [type=Calibration, subType=T Jones, readme=] # Table
   keywords: [Type=T Jones, Interval=30, DeltaT=1] # Columns: StartTime
   StopTime Gain SolutionOK Fit FitWeight # iSolutionOK iFit iFitWeight

.. container:: param

   function **colnames**

   .. container:: collcontent

      .. container:: methoddesc

         The names of the columns in the table are returned as a vector
         of Strings.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         tb.open("tcal") tb.colnames() # StartTime StopTime Gain
         SolutionOK Fit FitWeight iSolutionOK iFit iFitWeight

.. container:: param

   function **rownumbers**

   .. container:: collcontent

      .. container:: methoddesc

         !!!NOTE INPUT PARAMETERS IGNORED!!! This function can be useful
         after a selection or a sort. It returns the row numbers of the
         rows in this table with respect to the given table. If no table
         is given, the original table is used. \\\For example: \\begin
         {verbatim} !!!NOTE INPUT PARAMETERS IGNORED!!!
         tb.open('3C273XC1.MS') t1=tb.selectrows([1,3,5,7,9])
         t1.rownumbers() # [1L, 3L, 5L, 7L, 9L] t2=t1.selectrows([2,4])
         t2.rownumbers(t1) # [2L, 4L] t2.rownumbers(tb.name()) # [5L,
         9L] t2.rownumbers() # [5L, 9L] \\end{verbatim} The last
         statements show that the function returns the row numbers
         referring to the given table. Table t2 contains rows 2 and 4 in
         table t1, which are rows 5 and 9 in table '3C273XC1.MS'. Note
         that when a table is opened using its name, that table can be a
         reference table. Thus in the example above the last 2
         statements may give different results depending on the fact if
         3C273XC1.MS is a reference table or not. \\\The function should
         always be called with a table argument. The ability of omitting
         the argument is only present for backward compatibility. The
         function can be useful to get the correct values from the
         result of a getcol or getcolslice on the original table.
         !!!NOTE INPUT PARAMETERS IGNORED!!!

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         tab : undefined

      .. container:: methodparmtable

         Table to which the row numbers refer

.. container:: parameters2

   nbytes : undefined = 0

.. container:: methodparmtable

   Maximum cache size in bytes

.. container:: methodsection

   Example

.. container:: methodexam

   !!!NOTE INPUT PARAMETERS IGNORED!!! tb.open("3C273XC1.MS") tb.nrows()
   #7669L data=tb.getcolslice("DATA", [0,0], [0,0]) data.shape #(1, 1,
   7669) selt=tb.query("ANTENNA1==1") selt.nrows() #544L print
   len(selt.rownumbers()) #544L

.. container:: param

   function **setmaxcachesize**

   .. container:: collcontent

      .. container:: methoddesc

         It can sometimes be useful to limit the size of the cache used
         by a column stored with the tiled storage manager. This
         function requires some more knowledge about the table system
         and is not meant for the casual user.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnname : undefined

      .. container:: methodparmtable

         Name of column

.. container:: parameters2

   nbytes : undefined

.. container:: methodparmtable

   Maximum cache size in bytes

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("3C273XC1.MS") tb.nrows() # 7669L tb.setmaxcachesize ("DATA",
   4*1024*1024); # True

.. container:: param

   function **isscalarcol**

   .. container:: collcontent

      .. container:: methoddesc

         A column may contain either scalars or arrays in each cell.
         This tool function tests if the specified column has scalar
         contents.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnname : undefined

      .. container:: methodparmtable

         Name of column

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("tcal") tb.isscalarcol("StartTime") # True tb.open("tcal")
   tb.isscalarcol("Gain") # False

.. container:: param

   function **isvarcol**

   .. container:: collcontent

      .. container:: methoddesc

         This functions tells if the column contains variable shaped
         arrays. If so, the function \\texttt{getvarcol} should be used
         to get the entire column. Otherwise \\texttt{getcol} can be
         used.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnname : undefined

      .. container:: methodparmtable

         Name of column

.. container:: param

   function **coldatatype**

   .. container:: collcontent

      .. container:: methoddesc

         A column may contain various data types. This tool function
         returns the type of the column as a string.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnname : undefined

      .. container:: methodparmtable

         Name of column

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("tcal") tb.coldatatype("StartTime") # double tb.open("tcal")
   tb.coldatatype("Gain") # complex

.. container:: param

   function **colarraytype**

   .. container:: collcontent

      .. container:: methoddesc

         The possible column array types are defined as:
         \\begin{description} \\item[FixedShape] FixedShape means that
         the shape of the array must be the same in each cell of the
         column. If not given, the array shape may vary. Option Direct
         forces FixedShape. \\item[Direct] Direct means that the data is
         directly stored in the table. Direct forces option FixedShape.
         If not given, the array is indirect, which implies that the
         data will be stored in a separate file. \\end{description}

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnname : undefined

      .. container:: methodparmtable

         Name of column

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("tcal") tb.colarraytype("Gain") # Direct,FixedShape

.. container:: param

   function **ncols**

   .. container:: collcontent

      .. container:: methoddesc

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         tb.open("3C273XC1.MS") tb.ncols() # 23L

.. container:: param

   function **nrows**

   .. container:: collcontent

      .. container:: methoddesc

         Note that rows are numbered starting at 0.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         tb.open("3C273XC1.MS") tb.nrows() # 7669L

.. container:: param

   function **addrows**

   .. container:: collcontent

      .. container:: methoddesc

         Rows can be added to the end of a table that was opened
         nomodify=False. The new rows are empty.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         nrow : undefined = 1

      .. container:: methodparmtable

         Number of rows to add

.. container:: param

   function **removerows**

   .. container:: collcontent

      .. container:: methoddesc

         Remove the row numbers specified in the vector from the table.
         It fails when the table does not support row removal.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         rownrs : undefined

      .. container:: methodparmtable

         Row numbers to remove

.. container:: param

   function **addcols**

   .. container:: collcontent

      .. container:: methoddesc

         Columns can be added to a table that was opened nomodify=False.
         The new columns will be filled with a default value (0 or
         blank). !!!THESE COLUMN DESCRIPTION FUNCTIONS HAVE NOT BEEN
         IMPLEMENTED!!! \\\For each column to be added a column
         description has to be setup using function
         tablecreatescalarcoldesc or tablecreatearraycoldesc. When
         multiple columns are used, they have to be combined in a single
         record using tablecreatedesc. \\\It is possible to specify data
         manager info in order to define a data manager (storage manager
         or virtual column engine) for the columns to be added.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         desc : undefined

      .. container:: methodparmtable

         Description of one or more columns

.. container:: parameters2

   dminfo : undefined

.. container:: methodparmtable

   Optional description data manager to use

.. container:: methodsection

   Example

.. container:: methodexam

   !!!REQUIRES COLUMN DESCRIPTION FUNCTIONS THAT HAVE NOT BEEN
   IMPLEMENTED!!! tb.open("mytable", nomodify=False)
   dc3=tablecreatescalarcoldesc('C3', 'a')
   dc4=tablecreatescalarcoldesc('C4', as_float(0))
   dc5=tablecreatearraycoldesc('C5', as_double(0), 2, [10,20])
   tb.addcols(dc3) # True tb.addcols(tablecreatedesc(dc4, dc5)) # True A
   single column can be added as such, but multiple columns have to be
   combined.

.. container:: param

   function **renamecol**

   .. container:: collcontent

      .. container:: methoddesc

         A column can be renamed in a table that was opened
         nomodify=False. \\\However, renaming is not possible in a
         (reference) table resulting from a select or sort operation.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         oldname : undefined

      .. container:: methodparmtable

         name of column to be renamed

.. container:: parameters2

   newname : undefined

.. container:: methodparmtable

   new name of column

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("3C273XC1.MS", nomodify=False) tb.renamecol ('DATA', 'DATA2')
   # T print tb.colnames() tb.renamecol ('DATA2', 'DATA') # T print
   tb.colnames() Column \\texttt{DATA} is renamed to \\texttt{DATA2} and
   then back to \\texttt{DATA} again..

.. container:: param

   function **removecols**

   .. container:: collcontent

      .. container:: methoddesc

         Columns can be removed from a table that was opened
         nomodify=False. \\\It may not always be possible to remove a
         column, because some data managers do not support column
         removal. However, if all columns of a data manager are removed,
         it will always succeed. It results in the removal of the entire
         data manager (and its possible files). \\\Note that function
         getdminfo can be used to find which columns are served by which
         data manager.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnames : undefined

      .. container:: methodparmtable

         names of columns to be removed

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("mytable", nomodify=False) tb.removecols ("col1 col2") # T
   print tb.colnames() Two columns are removed.

.. container:: param

   function **iscelldefined**

   .. container:: collcontent

      .. container:: methoddesc

         A column containing variable shaped arrays can have an empty
         cell (if no array has been put into it). This function tests if
         a cell is defined (thus is not empty). Note that a scalar
         column and a fixed shape array column cannot have empty cells.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnname : undefined

      .. container:: methodparmtable

         Name of column

.. container:: parameters2

   rownr : undefined = 0

.. container:: methodparmtable

   Row number, starting at 0

.. container:: param

   function **getcell**

   .. container:: collcontent

      .. container:: methoddesc

         A cell is the value at one row in one column. It may be a
         scalar or an array.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnname : undefined

      .. container:: methodparmtable

         Name of column

.. container:: parameters2

   rownr : undefined = 0

.. container:: methodparmtable

   Row number, starting at 0

.. container:: param

   function **getcellslice**

   .. container:: collcontent

      .. container:: methoddesc

         A cell is the value at one row in one column. It must be an
         array. The slice must be specified as blc, trc with an optional
         stride. \\\In blc and trc -1 can be used to indicate all values
         for a dimension (-1 in blc is equivalent to 0, so -1 is
         especially useful for trc).

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnname : undefined

      .. container:: methodparmtable

         Name of column

.. container:: parameters2

   rownr : undefined

.. container:: methodparmtable

   Row number, starting at 0

.. container:: parameters2

   blc : undefined

.. container:: methodparmtable

   Bottom left corner (e.g. [0,0,0] is start of 3D array)

.. container:: parameters2

   trc : undefined

.. container:: methodparmtable

   Top right corner

.. container:: parameters2

   incr : undefined = 1

.. container:: methodparmtable

   Stride (defaults to 1 for all axes)

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("3C273XC1.MS") data=tb.getcellslice("DATA", 0, [0,0], [1,0])
   print data.shape # [2 1]

.. container:: param

   function **getcol**

   .. container:: collcontent

      .. container:: methoddesc

         The entire column (or part of it) is returned. Warning: it
         might be big! The functions can only be used if all arrays in
         the column have the same shape. That is guaranteed for columns
         containing scalars or fixed shaped arrays. For columns
         containing variable shaped arrays it only succeeds if all those
         arrays happen to have the same shape. \\\Note that function
         \\texttt{getvarcol} can be used to get a column of arbitrary
         shaped arrays, which also handles empty cells correctly.
         Function \\texttt{isvarcol} tells if a column contains variable
         shaped arrays. shaped

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnname : undefined

      .. container:: methodparmtable

         Name of column

.. container:: parameters2

   startrow : undefined = 0

.. container:: methodparmtable

   First row to read (default 0)

.. container:: parameters2

   nrow : undefined = -1

.. container:: methodparmtable

   Number of rows to read (default -1 means till the end)

.. container:: parameters2

   rowincr : undefined = 1

.. container:: methodparmtable

   Increment in rows to read (default 1)

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("3C273XC1.MS") # True gain=tb.getcol("DATA") print gain.shape
   # (4, 1, 7669)

.. container:: param

   function **getvarcol**

   .. container:: collcontent

      .. container:: methoddesc

         Function \\texttt{getcol} can only used if values in the column
         cells to get have the same shape. Function \\texttt{getvarcol}
         addresses this limitation by returning the values as a record
         instead of an array. Each field in the record contains the
         value for a column cell. If the value is undefined (i.e. the
         cell does not contain a value), the unset value is put in the
         record. Each field name is the letter r followed by the row
         number. The length of the record is the number of rows to get.
         \\\Note that the function \\texttt{isvarcol} tells if a column
         contains variable shaped arrays.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnname : undefined

      .. container:: methodparmtable

         Name of column

.. container:: parameters2

   startrow : undefined = 0

.. container:: methodparmtable

   First row to read (default 0)

.. container:: parameters2

   nrow : undefined = -1

.. container:: methodparmtable

   Number of rows to read (default -1 means till the end)

.. container:: parameters2

   rowincr : undefined = 1

.. container:: methodparmtable

   Increment in rows to read (default 1)

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("3C273XC1.MS") gain=tb.getvarcol("DATA") print len(gain) #
   7669

.. container:: param

   function **getcolslice**

   .. container:: collcontent

      .. container:: methoddesc

         A slice from the entire column (or part of it) is returned.
         Warning: it might be big! \\\In blc and trc -1 can be used to
         indicate all values for a dimension (-1 in blc is equivalent to
         1, so -1 is especially useful for trc). Note that blc and trc
         should not contain the row number, only the blc and trc of the
         arrays in the column.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnname : undefined

      .. container:: methodparmtable

         Name of column

.. container:: parameters2

   blc : undefined

.. container:: methodparmtable

   Bottom left corner (e.g. [0,0,0] is start of 3D array)

.. container:: parameters2

   trc : undefined

.. container:: methodparmtable

   Top right corner

.. container:: parameters2

   incr : undefined

.. container:: methodparmtable

   Stride (defaults to 1 for all axes)

.. container:: parameters2

   startrow : undefined = 0

.. container:: methodparmtable

   First row to read (default 0)

.. container:: parameters2

   nrow : undefined = -1

.. container:: methodparmtable

   Number of rows to read (default -1 means till the end)

.. container:: parameters2

   rowincr : undefined = 1

.. container:: methodparmtable

   Increment in rows to read (default 1)

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("3C273XC1.MS") data=tb.getcolslice("DATA", [0,0], [1,0])
   data.shape # (2 1 7669)

.. container:: param

   function **putcell**

   .. container:: collcontent

      .. container:: methoddesc

         A cell is the the value at one row in one column. It may be a
         scalar or an array.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnname : undefined

      .. container:: methodparmtable

         Name of column

.. container:: parameters2

   rownr : undefined

.. container:: methodparmtable

   Row number(s) (0-relative)

.. container:: parameters2

   thevalue : any

.. container:: methodparmtable

   Value

.. container:: param

   function **putcellslice**

   .. container:: collcontent

      .. container:: methoddesc

         A cell is the value at one row in one column. It must be an
         array. The slice must be specified as blc, trc with an optional
         stride. \\\In blc and trc -1 can be used to indicate all values
         for a dimension (-1 in blc is equivalent to 0, so -1 is
         especially useful for trc).

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnname : undefined

      .. container:: methodparmtable

         Name of column

.. container:: parameters2

   rownr : undefined

.. container:: methodparmtable

   Row number, starting at 0

.. container:: parameters2

   value : any

.. container:: methodparmtable

   Value

.. container:: parameters2

   blc : undefined

.. container:: methodparmtable

   Bottom left corner (e.g. [0,0,0] is start of 3D array)

.. container:: parameters2

   trc : undefined

.. container:: methodparmtable

   Top right corner

.. container:: parameters2

   incr : undefined = 1

.. container:: methodparmtable

   Stride (defaults to 1 for all axes)

.. container:: param

   function **putcol**

   .. container:: collcontent

      .. container:: methoddesc

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnname : undefined

      .. container:: methodparmtable

         Name of column

.. container:: parameters2

   value : any

.. container:: methodparmtable

   Array

.. container:: parameters2

   startrow : undefined = 0

.. container:: methodparmtable

   First row to put (default 0)

.. container:: parameters2

   nrow : undefined = -1

.. container:: methodparmtable

   Number of rows to put (default -1 means till the end)

.. container:: parameters2

   rowincr : undefined = 1

.. container:: methodparmtable

   Increment in rows to put (default 1)

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("3C273XC1.MS",nomodify=False) data=tb.getcol("DATA") # [could
   modify data here] tb.putcol("DATA", data) tb.flush()

.. container:: param

   function **putvarcol**

   .. container:: collcontent

      .. container:: methoddesc

         \\texttt{putcol} can only used if values in the column cells to
         put have the same shape. \\texttt{putvarcol} addresses this
         limitation by passing the values as a record instead of an
         array. Each field in the record contains the value for a column
         cell. So the length of the record has to match the number of
         rows to put. If a value is the unset value, no put is done for
         that row.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnname : undefined

      .. container:: methodparmtable

         Name of column

.. container:: parameters2

   value : undefined

.. container:: methodparmtable

   Record with values

.. container:: parameters2

   startrow : undefined = 0

.. container:: methodparmtable

   First row to put (default 0)

.. container:: parameters2

   nrow : undefined = -1

.. container:: methodparmtable

   Number of rows to put (default -1 means till the end)

.. container:: parameters2

   rowincr : undefined = 1

.. container:: methodparmtable

   Increment in rows to put (default 1)

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("3C273XC1.MS",nomodify=False) gain=tb.getvarcol("DATA", 0,
   10) tb.putvarcol("Gain", gain, 10, 10) tb.flush() This example copies
   the values from row 0-9 to row 10-19.

.. container:: param

   function **putcolslice**

   .. container:: collcontent

      .. container:: methoddesc

         In blc and trc, -1 can be used to indicate all values for a
         dimension (-1 in blc is equivalent to 0, so -1 is especially
         useful for trc). Note that blc and trc should not contain the
         row number, only the blc and trc of the arrays in the column.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnname : undefined

      .. container:: methodparmtable

         Name of column

.. container:: parameters2

   value : any

.. container:: methodparmtable

   Array

.. container:: parameters2

   blc : undefined

.. container:: methodparmtable

   Bottom left corner (e.g. [0,0,0] is start of 3D array)

.. container:: parameters2

   trc : undefined

.. container:: methodparmtable

   Top right corner

.. container:: parameters2

   incr : undefined = 1

.. container:: methodparmtable

   Stride (defaults to 1 for all axes)

.. container:: parameters2

   startrow : undefined = 0

.. container:: methodparmtable

   First row to put (default 0)

.. container:: parameters2

   nrow : undefined = -1

.. container:: methodparmtable

   Number of rows to put (default -1 means till the end)

.. container:: parameters2

   rowincr : undefined = 1

.. container:: methodparmtable

   Increment in rows to put (default 1)

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("3C273XC1.MS",nomodify=False) data_all=tb.getcolslice("DATA",
   [-1,-1], [-1,=1]) print data_all.shape # (4, 1, 7669)
   data=tb.getcolslice("DATA", [0,0],[3,0]) # can modify data here
   tb.putcolslice("DATA", data, [0,0],[3,0]) tb.flush()

.. container:: param

   function **getcolshapestring**

   .. container:: collcontent

      .. container:: methoddesc

         The shapes of the arrays in the entire column (or part of it)
         are returned as strings like [20,3]. When the column contains
         fixed shaped arrays, a single string is returned. Otherwise a
         vector of strings is returned.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnname : undefined

      .. container:: methodparmtable

         Name of column

.. container:: parameters2

   startrow : undefined = 0

.. container:: methodparmtable

   First row to read (default 0)

.. container:: parameters2

   nrow : undefined = -1

.. container:: methodparmtable

   Number of rows to read (default -1 means till the end)

.. container:: parameters2

   rowincr : undefined = 1

.. container:: methodparmtable

   Increment in rows to read (default 1)

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("3C273XC1.MS") shapes=tb.getcolshapestring("DATA")) print
   len(shapes)

.. container:: param

   function **getkeyword**

   .. container:: collcontent

      .. container:: methoddesc

         The value of the given table keyword is returned. The value can
         be of any type, including a record and a table. \\\If a keyword
         is a table, its value is returned as a string containing the
         table name prefixed by 'Table: '. \\\It is possible that the
         value of a keyword is a record itself (arbitrarily deeply
         nested). A field in such a subrecord can be read by separating
         the name with dots.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         keyword : any

      .. container:: methodparmtable

         Name or seqnr of keyword: string or int

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open('3C273XC1.MS') tb.getkeywords() tb.getkeyword('MS_VERSION') #
   2.0 tb.close() tb.open('tcal') tb.getkeyword('rec.fld') # get field
   from a record # 3.14

.. container:: param

   function **getkeywords**

   .. container:: collcontent

      .. container:: methoddesc

         The values of all table keywords are returned. The values can
         be of any type, including a record and a table. \\\If a keyword
         is a table, its value is returned as a string containing the
         table name prefixed by 'Table: '.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         tb.open('3C273XC1.MS') tb.getkeywords() #{'ANTENNA': 'Table:
         /home/aips2mgr/testing/3C273XC1.MS/ANTENNA', #
         'DATA_DESCRIPTION': 'Table:
         /home/aips2mgr/testing/3C273XC1.MS/DATA_DESCRIPTION', # 'FEED':
         'Table: /home/aips2mgr/testing/3C273XC1.MS/FEED', # 'FIELD':
         'Table: /home/aips2mgr/testing/3C273XC1.MS/FIELD', #
         'FLAG_CMD': 'Table:
         /home/aips2mgr/testing/3C273XC1.MS/FLAG_CMD', # 'HISTORY':
         'Table: /home/aips2mgr/testing/3C273XC1.MS/HISTORY', #
         'MS_VERSION': 2.0, # 'OBSERVATION': 'Table:
         /home/aips2mgr/testing/3C273XC1.MS/OBSERVATION', # 'POINTING':
         'Table: /home/aips2mgr/testing/3C273XC1.MS/POINTING', #
         'POLARIZATION': 'Table:
         /home/aips2mgr/testing/3C273XC1.MS/POLARIZATION', #
         'PROCESSOR': 'Table:
         /home/aips2mgr/testing/3C273XC1.MS/PROCESSOR', # 'SOURCE':
         'Table: /home/aips2mgr/testing/3C273XC1.MS/SOURCE', #
         'SPECTRAL_WINDOW': 'Table:
         /home/aips2mgr/testing/3C273XC1.MS/SPECTRAL_WINDOW', # 'STATE':
         'Table: /home/aips2mgr/testing/3C273XC1.MS/STATE'}

.. container:: param

   function **getcolkeyword**

   .. container:: collcontent

      .. container:: methoddesc

         The value of the given column keyword is returned. The value
         can be of any type, including a record and a table. \\\If a
         keyword is a table, its value is returned as a string
         containing the table name prefixed by 'Table: '. \\\It is
         possible that the value of a keyword is a record itself
         (arbitrarily deeply nested). A field in such a subrecord can be
         read by separating the name with dots.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnname : undefined

      .. container:: methodparmtable

         Name of column

.. container:: parameters2

   keyword : any

.. container:: methodparmtable

   Name or seqnr of keyword: string or int

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("3C273XC1.MS") tb.getcolkeyword("UVW", "QuantumUnits")
   #array(['m', 'm', 'm'], # dtype='|S2')

.. container:: param

   function **getcolkeywords**

   .. container:: collcontent

      .. container:: methoddesc

         The values of all keywords for the given column are returned.
         The values can be of any type, including a record and a table.
         \\\If a keyword is a table, its value is returned as a string
         containing the table name prefixed by 'Table: '.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnname : undefined

      .. container:: methodparmtable

         Name of column

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("3C273XC1.MS") tb.getcolkeywords("UVW") #{'MEASINFO': {'Ref':
   'ITRF', 'type': 'uvw'}, # 'QuantumUnits': array(['m', 'm', 'm'], #
   dtype='|S2')}

.. container:: param

   function **putkeyword**

   .. container:: collcontent

      .. container:: methoddesc

         Put a table keyword. The value of the keyword can be a scalar
         or an array of any type or it can be a record. \\\It is
         possible to define a keyword holding a subtable. In that case a
         special string containing the name of the subtable will be
         passed to the table client. \\\It is possible that the value of
         a keyword is a record itself (arbitrarily deeply nested). A
         field in such a subrecord can be written by separating the name
         with dots. If a subrecord does not exist, an error is returned
         unless \\texttt{makesubrecord=True} is given. In such a case
         intermediate records are created when needed.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         keyword : any

      .. container:: methodparmtable

         Name or seqnr of keyword: string or int

.. container:: parameters2

   value : any

.. container:: methodparmtable

   Value of keyword

.. container:: parameters2

   makesubrecord : undefined = false

.. container:: methodparmtable

   Create intermediate records

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("3C273XC1.MS", nomodify=False) tb.putkeyword("VERSION",
   "1.66") # True # define ANTENNA subtable tb.putkeyword("ANTENNA",
   'Table: 3C273XC1.MS/ANTENNA') tb.flush() # True # write a field in a
   record and create subrecords when needed tb.putkeyword("REC.SUB.FLD",
   "val", True) # True # write a keyword with a record value
   tb.putkeyword("REC", {'SUB': {'FLD': 'val'}}) # True Note that the
   last example does the same as the previous one (assuming that
   \\texttt{REC} does not exist yet with other fields).

.. container:: param

   function **putkeywords**

   .. container:: collcontent

      .. container:: methoddesc

         Put multiple table keywords. All fields in the given record are
         put as table keywords. The value of each field can be a scalar
         or an array of any type or it can be a record. \\\It is also
         possible to define a keyword holding a subtable. This can be
         done by giving the keyword a string value consisting of the
         subtable name prefixed by 'Table: '.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         value : undefined

      .. container:: methodparmtable

         Record of keyword=value pairs

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open('3C273XC1.MS', nomodify=False) kw=tb.getkeywords() print
   kw['MS_VERSION'] # 2.0 kw['MS_VERSION']=2.1 tb.putkeywords(kw) #
   !!!BROKEN. Keywords containing float are not handled properly!!!
   tb.flush() # True

.. container:: param

   function **putcolkeyword**

   .. container:: collcontent

      .. container:: methoddesc

         Put a keyword in the given column. The value of the keyword can
         be a scalar or an array of any type or it can be a record.
         \\\It is possible to define a keyword holding a subtable. In
         that case a special string containing the name of the subtable
         will be passed to the table client. \\\It is possible that the
         value of a keyword is a record itself (arbitrarily deeply
         nested). A field in such a subrecord can be written by
         separating the name with dots. If a subrecord does not exist,
         an error is returned unless \\texttt{makesubrecord=True} is
         given. In such a case intermediate records are created when
         needed.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnname : undefined

      .. container:: methodparmtable

         Name of column

.. container:: parameters2

   keyword : any

.. container:: methodparmtable

   Name or seqnr of keyword,string or int

.. container:: parameters2

   value : any

.. container:: methodparmtable

   Value of keyword

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("3C273XC1.MS", nomodify=False)
   ckw=tb.getcolkeyword("UVW","QuantumUnits") print ckw # modify ckw as
   desired tb.putcolkeyword("UVW","QuantumUnits",ckw) # True tb.flush()
   # True

.. container:: param

   function **putcolkeywords**

   .. container:: collcontent

      .. container:: methoddesc

         Put multiple keywords in the given column. All fields in the
         given record are put as column keywords. The value of each
         field can be a scalar or an array of any type or it can be a
         record. \\\It is also possible to define a keyword holding a
         subtable. This can be done by giving the keyword a string value
         consisting of the subtable name prefixed by 'Table: '.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnname : undefined

      .. container:: methodparmtable

         Name of column

.. container:: parameters2

   value : undefined

.. container:: methodparmtable

   Record of keyword=value pairs

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("3C273XC1.MS", nomodify=False) kws = tb.getcolkeywords("UVW")
   kws #{'MEASINFO': {'Ref': 'ITRF', 'type': 'uvw'}, # 'QuantumUnits':
   array(['m', 'm', 'm'], # dtype='|S2')} kws['MEASINFO']['Ref']='B1950'
   tb.putcolkeywords(kws) # True

.. container:: param

   function **removekeyword**

   .. container:: collcontent

      .. container:: methoddesc

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         keyword : any

      .. container:: methodparmtable

         Name or seqnr of keyword: string or int

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("3C273XC1.MS", nomodify=False) tb.removekeyword("MS_VERSION")
   # True tb.flush() # True

.. container:: param

   function **removecolkeyword**

   .. container:: collcontent

      .. container:: methoddesc

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnname : undefined

      .. container:: methodparmtable

         Name of column

.. container:: parameters2

   keyword : any

.. container:: methodparmtable

   Name or seqnr of keyword: string or int

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("3C273XC1.MS", nomodify=False) tb.removecolkeyword("UVW",
   "QuantumUnits") # True tb.flush() # True

.. container:: param

   function **getdminfo**

   .. container:: collcontent

      .. container:: methoddesc

         This function returns the types and names of the data managers
         used. For each data manager it also returns the names of the
         columns served by it. The information is returned as a record
         containing a subrecord for each data manager. Each subrecord
         contains the fields TYPE, NAME and COLUMNS.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         tb.open('3C273XC1.MS') rec = tb.getdminfo() Print the output
         record shows that the table uses 9 storage managers.

.. container:: param

   function **keywordnames**

   .. container:: collcontent

      .. container:: methoddesc

         This function returns a vector of strings containing the names
         of all table keywords.

      .. container:: methodsection

         Parameters : None

.. container:: param

   function **fieldnames**

   .. container:: collcontent

      .. container:: methoddesc

         This function returns a vector of strings containing the names
         of all fields in the given table keyword. It is only valid if
         the keyword value is a record. \\\If no keyword name is given,
         the names of all table keywords are returned.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         keyword : undefined

      .. container:: methodparmtable

         keyword name

.. container:: param

   function **colkeywordnames**

   .. container:: collcontent

      .. container:: methoddesc

         This function returns a vector of strings containing the names
         of all keywords in the column with the given name..

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnname : undefined

      .. container:: methodparmtable

         column name

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open('3C273XC1.MS') tb.colkeywordnames("UVW")

.. container:: param

   function **colfieldnames**

   .. container:: collcontent

      .. container:: methoddesc

         This function returns a vector of strings containing the names
         of all fields in the given keyword in the given column. It is
         only valid if the keyword value is a record. \\\If no keyword
         name is given, the names of all keywords in the column are
         returned.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnname : undefined

      .. container:: methodparmtable

         column name

.. container:: parameters2

   keyword : undefined

.. container:: methodparmtable

   keyword name

.. container:: param

   function **getdesc**

   .. container:: collcontent

      .. container:: methoddesc

         The table description is a casapy record that contains a
         complete description of the layout of the table (except for the
         number of rows). \\\\ By default the actual table description
         is returned (thus telling the actual shapes and data managers
         used). It is also possible to get the table description used
         when creating the table.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         actual : undefined = true

      .. container:: methodparmtable

         actual table description?

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("3C273XC1.MS") tb.getdesc()

.. container:: param

   function **getcoldesc**

   .. container:: collcontent

      .. container:: methoddesc

         The column description is a casapy record that contains a
         complete description of the layout of a specified column
         (except for the number of rows). It can be used to construct a
         table description.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columnname : undefined

      .. container:: methodparmtable

         Name of column

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("3C273XC1.MS") tb.getcoldesc("DATA") #{'comment': 'The data
   column', # 'dataManagerGroup': 'TiledData', # 'dataManagerType':
   'TiledShapeStMan', # 'maxlen': 0, # 'ndim': 2, # 'option': 0, #
   'valueType': 'complex'}

.. container:: param

   function **ok**

   .. container:: collcontent

      .. container:: methoddesc

         Perform a number of sanity checks and return T if ok. Failure
         (returning F) is a sign of a bug.

      .. container:: methodsection

         Parameters : None

.. container:: param

   function **clearlocks**

   .. container:: collcontent

      .. container:: methoddesc

         Occasionally a table will be inretrievably locked to another
         process no matter how much closing is done. So clearLocks will
         unlock all the files in the table cache that use AutoLocking.

      .. container:: methodsection

         Parameters : None

.. container:: param

   function **listlocks**

   .. container:: collcontent

      .. container:: methoddesc

         Occasionally a table will be inretrievably locked to another
         process no matter how much closing is done. So listLocks will
         list the offending tables (and unoffending ones, too), so we
         can figure out where the problem might be.

      .. container:: methodsection

         Parameters : None

.. container:: param

   function **statistics**

   .. container:: collcontent

      .. container:: methoddesc

         This function computes descriptive statistics on the table
         column. It returns the statistical values as a dictionary. The
         given column name must be a numerical column. If it is a
         complex valued column, the parameter complex\_value defines
         which derived real value is used for the statistics
         computation.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         column : undefined

      .. container:: methodparmtable

         Column name

.. container:: parameters2

   complex_value : undefined

.. container:: methodparmtable

   Which derived value to use for complex columns (amp, amplitude,
   phase, imag, real, imaginary)

.. container:: parameters2

   useflags : undefined = true

.. container:: methodparmtable

   Use the data flags

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("ggtau.1mm.amp.gcal") s = tb.statistics(column="GAIN",
   complex_value="phase")

.. container:: param

   function **showcache**

   .. container:: collcontent

      .. container:: methoddesc

         Show the contents of the table cache.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         verbose : undefined = true

      .. container:: methodparmtable

.. container:: methodsection

   Example

.. container:: methodexam

   tb.showcache()

.. container:: param

   function **testincrstman**

   .. container:: collcontent

      .. container:: methoddesc

         Checks consistency of an Incremental Store Manager bucket
         layout In case of corruption it returns False and a SEVERE msg
         is posted containing information about the location of the
         corrupted bucket

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         column : undefined

      .. container:: methodparmtable

         Column name

.. container:: methodsection

   Example

.. container:: methodexam

   mytb = tbtool() mytb.open('uid___A002_X841035_X203.ms.split')
   mytb.testincrstman('FLAG_ROW')

.. container:: section
   :name: viewlet-below-content-body
