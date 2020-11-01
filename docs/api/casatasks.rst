casatasks
====================

Tasks in CASA are python interfaces to the more basic toolkit. Tasks are executed to perform a single job,
such as loading, plotting, flagging, calibrating, and imaging the data.

The parameters used and their defaults can be obtained by typing ``help(<taskname>)`` at the Python prompt,
where ``<taskname>`` is the name of a given task. This command lists all parameters, a brief
description of the parameter, the parameter default, and any options if there are limited allowed values
for the parameter.

.. rubric:: Experimental tasks and algorithms

Some tasks and algorithms in CASA are labelled as **Experimental** or **Unverified**. These tasks have
not been fully commissioned and/or verified.  Such tasks are provided to enhance user capabilities, or because
they are required for specific pipeline use.

The label `Experimental` or `Unverified` means that the task/algorithm falls under the
following disclaimers:

- Only a subset of modes have been incorporated into CASA unit/regression tests. These are
  documented in CASA Docs. Other options/modes may be run, and might work just fine, but they are
  not part of what has been tested carefully.
- Some parameters have been tested for specific use cases (as part of the algorithm development,
  publication, and CASA test programs), but we have not yet established best practices for all
  different situations. This information will build over time and will be incorporated into our
  documentation as appropriate.
- Experimental tasks and algorithms may have Known Issues, representing CASA\'s current
  understanding of the state of the code. These `Known Issues <../notebooks/introduction.ipynb#known-issues>`_
  are clearly defined as part of CASA Docs.
- Parameter names and task structure can change, based on feedback and improved understanding of
  usability.

It is expected that ALMA and VLA pipelines will begin using experimental tasks only after they have
stabilized for stand-alone use.

The complete listing of tasks available in CASA is as follows:

Input / Output
^^^^^^^^^^^^^^^

.. automodsumm:: casatasks.data
   :toctree: tt
   :nosignatures:
   :functions-only:


Information
^^^^^^^^^^^^^^^

.. automodsumm:: casatasks.information
   :toctree: tt
   :nosignatures:
   :functions-only:


Flagging
^^^^^^^^^^^^^

.. automodsumm:: casatasks.flagging
   :toctree: tt
   :nosignatures:
   :functions-only:


Calibration
^^^^^^^^^^^^^

.. automodsumm:: casatasks.calibration
   :toctree: tt
   :nosignatures:
   :functions-only:


Imaging
^^^^^^^^^^^^^^^

.. automodsumm:: casatasks.imaging
   :toctree: tt
   :nosignatures:
   :functions-only:


Single Dish
^^^^^^^^^^^^^^^

.. automodsumm:: casatasks.single
   :toctree: tt
   :nosignatures:
   :functions-only:


Manipulation
^^^^^^^^^^^^^^^

.. automodsumm:: casatasks.manipulation
   :toctree: tt
   :nosignatures:
   :functions-only:


Analysis
^^^^^^^^^

.. automodsumm:: casatasks.analysis
   :toctree: tt
   :nosignatures:
   :functions-only:


Visualization
^^^^^^^^^^^^^^^

.. automodsumm:: casatasks.visualization
   :toctree: tt
   :nosignatures:
   :functions-only:


Simulation
^^^^^^^^^^^^^^^

.. automodsumm:: casatasks.simulation
   :toctree: tt
   :nosignatures:
   :functions-only:
