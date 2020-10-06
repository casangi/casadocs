

.. _Description:

Description
   

.. _Examples:

Examples
   task examples
   
   To apply a prioritized list of reference antennas using
   *refantmode='flex'*:
   
   ::
   
      | rerefant(vis='n5921.ms',
      |          tablein='n5921.gcal',
      |          caltable='n5921_ea03ish.gcal',  # Output caltable
      |          refant='ea03,ea05,ea23,ea01',   # prioritized list
        of reference antennas
      |          refantmode='flex')              # flexible use of
        alternates
   
   To strictly apply a preferred reference antenna:
   
   ::
   
      | rerefant(vis='n5921.ms',
      |          tablein='n5921.gcal',
      |          caltable='n5921_ea03.gcal',     # Output caltable
      |          refant='ea03',                  # the strictly
        preferred reference antenna
      |          refantmode='strict')            # strict!
   

.. _Development:

Development
   