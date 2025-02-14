.. include:: <isogrk1.txt>

.. _Description:

Description
   This task changes the phase center of an MS by modifying the *UVW*
   coordinates and the specified data column(s) (via the **datacolumn**
   parameter) of the input MS and creating an output MS with these changes.
   The *PHASE_DIR* column of the *FIELD* subtable of the new MS is updated
   with the new phase center(s). Many MS selection parameters are supported
   (see `Visibility Data Selections
   <../../notebooks/visibility_data_selection.ipynb>`__
   for details). 

   .. danger:: **ALERT:** Partial spectral window selection via the *spw* parameter (eg, spw='1:20~25') may cause errors. This issue is being investigated and will be fixed in a subsequent version of CASA. As a workaround, if you require such a selection, first specify it in and run split to create the desired selection and use the resulting MS as input to **phaseshift**.

   .. danger:: **ALERT:** If you intend to move the phasecenter far enough away from the antenna pointing center, please be aware that the pointing table needs to exist in the MS, for the imaging tasks to know the world coordinates at which to center primary beams. If a pointing table does not already exist, please consider simply using tclean(phasecenter='') for on-the-fly phase rotation if the intention is to anyway run imaging soon after phaseshift, as this on-the-fly operation will still use the original (unmodified) phase/pointing center and primary beams will be correctly located.

   The input MS is not modified, and so the *outputvis* parameter must be specified; note that this
   behavior is different from that of task *fixvis*. The implementation assumes
   that the *UVW* coordinates are correct in the frame in which they are
   specified; these coordinates are transformed via rotation to the new
   phase center. No attempt is made to recompute the *UVW* values because of,
   eg, antenna position changes (please see the `Development`_ section for more
   details),

   The new phase center is specified via the **phasecenter** parameter.
   The standard syntax for specifying astronomical world direction coordinates
   is supported (*e.g.* 'J2000 19h45m20.56 -50d30m45.7' or
   'J2000 19:45:20.56 -50.30.45.7'). Coordinate systems that are time
   dependent are not supported, such as topocentric or geodetic systems
   (*e.g.* azimuth-elevation). Ephemeris objects are likewise not supported.

   The **phasecenter** parameter can be of string type (one single phase center)
   or of dictionary type (multiple phase centers, with up to one entry for every
   field present in the input MS). When using a dictionary it is possible to
   specify a different phase center for every field of the input MeasurementSet.

   The new phase center(s) are written in the output MeasurementSet (subtable FIELD,
   column PHASE_DIR) using the same reference frame(s) as in the input
   MeasurementSet. This follows the general rules of propagation of metadata
   in mstransform whereby the output MeasurementSet preserves the reference frames
   from the input MeasurementSet. If the center(s) given in the input
   **phasecenter** parameter use different reference frame(s), these will be
   converted to the reference frame(s) used in the input (and output) MeasurementSet

   The **phaseshift** application uses a similar algorithm as **tclean** (via its 
   **phasecenter** parameter) for phase center shifting. However, these two
   applications use a signficantly different algorithm than **plotms** does for phase
   shifting, so results, particularly for larger shifts, are likely to diverge for
   **plotms** and **phaseshift**/**tclean**.
   
.. _Examples:

Examples
   **Example 1:**

   Shift a single field MS to a new phase center in J2000 coordinates.

   .. code-block:: python
   
      # shift the phase center to J2000 04:52:16 -02.04.55
      # note that any valid direction syntax is supported, including
      # FRAME XXhXXmXX.Xs YYdYYmYY.Ys
      # FRAME XX.XXdeg YY.YYdeg
      # FRAME XX.XXrad YY.YYrad
      # the longitude-like and latitude-like coordinates can have different syntaxes, eg
      # FRAME XXhXXmXX.Xs YY.YYrad
      phaseshift(
          vis="unshifted.ms", outputvis="shifted.ms",
          phasecenter='J2000 04:52:16 -02.04.55'
      )

   **Example 2:**
   Shift a multi-field MS to use new phase centers for some of its fields (in J2000 frame).

   .. code-block:: python

      # Use different phase centers for different input fields.
      # The field not given in the dictionary of output centers will not be shifted but
      # will be included in the output MS (as selected or not in the **field** parameter).
      # For example, if "input.ms" has fields 0 to 5, the output MS will still have
      # these fields. Only fields 2, 3, and 5 are modified.
      new_centers = {"2": "J2000 04:52:16 -02.04.55",
                     "3": "ICRS 13:05:27.2780 -049.28.04.458",
		     "5": "J2000 04:52:16 -02.04.55"}
      phaseshift(vis="input.ms", outputvis="out_shifted.ms", phasecenter=new_centers)

   **Example notebook**

  There is a `Community Examples Notebook <https://casadocs.readthedocs.io/en/stable/examples/community/phaseshift.html>`__
  in CASA Docs describing in detail the numerical characterization of
  phaseshift, which provides a complete script and detailed results regarding the correctness
  of the results produced by phaseshift. In summary, in a 1.0 GHz VLA simulation in which the
  phase center and a source were initially separated by 2.7 degrees, using phaseshift to shift
  the phase center to be coincident with the source resulted in the source being located less
  than 30 marcsec (0.003 pixels) from the simulated position. In a 150 GHz ALMA simulation in
  which the phase center and a source were initially separated by 1.2 arcmin, using phaseshift
  to shift the phase center to be coincident with the source resulting in the source being
  located less than 90 |mgr| arcsec (0.001 pixels) from the simulated position. 
    
.. _Development:

Development

   - Support for time-dependent coordinate frames and ephemeris objects
     is planned for ngCASA only. However, if greatly desired, requests for
     such support will be considered prior to that. Please send us a request
     via the Help Desk should you have such a need.
   - Specifying the new phase center in terms of an offset from
     the original phase center is currently not supported. However, if
     there is a need for such support, it can be added. Please send us a request
     via the Help Desk should you have such a need.
   - There is currently no support for the possible use case of updating only
     the *UVW* values (eg, based on antenna position updates), but not the associated
     data values. The deprecated task **fixvis** has this functionality, so it may
     be used for this purpose. If such support will be needed after **fixvis** is
     removed, it can be added. Please send us a request via the Help Desk should you
     have such a need.

 

