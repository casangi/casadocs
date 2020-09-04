#
# stub function definition file for docstring parsing
#

def sdsmooth(infile, datacolumn='data', antenna='', field='', spw='', timerange='', scan='', pol='', intent='', reindex=True, kernel='gaussian', kwidth=5, outfile='', overwrite=False):
    r"""
Smooth spectral data 

Parameters
   - **infile** (string) - name of input SD dataset [1]_
   - **datacolumn** (string='data') - name of data column to be used ["data", "float_data", or "corrected"] [2]_
   - **antenna** (string='') - select data by antenna name or ID, e.g. "PM03" [3]_
   - **field** (string='') - select data by field IDs and names, e.g. "3C2*" (""=all) [4]_
   - **spw** (string='') - select data by spectral window IDs, e.g. "3,5,7" (""=all) [5]_
   - **timerange** (string='') - select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help) [6]_
   - **scan** (string='') - select data by scan numbers, e.g. "21~23" (""=all) [7]_
   - **pol** (string='') - select data by polarization IDs, e.g. "0,1" (""=all) [8]_
   - **intent** (string='') - select data by observational intent, e.g. "*ON_SOURCE*" (""=all) [9]_
   - **reindex** (bool=True) - Re-index indices in subtables based on data selection [10]_
   - **kernel** (string='gaussian') - spectral smoothing kernel type [11]_

      .. raw:: html

         <details><summary><i> kernel = gaussian </i></summary>

      - **kwidth** (int=5) - smoothing kernel width in channel [12]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> kernel = boxcar </i></summary>

      - **kwidth** (int=5) - smoothing kernel width in channel [12]_

      .. raw:: html

         </details>
   - **outfile** (string='') - name of output file [13]_
   - **overwrite** (bool=False) - overwrite the output file if already exists [True, False]  [14]_


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




Details
   Explanation of each parameter

.. [1] 
   **infile** (string)
      | name of input SD dataset
.. [2] 
   **datacolumn** (string='data')
      | name of data column to be used ["data", "float_data", or "corrected"]
.. [3] 
   **antenna** (string='')
      | select data by antenna name or ID, e.g. "PM03"
.. [4] 
   **field** (string='')
      | select data by field IDs and names, e.g. "3C2*" (""=all)
.. [5] 
   **spw** (string='')
      | select data by spectral window IDs, e.g. "3,5,7" (""=all)
.. [6] 
   **timerange** (string='')
      | select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)
.. [7] 
   **scan** (string='')
      | select data by scan numbers, e.g. "21~23" (""=all)
.. [8] 
   **pol** (string='')
      | select data by polarization IDs, e.g. "0,1" (""=all)
.. [9] 
   **intent** (string='')
      | select data by observational intent, e.g. "*ON_SOURCE*" (""=all)
.. [10] 
   **reindex** (bool=True)
      | Re-index indices in subtables based on data selection
.. [11] 
   **kernel** (string='gaussian')
      | spectral smoothing kernel type
.. [12] 
   **kwidth** (int=5)
      | smoothing kernel width in channel
.. [13] 
   **outfile** (string='')
      | name of output file
.. [14] 
   **overwrite** (bool=False)
      | overwrite the output file if already exists

    """
    pass
