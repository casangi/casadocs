setjy -- Fills the model column with the visibilities of a calibrator -- modeling, calibration task
=======================================

Description
---------------------------------------

This task places the model visibility amp and phase associated with a
specified clean components image into the model column of the data
set.  The flux density (I,Q,U,V) for a point source calibrator can be
entered explicitly.

setjy need only be run on the calibrator sources with a known flux
density and/or model.

Models are available in CASA for 3C48, 3C138, 3C286, and 3C147 between 230 MHz 
and 43 GHz.  In addition, P-band models for the frequency range between 230 - 
470 MHz are available in CASA for 3C123, 3C196, 3C295, and 3C380.
These models are scaled to the precise frequency of the data.  Only I models are
presently available.

For Solar System Objects, model determination was updated and it is
available via the 'Butler-JPL-Horizons 2012' standard. Currently they
are modeled as uniformtemperature disks based on their ephemeris at
the time of observation (note that this may oversimplify objects, in
particular asteroids). Specify the name of the object in the 'field'
parameter.

The location of the models is system dependent:  At the AOC, the
models are in the directory::/usr/lib/casapy/data/nrao/VLA/CalModels/
3C286_L.im (egs).



Parameters
---------------------------------------
.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   * - Parameter
     - Default
     - Description
   * - vis
     - :code:`''`
     - Name of input visibility file
   * - field
     - :code:`''`
     - Select field using field id(s) or field name(s)
   * - spw
     - :code:`''`
     - Select spectral window/channels
   * - selectdata
     - :code:`False`
     - Other data selection parameters
   * - timerange
     - :code:`''`
     - Select data based on time range
   * - scan
     - :code:`''`
     - Scan number range
   * - intent
     - :code:`''`
     - Select observing intent
   * - observation
     - :code:`''`
     - Select by observation ID(s)
   * - scalebychan
     - :code:`True`
     - Scale the flux density on a per channel basis or else on a per spw basis
   * - standard
     - :code:`'Perley-Butler 2017'`
     - Flux density standard
   * - model
     - :code:`''`
     - File location for field model
   * - modimage
     - :code:`''`
     - File location for field model (deprecated)
   * - listmodels
     - :code:`False`
     - List the available models for VLA calibrators or Tb models for Solar System objects
   * - fluxdensity
     - :code:`int(-1)`
     - Specified flux density in Jy [I,Q,U,V]; (-1 will lookup values)
   * - spix
     - :code:`float(0.0)`
     - Spectral index (including higher terms) of I fluxdensity
   * - reffreq
     - :code:`'1GHz'`
     - Reference frequency for spix
   * - polindex
     - :code:`numpy.array( [  ] )`
     - Coefficients of an expansion of frequency-dependent linear polarization fraction expression
   * - polangle
     - :code:`numpy.array( [  ] )`
     - Coefficients of an expansion of frequency-dependent polarization angle expression (in radians)
   * - rotmeas
     - :code:`float(0.0)`
     - Rotation measure (in rad/m^2)
   * - fluxdict
     - :code:`{ }`
     - Output dictionary from fluxscale
   * - useephemdir
     - :code:`False`
     - Use directions in the ephemeris table
   * - interpolation
     - :code:`'nearest'`
     - Method to be used to interpolate in time
   * - usescratch
     - :code:`False`
     - Will create if necessary and use the MODEL_DATA
   * - ismms
     - :code:`False`
     - to be used internally for MMS
   * - fluxd
     - :code:`[ ]`
     - Dictionary containing flux densities and their errors.


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file
                     Default: none

                        Example: vis='ngc5921.ms'



field
---------------------------------------

:code:`''`

Select field using field id(s) or field name(s)
                     Default: '' (all fields, but run setjy one field
                     at a time)
                     
                     Use 'go listobs' to obtain the list id's or
                     names. If field string is a non-negative integer,
                     it is assumed a field index,  otherwise, it is
                     assumed a field name.

                        Examples:
                        field='0~2'; field ids 0,1,2
                        field='0,4,5~7'; field ids 0,4,5,6,7
                        field='3C286,3C295'; field named 3C286 and
                        3C295
                        field = '3,4C*'; field id 3, all names
                        starting with 4C
Field name(s)


spw
---------------------------------------

:code:`''`

Select spectral window/channels
                     Default: '' (all spectral windows)

                     NOTE: setjy only selects by spectral window, and
                     ignores channel selections.  Fine-grained control
                     could be achieved using (and possibly
                     constructing) a cube for modimage.



