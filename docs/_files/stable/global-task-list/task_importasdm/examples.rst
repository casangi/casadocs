.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Examples
========

.. container::
   :name: viewlet-below-content-title

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      In the simplest form, setting bdfflags=True and verbose=True:

      .. container:: casa-input-box

         importasdm(asdm='uid___A002_Xbbadbe_X88ec.asdm.sdm',
         vis='uid___A002_Xbbadbe_X88ec.ms', bdfflags=True, verbose=True)

       

      Import both the corrected and uncorrected WVR data from an ALMA
      dataset with wvr_corrected_data='both' and setting bdfflags=True
      and verbose=True:

      .. container:: casa-input-box

         importasdm(asdm='uid___A002_Xbbadbe_X88ec.asdm.sdm',
         vis='uid___A002_Xbbadbe_X88ec.ms', wvr_corrected_data='both',
         bdfflags=True, verbose=True)

      In this case, two MeasurementSets are created, one with
      WVR-uncorrected data filled in the MAIN table and the other with
      WVR-corrected data filled in the MAIN table.

       

      To import data from the VLA (and replicate the behaviour of the
      deprecated task **importevla**):

      .. container:: casa-input-box

         importasdm(asdm='19A-119.sb123243.58235.79924266203',
         vis='19A-119.sb123243.58235.79924266203.ms', ocorr_mode='co',
         with_pointing_correction=True, process_flags=True)

         flagdata(vis='19A-119.sb123243.58235.79924266203.ms',
         mode='shadow')

         flagdata(vis='19A-119.sb123243.58235.79924266203.ms',
         mode='clip', correlation='ABS_ALL', and clipzeros=True)

      Note that while online flags can thus be created by leaving the
      parameter *process_flags = True* by default, the additional
      flagging steps need to be performed after **importasdm** to flag
      zero values and shadowing of antennas, in order to replicate the
      behavior of the deprecated task **importevla**. See the CASA Docs
      pages on `importing
      (u,v)-data <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/visibility-data-import-export/uv-data-import>`__
      for details.

       

.. container:: section
   :name: viewlet-below-content-body
