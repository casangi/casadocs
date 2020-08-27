#
# stub function definition file for docstring parsing
#

def sdsmooth(infile, datacolumn='data', antenna='', field='', spw='', timerange='', scan='', pol='', intent='', reindex=True, kernel='gaussian', kwidth=5, outfile='', overwrite=False):
    """
Smooth spectral data 

| Task sdsmooth performs smoothing along spectral axis using user-specified 
|  smoothing kernel. Currently gaussian and boxcar kernels are supported.

Parameters
----------
infile : string
   name of input SD dataset
datacolumn : string
   name of data column to be used ["data", "float_data", or "corrected"]
antenna : string
   select data by antenna name or ID, e.g. "PM03"
field : string
   select data by field IDs and names, e.g. "3C2*" (""=all)
spw : string
   select data by spectral window IDs, e.g. "3,5,7" (""=all)
timerange : string
   select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)
scan : string
   select data by scan numbers, e.g. "21~23" (""=all)
pol : string
   select data by polarization IDs, e.g. "0,1" (""=all)
intent : string
   select data by observational intent, e.g. "*ON_SOURCE*" (""=all)
reindex : bool
   Re-index indices in subtables based on data selection
kernel : string
   spectral smoothing kernel type
outfile : string
   name of output file
overwrite : bool
   overwrite the output file if already exists [True, False] 

Other Parameters
----------
kwidth : int
   smoothing kernel width in channel

Notes
-----





   Smooth spectral data



      Task **sdsmooth** performs smoothing along the spectral axis using
      a user-specified smoothing kernel. Currently, 'Gaussian' and
      'boxcar' kernels are supported.

      The default Kernel shape is 'Gaussian'. The width of the function
      is specified with the *kwidth* parameter, in number of channels.

      Standard data selection parameters are used: *antenna*, *field*,
      *spw*, *scan*, *timerange*, *pol,* and *intent*.

       

      Weights are propagated to smoothed spectra following:

      :math:`W^{k}_{\rm out} = \frac{ (\sum_{i=1}^{n} c_{i})^{2} } { (\sum_{i=1}^{n} c^{2}_{i} / W^{j+i}_{\rm inp}) } `
         ,

      where :math:`W` is the input/output weight, :math:`c` is the
      spectral smoothing kernel originated from a channel
      :math:`k` where the weight is evaluated, and :math:`n` is the
      width of the spectral smoothing kernel in channels. In the case of
      Gaussian, :math:`n` corresponds to FWHM in channels.

      | 
      |

    """
    pass
