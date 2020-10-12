

.. _Description:

Description
   

.. _Examples:

Examples
   To correct an image for the primary beam response out to a radius
   where the sensitivity drops to 10% of the maximum value in the
   pointing center:
   
   ::
   
      impbcor(imagename="attenuated.im", pbimage="mypb.im",
      outfile="pbcorred.im", mode="divide", cutoff=0.1)
   

.. _Development:

Development
   --CASA Developer--
   
   