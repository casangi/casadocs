#
# stub function definition file for docstring parsing
#

def apparentsens(vis, field='', spw='', intent='', selectdata=True, timerange='', uvrange='', antenna='', scan='', observation='', imsize=100, cell='"1arcsec"', stokes='I', specmode='mfs', weighting='natural', robust=0.5, npixels=0, uvtaper=['']):
    r"""
Imaging sensitivity estimataion

Parameters
   - **vis** ({string, stringArray}) - Name of input visibility file(s)
   - **selectdata** (bool=True) - Enable data selection parameters

      .. raw:: html

         <details><summary><i> selectdata = True </i></summary>

      - **field** ({string, stringArray}='') - field(s) to select
      - **spw** ({string, stringArray}='') - spw(s)/channels to select
      - **timerange** ({string, stringArray}='') - Range of time to select from data
      - **uvrange** ({string, stringArray}='') - Select data within uvrange
      - **antenna** ({string, stringArray}='') - Select data based on antenna/baseline
      - **scan** ({string, stringArray}='') - Scan number range
      - **observation** ({string, int}='') - Observation ID range
      - **intent** ({string, stringArray}='') - Scan Intent(s)

      .. raw:: html

         </details>
   - **imsize** ({int, intArray}=100) - Number of pixels
   - **cell** ({int, double, intArray, doubleArray, string, stringArray}='"1arcsec"') - Cell size
   - **stokes** (string='I') - Stokes Planes to make (I only, for now)
   - **specmode** (string='mfs') - Spectral definition mode (mfs only, for now)
   - **weighting** (string='natural') - Weighting scheme (natural,uniform,briggs)

      .. raw:: html

         <details><summary><i> weighting = natural </i></summary>

      - **uvtaper** (stringArray=['']) - uv-taper on outer baselines in uv-plane

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> weighting = briggs </i></summary>

      - **robust** (double=0.5) - Robustness parameter
      - **npixels** (int=0) - Number of pixels to determine uv-cell size (0 : -/+ 3 pixels)
      - **uvtaper** (stringArray=['']) - uv-taper on outer baselines in uv-plane

      .. raw:: html

         </details>


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
         :name: title1

      The **apparentsens** task use the same data selection as the
      **tclean** task, as well as a subset of the image geometry and
      weighting parameters.  All operate in essentially the same way
      (with exceptions noted below), and the **tclean** documentation
      should be consulted for details on how to set them.

      .. rubric:: *specmode*
         :name: specmode

      For now, it is only meaningful to use specmode='mfs'.  Use of
      specmode='cube' will be supported in future (and a apparent
      sensitivity spectrum will be returned and reported).

      .. rubric:: *stokes*
         :name: stokes

      Currently, **apparentsens** will report the sensitivity for
      stokes='I' only.  Support for polarization-dependent sensitivity
      estimates will be added in future.

       

      .. rubric:: * *
         :name: section

      .. rubric:: * *
         :name: section-1

    """
    pass
