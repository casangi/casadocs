.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Working with MS Data
====================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   The CASA data format and how to work with it

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Visibility Data
         :name: visibility-data
         :class: subsection

      The ALMA and VLA raw data are stored in their respective archives
      in the (ALMA) Science Data Model (A)SDM format.  The definition of
      the format can be found
      `here <https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals/the-science-data-model>`__. 

      To bring them into CASA, the (A)SDMs are filled into a so-called
      `MeasurementSet <https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals/measurement-set>`__
      (or MS) (format description can be found
      `here <https://casa.nrao.edu/../Memos/229.html>`__). In its
      logical structure, the MS looks like a generalized description of
      data from any interferometric or single dish telescope.
      Physically, the MS consists of several tables in a directory on
      disk, in XML format.

      Tables in CASA are actually directories containing files that are
      the sub-tables. For example, when you create a MS called AM675.ms,
      then the name of the directory where all the tables are stored
      will be called AM675.ms/. See chapter "`Visibility Data Import
      Export <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/visibility-data-import-export>`__"
      for more information on MeasurementSet and Data Handling in CASA.

      The data that you originally get from a telescope can be put in
      any directory that is convenient to you. Once you "fill" the data
      into a MeasurementSet that can be accessed by CASA, it is
      generally best to keep that MS in the same directory where you
      started CASA so you can get access to it easily (rather than
      constantly having to specify a full path name).

      When you generate calibration solutions or images (again these are
      in table format), these will also be written to disk. It is a good
      idea to keep them in the directory in which you started CASA, too.

      .. rubric:: How do I get rid of my data in CASA?
         :name: sec51

      Note that when you delete a MeasurementSet, calibration table, or
      image, which are in fact directories, you must delete this and all
      underlying directories and files. If you are not running CASA,
      this is most simply done by using the file delete method of the
      operating system from which you started CASA. For example, when
      running CASA on a Linux system, in order to delete the
      MeasurementSet named AM675.ms type

      .. container:: casa-input-box

         CASA <5>: !rm -r AM675.ms

      from within CASA. The ! tells CASA that a system command follows
      (see "`Python Basics for
      CASA <https://casa.nrao.edu/casadocs-devel/stable/old-pages/casa-and-python/python-basics-for-casa>`__"),
      and the -r makes sure that all subdirectories are deleted
      recursively.

      It is convenient to prefix all MS, calibration tables, and output
      files produced in a run with a common string. For example, one
      might prefix all files from VLA project AM675 with AM675, e.g.
      AM675.ms, AM675.cal, AM675.clean. Then,

      .. container:: casa-input-box

         CASA <6>: !rm -r AM675\*

       will clean up all of these. 

      In scripts, the ! escape to the OS will not work. Instead, use the
      **os.system**\ () function (see page "`Python and
      CASA <https://casa.nrao.edu/casadocs-devel/stable/old-pages/casa-and-python/python-and-casa>`__")
      to do the same thing:

      .. container:: casa-input-box

         os.system('rm -r AM675*')

      If you are within CASA, then the CASA system is keeping a cache of
      tables that you have been using and using the OS to delete them
      will confuse things. For example, running a script that contains
      *rm* commands multiple times will often not run or crash the
      second time as the cache gets confused. The clean way of removing
      CASA tables (MS, caltables, images) inside CASA is to use the
      **rmtables** task:

      .. container:: casa-input-box

         rmtables('AM675.ms')

      and this can also be wildcarded (though you may get warnings if it
      tries to delete files or directories that fit the name wildcard
      that are not CASA tables).

      .. container:: alert-box

         **ALERT**: **rmtables** is the preferred way to remove data.
         **clean** is a good example where frequently data are left in
         the cache after deleting the output files via "!rm -r".
         Restarting **clean** then sometimes claims that the files still
         exist, even though they are not present on disk anymore.
         **rmtables** will completely remove the files on disks and all
         cached versions and restarting **clean** will work as intended.
          

      .. container:: alert-box

         **ALERT:** Some CASA processes lock the file and forget to give
         it up when they are done. You will get *WARNING* messages from
         **rmtables** and your script will probably crash second time
         around as the file isn’t removed. The safest thing is still to
         exit CASA and start a new session for multiple runs.

       

      .. rubric:: What’s in my data?
         :name: whats-in-my-data

      The actual data is in a large *MAIN* table that is organized in
      such a way that you can access different parts of the data easily.
      This table contains a number of “rows”, which are effectively a
      single timestamp for a single spectral window (like an IF from the
      VLA) and a single baseline (for an interferometer).

      There are a number of “columns” in the MS, the most important of
      which for our purposes is the DATA column — this contains the
      original visibility data from when the MS was created or filled.
      There are other helpful “scratch” columns which hold useful
      versions of the data or weights for further processing: the
      CORRECTED_DATA column, which is used to hold calibrated data and
      an optional MODEL_DATA column, which may hold the Fourier
      inversion of a particular model image. The creation and use of the
      scratch columns is generally done behind the scenes, but you
      should be aware that they are there (and when they are used). We
      will occasionally refer to the rows and columns in the MS.

.. container:: section
   :name: viewlet-below-content-body
