.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Description
===========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Convert a CASA visibility data set to a UVFITS file

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      The task **exportuvfits** takes a MeasurementSet and exports it to
      a UVFITS format file.

      UVFITS is a general format dataset used to transfer data between
      different software systems. In CASA, exportuvfits is mainly
      developed to transfer data from CASA to AIPS, but it also serves
      the UVFITS format used in other software packages (e.g., MIRIAD).
      A UVFITS file is written in floating point format.
      **exportuvfits** accepts a number of parameters that can control
      what is written out (see e.g. the *spw*, *multisource*,
      *combinespw* parameter descriptions).

      .. container:: alert-box

         **WARNING:** Some external software packages (e.g., GILDAS)
         cannot easily read CASA UVFITS files when more than one
         spectral window are exported in exportuvfits. In those cases,
         please export a single spectral window at a time by setting the
         *‘spw’* parameter.

      The parameters of *field*, *spw*, *antenna*, and *timerange*
      select the data that are exported from the MS dataset. The
      *datacolumn* parameter chooses which data-containing column of the
      MS is to be written out to the UVFITS file. Choices are: '*data*',
      '*corrected*', '*model*', and '*weight*'.

      The *multisource* parameter determines whether the UVFITS file is
      a multi-source file or a single-source file, if you have a
      single-source MS or choose only a single source. Multi-source
      UVFITS files have multiple source IDs in the source (SU) table.
      Some programs (i.e. difmap) only accept single-source format
      files. Note that if you select more than one source in *field*,
      then the *multisource* parameter will be overridden to be *True*
      regardless. 

      MSes where the tuning changed with time should be exported to
      multiple UVFITS files using *spw* to select one tuning (set of
      simultaneous spectral windows) per file (e.g. 10 minutes at 4.8
      GHz followed by 15 minutes at 8.4 GHz). 

      The *combinespw* parameter allows combination of all spectral
      windows at one time. If *True*, then all spectral windows must
      have the same shape. In other words, they should have the same
      number of channels and polarizations, and each channel must have
      the same width, and each IF (Intermediate Frequency) must be
      present (even if flagged) throughout the entire observation. If
      these conditions are met, all spectral windows are exported as a
      set of IFs in a single FREQID setup instead of giving each
      spectral window its own FREQID in the FITS file. (IF and FREQID
      are the identification number of a spectral window and the
      spectral set up of a baseband in the FITS file, respectively.) If
      these conditions are not met the data must be exported using
      multiple FREQIDs, the UVFITS equivalent of a general spectral
      window. This matters since many (sub)programs will work with
      multiple IFs, but not multiple FREQIDs. For example, a UVFITS file
      with multiple FREQIDs can be read by AIPS, but you may find that
      you have to separate the FREQIDs with **split** before you can do
      very much with them. 

      You can fill in missing data as needed to fit the IF structure
      using *padwithflags* option. To do that, not only set
      *padwithflags*\ =True, but also *combinespw=*\ True. This is
      appropriate if the MS had a few frequency-dependent flags applied,
      and was then time-averaged by split, or when exporting for use by
      difmap.  If the spectral windows were observed at different times,
      *padwithflags*\ =True will add a large number of flags, making the
      output file significantly longer.  It does not yet support
      spectral windows with different widths.

      It is recommended to perform any required data averaging using
      other tasks (e.g., **split** or **mstransform**) before exporting
      the UVFITS file with **exportuvfits**.

      A NOTE ON WEIGHTS: If the MS has no WEIGHT_SPECTRUM column, or if
      it does but that column contains no data, **exportuvfits** will
      compute for each visibility the weight it writes to the UVFITS
      file by dividing the associated WEIGHT column value in the MS by
      the number of channels in the relevant spectral window within
      which that visibility is located.

      Optionally, the parameter *overwrite* can be use to overwrite
      existing uvfits files with the same name as that specified in the
      *fitsfile* parameter.

       

       

.. container:: section
   :name: viewlet-below-content-body
