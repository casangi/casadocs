ft -- Insert a source model  a visibility set: -- imaging, calibration task
=======================================

Description
---------------------------------------

       A source model (souce.model image) or components list is converted into 
       model visibilities that is inserted into the MODEL_DATA column or alternatively 
       is stored  in the header of the MS to be served on the fly when requested.  This is
       needed to use more complicated sources than setjy provides; e.g resolved source 
       or off centered sources in gaincal.  (Setjy will
       automatically make this ft step.)

       The sources currently available are 3C48, 3C138, 3C147, 3C286
       at 1.4, 5.0, 8.4, 15, 22, 43 GHz.  Their location is site
       dependent.  In Charlottesville and at the SOC, the models are
       in /usr/lib/casapy/data/nrao/VLA/CalModels.
	


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
     - 
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - model
     - :code:`''`
     - 
   * - nterms
     - :code:`int(1)`
     - 
   * - reffreq
     - :code:`''`
     - 
   * - complist
     - :code:`''`
     - 
   * - incremental
     - :code:`False`
     - 
   * - usescratch
     - :code:`False`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file (MS)


field
---------------------------------------

:code:`''`

Field selection


spw
---------------------------------------

:code:`''`

Spw selection


model
---------------------------------------

:code:`''`

Name of input model image(s)


nterms
---------------------------------------

:code:`int(1)`

Number of terms used to model the sky frequency dependence


reffreq
---------------------------------------

:code:`''`

Reference frequency (e.g. \'1.5e+9\' or \'1.5GHz\')


complist
---------------------------------------

:code:`''`

Name of component list


incremental
---------------------------------------

:code:`False`

Add to the existing model visibility?


usescratch
---------------------------------------

:code:`False`

If True predicted  visibility  is stored in MODEL_DATA column




