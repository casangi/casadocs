

.. _Description:

Description
   

.. _Examples:

Examples
   task examples
   
   Plot antenna positions and make a plot in a ps-file:
   
   ::
   
      | # In CASA
      | plotants(vis='ngc5921.ms', figfile='ngc5921ants.ps')
   
   Plot logarithmic positions of antennas in main table, labeled with
   antenna ID:
   
   ::
   
      plotants(vis='ngc5921.ms', antindex=True, logpos=True,
      checkbaselines=True)
   
   Plot antenna positions but exclude antennas 1, 2, 3, 5, and 7:
   
   ::
   
      plotants(vis='ngc5921.ms', exclude='1~3,5,7')
   

.. _Development:

Development
   task developer
   
   --CASA Developer--
   
   