#
# stub function definition file for docstring parsing
#

def sdpolaverage(infile, datacolumn='data', antenna='', field='', spw='', timerange='', scan='', intent='', polaverage='', outfile=''):
    """
Average SD spectra over polarisation

| The task sdpolaverage exports data averaged over different polarisations.
|    Scope of this task is to obtain Stokes I from orthogonal autocorrelation 
|    pairs (XXYY/LLRR). Available options include:
|
|    * '' (blank string as the default: polarisation averaging turned off)
|    * stokes
|    * geometric

Parameters
----------
infile : string
   name of input SD dataset
datacolumn : string
   name of data column to be used ["data", "float_data", or "corrected_data"]
antenna : string
   select data by antenna name or ID, e.g. "PM03"
field : string
   select data by field IDs and names, e.g. "3C2*" (""=all)
spw : string
   select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all)
timerange : string
   select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)
scan : string
   select data by scan numbers, e.g. "21~23" (""=all)
intent : string
   select data by observational intent, e.g. "*ON_SOURCE*" (""=all)
polaverage : string
   polarization averaging mode ("", "stokes" or "geometric").
outfile : string
   name of output file

Other Parameters
----------

Notes
-----





   Averaging over different polarizations for Single Dish MS data



      Task **sdpolaverage** is used to export Single Dish MS data
      averaged over different polarizations, to obtain Stokes I from
      orthogonal autocorrelation pairs (XXYY/LLRR). 

      .. rubric:: Polarization Average
         :name: polarization-average

      Two modes of polarizaton averaging are available. One is 'stokes'
      which is an average based on a formulation of Stokes parameter. In
      this mode, averaged data is calculated by (XX + YY) / 2 or (RR +
      LL) / 2. The other option is 'geometric', which is a conventional
      way of averaging in the field of single-dish data reduction; the
      output data is given by weighted average of XX and YY, or RR and
      LL.

    """
    pass
