casalith
====================

CASA monolithic environment bundling Python and library dependencies into a single download package.

.. currentmodule:: casalith



tasks
^^^^^

A few remaining tasks are found only in the monolithic environment

.. automodsumm:: casalith
   :toctree: tt
   :nosignatures:
   :functions-only:



executables
^^^^^^^^^^^

The following executable applications are located in the <casa release>/bin directory of the expanded monolithic CASA tarball:

.. data:: python3(v3.6.7)

.. data:: pip3(v9.0.1)

.. data:: 2to3

.. data:: casa

.. data:: mpicasa

.. data:: casaviewer


python libraries
^^^^^^^^^^^^^^^^

The following third party libraries are included in the python distribution of monolithic casa and available as imports:

.. data:: libraries(attrs==19.3.0, backcall==0.1.0, certifi==2020.12.5, cycler==0.10.0, decorator==4.4.2, grpcio==1.29.0, importlib-metadata==1.6.0, ipython==7.15.0, ipython-genutils==0.2.0, jedi==0.17.0, kiwisolver==1.2.0, matplotlib==3.2.1, more-itertools==8.3.0, mpi4py==3.0.3, numpy==1.18.4, packaging==20.4, parso==0.7.0, pexpect==4.8.0, pickleshare==0.7.5, pluggy==0.13.1, prompt-toolkit==3.0.5, protobuf==3.12.2, ptyprocess==0.6.0, py==1.8.1, pyfits==3.5, Pygments==2.6.1, pyparsing==2.4.7, pytest==5.4.2, python-dateutil==2.8.1, pytz==2020.1, scipy==1.4.1, six==1.15.0, traitlets==4.3.3, wcwidth==0.2.2, zipp==3.1.0)


Note that each component in the modular CASA distribution uses a subset of these same dependencies.

The definition is provided here in pip compatible format such that one could save the preceding list to a list.txt file and
recreate using:

::

   pip install -r list.txt


