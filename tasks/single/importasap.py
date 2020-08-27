#
# stub function definition file for docstring parsing
#

def importasap(infile, outputvis='', flagbackup=True, overwrite=False, parallel=False):
    """
Convert ASAP Scantable data  into a CASA visibility file (MS)

| Convert ASAP Scantable data  into a CASA visibility file (MS)

Parameters
----------
infile : string
   Name of input ASAP Scantable data
outputvis : string
   Root name of the ms to be created. Note the .ms is NOT added.
flagbackup : bool
   Back up flag column before applying flags.
overwrite : bool
   Over write an existing MS(s)
parallel : bool
   Turn on parallel execution

Other Parameters
----------

Notes
-----





   Convert ASAP Scantable data into a CASA visibility file (MS).



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

    """
    pass
