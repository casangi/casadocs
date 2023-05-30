

.. _Description:

Description
   Allows users to manually set or append to the intents in the MS. Several selection parameters can
    be used to target which intents to change including scan, field, and ObsId. Users will be able to
    either overwrite the existing intents within the table, or append to the existing ones.
   
   .. warning:: **WARNING**: This task will allow the user to specify any string to add to the
    intents without enforcing any specific list of allowed intents.

   
    .. rubric:: Parameters
   
   *vis*
   Specify the name of the measurment set as a string
   
   *intent*
   Specify the name(s) of intents to replace or append to the selected data
  
   *mode*
   mode 'set' will replace the add a new intent selection and replace the selected data with the provided intents value
   mode 'append' will add the new intent selection to the existing selected data
   
   *field*
    Select on MS fields. The default selection of '' is all fields
   
   *scan*
    Select on MS scans. The default selection of '' is all scans
   
   *obsid*
    Select on observation ids. The default selection of '' is all obs ids

.. _Examples:

Examples
   This will replace the intents of the ms where scan is between 0 and 3, field is 0, and obsid with the new intent of 'AMPLI':
   
   ::
   
      defintent(vis='gaincaltest2.ms', intent='AMPLI', mode='set',
       scan='0~3', field='0', obsid='0')

.. _Development:

Development
   No additional development details


