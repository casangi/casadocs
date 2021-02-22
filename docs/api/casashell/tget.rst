tget
=====

.. currentmodule:: casashell


.. function:: tget(taskname=None, savefile='')

   Recover saved values of the inputs to a task. If given a taskname, sets taskname as the current active (default) task.

   Parameters
      - **taskname** (*obj* , *string*, or *None*) - task object or task name. None will use current active (default) task.
      - **savefile** (str) - Input file for the task inputs. default: <taskname>.last then <taskname>.saved. example: savefile='tclean.orion'

   Description
      This is a convenient way to retrieve the paramaters used in a previous task invocation. Typing
      ``tget`` without a taskname will recover the saved parameter values for the task that is currently
      active (default). If a task (or task name) is provided for the taskname parameter, e.g. ``tget <task>``,
      that task will become the active task and the parameter values will be restored for it.

      The previous task parameter values are stored in files. By default, they are retrieved based upon
      the name of the task. This is done by searching for

      1. a ``<taskname>.last`` file
      2. a ``<taskname>.saved`` file

      and then executing the Python in these files. For example, ::

         default('gaincal') #set current active task to gaincal and default
         tget #read saved inputs from gaincal.last (or gaincal.saved)
         inp() #see these inputs!
         tget bandpass #now get from bandpass.last (or bandpass.saved)
         inp() #task is now bandpass, with recovered inputs

      The ``savefile`` parameter can be used to cause ``tget`` to retrieve parameter values from a file
      with a different name. Supplying both the ``taskname`` and ``savefile`` parameters makes the
      specified task the active task and loads the defaults saved in the specified ``savefile``, for
      example, ::

         tget(gaincal,"ngc-calib.last")

      If the ``taskname`` parameter is omitted, The active task is used. For example ::

         default(tclean)
         tget(savefile='good-clean.last')

      Here, the active task is set with ``default(<task>)`` before loading the parameter values
      with ``tget``.
      
      **Note:** ``tget`` does not check whether the parameters in a named ``savefile`` came from the ``taskname``
      or active task. The global parameters set in that file will be set by ``tget``.
