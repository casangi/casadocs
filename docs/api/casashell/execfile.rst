execfile
=========

.. currentmodule:: casashell


.. function:: execfile(filename, globals=globals())

   Execute file

   Parameters
      - **filename** (*string*) - name of file to execute
      - **globals** (*dictionary*) - the environment for evaluation

   Description
      Python 3 removed the ``execfile`` builtin function. CASA provides a convenience function that
      attempts to reproduce the behavior of the Python 2.7 builtin ``execfile`` function. While casashell 
      tasks (tasks run in the CASA shell environment) could be treated as scriptable in the 
      Python 2.7/CASA 5 version of execfile, in Python 3/CASA 6 this behavior is not supported. 
      Python replacements for execfile exist [i.e., "%run -i" or "exec(open(read..."] 
      which provide some scripting capabilities for casashell commands, though these Python alternatives 
      are not tested in any internal CASA regression tests.

      ``execfile`` evaluates contents of ``filename`` in the environment specified by ``globals``.


      When ``execfile`` is used within the ``filename`` being evaluated, it is necessary to add
      ``globals( )`` as the second argument to those execfile calls in order for the secondary
      script to know about the global variables of the calling script. For example, within a script
      ‘mainscript.py’, calls to another script ‘myscript.py’ should be written as
      ``execfile(‘myscript.py’, globals())``.

