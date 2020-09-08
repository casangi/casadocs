#
# stub function definition file for docstring parsing
#

def polcal(vis, caltable='', field='', spw='', intent='', selectdata=True, timerange='', uvrange='', antenna='', scan='', observation='', msselect='', solint='inf', combine='obs,scan', preavg=300.0, refant='', minblperant=4, minsnr=3.0, poltype='D+QU', smodel=[''], append=False, docallib=False, callib='', gaintable=[''], gainfield=[''], interp=[''], spwmap=['']):
    r"""
Determine instrumental polarization calibrations

Parameters
   - vis_ (string) - Name of input visibility file
   - caltable_ (string='') - Name of output gain calibration table
   - field_ (string='') - Select field using field id(s) or field name(s)
   - spw_ (string='') - Select spectral window/channels
   - intent_ (string='') - Select observing intent
   - selectdata_ (bool=True) - Other data selection parameters

      .. raw:: html

         <details><summary><i> selectdata = True </i></summary>

      - timerange_ (string='') - Select data based on time range
      - uvrange_ (variant='') - Select data within uvrange (default units meters)
      - antenna_ (string='') - Select data based on antenna/baseline
      - scan_ (string='') - Scan number range
      - observation_ ({string, int}='') - Select by observation ID(s)
      - msselect_ (string='') - Optional complex data selection (ignore for now)

      .. raw:: html

         </details>
   - solint_ (variant='inf') - Solution interval
   - combine_ (string='obs,scan') - Data axes which to combine for solve (obs, scan, spw, and/or field)
   - preavg_ (double=300.0) - Pre-averaging interval (sec)
   - refant_ (string='') - Reference antenna name(s)
   - minblperant_ (int=4) - Minimum baselines _per antenna_ required for solve
   - minsnr_ (double=3.0) - Reject solutions below this SNR
   - poltype_ (string='D+QU') - Type of instrumental polarization solution (see help)
   - smodel_ (doubleArray=['']) - Point source Stokes parameters for source model.
   - append_ (bool=False) - Append solutions to the (existing) table
   - docallib_ (bool=False) - Use callib or traditional cal apply parameters

      .. raw:: html

         <details><summary><i> docallib = False </i></summary>

      - gaintable_ (stringArray=['']) - Gain calibration table(s) to apply
      - gainfield_ (stringArray=['']) - Select a subset of calibrators from gaintable(s)
      - interp_ (stringArray=['']) - Interpolation mode (in time) to use for each gaintable
      - spwmap_ (intArray=['']) - Spectral window mappings to form for gaintable(s)

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> docallib = True </i></summary>

      - callib_ (string='') - Cal Library filename

      .. raw:: html

         </details>


Description
   The **polcal** task supports solving for systematic calibration
   relating to the linear and circular polarization sensitivity of
   synthesis observations, namely, the instrumental polarization and
   cross-hand phase.

   The heuristics of polarization calibration are described in more
   detail
   `here <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration/instrumental-polarization-calibration>`__.

   .. rubric:: Common calibration solve parameters
      

   See `"Solving for
   Calibration" <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration/solving-for-calibration>`__
   for more information on the task parameters **polcal** shares with
   all solving tasks, including data selection, general solving
   properties and arranging prior calibration. Below we describe
   parameters unique to **polcal**, and those common parameters with
   unique properties. Since parallactic angle is usually an important
   part of instrumental polarization calibration, the **polcal** task
   will implicitly turn *parang=True*, and it is not a user-setable
   parameter.

   .. rubric:: Polarization Calibration type: *poltype*
      

   The *poltype* parameter supports a range of modes to accommodate a
   variety of situations. Except where noted, these options are not
   basis-specific.

   -  *'Df' -* Solve for instrumental polarization (leakage D-terms),
      using the transform of a specified IQU model; requires no
      parallactic angle coverage, but if the source polarization is
      non-zero, the gain calibration must have the correct R-L phase
      registration. (Note: this is unlikely, so just use *'D+X'* to
      let the cross-hand phase registration float). This will produce
      a calibration table of type D.
   -  *'Df+X'* - For circular basis only, solve for instrumental
      polarization D-terms and the cross-hand phase correction, using
      the transform of an IQU model; this mode requires at least 2
      distinct parallactic angles to separate the net instrumental
      polarization and the cross-hand phase (same as position angle
      for circulars). This will produce a calibration table of type
      D. Please note: no table of type X will be produced, so you
      must follow this by a run of **polcal** with *poltype='Xf'*
      (see below)
   -  *'Df+QU'* - For circular basis only, solve for instrumental
      polarization and source Q+iU; requires at least 3 distinct
      parallactic angles to separate the net instrumental
      polarization from the *apparent* source Q and U. This will
      produce a calibration table of type D.
   -  'Xf' - Solve only for the cross-hand phase (same as position
      angle for the circular basis); best to use this after getting
      the D-terms from one of the above modes. Requires the
      observation of a calibrator with known Q+iU (or at least known
      U/Q). This will produce a calibration table of type X.
   -  '*Dflls'* - A specialized mode which explicitly solves a
      linearized form of the cross-hand data for the D-terms. *
      *
   -  '*Xfparang+QU*' - For observations of a distinctly linearly
      polarized calibrator over a significant parallactic angle
      range, solve for the apparent cross-hand phase spectrum
      (channelized) and integrated (per-spw) fractional linear
      polarization, Q and U. This mode is intended for use prior to
      solving for the instrumental polarization (e.g., Df) and works
      for either the linear or circular basis, as long as there is
      adequate parallactic angle to isolate the polarized calibrator
      signal and cross-hand phase in the visibility cross-hands from
      any instrumental polarization contribution. A significantly
      polarized (> few %) calibrator should be used, and a non-zero
      polarized model prior should be specified in the smodel
      parameter. For the linear basis, the prior model (if reasonably
      accurate) will be used to correctly resolve the 180 degree
      ambiguity in the cross-hand phase and Q,U sign. For the
      circular basis, an accurate prior polarized model will achieve
      a good nominal position angle calibration; if the polarization
      model is specified without accurate prior position angle
      knowledge, the resulting Q,U estimate will be relative, and a
      traditional position angle calibration will be necessary (after
      solving for the instrumental polarization).
   -  *'PosAng'* - Solve directly for the absolute position angle
      offset spectrum, for either the linear or circular basis. The
      resulting calibration table stores the position angle offset
      directly, as an angle in radians. Note that for the circular
      basis (only!), this is interchangeable with the position angle
      calibration traditionally provided by general cross-hand phase
      calibration (e.g., poltype='Xf', for which position angle is
      0.5 times the cross-hand phase). For the linear basis, this is
      the only way to directly calibrate the absolute position angle.

   .. warning:: 'Xfparang+QU' and 'PosAng' are considered "experimental" in
      CASA 5.5. As more experience is gained in their use,
      additional advice will be added here.

   In each of these options, the *'f'* causes channelized solutions
   to be obtained, which is usually desirable for modern instruments.
   Omitting the *'f'* will generate strictly unchannelized solutions.




Details
   Explanation of each parameter

.. _vis:

   .. rubric:: vis

   | Name of input visibility file

.. _caltable:

   .. rubric:: caltable

   | Name of output gain calibration table

.. _field:

   .. rubric:: field

   | Select field using field id(s) or field name(s)

.. _spw:

   .. rubric:: spw

   | Select spectral window/channels

.. _intent:

   .. rubric:: intent

   | Select observing intent

.. _selectdata:

   .. rubric:: selectdata

   | Other data selection parameters

.. _timerange:

   .. rubric:: timerange

   | Select data based on time range

.. _uvrange:

   .. rubric:: uvrange

   | Select data within uvrange (default units meters)

.. _antenna:

   .. rubric:: antenna

   | Select data based on antenna/baseline

.. _scan:

   .. rubric:: scan

   | Scan number range

.. _observation:

   .. rubric:: observation

   | Select by observation ID(s)

.. _msselect:

   .. rubric:: msselect

   | Optional complex data selection (ignore for now)

.. _solint:

   .. rubric:: solint

   | Solution interval

.. _combine:

   .. rubric:: combine

   | Data axes which to combine for solve (obs, scan, spw, and/or field)

.. _preavg:

   .. rubric:: preavg

   | Pre-averaging interval (sec)

.. _refant:

   .. rubric:: refant

   | Reference antenna name(s)

.. _minblperant:

   .. rubric:: minblperant

   | Minimum baselines _per antenna_ required for solve

.. _minsnr:

   .. rubric:: minsnr

   | Reject solutions below this SNR

.. _poltype:

   .. rubric:: poltype

   | Type of instrumental polarization solution (see help)

.. _smodel:

   .. rubric:: smodel

   | Point source Stokes parameters for source model.

.. _append:

   .. rubric:: append

   | Append solutions to the (existing) table

.. _docallib:

   .. rubric:: docallib

   | Use callib or traditional cal apply parameters

.. _callib:

   .. rubric:: callib

   | Cal Library filename

.. _gaintable:

   .. rubric:: gaintable

   | Gain calibration table(s) to apply

.. _gainfield:

   .. rubric:: gainfield

   | Select a subset of calibrators from gaintable(s)

.. _interp:

   .. rubric:: interp

   | Interpolation mode (in time) to use for each gaintable

.. _spwmap:

   .. rubric:: spwmap

   | Spectral window mappings to form for gaintable(s)
   |                      Only used if callib=False
   |                      default: [] (apply solutions from each calibration spw to
   |                      the same MS spw only)
   |                      Any available calibration spw can be mechanically mapped to any 
   |                       MS spw. 
   |                      Examples:
   |                         spwmap=[0,0,1,1] means apply calibration 
   |                           from cal spw = 0 to MS spw 0,1 and cal spw 1 to MS spws 2,3.
   |                         spwmap=[[0,0,1,1],[0,1,0,1]] (use a list of lists for multiple
   |                           gaintables)


    """
    pass
