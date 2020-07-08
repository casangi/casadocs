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

            Name of input visibility file

Example

.. container:: param

   .. container:: parameters2

      options : string = ap

   List options: ap only

Example

.. container:: param

   .. container:: parameters2

      datacolumn : string = data

   Column to list: data, float_data, corrected, model, residual

Allowed Value(s)

data float_data corrected model residual

Example

.. container:: param

   .. container:: parameters2

      field : string

   Field names or index to be listed

Example

''==>all

.. container:: param

   .. container:: parameters2

      spw : string = \*

   Spectral window channels

Example

'*'==>all, spw='1:5~57'

.. container:: param

   .. container:: parameters2

      selectdata : bool = False

   Other data selection parameters

Example

.. container:: param

   .. container:: parameters2

      antenna : string

   Antenna/baselines

Example

''==>all, antenna = '3'

.. container:: param

   .. container:: parameters2

      timerange : string

   Time range

Example

''==>all

.. container:: param

   .. container:: parameters2

      correlation : string

   Correlations

Example

''==>all, correlation = 'RR RL'

.. container:: param

   .. container:: parameters2

      scan : string

   Scan numbers

Example

.. container:: param

   .. container:: parameters2

      feed : string

   Multi-feed numbers (Not yet implemented)

Example

.. container:: param

   .. container:: parameters2

      array : string

   Array numbers (Not yet implemented)

Example

.. container:: param

   .. container:: parameters2

      observation : string int

   Select by observation ID(s)

Example

.. container:: param

   .. container:: parameters2

      uvrange : string

   uv range

Example

''==>all; not yet implemented

.. container:: param

   .. container:: parameters2

      average : string

   Averaging mode

Allowed Value(s)

none time chan both

Example

''==>none (Not yet implemented)

.. container:: param

   .. container:: parameters2

      showflags : bool = False

   Show flagged data (Not yet implemented)

Example

.. container:: param

   .. container:: parameters2

      pagerows : int = 50

   Rows per page

Example

.. container:: param

   .. container:: parameters2

      listfile : string

   Output file

Example

.. container:: section
   :name: viewlet-below-content-body
