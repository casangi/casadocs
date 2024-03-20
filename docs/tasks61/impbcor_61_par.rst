impbcor -- Construct a primary beam corrected image from an image and a primary beam pattern. -- analysis task
=======================================

Parameter descriptions
=======================================



---------------------------------------
imagename
---------------------------------------

Name of the input (CASA, FITS, MIRIAD) image



---------------------------------------
pbimage
---------------------------------------

Name of the image (CASA, FITS, MIRIAD) of the primary
beam pattern or an array of pixel values.
                     Default: ''



---------------------------------------
outfile
---------------------------------------

Name of output CASA image. 
                     Default: none. Must be specified.



---------------------------------------
overwrite
---------------------------------------

If output file is specified, controls if an already
existing file by the same name can be overwritten. 
                     Default: True
                     Options: True|False

                     If true, the user is not prompted, the file if it
                     exists is automatically overwritten.



---------------------------------------
box
---------------------------------------

Rectangular region to select in direction plane.
                     Default: '' (use the entire direction plane)



---------------------------------------
region
---------------------------------------

Region selection. 
                     Default: '' (use the full image)



---------------------------------------
chans
---------------------------------------

Channels to use. 
                     Default: '' (use all channels)



---------------------------------------
stokes
---------------------------------------

Stokes planes to use.
                     Default: '' (use all Stokes planes)



---------------------------------------
mask
---------------------------------------

Mask to use.
                     Default: none



---------------------------------------
mode
---------------------------------------

Divide or multiply the image by the primary beam image. 
                     Default: 'divide'

                     Minimal match supported.



---------------------------------------
cutoff
---------------------------------------

Primary beam cutoff.
                     Default: -1.0 (no cutoff)

                     If mode is "d", all values less than this will be
                     masked. If "m", all values greater will be
                     masked. Less than 0, no cutoff (default)



---------------------------------------
stretch
---------------------------------------

Stretch the mask if necessary and possible? 
                     Default: False
                     Options: False|True



