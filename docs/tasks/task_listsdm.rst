

.. _Description:

Description
   Prints observational information from an SDM directory to the CASA logger, returning a dictionary keyed by scan.

   The listsdm task reads SDM XML tables, processes the observation information contained therein, and prints this
   information to the CASA log. It will also return a dictionary keyed on scan number. The dictionary contains the
   following information:

   +---------------------------+-----------------------------------------+
   | **Name**                  | **Description**                         |
   +---------------------------+-----------------------------------------+
   | 'baseband'                | list of baseband name(s)                |
   +---------------------------+-----------------------------------------+
   |'chanwidth'                | list of channel widths (Hz)             |
   +---------------------------+-----------------------------------------+
   | 'end'                     | observation end time (UTC)              |
   +---------------------------+-----------------------------------------+
   | 'field'                   | field ID                                |
   +---------------------------+-----------------------------------------+
   | 'intent'                  | scan intent(s)                          |
   +---------------------------+-----------------------------------------+
   | 'nchan'                   | list of number of channels              |
   +---------------------------+-----------------------------------------+
   | 'nsubs'                   | number of subscans                      |
   +---------------------------+-----------------------------------------+
   | 'reffreq'                 | list of reference frequencies (Hz)      |
   +---------------------------+-----------------------------------------+
   | 'source                   | source name                             |
   +---------------------------+-----------------------------------------+
   | 'spws'                    | list of spectral windows                |
   +---------------------------+-----------------------------------------+
   | 'start'                   | observation start time (UTC)            |
   +---------------------------+-----------------------------------------+
   | 'timerange'               | start time - end time range (UTC)       |
   +---------------------------+-----------------------------------------+


.. _Examples:

Examples
   To print information about the requested SDM to the CASA logger:

   ::

      listsdm(sdm='Example_sb1382796_2_000.55368.51883247685.sdm')


.. _Development:

Development
   No additional development details
