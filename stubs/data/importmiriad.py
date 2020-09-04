#
# stub function definition file for docstring parsing
#

def importmiriad(mirfile, vis='', tsys=False, spw=[-1], vel='', linecal=False, wide=[''], debug=0):
    r"""
Convert a Miriad visibility file into a CASA MeasurementSet

Parameters
   - **mirfile** (string) - Name of input Miriad visibility file [1]_
   - **vis** (string='') - Name of output MeasurementSet [2]_
   - **tsys** (bool=False) - Use the Tsys to set the visibility weights [3]_
   - **spw** (intArray=[-1]) - Select spectral window/channels [4]_
   - **vel** (string='') - Select velocity reference (TOPO,LSRK,LSRD) [5]_
   - **linecal** (bool=False) - (CARMA) Apply line calibration [6]_
   - **wide** (intArray=['']) - (CARMA) Select wide window averages [7]_
   - **debug** (int=0) - Display increasingly verbose debug messages [8]_


Description
   The task **importmiriad** allows one to import visibilities in the
   MIRIAD data format to be converted to a MeasurementSet. The task
   has mainly been tested on data from the ATCA and CARMA telescopes
   and the inputs are:

   ::

      #In CASA
      # importmiriad :: Convert a Miriad visibility file into a CASA
      MeasurementSet
      mirfile       =     ''    # Name of input Miriad
      visibility file
      vis         =     ''    # Name of output
      MeasurementSet
      tsys        =   False    # Use the Tsys to set
      the visibility
                          #  weights
      spw         =    [-1]    # Select spectral
      windows, default is
                          #  all
      vel         =     ''    # Select velocity
      reference
                          #  (TOPO,LSRK,LSRD)
      linecal       =   False    # (CARMA) Apply line
      calibration
      wide        =     []    # (CARMA) Select wide
      window averages
      debug        =     0    # Display increasingly
      verbose debug
                          #  messages

   -  The *mirfile* parameter specifies a single MIRIAD visibility
      dataset which**must have any calibration done in MIRIAD
      already applied to it**.MIRIADcalibration tables are usually
      applied on the fly within MIRIAD;such steps (e.g., uvaver)
      need to be taken within MIRIAD such that your
      MIRIADvisibilities have the calibration permanently applied.
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




Details
   Explanation of each parameter

.. [1] 
   **mirfile** (string)
      | Name of input Miriad visibility file
      |                      Default: none
      | 
      |                         Example: mirfile='mydata.uv'
.. [2] 
   **vis** (string='')
      | Name of output MeasurementSet
      |                      Default: none
      | 
      |                         Example: vis='mydata.ms'
.. [3] 
   **tsys** (bool=False)
      | Use the Tsys to set the visibility weights
      |                      Default: False
      |                      Options: False|True
.. [4] 
   **spw** (intArray=[-1])
      | Select spectral window/channels
      |                      Default: '' (all spectral windows and channels)
      |            
      |                         Examples:
      |                         spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
      |                         spw='<2';  spectral windows less than 2 (i.e. 0,1)
      |                         spw='0:5~61'; spw 0, channels 5 to 61
      |                         spw='0,10,3:3~45'; spw 0,10 all channels, spw
      |                         3 - chans 3 to 45.
      |                         spw='0~2:2~6'; spw 0,1,2 with channels 2
      |                         through 6 in each.
      |                         spw = '*:3~64'  channels 3 through 64 for all sp id's
      |                         spw = ' :3~64' will NOT work.
.. [5] 
   **vel** (string='')
      | Select velocity reference
      |                      Default: telescope dependent, ATCA -> TOPO, CARMA
      |                      -> LSRK
      |                      Options: TOPO|LSRK|LSRD
      | 
      |                         Example: vel='LSRK'
.. [6] 
   **linecal** (bool=False)
      | (CARMA) Apply line calibration
      |                      Default: False
      |                      Options: False|True
      |  
      |                      Only useful for CARMA data
.. [7] 
   **wide** (intArray=[''])
      | (CARMA) Select wide window averages
      | 
      |                      Select which of the wide-band channels should be loaded 
      |                      Only useful for CARMA data
.. [8] 
   **debug** (int=0)
      | Display increasingly verbose debug messages
      |                      Default: 0
      | 
      |                         Example: debug=1

    """
    pass
