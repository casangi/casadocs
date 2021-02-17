

.. _Description:

Description
   The **apparentsens** task calculates the point source sensitivity
   for the specified selected data, and according to the desired
   imaging geometry and uv grid weighting. The calculation is
   performed solely using the weight information stored in the MS
   WEIGHT column (or WEIGHT_SPECTRUM, if present), and as adjusted by
   the net imaging weighting function (natural, uniform, robust,
   taper, etc.). Therefore, it is assumed that the MS WEIGHTs have
   been properly initialized and calibrated along with the visibility
   data. As long as the WEIGHTs are in the inverse square units of
   the visibilities (i.e., inverse variance weights), the calculation
   should yield a reasonably accurate theoretical imaging sensitivity
   for data at any stage of the calibration (though data at early and
   intermediate stages of calibration may not be sufficiently
   coherent for imaging at high–or even modest–fidelity).
   
   Two values are returned in a dictionary and reported in the
   logger. First, the apparent sensitivity (in the units implied by
   the WEIGHTs’ units), for the specified imaging geometry and
   weighting scheme (dictionary key: 'effSens'). Second, a unitless
   factor describing the ratio of the apparent sensitivity to that
   obtained with pure ’natural’ weighting (the nominal maximum
   possible sensitivity; dictionary key: 'relToNat'). When ’natural’
   weighting is selected, this ratio factor will be precisely 1.0;
   all other weighting choices will yield an apparent sensitivity
   ratio greater than 1.0.  I.e., all non-natural weighting schemes
   are *less* sensitive (higher rms) than natural. 
   
   Currently, **apparentsens** reports only the continuum sensitivity
   for the selected data, and in particular, for the aggregate
   bandwidth indicated by the spectral window selection. The
   calculation further assumes that the visibility samples are each
   entirely independent, i.e., that there are no redundant samples
   such as would occur for overlapping spectral windows.  If the
   per-channel visibility weights reflect their own isolated
   sensitivity, the reported *continuum* sensitivity will be
   over-estimated if the data have been smoothed (i.e., Hanning
   smoothed channels individually have sensitivity a factor 8/3 times
   their apparent bandwidth, and this factor is not yet accounted for
   when forming the continuum sensitivity estimate).  
   
   A future version of **apparentsens** will support reporting a
   sensitivity spectrum for the spectral line case. For now, spectral
   line sensitivity may be reasonably estimated by dividing the
   reported continuum sensitivity by the square root of the
   fractional bandwidth of a single image channel, or by selecting a
   bandwidth matching the width of a single image channel.   In
   either case, sufficient care should be applied with respect to the
   additional per-channel sensitivity introduced by having smoothed
   (e.g., Hanning) the visilbility, as described above.
   
    
   
   .. rubric:: Parameter descriptions
      
   
   The **apparentsens** task use the same data selection as the
   **tclean** task, as well as a subset of the image geometry and
   weighting parameters.  All operate in essentially the same way
   (with exceptions noted below), and the **tclean** documentation
   should be consulted for details on how to set them.
   
   - *specmode* : For now, it is only meaningful to use specmode='mfs'.  Use of
     specmode='cube' will be supported in future (and a apparent
     sensitivity spectrum will be returned and reported).
   
   - *stokes* : Currently, **apparentsens** will report the sensitivity for
     stokes='I' only.  Support for polarization-dependent sensitivity
     estimates will be added in future.

.. _Examples:

Examples
   For a MeasurementSet 'calibrated.ms', the continuum imaging
   sensitivity using natural weighting for field id 3 and a subset of
   channels in spw 0 can be obtained as follows:
   
   ::
   
      aps=apparentsens(vis='calibrated.ms',
                       spw='0:0~30;40~80',
                       field='3',
                       specmode='mfs',
                       cell='0.007arcsec',imsize=[2048, 2048],
                       weighting='natural')

      print aps
   
    
   
   The returned dictionary is (also reported in logger):
   
   ::
   
      {'relToNat': 1.0000000000089664, 'effSens':
      1.0022319615408699e-05}
   
   Note that the 'relToNat' factor is 1.0.
   
   For the same MS and selection, but with Briggs weighting:
   
   ::
   
      aps=apparentsens(vis='calibrated.ms',
                       spw='0:0~30;40~80',
                       field='3',
                       specmode='mfs',
                       cell='0.007arcsec',imsize=[2048, 2048],
                       weighting='briggs',
                       robust=0.5)

      print aps
   
   The returned dictionary is (also reported in logger):
   
   ::
   
      {'relToNat': 1.1450564209993626, 'effSens':
      1.1476121428828694e-05}
   
   Note that Briggs weighting is ~14% less sensitive in this case.
   

.. _Development:

Development
   No additional development details
