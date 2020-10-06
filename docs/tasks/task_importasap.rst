

.. _Description:

Description
   

.. _Examples:

Examples
   task examples
   
   To convert an ASAP (scantable) based format file into
   MeasurementSet format:
   
   ::
   
      importasap(infile='mydata.asap',
          outputvis='mydata.ms',
          flagbackup=True,
          overwrite=False,
          parallel=False)
   
   By default, importasap preserves flags, will not overwrite any
   existing files with the output, and will not engage parallel
   processing in the conversion (which would otherwise make the
   conversion faster).
   

.. _Development:

Development
   task developer
   
   --CASA Developer--
   
   