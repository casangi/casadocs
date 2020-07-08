.. container::
   :name: viewlet-above-content-title

Introduction
============

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Introduction to Synthesis Imaging: Measurement Equation, Iterative
   χ2\ :math:`\chi^2` minimization, Major and Minor cycles, Algorithm
   Options, etc.

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      This section describes the framework used by CASA for
      interferometric image reconstruction

      .. rubric:: Concept :
         :name: concept

      Image reconstruction in radio interferometry is the process of
      solving the linear system of equations
      →V=[A]→I\ :math:`\vec{V} = [A] \vec{I}`, where →V\ :math:`\vec{V}`
      represents visibilities calibrated for direction independent
      effects, →I\ :math:`\vec{I}` is a list of parameters that model
      the sky brightness distribution (for example, a image of pixels)
      and [A]\ :math:`[A]` is the measurement operator that encodes the
      process of how visibilities are generated when a telescope
      observes a sky brightness →I\ :math:`\vec{I}`.  [A]\ :math:`[A]`
      is generally given by [Sdd][F]\ :math:`[S_{dd}][F]` where
      [F]\ :math:`[F]` represents a 2D Fourier transform, and
      [Sdd]\ :math:`[S_{dd}]` represents a 2D spatial frequency sampling
      function that can include direction-dependent instrumental
      effects. For a practical interferometer with a finite number of
      array elements, [A]\ :math:`[A]` is non-invertible because of
      unsampled regions of the uv\ :math:`uv` plane. Therefore, this
      system of equations must be solved iteratively, applying
      constraints via various choices of image parameterizations and
      instrumental models.

       

      .. rubric:: Implementation ( major and minor cycles ):
         :name: implementation-major-and-minor-cycles

      Image reconstruction in CASA comprises an outer loop of *major
      cycles* and an inner loop of *minor cycles*. The major cycle
      implements transforms between the data and image spaces and the
      minor cycle operates purely in the image domain. Together, they
      implement an iterative weighted χ2\ :math:`\chi^2` minimization
      process that solves the measurement equation.

       

      |image1|

      ======= =======================================================
      Type    Figure
      ID      imagingoverview-fig-majorminorcycles
      Caption Iterative Image Reconstruction - Major and Minor Cycles
      ======= =======================================================

       

      The data to image transform is called the *imaging* step in which
      a pseudo inverse of [Sdd][F]\ :math:`[S_{dd}][F]` is computed and
      applied to the visibilities. Operationally, weighted visibilities
      are convolutionally resampled onto a grid of spatial-frequency
      cells, inverse Fourier transformed, and normalized. This step is
      equivalent to calculating the normal equations as part of a least
      squares solution. The image to data transform is called the
      *prediction* step and it evaluates the measurement equation to
      convert a model of the sky brightness into a list of model
      visibilities that are later subtracted from the data to form
      residual visibilities. For both transforms, direction dependent
      instrumental effects can be accounted for via carefully
      constructed convolution functions.

      Iterations begin with an initial guess for the image model.  Each
      major cycle consists of the prediction of model visibilities, the
      calculation of residual visibilities and the construction of a
      residual image. This residual image contains the effect of
      incomplete sampling of the spatial-frequency plane but is
      otherwise normalized to the correct sky flux units. In its
      simplest form, it can be written as a convolution of the true sky
      image with a point spread function. The job of the minor cycle is
      to iteratively build up a model of the true sky by separating it
      from the point spread function. This step is also called
      *deconvolution* and is equivalent to the process of solving the
      normal equations as part of a least squares solution. Different
      reconstruction algorithms can operate as minor cycle iterations,
      allowing for flexibility in (for example) how the sky brightness
      is parameterized. The imaging step can be approximate in that
      several direction dependent effects, especially baseline,
      frequency or time-dependent ones can sometimes  ignored, minor
      cycles can be approximate in that they use only PSF patches and do
      not try to be accurate over the entire image, but the prediction
      step of the major cycle must be as accurate as possible such that
      model components are converted to visibilities by including all
      possible instrumental effects.

      .. container:: info-box

         **Basic Sequence of Imaging Logic:**

         | Data : Calibrated visibilities, data weights, UV sampling
           function
         | Input : Algorithm and iteration controls (stopping threshold,
           loop gain,...)
         | Output : Model Image, Restored Image, Residual Image,...
         | Initialize the model image
         | Compute the point spread function
         | Compute the initial residual image
         | While ( not reached global stopping criterion )            
           /\* Major Cycle \*/
         | {
         |     While ( not reached minor-cycle stopping criterion )   
           /\* Minor Cycle \*/
         |     {
         |         Find the parameters of a new flux component
         |         Update the model and residual images
         |     }
         |     Use current model image to predict model visibilities
         |     Calculate residual visibilities (data - model)
         |     Compute a new residual image from residual visibilities
         | }
         | Convolve the final model image with the fitted beam and add
           to the residual image

      .. rubric::  
         :name: section

      .. rubric:: Algorithmic Options :
         :name: algorithmic-options

      Within the CASA implementation, numerous choices are provided to
      enable the user to fine-tune the details of their image
      reconstruction. Images can be constructed as spectral cubes with
      multiple frequency channels or single-plane wideband continuum
      images. One or more sub images may be defined to cover a wide
      field of view without incurring the computational expense of very
      large images. The iterative framework described above is based on
      the Cotton-Schwab Clean algorithm `[3] <#cit3>`__, but variants
      like Hogbom Clean `[1] <#cit1>`__ and Clark Clean `[2] <#cit2>`__
      are available as subsets of this framework. The major cycle allows
      controls over different data weighting schemes `[10] <#cit10>`__
      and convolution functions that account for wide-field
      direction-dependent effects during imaging and prediction
      [`[6] <#cit6>`__, `[7] <#cit7>`__ , `[8] <#cit8>`__].
      Deconvolution options include the use of point source vs
      multi-scale image models `[4] <#cit4>`__ , narrow-band or
      wide-band models `[5] <#cit5>`__, controls on iteration step size
      and stopping criteria, and external constraints such as
      interactive and non-interactive image masks. Mosaics may be made
      with data from multiple pointings, either with each pointing
      imaged and deconvolved separately before being combined in a final
      step, or via a joint imaging and deconvolution `[9] <#cit9>`__.
      Options to combine single dish and interferometer data during
      imaging also exist. More details about these algorithms can be
      obtained from [`[10] <#cit10>`__, `[11] <#cit11>`__,
      `[12] <#cit12>`__, `[13] <#cit13>`__] 

       

       

      .. rubric:: References :
         :name: references

      +-----------------+---------------------------------------------------+
      | Citation Number | 1                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | J. A. Hogbom 1974                                 |
      |                 | (`ADS <http://a                                   |
      |                 | dsabs.harvard.edu/full/1974A%26AS...15..417H>`__) |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 2                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | B. G. Clark 1980                                  |
      |                 | (`ADS <http://                                    |
      |                 | adsabs.harvard.edu/abs/1980A%26A....89..377C>`__) |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 3                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | F. R. Schwab, 1984                                |
      |                 | (`ADS <http:                                      |
      |                 | //adsabs.harvard.edu/abs/1984AJ.....89.1076S>`__) |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 4                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | T. J. Cornwell, 2008                              |
      |                 | (`IEEE <                                          |
      |                 | http://ieeexplore.ieee.org/document/4703304/>`__) |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 5                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | U.Rau, 2011 (`Astronomy and                       |
      |                 | Astrophysics) <https://www.aanda.org/artic        |
      |                 | les/aa/abs/2011/08/aa17104-11/aa17104-11.html>`__ |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 6                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | T. J. Cornwell, 2008                              |
      |                 | (`IEEE <                                          |
      |                 | http://ieeexplore.ieee.org/document/4703511/>`__) |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 7                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | S. Bhatnagar, 2008                                |
      |                 | (`ADS <http:                                      |
      |                 | //adsabs.harvard.edu/abs/2008A&A...487..419B>`__) |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 8                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | S.Bhatnagar, 2013                                 |
      |                 | (`ADS <http:                                      |
      |                 | //adsabs.harvard.edu/abs/2013ApJ...770...91B>`__) |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 9                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | T. J. Cornwell, 1988                              |
      |                 | (`ADS <http://                                    |
      |                 | adsabs.harvard.edu/abs/1988A%26A...202..316C>`__) |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 10                                                |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Briggs D.S. 1999 (`Astron. Soc. Pac. Conf.        |
      |                 | Ser. <http                                        |
      |                 | ://www.aspbooks.org/publications/180/127.pdf>`__) |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 11                                                |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Cornwell, T.J 1999 (`Astron. Soc. Pac. Conf.      |
      |                 | Ser. <http                                        |
      |                 | ://www.aspbooks.org/publications/180/151.pdf>`__) |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 12                                                |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Cornwell, T.J., "The Generic Interferometer: II   |
      |                 | Image Solvers'', Aips++ note 184. Aug 1995        |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 13                                                |
      +-----------------+---------------------------------------------------+
      | Citation Text   | U.Rau, 2009                                       |
      |                 | (`IEEE <                                          |
      |                 | http://ieeexplore.ieee.org/document/5109712/>`__) |
      +-----------------+---------------------------------------------------+

       

   .. container::
      :name: citation-container

      .. container::
         :name: citation-title

         Bibliography

      .. container::

         :sup:`1. J. A. Hogbom 1974
         (`\ `ADS <http://adsabs.harvard.edu/full/1974A%26AS...15..417H>`__\ :sup:`)`\ `↩ <#ref-cit1>`__

      .. container::

         :sup:`2. B. G. Clark 1980
         (`\ `ADS <http://adsabs.harvard.edu/abs/1980A%26A....89..377C>`__\ :sup:`)`\ `↩ <#ref-cit2>`__

      .. container::

         :sup:`3. F. R. Schwab, 1984
         (`\ `ADS <http://adsabs.harvard.edu/abs/1984AJ.....89.1076S>`__\ :sup:`)`\ `↩ <#ref-cit3>`__

      .. container::

         :sup:`4. T. J. Cornwell, 2008
         (`\ `IEEE <http://ieeexplore.ieee.org/document/4703304/>`__\ :sup:`)`\ `↩ <#ref-cit4>`__

      .. container::

         :sup:`5. U.Rau, 2011 (`\ `Astronomy and
         Astrophysics) <https://www.aanda.org/articles/aa/abs/2011/08/aa17104-11/aa17104-11.html>`__\ `↩ <#ref-cit5>`__

      .. container::

         :sup:`6. T. J. Cornwell, 2008
         (`\ `IEEE <http://ieeexplore.ieee.org/document/4703511/>`__\ :sup:`)`\ `↩ <#ref-cit6>`__

      .. container::

         :sup:`7. S. Bhatnagar, 2008
         (`\ `ADS <http://adsabs.harvard.edu/abs/2008A&A...487..419B>`__\ :sup:`)`\ `↩ <#ref-cit7>`__

      .. container::

         :sup:`8. S.Bhatnagar, 2013
         (`\ `ADS <http://adsabs.harvard.edu/abs/2013ApJ...770...91B>`__\ :sup:`)`\ `↩ <#ref-cit8>`__

      .. container::

         :sup:`9. T. J. Cornwell, 1988
         (`\ `ADS <http://adsabs.harvard.edu/abs/1988A%26A...202..316C>`__\ :sup:`)`\ `↩ <#ref-cit9>`__

      .. container::

         :sup:`10. Briggs D.S. 1999 (`\ `Astron. Soc. Pac. Conf.
         Ser. <http://www.aspbooks.org/publications/180/127.pdf>`__\ :sup:`)`\ `↩ <#ref-cit10>`__

      .. container::

         :sup:`11. Cornwell, T.J 1999 (`\ `Astron. Soc. Pac. Conf.
         Ser. <http://www.aspbooks.org/publications/180/151.pdf>`__\ :sup:`)`\ `↩ <#ref-cit11>`__

      .. container::

         :sup:`12. Cornwell, T.J., "The Generic Interferometer: II Image
         Solvers'', Aips++ note 184. Aug 1995`\ `↩ <#ref-cit12>`__

      .. container::

         :sup:`13. U.Rau, 2009
         (`\ `IEEE <http://ieeexplore.ieee.org/document/5109712/>`__\ :sup:`)`\ `↩ <#ref-cit13>`__

.. container:: section
   :name: viewlet-below-content-body

.. |image1| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/figmajorminor.png/@@images/31c10d18-b236-421e-aca7-9563437527d6.png
   :class: image-inline
   :width: 635px
   :height: 347px
