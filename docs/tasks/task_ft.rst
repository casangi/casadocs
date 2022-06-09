

.. _Description:

Description
   **ft** converts a source model or a components list into model
   visibilities that is inserted into the MODEL_DATA column of the
   MS. Alternatively (*usescratch=False*) it can be stored in the
   header of the MS to be served on the fly when requested. The
   function of **ft** is needed to use more complicated sources, or
   to attach models to be subtracted later from the visibilities with
   **uvsub**. 
   
   The source model should be in units of Jy/pixel, usually a
   \*.model image that **tclean** saves as a result of
   deconvolution. 
   
   **ft** only uses a standard gridder (a prolate spheroidal) but
   supports multi-term images (see **tclean** help). Other gridders,
   like *mosaic* or *widefield*, are currently not supported. If you
   need one of the non-standard gridders, attach the model to the
   MS with the task **tclean**, setting *savemodel=True*,
   and *gridder* to the requested algorithm. 
   
   The default is to replace any current MODEL in the MS by the model
   specified in the *model* or *complist* parameters. The parameter
   *incremental=True* will add the specified model to the
   current MODEL in the MS. This can be useful, e.g., when new point
   sources are identified that need to be added to the model in the
   MS. 
   
   When both, a *model* and a component list (in *complist*) are
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
      operating system; **setjy** *(listmodels=True)* will show all
      available models.
   

.. _Examples:

Examples
   **Example 1:**
   
   Add a multi-term model (image.model from clean) to an MS
   ('myMS.ms'), spectral window 3, writing directly to the MODEL
   column:
   
   ::
   
      ft(vis='myMS.ms', spw=3, nterms=2,
         model=['image.model.tt0','image.model.tt1'], usescratch=True)

   
   **Example 2:**
   
   Create a component list with a point source at position J2000
   12h33m45.3s -23d01m11.2s with a spectral index of -0.8 and a flux
   of 13.4 Jy at a reference frequency of 1.25GHz; insert it into
   'myMS.ms' as a virtual model for field 3:
   
   ::
   
      # first create the component list
      cl.addcomponent(shape='point', flux='13.4Jy', spectrum type='spectral index',
                      index=-0.8, freq'1.25GHz', dir='J2000 12h33m45.3s -23d01m11.2s')

      # save the component list under the name 'mycomplist.cl'
      cl.rename('mycomplist.cl')
      cl.close()

      # now insert the component list into myMS.ms as a virtual MODEL
      ft(vis='myMS.ms', field='3', complist='mycomplist.cl', usescratch=True)


.. _Development:

Development
   No additional development details

