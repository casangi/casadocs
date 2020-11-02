

.. _Description:

Description
   This task can manage flag backups of a MeasurementSet.
   flag backups (or versions) are copies of the FLAG column of a
   MeasurementSet, which are saved as a directory on disk with the
   same basename of the MS from which it was created, with a
   \*.flagversions suffix. The flag backups can be restored to the
   data set from which they were created in order to get back to a
   previous flag version. On running **importasdm**, a flag version
   called 'Original' is produced by default. It is recommended to
   save a flag backup at the beginning or after serious editing.  
   
   .. warning:: The flag versions created from one MS should not
      be restored to another MS. They are unique to the MS from which
      they were created. In the case of flags created from a
      `Multi-MS <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/the-multi-ms>`__,
      it is not possible to restore the flag versions to a serial MS
      and vice versa.
   
   flagmanager also returns a dictionary for mode='list', returning
   the flag version names and comments. 
   
   More information on flagmanager is also available in the `Data
   Examination and
   Editing <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing/managing-flag-versions-flagmanager>`__
   pages of CASAdocs.  
   
    
   
   .. rubric:: Parameter description
      
   
   .. rubric:: *vis*
      
   
   Name of input MeasurementSet or Multi-MS from where the flags were
   created.
   
   .. rubric:: *mode*
      
   
   Flag version operation. Below is the list of options for the
   *mode* parameter:
   
   -  'list': list existing flag versions
   -  'save': save the FLAG column from *vis* to a specified flag
      file. If the name given in *versionname* already exists, the
      task will give a warning and rename it to a name with a suffix
      '.old.timestamp'. The respective entry in FLAG_VERSION_LIST
      will also be updated.
   -  'restore': restore the specified flag file into the
      MeasurementSet given in *vis*
   -  'delete': delete the specified flag file
   -  'rename': will rename a specified flag file
   
   .. rubric:: *mode='save', 'restore', 'delete', 'rename'* expandable parameters
   
   .. rubric:: *versionname*
   
   Flag version name. The default is none *.* There should be no
   embedded blanks in the *versionname*.
   
   .. rubric:: *mode='save', 'rename'* expandable parameters
      
   
   .. rubric:: *comment*
      
   
   Short description of a *versionname*, when mode is 'save' or
   'rename'.
   
   .. rubric:: *mode='save', 'restore'* expandable parameters
      
   
   .. rubric:: *merge*
      
   
   Merge operation to use when saving the flags. Options available
   are: 'replace', and the experimental 'or', 'and'. Use the last two
   options at your own risk.
   
   .. rubric:: *mode='rename'* expandable parameters
      
   
   .. rubric:: *oldname*
      
   
   This parameter give the *oldname* of the flag versions when
   *mode='rename'*.
   

.. _Examples:

Examples
   Examples of using **flagmanager** to manipulate the flag versions of a MeasurementSet
      
   
   First save the flags from a MS using **flagdata**
   
   ::
   
      flagdata('my.ms', mode='manual', autocorr=True, flagbackup=True)
   
   List the existing flag versions of the above MS
   
   ::
   
      flagmanager('my.ms', mode='list')
   
   The output of the above command can be seen below. Note that the
   first flag versions is called 'Original", which was saved at
   import time using **importasdm**. The second entry called
   'flagdata_1' is the flag versions from the above manual flagging.
   
   ::
   
      2018-04-23 18:47:19 INFO flagmanager::agentflagger:: + MS : /Users/casadir/work/my.ms
   
      2018-04-23 18:47:19 INFO flagmanager::agentflagger:: main : working copy in main table
   
      2018-04-23 18:47:19 INFO flagmanager::agentflagger:: Original : Original flags at import into CASA
   
      2018-04-23 18:47:19 INFO flagmanager::agentflagger:: flagdata_1 : Flags autosave on 2018-04-23 20:47:14
   
   A captured Python dictionary returns the same content but is
   machine readable: 
   
   ::
   
      myflaglist = flagmanager('myvis.ms', mode='list')
   
   ::
   
      {0:{'name': 'Original', 'comment': 'Original flags at import into CASA'},
       1:{'name': 'flagdata_1', 'comment': 'Flags autosave on 2018-04-23 20:47:14'}}
   

   Rename the flag version to a more meaningful name
   
   ::
   
      flagmanager('my.ms', mode='rename', oldname='flagdata_1', versionname='autocorr', comment='Flags from autocorrelation')
   
   Restore the original flags to the MS
   
   ::
   
      flagmanager('my.ms', mode='restore', versionname='Original')
   

.. _Development:

Development
   None