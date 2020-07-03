.. container::
   :name: viewlet-above-content-title

Flags and data-averaging
========================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   How flags are treated and propagated when using data average (time or
   channel average).

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      CASA uses common infrastructure to implement data average
      transformations across different tasks. This infrastructure
      follows certain common rules to propagate flags from the original
      data to the averaged data. This page explains the common rules
      that different CASA tasks follow to produce the flags of averaged
      data; in other words, these rules dictate how data averaging
      transformations propagate the flags from the original data to the
      averaged data. 

      These rules apply to `channel
      average <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/uv-manipulation/channel-average>`__
      and `time
      average <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/uv-manipulation/time-average>`__,
      as implemented by

      -  tasks such as **mstransform** and **split**, to output averaged
         MeasurementSets, or
      -  tasks such as **flagdata** and **plotms**, to transform data
         on-the-fly and then modify the flags in the input
         MeasurementSets.

      In short, the rule that CASA follows for the propagation of flags
      from the original input data to the averaged data is a logical
      AND. This is detailed in the next section. The second subsection
      explains how tasks such as flagdata and plotms propagate back the
      averaged flags to the input MeasurementSet.

      In what follows we explain how CASA treats flags and data when
      using data averaging. By the term *data*, we refer to the data
      columns present in a MeasurementSet (DATA, CORRECTED_DATA, etc.).
      The data always have a companion FLAG column, with matching
      dimensions. The data also have other companion columns related to
      weights: WEIGHT, SIGMA, WEIGHT_SPECTRUM, SIGMA_SPECTRUM. The focus
      of this page is on data flags. But data average, and the use of
      the data weights in the average, also plays a role in the
      explanations below. The treatment of data weights in CASA is
      explained in more detail in `Data
      weights <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-weights>`__.

      .. rubric:: Propagation of flags from the original data to the
         averaged data
         :name: propagation-of-flags-from-the-original-data-to-the-averaged-data

      | For a given bin of input data and flags, the averaged flags are
        calculated as the logical "AND" of all the flags in the input
        bin (timebin or chanbin). The averaged flag will be set only if
        all the flags in the input bin are set.
      | Let us first illustrate this with examples. For simplicity we
        consider some examples of channel average.
      | The flags for every data channel are represented by an 'X' (flag
        set) or a 'O' (flag unset). There are 12 channels and we try
        different channel bins:

      ::

         Flags in the input bin  ------------> averaged flags
         ----------------------------------------------------

                                  chanbin=2
         X X X O O X X X X X O X ------------> X O O X X O

                                  chanbin=3
                                 ------------> X O X O

                                  chanbin=4
                                 ------------> O O O

      The implication of this AND rule is that after applying the
      averaging transformation the percentage of data flagged can only
      remain the same or decrease. And it will tend to decrease more as
      the bin size increases. It will also tend to decrease more for
      more sparse patterns of original flags. In an averaged dataset one
      should expect a lower percentage of flags, proportionally to the
      bin size used and the sparseness of the flags of the original
      data.

      For time average the same principle applies, on a per-baseline
      basis, with the only difference that the bins are defined across
      time instead of channels.

      .. rubric:: The AND rule of propagation of flags to the averaged
         data
         :name: the-and-rule-of-propagation-of-flags-to-the-averaged-data

      | The logical "AND" rule can be formulated as follows. Let us
        consider a bin size $n$, and original data $d_i, i=0,... n-1$,
        with associated flags, $f_i$. Every subindex $_i$ corresponds to
        a value of the data column for a given baseline, time and
        channel. As a convention, $f_i = 1$ when the flag is set, and
        $f_i = 0$ when the flag is not set.
      | For every data point produced in the averaged data, $d_{avg}$,
        its flag, $f_{avg}$, is calculated as:
      | $f_{avg} = \\prod_{i=0}^{n-1} f_i$
      | That is, the value of the averaged flag is defined as the
        product of the values of the flags in the input bin.

      .. rubric:: How flags and data are averaged
         :name: how-flags-and-data-are-averaged

      Does the "AND" rule mean that flagged data becomes unflagged via
      averaging? No, this doesn't mean that CASA uses flagged data or
      unsets the flags of the initially flagged data. If any data point
      in the input bin is not flagged, the averaged data point will be
      not flagged. But this does not imply that flagged data is
      propagated to the averaged data. When one or more of the data in
      the input bin are no flagged, only the data that are not flagged
      are used in the average. The flagged data in the original bin are
      excluded from the average. These are the two possible scenarios:

      A) If one or more unflagged data points can be found in the input
      bin, the averaged data will be produced as follows:

      -  averaged data: calculated as the average of the input data
         points that are not flagged.
      -  averaged flag: not set

      B) Only if all the data points in the input bin are flagged, then
      the averaged data will be produced as follows:

      -  averaged data: calculated as the average of all the input data
         in the bin (all flagged).
      -  averaged flag: set

      | To define an equation of data averaging with flags, let us now
        consider the data weights. A bin of $n$ data points $d_i,
        i=0,...n-1$, with flags $f_i$, are averaged into an average data
        point $d_{avg}$ with flag $f_{avg}$. The $d_i$ are the
        visibility data and the $w_i$ are their respective weights. CASA
        calculates the averaged data, $d_{avg}$ as:
      | $d_{avg}= f_{avg} \\times \\sum_{i=0}^{n-1} w_i d_i  +
        (1-f_{avg}) \\times \\sum_{i=0}^{n-1} (1-f_i) w_i d_i =
        \\prod_{i=0}^{n-1} f_i \\times \\sum_{i=0}^{n-1} w_i d_i  + 
        (1-\prod_{i=0}^{n-1} f_i) \\times \\sum_{i=0}^{n-1} (1-f_i) w_i
        d_i $

      There are two terms, and they are mutually exclusive

      -  The first one represents the case where all input data are
         flagged (scenario B above). The output averaged data is flagged
         and the averaged data is calculated from all the input data in
         the bin.
      -  The second term represents the case where some input data are
         not flagged (scenario A). The output averaged data is not
         flagged and the data is calculated as the average of all the
         unflagged input data in the bin.

      | In any case, data that is flagged in the input data is either:
      | a) never propagated or used after the data average (when there
        is other not flagged data in the bin),
      | b) propagated but kept flagged (when all the data in the bin are
        flagged).

      .. rubric:: Writing and (back)propagation of flags from the
         averaged data to the original data (input MeasurementSet)
         :name: writing-and-backpropagation-of-flags-from-the-averaged-data-to-the-original-data-input-measurementset

      | This section concerns tasks such as flagdata or plotms which can
        apply on-the-fly average, either time or frequency, flag and/or
        unflag data, and write the averaged flags back to the original 
        MeasurementSet. These tasks have the additional complexity that
        they need to be able to propagate back to the original
        MeasurementSet flags from averaged data+flags that have been
        transformed on-the-fly. A reverse or backward propagation is
        required to map the averaged flags to the original
        MeasurementSet.
      | These tasks can perform the following sequence of data
        manipulation steps, all in one go:
      | a) Take an input MeasurementSet and apply averaging on the
        data+flags.
      | b) Edit or modify the averaged flags.
      | c) Write the edited averaged flags back to the original input
        MeasurementSet.
      | Since CASA 5.7/6.1, CASA implements two alternative approaches
        to step c:
      | 1) flagdata alternative: preserve pre-existing flags, flags can
        be added (set) but never removed (unset).
      | 2) plotms alternative: flags can be added (set) but also removed
        (unset).
      | Flagdata will only add new flags (true or 1) to the original
        data. It will never unset a previously set flag.
      | This is implemented as follows. If an averaged flag is set, the
        flag is propagated back to all the original flags in the
        corresponding input bin. If an averaged flag is not set, nothing
        is done, and the flags that might be set in the corresponding
        input bin remain set. As a consequence, a flagdata command that
        uses data average will only increase the amount of flags in the
        input MeasurmentSet (or simply keep the same amount, if the
        flagging methods applied do not add any new flags). This way,
        all original flags are preserved in the input MeasurementSet.
      | In contrast, plotms will write back to the input MeasurementSet
        both true (1) and false (0) flag values. That is, plotms can set
        and unset flags, and the initially set flags in the input
        MeasurementSet are not necessarily preserved.

.. container:: section
   :name: viewlet-below-content-body
