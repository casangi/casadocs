Examples
========

.. container:: documentDescription description

   task examples

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

         | tsdimaging(infiles='mydata.ms',
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

         start=100 #(mode='channel')
         start='22.3GHz' #(mode='frequency')
         start='5.0km/s' #(mode='velocity')

       

      The parameter *phasecenter* sets the center direction of the
      image:

      .. container:: casa-input-box

         phasecenter=6
         phasecenter='J2000 19h30m00 -40d00m00'
         phasecenter='J2000 292.5deg -40.0deg'
         phasecenter='J2000 5.105rad -0.698rad'
         phasecenter='ICRS 13:05:27.2780 -049.28.04.458'
         phasecenter='myComet_ephem.tab'
         phasecenter='MOON'
         phasecenter='TRACKFIELD'

.. container:: section
   :name: viewlet-below-content-body
