.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Image Import/Export
===================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Im/Exporting FITS files and dumping the data into Python

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Image Import/Export to FITS
         :name: image-importexport-to-fits

      These tasks will allow you to write your CASA image to a FITS file
      that other packages can read, and to import existing FITS files
      into CASA as an image.

      .. rubric:: FITS Image Export (exportfits)
         :name: fits-image-export-exportfits

      To export your images to fits format use the **exportfits** task.
      The inputs are:

      .. container:: casa-input-box

         | #  exportfits :: Convert a CASA image to a FITS file
         | imagename    =         ''   #  Name of input CASA image
         | fitsimage    =         ''   #  Name of output image FITS file
         | velocity     =      False   #  Use velocity (rather than
           frequency) as spectral axis
         | optical      =      False   #  Use the optical (rather than
           radio) velocity convention
         | bitpix       =        -32   #  Bits per pixel
         | minpix       =          0   #  Minimum pixel value
         | maxpix       =          0   #  Maximum pixel value
         | overwrite    =      False   #  Overwrite pre-existing
           imagename
         | dropstokes   =      False   #  Drop the Stokes axis?
         | stokeslast   =       True   #  Put Stokes axis last in
           header?

      | The *dropstokes* or *stokeslast* parameter may be needed to make
        the FITS image compatible with an external application.
      | For example,

      .. container:: casa-input-box

           
         exportfits('ngc5921.demo.cleanimg.image','ngc5921.demo.cleanimg.image.fits')

      .. rubric:: 
         FITS Image Import (importfits)
         :name: fits-image-import-importfits

      You can also use the **importfits** task to import a FITS image
      into CASA image table format. Note, the CASA viewer can read fits
      images so you don’t need to do this if you just want to look at
      the image. The inputs for **importfits** are:

      .. container:: casa-input-box

         | #  importfits :: Convert an image FITS file into a CASA image
         | fitsimage           =         ''        #  Name of input
           image FITS file
         | imagename           =         ''        #  Name of output
           CASA image
         | whichrep            =          0        #  If fits image has
           multiple
         |                                         #   coordinate reps,
           choose one.
         | whichhdu            =          0        #  If its file
           contains
         |                                         #    multiple images,
           choose one.
         | zeroblanks          =       True        #  Set blanked pixels
           to zero (not NaN)
         | overwrite           =      False        #  Overwrite
           pre-existing imagename
         | defaultaxes         =      False        #  Add the default 4D
         |                                         #   coordinate axes
           where they are missing
         | defaultaxesvalues   =         []        #  List of values to
           assign to
         |                                         #   added degenerate
           axes when
         |                                         #   defaultaxes=True
           (ra,dec,freq,stokes)

      For example, we can read the above image back in

      .. container:: casa-input-box

         importfits('ngc5921.demo.cleanimg.image.fits','ngc5921.demo.cleanimage')

       

      .. rubric::  
         :name: section

      .. rubric:: Extracting data from an image (**imval**)
         :name: extracting-data-from-an-image-imval

      | 
      | The **imval** task will extract the values of the data and mask
        from a specified region of an image and place in the task return
        value as a Python dictionary. The inputs are:

      .. container:: casa-input-box

         | #  imval :: Get the data value(s) and/or mask value in an
           image.
         | imagename  =      ''   #  Name of the input image
         | region     =      ''   #  Image Region.  Use viewer
         | box        =      ''   #  Select one or more box regions
         | chans      =      ''   #  Select the channel(spectral) range
         | stokes     =      ''   #  Stokes params to image
           (I,IV,IQU,IQUV)

      | Area selection using `box <#region-selection--box->`__ and
        `region <#regions--region->`__ is detailed above. By default,
        *box=' '* will extract the image information at the reference
        pixel on the direction axes. `Plane
        selection <#plane-selection--chans--stokes->`__ is controlled by
        *chans* and *stokes*. By default, *chans=' '* and *stokes=' '*
        will extract the image information in all channels and Stokes
        planes.
      | For instance,

      .. container:: casa-input-box

         xval = imval('myimage', box='144,144', stokes='I' )

      will extract the Stokes I value or spectrum at pixel 144,144,
      while

      .. container:: casa-input-box

         xval = imval('myimage', box='134,134.154,154', stokes='I' )

      will extract a 21 by 21 pixel region. Extractions are returned in
      NumPy arrays in the return value dictionary, plus some extra
      elements describing the axes and selection:

      .. container:: casa-output-box

         | 
         | CASA <2>: xval = imval('ngc5921.demo.moments.integrated')
         | CASA <3>: xval
         |   Out[3]:
         | {'axes': [[0, 'Right Ascension'],
         |           [1, 'Declination'],
         |           [3, 'Frequency'],
         |           [2, 'Stokes']],
         |  'blc': [128, 128, 0, 0],
         |  'data': array([ 0.89667124]),
         |  'mask': array([ True], dtype=bool),
         |  'trc': [128, 128, 0, 0],
         |  'unit': 'Jy/beam.km/s'}

      extracts the reference pixel value in this 1-plane image. Note
      that the '*data'* and '*mask'* elements are NumPy arrays, not
      Python lists. To extract a spectrum from a cube:

      .. container:: casa-output-box

         | 
         | CASA <8>: xval =
           imval('ngc5921.demo.clean.image',box='125,125')
         | CASA <9>: xval
         |   Out[9]:
         | {'axes': [[0, 'Right Ascension'],
         |           [1, 'Declination'],
         |           [3, 'Frequency'],
         |           [2, 'Stokes']],
         |  'blc': [125, 125, 0, 0],
         |  'data': array([  8.45717848e-04,   1.93370355e-03,  
           1.53750915e-03,
         |          2.88399984e-03,   2.38683447e-03,   2.89159478e-04,
         |          3.16268904e-03,   9.93389636e-03,   1.88773088e-02,
         |          3.01138610e-02,   3.14478502e-02,   4.03211266e-02,
         |          3.82498614e-02,   3.06552909e-02,   2.80734301e-02,
         |          1.72479432e-02,   1.20884273e-02,   6.13593217e-03,
         |          9.04005766e-03,   1.71429547e-03,   5.22095338e-03,
         |          2.49114982e-03,   5.30831399e-04,   4.80734324e-03,
         |          1.19265869e-05,   1.29435991e-03,   3.75700940e-04,
         |          2.34788167e-03,   2.72604497e-03,   1.78467855e-03,
         |          9.74952069e-04,   2.24676146e-03,   1.82263291e-04,
         |          1.98463408e-06,   2.02975096e-03,   9.65532148e-04,
         |          1.68218743e-03,   2.92119570e-03,   1.29359076e-03,
         |         -5.11484570e-04,   1.54162932e-03,   4.68662125e-04,
         |         -8.50282842e-04,  -7.91683051e-05,   2.95954203e-04,
         |         -1.30133145e-03]),
         |  'mask': array([ True,  True,  True,  True,  True,  True, 
           True,  True,  True,
         |         True,  True,  True,  True,  True,  True,  True, 
           True,  True,
         |         True,  True,  True,  True,  True,  True,  True, 
           True,  True,
         |         True,  True,  True,  True,  True,  True,  True, 
           True,  True,
         |         True,  True,  True,  True,  True,  True,  True, 
           True,  True,  True], dtype=bool),
         |  'trc': [125, 125, 0, 45],
         |  'unit': 'Jy/beam'}

      To extract a region from the plane of a cube:

      .. container:: casa-output-box

         | CASA <13>: xval =
           imval('ngc5921.demo.clean.image',box='126,128,130,129',chans='23')
         | CASA <14>: xval
         |   Out[14]:
         | {'axes': [[0, 'Right Ascension'],
         |           [1, 'Declination'],
         |           [3, 'Frequency'],
         |           [2, 'Stokes']],
         |  'blc': [126, 128, 0, 23],
         |  'data': array([[ 0.00938627,  0.01487772],
         |        [ 0.00955847,  0.01688832],
         |        [ 0.00696965,  0.01501907],
         |        [ 0.00460964,  0.01220793],
         |        [ 0.00358087,  0.00990202]]),
         |  'mask': array([[ True,  True],
         |        [ True,  True],
         |        [ True,  True],
         |        [ True,  True],
         |        [ True,  True]], dtype=bool),
         |  'trc': [130, 129, 0, 23],
         |  'unit': 'Jy/beam'}
         | CASA <15>: print xval['data'][0][1]
         | 0.0148777160794

      In this example, a rectangular box was extracted, and you can see
      the order in the array and how to address specific elements.

        

.. container:: section
   :name: viewlet-below-content-body
