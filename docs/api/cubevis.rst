cubevis
====================

Cubevis is a casangi package containing visualization tools for CASA images.
This package relies on the CASA data processing system as the processing backend while providing control and visualization using Bokeh.

.. automodsumm:: cubevis
   :toctree: tt
   :nosignatures:
   :functions-only:

iclean
^^^^^^^^^

.. data:: Interactive Clean

The iclean task is designed to use the same API parameters as tclean, with only a couple exceptions:
interactive : this parameter does not exist in iclean and interactive mode is always on
fullsummary :  this parameter does not exist in iclean and fullsummary is always set to True when iclean makes calls to tclean and deconvolve

For all other API parameters please reference the [tclean API](../api/tt/casatasks.imaging.tclean.html).

For a detailed description of the interactive clean GUI please reference the [Interactive Clean page](../notebooks/interactive_clean.html).

**Note** notes here
