

.. _Description:

Description
   

.. _Examples:

Examples
   task examples
   
   To fit a maximum of 2 Gaussian singlets plus a second order
   polynomial function to a 1-dimensional spectral profile of an
   image, and return a dictionary of the fit:
   
   ::
   
      res = specfit(imagename="myspectrum.im", ngauss=2,
      box="3,3,4,5", poly=2, multifit=true, wantreturn=True)
   

.. _Development:

Development
   