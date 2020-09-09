#
# stub function definition file for docstring parsing
#

def flagmanager(vis, mode='list', versionname='', oldname='', comment='', merge='replace'):
    r"""
Enable list, save, restore, delete and rename flag version files.

Parameters
   - vis_ (string) - Name of input visibility file (MS)
   - mode_ (string='list') - Operation: list, save, restore, delete, rename

      .. raw:: html

         <details><summary><i> mode = save </i></summary>

      - versionname_ (string='') - Flag version name
      - comment_ (string='') - Short description of a versionname
      - merge_ (string='replace') - Merge option: replace will save or over-write the flags

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = restore </i></summary>

      - versionname_ (string='') - Flag version name
      - merge_ (string='replace') - Merge option: replace will save or over-write the flags

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = delete </i></summary>

      - versionname_ (string='') - Flag version name

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = rename </i></summary>

      - oldname_ (string='') - Flag version to rename
      - versionname_ (string='') - Flag version name
      - comment_ (string='') - Short description of a versionname

      .. raw:: html

         </details>


Description
   This task canmanageflagbackups of a MeasurementSet.
   flagbackups (or versions) arecopies of the FLAG column of a
   MeasurementSet, which are saved as a directoryon disk with the
   same basename of the MS from which it was created, with a
   \*.flagversions suffix. The flagbackups can be restored to the
   data setfrom which they werecreated in order toget back to a
   previous flag version. On running **importasdm**, a flag version
   called 'Original' is produced by default. It is recommended to
   save a flagbackup at the beginning or after serious editing.

   .. warning:: **WARNING**: The flag versions created from one MS should not
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

   .. rubric:: *mode='save', 'restore', 'delete', 'rename'*
      expandable parameters
      

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


.. _vis:

vis (string)
   | Name of input visibility file (MS)

.. _mode:

mode (string='list')
   | Operation: list, save, restore, delete, rename

.. _versionname:

versionname (string='')
   | Flag version name

.. _oldname:

oldname (string='')
   | Flag version to rename

.. _comment:

comment (string='')
   | Short description of a versionname

.. _merge:

merge (string='replace')
   | Merge option: replace will save or over-write the flags


    """
    pass
