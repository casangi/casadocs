fluxscale -- Bootstrap the flux density scale from standard calibrators -- calibration task
=======================================

Description
---------------------------------------

Bootstrap the flux density scale from standard calibrators.
	


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
   * - fluxtable
     - :code:`''`
     - Name of output, flux-scaled calibration table
   * - reference
     - :code:`numpy.array( [  ] )`
     - Reference field name(s) (transfer flux scale FROM)
   * - transfer
     - :code:`numpy.array( [  ] )`
     - Transfer field name(s) (transfer flux scale TO), \'\' -> all
   * - listfile
     - :code:`''`
     - Name of listfile that contains the fit information.  Default is '' (no file).
   * - append
     - :code:`False`
     - Append solutions?
   * - refspwmap
     - :code:`numpy.array( [  ] )`
     - Scale across spectral window boundaries
   * - gainthreshold
     - :code:`float(-1.0)`
     - Threshold (% deviation from the median) on gain amplitudes to be used in the flux scale calculation
   * - antenna
     - :code:`''`
     - Select data based on antenna/baseline
   * - timerange
     - :code:`''`
     - Select data based on time range
   * - scan
     - :code:`''`
     - Scan number range
   * - incremental
     - :code:`False`
     - Incremental caltable
   * - fitorder
     - :code:`int(1)`
     - Order of spectral fitting
   * - display
     - :code:`False`
     - Display some statistics of flux scaling
   * - fluxd
     - :code:`[ ]`
     - 


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

                        Example: caltable='ngc5921.gcal'. This cal
			table was obtained from task gaincal.=



fluxtable
---------------------------------------

:code:`''`

Name of output, flux-scaled calibration table
                     Default: none

                        Example: fluxtable='ngc5921.gcal2'

                     The gains in this table have been adjusted by the
		     derived flux density each calibrator.  The
		     MODEL_DATA column has NOT been updated for the
		     flux density of the calibrator.  Use setjy to do
		     this if it is a point source.



reference
---------------------------------------

:code:`numpy.array( [  ] )`

Reference field name(s) (transfer flux scale FROM)
                     Default: none

                        Example: reference='1328+307'

                     The names of the fields with a known flux
		     densities or visibilities that have been placed
		     in the MODEL column by setjy or ft for a model
		     not in the CASA system. The syntax is similar to
		     field.  Hence field index or names can be used.



transfer
---------------------------------------

:code:`numpy.array( [  ] )`

Transfer field name(s) (transfer flux scale TO)
                     Default: '' (all sources in caltable that are not
		     specified as reference sources.  Do not include
		     unknown target sources)

                     The names of the fields with unknown flux
		     densities. These should be point-like calibrator
		     sources The syntax is similar to field.  Hence
		     source index or names can be used.

                        Examples: transfer='1445+099, 3C84'; transfer
			= '0,4'

                     NOTE: All fields in reference and transfer must
		     have solutions in the caltable.



listfile
---------------------------------------

:code:`''`

Name of listfile that contains the fit information.
                     Default: '' (no fit listfile will be created)

                     The list file contains the flux density, flux
		     density error, S/N, and number of solutions (all
		     antennas and feeds) for each spectral window.  
                     NOTE: The nominal spectral window frequencies
		     will be included in the future.



append
---------------------------------------

:code:`False`

Append fluxscaled solutions to the fluxtable?
                     Default: False (will overwrite if already
		     existing)
                     Options: False|True



refspwmap
---------------------------------------

:code:`numpy.array( [  ] )`

Vector of spectral windows enabling scaling across
spectral windows
                     Default: [-1] (none)

                        Example with 4 spectral windows:
                        If the reference fields were observed only in
			spw=1 and 3, and the transfer fields were
			observed in all 4 spws (0,1,2,3), specify
			refspwmap=[1,1,3,3]. This will ensure that
			transfer fields observed in spws 0,1,2,3 will
			be referenced to reference field solutions
			only in spw 1 or 3.



gainthreshold
---------------------------------------

:code:`float(-1.0)`

Threshold in the input gain solutions to be used in % deviation from median values.
                     Default: -1 (no threshold)

                        Example: gainthreshold=0.15 (only used the
			gain solutions within 15% (inclusive) of the
			median gain value (per field and per spw). 



antenna
---------------------------------------

:code:`''`

Select data based on antenna/baseline
                     Subparameter of antenna
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



timerange
---------------------------------------

:code:`''`

Select data based on time range
                     Subparameter of antenna
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
                     Subparameter of antenna
                     Default: '' = all



incremental
---------------------------------------

:code:`False`

Create an incremental caltable containing only gain
correction factors ( flux density= 1/(gain correction factor)**2)?
                     Default: False
                     Options: False|True

                        Example: incremental=True (output a caltable
			containing flux scale factors.)

                     NOTE: If you use the incremental option, note
		     that BOTH this incremental fluxscale table AND an
		     amplitude vs. time table should be supplied in
		     applycal.



fitorder
---------------------------------------

:code:`int(1)`

Polynomial order of the spectral fitting for valid flux
densities
                     Default: 1

                     It falls back to a lower fitorder if there are
		     not enough solutions to fit with the requested
		     fitorder.



display
---------------------------------------

:code:`False`

Display statistics and/or spectral fitting results.
                     Default: False
                     Options: False|True

                     Currently only a histogram of the correction
		     factors to derive the final flux density for each
		     spectral window will be plotted.



fluxd
---------------------------------------

:code:`[ ]`

Dictionary containing the transfer fluxes and their errors.




