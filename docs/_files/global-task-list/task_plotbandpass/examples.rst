.. container::
   :name: viewlet-above-content-title

Examples
========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task examples

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      To plot the system temperature (channel vs. amplitude) of fields
      0, 1 and 4, overlaying all antennas, and printing a png plot:

      .. container:: casa-input-box

         plotbandpass(caltable='X3c1.tsys', overlay='antenna',
         yaxis='amp', field='0~1,4', xaxis='chan',
         figfile='tsys.png').    

      To overplot two bandpass tables, with x-axis frequency:

      .. container:: casa-input-box

         plotbandpass(caltable='bandpass.bcal',
         caltable2='bandpass.bcal_smooth', xaxis='freq')

      To overplot the XX-polarisation two bandpass tables, with x-axis
      frequency; the atmospheric transmission curve is also computed and
      overlaid:

      .. container:: casa-input-box

         plotbandpass(caltable='bandpass.bcal',
         caltable2='bandpass.bcal_smooth', xaxis='freq', poln='X',
         showatm=True)

      The following returns void unless the *channeldiff* option is
      selected, in which case it returns a dictionary containing the
      statistics of the solutions, keyed by the antenna name,
      followed by the spw, timerange, polarization, and finally 'amp'
      and/or 'phase' depending on the yaxis selection.

      .. container:: casa-input-box

         plotbandpass(caltable='bandpass.bcal',channeldiff='5')

       

.. container:: section
   :name: viewlet-below-content-body
