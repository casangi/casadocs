.. container::
   :name: viewlet-above-content-title

Parameters
==========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task applycal parameters

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               imagename : string

            Input image cube. Default: none Example:
            imagename='ngc5921_task.image'

Example

imagename='ngc5921_task.image'

.. container:: param

   .. container:: parameters2

      mode : string = summary

   Mode of operation. Default: summary Options: "add", "del", "get",
   "history", "list", "put", or "summary". \* add: Add a new metadata
   value to the image. The behavior of mode="add" depends on the
   keyword. In general, the return value will be True if the operation
   succeeds, or False if it fails or is not supported. If unsuccessful
   or not supported, a message is normally logged which describes the
   failure. In most cases, you probably want to use mode='put' rather
   than mode='add'. We continue to support mode='add' mainly for
   backward compatibility. \* del: Delete a key or reset its value to a
   fidicual value if possible. Ignores all but imagename, mode, and
   hdkey parameters. In general, the return value will be True if the
   operation succeeds, or False if it fails or is not supported. If
   unsuccessful or not supported, a warning message is normally logged
   which describes the failure. \* get: Return the specified keyword
   value. Ignores all but imagename, mode, and hdkey parameters. \*
   history: Log image history. Ignores all but imagename and mode
   parameters. \* list: Show supported keywords and their values.
   Ignores all but imagename and mode parameters. put: Modify the
   specified value associated with the keyword. True is returned if the
   metadatum was successfully modified, False otherwise. Normally, a
   diagnostic message is logged if there is a failure. Only the
   parameter specified is modified; eg, no modification of reference
   direction occurs to implicitly account for precession to a new
   reference frame. \* summary: Log a summary of the image and return a
   dictionary of various metadata values. Ignores all but imagename and
   mode parameters. IMPORTANT: Lists of keywords for the various modes
   of operation are given in the imhead task pages of CASA Docs
   (https://casa.nrao.edu/casadocs/). The behavior of mode='add|del|get
   depends on the keyword. Modes "add", "del", and "put" will not work
   if the image is read-only (eg a FITS image). NOTE: Only limited
   checking is implemented to ensure modifying a specific value will
   leave the image metadata in a consistent state, so, if one is not
   careful, one could end up with an image that has an inconsistent set
   of metadata and is therefore, nonsensical and useless That is,
   PROCEED AT YOUR OWN RISK when using modes add, del, or put.

Allowed Value(s)

list history get put add del summary

Example

.. container:: param

   .. container:: parameters2

      hdkey : string

   Keyword to use with get, put, add, or del. Subparameter of
   mode=get|put|add|del Only "get" will work if the image is read-only
   (eg, a FITS image). Example: hdkey='telescope'

Example

hdkey='telescope'

.. container:: param

   .. container:: parameters2

      hdvalue : undefined

   Keyword value used for modes 'put' and 'add'. Subparameter of
   mode='put|add' ('del') Also used for mode="del" when hdvalue="masks.
   Example: hdvalue='VLA'

Example

hdvalue='VLA'

.. container:: param

   .. container:: parameters2

      verbose : bool = False

   Give a full listing of beams or just a short summary? Only used when
   the image has multiple beams and mode="summary".

Example

.. container:: section
   :name: viewlet-below-content-body
