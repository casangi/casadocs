

.. _Description:

Description
   

.. _Examples:

Examples
   task examples
   
   This example was taken from the simulation CASAguide located
   `here <https://casaguides.nrao.edu/index.php/Simulation_Guide_Component_Lists_(CASA_5.1)>`__.
   
   ::
   
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
   
   ::
   
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
   

.. _Development:

Development
   task developer
   
   --CASA Developer--
   
   