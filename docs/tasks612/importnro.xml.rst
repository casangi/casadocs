importnro -- Convert NOSTAR data into a CASA visibility file (MS) -- single dish, import/export task
=======================================

Description
---------------------------------------

Task importnro enables one to convert the data obtained with the
NRO45m telescope into the CASA MS2 format. At this moment, only the
OTF data (NOSTAR data) obtained with the SAM45 spectrometer is
supported, and the OTF data obtained with the other spectrometers
(e.g., AOS) and the PSW data (NEWSTAR data) are outside of scope
(Jan./25/2017)



Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - infile
     - :code:`''`
     - Name of input NOSTAR data
   * - outputvis
     - :code:`''`
     - Root name of the ms to be created. Note the .ms is NOT added
   * - overwrite
     - :code:`False`
     - Over write an existing MS(s)
   * - parallel
     - :code:`False`
     - Turn on parallel execution


Parameter Explanations
=======================================



infile
---------------------------------------

:code:`''`

Name of input NOSTAR data
                     Default: none



outputvis
---------------------------------------

:code:`''`

Root name of the ms to be created. Note the .ms is NOT
added 
                     Default: none

                        Example: outputvis='myms.ms'



overwrite
---------------------------------------

:code:`False`

Over write an existing MS(s)
                     Default: False (do not overwrite)
                     Options: False|True



parallel
---------------------------------------

:code:`False`

Turn on parallel execution
                     Default: False (serial execution)
                     Options: False|True





