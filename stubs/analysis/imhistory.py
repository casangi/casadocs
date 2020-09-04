#
# stub function definition file for docstring parsing
#

def imhistory(imagename, mode='list', verbose=True, origin='imhistory', message=''):
    r"""
Retrieve and modify image history

Parameters
   - **imagename** (string) - Name of the input spectral line image [1]_
   - **mode** (string='list') - Mode to run in, "list" to retrieve history, "append" to append a record to history. [2]_

      .. raw:: html

         <details><summary><i> mode = list </i></summary>

      - **verbose** (bool=True) - Write history to logger if mode="list"? [3]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = append </i></summary>

      - **origin** (string='imhistory') - Origin of appended message. Only used for mode="append". [4]_
      - **message** (string='') - Message to append. Only used of mode="append". [5]_

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

.. [1] 
   **imagename** (string)
      | Name of the input (CASA or FITS) image
      |                      Default: none
      | 
      |                         Example: imagename='ngc5921.im'
.. [2] 
   **mode** (string='list')
      | Operating mode.
      |                      Default: 'list' (retrieve history)
      |                      Options: 'list|append' ('append' to append a
      |                      record to history)
.. [3] 
   **verbose** (bool=True)
      | Write history to logger if mode="list"?
      |                      Subparameter of mode='list'
      |                      Default: True
      |                      Options: True|False
.. [4] 
   **origin** (string='imhistory')
      | Origin of appended message. 
      |                      Subparameter of mode='append'
      |                      Default: 'imhistory'
      | 
      |                      The user can specify any string. This string will
      |                      appear as a tag at the start of the appended line
      |                      in the image history. Only used for mode="append".
.. [5] 
   **message** (string='')
      | Message to append. 
      |                      Subparameter of mode='append'
      |                      Default: none
      | 
      |                      Only used of mode="append".

    """
    pass
