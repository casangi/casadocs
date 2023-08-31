.. _Description:

Description
   
   Allows users to manually set or append to the intents in the MS. Several selection parameters can
   be used to target which intents to change including scan, field, and ObsId. Users will be able to
   add either brand new intents, or a new intent appended to existing intent value(s).
   
.. warning:: **WARNING**: This task will allow the user to specify any string to add to the
    intents without enforcing any specific list of allowed intents.

   
.. rubric:: Parameters
   
*vis*
   
   Specify the name of the MS as a string
   
*intent*
   
   Specify the name(s) of intents to replace or append to the selected data
   
*mode*
   
   mode ‘set’ will replace the selected data with the provided intents; mode ‘append’ will add the new intent selection to the existing selected data intents
   
*outputvis*
   
    Set the name of the modified MS that will be created by the task. If outputvis is equal to vis then the provided vis will be modified and a copy will not be made.
   
*field*
    
    Select on MS fields. The default selection of '' is all fields
   
*scan*
   
    Select on MS scans. The default selection of '' is all scans
   
*obsid*
   
    Select on observation ids. The default selection of '' is all obs ids

.. _Examples:

Examples
   This will replace the intents of the MS where scan is between 0 and 3, field is 0, and obsid with the new intent of 'AMPLI'. The vis will be copied and the output with the modified intents will be called outputcopy.ms:
   
   ::
   
      defintent(vis='gaincaltest2.ms', intent='AMPLI', mode='set',
       outputvis='outputcopy.ms', scan='0~3', field='0', obsid='0')

.. _Development:

Development
   No additional development details


