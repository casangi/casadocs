

.. _Description:

Description
   The **sdms** tool offers an interface to process MS-formatted
   single-dish (hereafter SD) data. The provided capabilities include
   importing data to CASA in MS format from other formats (NRO's
   NOSTAR format and ATNF Scantable), selecting data, baseline
   fitting/subtraction, line fitting, smoothing, and so on. 
   
   In case you want to import SD data from other formats, do first as
   follows
   
   ::
   
      *sdms.import{asap|nro}(infile='foo.asap', outfile='foo.ms')*
   
   To open your MS-formatted SD data with the **sdms** tool, run the
   following command
   
   ::
   
      *sdms.open('foo.ms')*
   
   Finally, don't forget to close the **sdms** tool by
   
   ::
   
      *sdms.close()*
   
   Note also that only one SD dataset can be attached to the **sdms**
   tool at a time.
   
   Since the **sdms** tool provides SD-specific functions only, you
   might want to use the **ms** tool functions as well to get some
   information about the data to process. Here is an example:
   
   ::
   
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
   

.. _Examples:

Examples
   If you already have your SD data in MS format, you can operate on
   that data as follows. Here is an example to fit 3rd order
   polynomials to spectra stored in the FLOAT_DATA column with
   *field='M100'* and with *spw=5* and *7*, subtract it, then
   save the residual spectra into another file:
   
   ::
   
      sdms.open('foo.ms')
   
      sdms.set_selection(field='M100', spw='5,7')
   
      sdms.subtract_baseline(order=3, datacolumn='float_data',
      outfile='bar.ms')
   
      sdms.close()
   
   When importing SD data from other data formats than MS, do as
   follows:
   
   ::
   
      sdms.importnro(infile='foo.Y', outfile='bar.ms')      # import
      from NOSTAR format
   
    or
   
   ::
   
      sdms.importasap(infile='foo.asap', outfile='baz.ms')  # import
      from Scantable
   
   Once you get your data in MS format, you can process it as shown
   in the code sample at the top of this page.
   

.. _Development:

Development
   No additional development details

