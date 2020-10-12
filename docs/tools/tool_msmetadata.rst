

.. _Description:

Description
   tool msmetadata description
   
   msmetadata (msmd) is a powerful tool that allows users to directly
   access MeasurementSets. It is not generally used in the data
   reduction and is recommended for advanced users that want to
   manipulate MeasurementSet tables. The default global tool is
   named  msmd.
   
   .. rubric:: Summary of Tool Use
      
   
   The simplest and most common way to attach an msmd tool to a
   MeasurementSet is to use the  **msmd.open()** method which
   requires that you specify the name of the MeasurementSet table.
   When one has finished with the tool, the msmd.close() or
   msmd.done() method should be called to free up resources that the
   tool uses when it is attached to an MeasurementSet (MS). msmd has
   several functions, as for example: get the list of spectral
   windows, antenna numbers, band widths, field names, intents, numer
   of channels for a given spectral window, phase centers, scan
   numbers, observing time for a specific scan, and many other
   functions listed in Methods.
   
   NOTE: Any modifications to an MS while an associated msmd tool is
   open will not be reflected in the msmd tool. You must close and
   reopen the tool if you want to capture changes made to metadata of
   an MS if such a change occurs.
   

.. _Examples:

Examples
   tool msmetadata examples
   
   ::
   
      | # attach tool to an MS
      | msmd.open("3C273XC1.MS")
      | # get the number of spectral windows
      | nspw = msmd.nspw()
      | # free up resources used by the attached tool
      | msmd.done()
   
   We open the tool by querying the MS for its metadata. We then get
   the number of spectral windows in the dataset and close the tool.
   
    
   
   ::
   
      | # attach tool to an MS
      | msmd.open("3C273XC1.MS")
      | # get the diameter of the antenna named 'VB2'
      | diameter = msmd.antennadiameter()
      | # free up resources used by the attached tool
      | msmd.done()
   
   We open the tool by querying the MS for its metadata. We then get
   the diameter of antenna 'VB2' and close the tool.
   
    
   
   ::
   
      | # attach tool to an MS
      | msmd.open("3C273XC1.MS")
      | # get the on-source integration time
      | exposure_time = msmd.effexposuretime()
      | # free up resources used by the attached tool
      | msmd.done()
   
   We open the tool by querying the MS for its metadata. We then get
   the on-source integration time and close the tool.
   
    
   
   ::
   
      | # attach tool to an MS
      | msmd.open("3C273XC1.MS")
      | # get the field names in the MS
      | fieldnames = msmd.fieldnames()
      | # free up resources used by the attached tool
      | msmd.done()
   
   We open the tool by querying the MS for its metadata. We then get
   the field names fromm the MS and close the tool.
   

.. _Development:

Development
   --CASA Developer--
   