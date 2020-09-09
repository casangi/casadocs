#
# stub function definition file for docstring parsing
#

def sdsmooth(infile, datacolumn='data', antenna='', field='', spw='', timerange='', scan='', pol='', intent='', reindex=True, kernel='gaussian', kwidth=5, outfile='', overwrite=False):
    r"""
Smooth spectral data 

Parameters
   - infile_ (string) - name of input SD dataset
   - datacolumn_ (string='data') - name of data column to be used ["data", "float_data", or "corrected"]
   - antenna_ (string='') - select data by antenna name or ID, e.g. "PM03"
   - field_ (string='') - select data by field IDs and names, e.g. "3C2*" (""=all)
   - spw_ (string='') - select data by spectral window IDs, e.g. "3,5,7" (""=all)
   - timerange_ (string='') - select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)
   - scan_ (string='') - select data by scan numbers, e.g. "21~23" (""=all)
   - pol_ (string='') - select data by polarization IDs, e.g. "0,1" (""=all)
   - intent_ (string='') - select data by observational intent, e.g. "*ON_SOURCE*" (""=all)
   - reindex_ (bool=True) - Re-index indices in subtables based on data selection
   - kernel_ (string='gaussian') - spectral smoothing kernel type

      .. raw:: html

         <details><summary><i> kernel = gaussian </i></summary>

      - kwidth_ (int=5) - smoothing kernel width in channel

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> kernel = boxcar </i></summary>

      - kwidth_ (int=5) - smoothing kernel width in channel

      .. raw:: html

         </details>
   - outfile_ (string='') - name of output file
   - overwrite_ (bool=False) - overwrite the output file if already exists [True, False] 


Description
   Task **sdsmooth** performs smoothing along the spectral axis using
   a user-specified smoothing kernel. Currently, 'Gaussian' and
   'boxcar' kernels are supported.

   The default Kernel shape is 'Gaussian'. The width of the function
   is specified with the*kwidth* parameter, in number of channels.

   Standard data selection parameters are used: *antenna*, *field*,
   *spw*, *scan*, *timerange*, *pol,* and *intent*.

   

   Weights are propagated to smoothed spectra following:

   :math:`W^{k}_{\rm out} = \frac{ (\sum_{i=1}^{n} c_{i})^{2} } { (\sum_{i=1}^{n} c^{2}_{i} / W^{j+i}_{\rm inp}) }`
    ,

   where :math:`W` is the input/output weight, :math:`c`is the
   spectral smoothing kernel originated from a channel
   :math:`k`where the weight is evaluated, and :math:`n`is the
   width of the spectral smoothing kernel in channels. In the case of
   Gaussian, :math:`n`corresponds to FWHM in channels.

   | 
   |


.. _infile:

infile (string)
   | name of input SD dataset

.. _datacolumn:

datacolumn (string='data')
   | name of data column to be used ["data", "float_data", or "corrected"]

.. _antenna:

antenna (string='')
   | select data by antenna name or ID, e.g. "PM03"

.. _field:

field (string='')
   | select data by field IDs and names, e.g. "3C2*" (""=all)

.. _spw:

spw (string='')
   | select data by spectral window IDs, e.g. "3,5,7" (""=all)

.. _timerange:

timerange (string='')
   | select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)

.. _scan:

scan (string='')
   | select data by scan numbers, e.g. "21~23" (""=all)

.. _pol:

pol (string='')
   | select data by polarization IDs, e.g. "0,1" (""=all)

.. _intent:

intent (string='')
   | select data by observational intent, e.g. "*ON_SOURCE*" (""=all)

.. _reindex:

reindex (bool=True)
   | Re-index indices in subtables based on data selection

.. _kernel:

kernel (string='gaussian')
   | spectral smoothing kernel type

.. _kwidth:

kwidth (int=5)
   | smoothing kernel width in channel

.. _outfile:

outfile (string='')
   | name of output file

.. _overwrite:

overwrite (bool=False)
   | overwrite the output file if already exists


    """
    pass
