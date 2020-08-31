#
# stub function definition file for docstring parsing
#

def conjugatevis(vis, spwlist='""', outputvis='', overwrite=False):
    r"""
Change the sign of the phases in all visibility columns.

Parameters
   - **vis** (string) - Name of input visibility file
   - **spwlist** (variant='""') - Spectral window selection
   - **outputvis** (string='') - Name of output visibility file
   - **overwrite** (bool=False) - Overwrite the outputvis if it exists?


Description
      This task changes the sign of the phases in all visibility
      columns, thus creating the complex conjugate values. A complex
      number and its complex conjugate have equal real parts and
      imaginary parts that are equal in magnitude but opposite in sign.

       

      .. rubric:: Parameter descriptions
         :name: parameter-descriptions

      .. rubric:: vis
         :name: vis

      Name of input visibility file. For example: *vis='filename.ms'*

      .. rubric:: spwlist
         :name: spwlist

      Selects spectral window(s). For example: *spw=[1,2]*. By default,
      all spws will be conjugated.

      .. rubric:: outputvis
         :name: outputvis

      Name of output visibility file. Default:
      'conjugatedvis_filename.ms'

      .. rubric:: overwrite
         :name: overwrite

      Overwrites the *outputvis* if it exists. Default=False

    """
    pass
