go
======

.. currentmodule:: casashell


.. function:: go(taskname=None)

   Execute given task using parameters from the workspace. If given a taskname, sets
   taskname as the current active (default) task.

   If the task is successfully executed, then a ``<taskname>.last`` file
   is created in the working directory containing the parameter values

   Parameters
      - **taskname** (*obj*, *string*, or *None*) - task object or task name. None will use current active (default) task.

   Description
      You can execute a task using the ``go()`` command, either explicitly ::

         CASA <44>: go listobs
         ---------> go(listobs)
         Executing: listobs()
         ...

      or implicitly if the active (default) task has already been set (e.g. by previous use of ``default()`` or ``inp()``) ::

         CASA <45>: inp tclean
         CASA <46>: go()
         ---------> go()
         Executing: tclean()
         ...

      You can also execute a task simply by typing the taskname. ::

         CASA <46>: tclean
         ---------> tclean()
         Executing: tclean()
         ...

