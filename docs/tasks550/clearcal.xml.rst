clearcal -- Re-initializes the calibration for a visibility data set -- calibration task
=======================================

Description
---------------------------------------
 
Clearcal reinitializes the calibration columns in a measurement
set. Specificially, it will set the MODEL_DATA column (if present) to
unity in total intensity and zero in polarization, and it will set the
CORRECTED_DATA column to the original (observed) DATA in the DATA
column.  Use the field and spw parameters to select which data to
initialize.  If the dataset does not yet have the scratch columns,
they will be created (MODEL_DATA only if addmodel=True) and initilized
for the whole dataset (field, spw, and intent will be ignored in this
case).



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
     - Name of input visibility file (MS)
   * - field
     - :code:`''`
     - Select field using field id(s) or field name(s)
   * - spw
     - :code:`''`
     - Select spectral window/channels
   * - intent
     - :code:`''`
     - Select observing intent
   * - addmodel
     - :code:`False`
     - Add MODEL_DATA scratch column


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file (MS)
                     Default: none

                        Example: vis='ngc5921.ms'



field
---------------------------------------

:code:`''`

Select field using field id(s) or field name(s)
                     default: '' (all fields)
                     
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



addmodel
---------------------------------------

:code:`False`

add MODEL_DATA along with CORRECTED_DATA?
                     Default: False (model will not be added)
                     Options: False|True

                     If False, it will add/reset only CORRECTED_DATA,
		     model visibilities will then be evaluated when
		     needed.





