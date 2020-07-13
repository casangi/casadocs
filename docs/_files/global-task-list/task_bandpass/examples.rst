Examples
========

.. container:: documentDescription description

   task bandpass examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      To solve for a B-bandpass using a single short scan on the
      calibrator (with no prior gain calibration available):

      .. container:: casa-input-box

         | bandpass(vis = 'n5921.ms',
         |          caltable='n5921.bcal',
         |          gaintable='',                   # No gain tables yet
         |          gainfield='',
         |          interp='',
         |          field='0',                      # Calibrator
           1331+305 = 3C286 (FIELD_ID 0)
         |          spw='',                         # all channels
         |          selectdata=False,               # No other selection
         |          bandtype='B',                   # standard
           time-binned B (rather than BPOLY)
         |          solint='inf',                   # set solution
           interval arbitrarily long
         |          refant='15')                    # ref antenna 15
           (=VLA:N2) (ID 14)

      On the other hand, we might have a number of scans on the bandpass
      calibrator spread over time, but we want a single bandpass
      solution. In this case, we could solve for and then pre-apply an
      initial gain calibration, and let the bandpass solution cross
      scans:

      .. container:: casa-input-box

         | bandpass(vis='n5921.ms',
         |          caltable='n5921.bcal',
         |          field='0',                      # Calibrator
           1331+305 = 3C286 (FIELD_ID 0)
         |          spw='',                         # all channels
         |          selectdata=False,               # No other selection
         |          bandtype='B',                   # standard
           time-binned B (rather than BPOLY)
         |          solint='inf',                   # set solution
           interval arbitrarily long
         |          combine='scan',                 # Solution crosses
           scans(ID 14)
         |          refant='15',                    # ref antenna 15
           (=VLA:N2)
         |          gaintable='n5921.init.gcal',    # Our previously
           determined G table
         |          gainfield='0',
         |          interp='linear')                # Do linear
           interpolation

      To solve for a single bandpass from two spectral windows (0 and 1)
      that is intended for a third (2), we add 'spw' to combine (also
      using a prior gain solution):

      .. container:: casa-input-box

         | bandpass(vis='n5921.ms',
         |          caltable='n5921.bcal2',
         |          field='0',                      # Calibrator
           1331+305 = 3C286 (FIELD_ID 0)
         |          spw='0,1',                      # all channels in
           spws 0 and 1
         |          selectdata=False,               # No other selection
         |          bandtype='B',                   # standard
           time-binned B (rather than BPOLY)
         |          solint='inf',                   # set solution
           interval arbitrarily long
         |          combine='scan,spw',             # Combine scans and
           spws into a single solution
         |          refant='15',                    # ref antenna 15
           (=VLA:N2)
         |          gaintable='n5921.init.gcal',    # Our previously
           determined G table
         |          gainfield='0',
         |          interp='linear')                # Do linear
           interpolation on gaintable

      The resulting bandpass table will have average channels labeled
      with the average frequencies of the input spectral windows
      channels.  Applying this solution will require use of relative
      frequency interpolation.   See
      `here <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration/solving-for-calibration>`__,
      for more information.

       

      To solve for a BPOLY (5th order in amplitude, 7th order in phase),
      using data from field 2, with prior **gaincal** corrections
      pre-applied:

      .. container:: casa-input-box

         | bandpass(vis='data.ms',          # input data set
         |          caltable='cal.BPOLY',   #
         |          spw='0:2~56',           # Use channels 3-57 (avoid
           end channels)
         |          field='0',              # Select bandpass calibrator
           (field 0)
         |          bandtype='BPOLY',       # Select bandpass
           polynomials
         |          degamp=5,               #   5th order amp
         |          degphase=7,             #   7th order phase
         |          gaintable='cal.G',      # Pre-apply gain solutions
           derived previously
         |          refant='14')            #   

       

.. container:: section
   :name: viewlet-below-content-body
