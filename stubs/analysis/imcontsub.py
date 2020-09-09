#
# stub function definition file for docstring parsing
#

def imcontsub(imagename, linefile='', contfile='', fitorder=0, region='', box='', chans='', stokes=''):
    r"""
Estimates and subtracts continuum emission from an image cube

Parameters
   - imagename_ (string) - Name of the input spectral line image
   - linefile_ (string='') - Output continuum-subtracted image file name
   - contfile_ (string='') - Output continuum image file name
   - fitorder_ (int=0) - Polynomial order for the continuum estimation
   - region_ (string='') - Region selection.
   - box_ ({string, intArray, stringArray}='') - Rectangular region to select in direction plane. Default is to use the entire direction plane.
   - chans_ (string='') - Channels to use.
   - stokes_ (string='') - Stokes planes to use.


Description
   For each direction pixel in an image (or a subset selected by
   *region* and/or *box*), this task estimates the continuum by
   fitting a polynomial to one or more subsets of the channels. In
   most cases, the user should choose the subset(s) of channels to be
   free of spectral lines. The continuum estimate is saved in
   *contfile*and subtracted from the image (or its subset) to make a
   spectral line estimate, which is saved in *linefile*.

   While imcontsub offersusers theoption to save the continuum
   estimate as a (multi-channel) dataset, the optimal way to create a
   continuum image is by using the multi-frequency synthesis (MFS)
   option in **tclean**.

   Note that fitting the continuum and subtracting it from a spectral
   line data set can also be done in the *(u,v)*-domain using the
   task **uvcontsub**.

   

   .. rubric:: Task-specific Parameter Descriptions
      

   .. rubric:: *linefile*
      

   Name of image to which to save the result of subtracting the
   computed continuum from the input image.

   .. rubric:: *contfile*
      

   The computed continuum image.

   .. rubric:: *fitorder*
      

   Order of polynomial to fit to the specified spectral channels to
   determine the continuum.

   .. rubric:: *chans*
      

   Spectral channels to use for fitting a polynomial to determine
   continuum.


.. _imagename:

imagename (string)
   | Input image cube.
   |                      Default: none
   | 
   |                         Example: imagename='ngc5921_task.im'

.. _linefile:

linefile (string='')
   | Name of continuum-subtracted output spectral line cube
   |                      Default: none
   | 
   |                         Example: outline='ngc5921_line.im'

.. _contfile:

contfile (string='')
   | Name of output continuum cube
   |                      Default: none
   | 
   |                         Example: contfile='ngc5921_cont.im'

.. _fitorder:

fitorder (int=0)
   | Polynomial order for the continuum estimation
   |                      Default: 0
   | 
   |                         Example: fitorder=2

.. _region:

region (string='')
   | Region selection. 
   |                      Default: '' (use the full image)

.. _box:

box ({string, intArray, stringArray}='')
   | Rectangular region to select in direction plane.
   |                      Default: '' (use the entire direction plane)

.. _chans:

chans (string='')
   | Channels to use. 
   |                      Default: '' (use all channels)

.. _stokes:

stokes (string='')
   | Stokes planes to use.
   |                      Default: '' (use all Stokes planes)


    """
    pass
