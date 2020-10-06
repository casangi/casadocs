

.. _Description:

Description
   

.. _Examples:

Examples
   task examples
   
   ::
   
      | # rebin the first two axes (normally the direction axes)
      | imrebin(imagename="my.im", outfile="rebinned.im",
        factor=[2,3])
      | # rebin the frequency axis, which is the fourth axis in this
        image
      | imrebin(imagename="my2.im", outfile="rebinned2.im",
        factor=[1,1,1,4])
   

.. _Development:

Development
   task developer
   
   --CASA Developer--
   
   