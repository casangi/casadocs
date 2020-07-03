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

   Bootstrap the flux density scale from standard calibrators.

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Summary:  The *'G'* or *'T'* solutions obtained by **gaincal** for
      calibrators for which the flux density was unknown and assumed to
      be 1 Jansky are correct in a time- and antenna- relative sense,
      but are mis-scaled by a factor equal to the inverse of the square
      root of the true flux density. This scaling can be corrected by
      enforcing the constraint that mean gain amplitudes determined from
      calibrators of unknown flux density should be the same as
      determined from those with known flux densities. The **fluxscale**
      task exists for this purpose.

      Before running **fluxscale**, one must have first run **setjy**
      for the reference sources and run a **gaincal** that includes
      reference and transfer fields. The reference field(s) should be
      standard flux density calibrators for which an accurate flux
      density (or better, a model image, especially if it is a resolved
      source) is known. The transfer fields are all other calibrators,
      typically point sources (to a good approximation), and for which
      actual flux density is unknown. When running **fluxscale**, the
      input *caltable* will be scaled and written out into the
      output *fluxtable* such that the correct scaling will be applied
      to the transfer sources. The *fluxtable* parameter is required,
      and if it is already present, it will not be overwritten. The user
      can set *append*\ =True to append the flux-scaled results to the
      existing table. If *incremental=True,* a simple incremental
      calibration table will be generated that contains a single
      antenna-based solution per field embodying the required scale
      factors. If *incremental=False,* a copy of the input caltable is
      generated, with the required scale factors applied to the transfer
      fields.

      **fluxscale** applies the constraint that net system gain was, in
      fact, independent of field, time, and direction, on average, and
      that field-dependent gains in the input caltable are solely a
      result of the unknown flux densities for the calibrators. Using
      time-averaged gain amplitudes, the ratio between each ordinary
      calibrator and the flux density calibrator(s) is formed for each
      antenna and polarization (which they have in common). The average
      of this ratio over antennas and polarizations yields a correction
      factor that is applied to the ordinary calibrators' gains.

      The square of the gain correction factor for each calibrator and
      spw is the presumed flux density of that calibrator (if the
      assumed flux density when solving was 1 Jy), and is reported in
      the logger. The errors reported with this value reflect the
      scatter in gain ratio over antennas and polarizations, divided by
      the square root of the number of  antennas and polarizations
      available. If the flux densities for multiple spws exist, fitted
      spectral index and (for nspw>2) curvature are also reported. The
      fit is done for

      $log(S_\nu) = a_o + a_1*(log(\nu/\nu_0)) +
      a_2*(log(\nu/\nu_0))**2$.

      The reference frequency, $\nu_0$ (the mean of $log(\nu)$) is
      reported in the logger along with the flux density at that
      frequency. The fit results are also reported in the returned
      Python dictionary which takes the form:

      .. container:: casa-output-box

         | {fieldIdstr: {spwIdstr: {'fluxd':array([I,Q,U,V]),
         |                          'fluxdErr': corresponding errors,
         |                          'numSol': corresponding no. of
           solutions}
         |               'fieldName': field name,
         |               'fitFluxd': fitted flux density at the
           reference frequency,
         |               'fitFluxdErr': fitted flux density error,
         |               'fitRefFreq': reference frequency,
         |               'covarMat': covariance matrix for the fit,
         |               'spidx': a_0, a_1, a_2
         |               'spidxerr': errors in a_0,a_1, a_2}
         |  'freq': (center) spw frequencies
         |  'spwID': list of spw IDs,
         |  'spwName': list of spw names}

      where fieldIdstr and spwIdstr are field Id and spw Id in string
      type, respectively. The 'spidx' coefficients, $a_0$, $a_1$, and
      $a_2$ are the $log(S_{\nu=\nu0})$, the spectral index, and the
      curvature, respectively. If only a single spectral window is
      present, no fitting is performed but fitFluxd and fitRefFreq are
      filled with the values from fluxd and freq, respectively.

      The calibrator models are currently not revised within the MS to
      reflect the flux densities derived by **fluxscale**. Use **setjy**
      to set these, if necessary.

      The constant gain constraint is usually a reasonable assumption
      for the electronic systems on typical antennas. It is important
      that external time- and/or elevation-dependent effects are
      separately accounted for when solving for the gain solution
      supplied to **fluxscale**, e.g., gain curves, opacity, etc. (see
      **gencal**). 

      The **fluxscale** results can also be degraded by poor pointing
      during the observation. The parameters, *gainthreshold* and
      *antenna* (and *timerange*/*scan*) can be used to control the data
      to be used in the flux derivation in such cases. Please note that,
      regardless of the antennas that are selected for deriving the
      scaling, the scaling solution is applied to all valid
      (non-flagged) antennas. The *gainthreshold* parameter sets the
      range of the input gain to be used in terms of the fractional
      deviation from their median values (per field, per spectral
      window).

      If the reference and transfer fields were observed in different
      spectral windows, the *refspwmap* parameter may be used to achieve
      the scaling calculation across spectral window boundaries. In
      general, this will yield less accurate flux density calibration.

      The **fluxscale** task can be executed on either *'G'* or *'T'*
      solutions, but it should only be used on one of these types if
      solutions exist for both and one was solved relative to the other
      (use **fluxscale** only on the first of the two).

      .. container:: alert-box

         **ALERT:** *'GSPLINE'* solutions from **gaincal** are not
         supported in **fluxscale**.

       

      .. rubric:: Using resolved calibrators
         :name: using-resolved-calibrators

      If the flux density calibrator is resolved, the assumption that it
      is a point source will cause solutions on outlying antennas to be
      biased in amplitude. In turn, the **fluxscale** step will be
      biased. In general, it is best to use a model for the calibrator,
      but if such a model is not available, it is important to limit the
      solution on the flux density calibrator to only the subset of
      antennas that have baselines short enough that the point-source
      assumption is valid. Such a subset of antennas can be selected for
      the **fluxscale** calculation using the *antenna* parameter, which
      uses standard antenna-selection syntax. Specifying something in
      *antenna* also reveals *timerange* and *scan* selection parameters
      which enable more specific selection on these axes.

      Alternatively, limiting the **fluxscale** calculation to antennas
      on unresolved baselines can be effected by using *antenna* and
      *uvrange* selection when solving for the flux density calibrator
      in **gaincal**. Please see the Examples section.

       

.. container:: section
   :name: viewlet-below-content-body
