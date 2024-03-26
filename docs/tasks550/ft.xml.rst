ft -- Insert a source model as a visibility set -- imaging, calibration task
=======================================

Description
---------------------------------------

A source model (souce.model image) or components list is converted
into model visibilities that is inserted into the MODEL_DATA column or
alternatively is stored  in the header of the MS to be served on the
fly when requested. 

Setjy will automatically make this ft step on the sources currently
available, which are 3C48, 3C138, 3C147, 3C286 at 1.4, 5.0, 8.4, 15,
22, 43 GHz.  Their location is site dependent.  In Charlottesville and
Socorro, the models are in
/usr/lib(lib64)/casapy/data/nrao/VLA/CalModels.



Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - vis
     - :code:`''`
     - Name of input visibility file
   * - field
     - :code:`''`
     - Select field using field id(s) or field name(s)
   * - spw
     - :code:`''`
     - Select spectral window/channels
   * - model
     - :code:`''`
     - Name of input model image(s)
   * - nterms
     - :code:`int(1)`
     - Number of terms used to model the sky frequency dependence
   * - reffreq
     - :code:`''`
     - Reference frequency (e.g. \'1.5e+9\' or \'1.5GHz\')
   * - complist
     - :code:`''`
     - Name of component list
   * - incremental
     - :code:`False`
     - Add to the existing model visibility?
   * - usescratch
     - :code:`False`
     - If True, predicted  visibility  is stored in MODEL_DATA column


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file
                     Default: none

                        Example: vis='ngc5921.ms'



field
---------------------------------------

:code:`''`

Select field using field id(s) or field name(s)
                     Default: '' (all fields)
                     
                     BUT, only one source can be specified in a
		     multi-source vis.


                        Examples: 
                        field = '1328+307'  specifies source
			'1328+307'
                        field = '4' specified field with index 4



spw
---------------------------------------

:code:`''`

Select spectral window/channels
                     Default: '' (all spectral windows and channels)
      


model
---------------------------------------

:code:`''`

Name of input model image(s)
                     Default: '' (none)

                        Example:
			model='/usr/lib/casapy/data/nrao/VLA/CalModels/3C286_X.im'

                     NOTE: The model visibilities are scaled from the
		     model frequency to the observed frequency of the
		     data.



nterms
---------------------------------------

:code:`int(1)`

Number of terms used to model the sky frequency
dependence
                     Default: 1 (one model image is required)

                        Example: nterms=3 - represents a 2nd order
			Taylor-polynomial in frequency and should be
			used in conjuction with coefficient model
			images as
			model=['xxx.model.tt0','xxx.model.tt1',
			'xxx.model.tt2']



reffreq
---------------------------------------

:code:`''`

Reference-frequency about which this Taylor-expansion is
defined.
                     Default: '' (reads the reference frequency from
		     the model image)

                        Example: reffreq = '1.5GHz'



complist
---------------------------------------

:code:`''`

Name of component list
                     Default: none

                        Example: complist='test.cl'

                     WARNING: component lists are difficult to make



incremental
---------------------------------------

:code:`False`

Add model visibility to the existing model visibilties
stored in the MS
                     Default: False
                     Options: False|True



usescratch
---------------------------------------

:code:`False`

Story visibilities in MODEL_DATA column?
                     Default: False
                     Options: False|True

                     If True, model visibilities will be stored in the
		     scratch column MODEL_DATA; if False, the model
		     visibilities will be generated  on the fly (this
		     mode may save some disk space equivalent to the
		     volume of the observed data).





