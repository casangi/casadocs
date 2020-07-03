.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Examples
========

.. container::
   :name: viewlet-below-content-title

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      mode='get' (image has direction and spectral coordinates)

      .. container:: casa-input-box

         | epoch = imhead(imagename=imagename, mode="get",
           hdkey="date-obs")
         | observer = imhead(imagename=imagename, mode="get",
           hdkey="observer")
         | projection = imhead(imagename=imagename, mode="get",
           hdkey="projection")
         | restfreq = imhead(imagename=imagename, mode="get",
           hdkey="restfreq")

      mode='add'

      .. container:: casa-input-box

         | 
         | if imhead(imagename=imagename, mode="add", hdkey="mykey",
           hdvalue="myvalue"):
         |      print "mykey added".
         | else:
         |      print "addition of mykey failed."

      mode="del"

      .. container:: casa-input-box

         | if imhead(imagename=imagename, mode="del", hdkey="mykey"):
         |      print "mykey deleted".
         | else:
         |      print "deletion of mykey failed."

      mode="put"

      .. container:: casa-input-box

         | # change the reference RA value
         | key = 'crval1'
         | imhead(imagename=imagename, mode="put", hdkey=key,
           hdvalue="3:00:00")
         | # or equivalently
         | imhead(imagename=imagename, mode="put", hdkey=key,
           hdvalue="45deg")
         | # change the direction reference frame (NOTE, no precession
           of the existing
         | # reference values is done!)
         | imhead(imagename=imagename, mode="put", hdkey="equinox",
           hdvalue="GALACTIC")
         | # change the object
         | imhead(imagename=imagename, mode="put", hdkey="object",
           hdvalue="Milliways, also known as The Restaurant at the End
           of the Universe")

      | 

.. container:: section
   :name: viewlet-below-content-body
