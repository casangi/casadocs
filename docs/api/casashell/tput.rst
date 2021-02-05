tput
=====


.. currentmodule:: casashell

.. function:: tput(taskname=None, outfile='')

   Save the current parameter values of a task to its ``<taskname>.last`` file

   Parameters
      - **taskname** (*obj* or *None*) - task object, None will use current default
      - **outfile** (str) - Output file for the task inputs. default: task.last example: savefile=task.orion

   Description
      This is a shorthand to ``saveinputs`` and is a counterpart to ``tget``. Typing
      ``tput`` without a taskname will save the values of the inputs for the current
      task as given in the current value of the taskname parameter.

      Adding a task name, e.g. ``tput <taskname>`` will save the values for the specified task.
      For example, ::

         default('gaincal') #set current task to gaincal and default
         tget #read saved inputs from gaincal.last (or gaincal.saved)
         inp() #see these inputs!
         vis = 'new.ms' #change the vis parameter
         tput #save back to the gaincal.last file for later use

