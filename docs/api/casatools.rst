casatools
====================

The CASA toolkit is the foundation of the functionality in the package, and consists of a suite of
C++ classes that wrapped and imported in Python. The tools are typically used inside casatasks, but they can also be
used directly by advanced users to perform operations that are not available through the tasks.  Tools are typically
instantiated as stateful objects in Python.

.. rubric:: Tool Listing

.. automodsumm:: casatools
   :toctree: tt
   :nosignatures:
   :classes-only:
   :template: tooldoc.rst


.. currentmodule:: casatools


.. rubric:: Special Cases

In some cases, the state within a tool must be maintained singularly for an entire CASA session. In these cases,
a singleton object is instantiated and provided directly to the user.

.. data:: ctsys

   Singleton object from utils tool. See utils tool documentation for methods

   Examples
      ctsys is already instantiated and provides access to the methods of the utils tool class. For example: ::

         >>> from casatools import ctsys   # modular casa only, already imported in monolithic
         >>> ctsys.hostinfo()


.. data:: casalog

   Singleton object from logsink tool. See logsink tool documentation for methods

   Examples
      casalog is already instantiated and provides access to the methods of the utils tool class. For example: ::

         >>> from casatools import casalog   # modular casa only, already imported in monolithic
         >>> casalog.post('my example log message', 'INFO')

