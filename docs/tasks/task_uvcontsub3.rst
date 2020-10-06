

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
   
      uvcontsub3(vis='myMS.ms',fitspw='0:10~100;300~350')
   

.. _Development:

Development
   task developer
   
   --CASA Developer--
   
   