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
      attempts to reproduce the behavior of the Python 2.7 builtin ``execfile`` function.

      ``execfile`` evaluates contents of ``filename`` in the environment specified by ``globals``.
