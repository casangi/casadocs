.. container::
   :name: viewlet-above-content-title

accum
=====

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task accum description

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Summary
         :name: summary

      .. container:: alert-box

         Please note: The **accum** task has been designated for
         deprecation, and will be removed in CASA 5.8/6.2.

       

      **accum** will interpolate and extrapolate a temporal calibration
      table onto a new table that has a regularly-space time grid. The
      first run of **accum** defines the time grid and fills this table
      with the results from the input table. Subsequent use of **accum**
      will combine additional calibration tables onto the same grid of
      the initial **accum** table to obtain an output **accum** table. 

       

      .. rubric:: Parameter descriptions
         :name: title0

      .. rubric:: *vis*
         :name: vis

      Name of input MeasurementSet. No default.

      .. rubric:: *tablein*
         :name: tablein

      Input cumulative calibration table. Default: ''* * means none. On
      first execution of **accum**, *tablein=''*  and *accumtime* is
      used to generate *tablein* with the specified time gridding.

      .. rubric:: *tablein* expandable parameters
         :name: tablein-expandable-parameters

      .. rubric:: *accumtime*
         :name: accumtime

      The time separation when making *tablein*. Default: 1.0\ * * (1
      second). This time should not be less than the visibiility
      sampling time, but should be less than about 30% of a typical scan
      length.

       

      .. rubric:: *incrtable*
         :name: incrtable

      The calibration data to be interpolated onto the *tablein* file.
      Default: ''. Must be specified.

      .. rubric:: *caltable *
         :name: caltable

      The output cumulative calibration file. Default: ''  means use
      *tablein* as the output file.

      .. rubric:: *field*
         :name: field

      Standard field ID or name selection for *tablein* to process.
      Default: '' = all fields. (See `Data Selection in a
      MeasurementSet <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__ for
      more details.)

      .. rubric:: *calfield*
         :name: calfield

      Select field(s) from *incrtable* to process. Default: '' = all
      fields. (See `Data Selection in a
      MeasurementSet <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__ for
      more details.) 

      .. rubric:: *interp*
         :name: interp

      Interpolation type (in time,freq) to use for each gaintable. When
      frequency interpolation is relevant (B, Df, Xf), separate
      time-dependent and freq-dependent *interp* types with a comma
      (freq *interp* type should be after the comma). Specifications for
      frequency are ignored when the calibration table has no
      channel-dependence. Time-dependent interp options ending in 'PD'
      enable a "phase delay" correction per spw for
      non-channel-dependent calibration types. For multi-obsId datasets,
      'perobs' can be appended to the time-dependent interpolation
      specification to enforce obs ID boundaries when interpolating in
      time. Options: Time - 'nearest'*,* 'linear'*;* Freq - 'nearest'*,*
      'linear'*,* 'cubic'*,* 'spline'*. D*\ efault: 'linear,linear' for
      all gaintable(s). See also: `Solving for
      Calibration <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration/solving-for-calibration>`__.

      .. rubric:: *spwmap*
         :name: spwmap

      Spectral windows combinations to form gaintable(s). Default: [ ]
      (apply solutions from each spw to that spw only). See
      also: `Solving for
      Calibration <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration/solving-for-calibration>`__.

       

.. container:: section
   :name: viewlet-below-content-body

.. toctree::
   :hidden:
   :maxdepth: 3

   task_accum/about
   task_accum/examples
