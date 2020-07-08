.. container::
   :name: viewlet-above-content-title

Parameters
==========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task parameters

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               vis : string

            Name of input Measurement set or Multi-MS.

Example

.. container:: param

   .. container:: parameters2

      outputvis : string

   Name of output Measurement Set or Multi-MS.

Example

.. container:: param

   .. container:: parameters2

      createmms : bool = False

   Create a multi-MS output from an input MS.

Example

.. container:: param

   .. container:: parameters2

      separationaxis : string = auto

   Axis to do parallelization across(scan,spw,auto,baseline).

Allowed Value(s)

auto spw scan baseline

Example

.. container:: param

   .. container:: parameters2

      numsubms : string int = auto

   The number of Sub-MSs to create (auto or any number)

Example

.. container:: param

   .. container:: parameters2

      tileshape : intArray = 0

   List with 1 or 3 elements giving the tile shape of the disk data
   columns.

Example

.. container:: param

   .. container:: parameters2

      field : string stringArray int intArray

   Select field using ID(s) or name(s).

Example

.. container:: param

   .. container:: parameters2

      spw : string stringArray int intArray

   Select spectral window/channels.

Example

.. container:: param

   .. container:: parameters2

      scan : string stringArray int intArray

   Select data by scan numbers.

Example

.. container:: param

   .. container:: parameters2

      antenna : string stringArray int intArray

   Select data based on antenna/baseline.

Example

.. container:: param

   .. container:: parameters2

      correlation : string stringArray

   Correlation: '' ==> all, correlation="XX,YY".

Example

.. container:: param

   .. container:: parameters2

      timerange : string stringArray int intArray

   Select data by time range.

Example

.. container:: param

   .. container:: parameters2

      intent : string stringArray int intArray

   Select data by scan intent.

Example

.. container:: param

   .. container:: parameters2

      array : string stringArray int intArray

   Select (sub)array(s) by array ID number.

Example

.. container:: param

   .. container:: parameters2

      uvrange : string stringArray int intArray

   Select data by baseline length.

Example

.. container:: param

   .. container:: parameters2

      observation : string stringArray int intArray

   Select by observation ID(s).

Example

.. container:: param

   .. container:: parameters2

      feed : string stringArray int intArray

   Multi-feed numbers: Not yet implemented.

Example

.. container:: param

   .. container:: parameters2

      datacolumn : string = corrected

   Which data column(s) to process.

Allowed Value(s)

corrected data model data,model,corrected float_data lag_data
float_data,data lag_data,data all

Example

.. container:: param

   .. container:: parameters2

      realmodelcol : bool = False

   Make real a virtual MODEL column.

Example

.. container:: param

   .. container:: parameters2

      keepflags : bool = True

   Keep \*completely flagged rows\* or drop them from the output.

Example

.. container:: param

   .. container:: parameters2

      usewtspectrum : bool = False

   Force creation of the columns WEIGHT_SPECTRUM and SIGMA_SPECTRUM in
   the output MS, even if not present in the input MS.

Example

.. container:: param

   .. container:: parameters2

      combinespws : bool = False

   Combine the input spws into a new output spw. Only supported when the
   number of channels is the same for all the spws.

Example

.. container:: param

   .. container:: parameters2

      chanaverage : bool = False

   Average data in channels.

Example

.. container:: param

   .. container:: parameters2

      chanbin : int intArray = 1

   Width (bin) of input channels to average to form an output channel.

Example

.. container:: param

   .. container:: parameters2

      hanning : bool = False

   Hanning smooth data to remove Gibbs ringing.

Example

.. container:: param

   .. container:: parameters2

      regridms : bool = False

   Transform channel labels and visibilities to a different spectral
   reference frame. Notice that u,v,w data is not transformed.

Example

.. container:: param

   .. container:: parameters2

      mode : string = channel

   Regridding mode (channel/velocity/frequency/channel_b).

Allowed Value(s)

channel velocity frequency channel_b

Example