selectdata
---------------------------------------

:code:`False`

Other parameters for selecting part(s) of the MS to
operate on.
                     Default: False
                     Options: False|True

                     Currently all time-oriented and most likely only
                     of interest when using a Solar System object as a
                     calibrator.



timerange
---------------------------------------

:code:`''`

Select data based on time range
                     Subparameter of selectdata=True
                     Default = '' (all)

                        Examples:
                        timerange =
                        'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
                        (Note: if YYYY/MM/DD is missing date defaults
                        to first day in data set.)
                        timerange='09:14:0~09:54:0' picks 40 min on
                        first day 
                        timerange= '25:00:00~27:30:00' picks 1 hr to 3
                        hr 30min on NEXT day
                        timerange='09:44:00' pick data within one
                        integration of time
                        timerange='>10:24:00' data after this time



scan
---------------------------------------

:code:`''`

Scan number range
                     Subparameter of selectdata=True
                     Default: '' = all

                        Example:scan='1~5'

                     For multiple MS input, a list of scan strings can
                     be used:
                     scan=['0~100','10~200']
                     scan='0~100; scan ids 0-100 for all input MSes
                     Check 'go listobs' to insure the scan numbers are
                     in order.



intent
---------------------------------------

:code:`''`

Select observing intent
                     Default: '' (all

                        Example: using wildcard characters,
                        intent="*CALIBRATE_AMPLI*" will match field(s)
                        contains CALIBRATE_AMPLI in a list of intents

                     WARNING: If a source with a specific field id has
                     scans that can be distinguishable with intent
                     selection, one should set
                     usescatch=True. Otherwise, any existing model of
                     the source may be cleared and overwritten even if
                     the part of the scans not selected by intent.



observation
---------------------------------------

:code:`''`

Select by observation ID(s)
                     Subparameter of selectdata=True
                     Default: '' = all

                         Example: observation='0~2,4'



scalebychan
---------------------------------------

:code:`True`

Scale the flux density on a per channel basis?
                     Default: True
                     Options: True|False

                     This determines whether the fluxdensity set in
                     the model is calculated on a per channel
                     basis. If False then it only one fluxdensity
                     value is calculated per spw.  (Either way, all
                     channels in spw are modified.)  It is effectively
                     True if fluxdensity[0] >  0.0. 



standard
---------------------------------------

:code:`'Perley-Butler 2017'`

Flux density standard, used if fluxdensity[0] less than 0.0
                     Default: 'Perley-Butler 2017'
                     Options: 'Baars', 'Perley 90', 'Perley-Taylor
                     95', 'Perley-Taylor 99', 'Perley-Butler 2010',
                     'Perley-Butler 2013', 'Perley-Butler 2017',
                     'Scaife-Heald 2012', 'Stevens-Reynolds 2016',
                     'Butler-JPL-Horizons 2010', 'Butler-JPL-Horizons
                     2012', 'manual' 'fluxscale'

                     All but the last four options are for
                     extragalactic calibrators. The two 'Butler-JPL'
                     standards are for Solar System objects. Note that
                     Scaife-Heald 2012 is for the low frequencies
                     (mostly valid for the frequency range,
                     30-300MHz). 

                     Flux density calculation with Solar System
                     objects depends on ephemerides. The setjy task
                     looks for the data in
                     os.getenv('CASAPATH').split()[0] +
                     '/data/ephemerides/JPL-Horizons'. If no ephemeris
                     for the right object at the right time is
                     present, the calculation will fail.  Ask the
                     helpdesk to make an ephemeris.

                     For more information on individual calibrators,
                     see CASA Docs (https://casa.nrao.edu/casadocs/)



model
---------------------------------------

:code:`''`

Model image (I only) for setting the model visibilities.
                     Subparameter of standard="Perley-Butler 2010",
                     "Perley-Butler 2013", and "Perley-Butler 2017"
                     Default: '' (do not use a model image)

                     The model can be a cube, and its channels do not
                     have to exactly match those of vis.  It is
                     recommended to use model for sources that are
                     resolved by the observation, but the
                     Butler-JPL-Horizons standard supplies a basic
                     model of what several Solar System objects look
                     like. Each field must be done separately when
                     using a model image. 

                     Both the amplitude and phase are calculated.  At
                     the AOC or CV, the models are located in
                     casa['dirs']['data'] + '/nrao/VLA/CalModels/',
                     e.g. /usr/lib/casapy/data/nrao/VLA/CalModels/3C286_L.im
                     lib64

                     If model does not start with '/', setjy will look
                     for a match in '.', './CalModels', and any
                     CalModels directories within the
                     casa['dirs']['data'] tree (excluding certain
                     branches).

                     Note that model should be deconvolved, i.e. a set
                     of clean components instead of an image that has
                     been convolved with a clean beam.



modimage
---------------------------------------

:code:`''`

File location for field model
                     Deprecated



listmodels
---------------------------------------

:code:`False`

List the available models for VLA calibrators or Tb
models for Solar System objects
                     Subparameter of standard="Perley-Butler 2010",
                     "Perley-Butler 2013", and "Perley-Butler 2017" 
                     Default: False
                     Options: False|True

                     If True, do nothing but list candidates for model
                     (for extragalactic calibrators) that are present
                     on the system. It looks for *.im* *.mod* in
                     . including its sub-directories but skipping any
                     directory name start with ".", CalModels, and
                     CalModels directories in the casa['dirs']['data']
                     tree. It does not check whether they are
                     appropriate for the MS! If
                     standard='Butler-JPL-Horizons 2012', Tb models
                     (frequency-dependend brightness temperature
                     models) for Solar System objects used in the
                     standard. For standard='Butler-JPL-Horizons
                     2010', the recognized Solar System objects are
                     listed.



fluxdensity
---------------------------------------

:code:`int(-1)`

Specified flux density in Jy [I,Q,U,V]
                     Subparameter of standard="manual"
                     Default: -1 (uses [1,0,0,0] flux density for
                     unrecognized sources, and standard flux densities
                     for ones recognized by the default standard
                     Perley-Butler 2010).  

                     Only one flux density can be specified at a
                     time. The phases are set to zero.
                     setjy will try to use the standard if fluxdensity
                     is not positive.

                        Examples: 
                        fluxdensity=-1  will use the default standard
                        for recognized calibrators (like 3C286, 3C147
                        and 3C48) and insert 1.0  for selected fields
                        with unrecognized sources.
                        field = '1'; fluxdensity=[3.2,0,0,0] will put
                        in a flux density of I=3.2 for field='1'

                     At present (June 2000), this is the only method
                     to insert apolarized flux density model.

                        Example: fluxdensity=[2.63,0.21,-0.33,0.02]
                        will put in I,Q,U,V flux densities of
                        2.63,0.21,-0.33, and 0.02, respectively, in
                        the model column.



spix
---------------------------------------

:code:`float(0.0)`

Spectral index for I flux density
                     Subparameter of standard="manual"
                     Default: [] =>0.0 (no effect)
                     Options: a float or a list of float values

                     S = fluxdensity *
                     (freq/reffreq)**(spix[0]+spix[1]*log(freq/reffreq)+..)

                     Only used if fluxdensity is being used.
                     IMPORTANT: If fluxdensity is positive, and spix
                     is nonzero, then reffreq must be set too!

                     It is applied in the same way to all
                     polarizations, and does not account for Faraday
                     rotation or depolarization.

                        Example: [-0.7, -0.15] for alpha and a curvature term



reffreq
---------------------------------------

:code:`'1GHz'`

Reference frequency for spix
                     Subparameter of standard="manual"
                     Default: '1GHz' (this is only here to prevent
                     division by 0!)

                     Given with a unit with an optional frequency
                     frame (if the frame is not given, LSRK is
                     assumed). There should be no space between the
                     value and the unit  (e.g. '100.0GHz' or 'TOPO
                     100.0GHz' are correct but with  '100.0 GHz' you
                     will see a warning message that it will be
                     defaulted to LSRK). 

                        Example: '86.0GHz', 'TOPO 86.0GHz', '4.65e9Hz'

                     NOTE: If the flux density is being scaled by
                     spectral index, then reffreq must be set to
                     whatever reference frequency is correct for the
                     given fluxdensity and spix.  It cannot be
                     determined from vis.  On the other hand, if spix
                     is 0, then any positive frequency can be used
                     (and ignored).



polindex
---------------------------------------

:code:`numpy.array( [  ] )`

Coefficients of the frequency-dependent linear
polarization index (polarization fraction) 
                     Subparameter of standard="manual"
                     Default: []

                     Expressed as pol. index = sqrt(Q^2+U^2)/I = c0 +
                     c1*((freq-reffreq)/reffreq) +
                     c2*((freq-reffreq)/reffreq)^2 + .. When Q and U
                     flux densities are given fluxdensity, c0 is
                     determined from these flux densities and the
                     entry for c0 in polindex is ignored. Or Q and U
                     flux densities in fluxdensity can be set to 0.0
                     and then polindex[0] and polangle[0] are used to
                     determine Q and U at reffreq.

                        Example: [0.2, -0.01] (= [c0,c1]) 



polangle
---------------------------------------

:code:`numpy.array( [  ] )`

Coefficients of the frequency-dependent linear
polarization angle (in radians)
                     Subparameter of standard="manual"
                     Default: []

                     Expressed as pol. angle = 0.5*arctan(U/Q) = d0 +
                     d1*((freq-reffreq)/reffreq) +
                     d2*((freq-reffreq)/reffreq)^2 + .. When Q and U
                     flux densities are given in fluxdensity, d0 is
                     determined from these flux densities and the
                     entry for d0 in polangle is ignored. Or Q and U
                     flux densities in fluxdensity can be set to 0.0
                     and then polindex[0] and polangle[0] are used to
                     determine Q and U at reffreq. Here polangle
                     parameters are assumed to represent the intrinsic
                     polarization angle.

                        Example: [0.57, 0.2] (=[d0,d1])



rotmeas
---------------------------------------

:code:`float(0.0)`

Rotation measure (in rad/m^2)
                     Subparameter of standard="manual"
                     Default: 0.0

                     Note on the use of polindex, polangle and rotmeas
                     When the frequnecy-dependent polindex and
                     polangle are used, be sure to include all the
                     coefficients of both polindex and polangle to
                     describe frequency depencency. Otherwise
                     frequency-dependent Q and U flux densities are
                     not calculated correctly. If rotmeas is given,
                     the calculated Q and U flux densities are then
                     corrected for the Faraday rotation.



fluxdict
---------------------------------------

:code:`{ }`

Output dictionary from fluxscale
                     Subparameter of standard="fluxscale"

                     Using the flexibly results, the flux density,
                     spectral index, and reference frequency are
                     extracted and set to fluxdensity, spix, and
                     reffreq parameters, respectively. The field and
                     spw selections can be used to specify subset of
                     the fluxdict to be used to set the model. If they
                     are left as default (field="", spw="") all fields
                     and/or spws in the fluxdict (but those spws with
                     fluxd=-1 will be skipped) are used. 
 


useephemdir
---------------------------------------

:code:`False`

Use directions in the ephemeris table for the solar
system object?
                     Subparameter of standard="Butler-JPL-Horizons
                     2012",
                     Default: False
                     Options: False|True



interpolation
---------------------------------------

:code:`'nearest'`

Method to be used to interpolate in time for the time
variable sources (3C48,3C138,3C147).
                     Subparameter of standard="Perley-Butler 2013",
                     and "Perley-Butler 2017" 
                     Default: 'nearest'
                     Options: 'nearest|linear|cubic|spline'

                     This parameter is ignored for other non-variable
                     sources in the standard.



usescratch
---------------------------------------

:code:`False`

Will create if necessary and use the MODEL_DATA
                     Default: False
                     Options: False|True

                     * If False: 'virtual' model is created. The model
                       information is saved either in the SOURCE_MODEL
                       column in the SOURCE table (if one exists) or
                       in the keyword of the main table in the MS and
                       model visibilities are evaluated on the fly
                       when calculating  calibration or plotting in
                       plotms.
                     * If True: the model visibility will be evaluated
                       and saved on disk in the MODEL_DATA column.
                       This will increase your ms in size by a factor
                       of 1.5 (w.r.t. the case where  you only have
                       the DATA and the CORRECTED_DATA column). Use
                       True if you need to interact with the
                       MODEL_DATA in python, say. Also, use True if
                       you need finer than field and spw  selections
                       using scans/time (and when use with intent
                       selection, please see WARNING section in the
                       intent parameter description).

                     By running usescratch=T, it will remove the
                     existing virtual model from previous
                     runs. usescratch=F will not remove the existing
                     MODEL_DATA but in subsequent process the virtual
                     model with matching field and spw combination
                     will be used if it exists regardless of the
                     presence of the MODEL_DATA column.

                     NOTE: for usescratch=False, timerange, scan, and
                     observation are ignored (i.e. time-specific
                     virtual model is not possible.).



ismms
---------------------------------------

:code:`False`

to be used internally for MMS


fluxd
---------------------------------------

:code:`[ ]`

Dictionary containing flux densities and their errors.




