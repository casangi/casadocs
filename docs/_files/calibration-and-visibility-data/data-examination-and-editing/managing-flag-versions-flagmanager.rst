.. container::
   :name: viewlet-above-content-title

Manage flag versions
====================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Managing flag versions

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      The flagmanagertask will allow you to manage different versions of
      flags in your data. These are stored inside a CASA flag versions
      table, under the name of the MS <msname>.flagversions. For
      example, for the MSjupiter6cm.usecase.ms, there will need to
      bejupiter6cm.usecase.ms.flagversionson disk. This is created on
      import (by importasdm, importvlaor importuvfits) or when flagging
      is first done on an MS without a.flagversions.

      By default, when the.flagversionsis created, this directory will
      contain aflags.Originaltable containing a copy of the original
      flags in theMAINtable of the MS so that you have a backup. It will
      also contain a file calledFLAG_VERSION_LISTthat has the
      information on the various flag versions there. Theflag
      versionsare cumulative, i.e. a specific version number contains
      all the flags from the lower version numbers, too.

      The flags are stored in an MS column of the same spectral and
      correlator polarization shape as the visibility data values, with
      Boolean 1 to indicate that a particular time, channel,
      polarization has been flagged or 0 for unflagged.

       

      The inputs for flagmanagerare:

      .. container:: casa-input-box

         | vis                 =         ''        #   Name of input
           visibility file (MS)
         | mode                =     'list'        #   Flag management
           operation (list,save,restore,delete)

      Themode=’list’option will list the available flag versions from
      the<msname>.flagversionsfile in the logger. For example:

      .. container:: casa-input-box

         | CASA <102>: default('flagmanager')
         | CASA <103>: vis = 'jupiter6cm.usecase.ms'
         | CASA <104>: mode = 'list'
         | CASA <105>: flagmanager()
         | MS : /home/imager-b/smyers/Oct07/jupiter6cm.usecase.ms

         | main : working copy in main table
         | Original : Original flags at import into CASA
         | flagautocorr : flagged autocorr
         | flagdata_1 : Flags autosave on 2018-07-16 08:57:20]

      mode='list' will also return a Python dictionary with the
      available flag versions. For example:

      .. container:: casa-input-box

         myflags = flagmanager('jupiter6cm.usecase.ms', mode='list')

         myflags

         {0: {'comment': 'Original flags at import into CASA', 'name':
         'Original'},1: {'comment': 'flagged autocorr', 'name':
         'flagautocorr'},2: {'comment': 'Flags autosave on 2018-07-16
         08:57:20', 'name': 'flagdata_1'},'MS':
         '/home/imager-b/smyers/Oct07/jupiter6cm.usecase.ms'}}

      Themodeparameter expands the options. For example, if you wish to
      save the current flagging state ofvis=<msname>:

      .. container:: casa-input-box

         | mode                =     'save'        #   Flag management
           operation (list, save, restore, delete)
         | versionname         =         ''        #   Name of flag
           version (no spaces)
         | comment             =         ''        #   Short description
           of flag version
         | merge               =  'replace'        #   Merge option
           (replace, and, or)

      with the output version name specified byversionname. For example,
      the abovexyflagsversion was written using:

      .. container:: casa-input-box

         | default('flagmanager')
         | vis = 'jupiter6cm.usecase.ms'
         | mode = 'save'
         | versionname = 'xyflags'
         | comment = 'Plotxy flags'
         | flagmanager()

      and you can see that there is now a sub-table in the flag versions
      directory:

      .. container:: casa-input-box

         | CASA <106>: ls jupiter6cm.usecase.ms.flagversions/
         |   IPython system call: ls -F
           jupiter6cm.usecase.ms.flagversions/
         |   flags.flagautocorr  flags.Original  flags.xyflags 
           FLAG_VERSION_LIST

      It is recommended that you use this task regularly to save
      versions during flagging.

      Note that if a flag version already exists under a name, the task
      will give a warning and add a suffix ’.old.timestamp’ to the
      previous version.

      You can restore a previously saved set of flags using
      themode=’restore’option:

      .. container:: casa-input-box

         | mode                =  'restore'        #   Flag management
           operation (list,save,restore,delete)
         | versionname         =         ''        #   Name of flag
           version (no spaces)
         | merge               =  'replace'        #   Merge option
           (replace, and, or)

      Themergesub-parameter will control how the flags are restored.
      Formerge=’replace’, the flags inversionnamewill replace those in
      the MAIN table of the MS. Formerge=’and’, only data that is
      flagged in BOTH the current MAIN table and inversionnamewill be
      flagged. Formerge=’or’, data flagged in EITHER the MAIN or
      inversionnamewill be flagged.

      Themode=’delete’option can be used to removeversionnamefrom the
      flag versions:

      .. container:: casa-input-box

         | mode                =   'delete'        #   Flag management
           operation (list,save,restore,delete)
         | versionname         =         ''        #   Name of flag
           version (no spaces)

.. container:: section
   :name: viewlet-below-content-body
