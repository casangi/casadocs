tput
=====


.. currentmodule:: casashell

.. function:: tput(taskname=None, outfile='')

   Save the current parameter values of a task to its ``<taskname>.last`` file. If given a taskname, sets 
   taskname as the current active (default) task.

   Parameters
      - **taskname** (*obj*, *string*, or *None*) - task object or task name. None will use current active (default) task.
      - **outfile** (str) - Output file for the task inputs. default: <taskname>.last example: savefile='tclean.orion'

   Description
      This is a shorthand to ``saveinputs`` and is a counterpart to ``tget``. Typing
      ``tput`` without a taskname will save the values of the inputs for the current active (default)
      task.

      Adding a task name, e.g. ``tput <taskname>`` will save the values for the specified task.
      For example, ::

         default('gaincal') #set current task to gaincal and default
         tget #read saved inputs from gaincal.last (or gaincal.saved)
         inp() #see these inputs!
         vis = 'new.ms' #change the vis parameter
         tput #save back to the gaincal.last file for later use

