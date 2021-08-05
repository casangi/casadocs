.. include:: <isogrk1.txt>

.. _Description:

Description
   This task changes the phase center of an MS by modifying the *UVW*
   coordinates and the specified data column(s) (via the **datacolumn**
   parameter) of the input MS and creating an output MS with these changes.
   The *PHASE_DIR* column of the *FIELD* subtable of the new MS is updated
   with the new phase center. Many MS selection parameters are supported (see
   `Visibility Data Selections
   <../../notebooks/visibility_data_selection.ipynb>`__
   for details). 

   .. danger:: **ALERT:** Partial spectral window selection via the *spw* parameter (eg, spw='1:20~25') may cause errors. This issue is being investigated and will be fixed in a subsequent version of CASA. As a workaround, if you require such a selection, first specify it in and run split to create the desired selection and use the resulting MS as input to **phaseshift**.

   .. danger:: **ALERT:** If you intend to move the phasecenter far enough away from the antenna pointing center, please be aware that the pointing table needs to exist in the MS, for the imaging tasks to know the world coordinates at which to center primary beams. If a pointing table does not already exist, please consider simply using tclean(phasecenter='') for on-the-fly phase rotation if the intention is to anyway run imaging soon after phaseshift, as this on-the-fly operation will still use the original (unmodified) phase/pointing center and primary beams will be correctly located.

   The input MS is not modified, and so the *outvis* parameter must be specified; note that this
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
   
   The **phaseshift** application uses a similar algorithm as **tclean** (via its 
   **phasecenter** parameter) for phase center shifting. However, these two
   applications use a signficantly different algorithm than **plotms** does for phase
   shifting, so results, particularly for larger shifts, are likely to diverge for
   **plotms** and **phaseshift**/**tclean**.
   
.. _Examples:

Examples
   .. code-block:: python
   
      # shift the phase center to J2000 04:52:16 -02.04.55
      # note that any valid direction syntax is supported, including
      # FRAME XXhXXmXX.Xs YYdYYmYY.Ys
      # FRAME XX.XXdeg YY.YYdeg
      # FRAME XX.XXrad YY.YYrad
      # the longitude-like and latitude-like coordinates can have different syntaxes, eg
      # FRAME XXhXXmXX.Xs YY.YYrad
      phaseshift(
          vis='unshifted.ms', outvis='shifted.ms',
          phasecenter='J2000 04:52:16 -02.04.55'
      )

  There is a memo [link to be provided] describing in detail the numerical characterization of
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
   * Support for time-dependent coordinate frames and ephemeris objects
     is planned for ngCASA only. However, if greatly desired, requests for
     such support will be considered prior to that. Please send us a request
     via the Help Desk should you have such a need.
   * Specifying the new phase center in terms of an offset from
     the original phase center is currently not supported. However, if
     there is a need for such support, it can be added. Please send us a request
     via the Help Desk should you have such a need.
   * There is currently no support for the possible use case of updating only
     the *UVW* values (eg, based on antenna position updates), but not the associated
     data values. The deprecated task **fixvis** has this functionality, so it may
     be used for this purpose. If such support will be needed after **fixvis** is
     removed, it can be added. Please send us a request via the Help Desk should you
     have such a need.

 

