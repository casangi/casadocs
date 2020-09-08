#
# stub function definition file for docstring parsing
#

def importasap(infile, outputvis='', flagbackup=True, overwrite=False, parallel=False):
    r"""
Convert ASAP Scantable data  into a CASA visibility file (MS)

Parameters
   - infile_ (string) - Name of input ASAP Scantable data
   - outputvis_ (string='') - Root name of the ms to be created. Note the .ms is NOT added.
   - flagbackup_ (bool=True) - Back up flag column before applying flags.
   - overwrite_ (bool=False) - Over write an existing MS(s)
   - parallel_ (bool=False) - Turn on parallel execution


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

.. _infile:

   .. rubric:: infile

   | Name of input ASAP Scantable data
   |                      Default: none
   | 
   |                         Example: infile='mydata.asap'

.. _outputvis:

   .. rubric:: outputvis

   | Name of output visibility file
   |                      Default: '' (same as vis)
   | 
   |                         Example: outputvis='myms.ms'
   | 
   |                      NOTE: Note the .ms is NOT added

.. _flagbackup:

   .. rubric:: flagbackup

   | Back up flag column before applying flags.
   |                      Default: True
   |                      Options: True|False

.. _overwrite:

   .. rubric:: overwrite

   | Over write an existing MS(s)
   |                      Default: False (do not overwrite)
   |                      Options: False|True

.. _parallel:

   .. rubric:: parallel

   | Turn on parallel execution
   |                      Default: False (serial execution)
   |                      Options: False|True


    """
    pass
