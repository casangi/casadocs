#
# stub function definition file for docstring parsing
#

def conjugatevis(vis, spwlist='""', outputvis='', overwrite=False):
    r"""
Change the sign of the phases in all visibility columns.

Parameters
   - vis_ (string) - Name of input visibility file
   - spwlist_ (variant='""') - Spectral window selection
   - outputvis_ (string='') - Name of output visibility file
   - overwrite_ (bool=False) - Overwrite the outputvis if it exists?


Description
   This task changes the sign of the phases in all visibility
   columns, thus creating the complex conjugate values. A complex
   number and its complex conjugate have equal real parts and
   imaginary parts that are equal in magnitude but opposite in sign.


.. _vis:

vis (string)
   | Name of input visibility file
   |                      Default: none
   | 
   |                         Example: vis='ngc5921.ms'

.. _spwlist:

spwlist (variant='""')
   | Spectral window selection
   |                      Default:[] (all spws will be conjugated)
   | 
   |                         Example: spw=[1,2]

.. _outputvis:

outputvis (string='')
   | Name of output visibility file
   |                      Default: 'conjugated_'+vis
   | 
   |                         Example: outputvis='conjugated.ms'

.. _overwrite:

overwrite (bool=False)
   | Overwrite the outputvis if it exists?
   |                      Default: False
   |                      Options: False|True


    """
    pass
