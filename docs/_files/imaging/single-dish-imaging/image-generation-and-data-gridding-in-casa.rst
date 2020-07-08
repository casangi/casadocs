.. container::
   :name: viewlet-above-content-title

Theoretical Description
=======================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   A theoretical description of single-dish image generation and data
   gridding

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      For single-dish observations, ALMA uses on-the-fly mapping.  The
      technique is described in Mangum et al. (2007) `[1] <#cit1>`__.

      Converting single-dish observations into an image or cube is done
      almost entirely in the image domain. After taking and calibrating
      the data, the process follows three steps:

      #. Forming the image grid
      #. Populating the image grid
      #. Smoothing the image data

      The fundamental parameter relevant to image quality is the
      sampling interval. There are a number of sampling functions that
      need to be considered: the sky sampling function, the image grid
      sampling function, and the response function of the single-dish
      beam. These functions all convolve against each other to yield an
      effective image resolution somewhat poorer than the actual
      theoretical FWHM of the telescope primary beam.

      The dimensions and extent of the image grid are determined by the
      mapped area on the sky. The gridding pixel size must be at least
      one half the size of the theoretical beam when convolved with the
      sky-sampling function. Since the sky sampling function is
      typically 1/3 to 1/5 of the primary beam, and the effective FWHM
      of the telescope and sky sampling function is close to that of the
      telescope anyway, it's safe to use a pixel dimension that is 1/3th
      the width of the primary beam.

      For example, a 30" telescope beam with a 6" sky sampling function
      has an effective FWHM of
      ∼√(302+62)≃\ :math:`\sim \sqrt{(30^2+6^2)}\simeq` 30.6".
      Therefore, computing an image pixel size that is 30"/3 = 10", is
      appropriately oversampling the effective beam FWHM and sampling
      interval.

      After the coordinates of the data are transformed into sky
      coordinates, the image grid is formed with dimensions either
      consistent with the user specifications, or so that the image
      fully encompasses the observed sky positions.  

      For each pixel in the grid (e.g. in RA-Dec space), the gridding
      process searches through the data for measurements taken within
      some cutoff radius (specified by *convsupport*). Depending on
      their distance from the grid coordinate, the observation is
      weighted according to the *kernel* type and added together in the
      spatial domain (i.e. entire spectra are added together). If
      the *clipminmax* function is invoked, the maximum AND minimium
      data in the ensemble (prior to weighting) are rejected before
      summing. This process is repeated iteratively for each element in
      the grid.

       

      +-----------------+---------------------------------------------------+
      | Citation Number | 1                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Mangum, et al. 2007, A&A, 474, 679-687            |
      |                 | (`ADS <http://www.aan                             |
      |                 | da.org/articles/aa/pdf/2007/41/aa7811-07.pdf>`__) |
      +-----------------+---------------------------------------------------+

   .. container::
      :name: citation-container

      .. container::
         :name: citation-title

         Bibliography

      .. container::

         :sup:`1. Mangum, et al. 2007, A&A, 474, 679-687
         (`\ `ADS <http://www.aanda.org/articles/aa/pdf/2007/41/aa7811-07.pdf>`__\ :sup:`)`\ `↩ <#ref-cit1>`__

.. container:: section
   :name: viewlet-below-content-body
