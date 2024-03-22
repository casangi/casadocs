vishead -- List, summary, get, and put metadata in a measurement set -- information, manipulation task
=======================================

Description
---------------------------------------


        This task allows the user to manipulate some meta-data keywords in a
        measurement set.  The mode='list' shows those keywords that are
        presently implemented, with their values.  The contents associated
        with the keywords can be obtained with mode='get' and changed with mode='put'. 

        The modes that are available are:

           list    --- List all keywords that are recognized, and list the
                       value(s) for each.  Only these keywords can be obtained
                       (get) or changed (put) 
           summary --- Provides a summary that is equivalent to running listobs(verbose=False)
           get     --- Get the specified keyword value(s) from the ms
           put     --- Put the specified keyword value(s) into the ms

        Keywords currently implemented are:

           cal_grp              
           field                 Field names
           fld_code              Field Observing codes
           freq_group_name       
           log                   
           observer              Observer name
           project               Project name
           ptcs                  Phase tracking centers for each field
           release_date          
           schedule
           schedule_type
           spw_name              Spectral parameters?
           source_name           Source Names (=Field Names?)
           telescope             Telescope Name

        Note that the default list of keywords is a subset of the former list. To get
        all the keywords set listitemts=[]. See task parameter listitems for more details.





Parameters
---------------------------------------
.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   * - Parameter
     - Default
     - Description
   * - vis
     - :code:`''`
     - Name of input visibility file
   * - mode
     - :code:`'summary'`
     - Mode of operation for vishead
   * - listitems
     - :code:`numpy.array( [ 'telescope','observer','project','field','freq_group_name','spw_name','schedule','schedule_type','release_date' ] )`
     - Keyword items to list. This parameter is only relevant in list mode. Note that the default list is a subset of the possible keywords. To get all the keywords set listitems=[]
   * - hdkey
     - :code:`''`
     - Keyword to get/put
   * - hdindex
     - :code:`''`
     - Index (counting from 0) if keyword is an array (used in get/put mode only). The empty string means all elements
   * - hdvalue
     - :code:`''`
     - Value of the keywords to be put in the MS (used in put mode only)


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file


mode
---------------------------------------

:code:`'summary'`

Mode of operation for vishead


listitems
---------------------------------------

:code:`numpy.array( [ 'telescope','observer','project','field','freq_group_name','spw_name','schedule','schedule_type','release_date' ] )`

Keyword items to list. This parameter is only relevant in list mode. Note that the default list is a subset of the possible keywords. To get all the keywords set listitems=[]


hdkey
---------------------------------------

:code:`''`

Keyword to get/put


hdindex
---------------------------------------

:code:`''`

Index (counting from 0) if keyword is an array (used in get/put mode only). The empty string means all elements


hdvalue
---------------------------------------

:code:`''`

Value of the keywords to be put in the MS (used in put mode only)




