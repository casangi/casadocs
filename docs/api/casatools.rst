casatools
====================

The CASA toolkit is the foundation of the functionality in the package, and consists of a suite of
functions that are callable from Python. The tools are used by the tasks, and can be used by advanced
users to perform operations that are not available through the tasks.

It is beyond the scope of this reference to describe the toolkit in detail. Occasionally, examples
will be given that utilize the tools. In short, tools are always called as functions, with any
parameters that are not to be defaulted given as arguments. For example: ::

   ia.open('ngc5921.chan21.clean.cleanbox.mask')
   ia.calcmask('"ngc5921.chan21.clean.cleanbox.mask">0.5','mymask')
   ia.summary()
   ia.close()

uses the image tool (**ia**) to turn a clean mask image into an image mask.

.. rubric:: Tool Listing

.. automodsumm:: casatools
   :toctree: tt
   :nosignatures:
   :classes-only:
   :template: tooldoc.rst


