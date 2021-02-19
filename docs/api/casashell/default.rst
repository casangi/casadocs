default
========

.. currentmodule:: casashell


.. function:: default(taskname)

   Set the current default task for inp and go commands and reset task parameter values

   Parameters
      - **taskname** (*string*) - name of task

   Description
      Each task has a special set of default parameters defined for its parameters. You can
      use the **default()** command to reset the parameters for a specified task (or the
      current task as defined by the taskname variable) to their default.

      The ``default()`` command resets the values of the task parameters to a set
      of "defaults" as specified in the task code. Some defaults are blank strings '' or empty
      lists [], others are specific numerical values, strings, or lists. It is important to
      understand that just setting a string parameter to an empty string '' is not setting it
      to its default! Some parameters do not have a blank as an allowed value. See the help for
      a particular task to find out its default. If '' is the default or an allowed value, it
      will say so explicitly.

