.. container::
   :name: viewlet-above-content-title

listcal
=======

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task description

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      This task lists antenna gain solutions in tabular form. The table
      is organized as follows. Solutions are output by

      #. Spectral window
      #. Antenna
      #. Time
      #. Channel
      #. and Polarization

      where the inner-most loop is over polarization.

      | The **listcal** output table contains two table headers. The
        top-level header is printed each time the spectral window
        changes. This header lists
      | the spectral window ID (SpwID), the date of observation (Date),
        the calibration table name (CalTable), and the measurement set
        name (MS name). 

      A lower-level header is printed when the top-level header is
      printed, when the antenna names change, and for every *pagerows*
      of output. The lower-level header columns are described here:

      =========== ===================================================
      Column name Description
      Ant         Antenna name (contains sub-columns: Amp, Phs, F)
      Time        Visibility timestamp corresponding to gain solution
      Field       Field name
      Chn         Channel number
      Amp         Complex solution amplitude
      Phs         Complex solution phase
      F           Flag
      =========== ===================================================

      Elements of the "F" column contain an 'F' when the datum is
      flagged, and '' (whitespace) when the datum is not flagged.
      Presently, the polarization mode names (for example: R, L) are not
      given, but the ordering of the polarization modes (left-to-right)
      is equivalent to the order output by task **listobs** (see "Feeds"
      in **listobs** output).

       

      .. rubric:: Parameter descriptions
         :name: parameter-descriptions

      .. rubric:: *vis*
         :name: vis

      Name of input visibility file. Default: none. Examples:
      *vis='ngc5921.ms'*

      .. rubric:: *caltable*
         :name: caltable

      Name of input calibration table. Default: none. Examples:
      *caltable='ngc5921.gcal'*

      .. rubric:: *field*
         :name: field

      Select data based on field ID(s) or name(s). Default: '' => all.
      Examples: *field='1'*; *field='0~2'* field IDs inclusive from 0 to
      2; *field='3C*'* all field names starting with 3C

      .. rubric:: *antenna*
         :name: antenna

      Select calibration data based on antenna. Default: '' => all.
      Examples: *antenna='5'*; *antenna='5,6'* antenna index 5 and 6
      solutions; *antenna='VA05','VA06'* VLA antenna 5 and 6

      .. rubric:: *spw*
         :name: spw

      Select spectral window, channel to list. Default: '' => all spws
      and channels. Examples: *spw='2:34'* spectral window 2, channel 34
      (will only list one spw, one channel at a time)

      .. rubric:: *listfile*
         :name: listfile

      Write output to disk (will not overwrite). Default: '' => write to
      screen

      .. rubric:: *pagerows*
         :name: pagerows

      Rows per page of listing. Default: 50; *pagerows=0* => do not
      paginate

       

.. container:: section
   :name: viewlet-below-content-body


.. toctree::
   :hidden:
   :maxdepth: 3

   task_listcal/about
   task_listcal/parameters
   task_listcal/changelog
   task_listcal/examples
   task_listcal/developer