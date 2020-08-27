#
# stub function definition file for docstring parsing
#

def importfits(fitsimage, imagename='', whichrep=0, whichhdu=-1, zeroblanks=True, overwrite=False, defaultaxes=False, defaultaxesvalues='[]', beam='[]'):
    """
Convert an image FITS file into a CASA image

| Convert an image FITS file into a CASA image

Parameters
----------
fitsimage : string
   Name of input image FITS file
imagename : string
   Name of output CASA image
whichrep : int
   If fits image has multiple coordinate reps, choose one.
whichhdu : int
   If fits file contains multiple images, choose one (0 = first HDU, -1 = first valid image).
zeroblanks : bool
   Set blanked pixels to zero (not NaN)
overwrite : bool
   Overwrite output file if it exists?
defaultaxes : bool
   Add the default 4D coordinate axes where they are missing; value True requires setting defaultaxesvalues
defaultaxesvalues : variant
   List of values to assign to added degenerate axes when defaultaxes==True (ra,dec,freq,stokes)
beam : variant
   List of values to be used to define the synthesized beam [BMAJ,BMIN,BPA] (as in the FITS keywords)

Other Parameters
----------

Notes
-----





   importfits task: Convert an image FITS file into a CASA image



      You can use the **importfits** task to import a FITS image into
      CASA image format. Note, the CASA viewer can read FITS images so
      you don’t need to do this if you just want to look at the image.

      The CASA FITS reader uses wcslib by Mark Calabretta and thus
      implements the latest FITS standard (3.0). The intention of both
      wcslib and the added CASA code is to accommodate certain common
      deviations from the standard and be forgiving rather than
      pedantic. In some cases, however, images deviating too far from
      the standard will not be readable and you might see error
      messages. Read these carefully and try to consult the FITS
      documentation
      ( https://fits.gsfc.nasa.gov/standard30/fits_standard30aa.pdf ) to
      see how you have to change the header of your FITS image to make
      it sufficiently compliant with the standard.

      The inputs for **importfits** are:

      .. note:: | # importfits :: Convert an image FITS file into a CASA image
         | fitsimage         = ''    # Name of input image FITS file
         | imagename         = ''    # Name of output CASA image
         | whichrep          = 0     # If fits image has multiple
           coordinate reps, choose one.
         | whichhdu          = -1    # If its file contains multiple
           images, choose one (0 = first HDU, -1 = first valid image).
         | zeroblanks        = True  # Set blanked pixels to zero (not
           NaN)
         | overwrite         = False # Overwrite pre-existing imagename
         | defaultaxes       = False # Add the default 4D coordinate
           axes where they are missing; value True requires setting
           defaultaxesvalues
         | defaultaxesvalues = []    # List of values to assign to added
           degenerate axes when defaultaxes==True (ra,dec,freq,stokes)
         | beam              = []    # List of values to be used to
           define the synthesized beam [BMAJ,BMIN,BPA] (as in the FITS
           keywords)

      Here a description of the non-self-explanatory parameters:

      | 
      | *whichrep* -- If the FITS image has multiple coordinate
        representations, this parameter lets you choose which one to use
        (numbering starts at 0). Example: whichrep=1 .

      | *whichhdu* -- If the fits file contains multiple images, you can
        choose the header data unit by number. The value "-1" (default)
        chooses the first valid one.
      | CASA images by default have a 4D coordinate system (ra, dec,
        stokes, freq). Your input image may not have that. Setting the
        parameter *defaultaxes* to True, will make **importfits** add
        the missing axes as degenerate (one-pixel) axes and will take
        the coordinate values for these axes from the list in the
        parameter *defaultaxesvalues* (ra,dec,stokes, freq). For
        existing axes, empty strings can be given as values. For the
        directions and spectral values, any valid angle/frequency
        expressions can be given. Example:
        defaultaxesvalues=['19h30m00', '-02d30m00', '88.5GHz', 'Q']. If
        the order of the fits files ins not ra, dec, stokes, freq,
        **imtrans** can be used to change the order. 

      If your input image does not provide a beam or you want to
      override it, you can provde a list of values to be used to define
      the synthesized beam [BMAJ,BMIN,BPA] (as in the FITS keywords) in
      the parameter *beam*. Note that the FITS keywords typically list
      the BMAJ, BMIN and BPA in degrees, but they can be specified with
      other units in importfits. Example: beam=['0.35arcsec',
      '0.24arcsec', '25deg']

    """
    pass
