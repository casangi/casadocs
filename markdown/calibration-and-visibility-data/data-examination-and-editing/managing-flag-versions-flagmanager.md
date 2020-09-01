

# Manage flag versions 

Managing flag versions

The **flagmanager** task will allow you to manage different versions of flags in your data. These are stored inside a CASA flag versions table, under the name of the MS \<msname\>.flagversions. For example, for the MS jupiter6cm.usecase.ms, there will need to be jupiter6cm.usecase.ms.flagversions on disk. This is created on import (by **importasdm**, **importvla** or **importuvfits**) or when flagging is first done on an MS without a .flagversions. 

By default, when the .flagversions is created, this directory will contain a flags.Original table containing a copy of the original flags in the MAIN] table of the MS so that you have a backup. It will also contain a file called [FLAG_VERSION_LIST that has the information on the various flag versions there. The flag versions are cumulative, i.e. a specific version number contains all the flags from the lower version numbers, too. 

The flags are stored in an MS column of the same spectral and correlator polarization shape as the visibility data values, with Boolean 1 to indicate that a particular time, channel, polarization has been flagged or 0 for unflagged.

 

The inputs for **flagmanager**  are:

```
vis                 =         ''        #   Name of input visibility file (MS)
mode                =     'list'        #   Flag management operation (list,save,restore,delete)
```

The mode='list' option will list the available flag versions from the \<msname\>.flagversions file in the logger. For example:

```
CASA <102>: default('flagmanager')
CASA <103>: vis = 'jupiter6cm.usecase.ms'
CASA <104>: mode = 'list'
CASA <105>: flagmanager()
MS : /home/imager-b/smyers/Oct07/jupiter6cm.usecase.ms

main : working copy in main table
Original : Original flags at import into CASA
flagautocorr : flagged autocorr
flagdata_1 : Flags autosave on 2018-07-16 08:57:20]
```

*mode=\'list\'* will also return a Python dictionary with the available flag versions. For example:

```
myflags = flagmanager('jupiter6cm.usecase.ms', mode='list')

myflags

{0: {'comment': 'Original flags at import into CASA', 'name': 'Original'},1: {'comment': 'flagged autocorr', 'name': 'flagautocorr'},2: {'comment': 'Flags autosave on 2018-07-16 08:57:20', 'name': 'flagdata_1'},'MS': '/home/imager-b/smyers/Oct07/jupiter6cm.usecase.ms'}}
```

The mode] parameter expands the options. For example, if you wish to save the current flagging state of [vis=\<msname\>:

```
mode                =     'save'        #   Flag management operation (list, save, restore, delete)
versionname         =         ''        #   Name of flag version (no spaces)
comment             =         ''        #   Short description of flag version
merge               =  'replace'        #   Merge option (replace, and, or)
```

  with the output version name specified by ]versionname. For example, the above [xyflags version was written using: 

```
default('flagmanager')
vis = 'jupiter6cm.usecase.ms'
mode = 'save'
versionname = 'xyflags'
comment = 'Plotxy flags'
flagmanager()
```

  and you can see that there is now a sub-table in the flag versions directory:

```
CASA <106>: ls jupiter6cm.usecase.ms.flagversions/
  IPython system call: ls -F jupiter6cm.usecase.ms.flagversions/
  flags.flagautocorr  flags.Original  flags.xyflags  FLAG_VERSION_LIST
```

It is recommended that you use this task regularly to save versions during flagging.

Note that if a flag version already exists under a name, the task will give a warning and add a suffix '.old.timestamp' to the previous version.

You can restore a previously saved set of flags using the mode='restore' option:

```
mode                =  'restore'        #   Flag management operation (list,save,restore,delete)
versionname         =         ''        #   Name of flag version (no spaces)
merge               =  'replace'        #   Merge option (replace, and, or)
```

  The ]merge] sub-parameter will control how the flags are restored. For [merge='replace'], the flags in [versionname] will replace those in the MAIN table of the MS. For [merge='and'], only data that is flagged in BOTH the current MAIN table and in [versionname] will be flagged. For [merge='or', data flagged in EITHER the MAIN or in [versionname will be flagged.

The mode='delete'] option can be used to remove [versionname from the flag versions:

```
mode                =   'delete'        #   Flag management operation (list,save,restore,delete)
versionname         =         ''        #   Name of flag version (no spaces)
```

