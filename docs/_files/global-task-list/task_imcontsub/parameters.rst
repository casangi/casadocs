Parameters
==========

.. container:: documentDescription description

   task imcontsub parameters

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               imagename : string

            Input image cube. Default: none Example:
            imagename='ngc5921_task.im'

Example

inputfile=ngc5921_task.image

.. container:: param

   .. container:: parameters2

      linefile : string

   Name of continuum-subtracted output spectral line cube Default: none
   Example: outline='ngc5921_line.im'

Example

outline=ngc5921_line.image

.. container:: param

   .. container:: parameters2

      contfile : string

   Name of output continuum cube Default: none Example:
   contfile='ngc5921_cont.im'

Example

outcont=ngc5921_cont.image

.. container:: param

   .. container:: parameters2

      fitorder : int = 0

   Polynomial order for the continuum estimation Default: 0 Example:
   fitorder=2

Allowed Value(s)

0

Example

fitorder=2

.. container:: param

   .. container:: parameters2

      region : string

   Region selection. Default: '' (use the full image)

Example

.. container:: param

   .. container:: parameters2

      box : string intArray stringArray

   Rectangular region to select in direction plane. Default: '' (use the
   entire direction plane)

Example

.. container:: param

   .. container:: parameters2

      chans : string

   Channels to use. Default: '' (use all channels)

Example

.. container:: param

   .. container:: parameters2

      stokes : string

   Stokes planes to use. Default: '' (use all Stokes planes)

Example

.. container:: section
   :name: viewlet-below-content-body
