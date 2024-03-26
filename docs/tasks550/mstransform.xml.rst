mstransform -- Split the MS, combine/separate/regrid spws and do channel and time averaging -- manipulation task
=======================================

Description
---------------------------------------

    
    The task mstransform can do the same functionalities available
    in cvel, partition, hanningsmooth and split without the need to read and write
    the output to disk multiple times. The main features of this task
    are:
    
    * take an input MS or Multi-MS (MMS)
    * ability to create an output MS or MMS
    * spw combination and separation
    * channel averaging taking flags and weights into account
    * time averaging taking flags and weights into account
    * reference frame transformation
    * Hanning smoothing
    
    All these transformations will be applied on the fly without any writing to
    disk to optimize I/O. The user can ask to create a Multi-MS in parallel using CASA's 
    cluster infrastructure using the parameter createmms. See MPIInterface 
    for more information on the cluster infrastructure.

    This task is implemented in a modular way to preserve the functionalities
    available in the replaced tasks. One can choose which functionality to apply
    or apply all of them by setting the corresponding parameters to True. Note 
    that there is an order in which the transformations are applied to the data that 
    makes logical sense on the point of view of the data analysis. 

    This task can create a multi-MS as the output. General selection
    parameters are included, and one or all of the various data columns
    (DATA, LAG_DATA and/or FLOAT_DATA, and possibly MODEL_DATA and/or
    CORRECTED_DATA) can be selected. It can also be used to create a normal
    MS, split-based on the given data selection parameters.

    The mstransform task creates a Multi-MS in parallel, using the CASA MPI framework.
    The user should start CASA as follows in order to run it in parallel.
    
    1) Start CASA on a single node with 8 engines. The first engine will be used as the
       MPIClient, where the user will see the CASA prompt. All other engines will be used
       as MPIServers and will process the data in parallel.
           mpicasa -n 8 casa --nogui --log2term
           mstransform(.....)
        
    2) Running on a group of nodes in a cluster.
           mpicasa -hostfile user_hostfile casa ....
           mstransform(.....)
            
        where user_hostfile contains the names of the nodes and the number of engines to use 
        in each one of them. Example:
            pc001234a, slots=5
            pc001234b, slots=4
     
    If CASA is started without mpicasa, it is still possible to create an MMS, but
    the processing will be done in sequential.
	
    The resulting WEIGHT_SPECTRUM produced by mstransform is in the statistical
    sense correct for the simple cases of channel average and time average, but not for
    the general re-gridding case, in which the error propagation formulas applicable for 
    WEIGHT_SPECTRUM are yet to be defined. Currently, as in cvel and in the imager,
    WEIGHT_SPECTRUM is transformed in the same way as the other data columns.
    Notice that this is not formally correct from the statistical point of view, 
    but is a good approximation at this stage.
        
    NOTE: the input/output in mstransform have a one-to-one relation.
          input MS  --  output MS
          input MMS --  output MMS
    
       unless the user sets the parameter createmms to True to create the following:
          input MS  --  output MMS




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
     - 
   * - outputvis
     - :code:`''`
     - 
   * - createmms
     - :code:`False`
     - 
   * - separationaxis
     - :code:`'auto'`
     - 
   * - numsubms
     - :code:`'auto'`
     - 
   * - tileshape
     - :code:`numpy.array( [  ] )`
     - 
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - scan
     - :code:`''`
     - 
   * - antenna
     - :code:`''`
     - 
   * - correlation
     - :code:`''`
     - 
   * - timerange
     - :code:`''`
     - 
   * - intent
     - :code:`''`
     - 
   * - array
     - :code:`''`
     - 
   * - uvrange
     - :code:`''`
     - 
   * - observation
     - :code:`''`
     - 
   * - feed
     - :code:`''`
     - 
   * - datacolumn
     - :code:`'corrected'`
     - 
   * - realmodelcol
     - :code:`False`
     - 
   * - keepflags
     - :code:`True`
     - 
   * - usewtspectrum
     - :code:`False`
     - 
   * - combinespws
     - :code:`False`
     - 
   * - chanaverage
     - :code:`False`
     - 
   * - chanbin
     - :code:`int(1)`
     - 
   * - hanning
     - :code:`False`
     - 
   * - regridms
     - :code:`False`
     - 
   * - mode
     - :code:`'channel'`
     - 
   * - nchan
     - :code:`int(-1)`
     - 
   * - start
     - :code:`int(0)`
     - 
   * - width
     - :code:`int(1)`
     - 
   * - nspw
     - :code:`int(1)`
     - 
   * - interpolation
     - :code:`'linear'`
     - 
   * - phasecenter
     - :code:`''`
     - 
   * - restfreq
     - :code:`''`
     - 
   * - outframe
     - :code:`''`
     - 
   * - veltype
     - :code:`'radio'`
     - 
   * - preaverage
     - :code:`False`
     - 
   * - timeaverage
     - :code:`False`
     - 
   * - timebin
     - :code:`'0s'`
     - 
   * - timespan
     - :code:`''`
     - 
   * - maxuvwdistance
     - :code:`float(0.0)`
     - 
   * - docallib
     - :code:`False`
     - 
   * - callib
     - :code:`''`
     - 
   * - douvcontsub
     - :code:`False`
     - 
   * - fitspw
     - :code:`''`
     - 
   * - fitorder
     - :code:`int(0)`
     - 
   * - want_cont
     - :code:`False`
     - 
   * - denoising_lib
     - :code:`True`
     - 
   * - nthreads
     - :code:`int(1)`
     - 
   * - niter
     - :code:`int(1)`
     - 
   * - disableparallel
     - :code:`False`
     - 
   * - ddistart
     - :code:`int(-1)`
     - 
   * - taql
     - :code:`''`
     - 
   * - monolithic_processing
     - :code:`False`
     - 
   * - reindex
     - :code:`True`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input Measurement set or Multi-MS.


