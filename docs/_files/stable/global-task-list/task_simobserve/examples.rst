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

      This example was taken from the simulation CASAguide located
      `here <https://casaguides.nrao.edu/index.php/Simulation_Guide_Component_Lists_(CASA_5.1)>`__.

      .. container:: casa-input-box

         | default("simobserve")
         | project = "FITS_list"
         | skymodel = "Gaussian.fits"
         | inwidth = "1GHz"
         | complist = 'point.cl'
         | compwidth = '1GHz'
         | direction = "J2000 10h00m00.0s -30d00m00.0s"
         | obsmode = "int"
         | antennalist = 'alma.cycle5.1.cfg'
         | totaltime = "28800s"
         | mapsize = "10arcsec"
         | thermalnoise = ''
         | simobserve()

      This example demonstrates the use of the *comp_nchan* parameter to
      simulate a disk and produce a multi-channel MS (with a flat
      spectrum).

      .. container:: casa-input-box

         simobserve(project="test_project",
                    complist="complist.cl",
                    compwidth="2000.00MHz",
                    comp_nchan=128,
                    integration="6.05s",
                    mapsize=['11.51arcsec'],
                    hourangle="1.5h",
                    totaltime="677.6s",
                    antennalist="antennalist.cfg2",
                    sdantlist="aca.tp.cfg",
                    thermalnoise="")

       

       

.. container:: section
   :name: viewlet-below-content-body
