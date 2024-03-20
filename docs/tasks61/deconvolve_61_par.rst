deconvolve -- Image based deconvolver -- imaging task
=======================================

Parameter descriptions
=======================================



---------------------------------------
imagename
---------------------------------------

Input image to deconvolve


---------------------------------------
model
---------------------------------------

Output image containing deconvolved point model


---------------------------------------
psf
---------------------------------------

Point spread function (dirty beam)


---------------------------------------
alg
---------------------------------------

Algorithm to use (clark, hogbom, multiscale, mem) 


---------------------------------------
niter
---------------------------------------

number of iteration in deconvolution process


---------------------------------------
gain
---------------------------------------

CLEAN gain parameter


---------------------------------------
threshold
---------------------------------------

level below which sources will not be deconvolved


---------------------------------------
mask
---------------------------------------

image mask to limit region of deconvolution


---------------------------------------
scales
---------------------------------------

scale sizes (pixels) to deconvolve


---------------------------------------
sigma
---------------------------------------

mem parameter: Expected noise in image


---------------------------------------
targetflux
---------------------------------------

mem parameter: Estimated total flux in image


---------------------------------------
prior
---------------------------------------

mem parameter: prior image for mem search


