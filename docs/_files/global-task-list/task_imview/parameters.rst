Parameters
==========

.. container:: documentDescription description

   task parameters

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               raster : string record

            (Optional) Raster filename (string) or complete raster
            config dictionary. The allowed dictionary keys are file
            (string), scaling (numeric), range (2 element numeric
            vector), colormap (string), and colorwedge (bool).

Example

.. container:: param

   .. container:: parameters2

      contour : string record

   (Optional) Contour filename (string) or complete contour config
   dictionary. The allowed dictionary keys are file (string), levels
   (numeric vector), unit (float), and base (float).

Example

.. container:: param

   .. container:: parameters2

      zoom : int string record = 1

   (Optional) zoom can specify intermental zoom (integer), zoom region
   read from a file (string) or dictionary specifying the zoom region.
   The dictionary can have two forms. It can be either a simple region
   specified with blc (2 element vector) and trc (2 element vector)
   [along with an optional coord key ("pixel" or "world"; pixel is the
   default) or a complete region rectangle e.g. loaded with
   "rg.fromfiletorecord( )". The dictionary can also contain a channel
   (integer) field which indicates which channel should be displayed.

Example

.. container:: param

   .. container:: parameters2

      axes : string record

   (Optional) this can either be a three element vector (string) where
   each element describes what should be found on each of the x, y, and
   z axes or a dictionary containing fields "x", "y" and "z" (string).

Example

.. container:: param

   .. container:: parameters2

      out : string record

   (Optional) Output filename or complete output config dictionary. If a
   string is passed, the file extension is used to determine the output
   type (jpg, pdf, eps, ps, png, xbm, xpm, or ppm). If a dictionary is
   passed, it can contain the fields, file (string), scale (float), dpi
   (int), or orient (landscape or portrait). The scale field is used for
   the bitmap formats (i.e. not ps or pdf) and the dpi parameter is used
   for scalable formats (pdf or ps).

Example

.. container:: section
   :name: viewlet-below-content-body
