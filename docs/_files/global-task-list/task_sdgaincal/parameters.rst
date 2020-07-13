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

               infile : string

            name of input SD dataset (must be MS)

Example

.. container:: param

   .. container:: parameters2

      calmode : string = doublecircle

   gain calibration mode

Allowed Value(s)

doublecircle

Example

.. container:: param

   .. container:: parameters2

      radius : undefined

   radius of central region to be used for calibration

Example

.. container:: param

   .. container:: parameters2

      smooth : bool = True

   smooth data or not

Example

.. container:: param

   .. container:: parameters2

      antenna : string

   select data by antenna name or ID, e.g. "PM03"

Example

.. container:: param

   .. container:: parameters2

      field : string

   select data by field IDs and names, e.g. "3C2*" ("" = all)

Example

.. container:: param

   .. container:: parameters2

      spw : string

   select data by spw IDs (spectral windows), e.g., "3,5,7" ("" = all)

Example

.. container:: param

   .. container:: parameters2

      scan : string

   select data by scan numbers, e.g. "21~23" (""=all)

Example

.. container:: param

   .. container:: parameters2

      intent : string

   select data by observation intent, e.g. "OBSERVE_TARGET#ON_SOURCE"
   (""=all)

Example

.. container:: param

   .. container:: parameters2

      applytable : undefined

   (List of) sky and/or tsys tables for pre-application

Example

.. container:: param

   .. container:: parameters2

      interp : undefined

   Interp type in time[,freq], per gaintable. default==linear,linear

Example

.. container:: param

   .. container:: parameters2

      spwmap : intArray

   Spectral window mappings to form for applytable(s) Only used if
   callib=False default: [] (apply solutions from each calibration spw
   to the same MS spw only) Any available calibration spw can be
   mechanically mapped to any MS spw. Examples: spwmap=[0,0,1,1] means
   apply calibration from cal spw = 0 to MS spw 0,1 and cal spw 1 to MS
   spws 2,3. spwmap=[[0,0,1,1],[0,1,0,1]] (use a list of lists for
   multiple applytables)

Example

.. container:: param

   .. container:: parameters2

      outfile : string

   name of output caltable

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   overwrite the output file if already exists

Example

.. container:: section
   :name: viewlet-below-content-body
