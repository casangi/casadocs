Description
   The exportfits task exports CASA-produced images as FITS files for
   transporting to other software packages or publication.

   With the default settings, this task will produce FITS image files
   with 4 dimensions: RA, Dec, radio frequency, and polarization
   (Stokes parameters). Several options influence the shape of the
   output data array. Setting dropstokes=True will cause the
   polarization axis to be omitted. Setting velocity=True will cause
   the spectral axis to have units of velocity rather than
   frequency. Setting stokeslast=False will interchange the order of
   the polarization and spectral axes (i.e, polarization will be the
   third dimension, and frequency the fourth). Finally, setting
   dropdeg=True will cause any "degenerate" axes, those with length
   1, to be omitted. For example a total-intensity continuum image
   would result in a 2-dimensional output array (RA, Dec only) when
   using this option.

   The bitpix parameter specifies the number of bits used to
   represent a data value in the FITS image array. The allowed values
   for bitpix are 16 or -32 meaning the data values are represented
   as 16-bit twos-complement binary integer or IEEE single precision
   floating point, respectively. We recommend using the default value
   -32 in most cases. Using 16 bits results in smaller FITS files, at
   the expense of dynamic range in the image. It may also be
   necessary to use specific bitpix values depending on the
   requirements of any external programs that will be reading the
   FITS files.

   The minpix and maxpix parameters are used to specifiy the minimum
   and maximum data values when re-scaling to integers in the 16-bit
   case; this affects the dynamic range of the exported image. Data
   values outside this range will be clipped. If unspecified, these
   will be determined automatically from the minimum and maximum data
   values present.

   Generally, the conversion follows the `official FITS standard
   3.0. <https://fits.gsfc.nasa.gov/standard30/fits_standard30aa.pdf>`__

   .. note:: Info: Note that no subimaging of the fits image can be made
      with this task. The spectral reference frame can be changed
      prior to export using the task imreframe.
