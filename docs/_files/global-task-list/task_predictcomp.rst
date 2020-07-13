predictcomp
===========

.. container:: documentDescription description

   task description

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      This task makes a flux model as a component list from one of the
      flux calibrator standards used by the setjy task. It also returns
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
         :name: parameter-descriptions
         :class: p1

      .. rubric:: *objname*
         :name: objname

      The object name as recognized by **setjy**. If the object
      specified is not visible from the specified telescope, an error
      will be thrown to this effect.

      .. rubric:: *standard*
         :name: standard

      Sets the flux density model standard from **setjy**, namely
      Perley-Taylor 99, Baars, Perley 90, Perley-Taylor 95,
      Butler-JPL-Horizons 2010, Butler-JPL-Horizons 2012.

      .. rubric:: *epoch*
         :name: epoch

      Sets the time that **predictcomp** uses, which is only relevant
      for Solar Object standards, using a standard CASA date/time format
      (e.g., '2018-12-31/5:34:12').

      .. rubric:: *minfreq*
         :name: minfreq

      Sets the minimum predicted frequency of the model. Units must be
      given. Examples: *minfreq='230GHz'*

      .. rubric:: *maxfreq*
         :name: maxfreq

      Sets the maximum predicted frequency of the model. Units must be
      given. Examples: *maxfreq='265GHz'*

      .. rubric:: *nfreqs*
         :name: nfreqs

      Sets the frequency interval for the predicted visibilities.
      Examples: *minfreq='230GHz' maxfreqs='265GHz' nfreqs=5*, the
      predicted visibilities will be determined for frequencies of equal
      interval determined by the equation
      :math:`(maxfreqs - minfreqs) / nfreqs` (in this case, for
      frequencies 230, 239, 248, 256, and 265 GHz).

      .. rubric:: *prefix*
         :name: prefix

      The component list will be saved to '<prefix> +
      <objname>_spw0_<minfreq><epoch>.cl'. If a component list of the
      same name already exists, **predictcomp** will remove the previous
      version. Default: ' ' which will create the component list name
      sans the prefix. Examples: *prefix='Bands3to7_'*, which could
      produce 'Bands3to7_Uranus_spw0_100GHz55877d.cl' (depending on the
      other parameters).

      .. rubric:: *antennalist*
         :name: antennalist

      When *antennalist* is given a valid array configuration file, the
      task predicts and plots (if set) the visibility amplitudes for the
      array configuration. The search path is: .:casa['dirs']['data'] +
      '/alma/simmos/'. Default: '', None just makes a component list.
      Examples: *antennalist='alma.cycle0.extended.cfg'*

      .. rubric:: antennalist expandable parameters
         :name: antennalist-expandable-parameters

      .. rubric:: *showplot*
         :name: showplot

      Whether or not to show a plot of the visibility amplitudes vs. uv
      distance on the screen.

      .. rubric:: *savefig*
         :name: savefig

      Filename for saving a plot of the amplitude vs. uv distances.

      .. rubric:: *symb*
         :name: symb

      One of matplotlib's codes for plot symbols: .:,o^v<>s+xDd234hH|_.
      Default: '.'

      .. rubric:: *include0amp*
         :name: include0amp

      Force the amplitude axis to start at 0. Default: False

      .. rubric:: *include0bl*
         :name: include0bl

      Force the baseline axis to start at 0. Default: False

      .. rubric:: *blunit*
         :name: blunit

      Unit of the baseline axis ('' or 'klambda'). Default: ' ' = use a
      unit in the data

      .. rubric:: *showbl0flux*
         :name: showbl0flux

      Print the zero baseline flux. Default: False

       

.. container:: section
   :name: viewlet-below-content-body

.. toctree::
   :hidden:
   :maxdepth: 3

   task_predictcomp/parameters
   task_predictcomp/changelog
   task_predictcomp/examples
