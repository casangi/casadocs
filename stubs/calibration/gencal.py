#
# stub function definition file for docstring parsing
#

def gencal(vis, caltable='', caltype='', infile='', spw='', antenna='', pol='', parameter=[''], uniform=True):
    r"""
Specify Calibration Values of Various Types

Parameters
   - vis_ (string) - Name of input visibility file
   - caltable_ (string='') - Name of input calibration table
   - caltype_ (string='') - The calibration type: (amp, ph, sbd, mbd, antpos, antposvla, tsys, evlagain, opac, gc, gceff, eff, tecim)

      .. raw:: html

         <details><summary><i> caltype = tecim </i></summary>

      - infile_ (string='') - Input ancilliary file

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> caltype = gc </i></summary>

      - infile_ (string='') - Input ancilliary file

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> caltype = gceff </i></summary>

      - infile_ (string='') - Input ancilliary file

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> caltype = tsys </i></summary>

      - uniform_ (bool=True) - Assume uniform calibration values across the array

      .. raw:: html

         </details>
   - spw_ (string='') - Select spectral window/channels
   - antenna_ (string='') - Select data based on antenna/baseline
   - pol_ (string='') - Calibration polarizations(s) selection
   - parameter_ (doubleArray=['']) - The calibration values


Description
   The **gencal** task provides a means of specifying antenna-based
   calibration values manually. The values are put in designated
   tables and applied to the data using other tasks (**applycal**,
   **gaincal**, **bandpass**, etc.). Several specialized calibrations
   are also generated with **gencal**.

   

   .. rubric:: Calibration types: *caltype*
      

   The **gencal** task supports many different calibration types via
   the *caltype* parameter. These are listed here in two groups. Many
   of these options are part of `Preparing for
   Calibration <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration/preparing-for-calibration>`__
   and more information about how they work can be found in that
   section.

   .. rubric:: Manual *caltype* s
      

   The following enable directly specifying calibration factors for
   each specified *pol*, *antenna*, *spw*. Except where noted, each
   expects one real *parameter* value per specified *pol*, *antenna*,
   and *spw*.

   -  'amp'= amplitude correction
   -  'ph' = phase correction
   -  'sbd'= single-band delay (phase-frequency slope for each spw)
   -  'mbd'= multi-band delay (phase-frequency slope over all spw)
   -  'opac' = Tropospheric opacity (1 real parameter [in nepers] per
      antenna, spw)
   -  'antpos' = ITRF antenna position corrections (3 real parameters
      [in m] for each antenna; see below)
   -  'antposvla' = VLA-centric antenna position corrections (3 real
      parameters [in m] for each antenna; see below)

   .. rubric:: Specialized *caltype* s
      

   The following *caltype* options automatically generate caltables
   from ancilliary information found in the MS or elsewhere. The
   *pol, antenna, spw,* and *parameter* options are ignored for
   these.

   -  'tsys' = Tsys from the MS.SYSCAL table (ALMA)
   -  'swpow' = VLA switched-power gains from MS.SYSPOWER, CALDEVICE
   -  'rq' = VLA requantizer gains \_only\_
   -  'swp/rq' = VLA switched-power gains divided by requantizer gain
   -  'gc' = Gain curve (zenith-angle-dependent gain) (VLA only;
      auto-lookup)
   -  'eff' = Antenna efficiency (sqrt(K/Jy)) (VLA only)
   -  'gceff' = Gain curve and efficiency (VLA only)
   -  'tecim' = Time-dependent TEC image specified in *infile*
      subparameter
   -  'antpos' = For VLA datasets, automatic lookup of antenna
      position corrections if *antenna=''*

   

   .. rubric:: Specifying calibration values: *pol, antenna, spw,
      parameter*
      

   Generic calibration values for the "manual *caltype* s" listed
   above should be specified in the *parameter* argument as a list.
   The length of the list must correspond to the net length of the
   specific polarizations, antennas, and spws specified in the *pol*,
   *antenna*, and *spw* selection arguments. The values specified in
   *parameter* will be duplicated over all members of any selection
   axis that is not explicitly specified (*pol* ='', *spw* =''
   and/or *antenna* ='') E.g., if
   *pol* = *antenna* = *spw* ='', it only makes sense to specify
   a single *parameter* value (or three, for *antpos* and
   *antposvla*), and this will be duplicated for all pols, antennas,
   and spws. If multiple *parameter* values are specified, at least
   one of *pol*, *spw*, or *antenna* must be non-trivial, and the
   number of values in *parameter* must be consistent with the range
   of specified *pol*, *spw*, and/or *antenna*. E.g., if only a
   non-trivial *spw* selection is specified, then the *parameter*
   value list should match the number of spws specified, and these
   values will be duplicated for all polarizations and antennas. If
   more than one of *pol*, *spw*, and *antenna* is non-trivially
   specified, the number of *parameter* values specified should
   match the product of the number specified selection elements. The
   *parameter* values should be sorted by *pol* (fastest), *antenna*,
   and *spw* (slowest). Un-specified elements on non-trivially
   specified axes will be filled with nominal values (i.e., it is not
   necessary to exhaustively specify all elements on any axis or use
   nominal *parameter* values explicitly). **Please consult the
   examples for additional guidance.** There is currently no support
   for time-dependent calibration specfication; in all cases, the
   specified *parameter* values will be assumed constant in time
   (though their impact on the data may be time-dependent, depending
   on the *caltype*).

   The same *caltable* can be specified for multiple runs of
   **gencal**, in which case the specified *parameter* values will be
   incorporated cumulatively. E.g., amplitude-like values
   (*caltype='amp'*) multiply and phase-like values ('ph',
   'sbd','mbd','antpos') add. Also, 'amp' and 'ph' calibrations can
   be incorporated into the same *caltable* (in separate cumulative
   runs), but each of the other types require their own unique
   *caltable*. A mechanism for specifying manual corrections via a
   text file will be provided in the future.

   The calibration tables generated by **gencal** can be applied to
   the data in all other tasks that accept specified calibration for
   (pre-)application, e.g.,
   `applycal. <https://casa.nrao.edu/casadocs-devel/stable/task_applycal>`__
   **gaincal**, **bandpass**, etc.

   Consult the Examples for more information on the many *caltype*
   options in **gencal**.

   .. rubric:: Notes on specific *caltype* s
      

   -  'antpos' For antenna position corrections
      (*caltype='antpos'*), the antenna position offsets are
      specified in the ITRF frame. For the Karl G. Jansky VLA,
      automated lookup of the antenna position corrections is enabled
      when antenna is unspecified (*antenna=''*) for this *caltype*.
      Note that this requires internet connection to access the VLA
      antenna position correction site. More information can be found
      `here <https://casa.nrao.edu/casadocs-devel/stable/external-data/vla-baseline-corrections>`__.
   -  'antposvla' For (old) pre-upgrade VLA position corrections,
      specify the values in the VLA-centric frame and **gencal** will
      rotate them to ITRF before storing them in the output caltable.
      More information can be found
      `here <https://casa.nrao.edu/casadocs-devel/stable/external-data/vla-baseline-corrections>`__.
   -  VLA switched power calibration is supported in three modes:
      'swpow' (formerly 'evlagain', a syntax which has been
      deprecated) yields the formal VLA switched power calibration
      which describes voltage gain as sqrt(Pdif/Tcal) (used to
      correct the visibility data) and Tsys as Psum*Tcal/Pdif/2 (used
      to correct the weights). 'swpow' implicitly includes any
      requantizer gain scale and adjustments. 'rq' yields only the
      requantizer voltage gains (Tsys is set to 1.0 to avoid weight
      adjustments). 'swp/rq' yields the ordinary switched power
      voltage gains divided by the requantizer voltage gain (Tsys is
      calculated normally). The 'rq' and 'swp/rq' modes are are
      mainly intended for testing and evaluating the VLA switched
      power systems.
   -  For *caltype='opac'*, only constant (in time) opacities are
      supported via **gencal**. 
   -  For gaincurve and efficiency (*caltype='gc'*, *'gceff'*, or
      *'eff'*), observatory-provided factors are determined per spw
      according to the observing frequencies. The parameter argument
      is ignored. These *caltype* s are currently only supported for
      VLA (including pre-upgrade VLA) processing. (Appropriate
      factors for ALMA are TBD.)


.. _vis:

vis (string)
   | Name of input visibility file
   |                      Default: none
   | 
   |                         Example: vis='ngc5921.ms'

.. _caltable:

caltable (string='')
   | Name of input calibration table
   |                      Default: none
   | 
   |                      If a calibration table does not exist, it will be
   |                      created. Specifying an existing table will result
   |                      in the parameters being applied
   |                      cumulatively. Only a single time-stamp for all
   |                      calibrations are supported, currently.  Do not
   |                      use a caltable created by gaincal, bandpass,
   |                      etc. 
   | 
   |                         Example: caltable='test.G'

.. _caltype:

caltype (string='')
   | The calibration parameter type being specified
   |                      Default: none
   |                      Options: 'amp', 'ph', 'sbd', 'mbd', 'antpos',
   |                      'antposvla', 'tsys', 'evlagain', 'opac', 'gc',
   |                      'gceff', 'eff', 'tecim'
   | 
   |                      * 'amp' = gain (G) amplitude (1 real parameter
   |                        per pol, antenna, spw)
   |                      * 'ph'  = gain (G) phase (deg) (1 real parameter
   |                        per pol, antenna, spw)
   |                      * 'sbd' = single-band delays (nsec) (1 real
   |                        parameter per pol, antenna, spw)
   |                      * 'mbd' = multi-band delay (nsec) (1 real
   |                        parameter per pol, antenna, spw)
   |                      * 'antpos' = antenna position corrections (m) (3
   |                        real ITRF offset parameters per antenna; spw,
   |                        pol selection will be ignored)
   |                        With antenna='', this triggers an automated
   |                        lookup of antenna positions for EVLA and ALMA.
   |                      * 'antposvla' = antenna position corrections (m)
   |                        specified in the old VLA-centric coordinate
   |                        system
   |                      * 'tsys' = Tsys from the SYSCAL table (ALMA)
   |                      * 'evlagain' = EVLA switched-power gains
   |                        (experimental)
   |                      * 'opac' = Tropospheric opacity (1 real parameter
   |                        per antenna, spw)
   |                      * 'gc' = Antenna zenith-angle dependent gain
   |                        curve (auto-lookup)
   |                      * 'gceff' = Gain curve and efficiency
   |                        (auto-lookup)
   |                      * 'eff' = Antenna efficiency (auto-lookup)
   | 
   |                         Example: caltype='ph'

.. _infile:

infile (string='')
   | Input ancilliary file
   |                     Subparameter of caltype='gc|gceff|tecim'
   |                     Default: none

.. _spw:

spw (string='')
   | Select spectral window/channels
   |                      Default: '' (all spectral windows and channels)
   |            
   |                         Examples:
   |                         spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
   |                         spw='<2';  spectral windows less than 2 (i.e. 0,1)
   |                         spw='0:5~61'; spw 0, channels 5 to 61
   |                         spw='0,10,3:3~45'; spw 0,10 all channels, spw
   |                         3 - chans 3 to 45.
   |                         spw='0~2:2~6'; spw 0,1,2 with channels 2
   |                         through 6 in each.
   |                         spw = '*:3~64'  channels 3 through 64 for all sp id's
   |                         spw = ' :3~64' will NOT work.

.. _antenna:

antenna (string='')
   | Select data based on antenna/baseline
   |                      Subparameter of selectdata=True
   |                      Default: '' (all)
   | 
   |                      If antenna string is a non-negative integer, it
   |                      is assumed an antenna index, otherwise, it is
   |                      assumed as an antenna name
   |   
   |                          Examples: 
   |                          antenna='5&6'; baseline between antenna
   |                          index 5 and index 6.
   |                          antenna='VA05&VA06'; baseline between VLA
   |                          antenna 5 and 6.
   |                          antenna='5&6;7&8'; baselines with
   |                          indices 5-6 and 7-8
   |                          antenna='5'; all baselines with antenna index
   |                          5
   |                          antenna='05'; all baselines with antenna
   |                          number 05 (VLA old name)
   |                          antenna='5,6,10'; all baselines with antennas
   |                          5,6,10 index numbers

.. _pol:

pol (string='')
   | Polarization selection for specified parameters
   |                      Default: pol='' (specified parameters apply to
   |                      all polarizations)
   | 
   |                         Example: pol='R' (specified parameters to
   |                         apply to R only)

.. _parameter:

parameter (doubleArray=[''])
   | The calibration values
   | 
   |                      The calibration parameters, specified as a list,
   |                      to store in the caltable for the spw, antenna,
   |                      and pol selection.  The required length of the
   |                      list is determined by the caltype and the spw,
   |                      antenna, pol selection.  One "set" of parameters
   |                      (e.g., one value for 'amp', 'ph', etc., three
   |                      values for 'antpos') specified the same value for
   |                      all indicated spw, antenna, and pol.
   |                      OR, 
   |                      When specifying a long list of calibration
   |                      parameter values, these should be ordered first
   |                      (fastest) by pol (if pol!=''), then by antenna
   |                      (if antenna!=''), and finally (sloweset) by spw
   |                      (if spw!='').  Unspecified selection axes must
   |                      not be enumerated in the parameter list

.. _uniform:

uniform (bool=True)
   | Assume uniform calibration values across the array
   |                     Subparameter of caltype='tsys'
   |                      Default: True
   |                      Options: True|False


    """
    pass
