.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Manipulate Ephemeris Objects
============================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   How to work with ephemeris objects in CASA

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      When an astronomical object has a proper motion, in particular
      objects in our solar system, a static (RA,Dec) position in the
      FIELD table of the MeasurementSet will not accurately describe the
      time-dependent position. Prior to CASA 4.2, there was no support
      for ephemeris objects other than the built-in reference frames for
      the Sun, the Moon, and the planets out to PLUTO. With CASA 4.2,
      several new features were introduced which help the user to attach
      an arbitrary ephemeris to a given field and work with the object
      from calibration to imaging. These can be used when no ephemeris
      table was provided by the observatory, or in cases where the use
      of an improved ephemeris table is necessary.

      .. rubric:: Ephemeris tables
         :name: ephemeris-tables

      The CASA format for ephemeris tables was introduced in the early
      development stages of CASA in connection with the Measures module.
      The me tool (see `CASA
      Tools <https://casa.nrao.edu/casadocs-devel/stable/old-pages/casa-tasks-and-tools/casa-tools>`__ on
      using the tool kit, as well as the inline help on the me tool
      inside CASA for specific usage) permits position calculations
      based on ephemerides in this format. Two examples for such tables
      can be found in the distribution directory in subdirectory
      data/ephemerides: VGEO is an ephemeris of Venus in the geocentric
      reference frame while VTOP is an ephemeris for the same object in
      the TOPO reference fame for the observatory location of the VLA.
      With the introduction of solar system source models (Butler) in
      the **setjy** task, a nearly complete set of ephemerides for the
      larger bodies in our solar system had to be made available. These
      are stored in nearly the same format as the above examples VGEO
      and VTOP (but with a few enhancements) in directory
      data/ephemerides/JPL-Horizons. If your object’s ephemeris is among
      those stored in data/ephemerides/JPL-Horizons, you can simply copy
      the ephemeris from there. Otherwise, you can request the ephemeris
      from the JPL-Horizons using the CASA commands (for example):

      .. container:: casa-input-box

         | # For CASA5 (for CASA6, the location of request is TBD)
         | import recipes.ephemerides.request as jplreq
         | jplreq.request_from_JPL(objnam='Mars',startdate='2012-01-01',enddate='2013-12-31',date_incr='0.1
           d', get_axis_orientation=False,
         | get_axis_ang_orientation=True,
         | get_sub_long=True, use_apparent=False, get_sep=False,
         | return_address='YOUR_EMAIL_ADDESS',
         | mailserver='YOUR_MAIL_SERVER_ADDRESS')

      where you need to fill in the parameters objnam, startdate,
      enddate,date_incr (the time interval between individual ephemeris
      table entries), return_address (your email address where you want
      to receive the ephemeris), and mailserver (the smtp server through
      which you want to send the request email). The other parameters
      should be set as shown. Within a short time, you should receive
      the requested ephemeris as an email from NASA’s
      JPL-Horizonssystem. Save the email into a file with the “save as”
      function of your mail client. See the next section on how to
      attach it to your dataset.

      .. rubric:: Using fixplanets to attach ephemerides to a field of a
         MeasurementSet
         :name: using-fixplanets-to-attach-ephemerides-to-a-field-of-a-measurementset

      As of CASA 4.6.0, importasdm fills the SOURCE coodinates with the
      correct postions based on the ephemerides table. Alternatively,
      one can use the task **fixplanets** to set the ephemeris of a
      given field in a MeasurementSet. Here is an example:

      .. container:: casa-input-box

         | fixplanets(vis='uid___A002_X1c6e54_X223.ms',
         | field='Titan', fixuvw=True, direction='mytitanephemeris')

      where you need to set the parameters vis to the name of your MS
      and the parameter field to the name of the field to which you want
      to attach the ephemeris. The parameter direction must be set to
      the name of your ephemeris table. Accepted formats are (a) the
      CASA format (as in VGEO or the ephemerides in
      data/ephemerides/JPL-Horizons as described above) and (b) the
      JPL-Horizons mail format which you obtain by saving an ephemeris
      email you received from JPL-Horizons. The parameter fixuvw should
      be set to True in order to trigger a recalculation of the UVW
      coordinates in your MS based on the new ephemeris. The task
      **fixplanets** can also be used for other field direction
      modifications. Please refer to the help text of the task.

      .. container:: info-box

         Note that among the ephemerides in the directory
         data/ephemerides/JPL-Horizons/you should only use those ending
         in’_J2000.tab’. They are the ones in J2000 coordinates.

      .. rubric:: Use of the ephemeris after attachment
         :name: use-of-the-ephemeris-after-attachment

      Once you have attached the ephemeris to a field of an MS, it will
      automatically be handled in tasks like **split** and **concat**
      which need to hand on the ephemeris to their output MSs. In
      particular **concat** recognizes when fields of the MSs to be
      concatenated use the same ephemeris and merges these fields if the
      time coverage of the provided ephemeris in the first MS also
      covers the observation time of the second MS. The ephemeris of the
      field in the first MS will then be used for the merged field. In
      order to inspect the ephemeris attached to a field, you can find
      it inside the FIELD subdirectory of your MS. The optional column
      EPHEMERIS_ID in the FIELD table points to the running number of
      the ephemeris table. A value of −1 indicates that no ephemeris is
      attached. Note that in case an ephemeris is attached to a field,
      the direction column entries for that field in the FIELD table
      will be interpreted as an offset to the ephemeris direction and
      are therefore set to (0.,0.) by default. This offset feature is
      used in mosaic observations where several fields share the same
      ephemeris with different offsets. The time column in the FIELD
      table should be set to the beginning of the observation for that
      field and serves as the nominal time for ephemeris queries.

      .. rubric:: Spectral frame transformation to the rest frame of the
         ephemeris object in task cvel
         :name: sec298

      The ephemerides contain radial velocity information. The task
      **cvel** can be used to transform spectral windows into the rest
      frame of the ephemeris object by setting the parameter outframe to
      “SOURCE” as in the following example:

      .. container:: casa-input-box

         | cvel(vis='europa.ms',
         | outputvis='cvel_europa.ms', outframe='SOURCE', mode =
           'velocity',
         | width = '0.3km/s', restfreq = '354.50547GHz')

      This will make **cvel** perform a transformation to the GEO
      reference frame followed by an additional Doppler correction for
      the radial velocity given by the ephemeris for the each field.
      (Typically, this should happen after calibration and after
      splitting out the spectral widows and the target of interest). The
      result is an MS with a single combined spectral window in
      reference frame REST. From this frame, further transformations to
      other reference frames are not possible.

      .. rubric:: Ephemerides in ALMA datasets
         :name: sec299

      The ALMA Science Data Model (the raw data format for ALMA data)
      now foresees an Ephemeris table. This feature has been in use
      since the beginning of ALMA Cycle 3 both for science targets and
      calibrator objects. With ALMA Cycle 3 (or later) datasets, the
      task **importasdm** will automatically translate the contents of
      the ASDM Ephemeris table into separate ephemeris tables in CASA
      format and attach them to the respective fields.

      In the case of mosaics, all fields belonging to a mosaic on an
      ephemeris object will share the same ephemeris. The individual
      mosaic pointings will use the offset mechanism described above to
      define the position of each field.

      .. rubric:: Imaging ALMA observations with tclean
         :name: sec299

      As of CASA 5.3, the tclean task can automatically handle the
      imaging of ALMA observations (both single-execution and
      multi-execution datasets, and both single-field and mosaics) by
      using the new *phasecenter='TRACKFIELD'* option. This option will
      use the ephemeris tables attached to each measurementSet by the
      ALMA control system. These tables will have ultimately been
      provided by the observatory for the case of large bodies (those
      selectable in the ALMA Observing Tool), or by the PI as
      attachments in the Observing Tool for the case of smaller bodies.

      .. container:: alert-box

         **WARNING**\ *:*  if you want to use the old method of
         concatenating calibrated MeasurementSets by using the
         *forcesingleephemfield* parameter to create a common joint
         ephemeris table, then you must still set
         *phasecenter='TRACKFIELD'* in tclean order to get a sensible
         image, even though you are passing it only one (concatenated)
         MeasurementSet. If not, you may get a corrupt image, even if
         you select a subset of data only from the first execution block
         in the concatenated MS.

      .. rubric:: Imaging observations from other telescopes with tclean
         :name: imaging-observations-from-other-telescopes-with-tclean

      For non-ALMA data, or to use a newer ephemeris than was available
      at the time of the ALMA observations, the user may set the
      phasecenter parameter to the name of an ephemeris file,
      constructed as described in the earlier section above.
      Alternatively, the user may set the phasecenter to the common name
      of the following bodies: 'MERCURY', 'VENUS', 'MARS', 'JUPITER',
      'SATURN', 'URANUS', 'NEPTUNE', 'PLUTO', 'SUN', 'MOON', in which
      case the standard DE200 ephemeris table distributed with CASA will
      be used.

.. container:: section
   :name: viewlet-below-content-body
