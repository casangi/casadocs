

.. _Description:

Description
   

.. _Examples:

Examples
   task examples
   
   Update the weights of a MS as in the **statwt** task. All channels
   in a SPW will receive equal weight:
   
   ::
   
      statwt("my.ms")
   
    
   
   Update the weights of a MS, using a calculation that disregards
   visibilities in spectral window 2 between channels 7 and 16. All
   channels in a SPW will receive equal weight, even those
   disregarded in the calculation:
   
   ::
   
      statwt("my.ms", fitspw='2:7~16’, excludechans=True)
   
    
   
   Update the weights of a MS using an algorithm robust to outliers.
   All channels in a SPW will receive equal weight:
   
   ::
   
      statwt("my.ms", statalg='chauvenet')
   
    
   
   Update the weights of a MS using time binning of 300s. All
   channels in a SPW will receive equal weight, and all times within
   a *timebin* will receive equal weight:
   
   ::
   
      statwt("my.ms", timebin="300s")
   
    
   
   Update the weights of a MS using time binning of 10 integrations.
   Each channel and integration will receive a unique weight. The
   weight calculation will consider all visibilities within the time
   bin:
   
   ::
   
      statwt("my.ms", timebin=10, slidetimebin=True, chanbin=1)
   
    
   
   Calculate, but do not update the weights of spectral window 3 of a
   MS. Return statistics which summarize the calculated weights as a
   dictionary:
   
   ::
   
      weight_stats = statwt("my.ms", preview=True, spw='3')
   

.. _Development:

Development
   