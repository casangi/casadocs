.. container::
   :name: viewlet-above-content-title

Parameters
==========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task accum parameters

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               vis : string

            Name of input visibility file Default: none Example:
            vis='ngc5921.ms'

Example

.. container:: param

   .. container:: parameters2

      tablein : string

   Input cumulative calibration table Default: '' (none) On first
   execution of accum, tablein='' and accumtime is used to generate
   tablein with the specified time gridding.

Example

.. container:: param

   .. container:: parameters2

      incrtable : string

   The calibration data to be interpolated onto the tablein file.
   Default: '' (must be specified)

Example

.. container:: param

   .. container:: parameters2

      caltable : string

   The output cumulative calibration table Default: '' (use tablein as
   the output file)

Example

.. container:: param

   .. container:: parameters2

      field : stringArray

   Select field using field id(s) or field name(s) Default: '' --> all
   fields Use 'go listobs' to obtain the list id's or names. If field
   string is a non-negative integer, it is assumed a field index,
   otherwise, it is assumed a field name. Examples: field='0~2'; field
   ids 0,1,2 field='0,4,5~7'; field ids 0,4,5,6,7 field='3C286,3C295';
   field named 3C286 and 3C295 field = '3,4C*'; field id 3, all names
   starting with 4C

Example

.. container:: param

   .. container:: parameters2

      calfield : stringArray

   Select field(s) from incrtable to process. Default: '' (all fields)

Example

.. container:: param

   .. container:: parameters2

      interp : string = linear

   Interpolation type (in time[,freq]) to use for each gaintable.
   Default: '' ('linear,linear' for all gaintable(s)) Options: Time:
   'nearest', 'linear' Freq: 'nearest', 'linear', 'cubic', 'spline' \*
   When frequency interpolation is relevant (B, Df, Xf), separate
   time-dependent and freq-dependent interp types with a comma (freq
   \_after\_ the comma). \* Specifications for frequency are ignored
   when the calibration table has no channel-dependence. \*
   Time-dependent interp options ending in 'PD' enable a "phase delay"
   correction per spw for non-channel-dependent calibration types. \*
   For multi-obsId datasets, 'perobs' can be appended to the
   time-dependent interpolation specification to enforce obsId
   boundaries when interpolating in time. Examples: interp='nearest' (in
   time, freq-dep will be linear, if relevant) interp='linear,cubic'
   (linear in time, cubic in freq) interp='linearperobs,spline' (linear
   in time per obsId, spline in freq) interp=',spline' (spline in freq;
   linear in time by default) interp=['nearest,spline','linear'] (for
   multiple gaintables)

Example

.. container:: param

   .. container:: parameters2

      accumtime : double int = 1.0

   The time separation when making tablein. Subparameter of tablein
   Default: 1.0 (1 second) Note: This time should not be less than the
   visibility sampling time, but should be less than about 30% of a
   typical scan length.

Example

.. container:: param

   .. container:: parameters2

      spwmap : intArray = -1

   Spectral windows combinations to form for gaintable(s) Default: []
   (apply solutions from each spw to that spw only) Examples:
   spwmap=[0,0,1,1] means apply the caltable solutions from spw = 0 to
   the spw 0,1 and spw 1 to spw 2,3. spwmap=[[0,0,1,1],[0,1,0,1]] (for
   multiple gaintables)

Example

.. container:: section
   :name: viewlet-below-content-body
