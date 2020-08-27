#
# stub function definition file for docstring parsing
#

def imhistory(imagename, mode='list', verbose=True, origin='imhistory', message=''):
    """
Retrieve and modify image history

| Retrieve and modify image history.
|
|This task provides access to the logtable of an image, where generally
|history information is stored. Two operation modes are supported. When
|mode="list", the history messages are returned as an array of
|strings. If verbose=True, this information is also written to the
|logger. When mode="append", a specified message (along with its
|specified origin) are appended to the logtable and True is returned if
|successful.

Parameters
----------
imagename : string
   Name of the input spectral line image
mode : string
   Mode to run in, "list" to retrieve history, "append" to append a record to history.

Other Parameters
----------
verbose : bool
   Write history to logger if mode="list"?
origin : string
   Origin of appended message. Only used for mode="append".
message : string
   Message to append. Only used of mode="append".

Notes
-----





   imhistory task: Retrieve and modify image history



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

    """
    pass
