.. container::
   :name: viewlet-above-content-title

Basics MeasurementSet
=====================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Description of the CASA UV Data Format

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Data is handled in CASA via the table system. In particular,
      visibility data are stored in a CASA table known as a
      MeasurementSet (MS). Details of the physical and logical MS
      structure are given below, but for our purposes here an MS is just
      a construct that contains the data. An MS can also store single
      dish data (as an auto-correlation-only data set), see
      "`Single-dish data calibration and
      reduction <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/single-dish-calibration/single-dish-data-calibration-and-reduction>`__".

      A full description of the MeasurementSet can be found
      `here <https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals/measurement-set>`__,
      and a description of the MS model column can be found in the
      `Synthesis
      Calibration <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration>`__
      section.

      .. container:: info-box

         Inside the Toolkit: MeasurementSets are handled in the ms tool.
         Import and export methods include ms.fromfits and ms.tofits.

      .. container:: info-box

         NOTE: Images are handled through special image tables, although
         standard FITS I/O is also supported. Images and image data are
         described in "\ `Dealing with
         Images" <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/dealing-with-images>`__\ .

      The headers of any FITS files can be displayed in the logger with
      the **listfits** task:

      .. container:: casa-input-box

         | # listfits :: List the HDU and typical data rows of a fits
           file:
         | fitsfile = '' # Name of input fits file

      More Information on how to access Visibility Data is provided in
      the "`Data Examination and
      Editing <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing>`__"
      chapter.

      Unless your data was previously processed by CASA, you will need
      to import it into CASA as an MS. Supported formats include some
      “standard” flavors of UVFITS, the VLA “Export” archive format, and
      most recently, the ALMA Science Data Model (ASDM) format. These
      are described in "`UV Data
      Import <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/visibility-data-import-export/uv-data-import>`__".

      Once in MeasurementSet form, your data can be accessed through
      various tools and tasks with a common interface. The most
      important of these is the `data
      selection <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__
      interface, which allows you to specify the subset of the data on
      which the tasks and tools will operate.

       

      .. rubric:: Under the Hood: Structure of the MeasurementSet
         :name: sec92

      .. container:: info-box

         Inside the Toolkit: Generic CASA tables are handled in the tb
         tool. You have direct access to keywords, rows and columns of
         the tables with the methods of this tool.

      It is not necessary that a casual CASA user know the specific
      details on how the data in the MS is stored and the contents of
      all the sub-tables. However, CASA docs occasionally refers to
      specific “columns” of the MS when describing the actions of
      various tasks, and thus we provide the following synopsis to
      familiarize the user with the necessary nomenclature.

      All CASA data files, including MeasurementSets, are written into
      the current working directory by default, with each CASA table
      represented as a separate sub-directory. MS names therefore need
      only comply with UNIX file or directory naming conventions, and
      can be referred to from within CASA directly, or via full path
      names.

      An MS consists of a *MAIN* table containing the visibility data
      and associated sub-tables containing auxiliary or secondary
      information. The tables are logical constructs, with contents
      located in the physical table.\* files on disk. The *MAIN* table
      consists of the table.\* files in the main directory of the
      MS-file itself, and the other tables are in the respective
      subdirectories. The various MS tables and sub-tables can be seen
      by listing the contents of the MS directory itself (e.g. using
      Unix ls), or via the **browsetable** task.

      See figure 1 for an example of the contents of a MS directory. Or,
      from the casa prompt,

      .. container:: casa-input-box

         | CASA <1>: ls ngc5921.ms #IPython system call: ls -F
           ngc5921.ms
         | ANTENNA           POLARIZATION     table.f1       
           table.f3_TSM1  table.f8
         | DATA_DESCRIPTION  PROCESSOR        table.f10      
           table.f4       table.f8_TSM1
         | FEED              SORTED_TABLE     table.f10_TSM1 
           table.f5       table.f9
         | FIELD             SOURCE           table.f11      
           table.f5_TSM1  table.f9_TSM1
         | FLAG_CMD          SPECTRAL_WINDOW  table.f11_TSM1 
           table.f6       table.info
         | HISTORY           STATE            table.f2       
           table.f6_TSM0  table.lock
         | OBSERVATION       table.dat        table.f2_TSM1   table.f7
         | POINTING          table.f0         table.f3       
           table.f7_TSM1

      .. container:: info-box

         NOTE: The MAIN table information is contained in the table.\*
         files in this directory.

      Each of the sub-table sub-directories contain their own table.dat
      and other files, e.g.

      .. container:: casa-input-box

         | CASA <2>: ls ngc5921.ms/SOURCE #IPython system call: ls -F
           ngc5921.ms/SOURCE
         | table.dat  table.f0  table.f0i  table.info  table.lock

      ..

         .. container::

            |image1|

         .. container::

            +---------+-----------------------------------------------------------+
            | Type    | Figure                                                    |
            +---------+-----------------------------------------------------------+
            | ID      | imex-ms-content                                           |
            +---------+-----------------------------------------------------------+
            | Caption | Figure 1: The contents of a MeasurementSet. These tables  |
            |         | compose a MeasurementSet named ngc5921.demo.ms on disk.   |
            |         | This display is obtained by using the File:Open menu in   |
            |         | browsetable and left double-clicking on the               |
            |         | ngc5921.demo.ms directory.                                |
            +---------+-----------------------------------------------------------+

         .. container::

             

      Each “row” in a table contains entries for a number of specified
      “columns”. For example, in the *MAIN* table of the MS, the
      original visibility data is contained in the *DATA* column — each
      “cell” contains a matrix of observed complex visibilities for that
      row at a single time stamp, for a single baseline in a single
      spectral window. The shape of the data matrix is given by the
      number of channels and the number of correlations
      (voltage-products) formed by the correlator for an array.

      Table 1 lists the non-data columns of the *MAIN* table that are
      most important during a typical data reduction session. Table 2 at
      the bottom lists the key data columns of the *MAIN* table of an
      interferometer MS. The MS produced by fillers for specific
      instruments may insert special columns, such as *ALMA_PHASE_CORR*,
      *ALMA_NO_PHAS_CORR* and *ALMA_PHAS_CORR_FLAG_ROW* for ALMA data
      filled using the **importasdm** filler. These columns are visible
      in **browsetable** and are accessible from the toolkit in the
      **ms** tool (e.g. the **ms.getdata** method) and from the **tb**
      “table” tool (e.g. using **tb.getcol**).

      .. container:: info-box

         NOTE: When you examine table entries for IDs such as FIELD_ID
         or DATA_DESC_ID, you will see 0-based numbers.

       

      +-------------------+-------------------------------------------------+
      | Parameter         | Contents                                        |
      +===================+=================================================+
      | *ANTENNA1*        | First antenna in baseline                       |
      +-------------------+-------------------------------------------------+
      | *ANTENNA2*        | Second antenna in baseline                      |
      +-------------------+-------------------------------------------------+
      | *FIELD_ID*        | Field (source no.) identification               |
      +-------------------+-------------------------------------------------+
      | *DATA_DESC_ID*    | Spectral window number, polarization identifier |
      |                   | pair (IF no.)                                   |
      +-------------------+-------------------------------------------------+
      | *ARRAY_ID*        | Subarray number                                 |
      +-------------------+-------------------------------------------------+
      | *OBSERVATION_ID*  | Observation identification                      |
      +-------------------+-------------------------------------------------+
      | *POLARIZATION_ID* | Polarization identification                     |
      +-------------------+-------------------------------------------------+
      | *SCAN_NUMBER*     | Scan number                                     |
      +-------------------+-------------------------------------------------+
      | *TIME*            | Integration midpoint time                       |
      +-------------------+-------------------------------------------------+
      | *UVW*             | UVW coordinates                                 |
      +-------------------+-------------------------------------------------+

      .. container::

         ======= ======================================================
         Type    Table
         ID      imex-tab-mscolumns
         Caption Table 1: Common columns in the *MAIN* table of the MS.
         ======= ======================================================

      .. container::

          

      The MS can contain a number of “scratch” columns, which are used
      to hold useful versions of other columns such as the data or
      weights for further processing. The most common scratch columns
      are:

      -  *CORRECTED_DATA* — used to hold calibrated data for imaging or
         display;
      -  *MODEL_DATA* — holds the Fourier inversion of a particular
         model image for calibration or imaging. This column is
         optional.

      The creation and use of the scratch columns is generally done
      behind the scenes, but you should be aware that they are there
      (and when they are used).

       

      +------------------------+-----------------+------------------------+
      | Column                 | Format          | Contents               |
      +========================+=================+========================+
      | *DATA*                 | Complex(Nc, Nf) | complex visibility     |
      |                        |                 | data matrix (=         |
      |                        |                 | ALMA_PHASE_CORR by     |
      |                        |                 | default)               |
      +------------------------+-----------------+------------------------+
      | *FLAG*                 | Bool(Nc, Nf)    | cumulative data flags  |
      +------------------------+-----------------+------------------------+
      | *WEIGHT*               | Float(Nc)       | weight for a row       |
      +------------------------+-----------------+------------------------+
      | *SIGMA*                | Float(Nc)       | sigma for a row        |
      +------------------------+-----------------+------------------------+
      | *WEIGHT_SPECTRUM*      | Float(Nc, Nf)   | individual weights for |
      |                        |                 | a data matrix          |
      +------------------------+-----------------+------------------------+
      | *SIGMA_SPECTRUM*       | Float(Nc, Nf)   | individual sigmas for  |
      |                        |                 | a data matrix          |
      +------------------------+-----------------+------------------------+
      | *ALMA_PHASE_CORR*      | Complex(Nc, Nf) | on-line phase          |
      |                        |                 | corrected data (Not in |
      |                        |                 | VLA data)              |
      +------------------------+-----------------+------------------------+
      | *ALMA_NO_PHAS_CORR*    | Bool(Nc, Nf)    | data that has not been |
      |                        |                 | phase corrected (Not   |
      |                        |                 | in VLA data)           |
      +------------------------+-----------------+------------------------+
      | *AL                    | Bool(Nc, Nf)    | flag to use            |
      | MA_PHAS_CORR_FLAG_ROW* |                 | phase-corrected data   |
      |                        |                 | or not (not in VLA     |
      |                        |                 | data)                  |
      +------------------------+-----------------+------------------------+
      | *MODEL_DATA*           | Complex(Nc, Nf) | Scratch: created by    |
      |                        |                 | calibrater or imager   |
      |                        |                 | tools                  |
      +------------------------+-----------------+------------------------+
      | *CORRECTED_DATA*       | Complex(Nc, Nf) | Scratch: created by    |
      |                        |                 | calibrater or imager   |
      |                        |                 | tools                  |
      +------------------------+-----------------+------------------------+

      +---------+-----------------------------------------------------------+
      | Type    | Table                                                     |
      +---------+-----------------------------------------------------------+
      | ID      | imex-tab-msmaintable                                      |
      +---------+-----------------------------------------------------------+
      | Caption | Table 2: Commonly accessed *MAIN* Table data-related      |
      |         | columns. **NOTE**: The columns *ALMA_PHASE_CORR,          |
      |         | ALMA_NO_PHAS_CORR and ALMA_PHAS_CORR_FLAG_ROW* are        |
      |         | specific to ALMA data filled using the **importasdm**     |
      |         | filler.                                                   |
      +---------+-----------------------------------------------------------+

      .. container::

          

      Data flags can be set in the MS, too. Whenever a flag is set, the
      data will be ignored in all processing steps but not physically
      deleted from the MS. The flags are channel-based and stored in the
      MS *FLAG* subtable. Backups can be stored in the MS.flagversions
      file that can be accessed via the **flagmanager**.

      The most recent specification for the MS is `MeasurementSet
      definition version
      2.0 <https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals/measurement-set>`__.

.. container:: section
   :name: viewlet-below-content-body

.. |image1| image:: https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/visibility-data-import-export/imex-ms-content.png/@@images/2129b51e-7f64-4c45-8d86-74f37b712dd1.png
   :class: image-inline
