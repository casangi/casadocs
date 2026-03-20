

.. _Description:

Description

This task retrieves the antenna positions for an ALMA Execution Block
via the web service Antenna Position Endpoint in the Uncertainties
database (\https://asa.alma.cl/uncertainties-service/uncertainties/versions/last/measurements/casa/),
which runs on an ALMA JAO hosted server. For a basic
run, the user must specify the outfile and the asdm, using the default
values for the other parameters. The antenna positions stored in the output
file can then be read by gencal so that the data reduction of the observation
can use the most up to date antenna positions. The web service is
described
`at this location <https://confluence.alma.cl/pages/viewpage.action?spaceKey=ICTDEVOPS&title=Antennas+Uncertainties+-+GENCAL+Endpoint+Implementation+2025>`__.

The input parameters are discussed in detail below.

The format of the returned file is a two element dictionary encoded in json. The
two keys of this dictionary are "data" and "metadata". The value associated with
the "data" key is a dictionary that contains antenna names as keys, with each
value being a three element list of x, y, and z ITRF coordinates. The value
associated with the "metadata" key is a dictionary containing various, possibly
useful metadata that describe the task and/or were used when the task was run. The
following code may be used to load these data structures into python variables.
    
    ::
        
        import ast, json
        ...
        with open("outfile.json", "r") as f:
            res_dict = json.load(f)
            antpos_dict = res_dict["data"]
            metadata_dict = res_dict["metadata"]

The metadata dictionary will include a "product_code" key which will have the
value "antposalma" to indicate the type of data product contained in the file.


.. _Examples:

Examples
   Get antenna positions which have positions with a signal-to-noise ratio
   greater than 5.
   
   ::
   
      getantposalma(
          outfile='my_ant_pos.json', asdm='valid ASDM name here', snr=5,
          hosts=['tbd1.alma.cl', 'tbd2.alma.cl'], firstintegration=True
     )
   

.. _Development:

Development
   No additional development details
