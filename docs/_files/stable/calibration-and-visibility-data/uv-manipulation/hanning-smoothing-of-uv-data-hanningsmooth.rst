.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Hanning Smooth UV-data
======================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Highlights on Hanning smoothing of data using task hanningsmooth

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      For strong spectral line sources (like RFI sources), the Gibbs
      phenomenon may cause ringing across the frequency channels of an
      observation. This is called the Gibbs phenomenon and a proven
      remedy is the Hanning smoothing algorithm. Hanning smoothing is a
      running mean across the spectral axis with a triangle as a
      smoothing kernel. The central channel is weighted by 0.5 and the
      two adjacent channels by 0.25 to preserve the flux; mathematically
      this is an N=5 sample Hann window kernel (including the outer-most
      zero-weight samples in the window). Hanning smoothing
      significantly reduces Gibbs ringing at the price of a factor of
      two in spectral resolution. Users should also be aware that it
      will introduce noise correlations between channels which can
      affect the interpretation of cross-channel chi-squared or uv-model
      fitting analyses.

      The new **hanningsmooth** task (based on **mstransform**) does not
      write to the input MS, but it always creates an output MS. It can
      also handle a Multi-MS and process it in parallel (see more
      information
      `here <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/testing-using-multi-ms>`__).

      In CASA, the **hanningsmooth** task will apply Hanning smoothing
      to a spectral line uv data MeasurementSet. The inputs are:

      .. container:: casa-input-box

         | #  hanningsmooth :: Hanning smooth frequency channel data to
           remove Gibbs ringing
         | vis                 =         ''        #  Name of input
           MeasurementSet or Multi-MS.
         | outputvis           =         ''        #  Name of output
           MeasurementSet or Multi-MS.
         | keepmms             =       True        #  If the input is a
           Multi-MS the output will also
         |                                            be a Multi-MS.
         | field               =         ''        #  Select field using
           ID(s) or name(s).
         | spw                 =         ''        #  Select spectral
           window/channels.
         | scan                =         ''        #  Select data by
           scan numbers.
         | antenna             =         ''        #  Select data based
           on antenna/baseline.
         | correlation         =         ''        #  Correlation: ''
           ==> all, correlation='XX,YY'.
         | timerange           =         ''        #  Select data by
           time range.
         | intent              =         ''        #  Select data by
           scan intent.
         | array               =         ''        #  Select
           (sub)array(s) by array ID number.
         | uvrange             =         ''        #  Select data by
           baseline length.
         | observation         =         ''        #  Select by
           observation ID(s).
         | feed                =         ''        #  Multi-feed
           numbers: Not yet implemented.
         | datacolumn          =      'all'        #  Input data
           column(s) to process.

      The *datacolumn* parameter determines which of the data columns is
      to be Hanning smoothed: ’all’, ’model’, ’corrected’, ’data’,
      ’float_data’ or ’lag_data’. ’all’ will use whichever of the
      visibility data columns that are present in the input MS. If
      ’corrected’ is specified, the task will smooth the input
      *CORRECTED_DATA* column and save the smoothed data in *DATA* of
      the output MS.

      The Hanning smoothing transformation in **mstransform** is
      available via a single parameter, as shown below:

      .. container:: casa-input-box

         | #  Hanning smooth in mstransform
         | hanning   = True        # Hanning smooth data to remove Gibbs
           ringing

.. container:: section
   :name: viewlet-below-content-body
