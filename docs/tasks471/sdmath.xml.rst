sdmath -- ASAP SD task for simple arithmetic of spectra -- single dish task
=======================================

Description
---------------------------------------

Task sdmath execute a simple arithmetic (i.e., subtraction, addition, 
multiplication, and division) expression for single dish spectra.
The spectral data file can be any of the formats supported by
ASAP (scantable, MS, rpfits, and SDFITS). In the expression, 
these file names should be put inside of single or double quotes.

You can use variables in the expression. If you want to use, you 
must define varnames dictionary. Name of variables should be simple, 
e.g. V0, V1, etc., to avoid unexpected error. Keys of varnames must 
be name of variables that you used in the expression, and their 
values will be substituted for variables in the expression. Allowed 
type for the value is numerical values, one- or two-dimensional lists 
(Python list or numpy.ndarray), and filename strings that indicate 
spectral data or ASCII text, which is space-separated list of 
numerical values consisting of adequate number of rows and columns. 
In case you give a list of file names in infiles, they are 
automatically referred to as IN0, IN1, etc. in expr and you can not 
use IN0, IN1, etc. as variable names in varnames.
  


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - infiles
     - :code:`numpy.array( [  ] )`
     - 
   * - expr
     - :code:`''`
     - 
   * - varnames
     - :code:`*UNKNOWN*`
     - 
   * - antenna
     - :code:`int(0)`
     - 
   * - fluxunit
     - :code:`''`
     - 
   * - telescopeparam
     - :code:`''`
     - 
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - scan
     - :code:`''`
     - 
   * - pol
     - :code:`''`
     - 
   * - outfile
     - :code:`''`
     - 
   * - outform
     - :code:`'ASAP'`
     - output file format [\'ASAP\', \'MS2\', \'ASCII\', or \'SDFITS\']
   * - overwrite
     - :code:`False`
     - 


Parameter Explanations
=======================================



infiles
---------------------------------------

:code:`numpy.array( [  ] )`

a list of names of input SD datasets


expr
---------------------------------------

:code:`''`

mathematical expression using spectra


varnames
---------------------------------------

:code:`*UNKNOWN*`

dictionary of variables and their values used in expr


antenna
---------------------------------------

:code:`int(0)`

select an antenna name or ID, e.g. \'PM03\' (only effective for MS input)


fluxunit
---------------------------------------

:code:`''`

units of the flux (\'\'=current)


telescopeparam
---------------------------------------

:code:`''`

parameters of telescope for flux conversion (see examples in help)


field
---------------------------------------

:code:`''`

select data by field IDs and names, e.g. \'3C2*\' (\'\'=all)


spw
---------------------------------------

:code:`''`

select data by IF IDs (spectral windows), e.g. \'3,5,7\' (\'\'=all)


scan
---------------------------------------

:code:`''`

select data by scan numbers, e.g. \'21~23\' (\'\'=all)


pol
---------------------------------------

:code:`''`

select data by polarization IDs, e.g. \'0,1\' (\'\'=all)


outfile
---------------------------------------

:code:`''`

name of output file (must be specified)


outform
---------------------------------------

:code:`'ASAP'`

output file format (See a WARNING in help)


overwrite
---------------------------------------

:code:`False`

overwrite the output file if already exists [True, False]