.. container:: param

   .. container:: parameters2

      nchan : int = -1

   Number of channels in the output spw (-1=all). Used for regridding,
   together with \\'start\' and \\'width\'.

Example

.. container:: param

   .. container:: parameters2

      start : undefined = 0

   Start of the output visibilities. Used for regridding, together with
   \\'width\' and \\'nchan\'. It can be in different units, depending on
   the regridding mode: first input channel (mode=\'channel\'), first
   velocity (mode=\'velocity\'), or first frequency
   (mode=\'frequency\'). Example values: \\'5\', \\'0.0km/s\',
   \\'1.4GHz\', for channel, velocity, and frequency modes,
   respectively.

Example

.. container:: param

   .. container:: parameters2

      width : undefined = 1

   Channel width of the output visibilities. Used for regridding,
   together with \\'start\', and \\'nchan\'. It can be in different
   units, depending on the regridding mode: number of input channels
   (mode=\'channel\'), velocity (mode=\'velocity\'), or frequency
   (mode=\'frequency\'. Example values: \\'2\', \\'1.0km/s\',
   \\'1.0kHz\', for channel, velocity, and frequency modes,
   respectively.

Example

.. container:: param

   .. container:: parameters2

      nspw : int = 1

   Number of output spws to create in output MS.

Example

.. container:: param

   .. container:: parameters2

      interpolation : string = linear

   Spectral interpolation method.

Allowed Value(s)

nearest linear cubic spline fftshift

Example

.. container:: param

   .. container:: parameters2

      phasecenter : undefined

   Phase center direction to be used for the spectral coordinate
   transformation: direction measure or field index

Example

.. container:: param

   .. container:: parameters2

      restfreq : string

   Rest frequency to use for output.

Example

.. container:: param

   .. container:: parameters2

      outframe : string

   Output reference frame (''=keep input frame).

Allowed Value(s)

topo geo lsrk lsrd bary galacto lgroup cmb source

Example

.. container:: param

   .. container:: parameters2

      veltype : string = radio

   Velocity definition.

Allowed Value(s)

optical radio

Example

.. container:: param

   .. container:: parameters2

      preaverage : bool = False

   Pre-average channels before regridding, when the ratio between the
   output and and input widths is greater than 2.

Example

.. container:: param

   .. container:: parameters2

      timeaverage : bool = False

   Average data in time.

Example

.. container:: param

   .. container:: parameters2

      timebin : string = 0s

   Bin width for time averaging.

Example

.. container:: param

   .. container:: parameters2

      timespan : string stringArray

   Span the timebin across scan, state or both.

Example

.. container:: param

   .. container:: parameters2

      maxuvwdistance : double = 0.0

   Maximum separation of start-to-end baselines that can be included in
   an average. (meters)

Example

.. container:: param

   .. container:: parameters2

      docallib : bool = False

   Enable on-the-fly (OTF) calibration as in task applycal

Example

.. container:: param

   .. container:: parameters2

      callib : string

   Path to calibration library file

Example

.. container:: param

   .. container:: parameters2

      douvcontsub : bool = False

   Enable continuum subtraction as in task uvcontsub

Example

.. container:: param

   .. container:: parameters2

      fitspw : string

   Spectral window:channel selection for fitting the continuum

Example

.. container:: param

   .. container:: parameters2

      fitorder : int = 0

   Polynomial order for the fits

Example

.. container:: param

   .. container:: parameters2

      want_cont : bool = False

   Produce continuum estimate instead of continuum subtracted data

Example

.. container:: param

   .. container:: parameters2

      denoising_lib : bool = True

   Use new denoising library (based on GSL) instead of casacore fitting
   routines

Example

.. container:: param

   .. container:: parameters2

      nthreads : int = 1

   Number of OMP threads to use (currently maximum limited by number of
   polarizations)

Example

.. container:: param

   .. container:: parameters2

      niter : int = 1

   Number of iterations for re-weighted linear fit

Example

.. container:: section
   :name: viewlet-below-content-body
