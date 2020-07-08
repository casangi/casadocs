.. container::
   :name: viewlet-above-content-title

Parameters
==========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task cvel parameters

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

            Name of input measurement set

Example

.. container:: param

   .. container:: parameters2

      outputvis : string

   Name of output measurement set

Example

.. container:: param

   .. container:: parameters2

      passall : bool = False

   Pass through (write to output MS) non-selected data with no change

Example

.. container:: param

   .. container:: parameters2

      field : string stringArray int intArray

   Select field using field id(s) or field name(s)

Example

.. container:: param

   .. container:: parameters2

      spw : string stringArray int intArray

   Select spectral window/channels

Example

.. container:: param

   .. container:: parameters2

      selectdata : bool = True

   Other data selection parameters

Example

.. container:: param

   .. container:: parameters2

      antenna : string

   Select data based on antenna/baseline

Example

.. container:: param

   .. container:: parameters2

      timerange : string

   Range of time to select from data

Example

.. container:: param

   .. container:: parameters2

      scan : string

   scan number range

Example

.. container:: param

   .. container:: parameters2

      array : string

   (sub)array indices

Example

.. container:: param

   .. container:: parameters2

      mode : string = channel

   Regridding mode

Allowed Value(s)

channel velocity frequency channel_b

Example

.. container:: param

   .. container:: parameters2

      nchan : int = -1

   Number of channels in output spw (-1=all). Used for regridding,
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

      interpolation : string = linear

   Spectral interpolation method

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

   rest frequency (see help)

Example

.. container:: param

   .. container:: parameters2

      outframe : string

   Output frame (not case-sensitive, \\'\'=keep input frame)

Allowed Value(s)

topo geo lsrk lsrd bary galacto lgroup cmb source

Example

.. container:: param

   .. container:: parameters2

      veltype : string = radio

   velocity definition

Allowed Value(s)

optical radio

Example

.. container:: param

   .. container:: parameters2

      hanning : bool = False

   If true, Hanning smooth data before regridding to remove Gibbs
   ringing.

Example

.. container:: section
   :name: viewlet-below-content-body
