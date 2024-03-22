imhistory -- Retrieve and modify image history -- analysis task
=======================================

Description
---------------------------------------

Retrieve and modify image history.

This task provides access to the logtable of an image, where generally
history information is stored. Two operation modes are supported. When
mode="list", the history messages are returned as an array of
strings. If verbose=True, this information is also written to the
logger. When mode="append", a specified message (along with its
specified origin) are appended to the logtable and True is returned if
successful.



Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - imagename
     - :code:`''`
     - Name of the input spectral line image
   * - mode
     - :code:`'list'`
     - Mode to run in, "list" to retrieve history, "append" to append a record to history.
   * - verbose
     - :code:`True`
     - Write history to logger if mode="list"?
   * - origin
     - :code:`'imhistory'`
     - Origin of appended message. Only used for mode="append".
   * - message
     - :code:`''`
     - Message to append. Only used of mode="append".


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Name of the input (CASA or FITS) image
                     Default: none

                        Example: imagename='ngc5921.im'



mode
---------------------------------------

:code:`'list'`

Operating mode.
                     Default: 'list' (retrieve history)
                     Options: 'list|append' ('append' to append a
                     record to history)



verbose
---------------------------------------

:code:`True`

Write history to logger if mode="list"?
                     Subparameter of mode='list'
                     Default: True
                     Options: True|False



origin
---------------------------------------

:code:`'imhistory'`

Origin of appended message. 
                     Subparameter of mode='append'
                     Default: 'imhistory'

                     The user can specify any string. This string will
                     appear as a tag at the start of the appended line
                     in the image history. Only used for mode="append".



message
---------------------------------------

:code:`''`

Message to append. 
                     Subparameter of mode='append'
                     Default: none

                     Only used of mode="append".





