Parameters
==========

.. container:: documentDescription description

   task applycal parameters

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               imagename : string

            Name of the input (CASA or FITS) image Default: none
            Example: imagename='ngc5921.im'

Example

imagename='ngc5921.im'

.. container:: param

   .. container:: parameters2

      mode : string = list

   Operating mode. Default: 'list' (retrieve history) Options:
   'list|append' ('append' to append a record to history)

Example

.. container:: param

   .. container:: parameters2

      verbose : bool = True

   Write history to logger if mode="list"? Subparameter of mode='list'
   Default: True Options: True|False

Example

.. container:: param

   .. container:: parameters2

      origin : string = imhistory

   Origin of appended message. Subparameter of mode='append' Default:
   'imhistory' The user can specify any string. This string will appear
   as a tag at the start of the appended line in the image history. Only
   used for mode="append".

Example

.. container:: param

   .. container:: parameters2

      message : string

   Message to append. Subparameter of mode='append' Default: none Only
   used of mode="append".

Example

.. container:: section
   :name: viewlet-below-content-body
