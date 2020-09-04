#
# stub function definition file for docstring parsing
#

def msuvbin(vis, field='', spw='', taql='', outvis='', phasecenter='', nx=1000, ny=1000, cell='1arcsec', ncorr=1, nchan=1, fstart='1GHz', fstep='1kHz', wproject=False, memfrac=0.5):
    r"""
grid the visibility data onto a defined uniform grid (in the form of an ms); multiple MS\'s can be done onto the same grid

Parameters
   - **vis** (string) -  [1]_
   - **field** (string='') -  [2]_
   - **spw** (string='') -  [3]_
   - **taql** (string='') -  [4]_
   - **outvis** (string='') -  [5]_
   - **phasecenter** (string='') -  [6]_
   - **nx** (int=1000) -  [7]_
   - **ny** (int=1000) -  [8]_
   - **cell** (string='1arcsec') -  [9]_
   - **ncorr** (int=1) -  [10]_
   - **nchan** (int=1) -  [11]_
   - **fstart** (string='1GHz') -  [12]_
   - **fstep** (string='1kHz') -  [13]_
   - **wproject** (bool=False) -  [14]_
   - **memfrac** (double=0.5) -  [15]_


Description
   .. warning:: **WARNING**: This task is currently experimental.

   .. rubric:: Summary
      

   **msuvbin** is a uv gridding task. It is primarily designed to be
   used for large volumes of data from multiple observing epochs that
   need to be imaged together in order to obtain a final image
   product for the target source or field of interest. One way of
   proceeding with such large multi-epoch data is to image each epoch
   separately and average the images afterward. Instead, **msuvbin**
   averages the visibilities on a common uv grid, then the resulting
   data product can be imaged using the task **clean** or **tclean**.
   Averaging such uv data into a common uv grid first has several
   conveniences and advantages, such as easily doing the proper
   weighted average. More details on this task can be found in the
   `EVLA Memo
   198 <https://library.nrao.edu/public/memos/evla/EVLAM_198.pdf>`__,which
   explains the current implementation in **msuvbin** and its
   limitations. In particular, note the issue/limitation of creating
   a uv grid with wprojection and then using Cotton-Schwab major
   cycles to image it; see the EVLA Memo 198 for more details.

   

   .. rubric:: Parameter descriptions
      

   .. rubric:: *vis*
      

   Name of input visibility file

   .. rubric:: *field*
      

   Field name list; note that thisposition will define the phase
   center of the output uv grid

   .. rubric:: *spw
      *
      

   Spectral window selection

   .. rubric:: *taql* 
      

   TaQl expression for data selection (see `Data Selection in a
   Measurement
   Set <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__ or `CASAcoreNOTE
   199:Table Query
   Language <https://casacore.github.io/casacore-notes/199.html>`__ for
   more information)

   .. rubric:: *outvis*
      

   Name of output grid

   .. rubric:: *phasecenter*
      

   Phase center of the grid,to be used when the phase center of the
   selected field is not the desired output phase center.
   Example:phasecenter='J2000 18h03m04 -20d00m45.1'

   .. rubric:: *nx*
      

   Number of pixels along the x axis of the grid. Default: 1000

   .. rubric:: *ny*
      

   Number of pixels along the y axis of the grid. Default: 1000

   .. rubric:: *cell*
      

   Cellsize of the grid (given in sky units). Default: '1arcsec'

   .. rubric:: *ncorr*
      

   Number of correlation/polarization plane in uv grid (allowed 1, 2,
   4). For example, if the input data set has the correlations RR and
   LL, and *ncorr* =1, then the output uv grid will be written as
   Stokes I. If *ncorr=* 2, then the output grid will have both the
   RR and LL correlations. Default: 1

   .. rubric:: *nchan*
      

   Number of spectral channels in the output uv grid. Default: 1

   .. rubric:: *fstart*
      

   Frequency of the first channel. Default: '1GHz' (the user needsto
   givea useful input here)

   .. rubric:: *fstep*
      

   Width of spectral channel. Default: '1kHz'

   .. rubric:: *wproject*
      

   Do wprojection correction while gridding. Default: False

   .. rubric:: *memfrac*
      

   Controls how much of computer's memory is available forgridding.
   Default=0.5




Details
   Explanation of each parameter

.. [1] 
   **vis** (string)
      | Name of input visibility file (MS)
.. [2] 
   **field** (string='')
      | Field selection of input ms
.. [3] 
   **spw** (string='')
      | Spw selection
.. [4] 
   **taql** (string='')
      | TaQl string for data selection
.. [5] 
   **outvis** (string='')
      | name of output uvgrid
.. [6] 
   **phasecenter** (string='')
      | phase center of uv grid
.. [7] 
   **nx** (int=1000)
      | Number of pixels of grid along the x-axis
.. [8] 
   **ny** (int=1000)
      | Number of pixels of grid along the y-axis
.. [9] 
   **cell** (string='1arcsec')
      | pixel cell size defined in sky dimension
.. [10] 
   **ncorr** (int=1)
      | number of correlations to store in grid
.. [11] 
   **nchan** (int=1)
      | Number of spectral channels in grid
.. [12] 
   **fstart** (string='1GHz')
      | Frequency of first spectral channel
.. [13] 
   **fstep** (string='1kHz')
      | spectral channel width
.. [14] 
   **wproject** (bool=False)
      | Do wprojection correction while gridding
.. [15] 
   **memfrac** (double=0.5)
      | Limit how much of memory to use

    """
    pass
