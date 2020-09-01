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
