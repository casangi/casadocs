saveinputs
===========

.. currentmodule:: casashell

.. function:: saveinputs(taskname=None, outfile=None)

   Save current task parameters to file. If given a taskname, sets taskname as the current active (default) task.

   Parameters
      - **taskname** (*obj*, *string*, or *None*) - task object or task name. None will use current active (default) task.
      - **outfile** (*string* or *None*) - output file name, None will use current active (default) taskname.

   Description
      ``saveinputs`` is a synonym for ``tput``. See ``tput`` for the full documentation.
