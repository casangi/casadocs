accor -- Normalize visibilities based on auto-correlations -- calibration task
=======================================

Description
---------------------------------------

Determines the amplitude corrections neede due to errors in sampler
thresholds using measurements of auto-correlation spectra. This
correction is typically requiered for data correlated with the DiFX
correlator (such as VLBA data).  Other correlators (such as the SFXC
correlator used to correlate EVN data at JIVE) already apply this
correction at the correlator.  In this case, running this task is not
necessary.



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
     - Name of output gain calibration table
   * - field
     - :code:`''`
     - Select field using field id(s) or field name(s)
   * - spw
     - :code:`''`
     - Select spectral window/channels
   * - intent
     - :code:`''`
     - Select observing intent
   * - selectdata
     - :code:`True`
     - Other data selection parameters
   * - timerange
     - :code:`''`
     - Select data based on time range
   * - antenna
     - :code:`''`
     - Select data based on antenna/baseline
   * - scan
     - :code:`''`
     - Scan number range
   * - observation
     - :code:`''`
     - Select by observation ID(s)
   * - msselect
     - :code:`''`
     - Optional complex data selection (ignore for now)
   * - solint
     - :code:`'inf'`
     - Solution interval: egs. \'inf\', \'60s\' (see help)
   * - combine
     - :code:`''`
     - Data axes which to combine for solve (obs, scan, spw, and/or field)
   * - append
     - :code:`False`
     - Append solutions to the (existing) table
   * - docallib
     - :code:`False`
     - Use callib or traditional cal apply parameters
   * - callib
     - :code:`''`
     - Cal Library filename
   * - gaintable
     - :code:`numpy.array( [  ] )`
     - Gain calibration table(s) to apply on the fly
   * - gainfield
     - :code:`numpy.array( [  ] )`
     - Select a subset of calibrators from gaintable(s)
   * - interp
     - :code:`numpy.array( [  ] )`
     - Temporal interpolation for each gaintable (''=linear)
   * - spwmap
     - :code:`numpy.array( [  ] )`
     - Spectral windows combinations to form for gaintables(s)


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file
                     default: none
                        
                        example: vis='ngc5921.ms'



caltable
---------------------------------------

:code:`''`

Name of output gain calibration table
                     default: none
                        
                        example: caltable='ngc5921.gcal'



field
---------------------------------------

:code:`''`

Select field using field id(s) or field name(s)
                     default: '' --> all fields
                     
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

                     Note: do not forget to include the flux density
		     calibrator if you have one!



spw
---------------------------------------

:code:`''`

Select spectral window/channels

                        Examples:
                        spw='0~2,4'; spectral windows 0,1,2,4 (all
			channels)
                        spw='<2';  spectral windows less than 2
			(i.e. 0,1)
                        spw='0:5~61'; spw 0, channels 5 to 61,
			INCLUSIVE
                        spw='*:5~61'; all spw with channels 5 to 61
                        spw='0,10,3:3~45'; spw 0,10 all channels, spw
			3, channels 3 to 45.
                        spw='0~2:2~6'; spw 0,1,2 with channels 2
			through 6 in each.
                        spw='0:0~10;15~60'; spectral window 0 with
			channels 0-10,15-60. (NOTE ';' to separate
			channel selections)
                        spw='0:0~10^2,1:20~30^5'; spw 0, channels
			0,2,4,6,8,10, spw 1, channels 20,25,30 
                        type 'help par.selection' for more examples.



intent
---------------------------------------

:code:`''`

Select observing intent
                     default: '' (no selection by intent)

                        Example: intent='*BANDPASS*'  (selects data
			labelled with BANDPASS intent)



selectdata
---------------------------------------

:code:`True`

Other data selection parameters
                     default: True (Must set selectdata=True to select
		     other selection parameters.)



timerange
---------------------------------------

:code:`''`

Select data based on time range
                     Subparameter of selectdata=True
                     default = '' (all)

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



antenna
---------------------------------------

:code:`''`

Select data based on antenna/baseline
                     Subparameter of selectdata=True
                     default: '' (all)

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

                     Note: just for antenna selection, an integer (or
		     integer list) is converted to a string and
		     matched against the antenna 'name' first. Only if
		     that fails, the integer is matched with the
		     antenna ID. The latter is the case for most
		     observatories, where the antenna name is not
		     strictly an integer.
 


scan
---------------------------------------

:code:`''`

Scan number range
                     Subparameter of selectdata=True
                     default: '' = all

                     Check 'go listobs' to insure the scan numbers are
		     in order.



