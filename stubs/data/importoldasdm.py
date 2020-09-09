#
# stub function definition file for docstring parsing
#

def importoldasdm(asdm, corr_mode='all', srt='all', time_sampling='all', ocorr_mode='co', compression=False):
    r"""
Convert an ALMA Science Data Model observation into a CASA visibility file

Parameters
   - asdm_ (string)
   - corr_mode_ (string='all')
   - srt_ (string='all')
   - time_sampling_ (string='all')
   - ocorr_mode_ (string='co')
   - compression_ (bool=False)




.. _asdm:

asdm (string)
   | Name of input asdm directory (on disk)

.. _corr_mode:

corr_mode (string='all')
   | specifies the correlation mode to be considered on input. A quoted string containing a sequence of ao co ac all separated by whitespaces is expected

.. _srt:

srt (string='all')
   | specifies the spectral resolution type to be considered on input. A quoted string containing a sequence of fr ca bw all separated by whitespaces is expected

.. _time_sampling:

time_sampling (string='all')
   | specifies the time sampling (INTEGRATION and/or SUBINTEGRATION)  to be considered on input. A quoted string containing a sequence of i si all separated by whitespaces is expected

.. _ocorr_mode:

ocorr_mode (string='co')
   | output data for correlation mode AUTO_ONLY (ao) or CROSS_ONLY (co) or CROSS_AND_AUTO (ca)

.. _compression:

compression (bool=False)
   | Flag for turning on data compression


    """
    pass
