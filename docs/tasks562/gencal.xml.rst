gencal -- Specify Calibration Values of Various Types -- calibration task
=======================================

Description
---------------------------------------

The gencal task provides a means of specifying antenna-based
calibration values manually.  The values are put in designated tables
and applied to the data using applycal. Several specialized
calibrations are also generated with gencal.

Current antenna-based gencal options (caltype) are:
* 'amp'= amplitude correction
* 'ph' = phase correction
* 'sbd'= single-band delay (phase-frequency slope for each spw)
* 'mbd'= multi-band delay (phase-frequency slope over all spw)
* 'antpos' = ITRF antenna position corrections
* 'antposvla' = VLA-centric antenna position corrections 
* 'tsys' = Tsys from the SYSCAL table (ALMA)
* 'swpow' = EVLA switched-power gains (experimental)
* 'evlagain' (='swpow') (this syntax will deprecate)
* 'rq' = EVLA requantizer gains _only_
* 'swp/rq' = EVLA switched-power gains divided by requantizer gain
* 'opac' = Tropospheric opacity
* 'gc' = Gain curve (zenith-angle-dependent gain) (VLA only)
* 'eff' = Antenna efficiency (sqrt(K/Jy)) (VLA only)
* 'gceff' = Gain curve and efficiency (VLA only)
* 'tecim' = Time-dep TEC image specified in infile
   


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
   * - caltable
     - :code:`''`
     - Name of input calibration table
   * - caltype
     - :code:`''`
     - The calibration type: (amp, ph, sbd, mbd, antpos, antposvla, tsys, evlagain, opac, gc, gceff, eff, tecim)
   * - infile
     - :code:`''`
     - Input ancilliary file
   * - spw
     - :code:`''`
     - Select spectral window/channels
   * - antenna
     - :code:`''`
     - Select data based on antenna/baseline
   * - pol
     - :code:`''`
     - Calibration polarizations(s) selection
   * - parameter
     - :code:`numpy.array( [  ] )`
     - The calibration values
   * - uniform
     - :code:`True`
     - Assume uniform calibration values across the array


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file
                     Default: none

                        Example: vis='ngc5921.ms'



caltable
---------------------------------------

:code:`''`

Name of input calibration table
                     Default: none

                     If a calibration table does not exist, it will be
                     created. Specifying an existing table will result
                     in the parameters being applied
                     cumulatively. Only a single time-stamp for all
                     calibrations are supported, currently.  Do not
                     use a caltable created by gaincal, bandpass,
                     etc. 

                        Example: caltable='test.G'



caltype
---------------------------------------

:code:`''`

The calibration parameter type being specified
                     Default: none
                     Options: 'amp', 'ph', 'sbd', 'mbd', 'antpos',
                     'antposvla', 'tsys', 'evlagain', 'opac', 'gc',
                     'gceff', 'eff', 'tecim'

                     * 'amp' = gain (G) amplitude (1 real parameter
                       per pol, antenna, spw)
                     * 'ph'  = gain (G) phase (deg) (1 real parameter
                       per pol, antenna, spw)
                     * 'sbd' = single-band delays (nsec) (1 real
                       parameter per pol, antenna, spw)
                     * 'mbd' = multi-band delay (nsec) (1 real
                       parameter per pol, antenna, spw)
                     * 'antpos' = antenna position corrections (m) (3
                       real ITRF offset parameters per antenna; spw,
                       pol selection will be ignored)
                       With antenna='', this triggers an automated
                       lookup of antenna positions for EVLA and ALMA.
                     * 'antposvla' = antenna position corrections (m)
                       specified in the old VLA-centric coordinate
                       system
                     * 'tsys' = Tsys from the SYSCAL table (ALMA)
                     * 'evlagain' = EVLA switched-power gains
                       (experimental)
                     * 'opac' = Tropospheric opacity (1 real parameter
                       per antenna, spw)
                     * 'gc' = Antenna zenith-angle dependent gain
                       curve (auto-lookup)
                     * 'gceff' = Gain curve and efficiency
                       (auto-lookup)
                     * 'eff' = Antenna efficiency (auto-lookup)

                        Example: caltype='ph'



infile
---------------------------------------

:code:`''`

Input ancilliary file
                    Subparameter of caltype='gc|gceff|tecim'
                    Default: none



spw
---------------------------------------

:code:`''`

Select spectral window/channels
                     Default: '' (all spectral windows and channels)
           
                        Examples:
                        spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
                        spw='<2';  spectral windows less than 2 (i.e. 0,1)
                        spw='0:5~61'; spw 0, channels 5 to 61
                        spw='0,10,3:3~45'; spw 0,10 all channels, spw
                        3 - chans 3 to 45.
                        spw='0~2:2~6'; spw 0,1,2 with channels 2
                        through 6 in each.
                        spw = '*:3~64'  channels 3 through 64 for all sp id's
                        spw = ' :3~64' will NOT work.



antenna
---------------------------------------

:code:`''`

Select data based on antenna/baseline
                     Subparameter of selectdata=True
                     Default: '' (all)

                     If antenna string is a non-negative integer, it
                     is assumed an antenna index, otherwise, it is
                     assumed as an antenna name
  
                         Examples: 
                         antenna='5&6'; baseline between antenna
                         index 5 and index 6.
                         antenna='VA05&VA06'; baseline between VLA
                         antenna 5 and 6.
                         antenna='5&6;7&8'; baselines with
                         indices 5-6 and 7-8
                         antenna='5'; all baselines with antenna index
                         5
                         antenna='05'; all baselines with antenna
                         number 05 (VLA old name)
                         antenna='5,6,10'; all baselines with antennas
                         5,6,10 index numbers



pol
---------------------------------------

:code:`''`

Polarization selection for specified parameters
                     Default: pol='' (specified parameters apply to
                     all polarizations)

                        Example: pol='R' (specified parameters to
                        apply to R only)



parameter
---------------------------------------

:code:`numpy.array( [  ] )`

The calibration values

                     The calibration parameters, specified as a list,
                     to store in the caltable for the spw, antenna,
                     and pol selection.  The required length of the
                     list is determined by the caltype and the spw,
                     antenna, pol selection.  One "set" of parameters
                     (e.g., one value for 'amp', 'ph', etc., three
                     values for 'antpos') specified the same value for
                     all indicated spw, antenna, and pol.
                     OR, 
                     When specifying a long list of calibration
                     parameter values, these should be ordered first
                     (fastest) by pol (if pol!=''), then by antenna
                     (if antenna!=''), and finally (sloweset) by spw
                     (if spw!='').  Unspecified selection axes must
                     not be enumerated in the parameter list



uniform
---------------------------------------

:code:`True`

Assume uniform calibration values across the array
                    Subparameter of caltype='tsys'
                     Default: True
                     Options: True|False





