#
# stub function definition file for docstring parsing
#

def conjugatevis(vis, spwlist='""', outputvis='', overwrite=False):
    r"""
Change the sign of the phases in all visibility columns.

Parameters
   - **vis** (string) - Name of input visibility file [1]_
   - **spwlist** (variant='""') - Spectral window selection [2]_
   - **outputvis** (string='') - Name of output visibility file [3]_
   - **overwrite** (bool=False) - Overwrite the outputvis if it exists? [4]_


Description
   This task changes the sign of the phases in all visibility
   columns, thus creating the complex conjugate values. A complex
   number and its complex conjugate have equal real parts and
   imaginary parts that are equal in magnitude but opposite in sign.

   

   .. rubric:: Parameter descriptions
      

   .. rubric:: vis
      

   Name of input visibility file. For example: *vis='filename.ms'*

   .. rubric:: spwlist
      

   Selects spectral window(s). For example: *spw=[1,2]*. By default,
   all spws will be conjugated.

   .. rubric:: outputvis
      

   Name of output visibility file. Default:
   'conjugatedvis_filename.ms'

   .. rubric:: overwrite
      

   Overwrites the *outputvis* if it exists. Default=False




Details
   Explanation of each parameter

.. [1] 
   **vis** (string)
      | Name of input visibility file
      |                      Default: none
      | 
      |                         Example: vis='ngc5921.ms'
.. [2] 
   **spwlist** (variant='""')
      | Spectral window selection
      |                      Default:[] (all spws will be conjugated)
      | 
      |                         Example: spw=[1,2]
.. [3] 
   **outputvis** (string='')
      | Name of output visibility file
      |                      Default: 'conjugated_'+vis
      | 
      |                         Example: outputvis='conjugated.ms'
.. [4] 
   **overwrite** (bool=False)
      | Overwrite the outputvis if it exists?
      |                      Default: False
      |                      Options: False|True

    """
    pass
