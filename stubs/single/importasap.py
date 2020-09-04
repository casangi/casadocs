#
# stub function definition file for docstring parsing
#

def importasap(infile, outputvis='', flagbackup=True, overwrite=False, parallel=False):
    r"""
Convert ASAP Scantable data  into a CASA visibility file (MS)

Parameters
   - **infile** (string) - Name of input ASAP Scantable data [1]_
   - **outputvis** (string='') - Root name of the ms to be created. Note the .ms is NOT added. [2]_
   - **flagbackup** (bool=True) - Back up flag column before applying flags. [3]_
   - **overwrite** (bool=False) - Over write an existing MS(s) [4]_
   - **parallel** (bool=False) - Turn on parallel execution [5]_


Description
   This is the task to convert single-dish scantable data format
   (ATNF Spectral Analysis Package, ASAP) into a CASA visibility data
   format (MeasurementSet, MS) to enable processing of
   scantable-format datasets (e.g. Parkes, Mopra Telescopes at ATNF).

   Prior to CASA 4.5, most of the ALMA data reduction process was
   done in Scantable format. Later CASA versions shifted towards
   eliminating the dependence on Scantable format. From CASA 5.0, no
   processing/reduction is done in Scantable format, and data with
   Scantable format must be transformed into MS format before
   reduction.




Details
   Explanation of each parameter

.. [1] 
   **infile** (string)
      | Name of input ASAP Scantable data
      |                      Default: none
      | 
      |                         Example: infile='mydata.asap'
.. [2] 
   **outputvis** (string='')
      | Name of output visibility file
      |                      Default: '' (same as vis)
      | 
      |                         Example: outputvis='myms.ms'
      | 
      |                      NOTE: Note the .ms is NOT added
.. [3] 
   **flagbackup** (bool=True)
      | Back up flag column before applying flags.
      |                      Default: True
      |                      Options: True|False
.. [4] 
   **overwrite** (bool=False)
      | Over write an existing MS(s)
      |                      Default: False (do not overwrite)
      |                      Options: False|True
.. [5] 
   **parallel** (bool=False)
      | Turn on parallel execution
      |                      Default: False (serial execution)
      |                      Options: False|True

    """
    pass
