

# MIRIAD-CASA Dictionary 

CASA tasks equivalent to MIRIAD tasks

The Table below provides a list of common Miriad tasks, and their equivalent CASA tool or tool function names. The two packages differ in both their architecture and calibration and imaging models, and there is often not a direct correspondence. However, this index does provide a scientific user of CASA who is familiar with MIRIAD, with a simple translation table to map their existing data reduction knowledge to the new package.

In particular, note that the procedure of imaging and cleaning of visibility data between CASA and MIRIAD differs slightly. In MIRIAD the tasks invert, clean and restor are used in order to attain \"CLEAN\" images, whereas in CASA the task **clean**/**tclean** achieves the same steps as a single task.

  MIRIAD Task   CASA task/tool                                                    Description
  ------------- ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------
  atlod         importatca                                                        Import ATCA RPFITS files
  blflag        plotms/msview                                                     Interactive baseline based editor/flagger
  cgcurs        viewer                                                            Interactive image analysis
  cgdisp        viewer                                                            Image display, overlays
  clean         clean/tclean                                                      Clean an image
  delhd         imhead (mode=\'del\'), clearcal                                   Delete values in dataset/remove calibration tables 
  fits          importmiriad,importfits, exportfits, importuvfits, exportuvfits   FITS uv/image filler
  gethd         imhead (mode=\'get\')                                             Return values in image header
  gpboot        fluxscale                                                         Set flux density scale
  gpcal         gaincal, polcal                                                   Polarization leakage and gain calibration
  gpcopy        applycal                                                          Copy calibration tables from one source to another
  gpplt         plotcal, plotms                                                   Plot calibration solutions
  imcomb        immath                                                            Image combination
  imfit         imfit                                                             Image-plane component fitter
  impol         immath (mode=\'poli\' or \'pola\')                                Manipulate polarization images (see [example](http://www.atnf.csiro.au/computing/software/miriad/userguide/node149.html))
  imstat        imstat                                                            Image statistics
  imsub         imsubimage                                                        Extract sub-image
  invert        clean/tclean                                                      Synthesis imaging/make dirty map
  linmos        im tool (im.linearmosaic)                                         Linear mosaic combination of images
  maths         immath                                                            Calculations involving images
  mfboot        fluxscale                                                         Set flux density scale
  mfcal         bandpass, gaincal                                                 Bandpass and gain calibration
  moment        immoments                                                         Calculate image moments
  prthd         imhead, listobs, vishead                                          Print header of image or uvdata
  puthd         imhead (mode=\'put\')                                             Add/edit values in image header
  restor        clean                                                             Restore a clean component model
  selfcal       clean, gaincal, etc.                                              Selfcalibration of visibility data
  uvplt         plotms                                                            Plot visibility data
  uvspec        plotms                                                            Plot visibility spectra data
  uvsplit       split                                                             Split visibility dataset by source/frequency etc

 

