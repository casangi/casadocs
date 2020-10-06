

.. _Description:

Description
   

.. _Examples:

Examples
   task fringefit examples
   
   Single-band delay: calibration of delay only for a single scan on
   a bright calibrator:
   
   ::
   
      | fringefit(vis='data.ms',
      |           caltable='data.sbd',                  # write
        solutions to this table on disk
      |           scan='30',                            # use only
        scan 30
      |           solint='inf',                         # use all
        timestamps in the scan
      |           refant='EF',                          # a big
        antenna does well as reference antenna
      |           minsnr=50,                            # empirically
        proven to be a good value is anything over 25
      |           zerorates=True,                       # for
        instrumental delay rates should not be used
      |           gaintable=['data.tsys','data.gc'],    # apply the
        amplitude calibration on the fly
      |           parang=True)                          # always True
        for VLBI
   
   Multi-band delay: calibration of time-dependent delay and
   delay-rate for a phase reference source, relative to single-band
   delay solution from above:
   
   ::
   
      | fringefit(vis='data.ms',
      |           caltable='data.mbd',                  # write
        solutions to this table disk
      |           solint='60',                          # anything
        shorter than the scan length will give more than 1 solution
      |           combine='spw',                        # combine
        spectral windows for this step, gives only a solution for
        spw0
      |           field='1',                            # select the
        field that is your phase reference calibrator
      |           refant='EF',                          # pick a big
        antenna or one close to the geometric center of the array
      |           minsnr=50,                            # this seems
        to be a sensible value
      |           gaintable=['data.tys', 'data.gc', 'data.sbd'],   #
        apply amplitude calibration and single band delay on the fly
      |           parang=True)                          # always set
        to True for VLBI
   
   The calibration table data.mbd will contain phase, delay, and rate
   solutions per antenna, per polarization and per solution interval.
   For data with multiple spectral windows the solutions will be
   assigned to spectral window 0 in the output cal table. In the
   **applycal** step, the parameter *spwmap* needs to be set to apply
   the solutions to all spectral windows. For example, in a dataset
   with 8 spectral windows: *spwmap=[8*[0]]*. Since the **applycal**
   step will include multiple calibration tables, this setting needs
   to correspond to the data.mbd table in the *gaintable* parameter:
   
   ::
   
      | applycal(vis='data.ms',
      |          field='0,1',                           # now select
        the phase calibrator AND the target source
      |          gaintable=['data.tsys', 'data.gc','data.sbd',
        'data.mbd'],    # include all the calibration tables
      |          interp=[],spwmap=[[], [], [],
        8*[0]],                         # map the spectral windows
        accordingly
      |          parang=True)                           # for VLBI
        this should always be True
   
   In cases where it is necessary to constrain the search for group
   delay and fringe rates at the FFT stage, the parameters
   *delaywindow* and *ratewindow* can be used:
   
   ::
   
      | fringefit(vis='data.ms',
      |           caltable='data.mbd',            # write solutions
        to this table disk
      |           solint='60',                    # anything shorter
        than the scan length will give more than 1 solution
      |           combine='spw',                  # combine spectral
        windows for this step, gives only a solution for spw0
      |           field='1',                      # select the field
        that is your phase reference calibrator
      |           refant='EF',                    # pick a big
        antenna or one close to the geometric center of the array
      |           minsnr=5,                       # we're looking for
        weak detections, but we have a good a priori idea of where
        they are to steer the FFT search
      |           delaywindow = [0,10],           # FFT delay search
        range of 0 to 10 nanoseconds
      |           ratewindow = [-5e-9,5e-9],      # FFT rate search
        range of -5 to 5 nanoseconds per second
      |           gaintable=['data.tys', 'data.gc', 'data.sbd'],   #
        apply amplitude calibration and single band delay on the fly
      |           parang=True)                    # always set to
        True for VLBI
   

.. _Development:

Development
   task developer
   
   --CASA Developer--
   
   