#
# stub function definition file for docstring parsing
#

def plotprofilemap(imagename, figfile='', overwrite=False, transparent=False, pol=0, spectralaxis='', restfreq='', plotrange='', title='', linecolor='b', linestyle='-', linewidth=0.2, separatepanel=True, plotmasked='empty', maskedcolor='gray', showaxislabel=False, showtick=False, showticklabel=False, figsize='', numpanels=''):
    r"""
Makes profile map.

Parameters
   - **imagename** (string) - Input image name (CASA image or FITS) [1]_
   - **figfile** (string='') - Output figure name [2]_
   - **pol** (int=0) - Polarization component to be plotted [5]_
   - **spectralaxis** (string='') - Type of spectral axis [6]_

      .. raw:: html

         <details><summary><i> spectralaxis = velocity </i></summary>

      - **restfreq** (string='') - Rest frequency [7]_

      .. raw:: html

         </details>
   - **plotrange** (string='') - Spectral axis range to plot [8]_
   - **title** (string='') - Title of the plot [9]_
   - **linecolor** (string='b') - Line color [10]_
   - **linestyle** (string='-') - Line style [11]_
   - **linewidth** (double=0.2) - Line width in points [12]_
   - **separatepanel** (bool=True) - Separate plots [13]_
   - **plotmasked** (string='empty') - Masked data handling [14]_

      .. raw:: html

         <details><summary><i> plotmasked = plot </i></summary>

      - **maskedcolor** (string='gray') - Line color for masked data [15]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> plotmasked = zero </i></summary>

      - **maskedcolor** (string='gray') - Line color for masked data [15]_

      .. raw:: html

         </details>
   - **showaxislabel** (bool=False) - Show axis labels on the bottom left panel [16]_
   - **showtick** (bool=False) - Show axis ticks [17]_

      .. raw:: html

         <details><summary><i> showtick = True </i></summary>

      - **showticklabel** (bool=False) - Show axis tick labels on the bottom left panel [18]_

      .. raw:: html

         </details>
   - **figsize** (string='') - Size of the figure [19]_
   - **numpanels** (string='') - Number of panels [20]_


Description
   The **plotprofilemap** makes a spectral profile map from a
   specified image. The task accepts both a CASA image or a FITS cube
   as an input. Output is to the screen, or to image file (specified
   with *figfile*).

   It is necessary to specify existing CASA image or FITS cube as an
   *imagename*. Otherwise, the task will fail. If *figfile* is
   specified, the profile map is saved as an PNG image. Please set
   *overwrite* to False if you don't want to overwrite existing file.

   Selection of data is enabled through polarisation only (since this
   task operates in image data, not measurement set format).

   The plot parameters can be manipulated via *plotrange*, *title*,
   *separatepanel*, *showaxislabel*, *showtick*, *figsize*; the line
   style can be specified through *linecolor*, *linestyle*,
   *linewidth*, and the actual number of sub-plots is specificed with
   *numpanels*.

   The number of panels along the horizontal and vertical direction
   can be specified via the parameter *numpanels*. It should be a
   string containing numerical values indicating the number of
   panels. If only one number is given it will be applied to both
   axes. If you want to provide different numbers to horizontal and
   vertical axes, you should give two numbers as a string separated
   by comma.

   | If the number of panels is less than the number of pixels of
     input image, more than one pixel is assigned to one panel. In
     that case, spectra to be shown are the average of the assigned
     spectra in each pixel.
   |  
   | Default value for *numpanels* is empty string ('') which
     corresponds to an auto calculation of the number of panels based
     on the number of pixels of input image. Formulas for the number
     of horizontal and vertical panels, nh and nv, are as follows:

   ::

      npanel = min(max(nx, ny), 8)
      step = (max(nx, ny) - 1) / npanel + 1
      nh = nx / step + 1
      nv = ny / step + 1

   where nx and ny are the number of pixels along direction axes. In
   the above calculation, upper limit for nh and nv is 9.

   The output image is directed to screen by default, but can be sent
   to a file image by naming a file with '*figfile'*. The image can
   also be made with a transparent background: *transparent=True*

   The behaviour of the task in the context of masked data (i.e. how
   to show data that are masked) is enabled with *plotmasked*, which
   can have values;

   ::

      'empty' (default; show empty panel)
      'zero' (plot zero level)
      'none' (show nothing)
      'text' (show text indicating 'NO DATA')
      'plot' (plot masked data with different color specified by maskedcolor)




Details
   Explanation of each parameter

.. [1] 
   **imagename** (string)
      | Input image name (CASA image or FITS)
.. [2] 
   **figfile** (string='')
      | Output figure name
.. [3] 
   **overwrite** (bool=False)
      | Overwrite existing figfile
.. [4] 
   **transparent** (bool=False)
      | Output transparent figure
.. [5] 
   **pol** (int=0)
      | Polarization component to be plotted
.. [6] 
   **spectralaxis** (string='')
      | Type of spectral axis
.. [7] 
   **restfreq** (string='')
      | Rest frequency
.. [8] 
   **plotrange** (string='')
      | Spectral axis range to plot
.. [9] 
   **title** (string='')
      | Title of the plot
.. [10] 
   **linecolor** (string='b')
      | Line color
.. [11] 
   **linestyle** (string='-')
      | Line style
.. [12] 
   **linewidth** (double=0.2)
      | Line width in points
.. [13] 
   **separatepanel** (bool=True)
      | Separate plots
.. [14] 
   **plotmasked** (string='empty')
      | Masked data handling
.. [15] 
   **maskedcolor** (string='gray')
      | Line color for masked data
.. [16] 
   **showaxislabel** (bool=False)
      | Show axis labels on the bottom left panel
.. [17] 
   **showtick** (bool=False)
      | Show axis ticks
.. [18] 
   **showticklabel** (bool=False)
      | Show axis tick labels on the bottom left panel
.. [19] 
   **figsize** (string='')
      | Size of the figure
.. [20] 
   **numpanels** (string='')
      | Number of panels

    """
    pass