outputvis
---------------------------------------

:code:`''`

Name of output Measurement Set or Multi-MS.


createmms
---------------------------------------

:code:`False`

Create a multi-MS output from an input MS.


separationaxis
---------------------------------------

:code:`'auto'`

Axis to do parallelization across(scan,spw,auto,baseline).


numsubms
---------------------------------------

:code:`'auto'`

The number of Sub-MSs to create (auto or any number)


tileshape
---------------------------------------

:code:`numpy.array( [  ] )`

List with 1 or 3 elements giving the tile shape of the disk data columns.


field
---------------------------------------

:code:`''`

Select field using ID(s) or name(s).


spw
---------------------------------------

:code:`''`

Select spectral window/channels.


scan
---------------------------------------

:code:`''`

Select data by scan numbers.


antenna
---------------------------------------

:code:`''`

Select data based on antenna/baseline.


correlation
---------------------------------------

:code:`''`

Correlation: '' ==> all, correlation="XX,YY".


timerange
---------------------------------------

:code:`''`

Select data by time range.


intent
---------------------------------------

:code:`''`

Select data by scan intent.


array
---------------------------------------

:code:`''`

Select (sub)array(s) by array ID number.


uvrange
---------------------------------------

:code:`''`

Select data by baseline length.


observation
---------------------------------------

:code:`''`

Select by observation ID(s).


feed
---------------------------------------

:code:`''`

Multi-feed numbers: Not yet implemented.


datacolumn
---------------------------------------

:code:`'corrected'`

Which data column(s) to process.


realmodelcol
---------------------------------------

:code:`False`

Make real a virtual MODEL column.


keepflags
---------------------------------------

:code:`True`

Keep *completely flagged rows* or drop them from the output.


usewtspectrum
---------------------------------------

:code:`False`

Force creation of the columns WEIGHT_SPECTRUM and SIGMA_SPECTRUM in the output MS, even if not present in the input MS.


combinespws
---------------------------------------

:code:`False`

Combine the input spws into a new output spw. Only supported when the number of channels is the same for all the spws.


