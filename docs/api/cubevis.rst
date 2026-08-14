cubevis
====================

Cubevis is a casangi_ package containing visualization tools for CASA images and image cubes.
This package relies on the CASA data processing system as the processing backend while providing control and visualization using Bokeh.
The casangi package provides the following functionality for use in CASA:

+---------------------+--------------------------------------+
| task / function     |  description                         |
+=====================+======================================+
| iclean              |  Interactive Clean Task              |
+---------------------+--------------------------------------+
| iclean.notebook     |  Interactive Clean Notebook GUI      |
+---------------------+--------------------------------------+


.. _casangi: https://github.com/casangi


iclean
^^^^^^^^^

.. data:: Interactive Clean

The iclean task is designed to use the same API parameters as tclean, with only a couple exceptions:

* **interactive** : this parameter does not exist in iclean and interactive mode is always on
* **fullsummary** :  this parameter does not exist in iclean and fullsummary is always set to True when iclean makes calls to tclean and deconvolve

For all other API parameters please reference the `tclean API`_.

.. _tclean API: ../api/tt/casatasks.imaging.tclean.html

For a detailed description of the interactive clean GUI please reference the `Interactive Clean`_ page.

.. _Interactive Clean: ../notebooks/interactive_clean.html


iclean.notebook
^^^^^^^^^^^^^^^

.. data:: Interactive Clean Notebook

The iclean task can be used within a notebook. When it is used from a notebook, it can either display the GUI in
a separeate browser tab or it can display the GUI within the notebook. To display the GUI within a notebook, the
:code:`iclean.notebook` function is used to create the GUI display of the iclean task. Once created, this GUI can be
displayed with the `Bokeh <https://bokeh.org/>`__ :code:`show` function, by using the :code:`show` **member function**
of the GUI object or by having the created GUI be the last result of the cell.

The :code:`notebook` member function accepts all of the same parameters as the `iclean` task itself, but instead
of executing the GUI, as the :code:`iclean` tasks does, the :code:`notebook` function just builds the GUI for
display and execution within a notebook.

For a detailed example of using the :code:`notebook` functionality of iclean within a notebook, please reference
the `Interactive Clean Notebook`_ page. This page should execute correctly in a local classic Notebook or Jupyter
Lab Notebook. Colab usage may fail because support for Colab is being finalized.

.. _Interactive Clean Notebook: ../notebooks/interactive_clean_notebook.html
