Parameters
==========

.. container:: documentDescription description

   task parameters

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               vis : string

            Name of measurement set

Example

.. container:: param

   .. container:: parameters2

      selectdata : bool = True

   Enable data selection parameters

Example

.. container:: param

   .. container:: parameters2

      field : string

   Selection based on field names or field index numbers. Default is
   all.

Example

"0~2", or "3C286"

.. container:: param

   .. container:: parameters2

      spw : string

   Selection based on spectral windows:channels. Default is all.

Example

"3"

.. container:: param

   .. container:: parameters2

      intent : string

   Selection based on intents. Default is all.

Example

"my_intent"

.. container:: param

   .. container:: parameters2

      array : string

   Selection based on array IDs. Default is all.

Example

"1"

.. container:: param

   .. container:: parameters2

      observation : string

   Selection based on observation IDs. Default is all.

Example

"1"

.. container:: param

   .. container:: parameters2

      scan : string

   Select data by scan numbers.

Example

"5"

.. container:: param

   .. container:: parameters2

      combine : string

   Ignore changes in these columns (scan, field, and/or state) when
   aggregating samples to compute weights. The value "corr" is also
   supported to aggregate samples across correlations.

Example

"scan,field"

.. container:: param

   .. container:: parameters2

      timebin : string int = 1

   Length for binning in time to determine statistics. Can either be
   integer to be multiplied by the representative integration time, a
   quantity (string) in time units

Example

5 or "100s"

.. container:: param

   .. container:: parameters2

      slidetimebin : bool = False

   Use a sliding window for time binning, as opposed to time block
   processing?

Example

True

.. container:: param

   .. container:: parameters2

      chanbin : string int = spw

   Channel bin width for computing weights. Can either be integer, in
   which case it is interpreted as number of channels to include in each
   bin, or a string "spw" or quantity with frequency units.

Example

5 or "1.5MHz"

.. container:: param

   .. container:: parameters2

      minsamp : int = 2

   Minimum number of unflagged visibilities required for computing
   weights in a sample. Must be >= 2.

Example

10

.. container:: param

   .. container:: parameters2

      statalg : string = classic

   Statistics algorithm to use for computing variances. Supported values
   are "chauvenet", "classic", "fit-half", and "hinges-fences". Minimum
   match is supported, although the full string must be specified for
   the subparameters to appear in the inputs list.

Example

"cl", "ch", "f", or "h"

.. container:: param

   .. container:: parameters2

      fence : double = -1

   Fence value for statalg="hinges-fences". A negative value means use
   the entire data set (ie default to the "classic" algorithm). Ignored
   if statalg is not "hinges-fences".

Example

0.2

.. container:: param

   .. container:: parameters2

      center : string = mean

   Center to use for statalg="fit-half". Valid choices are "mean",
   "median", and "zero". Ignored if statalg is not "fit-half".

Example

"mean", "median", or "zero"

.. container:: param

   .. container:: parameters2

      lside : bool = True

   For statalg="fit-half", real data are <=; center? If false, real data
   are >= center. Ignored if statalg is not "fit-half".

Example

True

.. container:: param

   .. container:: parameters2

      zscore : double = -1

   For statalg="chauvenet", this is the target maximum number of
   standard deviations data may have to be included. If negative, use
   Chauvenet\'s criterion. Ignored if statalg is not "chauvenet".

Example

3.5

.. container:: param

   .. container:: parameters2

      maxiter : int = -1

   For statalg="chauvenet", this is the maximum number of iterations to
   attempt. Iterating will stop when either this limit is reached, or
   the zscore criterion is met. If negative, iterate until the zscore
   criterion is met. Ignored if statalg is not "chauvenet".

Example

10

.. container:: param

   .. container:: parameters2

      fitspw : string

   Channels to include in the computation of weights. Specified as an MS
   select channel selection string.

Example

"0:5~30"

.. container:: param

   .. container:: parameters2

      excludechans : bool = False

   If True: invert the channel selection in fitspw and exclude the
   fitspw selection from the computation of the weights.

Example

True

.. container:: param

   .. container:: parameters2

      wtrange : doubleArray

   Range of acceptable weights. Data with weights outside this range
   will be flagged. Empty array (default) means all weights are good.

Example

[0.1, 10]

.. container:: param

   .. container:: parameters2

      flagbackup : bool = True

   Back up the state of flags before the run?

Example

True, False

.. container:: param

   .. container:: parameters2

      preview : bool = False

   Preview mode. If True, no data is changed, although the amount of
   data that would have been flagged is reported.

Example

True or False

.. container:: param

   .. container:: parameters2

      datacolumn : string = corrected

   Data column to use to compute weights. Supported values are "data",
   "corrected", "residual", and "residual_data" (case insensitive,
   minimum match supported).

Example

"data" or "corrected"

.. container:: section
   :name: viewlet-below-content-body
