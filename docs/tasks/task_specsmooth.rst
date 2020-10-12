

.. _Description:

Description
   

.. _Examples:

Examples
   task examples
   
   ::
   
      | # boxcar smooth the spectral axis by 3 pixels,
      | # say it's axis 2 and only write every other pixel
      | specsmooth(imagename="mynonsmoothed.im",
        outfile="myboxcarsmoothed.im",
      | axis=2, function="boxcar", dmethod="copy", width=3,
        overwrite=True)
   
   ::
   
      | # hanning smooth the spectral axis,
      | # say it's axis 2 and do not perform decimation of image
        planes
      | specsmooth(imagename="mynonsmoothed.im",
        outfile="myhanningsmoothed.im",
      | axis=2, dmethod=""," overwrite=True)
   

.. _Development:

Development
   task developer
   
   --CASA Developer--
   
   