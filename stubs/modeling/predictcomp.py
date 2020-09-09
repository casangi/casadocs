#
# stub function definition file for docstring parsing
#

def predictcomp(objname='', standard='Butler-JPL-Horizons 2010', epoch='', minfreq='', maxfreq='', nfreqs=2, prefix='', antennalist='', showplot=False, savefig='', symb='.', include0amp=False, include0bl=False, blunit='', showbl0flux=False):
    r"""
Make a component list for a known calibrator

Parameters
   - objname_ (string='') - Object name
   - standard_ (string='Butler-JPL-Horizons 2010') - Flux density standard
   - epoch_ (string='') - Epoch
   - minfreq_ (string='') - Minimum frequency
   - maxfreq_ (string='') - Maximum frequency
   - nfreqs_ (int=2) - Number of frequencies
   - prefix_ (string='') - Prefix for the component list directory name.
   - antennalist_ (string='') - Plot for this configuration

      .. raw:: html

         <details><summary><i> antennalist != '' </i></summary>

      - showplot_ (bool=False) - Plot S vs |u| to the screen?
      - savefig_ (string='') - Save a plot of S vs |u| to this filename
      - symb_ (string='.') - A matplotlib plot symbol code
      - include0amp_ (bool=False) - Force the amplitude axis to start at 0?
      - include0bl_ (bool=False) - Force the baseline axis to start at 0?
      - blunit_ (string='') - unit of the baseline axis
      - showbl0flux_ (bool=False) - Print the zero baseline flux ?

      .. raw:: html

         </details>
   - symb_ (string='.') - A matplotlib plot symbol code


Description
   This task makes a flux model as a component list from one of the
   flux calibrator standards used by thesetjy task. It also returns
   a Python dictionary of the predicted model and optionally plots
   the predicted visibility amplitudes versus uv-distance when the
   array configuration information is specified. It uses the same
   common prediction code as setjy but without the need for the
   actual visibility data. This task is useful for cross checking
   what setjy would set for model visilibilities or for finding a
   predicted flux density for a calibrator at a particular epoch,
   especially when the flux calibrator is a Solar System object.

   The following are the main keys of the returned dictionary (or
   False on error):

   -  'antennalist' - array configuration file
   -  'savedfig' - output file name for a plot
   -  'spectrum' - frequency setup information
   -  'clist' - output component list name
   -  'riseset' - times of rise and set of the object
   -  'standard' - flux standard used
   -  'shape' - model shape and position of the object
   -  'epoch' - epoch used
   -  'objname' - object name
   -  'freqs (GHz)' - frequencies
   -  'amps' - list of predicted visibility amplitudes
   -  'baselines' - list of baselines
   -  'blunit' - unit
   -  'azel' - AZ-El direction

   

   .. rubric:: Parameter descriptions
      

   .. rubric:: *objname*
      

   The object name as recognized by **setjy**. If the object
   specified is not visible from the specified telescope, an error
   will be thrown to this effect.

   .. rubric:: *standard*
      

   Sets the flux density model standard from **setjy**, namely
   Perley-Taylor 99, Baars, Perley 90, Perley-Taylor 95,
   Butler-JPL-Horizons 2010, Butler-JPL-Horizons 2012.

   .. rubric:: *epoch*
      

   Sets the time that **predictcomp** uses,which is only relevant
   for Solar Object standards, using a standard CASA date/time format
   (e.g., '2018-12-31/5:34:12').

   .. rubric:: *minfreq*
      

   Sets theminimum predicted frequency of the model. Units must be
   given. Examples: *minfreq='230GHz'*

   .. rubric:: *maxfreq*
      

   Sets the maximum predicted frequency of the model. Units must be
   given. Examples: *maxfreq='265GHz'*

   .. rubric:: *nfreqs*
      

   Sets the frequency interval for the predicted visibilities.
   Examples: *minfreq='230GHz' maxfreqs='265GHz' nfreqs=5*, the
   predicted visibilities will be determined for frequencies of equal
   interval determined by the equation
   :math:`(maxfreqs - minfreqs) / nfreqs` (in this case, for
   frequencies 230, 239, 248, 256, and 265 GHz).

   .. rubric:: *prefix*
      

   The component list will be saved to '<prefix> +
   <objname>_spw0_<minfreq><epoch>.cl'. If a component list of the
   same name already exists, **predictcomp** will remove the previous
   version. Default: ' ' which will create the component list name
   sans the prefix. Examples: *prefix='Bands3to7_'*, which could
   produce 'Bands3to7_Uranus_spw0_100GHz55877d.cl' (depending on the
   other parameters).

   .. rubric:: *antennalist*
      

   When *antennalist* is given a valid array configuration file, the
   task predicts and plots (if set) the visibility amplitudes for the
   array configuration. The search path is: .:casa['dirs']['data'] +
   '/alma/simmos/'. Default: '', None just makes a component list.
   Examples: *antennalist='alma.cycle0.extended.cfg'*

   .. rubric:: antennalist expandable parameters
      

   .. rubric:: *showplot*
      

   Whether or not to show a plot of the visibility amplitudes vs. uv
   distance on the screen.

   .. rubric:: *savefig*
      

   Filename for saving a plot of the amplitude vs. uv distances.

   .. rubric:: *symb*
      

   One of matplotlib's codes for plot symbols: .:,o^v<>s+xDd234hH|_.
   Default: '.'

   .. rubric:: *include0amp*
      

   Force the amplitude axis to start at 0. Default: False

   .. rubric:: *include0bl*
      

   Force the baseline axis to start at 0. Default: False

   .. rubric:: *blunit*
      

   Unit of the baseline axis ('' or 'klambda'). Default: ' ' = use a
   unit in the data

   .. rubric:: *showbl0flux*
      

   Print the zero baseline flux. Default: False


.. _objname:

objname (string='')
   | Object name

.. _standard:

standard (string='Butler-JPL-Horizons 2010')
   | Flux density standard

.. _epoch:

epoch (string='')
   | Epoch

.. _minfreq:

minfreq (string='')
   | Minimum frequency

.. _maxfreq:

maxfreq (string='')
   | Maximum frequency

.. _nfreqs:

nfreqs (int=2)
   | Number of frequencies

.. _prefix:

prefix (string='')
   | Prefix for the component list directory name.

.. _antennalist:

antennalist (string='')
   | Plot for this configuration

.. _showplot:

showplot (bool=False)
   | Plot S vs |u| to the screen?

.. _savefig:

savefig (string='')
   | Save a plot of S vs |u| to this filename

.. _symb:

symb (string='.')
   | A matplotlib plot symbol code

.. _include0amp:

include0amp (bool=False)
   | Force the amplitude axis to start at 0?

.. _include0bl:

include0bl (bool=False)
   | Force the baseline axis to start at 0?

.. _blunit:

blunit (string='')
   | unit of the baseline axis

.. _showbl0flux:

showbl0flux (bool=False)
   | Print the zero baseline flux ?


    """
    pass
