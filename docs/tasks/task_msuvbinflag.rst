

.. _Description:

Description
   .. warning:: **WARNING**: This task is currently experimental.
   
   **msuvbinflag** An algorithm to identify outliers in the UV plane 
   through a defined uniform grid by msuvbin. Both msuvbin and msuvbinflag 
   tasks are experimental. Msuvbinflag is automatic flagging algorithm for 
   the identification of Radio Frequency Interference (RFI) in the UV plane 
   for experimental purpose. The visibilities in input CASA Measurements Set (MS) 
   is first gridded into an uniformed UV plane with msuvbin task. 
   Then the significant outliers are computed for entire UV grid based on 
   the criterional settings configurable by users for three method options: 
   radian, diffential and regional mean. 
   After computing flags for each visibility in each uniformed UV bin, 
   the visibilities are transformed reverslity back to original order in the 
   MS file with flagging information. The first msuvbinflag release version 
   is for NRAO internal use to evaluate the speed and numarical 
   analysis performance.   


   
   .. rubric:: Parameter descriptions
   
   *vis*

   Name of input visibility file
   
   *field*
   
   Field name list; note that this position will define the phase
   center of the output uv grid
   
   *spw*
   
   Spectral window selection
   
   *taql*
   
   TaQl expression for data selection (see  `Data Selection in a
   Measurement
   Set <../../notebooks/visibility_data_selection.ipynb>`__  or `CASAcore NOTE
   199: Table Query
   Language <https://casacore.github.io/casacore-notes/199.html>`__  for
   more information)
   
   *outvis*
   
   Name of output grid
   
   *phasecenter*
   
   Phase center of the grid, to be used when the phase center of the
   selected field is not the desired output phase center.
   Example: phasecenter='J2000 18h03m04 -20d00m45.1'
   
   *nx*
   
   Number of pixels along the x axis of the grid. Default: 1000
   
   *ny*
   
   Number of pixels along the y axis of the grid. Default: 1000
   
   *cell*
   
   Cellsize of the grid (given in sky units). Default: '1arcsec'
   
   *ncorr*
   
   Number of correlation/polarization plane in uv grid (allowed 1, 2,
   4). For example, if the input data set has the correlations RR and
   LL, and *ncorr* =1, then the output uv grid will be written as
   Stokes I. If *ncorr=* 2, then the output grid will have both the
   RR and LL correlations. Default: 1
   
   *nchan*
   
   Number of spectral channels in the output uv grid. Default: 1
   
   *fstart*
   
   Frequency of the first channel. Default: '1GHz' (the user needs to
   give a useful input here)
   
   *fstep*
   
   Width of spectral channel. Default: '1kHz'
   
   *wproject*
   
   Do wprojection correction while gridding. Default: False
   
   *memfrac*
   
   Controls how much of computer's memory is available for gridding.
   Default=0.5
   

.. _Examples:

Examples
   
   

.. _Development:

Development
   No additional development details

