

.. _Description:

Description
   This task changes the sign of the phases in all visibility
   columns, thus creating the complex conjugate values. A complex
   number and its complex conjugate have equal real parts and
   imaginary parts that are equal in magnitude but opposite in sign.

   .. rubric:: Parameter descriptions

   *vis*
   
   Name of input visibility file. For example: *vis='filename.ms'*
   
   *spwlist*
   
   Selects spectral window(s). For example: *spw=[1,2]*. By default,
   all spws will be conjugated.
   
   *outputvis*
   
   Name of output visibility file. Default:
   'conjugatedvis_filename.ms'
   
   *overwrite*
   
   Overwrites the *outputvis* if it exists. Default=False


.. _Examples:

Examples
   Conjugate all visibilities for spectral windows 0 and 1 and store
   the modified data in a new MeasurementSet NGC253-conj.ms:
   
   ::
   
      conjugatevis(vis='NGC253.ms', spwlist=[0,1],
      outputvis='NGC253-conj.ms')


.. _Development:

Development
   No additional development details

