

# simutil 

A utility class to facilitate simulation

# Summary

**simutil** contains numerous utility methods which can assist users in generic ephemeris and geodesy calculations to aid in performing simulations and other activities in CASA, as well as some methods used internally by **simobserve** and **simanalyze**. Several of these tasks directly call the **simulator** tool in an attempt to lessen the amount of scripting required and to make it easier for the user. It is used by import and instantiation, similarly to testhelper and recipes:

```
from simutil import simutil

u=simutil()
```

```
help u.readantenna
```

Antenna configuration files are important for several tasks in **simutil** and other simulator tools. Below is an example of a properly formatted configuration file.

    #observatory=ALMA
    #COFA=-67.75,-23.02
    #coordsys=LOC (local tangent plane)
    # uid___A002_Xdb6217_X55ec_target.ms
    # x             y               z             diam  station  ant 
    -5.850273514   -125.9985379    -1.590364043   12.   A058     DA41
    -19.90369337    52.82680653    -1.892119601   12.   A023     DA42
    13.45860758    -5.790196849    -2.087805181   12.   A035     DA43
    5.606192499     7.646657746    -2.087775605   12.   A001     DA44
    24.10057423    -25.95933768    -2.08466565    12.   A036     DA45

The observatory, COFA (center of array), coordsys (coordinate system), x, y, z, diam (diameter) and name will be interpreted as header keys or value pairs if they contain \"=\" and begin with \#, and as comments otherwise. Other possible header keys are: zone, datum, or hemisphere. If no sixth column is provided, antenna names will default to station names. If no fifth column is provided, station names will default to A0x where x is the zero-indexed row number. To find the observatory name, one can check the known observatories list by using the **measures** tool command **me.obslist**. If an unknown observatory is specified, then one either must use absolute positions (coordsys, XYZ \[Cartesian coordinates\], UTM \[Universal Transverse Mercator\]), or specify COFA (longitude and latitude). coordsys can be XYZ (Earth-centered), UTM (easting, northing, and altitude), or LOC (xoffset, yoffset, and height). Files for many observatories can be found in the directory returned by the following command:

```
casa.values()[0]['data']+"/alma/simmos"
```

## **Tsys and Noise**

### simutil.noisetemp  

Noise temperature and efficiencies can be calculated for several telescopes: ALMA, ACA, EVLA, VLA, and SMA. The inputs for **simutil.noisetemp **method include: *telescope*, e.g., \"ALMA\", *freq* (observing frequency) as a quantity string, e.g., \"300GHz\", *diam* (optional - knows diameters for arrays above), e.g., \"12m\", *epsilon* = RMS surface accuracy in microns (also optional - this method contains the engineering specification values for each telescope). The outputs produced $\eta_p$ phase efficiency (from Ruze formula), $\eta_s$ spill (main beam) efficiency**,** $\eta_b$ geometrical blockage efficiency, $\eta_t$ taper efficiency, $\eta_q$ correlator efficiency including quantization, $t_{rx}$ receiver temperature. Where the total antenna efficiency can be calculated from these outputs as such: $\epsilon = \eta_p * \eta_s * \eta_b * \eta_t$.

<div class="alert alert-info">
**NOTE:** VLA correlator efficiency includes waveguide loss. EVLA correlator efficiency is probably optimistic at 0.88.
</div>

### simutil.sensitivity  

This method is used to calculate the noise in an observation by adding noise to visibilities in exactly the same way as **sm.corrupt** (if *doimnoise=True*) and also creates a simulated image from which to measure noise. The inputs to calculate sensitivity are: *freq*, *bandwidth* = channel width, e.g., \"1GHz\", *etime* = exposure time / length of track, e.g., \"500sec\", *integration* = scan time, e.g., \"10sec\", *elevation*, e.g., \"80deg\"; either an *antennalist* (a simobserve-format antenna configuration filename) must be given or the parameters *telescope*, *diam*, and *nant* (number of antennas) must be set. Other optional inputs include: *pwv* in mm, *doimnoise* uses the **simulator** task **sm.corrupt** to create an MS and image it to measure the noise, *integration* or integration time (units required) e.g., \"10s\", *debug*, *method* which is equivalent to the *mode* parameter in the **simulator** task **sm.setnoise** (options: \"tsys-atm\" (default) or \"tsys-manual\"), *tau0* or the zenith atmospheric opacity (must be set if *method=\"tsys-manual\"*), and *t_sky* (default=200 (K) when *method=\"tsys-manual\"*).

 

