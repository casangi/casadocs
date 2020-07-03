.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Overview
========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Overview of Visibility Data Import Export chapter

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      To use CASA to process your data, you first will need to get it
      into a form that is understood by the package. These are
      “MeasurementSets” for synthesis and single dish data, which is the
      purpose of this chapter. Importing images, or “image tables” as
      understood by CASA, is
      explained\ `here <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/image-import-and-export>`__\ .

      There are a number of tasks used to fill telescope-specific data
      and to import/export standard formats. These are:

      -  importasdm — import of ALMA data in ASDM format
      -  importuvfits — import visibility data in UVFITS format
      -  importfitsidi — import visibility data in the FITS-IDI format
      -  importvla — import data from VLA that is in export format
      -  importmiriad — import data from MIRIAD visibilities
      -  importatca — import ATCA data that is in the RPFITS (archive)
         format
      -  importgmrt — import GMRT data
      -  **importasap**\  — convert ASAP (ATNF Spectral Analysis
         Package) into a CASA visibility data format
      -  importnro — import NRO 45m data 
      -  exportasdm — convert a CASA MS into an ASDM
      -  exportuvfits — export a CASA MS in UVFITS format

.. container:: section
   :name: viewlet-below-content-body