chanaverage
---------------------------------------

:code:`False`

Average data in channels.


chanbin
---------------------------------------

:code:`int(1)`

Width (bin) of input channels to average to form an output channel.


hanning
---------------------------------------

:code:`False`

Hanning smooth data to remove Gibbs ringing.


regridms
---------------------------------------

:code:`False`

Transform channel labels and visibilities to a different spectral reference frame. Notice that u,v,w data is not transformed. 


mode
---------------------------------------

:code:`'channel'`

Regridding mode (channel/velocity/frequency/channel_b).


nchan
---------------------------------------

:code:`int(-1)`

Number of channels in the output spw (-1=all). Used for regridding, together with \'start\' and \'width\'.


start
---------------------------------------

:code:`int(0)`

Start of the output visibilities. Used for regridding, together with \'width\' and \'nchan\'. It can be in different units, depending on the regridding mode: first input channel (mode=\'channel\'), first velocity (mode=\'velocity\'), or first frequency (mode=\'frequency\'). Example values: \'5\', \'0.0km/s\', \'1.4GHz\', for channel, velocity, and frequency modes, respectively.


width
---------------------------------------

:code:`int(1)`

Channel width of the output visibilities. Used for regridding, together with \'start\', and \'nchan\'. It can be in different units, depending on the regridding mode: number of input channels (mode=\'channel\'), velocity (mode=\'velocity\'), or frequency (mode=\'frequency\'. Example values: \'2\', \'1.0km/s\', \'1.0kHz\', for channel, velocity, and frequency modes, respectively.


nspw
---------------------------------------

:code:`int(1)`

Number of output spws to create in output MS.


interpolation
---------------------------------------

:code:`'linear'`

Spectral interpolation method.


phasecenter
---------------------------------------

:code:`''`

Phase center direction to be used for the spectral coordinate transformation: direction measure or field index


restfreq
---------------------------------------

:code:`''`

Rest frequency to use for output.


outframe
---------------------------------------

:code:`''`

Output reference frame (''=keep input frame).


veltype
---------------------------------------

:code:`'radio'`

Velocity definition.


preaverage
---------------------------------------

:code:`False`

Pre-average channels before regridding, when the ratio between the output and and input widths is greater than 2.


timeaverage
---------------------------------------

:code:`False`

Average data in time.


timebin
---------------------------------------

:code:`'0s'`

Bin width for time averaging.


timespan
---------------------------------------

:code:`''`

Span the timebin across scan, state or both.


maxuvwdistance
---------------------------------------

:code:`float(0.0)`

Maximum separation of start-to-end baselines that can be included in an average. (meters)


docallib
---------------------------------------

:code:`False`

Enable on-the-fly (OTF) calibration as in task applycal


callib
---------------------------------------

:code:`''`

Path to calibration library file


douvcontsub
---------------------------------------

:code:`False`

Enable continuum subtraction as in task uvcontsub


fitspw
---------------------------------------

:code:`''`

Spectral window:channel selection for fitting the continuum


fitorder
---------------------------------------

:code:`int(0)`

Polynomial order for the fits


want_cont
---------------------------------------

:code:`False`

Produce continuum estimate instead of continuum subtracted data


denoising_lib
---------------------------------------

:code:`True`

Use new denoising library (based on GSL) instead of casacore fitting routines


nthreads
---------------------------------------

:code:`int(1)`

Number of OMP threads to use (currently maximum limited by number of polarizations)


niter
---------------------------------------

:code:`int(1)`

Number of iterations for re-weighted linear fit


disableparallel
---------------------------------------

:code:`False`

Hidden parameter for internal use only. Do not change it!


ddistart
---------------------------------------

:code:`int(-1)`

Hidden parameter for internal use only. Do not change it!


taql
---------------------------------------

:code:`''`

Table query for nested selections


monolithic_processing
---------------------------------------

:code:`False`

Hidden parameter for internal use only. Do not change it!


reindex
---------------------------------------

:code:`True`

Hidden parameter for use in the pipeline context only




