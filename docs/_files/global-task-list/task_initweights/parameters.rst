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

            Name of input visibility file (MS)

Example

.. container:: param

   .. container:: parameters2

      wtmode : string = nyq

   Initialization mode

Allowed Value(s)

nyq sigma weight ones delwtsp delsigsp tsys tinttsys

Example

.. container:: param

   .. container:: parameters2

      tsystable : string

   Tsys calibration table to apply on the fly

Example

.. container:: param

   .. container:: parameters2

      gainfield : string

   Select a subset of calibrators from Tsys table

Example

.. container:: param

   .. container:: parameters2

      interp : string

   Interpolation type in time[,freq]. default==\'linear,linear\'

Example

.. container:: param

   .. container:: parameters2

      spwmap : intArray

   Spectral windows combinations to form for gaintable(s)

Example

.. container:: param

   .. container:: parameters2

      dowtsp : bool = False

   Initialize the WEIGHT_SPECTRUM column

Example

.. container:: section
   :name: viewlet-below-content-body
