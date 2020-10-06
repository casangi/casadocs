

.. _Description:

Description
   

.. _Examples:

Examples
   task examples
   
   Let's assume we have multi-epoch observations on a particular
   field of interest with measurement sets vis_1.ms, vis_2.ms, ...
   vis_n.ms. The task **msuvbin** needs to be executed n times, one
   for each input data set with all the other parameters that define
   the output data set intact. For instance, for the 1st execution of
   **msuvbin**, one may set the following parameters:
   
   ::
   
      | vis = 'vis_1.ms'
      | field = '0'
      | spw = ''
      | taql = ''
      | outvis = "uvgrid.ms'
      | phasecenter = ''
      | nx = 2048
      | ny = 2048
      | cell = '2.0arcsec'
      | ncorr = 2
      | nchan = 320
      | fstart = "1025.00MHz"
      | fstep = "62.5kHz"
      | wproject = False
      | memfrac = 0.9
   
   Here we note the following:
   
   -  Field '0' was selected from the input data, and its position
      will define the phase center of the output uv grid. If another
      position is desired for the phase center, then the parameter
      *phasecenter* needs to be specified.
   
   -  *nx* and *ny* define the number of the pixels along the x and y
      axes of the grid, respectively. The size of each pixel is
      defined by the parameter *cell*. These would be the same values
      that one would use in the task **clean**/**tclean** for
      *imsize* and *cell* to image the output uv grid, and therefore
      need to be set by taking into account the image that one will
      eventually be making.
   
   -  *ncorr* defines the number of the correlations in the output uv
      grid. If the input data set has the correlations RR and LL, and
      *ncorr* is set to 1, then the output uv grid will be written as
      Stokes I. If *ncorr* is set to 2, then the output grid will
      have both the RR and LL correlations.
   
   -  *nchan* determines the number of channels in the output uv grid
      with a frequency width per channel set by the parameter
      *fstep*. The lowest frequency of the output data is set by the
      parameter *fstart*. Note that **msuvbin** will perform on the
      fly Doppler correction; the resulting grid will be in the LSRK
      frame. The *fstart* value is the starting frequency in the LSRK
      frame. The above example will produce a uv grid with 320
      channels starting at 1025 MHz in LSRK, with each channel having
      a width of 62.5 kHz.
   
   -  *memfrac* may be used to set how much memory the task should
      use. In the above example 90% of the available memory will be
      utilized by the task.
   
   After gridding the 1st data set, the task **msuvbin** will need to
   be executed on the other data sets one at a time by changing the
   *vis* parameter only (i.e., *vis='vis_2.ms'*, then
   *vis='vis_3.ms'*, etc...) and keeping the other parameters intact.
   The task **msuvbin** will perform the proper averaging when
   gridding the data sets on the same uv grid. The volume of the
   output data set stays the same regardless of how many measurement
   sets are added onto the same grid.
   

.. _Development:

Development
   task developer
   
   --CASA Developer--
   
   