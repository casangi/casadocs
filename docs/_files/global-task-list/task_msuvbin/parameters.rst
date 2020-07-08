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

      field : string

   Field selection of input ms

Example

.. container:: param

   .. container:: parameters2

      spw : string

   Spw selection

Example

.. container:: param

   .. container:: parameters2

      taql : string

   TaQl string for data selection

Example

.. container:: param

   .. container:: parameters2

      outvis : string

   name of output uvgrid

Example

.. container:: param

   .. container:: parameters2

      phasecenter : string

   phase center of uv grid

Example

.. container:: param

   .. container:: parameters2

      nx : int = 1000

   Number of pixels of grid along the x-axis

Example

.. container:: param

   .. container:: parameters2

      ny : int = 1000

   Number of pixels of grid along the y-axis

Example

.. container:: param

   .. container:: parameters2

      cell : string = 1arcsec

   pixel cell size defined in sky dimension

Example

.. container:: param

   .. container:: parameters2

      ncorr : int = 1

   number of correlations to store in grid

Allowed Value(s)

1 2 4

Example

.. container:: param

   .. container:: parameters2

      nchan : int = 1

   Number of spectral channels in grid

Example

.. container:: param

   .. container:: parameters2

      fstart : string = 1GHz

   Frequency of first spectral channel

Example

.. container:: param

   .. container:: parameters2

      fstep : string = 1kHz

   spectral channel width

Example

.. container:: param

   .. container:: parameters2

      wproject : bool = False

   Do wprojection correction while gridding

Example

.. container:: param

   .. container:: parameters2

      memfrac : double = 0.5

   Limit how much of memory to use

Allowed Value(s)

0.01 0.99

Example

.. container:: section
   :name: viewlet-below-content-body
