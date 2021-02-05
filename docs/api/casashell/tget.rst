tget
=====

.. currentmodule:: casashell


.. function:: tget(taskname=None, savefile='')

   Recover saved values of the inputs to a task

   Parameters
      - **taskname** (*obj* or *None*) - task object, None will use current default
      - **savefile** (str) - Output file for the task inputs. default: task.last then task.saved. example: savefile=task.orion

   Description
      This is a convenient alternative to using the Python execfile command. Typing ``tget`` without a
      taskname will recover the saved values of the inputs for the current task as given in the current
      value of the taskname parameter.

      Adding a task name, e.g. ``tget <taskname>`` will recover values for the specified task. This is
      done by searching for

      1. a ``<taskname>.last`` file
      2. a ``<taskname>.saved`` file

      and then executing the Python in these files. For example, ::

         default('gaincal') #set current task to gaincal and default
         tget #read saved inputs from gaincal.last (or gaincal.saved)
         inp() #see these inputs!
         tget bandpass #now get from bandpass.last (or bandpass.saved)
         inp() #task is now bandpass, with recovered inputs

