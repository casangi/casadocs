

.. _Description:

Description
   

.. _Examples:

Examples
   task examples
   
   .. rubric:: Split with field selections
      
   
   Create a new MS with field ID 3 and all field names starting with
   4C.
   
   ::
   
      split(vis='example.ms',outputvis='test.ms',field='3,4C*')
   
   .. rubric:: Split with spectral window and channel selections
      
   
   Split channels 3 through 64 for all SPW IDs.
   
   ::
   
      split(vis='example.ms', outputvis='test.ms', spw='*:3~64')
   
   Split with multiple channel selection. The following example will
   select channels 4 through 13 and 10 through 59 inclusive from spw
   8.
   
   ::
   
      split('example.ms',outputvis='test.ms',spw='8:4~13;10~59')
   
   Split with multiple spws and channel selections. The following
   example will select all channels from spw 4, channels 4 through 59
   inclusive from spw 7. It will also select channels 4 through 13
   and 10 through 59 from spw 8. The output MS will have three
   spectral windows, reindexed from 0 through 2.
   
   ::
   
      split('example.ms',outputvis='test.ms',spw='4,7:4~59,8:4~13;10~59')
   
   On the other hand, the following example will select only channels
   4 through 59 from all three spectral windows 4, 5 and 6.
   
   ::
   
      split('example.ms',outputvis='test.ms',spw='4~6:4~59')
   
    
   
   .. rubric:: Split with antenna selections
      
   
   Split using antenna selection. Non-negative integers are assumed
   to be antenna indices, and anything else is taken as an antenna
   name. The following example will split the baseline between
   antennas VA05 and VA06.
   
   ::
   
      split(vis='example.ms', outputvis='test.ms',
      antenna='VA05&VA06')
   
   .. rubric:: Channel Averaging
      
   
   Average 2 channels of first selected SPW and 3 channels in second
   SPW.
   
   ::
   
      split(vis='example.ms', outputvis='test.ms',spw='0,1',
      width=[2,3])
   
   .. rubric:: Time Averaging
      
   
   Average in time across scans. The following example can be useful
   when the scan number goes up with each integration as in many WSRT
   MSs.
   
   ::
   
      split(vis='example.ms', outputvis='test.ms',timebin='20s',
      combine='scan')
   

.. _Development:

Development
   