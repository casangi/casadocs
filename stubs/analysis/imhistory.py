#
# stub function definition file for docstring parsing
#

def imhistory(imagename, mode='list', verbose=True, origin='imhistory', message=''):
    r"""
Retrieve and modify image history

Parameters
   - imagename_ (string) - Name of the input spectral line image
   - mode_ (string='list') - Mode to run in, "list" to retrieve history, "append" to append a record to history.

      .. raw:: html

         <details><summary><i> mode = list </i></summary>

      - verbose_ (bool=True) - Write history to logger if mode="list"?

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = append </i></summary>

      - origin_ (string='imhistory') - Origin of appended message. Only used for mode="append".
      - message_ (string='') - Message to append. Only used of mode="append".

      .. raw:: html

         </details>


Description
   This task prints out the history information contained in the
   image file.

   The task provides access to the logtable of an image, where
   generally history information is stored, and prints out the
   history information (for each of the supported formats). Two
   operation modes are supported. When *mode="list"*, the history
   messages are returned as an array of strings. If *verbose=True*,
   this information is also written to the logger. When
   *mode="append"*, a specified message, along with its specified
   origin, are appended to the logtable and *True* is returned if
   successful.




Details
   Explanation of each parameter

.. _imagename:

   .. rubric:: imagename

   | Name of the input (CASA or FITS) image
   |                      Default: none
   | 
   |                         Example: imagename='ngc5921.im'

.. _mode:

   .. rubric:: mode

   | Operating mode.
   |                      Default: 'list' (retrieve history)
   |                      Options: 'list|append' ('append' to append a
   |                      record to history)

.. _verbose:

   .. rubric:: verbose

   | Write history to logger if mode="list"?
   |                      Subparameter of mode='list'
   |                      Default: True
   |                      Options: True|False

.. _origin:

   .. rubric:: origin

   | Origin of appended message. 
   |                      Subparameter of mode='append'
   |                      Default: 'imhistory'
   | 
   |                      The user can specify any string. This string will
   |                      appear as a tag at the start of the appended line
   |                      in the image history. Only used for mode="append".

.. _message:

   .. rubric:: message

   | Message to append. 
   |                      Subparameter of mode='append'
   |                      Default: none
   | 
   |                      Only used of mode="append".


    """
    pass
