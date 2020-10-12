

.. _Description:

Description
   

.. _Examples:

Examples
   Fit a second order polynomial (fitorder=2) to channels 3-8 and
   54-60 to an RA x Dec x Frequency x Stokes cube, selecting the
   Stokes I plane
   
   ::
   
      | ch = '3~8, 54~60'
      | imcontsub(imagename="myimage.im", linefile="mycontsub.im",
        fitorder=2, chans=ch, fitorder=2, stokes="I")
   

.. _Development:

Development
   --CASA Developer--
   
   Here would be a discussion of how applycal is implemented.  This
   is intended for the other members of the development team so is a
   technical discussion.  We will work on building these up over
   time.
   