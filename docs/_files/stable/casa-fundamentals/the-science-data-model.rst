.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Science Data Model
==================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Introduction to the Science Data Model

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      | It was decided realtively early in the preparatory phase of ALMA
        and EVLA that the two projects would
      | 1) use the same data analysis software (CASA) and
      | 2) use essentially the same archive data format, the (ALMA)
        Science Data Model, (A)SDM.
      | The SDM was developed to a first prototype by Francois
        Viallefond (Observatoire de Paris) as an extension and full
        generalisation of the MeasurementSet. The SDM is superior to the
        MS w.r.t. the storage of observatory raw data in that it is
        capable of capturing the metadata of an interferometic or
        total-power dataset completely without any compromise including
        all data relevant for calibration and observatory
        administration.

      Just like for the MS, one can think of the SDM as a relational
      database. And both databases have in principle a very similar
      layout. However, while the MS has only 12 required Subtables, the
      SDM uses typically 40 Subtables, and there are more optional ones.

      SDMs, however, are for data storage and data reduction should be
      done on the MeasurementSet (although when importing data through
      **importasdm** with option *lazy=True*  the ASDM is restructured
      to resemble an MS). 

      For the implementation of the SDM, (then) novel source code
      generation techniques were applied which permitted simultaneous
      implementation in Java and C++. As the actual representation of
      the data on disk, a hybrid format was chosen: all low-volume
      metadata is stored as XML files (one per table) while the bulk
      data is stored in a binary format (MIME) in so-called Binary Large
      Objects (BLOBs). In particular the Main table is stored as a
      series of BLOBs of a few GB each with lossless compression. This
      makes the SDM more efficient as a bulk data format than the MS
      which stores the the DATA column of the Main table as one single
      monolithic file.

      An up to date description of the tables of the SDM is `given in
      this
      pdf <https://casa.nrao.edu/../Documents/SDMTables_v10Jan2020.pdf>`__.

      This `tar
      file <https://casa.nrao.edu/../Documents/0asdmSchematas_v10Jan2020.tgz>`__
      contains the XML Schema Definition (xds) files for all of the
      tables described in the associated SDM Short Table Description.
      Use "tar xvfz 0asdmSchematas_v15July2019.tgz" to extract its
      contents.

      This `tar
      file <https://casa.nrao.edu/../Documents/0enumerationsschematas.tgz>`__
      contains the XML Schema Definition (xds) files for all of the
      enumerations used by the SDM tables. Use "tar xvfz
      0enumerationsSchematas.tgz" to extract its contents.

      The binary data format is `given in this
      pdf <http://casa.nrao.edu/bdf.pdf>`__.

.. container:: section
   :name: viewlet-below-content-body
