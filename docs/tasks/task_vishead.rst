

.. _Returns:

Returns
   out (tuple or dict) - when mode='get', tuple with the value of the
   requested keyword, and associated metainformation if
   available. When mode='list', a dictionary containing the values of
   each keyword given in the listitems parameter


.. _Description:

Description
   This task allows the user to manipulate some meta-data
   keywords in a measurement set. The mode='list' shows those
   keywords that are presently implemented, with their values. The
   contents associated with the keywords can be obtained with
   mode='get' and changed with mode='put'.

   The modes that are available are:
   
   -  list: List all keywords that are recognized, and list the
      value(s) for each.  Only these keywords can be obtained (get)
      or changed (put)
   -  summary: Provides a summary that is equivalent to running
      listobs(verbose=False)
   -  get: Get the specified keyword value(s) from the ms
   -  put: Put the specified keyword value(s) into the ms
   
   Keywords currently implemented are:
   
   -  cal_grp             
   -  field (Field names)
   -  fld_code (Field Observing codes)
   -  freq_group_name      
   -  log                  
   -  observer(Observer name)
   -  project (Project name)
   -  ptcs(Phase tracking centers for each field)
   -  release_date
   -  schedule
   -  schedule_type
   -  spw_name              
   -  source_name         
   -  telescope (Telescope Name)
   
   Note that the default list of keywords is a subset of the former list. To get
   all the keywords mentioned above set listitemts=[]. See
   the Parameter pages of vishead for more details.
   
   More information can also be found in the CASA Docs pages on
   `Listing and Changing MS
   Metadata <../../notebooks/data_examination.ipynb>`__.
   

.. _Examples:

Examples
   To list the available keywords in a MeasurementSet:
   
   ::
   
      vishead(vis='measurementset.ms',mode='list')

   
   To get the values for the phase center:
   
   ::
   
      vishead(vis='measurementset.ms',mode='get',hdkey='ptcs',hdindex='1')
   
   In this example, hdvalue [0][0] gives the RA,
   while hdvalue [0][1] gives the DEC in field '1'.

   
   To get the name for field 2:
   
   ::
   
      vishead(vis='measurementset.ms',mode='get',hdkey='field',hdindex='2')

   
   To change the name for field 2 into "junk".
   
   ::
   
      vishead(vis='measurementset.ms',mode='put',hdkey='field',hdindex='2',hdvalue='junk')

   
   .. note:: NOTE: To transfer the parameters to useful python items
      requires some care. Changing a number (e.g. RA of field=1 to
      0.5 radian) may be complicated to figure out.
   

.. _Development:

Development
   No additional development details

