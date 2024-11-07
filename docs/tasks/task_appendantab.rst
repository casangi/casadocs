.. _Description:

Allow users to append information available in antab files directly to a ms. 
Use a ms generated from importfitsidi and then use this task to append tsys and gain curve information
to the ms.


.. warning:: **WARNING**: The parser for the antab files can be quite strict which may effect some instruments disproportionately. If you had success with the vlbi tools version this parser is the same. This task also MUST be used with importfitsidi filled data. It is also recommended that, if using an ms generated from multiple fitsidi files, constobsid should be set to True if the resulting ms will be used in conjunction with this task.



.. rubric:: Parameters

*vis*

   Specify the name of the MS created from a fits file as a string

*outvis*

   Specify the name of the output vis that will have the antab information appended to it

*antab*
    Specify the antab file to be appended to the vis as a string

*overwrite*

   If True the outvis will overwrite a file that exists with the same name

*append_tsys*

    Using the tsys information available in the antab file append to the SYSCAL subtable when this is True

*append_gc*

    Using the gain curve information available in the antab file append to the GAIN_CURVE subtable when this is True


.. _Examples:

Examples
   This example will take a ms and output one with the name "appended_data.ms" by appending the tys and gc infromation from an antab file:

   ::
   
      appendantab(vis='imported_fits.ms', outvis='appended_data.ms, overwrite=False,
       append_tsys=True, append_gc=True)

.. _Development:

Development
   No additional development details