## **Geodesy and Antenna Positions**

<div class="alert alert-info">
**NOTE**: For more information on geodesy and pointing and other helper functions that are useful and available, click [here](https://www.ngs.noaa.gov/TOOLS/program_descriptions.html).
</div>

The ITRF frame mentioned in several of the following tasks is not the official ITRF (International Terrestrial Reference Frame), just a right-handed Cartesian system with X going through 0 latitude and 0 longitude, and Z going through the north pole.

### **simutil.readantenna     **

**simutil.readantenna** is a helper function to read antenna configuration files, using the *antab* parameter as an input. Outputs will be: earth-centered x,y,z, diameter, name, observatory_name, observatory_measure_dictionary.

<div class="alert alert-info">
**NOTE**: The observatory_measure_dictionary output was added between CASA 4.7 and 5.0.
</div>

### **simutil.baselineLengths**

When given an antenna *configfile*, this method will return the zenith baseline lengths.

### **simutil.approxBeam**

When given an antenna *configfile* and *freq* (in GHz)*,* this method will return the approximate beam size at zenith from the 90th percentile baseline length.

### **simutil.long2xyz  **

This method returns the nominal ITRF (X, Y, Z) coordinates \[m\] for a point at geodetic latitude (parameter *lat*) and longitude (parameter *lon*) \[radians\] and *elevation* \[m\]. 

### simutil.xyz2long         

When given ITRF Earth-centered (X, Y, Z, using the parameters *x*, *y*, and *z*) coordinates \[m\] for a point, this method returns geodetic latitude and longitude \[radians\] and elevation \[m\]. Elevation is measured relative to the closest point to the (latitude, longitude) on the WGS84 (World Geodetic System 1984) reference ellipsoid.

### **simutil.locxyz2itrf            **

This method returns the nominal ITRF (X, Y, Z) coordinates \[m\] for a point at \"local\" (x, y, z, using the parameters *locx*, *locy*, and *locz*) \[m\] measured at geodetic latitude (*lat*) and longitude (*longitude*) \[degrees\] and altitude (*alt*) of the reference point. The \"local\" (x, y, z) are measured relative to the closest point on the WGS84 reference ellipsoid, with z normal to the ellipsoid and y pointing north.

### **simtuil.itrf2loc            **

Given Earth-centered ITRF (X, Y, Z, using the parameters *x*, *y*, and *z*) coordinates \[m\] and the Earth-centered coords of the center of array (using the parameters *cx*, *cy*, and *cz*), this method returns local (x, y, z) \[m\] relative to the center of the array, oriented with x and y tangent to the closest point at the COFA (latitude, longitude) on the WGS84 reference ellipsoid, with z normal to the ellipsoid and y pointing north.

### **simutil.itrf2locname   **        

Given Earth-centered ITRF (X, Y, Z) coordinates \[m\] and the name of an known array using the *obsname* parameter (see **me.obslist**), the method **simutil.itrf2locname** returns local (x, y, z) \[m\] relative to the center of the array, oriented with x and y tangent to the closest point at the COFA (latitude, longitude) on the WGS84 reference ellipsoid, with z normal to the ellipsoid and y pointing north.

### **simutil.utm2xyz  **        

This method returns the nominal ITRF (X, Y, Z) coordinates \[m\] for a point at UTM *easting*, *northing*, *elevation* \[m\], and *zone* of a given *datum* (e.g., \'WGS84\') and north/south flag *nors* (\"N\" or \"S\", denotes northern or southern hemisphere). The ITRF frame used is not the official ITRF, just a right-handed Cartesian system with X going through 0 latitude and 0 longitude, and Z going through the north pole.  

### **simutil.utm2long         **

The method **simutil.utm2long** converts UTM coordinates to GPS longitude and latitude (in radians). This task has the following parameters: *east*, *north*, *zone*, *datum*, and *nors*.

 

## **Pointing and Directions**

### **simutil.calc_pointings2**

 This method is used to calculate mosaic pointings to cover a region. This returns a hexagonally packed list of pointings determined by the *size* (either \[size\[0\],size\[1\]\] or \[size,size\] if a single value is given) parameter separated by parameter *spacing* and fitting inside an area specified by *direction* and *maptype*. If multiple pointings can not be fit to the given parameters, a single pointing will be returned. If direction is a list, the task simply returns the direction and the number of pointings in it. The 3 options for *maptype* are: \"HEX\"agonal (default), \"SQU\"are, and \"ALM\"A (triangular tiling). The hexagonal packing starts with a horizontal row centered on *direction*, and the other rows alternate being horizontally offset by a half spacing. For hexagonal or square maptypes, the *relmargin* (default=0.5) parameter affects the number of pointings returned in the mosaic pattern. For triangular maptypes, the *beam* parameter is used to determine the number of pointings returned in the mosaic pattern, although this parameter is optional.

### **simutil.read_pointings**

This method will read a pointing list from a file using the parameter *filename*. The input file (ASCII) should contain at least 3 fields separated by a space which specify positions with epoch, RA and Dec (in degrees/minutes/seconds or hours/minutes/seconds). The optional field and time columns should be a list of decimal numbers which specifies integration time at each position (in units of seconds). The lines which start with \'\#\' are ignored and can be used as comment lines. Example of a file:

    #Epoch     RA          DEC      TIME(optional)
     J2000 23h59m28.10 -019d52m12.35 10.0
     J2000 23h59m32.35 -019d52m12.35 10.0
     J2000 23h59m36.61 -019d52m12.35 60.0

### **simutil.write_pointings**

This method will write a list of *pointings* out to a file (example above), given by the parameter *filename*. The optional parameter *time* can be an array of integration times.

### simutil.average_direction

This method will return the average of *directions* (default=None) as a string, and relative offsets.

### simutil.median_direction

This method will return the median of *directions* (default=None) as a string, and relative offsets.

### simutil.ephemeris

This method calculates the elevation of a source on a given *date*, in a given *direction*, seen from a given *telescope*. The *date* should be given in the format YEAR/MO/DY/TI:ME. The time given is referenced with the International Atomic Time, or TAI (from the French name name temps atomique international). Other optional parameters include: *usehourangle* (boolean parameter which sets or unsets the reference time at transit, essentially centering the plot), *ms* (uses the information from the OBSERVATION table in the given MeasurementSet and plots the entire range of the observation), and *cofa* (allows the user to change the center of the array position). The *cofa* parameter must be set if using an unknown observatory. A list of known observatories can be found by using the **measures** tool command **me.obslist**.

 

## **Utility**

### **simutil.statim **

This method will plot an *image* and calculate its statistics. Optional parameters: *plot* (default True), *incell*, *disprange* (low and high values for pl.imshow), *bar* (show colorbar, default=True), *showstats* (show stats on the image, default=True).

### **simutil.plotants**

An alternate antenna configuration plotting routine that takes arrays of *x,y*=local offset from the array center, *z*=altitude, *d*=diameter, and *name*. This method routine either plots points or, if the array is compact enough to see the diameters, plots to the actual scaled size of the dishes.****

### **simutil.modifymodel**

**simutil.modifymodel** is a method that converts a model image into a 4D-coordinate image that can be used in CASA, with axes in space, stokes, spectral order, which the Toolkit requires (e.g., **sm.predict** in the **simulator** tool). The input parameters *inimage* and *outimage* allow the user to specify the names of the input and output. Values that are absent in the input, or that the user wishes to override, can be input as quantity strings with the in\* parameters (*inbright*, *indirection*, *incell*, *incenter*, *inwidth*, *innchan*). e.g., *inbright*=\"4Jy/pixel\" will scale *outimage* to have 4Jy/pixel peak, *incell*=\"0.2arcsec\" will set the cell size in *outimage* to 0.2arcsec. The *flatimage* parameter allows one to also generate a flat (2D, integrated intensity) image from *inimage*, which can be useful for display purposes.

### **simutil.convimage**

Given a (2D) model (*modelflat*) image, this method will regrid it to the scale of the *outflat* image, and convolve it to the beam of the *outflat* image. This is useful to compare a skymodel with a simulated output image. The optional parameter *complist* allows the user to import a componentlist to add unresolved components to the *outflat* image. Information on creating a component list can be found in the CASA guides [here](https://casaguides.nrao.edu/index.php/Simulation_Guide_Component_Lists_(CASA_5.1)).

### **simutil.imtclean**

This wrapper function is the method by which the standard CASA imaging task **tclean** is called for simulated image reconstruction inside the task **simanalyze**. It replaces the deprecated method **simutil.imtclean**. If *dryrun*=True, this method only creates a template \'\[imagename.config\].tclean.last\' file for users to reference in their custom calls to **tclean**. The *cell* parameter expects a list of **qa.quantity** objects. Selecting individual fields for imaging is not supported.

