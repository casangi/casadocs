sdcal -- MS SD calibration task -- single dish task
=======================================

Description
---------------------------------------

Task sdcal implements a single-dish data calibration scheme similar to that of 
interferometry, i.e., generate calibration tables (caltables) and apply them. 
Available calibration modes are:
    'ps', 'otfraster', 'otf' for sky calibration
    'tsys' for Tsys calibration 
Each mode generates a caltable.
Caltables can be applied to the data by combining calibration
modes with the keyword 'apply'.

Calibration is applicable for fast moving source even like the moon which moves
quickly outside of the field of view (see the note of 'otf' mode in below).

Calibration mode must be set in accordance with the observing mode
of the data. Use case for each mode is as follows:
    'ps': position switch (including OTF) with explicit
          reference (OFF) spectra
    'otfraster': raster OTF scan without explicit OFFs
    'otf': non-raster OTF (e.g. double-circle) scan without explicit OFFs

So, if the data contains explicit reference spectra, 'ps' should
be used. Otherwise, 'otfraster' or 'otf' should be used.
In 'otfraster' and 'otf' modes, an edge marker automatically marks spectra from
specific regions of the observation pattern as reference (OFF) spectra.
These specific regions are:
- in 'otfraster' mode: regions near the beginning and the end of the raster 
scan lines.
- in 'otf' mode: regions near the periphery of the observation pattern.
Note: The 'otfraster' mode is designed for OTF observations without explicit OFF
spectra. However, it should work even if explicit reference spectra exist.
In that case, these spectra are ignored and spectra marked by edge marker are 
used as reference. 
Note: Detection of periphery scans in 'otf' mode is available for fast moving
sources, e.g., Sun, Moon. It is often the case antennas keep track of source motion
during the observations of moving sources so that the source is always at the map center.
In order to handle such observations, pheriphery search is done in the source frame
for known moving sources, in which the source is always at a rest position.

Apart from the way reference spectra are selected, the procedure to derive 
calibrated spectra is the same for all modes. Selected (or preset) 
OFF integrations are separated based on continuity in time domain, 
averaged in each segment, and then interpolated to timestamps for ON 
integrations. Effectively, it means that OFF integrations are 
averaged by each OFF spectrum for 'ps' mode, averaged by either ends 
of each raster row for 'otfraster' mode. The formula for calibrated 
spectrum is

    Tsys * (ON - OFF) / OFF. 

  


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - infile
     - :code:`''`
     - 
   * - calmode
     - :code:`'ps'`
     - SD calibration mode [\'ps\',\'otfraster\',\'otf\',\'tsys\',\'apply\', and allowed combinations]
   * - fraction
     - :code:`'10%'`
     - 
   * - noff
     - :code:`int(-1)`
     - 
   * - width
     - :code:`float(0.5)`
     - 
   * - elongated
     - :code:`False`
     - 
   * - applytable
     - :code:`''`
     - 
   * - interp
     - :code:`''`
     - 
   * - spwmap
     - :code:`*UNKNOWN*`
     - 
   * - outfile
     - :code:`''`
     - 
   * - overwrite
     - :code:`False`
     - overwrite the output file if already exists [True, False]
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - scan
     - :code:`''`
     - 
   * - intent
     - :code:`''`
     - 


Parameter Explanations
=======================================



infile
---------------------------------------

:code:`''`

name of input SD dataset (must be MS)


calmode
---------------------------------------

:code:`'ps'`

SD calibration mode


fraction
---------------------------------------

:code:`'10%'`

fraction of the OFF data to mark


noff
---------------------------------------

:code:`int(-1)`

number of the OFF data to mark


width
---------------------------------------

:code:`float(0.5)`

width of the pixel for edge detection


elongated
---------------------------------------

:code:`False`

whether observed area is elongated in one direction or not


applytable
---------------------------------------

:code:`''`

(List of) sky and/or tsys tables


interp
---------------------------------------

:code:`''`

Interpolation type in time[,freq]. Valid options are "nearest", "linear", "cspline", or any numeric string that indicates an order of polynomial interpolation. You can specify interpolation type for time and frequency separately by joining two of the above options by comma (e.g., "linear,cspline").


spwmap
---------------------------------------

:code:`*UNKNOWN*`

A dictionary indicating spw combinations to apply Tsys calibration to target. The key should be spw for Tsys calibration and its associated value must be a list of science spws to be applied.


outfile
---------------------------------------

:code:`''`

name of output file (See a WARNING in help)


overwrite
---------------------------------------

:code:`False`

overwrite the output file if already exists


field
---------------------------------------

:code:`''`

select data by field IDs and names, e.g. \'3C2*\' (\'\' = all)


spw
---------------------------------------

:code:`''`

select data by spw IDs (spectral windows), e.g., \'3,5,7\' (\'\' = all)


scan
---------------------------------------

:code:`''`

select data by scan numbers, e.g. \'21~23\' (\'\'=all)


intent
---------------------------------------

:code:`''`

select data by observation intent, e.g. \'OBSERVE_TARGET#ON_SOURCE\' (\'\'=all)




