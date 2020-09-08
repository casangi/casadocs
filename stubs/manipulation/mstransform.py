#
# stub function definition file for docstring parsing
#

def mstransform(vis, outputvis='', createmms=False, separationaxis='auto', numsubms='auto', tileshape=[0], field='', spw='', scan='', antenna='', correlation='', timerange='', intent='', array='', uvrange='', observation='', feed='', datacolumn='corrected', realmodelcol=False, keepflags=True, usewtspectrum=False, combinespws=False, chanaverage=False, chanbin=1, hanning=False, regridms=False, mode='channel', nchan=-1, start='0', width='1', nspw=1, interpolation='linear', phasecenter='', restfreq='', outframe='', veltype='radio', preaverage=False, timeaverage=False, timebin='0s', timespan='', maxuvwdistance=0.0, docallib=False, callib='', douvcontsub=False, fitspw='', fitorder=0, want_cont=False, denoising_lib=True, nthreads=1, niter=1, disableparallel=False, ddistart=-1, taql='', monolithic_processing=False, reindex=True):
    r"""
Split the MS, combine/separate/regrid spws and do channel and time averaging

Parameters
   - vis_ (string) - Name of input Measurement set or Multi-MS.
   - outputvis_ (string='') - Name of output Measurement Set or Multi-MS.
   - createmms_ (bool=False) - Create a multi-MS output from an input MS.

      .. raw:: html

         <details><summary><i> createmms = False </i></summary>

      - separationaxis_ (string='auto') - Axis to do parallelization across(scan,spw,auto,baseline).
      - numsubms_ ({string, int}='auto') - The number of Sub-MSs to create (auto or any number)
      - disableparallel_ (bool=False) - Hidden parameter for internal use only. Do not change it!
      - ddistart_ (int=-1) - Hidden parameter for internal use only. Do not change it!
      - taql_ (string='') - Table query for nested selections
      - reindex_ (bool=True) - Hidden parameter for use in the pipeline context only

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> createmms = True </i></summary>

      - separationaxis_ (string='auto') - Axis to do parallelization across(scan,spw,auto,baseline).
      - numsubms_ ({string, int}='auto') - The number of Sub-MSs to create (auto or any number)
      - disableparallel_ (bool=False) - Hidden parameter for internal use only. Do not change it!
      - ddistart_ (int=-1) - Hidden parameter for internal use only. Do not change it!
      - taql_ (string='') - Table query for nested selections
      - reindex_ (bool=True) - Hidden parameter for use in the pipeline context only

      .. raw:: html

         </details>
   - tileshape_ (intArray=[0]) - List with 1 or 3 elements giving the tile shape of the disk data columns.
   - field_ ({string, stringArray, int, intArray}='') - Select field using ID(s) or name(s).
   - spw_ ({string, stringArray, int, intArray}='') - Select spectral window/channels.
   - scan_ ({string, stringArray, int, intArray}='') - Select data by scan numbers.
   - antenna_ ({string, stringArray, int, intArray}='') - Select data based on antenna/baseline.
   - correlation_ ({string, stringArray}='') - Correlation: '' ==> all, correlation="XX,YY".
   - timerange_ ({string, stringArray, int, intArray}='') - Select data by time range.
   - intent_ ({string, stringArray, int, intArray}='') - Select data by scan intent.
   - array_ ({string, stringArray, int, intArray}='') - Select (sub)array(s) by array ID number.
   - uvrange_ ({string, stringArray, int, intArray}='') - Select data by baseline length.
   - observation_ ({string, stringArray, int, intArray}='') - Select by observation ID(s).
   - feed_ ({string, stringArray, int, intArray}='') - Multi-feed numbers: Not yet implemented.
   - datacolumn_ (string='corrected') - Which data column(s) to process.

      .. raw:: html

         <details><summary><i> datacolumn = model </i></summary>

      - realmodelcol_ (bool=False) - Make real a virtual MODEL column.

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> datacolumn = all </i></summary>

      - realmodelcol_ (bool=False) - Make real a virtual MODEL column.

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> datacolumn = data,model,corrected </i></summary>

      - realmodelcol_ (bool=False) - Make real a virtual MODEL column.

      .. raw:: html

         </details>
   - keepflags_ (bool=True) - Keep *completely flagged rows* or drop them from the output.
   - usewtspectrum_ (bool=False) - Force creation of the columns WEIGHT_SPECTRUM and SIGMA_SPECTRUM in the output MS, even if not present in the input MS.
   - combinespws_ (bool=False) - Combine the input spws into a new output spw. Only supported when the number of channels is the same for all the spws.
   - chanaverage_ (bool=False) - Average data in channels.

      .. raw:: html

         <details><summary><i> chanaverage = True </i></summary>

      - chanbin_ ({int, intArray}=1) - Width (bin) of input channels to average to form an output channel.

      .. raw:: html

         </details>
   - hanning_ (bool=False) - Hanning smooth data to remove Gibbs ringing.
   - regridms_ (bool=False) - Transform channel labels and visibilities to a different spectral reference frame. Notice that u,v,w data is not transformed. 

      .. raw:: html

         <details><summary><i> regridms = True </i></summary>

      - mode_ (string='channel') - Regridding mode (channel/velocity/frequency/channel_b).
      - nchan_ (int=-1) - Number of channels in the output spw (-1=all). Used for regridding, together with \'start\' and \'width\'.
      - start_ (variant='0') - Start of the output visibilities. Used for regridding, together with \'width\' and \'nchan\'. It can be in different units, depending on the regridding mode: first input channel (mode=\'channel\'), first velocity (mode=\'velocity\'), or first frequency (mode=\'frequency\'). Example values: \'5\', \'0.0km/s\', \'1.4GHz\', for channel, velocity, and frequency modes, respectively.
      - width_ (variant='1') - Channel width of the output visibilities. Used for regridding, together with \'start\', and \'nchan\'. It can be in different units, depending on the regridding mode: number of input channels (mode=\'channel\'), velocity (mode=\'velocity\'), or frequency (mode=\'frequency\'. Example values: \'2\', \'1.0km/s\', \'1.0kHz\', for channel, velocity, and frequency modes, respectively.
      - nspw_ (int=1) - Number of output spws to create in output MS.
      - interpolation_ (string='linear') - Spectral interpolation method.
      - phasecenter_ (variant='') - Phase center direction to be used for the spectral coordinate transformation: direction measure or field index
      - restfreq_ (string='') - Rest frequency to use for output.
      - outframe_ (string='') - Output reference frame (''=keep input frame).
      - veltype_ (string='radio') - Velocity definition.
      - preaverage_ (bool=False) - Pre-average channels before regridding, when the ratio between the output and and input widths is greater than 2.

      .. raw:: html

         </details>
   - preaverage_ (bool=False) - Pre-average channels before regridding, when the ratio between the output and and input widths is greater than 2.
   - timeaverage_ (bool=False) - Average data in time.

      .. raw:: html

         <details><summary><i> timeaverage = True </i></summary>

      - timebin_ (string='0s') - Bin width for time averaging.
      - timespan_ ({string, stringArray}='') - Span the timebin across scan, state or both.
      - maxuvwdistance_ (double=0.0) - Maximum separation of start-to-end baselines that can be included in an average. (meters)

      .. raw:: html

         </details>
   - docallib_ (bool=False) - Enable on-the-fly (OTF) calibration as in task applycal

      .. raw:: html

         <details><summary><i> docallib = True </i></summary>

      - callib_ (string='') - Path to calibration library file

      .. raw:: html

         </details>
   - douvcontsub_ (bool=False) - Enable continuum subtraction as in task uvcontsub

      .. raw:: html

         <details><summary><i> douvcontsub = True </i></summary>

      - fitspw_ (string='') - Spectral window:channel selection for fitting the continuum
      - fitorder_ (int=0) - Polynomial order for the fits
      - want_cont_ (bool=False) - Produce continuum estimate instead of continuum subtracted data
      - denoising_lib_ (bool=True) - Use new denoising library (based on GSL) instead of casacore fitting routines
      - nthreads_ (int=1) - Number of OMP threads to use (currently maximum limited by number of polarizations)
      - niter_ (int=1) - Number of iterations for re-weighted linear fit

      .. raw:: html

         </details>


Description
   **mstransform** is a multipurpose task that provides all the
   functionality of
   `split <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_split>`__,
   `partition <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_partition>`__,
   `cvel <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_cvel2>`__,
   `hanningsmooth <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_hanningsmooth>`__ **,** `uvcontsub <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_uvcontsub3>`__
   and
   `applycal <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_applycal>`__
   with the possibility of applying each of these transformations
   separately or together in an in-memory pipeline, thus avoiding
   unnecessary I/O steps. Each transformation can be activated
   through a boolean parameter in the task interface.Below are the
   main parameter descriptions. See also how to run **mstransform**
   for some use-cases in the
   `Examples <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_mstransform/examples>`__
   tab menu.

   

   .. rubric:: Parameter Descriptions
      

   .. rubric:: *createmms*
      

   When set to True, this parameter will create an output Multi-MS,
   which is the basic step for running CASA in parallel. See more
   about this in the
   `Parallelization <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing>`__
   chapter.

   

   .. rubric:: Combination of spws: *combinespws*
      

   Combine the input spectral windowsinto a new outputspectral
   window.Whenever the data to be combined has different *EXPOSURE*
   valuesin the spectral windows, mstransform will use the
   *WEIGHT_SPECTRUM*for the combination. If *WEIGHT_SPECTRUM* is not
   available, it willuse the values from the *WEIGHT* column. Each
   output channel is calculatedusing the following equation:

   .. math:: outputChannel_{j} = \frac{\sum (inputChannel_{i}*contributionFraction_{i}*inputWeightSpectrum_{i})}{\sum(contributionFraction_{i}*inputWeightSpectrum_{i})}

   .. warning:: **ALERT**: The combination of spws is only supported when the
      number of channels is the same forall the spws. Using this
      option with different numbers of channels fordifferent spws
      will result in an error.

   

   .. rubric:: Channel averaging: *chanaverage*
      

   Average data across channels. Partially flagged data is not
   included in the averageunless all data contributing to a given
   output channel is flagged. In this case, **mstransform**
   calculates the average of all flagged data, and writes it to the
   output MSwith the corresponding flag set to true. If present,
   *WEIGHT_SPECTRUM*/*SIGMA_SPECTRUM*are used together with the
   channelized flags (FLAG), to compute a weighted average (using
   *WEIGHT_SPECTRUM* for *CORRECTED_DATA* and *SIGMA_SPECTRUM* for
   *DATA*). The sub-parameter *chanbin* takes an integer number or a
   list of integers. If a list is given, each bin applies to one of
   the selected spws.

   .. note:: **NOTE**:*WEIGHT_SPECTRUM*/*SIGMA_SPECTRUM* will be used (if
      present) inaddition to the flags to compute a weighted
      average. The calculationsis done as follows:

   #. When WEIGHT_SPECTRUM/SIGMA_SPECTRUM are not present:

   .. math:: Average = \frac{\sum(Chan_{i}*Flag_{i})}{\sum(Flag_{i})}

   #. When WEIGHT_SPECTRUM/SIGMA_SPECTRUM are present:

   

   .. math:: Average = \sum(Chan_i*Flag_i*WeightSpectrum_i) \sum(Flag_i*WeightSpectrum_i)

   

   .. rubric:: Hanning smoothing: *hanning*
      

   This function Hanning smooths the frequency channels witha
   weighted running average to remove Gibbs ringing.The weights are
   0.5 for the central channel and 0.25 for each of the two adjacent
   channels. The first and last channels are flagged. Inclusion of a
   flagged value in an average causes that data value to be flagged.
   By default, all visibility data columns available in the MS will
   be smoothed, unless a specific column is given in the *datacolumn*
   parameter.

   

   .. rubric:: Reference frame transformation: *regridms*
      

   Transform channel labels and visibilities to a different spectral
   reference frame, which is appropriate for science analysis. For
   example, transform from TOPO to LSRK to correct for Doppler shifts
   throughout the time of the observation.

   .. note:: **NOTE**: U,V,W data are not transformed with this function

   The regridding *mode* can be "channel", "velocity", "frequency" or
   "channel_b", *channel*being the default.When set to *velocity*
   or *frequency*, it means that the channels must be specifiedin
   the respective units. When set to *channel_b* it means an
   alternative channel mode that does not force an equidistant grid,
   which is faster to process.

   The *start* sub-parameter gives the first channel to use in the
   output spw (depending on the *mode*).When *mode='channel'*,
   *start* means the first channel in the input spwto use when
   creating the output spw. When *mode='frequency'*,*start* means
   the lowest frequency of the output spw. If this informationis not
   available, **mstransform** will calculate it automatically.

   The *width* sub-parameter gives the width of the output channels.
   The *width* is expressed in different units, depending on the
   *mode* chosen. This way the sub-parameter *width* can take units
   of either number of input channels (mode="channel"), velocity
   (mode="velocity"), or frequency (mode="frequency"). For example,
   the value of the *width* parameter can be "4" (mode="channel"),
   "-1.0km/s" (mode="velocity"), or "1.0kHz" (mode="frequency").

   .. warning:: **NOTE**: **mstransform** will only shift spws with channel
      widths of the same sign in a single operation. If you are
      regridding spws with mixed positive and negative channel
      widths, you should run this task separated for each group of
      spws. You can verify the channel widths for your MS using
      **listobs** for example, and looking at the SPW table, column
      ChanWidth.

   It is possible to separate the spectral windows into a given
   number of spws. This is achieved with the sub-parameter *nspw*,
   which is activate when set to > 1.Internally, the frameworkwill
   combine the selected spws before separating them so thatchannel
   gaps and overlaps are taken into account. This sub-parameterwill
   create a regular grid of spws in the output MS. If *nchan*is set,
   it will refer to the number of output channels in eachof the
   separated spws.

   

   .. rubric:: Time averaging:*timeaverage*
      

   Average data across time by setting *timeaverage=True* and giving
   the bin for averaging using the sub-parameter *timebin*. Partially
   flagged data is not included in the averageunless all data
   contributing to a given output channel is flagged. In this case,
   **mstransform** calculates the average of all flagged data, and
   writes it to the output MSwith the corresponding flag set to
   True. If *keepflags=False*, the fully flagged datais not written
   to the output MS. If present,
   *WEIGHT_SPECTRUM*/*SIGMA_SPECTRUM*are used together with the
   channelized flags (*FLAG*), to compute a weighted average (using
   *WEIGHT_SPECTRUM* for *CORRECTED_DATA* and *SIGMA_SPECTRUM* for
   *DATA*). Otherwise *WEIGHT*/*SIGMA* are used instead to average
   together data from different integrations.

   The *timespan*sub-parameter will span the*timebin*across scans,
   states or both. State is equivalent to sub-scans and one scan may
   have several state IDs. Another option when doing time averaging
   is to provide amaximum separation of start-to-end baselines that
   can be included in an average with the use of the *maxuvwdistance*
   sub-parameter.

   

   .. rubric:: On-the-flycalibration parameters:*docallib*
      

   **mstransform** is able to apply the calibrations on the fly,
   similar to the **applycal** task. This is possible by specifyinga
   `Cal
   Library <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/uv-manipulation/on-the-fly-calibration>`__
   filename that contains the actual specification for the
   calibrations to be applied. See more about the Cal Library file
   syntax`here <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/cal-library-syntax>`__.
   See also an
   `example <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_mstransform/examples>`__
   of applying the Cal library in mstransform.

   

   .. rubric:: Multi-MS Processing using mstransform
      

   Task **mstransform** will process an input
   `Multi-MS <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/the-multi-ms>`__
   (MMS) in parallel whenever possible. Each Sub-MS ofthe MMS will
   be processed in a separate computer coreand the results will be
   post-processed at theend to create an output MMS. The output MMS
   will have the same *separationaxis* of the inputMMS, which will
   be written to the table.info file inside the MMS directory.

   Naturally, some transformations available in **mstransform**
   require more care when the userfirst partition the MS. If one
   wants to do a combination of spws by setting the
   parameter*combinespws=True* in **mstransform**, the input MMS
   needs to contain all theselected spws in each of the Sub-MSs or
   the processing will fail. For this, one may set the
   initial*separationaxis* to 'scan' or use the default 'auto' with
   a proper *numsubms* set so that each Sub-MS in the MMS is
   self-contained with all the necessary spws for the combination.

   The task will check if the Sub-MSs contain all the selected spws
   when *combinespws=True*and if not, it will issue a warning and
   process the input MMS as a monolithic MS. In thiscase, the
   separation axis of the output MMS will be set to 'scan',
   regardless of what the inputaxis was.

   A similar case happens when the separation axis of the input MMS
   is per 'scan' and the userwantsto do time averaging with time
   spanning across scans. If the individual Sub-MSs are
   notself-contained of the necessary scans and the duration of the
   scans is shorter than the given *timebin*, the spanning will not
   be possible. In this case, the task will process the input MMS
   asa monolithic MS and will set the axis of the output MMS to spw.

   It is important that the user sets the separation axis correctly
   when first partitioning the MS.See the table below for when it is
   possible to process the input MMS in parallel or not,
   using**mstransform**.

   +-----------------+-----------------+-----------------+-----------------+
   | **input MMS     | **com           | **nspw > 1**    | **tim           |
   | axis**          | binespws=True** |                 | eaverage=True** |
   |                 |                 |                 |                 |
   |                 |                 |                 | **ti            |
   |                 |                 |                 | mespan='scan'** |
   +-----------------+-----------------+-----------------+-----------------+
   | scan            | YES             | YES             | NO              |
   +-----------------+-----------------+-----------------+-----------------+
   | spw             | NO              | NO              | YES             |
   +-----------------+-----------------+-----------------+-----------------+
   | auto            | maybe           | maybe           | maybe           |
   +-----------------+-----------------+-----------------+-----------------+

   .. note:: **NOTE**: If **mstransform** decides it's not possible to
      process the MMS in parallel, it will still create an output but
      the processing will run serially without any parallelization
      involved.




Details
   Explanation of each parameter

.. _vis:

   .. rubric:: vis

   | Name of input Measurement set or Multi-MS.

.. _outputvis:

   .. rubric:: outputvis

   | Name of output Measurement Set or Multi-MS.

.. _createmms:

   .. rubric:: createmms

   | Create a multi-MS output from an input MS.

.. _separationaxis:

   .. rubric:: separationaxis

   | Axis to do parallelization across(scan,spw,auto,baseline).

.. _numsubms:

   .. rubric:: numsubms

   | The number of Sub-MSs to create (auto or any number)

.. _tileshape:

   .. rubric:: tileshape

   | List with 1 or 3 elements giving the tile shape of the disk data columns.

.. _field:

   .. rubric:: field

   | Select field using ID(s) or name(s).

.. _spw:

   .. rubric:: spw

   | Select spectral window/channels.

.. _scan:

   .. rubric:: scan

   | Select data by scan numbers.

.. _antenna:

   .. rubric:: antenna

   | Select data based on antenna/baseline.

.. _correlation:

   .. rubric:: correlation

   | Correlation: '' ==> all, correlation="XX,YY".

.. _timerange:

   .. rubric:: timerange

   | Select data by time range.

.. _intent:

   .. rubric:: intent

   | Select data by scan intent.

.. _array:

   .. rubric:: array

   | Select (sub)array(s) by array ID number.

.. _uvrange:

   .. rubric:: uvrange

   | Select data by baseline length.

.. _observation:

   .. rubric:: observation

   | Select by observation ID(s).

.. _feed:

   .. rubric:: feed

   | Multi-feed numbers: Not yet implemented.

.. _datacolumn:

   .. rubric:: datacolumn

   | Which data column(s) to process.

.. _realmodelcol:

   .. rubric:: realmodelcol

   | Make real a virtual MODEL column.

.. _keepflags:

   .. rubric:: keepflags

   | Keep *completely flagged rows* or drop them from the output.

.. _usewtspectrum:

   .. rubric:: usewtspectrum

   | Force creation of the columns WEIGHT_SPECTRUM and SIGMA_SPECTRUM in the output MS, even if not present in the input MS.

.. _combinespws:

   .. rubric:: combinespws

   | Combine the input spws into a new output spw. Only supported when the number of channels is the same for all the spws.

.. _chanaverage:

   .. rubric:: chanaverage

   | Average data in channels.

.. _chanbin:

   .. rubric:: chanbin

   | Width (bin) of input channels to average to form an output channel.

.. _hanning:

   .. rubric:: hanning

   | Hanning smooth data to remove Gibbs ringing.

.. _regridms:

   .. rubric:: regridms

   | Transform channel labels and visibilities to a different spectral reference frame. Notice that u,v,w data is not transformed.

.. _mode:

   .. rubric:: mode

   | Regridding mode (channel/velocity/frequency/channel_b).

.. _nchan:

   .. rubric:: nchan

   | Number of channels in the output spw (-1=all). Used for regridding, together with \'start\' and \'width\'.

.. _start:

   .. rubric:: start

   | Start of the output visibilities. Used for regridding, together with \'width\' and \'nchan\'. It can be in different units, depending on the regridding mode: first input channel (mode=\'channel\'), first velocity (mode=\'velocity\'), or first frequency (mode=\'frequency\'). Example values: \'5\', \'0.0km/s\', \'1.4GHz\', for channel, velocity, and frequency modes, respectively.

.. _width:

   .. rubric:: width

   | Channel width of the output visibilities. Used for regridding, together with \'start\', and \'nchan\'. It can be in different units, depending on the regridding mode: number of input channels (mode=\'channel\'), velocity (mode=\'velocity\'), or frequency (mode=\'frequency\'. Example values: \'2\', \'1.0km/s\', \'1.0kHz\', for channel, velocity, and frequency modes, respectively.

.. _nspw:

   .. rubric:: nspw

   | Number of output spws to create in output MS.

.. _interpolation:

   .. rubric:: interpolation

   | Spectral interpolation method.

.. _phasecenter:

   .. rubric:: phasecenter

   | Phase center direction to be used for the spectral coordinate transformation: direction measure or field index

.. _restfreq:

   .. rubric:: restfreq

   | Rest frequency to use for output.

.. _outframe:

   .. rubric:: outframe

   | Output reference frame (''=keep input frame).

.. _veltype:

   .. rubric:: veltype

   | Velocity definition.

.. _preaverage:

   .. rubric:: preaverage

   | Pre-average channels before regridding, when the ratio between the output and and input widths is greater than 2.

.. _timeaverage:

   .. rubric:: timeaverage

   | Average data in time.

.. _timebin:

   .. rubric:: timebin

   | Bin width for time averaging.

.. _timespan:

   .. rubric:: timespan

   | Span the timebin across scan, state or both.

.. _maxuvwdistance:

   .. rubric:: maxuvwdistance

   | Maximum separation of start-to-end baselines that can be included in an average. (meters)

.. _docallib:

   .. rubric:: docallib

   | Enable on-the-fly (OTF) calibration as in task applycal

.. _callib:

   .. rubric:: callib

   | Path to calibration library file

.. _douvcontsub:

   .. rubric:: douvcontsub

   | Enable continuum subtraction as in task uvcontsub

.. _fitspw:

   .. rubric:: fitspw

   | Spectral window:channel selection for fitting the continuum

.. _fitorder:

   .. rubric:: fitorder

   | Polynomial order for the fits

.. _want_cont:

   .. rubric:: want_cont

   | Produce continuum estimate instead of continuum subtracted data

.. _denoising_lib:

   .. rubric:: denoising_lib

   | Use new denoising library (based on GSL) instead of casacore fitting routines

.. _nthreads:

   .. rubric:: nthreads

   | Number of OMP threads to use (currently maximum limited by number of polarizations)

.. _niter:

   .. rubric:: niter

   | Number of iterations for re-weighted linear fit

.. _disableparallel:

   .. rubric:: disableparallel

   | Hidden parameter for internal use only. Do not change it!

.. _ddistart:

   .. rubric:: ddistart

   | Hidden parameter for internal use only. Do not change it!

.. _taql:

   .. rubric:: taql

   | Table query for nested selections

.. _monolithic_processing:

   .. rubric:: monolithic_processing

   | Hidden parameter for internal use only. Do not change it!

.. _reindex:

   .. rubric:: reindex

   | Hidden parameter for use in the pipeline context only


    """
    pass
