.. container::
   :name: viewlet-above-content-title

singledishms
============

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   tool singledisms

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      The **sdms** tool offers an interface to process MS-formatted
      single-dish (hereafter SD) data. The provided capabilities include
      importing data to CASA in MS format from other formats (NRO's
      NOSTAR format and ATNF Scantable), selecting data, baseline
      fitting/subtraction, line fitting, smoothing, and so on. 

      In case you want to import SD data from other formats, do first as
      follows

      .. container:: casa-input-box

         *sdms.import{asap|nro}(infile='foo.asap', outfile='foo.ms')*

      To open your MS-formatted SD data with the **sdms** tool, run the
      following command

      .. container:: casa-input-box

         *sdms.open('foo.ms')*

      Finally, don't forget to close the **sdms** tool by

      .. container:: casa-input-box

         *sdms.close()*

      Note also that only one SD dataset can be attached to the **sdms**
      tool at a time.

      Since the **sdms** tool provides SD-specific functions only, you
      might want to use the **ms** tool functions as well to get some
      information about the data to process. Here is an example:

      .. container:: casa-input-box

         *sdms.open('foo.ms')*

         **ms.open('foo.ms')**

         *spwinfo =* **ms.getspectralwindowinfo()**

         *nrow =* **ms.nrow()**

         **ms.close()**

         *...*

         *sdms.close()*

      For more information on the **ms** tool functionality, see `the ms
      tool
      document <https://casa.nrao.edu/casadocs-devel/stable/global-tool-list/tool_ms>`__.

.. container:: section
   :name: viewlet-below-content-body


.. toctree::
   :hidden:
   :maxdepth: 3

   tool_singledishms/about
   tool_singledishms/methods
   tool_singledishms/changelog
   tool_singledishms/examples
   tool_singledishms/developer