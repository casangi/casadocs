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

               imagename : string

            Name of the input image

Example

imagename='ngc5921_task.image'

.. container:: param

   .. container:: parameters2

      output : string

   Name of the output image

Example

output='newframed.image'; output='' will modify input image

.. container:: param

   .. container:: parameters2

      outframe : string = lsrk

   Spectral frame in which the frequency or velocity values will be
   reported by default

Allowed Value(s)

lsrk lsrd bary geo topo galacto lgroup cmb

Example

.. container:: param

   .. container:: parameters2

      epoch : string

   Epoch to be associated with this image

Example

For example: '2000/12/25/18:30:00.10'

.. container:: param

   .. container:: parameters2

      restfreq : string

   restfrequency to use for velocity values (e.g "1.420GHz" for the HI
   line)

Example

.. container:: section
   :name: viewlet-below-content-body
