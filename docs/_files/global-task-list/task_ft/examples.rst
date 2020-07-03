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

      **Example 1: **

      Add a multi-term model (image.model from clean) to an MS
      ('myMS.ms'), spectral window 3, writing directly to the MODEL
      column:

      .. container:: casa-input-box

         ft(vis='myMS.ms', spw=3, nterms=2,
         model=['image.model.tt0','image.model.tt1'], usescratch=True) 

       

      **Example 2: **

      Create a component list with a point source at position J2000
      12h33m45.3s -23d01m11.2s with a spectral index of -0.8 and a flux
      of 13.4 Jy at a reference frequency of 1.25GHz; insert it into
      'myMS.ms' as a virtual model for field 3:

      .. container:: casa-input-box

         | #first create the component list
         | cl.addcomponent(shape='point', flux='13.4Jy', spectrum
           type='spectral index', index=-0.8, freq'1.25GHz', dir='J2000
           12h33m45.3s -23d01m11.2s')
         | # save the component list under the name 'mycomplist.cl'
         | cl.rename('mycomplist.cl')
         | cl.close()
         | #now insert the component list into myMS.ms as a virtual
           MODEL
         | ft(vis='myMS.ms', field='3', complist='mycomplist.cl',
           usescratch=True)

       

.. container:: section
   :name: viewlet-below-content-body
