

.. _Description:

Description
   Convert a Miriad visibility dataset into a CASA MeasurementSet
   
   The task **importmiriad** allows one to import visibilities in the
   MIRIAD data format to be converted to a MeasurementSet. The task
   has mainly been tested on data from the ATCA and CARMA telescopes
   and the inputs are:
   
   ::
   
      #In CASA
      #  importmiriad :: Convert a Miriad visibility file into a CASA
      MeasurementSet
      mirfile             =         ''        #  Name of input Miriad
      visibility file
      vis                 =         ''        #  Name of output
      MeasurementSet
      tsys                =      False        #  Use the Tsys to set
      the visibility
                                              #   weights
      spw                 =       [-1]        #  Select spectral
      windows, default is
                                              #   all
      vel                 =         ''        #  Select velocity
      reference
                                              #   (TOPO,LSRK,LSRD)
      linecal             =      False        #  (CARMA) Apply line
      calibration
      wide                =         []        #  (CARMA) Select wide
      window averages
      debug               =          0        #  Display increasingly
      verbose debug
                                              #   messages
   
   -  The *mirfile* parameter specifies a single MIRIAD visibility
      dataset which **must have any calibration done in MIRIAD
      already applied to it**. MIRIAD calibration tables are usually
      applied on the fly within MIRIAD; such steps (e.g., uvaver)
      need to be taken within MIRIAD such that your
      MIRIAD visibilities have the calibration permanently applied.
   -  Set the *tsys* parameter to True to change the visibility
      weights from the MIRIAD default (usually the integration time)
      to the inverse of the noise variance using the recorded system
      temperature.
   -  The *spw* parameter can be used to select all or some of the
      simultaneous spectral windows from the input file. Use the
      default of ’all’ for all the data or use e.g., spw=’0,2’ to
      select the first and third window.
   -  The *vel* parameter can be used to set the output velocity
      frame reference. For ATCA this defaults to ’TOPO’ and for CARMA
      it defaults to ’LSRK’. Only change this if your data comes out
      with the incorrect velocity.
   -  The *linecal* parameter is only useful for CARMA data and can
      apply the line calibration if it is stored with the MIRIAD
      data.
   -  The *wide* parameter is only useful for CARMA data and can
      select which of the wide-band channels should be loaded.
   

.. _Examples:

Examples
   .. rubric:: Reading a MIRIAD file and converting it into a
      MeasurementSet   
      
   
   ::
   
      #In CASA
   
      importmiriad(mirfile='ngc5921.uv', vis='ngc5921.ms',tsys=True)
   
   We read the MIRIAD dataset ngc5921.uv and converted it to a
   MeasurementSet, using the recorded Tsys values to set the weights.
   

.. _Development:

Development
   --CASA Developer--
   
   