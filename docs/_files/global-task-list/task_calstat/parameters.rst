.. container::
   :name: viewlet-above-content-title

Parameters
==========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task calstat parameters

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               caltable : string

            Name of input calibration table Default: '' Example:
            vis='ggtau.1mm.amp.gcal'

Example

.. container:: param

   .. container:: parameters2

      axis : string = amplitude

   Which data to analyze. Default: 'amplitude' Options: 'amp',
   'amplitude', 'phase', 'real', 'imag', 'imaginary'. Also, the name of
   any real valued MS column can be given, e.g. TIME, POLY_COEFF_AMP,
   REF_ANT, ANTENNA1, FLAG, ... Note: the phase of a complex number is
   in radians in the range [-pi; pi].

Example

.. container:: param

   .. container:: parameters2

      datacolumn : string = gain

   Which data column to use if axis is 'amp', 'amplitude', 'phase',
   'real', 'imag' or 'imaginary'. Default: 'gain'

Example

.. container:: param

   .. container:: parameters2

      useflags : bool = True

   Take flagging into account? (not implemented, this parameter has no
   effect!) Default: False If useflags=False, flagged values are
   included in the statistics. If useflags=True, any flagged values are
   not used in the statistics.

Example

useflags=True

.. container:: param

   .. container:: parameters2

      xstat : undefined = {}

   Statistical information for the calibration table

Example

.. container:: section
   :name: viewlet-below-content-body
