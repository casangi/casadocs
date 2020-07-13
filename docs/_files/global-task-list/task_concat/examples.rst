Examples
========

.. container:: documentDescription description

   task concat examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Concatenate 'ngc5921.ms' into 'src2.ms' (the original src2.ms is
      lost):

      .. container:: casa-input-box

         concat(vis=['src2.ms','ngc5921.ms'], concatvis='src2.ms')

      Concatenate 'ngc5921.ms' and 'src2.ms' into a file named 'out.ms'
      (the original 'ngc5921.ms' and 'src2.ms' are untouched):

      .. container:: casa-input-box

         concat(vis=['src2.ms','ngc5921.ms'], concatvis='out.ms')

      Like the previous example but using a direction tolerance
      increased to 0.5 arcsec. Fields whose directions differ by less
      than this limit are merged into one field with the name and
      direction from the chronologically first input MS:

      .. container:: casa-input-box

         concat(vis=['src2.ms','ngc5921.ms'], concatvis='out.ms',
         dirtol='0.5arcsec')

      Concatenate many MSs:

      .. container:: casa-input-box

         | concat(vis=['v1.ms','v2.ms'], concatvis = 'vall.ms') #then
         | concat(vis=['v3.ms','v4.ms'], concatvis = 'vall.ms')

      vall.ms will contain v1.ms+v2.ms+v3.ms+v4.ms .

      .. container:: info-box

         **NOTE**: Run flagmanager to save flags in the *concatvis.*

.. container:: section
   :name: viewlet-below-content-body
