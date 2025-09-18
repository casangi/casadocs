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


**Note** notes here