observation
---------------------------------------

:code:`''`

Select by observation ID(s)
                     Subparameter of selectdata=True
                     default: '' = all

                         Example: observation='0~2,4'



msselect
---------------------------------------

:code:`''`

Optional complex data selection (ignore for now)



solint
---------------------------------------

:code:`'inf'`

Solution interval (units optional)
                     default: 'inf' (~infinite, up to boundaries
		     controlled by combine)
                     Options: 'inf' (~infinite), 'int' (per
		     integration), any float or integer value with or
		     without units

                        Examples: solint='1min'; solint='60s';
			solint=60 --> 1 minute
                        solint='0s'; solint=0; solint='int' --> per
			integration
                        solint-'-1s'; solint='inf' --> ~infinite, up
			to boundaries -interacts with combine



combine
---------------------------------------

:code:`''`

Data axes which to combine for solve
                     default: '' (solutions will break at obs, scan,
		     field, and spw)
                     Options: '','obs','scan','spw',field', or any
		     comma-separated combination in a single string

                     For gaintype='K', if combine includes 'spw',
		     multi-band delays will be determined; otherwise,
		     (per-spw) single-band delays will be determined.

                        Example: combine='scan,spw' (extend solutions
			over scan boundaries)



append
---------------------------------------

:code:`False`

Append solutions to the (existing) table
                     default: False (overwrite existing table or make
		     new table)

                     Appended solutions must be derived from the same
		     MS as the existing caltable, and solution spws
		     must have the same meta-info (according to spw
		     selection and solint) or be non-overlapping.



docallib
---------------------------------------

:code:`False`

Control means of specifying the caltables
                     default: False --> Use gaintable, gainfield,
		     interp, spwmap, calwt. 

                     If True, specify a file containing cal library in
		     callib



callib
---------------------------------------

:code:`''`

Cal Library filename
                     Subparameter of callib=True

                     If docallib=True, specify a file containing cal
		     library directives



gaintable
---------------------------------------

:code:`numpy.array( [  ] )`

Gain calibration table(s) to apply on the fly
                     Subparameter of callib=False
                     default: '' (none)

                        Examples: gaintable='ngc5921.gcal'
                        gaintable=['ngc5921.ampcal','ngc5921.phcal']



gainfield
---------------------------------------

:code:`numpy.array( [  ] )`

Select a subset of calibrators from gaintable(s)
                     Subparameter of callib=False
                     default:'' --> all sources in table
                     
                     gaintable='nearest' --> nearest (on sky)
		     available field in table. Otherwise, same syntax
		     as field

                        Examples: 
                        gainfield='0~2,5' means use fields 0,1,2,5
			from gaintable
                        gainfield=['0~3','4~6'] means use field 0
			through 3 from first gain file, field 4
			through 6 for second.



interp
---------------------------------------

:code:`numpy.array( [  ] )`

Interpolation type (in time[,freq]) to use for each
gaintable.
                     Subparameter of callib=False
                     default: '' --> 'linear,linear' for all gaintable(s)
                     Options: Time: 'nearest', 'linear'. Freq:
		     'nearest', 'linear', 'cubic', 'spline'

                     When frequency interpolation is relevant (B, Df,
		     Xf), separate time-dependent and freq-dependent
		     interp types with a comma (freq _after_ the
		     comma). Specifications for frequency are ignored
		     when the calibration table has no
		     channel-dependence. Time-dependent interp options
		     ending in 'PD' enable a "phase delay" correction
		     per spw for non-channel-dependent calibration
		     types.
                     For multi-obsId datasets, 'perobs' can be
		     appended to the time-dependent interpolation
		     specification to enforce obsId boundaries when
		     interpolating in time.

                        Examples: 
                        interp='nearest' (in time, freq-dep will be
			linear, if relevant)
                        interp='linear,cubic' (linear in time, cubic
			in freq) 
                        interp='linearperobs,spline' (linear in time
			per obsId, spline in freq) 
                        interp=',spline' (spline in freq; linear in
			time by default)
                        interp=['nearest,spline','linear']  (for
			multiple gaintables)



spwmap
---------------------------------------

:code:`numpy.array( [  ] )`

Spectral windows combinations to form for gaintables(s)
                     Subparameter of callib=False
                     default: [] (apply solutions from each spw to
		     that spw only)

                        Examples:
                        spwmap=[0,0,1,1] means apply the caltable
			solutions from spw = 0 to the spw 0,1 and spw
			1 to spw 2,3.
                        spwmap=[[0,0,1,1],[0,1,0,1]]





