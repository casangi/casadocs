

.. _Description:

Description
   

.. _Examples:

Examples
   .. rubric:: Example: Collapse a Subimage Along the Spectral Axis
      
   
   For this example, myimage.im is a 512x512x128x4
   (ra,dec,freq,stokes) image.
   
   ::
   
      imagename = "myimage.im"
   
   We want to only collapse the central 256x256 pixel region, so we
   define a box for the subregion.  Similarly, we avoid the 8 edge
   channels at each end of the band. These are often noisy from the
   imaging process.
   
   ::
   
      | box="127,127,383,383"
      | chans="8~119"
   
   We specify to collapse along the spectral axis (zero based
   index),  and to use the "mean" algorithm.
   
   ::
   
      | function="mean"
      | axis=2
   
   And finally we specify the output image name and call the
   **imcollapse** function.
   
   ::
   
      | outfile="collapse_spec_mean.im"
      | imcollapse(imagename=imagename, outfile=outfile,
        function=function, axes=axis, box=box, chans=chans)
   
   The resulting image (collapse_spec_mean.im) is 256x256x1x4 in
   size.
   

.. _Development:

Development
   