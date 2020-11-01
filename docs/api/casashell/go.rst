go
======

.. currentmodule:: casashell


.. function:: go(taskname=None)

   Execute given task using parameters from the workspace

   If the task is successfully executed, then a ``<taskname>.last`` file
   is created in the working directory containing the parameter values

   Parameters
      - **taskname** (*string* or *None*) - name of task, None will use current default

   Description
      You can execute a task using the ``go()`` command, either explicitly ::

         CASA <44>: go listobs
         ---------> go(listobs)
         Executing: listobs()
         ...

      or implicitly if taskname is defined (e.g. by previous use of ``default()`` or ``inp()`` ) ::

         CASA <45>: taskname = 'clean'
         CASA <46>: go()
         ---------> go()
         Executing: clean()
         ...

      You can also execute a task simply by typing the taskname. ::

         CASA <46>: clean
         ---------> clean()
         Executing: clean()
         ...

      The ``go()`` command can also be used to launch a different task without changing the current
      taskname, without disrupting the ``inp()`` process on the current task you are working on.
      For example ::

         default 'gaincal' #set current task to gaincal and default
         vis = 'n5921.ms' #set the working ms
         ... #set some more parameters
         go listobs #launch listobs w/o changing current task
         inp() #see the inputs for gaincal (not listobs!)

      **ALERT:** Doing ``go listobs(vis='foo.ms')`` will currently change the taskname, and will change *vis*,
      which might not be what is desired.


