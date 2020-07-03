.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Description
===========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task description

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. container:: alert-box

         **WARNING**\ *:* The task **oldstatwt** is identical to the
         task statwt in previous CASA versions, given that the current
         statwt underwent significant development for CASA 5.4.

      The WEIGHT and SIGMA columns of measurement sets are often set to
      arbitrary values (e.g., 1), or theoretically estimated from poorly
      known antenna and receiver properties. Many tasks (e.g.,
      **clean**) are insensitive to an overall scale error in WEIGHT,
      but are affected by errors in the relative weights between
      visibilities. Other tasks, such as **uvmodelfit**, or any task
      which depends on theoretical estimates of the noise, require
      (reasonably) correct weights and sigmas. **oldstatwt** empirically
      measures the visibility scatter (typically as a function of time,
      antenna, and/or baseline) and uses that to set WEIGHT and SIGMA.
      It is important that all necessary calibrations are applied to the
      data prior to running this task for correct determination of
      weights and sigmas.

      .. container:: info-box

         **NOTE**: Some of the parameters (*byantenna*, *sepacs*,
         *fitcorr*, and *timebin*) are not yet fully implemented.

       

      .. rubric:: Parameter descriptions
         :name: parameter-descriptions

      .. rubric:: *vis*
         :name: vis

      Name of input visibility file. Default: none. Examples:
      *vis='ngc5921.ms'*

      .. rubric:: *dorms*
         :name: dorms

      Estimate the scatter using RMS instead of the standard deviation.

      Ideally the visibilities used to estimate the scatter, as selected
      by *fitspw* and *fitcorr*, should be pure noise. If you know for
      certain that they are, then setting dorms to True will give the
      best result. Otherwise, use False (standard sample standard
      deviation). More robust scatter estimates like the interquartile
      range or median absolute deviation from the median are not offered
      because they require sorting by value, which is not possible for
      complex numbers. Default: False.

      .. rubric:: *byantenna*
         :name: byantenna

      Assume that the noise is factorable by antenna (feed). If False,
      treat it separately for each baseline (recommended if there is
      strong signal). Default: False (**\* *byantenna=True* is not yet
      implemented)

      .. rubric:: *byantenna=True* expandable parameters
         :name: byantennatrue-expandable-parameters

      .. rubric:: *sepacs*
         :name: sepacs

      If solving by antenna, treat autocorrelations separately.
      (Acknowledge that what autocorrelations "see" is very different
      from what crosscorrelations see.) Default: True (**\* not yet
      implemented).

       

      .. rubric:: *fitspw*
         :name: fitspw

      The (ideally) signal-free spectral window:channels to estimate the
      scatter from. Default: '' (All).

      .. rubric:: *fitcorr*
         :name: fitcorr

      The (ideally) signal-free correlations to estimate the scatter
      from. Default: '' (All) (**\* not yet implemented)

      .. rubric:: *combine*
         :name: combine

      Let samples span multiple spws, corrs, scans, and/or states.
      Examples:

      -  *combine = 'spw'*: Recommended when a line spans an entire spw
         - set *fitspw* to the neighboring spws and apply their weight
         to the line spw(s). However, the effect of the line signal per
         visibility may be relatively harmless compared to the noise
         difference between spws.
      -  *combine = 'scan'*: Can be useful when the scan number goes up
         with each integration, as in many WSRT MSes.
      -  *combine = ['scan', 'spw']*: disregard scan and spw numbers
         when gathering samples.
      -  *combine = 'spw,scan'*: Same as above.

      Default: '' (None).

      .. rubric:: *timebin*
         :name: timebin

      Sample interval. Default: '0s' or '-1s' (1 integration at a time).
      Examples: *timebin='30s'*, '10' means '10s' (**\* not yet
      implemented)

      .. rubric:: *minsamp*
         :name: minsamp

      Minimum number of unflagged visibilities for estimating the
      scatter. Selected visibilities for which the weight cannot be
      estimated will be flagged. Note that *minsamp* is effectively at
      least 2 if *dorms* is False, and 1 if it is True.

      .. rubric:: *field*
         :name: field

      Select fields in mosaic. Use field id(s) or field name(s). [go
      listobs to obtain the list id's or names] Default: '' = all
      fields. If field string is a non-negative integer, it is assumed
      to be a field index otherwise, it is assumed to be a field name.
      Examples: *field='0~2'*, field ids 0,1,2; *field='0,4,5~7'*, field
      ids 0,4,5,6,7; *field='3C286,3C295'*, field named 3C286 and 3C295;
      *field = '3,4C*'*, field id 3 and all names starting with 4C.

      .. rubric:: *spw*
         :name: spw

      Select spectral window/channels. Default: '' => all spectral
      windows and channels. Examples: *spw='0~2,4'*, spectral windows
      0,1,2,4 (all channels); *spw='0:5~61'*, spw 0, channels 5 to 61;
      *spw='<2'*, spectral windows less than 2 (i.e. 0,1);
      *spw='0,10,3:3~45'*, spw 0,10 all channels, spw 3, channels 3 to
      45; *spw='0~2:2~6'*; spw 0,1,2 with channels 2 through 6 in each;
      *spw='0:0~10;15~60'*; spectral window 0 with channels 0-10,15-60;
      *spw='0:0~10,1:20~30,2:1;2;3'*; spw 0, channels 0-10, spw 1,
      channels 20-30, and spw 2, channels, 1,2 and 3.

      .. rubric:: *antenna*
         :name: antenna

      Select data based on antenna/baseline. Default: '' (all). If
      antenna string is a non-negative integer, it is assumed to be an
      antenna index, otherwise, it is considered an antenna name.
      Examples: *antenna='5&6'*; baseline between antenna index 5 and
      index 6; *antenna='VA05&VA06'*, baseline between VLA antenna 5 and
      6; *antenna='5&6;7&8'*, baselines 5-6 and 7-8; *antenna='5'*, all
      baselines with antenna index 5; *antenna='05'*, all baselines with
      antenna number 05 (VLA old name); *antenna='5,6,9'*, all baselines
      with antennas 5,6,9 index numbers.

      .. rubric:: *timerange*
         :name: timerange

      Select data based on time range. Default: '' (all). Examples:
      *timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'*;

      .. container:: info-box

         **NOTE**: if YYYY/MM/DD is missing date defaults to first day
         in data set.

      *timerange='09:14:0~09:54:0'* picks 40 min on first day;
      *timerange='25:00:00~27:30:00'* picks 1 hr to 3 hr 30min on NEXT
      day; *timerange='09:44:00'* pick data within one integration of
      time; *timerange='>10:24:00'* data after this time.

      .. rubric:: *scan*
         :name: scan

      Scan number range. Default: '' (all). Examples: *scan='1~5'*.
      Check 'go listobs' to insure the scan numbers are in order.

      .. rubric:: *intent*
         :name: intent

      Select by scan intent (state). Case sensitive. Default: '' = all.
      Examples: *intent = 'CALIBRATE_ATMOSPHERE_REFERENCE'*; *intent =
      'calibrate_atmosphere_reference'*.upper() same as above. Select
      states that include one or both of CALIBRATE_WVR.REFERENCE or
      OBSERVE_TARGET_ON_SOURCE; *intent = 'CALIBRATE_WVR.REFERENCE,
      OBSERVE_TARGET_ON_SOURCE'*

      .. rubric:: *array*
         :name: array

      (Sub)array number range. Default: ''=all.

      .. rubric:: *correlation*
         :name: correlation

      Select correlations, e.g. 'RR, LL' or ['XY', 'YX']. Default ''
      (all).

      .. container:: info-box

         **NOTE**: In CASA v4.5, non-trivial correlation selection has
         been disabled since it was not working correctly, and it is
         likely undesirable to set the weights in a
         correlation-dependent way.

       

      .. rubric:: *observation*
         :name: observation

      Select by observation ID(s). Default: '' = all.

      .. rubric:: *datacolumn*
         :name: datacolumn

      Which data column to calculate the scatter from. Default:
      *datacolumn='corrected'*. Examples: *datacolumn='data'*. Options:
      'data', 'corrected', 'model', 'float_data'

      .. container:: info-box

         **NOTE**: 'corrected' will fall back to DATA if CORRECTED_DATA
         is absent.

       

.. container:: section
   :name: viewlet-below-content-body
