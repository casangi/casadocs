hanningsmooth -- Hanning smooth frequency channel data to remove Gibbs ringing -- manipulation task
=======================================

Description
---------------------------------------

The hanningsmooth task uses the MSTransform framework underneath but
keeps roughly the same interface as the old hanningsmooth task.
			
This function Hanning smooths the frequency channels with a weighted
running average. The weights are 0.5 for the central channel and 0.25
for each of the two adjacent channels. The first and last channels are
flagged. Inclusion of a flagged value in an average causes that data
value to be flagged. 

If the 'CORRECTED' data column is requested for an MS that does not
contain this column, it will use 'DATA' to calculate the smoothing and
save it to 'DATA' in the output MS.

WARNING: by default, all visibility columns will be smoothed. 



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
   * - outputvis
     - :code:`''`
     - Name of output visibility file
   * - keepmms
     - :code:`True`
     - Create a Multi-MS as the output if the input is a Multi-MS.
   * - field
     - :code:`''`
     - Select field using field id(s) or field name(s)
   * - spw
     - :code:`''`
     - Select spectral window/channels
   * - scan
     - :code:`''`
     - Scan number range
   * - antenna
     - :code:`''`
     - Select data based on antenna/baseline
   * - correlation
     - :code:`''`
     - Select data based on correlation
   * - timerange
     - :code:`''`
     - Select data based on time range
   * - intent
     - :code:`''`
     - Select observing intent
   * - array
     - :code:`''`
     - Select (sub)array(s) by array ID number.
   * - uvrange
     - :code:`''`
     - Select data by baseline length.
   * - observation
     - :code:`''`
     - Select by observation ID(s)
   * - feed
     - :code:`''`
     - Multi-feed numbers: Not yet implemented.
   * - datacolumn
     - :code:`'all'`
     - Which data column(s) to use for processing


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file
                     Default: none

                        Example: vis='ngc5921.ms'



outputvis
---------------------------------------

:code:`''`

Name of output visibility file
                     Default: '' (same as vis)

                        Example: outputvis='ngc5921_out.ms'



keepmms
---------------------------------------

:code:`True`

Create a Multi-MS as the output if the input is a
Multi-MS.

                     Default: True
                     Options: True|False

                     By default it will create a Multi-MS when the
		     input is a Multi-MS. The output Multi-MS will
		     have the same partition axis of the input
		     MMS. See CASA Docs for more information on
		     the MMS format.



field
---------------------------------------

:code:`''`

Select field using field id(s) or field name(s)
                     Default: '' (all fields)
                     
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



spw
---------------------------------------

:code:`''`

Select spectral window/channels
                     Default: ''=all spectral windows and channels
           
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

                     NOTE: mstransform does not support multiple
		     channel ranges per spectral window (';').



scan
---------------------------------------

:code:`''`

Scan number range
                     Subparameter of selectdata=True
                     Default: '' = all



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
                          antenna='!ea03,ea12,ea17': all baselines
			  except those that include EVLA antennas
			  ea03, ea12, or ea17.



correlation
---------------------------------------

:code:`''`

Select data based on correlation
                     Default: '' ==> all

                        Example: correlation="XX,YY".



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



intent
---------------------------------------

:code:`''`

Select observing intent
                     Default: '' (no selection by intent)

                        Example: intent='*BANDPASS*'  (selects data
			labelled with BANDPASS intent)



array
---------------------------------------

:code:`''`

(Sub)array number range
                     Default: '' (all)



uvrange
---------------------------------------

:code:`''`

Select data by baseline length.
                     Default = '' (all)

                        Examples:
                        uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lambda
                        uvrange='>4klambda';uvranges greater than 4 kilo-lambda
                        uvrange='0~1000km'; uvrange in kilometers



observation
---------------------------------------

:code:`''`

Select by observation ID(s)
                     Subparameter of selectdata=True
                     Default: '' = all

                         Example: observation='0~2,4'



feed
---------------------------------------

:code:`''`

Selection based on the feed 
                     NOT IMPLEMENTED YET!
                     Default: '' = all



datacolumn
---------------------------------------

:code:`'all'`

Which data column(s) to use for processing
                     (case-insensitive).
                     Default: 'all' (= whichever of the options that
		     are present)
                     Options: 'data', 'model', 'corrected',
		     'all','float_data', 'lag_data',
		     'float_data,data', 'lag_data,data'

                        Example: datacolumn='data'





