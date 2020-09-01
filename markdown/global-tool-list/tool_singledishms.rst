Description
      The **sdms** tool offers an interface to process MS-formatted
      single-dish (hereafter SD) data. The provided capabilities include
      importing data to CASA in MS format from other formats (NRO's
      NOSTAR format and ATNF Scantable), selecting data, baseline
      fitting/subtraction, line fitting, smoothing, and so on. 

      In case you want to import SD data from other formats, do first as
      follows

      .. note:: *sdms.import{asap|nro}(infile='foo.asap', outfile='foo.ms')*

      To open your MS-formatted SD data with the **sdms** tool, run the
      following command

      .. note:: *sdms.open('foo.ms')*

      Finally, don't forget to close the **sdms** tool by

      .. note:: *sdms.close()*

      Note also that only one SD dataset can be attached to the **sdms**
      tool at a time.

      Since the **sdms** tool provides SD-specific functions only, you
      might want to use the **ms** tool functions as well to get some
      information about the data to process. Here is an example:

      .. note:: *sdms.open('foo.ms')*

         **ms.open('foo.ms')**

         *spwinfo =* **ms.getspectralwindowinfo()**

         *nrow =* **ms.nrow()**

         **ms.close()**

         *...*

         *sdms.close()*

      For more information on the **ms** tool functionality, see `the ms
      tool
      document <https://casa.nrao.edu/casadocs-devel/stable/global-tool-list/tool_ms>`__.
