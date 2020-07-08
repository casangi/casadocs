.. container::
   :name: viewlet-above-content-title

Parameters
==========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task parameters

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               vis : string

            Name of input visibility file Default: none Example:
            vis='ngc5921.ms'

Example

.. container:: param

   .. container:: parameters2

      field : string

   Select field using field id(s) or field name(s) Default: '' (all
   fields) BUT, only one source can be specified in a multi-source vis.
   Examples: field = '1328+307' specifies source '1328+307' field = '4'
   specified field with index 4

Example

.. container:: param

   .. container:: parameters2

      spw : string

   Select spectral window/channels Default: '' (all spectral windows and
   channels)

Example

.. container:: param

   .. container:: parameters2

      model : undefined

   Name of input model image(s) Default: '' (none) Example:
   model='/usr/lib/casapy/data/nrao/VLA/CalModels/3C286_X.im' NOTE: The
   model visibilities are scaled from the model frequency to the
   observed frequency of the data.

Example

.. container:: param

   .. container:: parameters2

      nterms : int = 1

   Number of terms used to model the sky frequency dependence Default: 1
   (one model image is required) Example: nterms=3 - represents a 2nd
   order Taylor-polynomial in frequency and should be used in conjuction
   with coefficient model images as
   model=['xxx.model.tt0','xxx.model.tt1', 'xxx.model.tt2']

Example

.. container:: param

   .. container:: parameters2

      reffreq : string

   Reference-frequency about which this Taylor-expansion is defined.
   Default: '' (reads the reference frequency from the model image)
   Example: reffreq = '1.5GHz'

Example

.. container:: param

   .. container:: parameters2

      complist : string

   Name of component list Default: none Example: complist='test.cl'
   WARNING: component lists are difficult to make

Example

.. container:: param

   .. container:: parameters2

      incremental : bool = False

   Add model visibility to the existing model visibilties stored in the
   MS Default: False Options: False|True

Example

.. container:: param

   .. container:: parameters2

      usescratch : bool = False

   Story visibilities in MODEL_DATA column? Default: False Options:
   False|True If True, model visibilities will be stored in the scratch
   column MODEL_DATA; if False, the model visibilities will be generated
   on the fly (this mode may save some disk space equivalent to the
   volume of the observed data).

Example

.. container:: section
   :name: viewlet-below-content-body
