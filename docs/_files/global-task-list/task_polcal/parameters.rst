Parameters
==========

.. container:: documentDescription description

   task parameters

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               vis : string

            Name of input visibility file

Example

.. container:: param

   .. container:: parameters2

      caltable : string

   Name of output gain calibration table

Example

.. container:: param

   .. container:: parameters2

      field : string

   Select field using field id(s) or field name(s)

Example

.. container:: param

   .. container:: parameters2

      spw : string

   Select spectral window/channels

Example

.. container:: param

   .. container:: parameters2

      intent : string

   Select observing intent

Example

.. container:: param

   .. container:: parameters2

      selectdata : bool = True

   Other data selection parameters

Example

.. container:: param

   .. container:: parameters2

      timerange : string

   Select data based on time range

Example

.. container:: param

   .. container:: parameters2

      uvrange : undefined

   Select data within uvrange (default units meters)

Example

.. container:: param

   .. container:: parameters2

      antenna : string

   Select data based on antenna/baseline

Example

.. container:: param

   .. container:: parameters2

      scan : string

   Scan number range

Example

.. container:: param

   .. container:: parameters2

      observation : string int

   Select by observation ID(s)

Example

.. container:: param

   .. container:: parameters2

      msselect : string

   Optional complex data selection (ignore for now)

Example

.. container:: param

   .. container:: parameters2

      solint : undefined = inf

   Solution interval

Example

.. container:: param

   .. container:: parameters2

      combine : string = obs,scan

   Data axes which to combine for solve (obs, scan, spw, and/or field)

Example

.. container:: param

   .. container:: parameters2

      preavg : double = 300.0

   Pre-averaging interval (sec)

Example

.. container:: param

   .. container:: parameters2

      refant : string

   Reference antenna name(s)

Example

.. container:: param

   .. container:: parameters2

      minblperant : int = 4

   Minimum baselines \_per antenna\_ required for solve

Example

.. container:: param

   .. container:: parameters2

      minsnr : double = 3.0

   Reject solutions below this SNR

Example

.. container:: param

   .. container:: parameters2

      poltype : string = D+QU

   Type of instrumental polarization solution (see help)

Allowed Value(s)

D Df D+X Df+X D+QU Df+QU Dgen Dfgen Dgen+X Dfgen+X Dgen+QU Dfgen+QU Dlls
Dflls X Xf Xparang+QU Xfparang+QU PosAng Xj

Example

.. container:: param

   .. container:: parameters2

      smodel : doubleArray

   Point source Stokes parameters for source model.

Example

.. container:: param

   .. container:: parameters2

      append : bool = False

   Append solutions to the (existing) table

Example

.. container:: param

   .. container:: parameters2

      docallib : bool = False

   Use callib or traditional cal apply parameters

Example

.. container:: param

   .. container:: parameters2

      callib : string

   Cal Library filename

Example

.. container:: param

   .. container:: parameters2

      gaintable : stringArray

   Gain calibration table(s) to apply

Example

.. container:: param

   .. container:: parameters2

      gainfield : stringArray

   Select a subset of calibrators from gaintable(s)

Example

.. container:: param

   .. container:: parameters2

      interp : stringArray

   Interpolation mode (in time) to use for each gaintable

Example

.. container:: param

   .. container:: parameters2

      spwmap : intArray

   Spectral window mappings to form for gaintable(s) Only used if
   callib=False default: [] (apply solutions from each calibration spw
   to the same MS spw only) Any available calibration spw can be
   mechanically mapped to any MS spw. Examples: spwmap=[0,0,1,1] means
   apply calibration from cal spw = 0 to MS spw 0,1 and cal spw 1 to MS
   spws 2,3. spwmap=[[0,0,1,1],[0,1,0,1]] (use a list of lists for
   multiple gaintables)

Example

.. container:: section
   :name: viewlet-below-content-body
