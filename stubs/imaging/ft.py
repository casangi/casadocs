#
# stub function definition file for docstring parsing
#

def ft(vis, field='', spw='', model='', nterms=1, reffreq='', complist='', incremental=False, usescratch=False):
    r"""
Insert a source model as a visibility set

Parameters
   - vis_ (string) - Name of input visibility file
   - field_ (string='') - Select field using field id(s) or field name(s)
   - spw_ (string='') - Select spectral window/channels
   - model_ (variant='') - Name of input model image(s)
   - nterms_ (int=1) - Number of terms used to model the sky frequency dependence
   - complist_ (string='') - Name of component list
   - incremental_ (bool=False) - Add to the existing model visibility?
   - usescratch_ (bool=False) - If True, predicted  visibility  is stored in MODEL_DATA column


Description
   .. rubric:: Summary
      

   **ft** converts a source model or a components list into model
   visibilities that is inserted into the MODEL_DATA column of the
   MS. Alternatively (*usescratch=False*) it can be stored in the
   header of the MS to be served on the fly when requested. The
   function of **ft** is needed to use more complicated sources, or
   to attach models to be subtracted later from the visibilities with
   **uvsub**.

   The source model should be in units of Jy/pixel, usually a
   \*.model image that **tclean**saves as a result of
   deconvolution.

   **ft** only uses a standard gridder (a prolate spheroidal) but
   supports multi-term images (see **tclean** help). Other gridders,
   like *mosaic* or *widefield*, are currently not supported. If you
   need one of the non-standard gridders, attach the model to the
   MSwith the task**tclean,** setting **** *savemodel=True,*
   and *gridder* to the requested algorithm.

   The default is to replace any current MODEL in the MS by the model
   specified in the *model*or *complist* parameters. The parameter
   *incremental=True* will addthe specified model to the
   currentMODEL in the MS. This can be useful, e.g., when new point
   sources are identified that need to be added to the model in the
   MS.

   When both, a *model* and a component list (in*complist)* are
   specified, **ft** will only use the model image in the *model*
   parameter.

   **ft** is strict in its frequency interpretation. Only frequencies
   that the model covers are inserted into the MS. If the model has a
   different frequency range, it needs to be modified to span the MS
   spws that are to be associated. Otherwise, the frequency ranges
   that are not covered by the model will be unaltered in the model
   column, or filled with zeros in the case that a MODEL_DATA column
   is added because none previously existed.

   In addition to **tclean**, another alternative to **ft** is
   **setjy**, which attaches a model and also scales the flux of the
   model to a flux value calculated from a standard or to a provided
   value.

   .. note:: **NOTE**: Model images for standard VLA calibrators 3C48,
      3C138, 3C147, and 3C286 for the VLA bands are provided with the
      release. The location inside the package is dependent on the
      operating system;**setjy** *(listmodels=True)* will show all
      available models.




Details
   Explanation of each parameter

.. _vis:

   .. rubric:: vis

   | Name of input visibility file
   |                      Default: none
   | 
   |                         Example: vis='ngc5921.ms'

.. _field:

   .. rubric:: field

   | Select field using field id(s) or field name(s)
   |                      Default: '' (all fields)
   |                      
   |                      BUT, only one source can be specified in a
   |                      multi-source vis.
   | 
   | 
   |                         Examples: 
   |                         field = '1328+307'  specifies source
   |                         '1328+307'
   |                         field = '4' specified field with index 4

.. _spw:

   .. rubric:: spw

   | Select spectral window/channels
   |                      Default: '' (all spectral windows and channels)

.. _model:

   .. rubric:: model

   | Name of input model image(s)
   |                      Default: '' (none)
   | 
   |                         Example:
   |                         model='/usr/lib/casapy/data/nrao/VLA/CalModels/3C286_X.im'
   | 
   |                      NOTE: The model visibilities are scaled from the
   |                      model frequency to the observed frequency of the
   |                      data.

.. _nterms:

   .. rubric:: nterms

   | Number of terms used to model the sky frequency
   | dependence
   |                      Default: 1 (one model image is required)
   | 
   |                         Example: nterms=3 - represents a 2nd order
   |                         Taylor-polynomial in frequency and should be
   |                         used in conjuction with coefficient model
   |                         images as
   |                         model=['xxx.model.tt0','xxx.model.tt1',
   |                         'xxx.model.tt2']

.. _reffreq:

   .. rubric:: reffreq

   | Reference-frequency about which this Taylor-expansion is
   | defined.
   |                      Default: '' (reads the reference frequency from
   |                      the model image)
   | 
   |                         Example: reffreq = '1.5GHz'

.. _complist:

   .. rubric:: complist

   | Name of component list
   |                      Default: none
   | 
   |                         Example: complist='test.cl'
   | 
   |                      WARNING: component lists are difficult to make

.. _incremental:

   .. rubric:: incremental

   | Add model visibility to the existing model visibilties
   | stored in the MS
   |                      Default: False
   |                      Options: False|True

.. _usescratch:

   .. rubric:: usescratch

   | Story visibilities in MODEL_DATA column?
   |                      Default: False
   |                      Options: False|True
   | 
   |                      If True, model visibilities will be stored in the
   |                      scratch column MODEL_DATA; if False, the model
   |                      visibilities will be generated  on the fly (this
   |                      mode may save some disk space equivalent to the
   |                      volume of the observed data).


    """
    pass
