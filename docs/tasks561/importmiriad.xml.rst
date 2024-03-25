importmiriad -- Convert a Miriad visibility file into a CASA MeasurementSet -- import/export task
=======================================

Description
---------------------------------------

Convert a Miriad visibility file into a CASA MeasurementSet with
optional selection of spectral windows and weighting scheme
        


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - mirfile
     - :code:`''`
     - Name of input Miriad visibility file
   * - vis
     - :code:`''`
     - Name of output MeasurementSet
   * - tsys
     - :code:`False`
     - Use the Tsys to set the visibility weights
   * - spw
     - :code:`numpy.array( [  ] )`
     - Select spectral window/channels
   * - vel
     - :code:`''`
     - Select velocity reference (TOPO,LSRK,LSRD)
   * - linecal
     - :code:`False`
     - (CARMA) Apply line calibration
   * - wide
     - :code:`numpy.array( [  ] )`
     - (CARMA) Select wide window averages
   * - debug
     - :code:`int(0)`
     - Display increasingly verbose debug messages


Parameter Explanations
=======================================



mirfile
---------------------------------------

:code:`''`

Name of input Miriad visibility file
                     Default: none

                        Example: mirfile='mydata.uv'



vis
---------------------------------------

:code:`''`

Name of output MeasurementSet
                     Default: none

                        Example: vis='mydata.ms'



tsys
---------------------------------------

:code:`False`

Use the Tsys to set the visibility weights
                     Default: False
                     Options: False|True



spw
---------------------------------------

:code:`numpy.array( [  ] )`

Select spectral window/channels
                     Default: '' (all spectral windows and channels)
           
                        Examples:
                        spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
                        spw='<2';  spectral windows less than 2 (i.e. 0,1)
                        spw='0:5~61'; spw 0, channels 5 to 61
                        spw='0,10,3:3~45'; spw 0,10 all channels, spw
                        3 - chans 3 to 45.
                        spw='0~2:2~6'; spw 0,1,2 with channels 2
                        through 6 in each.
                        spw = '*:3~64'  channels 3 through 64 for all sp id's
                        spw = ' :3~64' will NOT work.



vel
---------------------------------------

:code:`''`

Select velocity reference
                     Default: telescope dependent, ATCA -> TOPO, CARMA
                     -> LSRK
                     Options: TOPO|LSRK|LSRD

                        Example: vel='LSRK'



linecal
---------------------------------------

:code:`False`

(CARMA) Apply line calibration
                     Default: False
                     Options: False|True
 
                     Only useful for CARMA data



wide
---------------------------------------

:code:`numpy.array( [  ] )`

(CARMA) Select wide window averages

                     Select which of the wide-band channels should be loaded 
                     Only useful for CARMA data



debug
---------------------------------------

:code:`int(0)`

Display increasingly verbose debug messages
                     Default: 0

                        Example: debug=1





