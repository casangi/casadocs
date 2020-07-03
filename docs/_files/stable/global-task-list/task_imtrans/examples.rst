.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Examples
========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task examples

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. container:: casa-input-box

         .. container::

            # Swap the stokes and spectral axes in an
            RA-Dec-Stokes-Frequency image
            imagename = "myim.im"
            outfile = "outim.im"
            order = "0132"
            imtrans()
            # or
            outfile = "myim_2.im"
            order = 132
            imtrans()
            # or
            outfile = "myim_3.im"
            order = ["r", "d", "f", "s"]
            imtrans()
            # or
            outfile = "myim_4.im"
            order = ["rig", "declin", "frequ", "stok"]
            imtrans()

.. container:: section
   :name: viewlet-below-content-body
