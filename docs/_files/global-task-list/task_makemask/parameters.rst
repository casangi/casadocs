Parameters
==========

.. container:: documentDescription description

   task parameters

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               mode : string = list

            Mask method (list, copy,expand,delete,setdefaultmask)

Allowed Value(s)

list copy expand delete setdefaultmask

Example

.. container:: param

   .. container:: parameters2

      inpimage : string stringArray

   Name of input image.

Example

.. container:: param

   .. container:: parameters2

      inpmask : string stringArray

   mask(s) to be processed: image masks,T/F internal masks(Need to
   include parent image names),regions(for copy mode)

Example

.. container:: param

   .. container:: parameters2

      output : string

   Name of output mask (imagename or imagename:internal_maskname)

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   overwrite output if exists?

Example

.. container:: param

   .. container:: parameters2

      inpfreqs : string intArray

   List of chans/freqs (in inpmask) to read masks from

Example

.. container:: param

   .. container:: parameters2

      outfreqs : string intArray

   List of chans/freqs (in output) on which to expand the mask

Example

.. container:: section
   :name: viewlet-below-content-body
