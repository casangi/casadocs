Examples
========

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      To generate a spectral line cube with 500 channels selected from
      channel 200 to 700:

      .. container:: casa-input-box

         | spw='0'
         | pol='XX'
         | src='Moon'

         | sdimaging(infiles='mydata.ms',
         |     spw=spw,
         |     nchan=500,
         |     start='200',
         |     width='1',
         |     cell=['30.0arcsec','30.0arcsec'],
         |     outfile='mydata.ms.im',
         |     imsize=[80,80],
         |     gridfunction='GAUSS',
         |     gwidth='4arcsec',
         |     stokes=pol,
         |     ephemsrcname=src)

       

      The *start* parameter can be specified in different units:

      .. container:: casa-input-box

         start=100 (mode='channel')
         start='22.3GHz' (mode='frequency')
         start='5.0km/s' (mode='velocity')

       

      The parameter *ephemsrcname* can be set to a solar system object:

      .. container:: casa-input-box

         ephemsrcname ='MERCURY'

.. container:: section
   :name: viewlet-below-content-body
