.. contents::
   :depth: 3
..

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

      Example of a **simalma** routine. More information on this can be
      seen
      `here <https://casaguides.nrao.edu/index.php/Simalma_(CASA_5.1)>`__.

      .. container:: casa-input-box

         | # Set simalma to default parameters
         | default("simalma")
         | # Our project name will be "m51", and all simulation products
           will be placed in a subdirectory "m51/"
         | project="m51"
         | overwrite=True
         | # Model sky = H_alpha image of M51
         | os.system('curl
           https://casaguides.nrao.edu/images/3/3f/M51ha.fits.txt -f -o
           M51ha.fits')
         | skymodel="M51ha.fits"
         | # Set model image parameters:
         | indirection="J2000 23h59m59.96s -34d59m59.50s"
         | incell="0.1arcsec"
         | inbright="0.004"
         | incenter="330.076GHz"
         | inwidth="50MHz"
         | antennalist=["alma.cycle5.3.cfg","aca.cycle5.cfg"]
         | totaltime="1800s"
         | tpnant = 2
         | tptime="7200s"
         | pwv=0.6
         | mapsize="1arcmin"
         | dryrun = False
         | simalma()

       

.. container:: section
   :name: viewlet-below-content-body
