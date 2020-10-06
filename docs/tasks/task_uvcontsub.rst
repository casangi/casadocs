

.. _Description:

Description
   

.. _Examples:

Examples
   task examples
   
   **Example 1: **
   
   Subtract the continuum of channels 10~100 and 300~350 in spw 0
   (assuming that the line is in channels 101~299). Note that we also
   exclude edge channels, e.g. the first 9 channels. We use a
   fitorder of 0 (default). 
   
   ::
   
      uvcontsub(vis='myMS.ms',fitspw='0:10~100;300~350')
   
    
   
   **Example 2: **
   
   subtract continuum across all spw, assuming that the line sits at
   23.694GHz with a 20 MHz width. We use fitorder 1 for the large
   frequency range.  
   
   ::
   
      uvcontsub(vis='myMS.ms', fitspw='23.684~23.704GHz',
      excludechans=True, combine='spw', fitorder=1)
   

.. _Development:

Development
   task developer
   
   --CASA Developer--
   
   