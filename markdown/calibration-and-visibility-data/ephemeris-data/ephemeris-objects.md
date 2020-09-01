

# Ephemeris Objects 

Background information concerning ephemeris objects

Since ALMA Cycle 3, the ALMA observatory includes in each raw dataset (SDM) all necessary ephemerides in the so-called Ephemeris table, an XML file which corresponds to the ephemeris used during the observation. Upon import to MS format, the task **importasdm** will translate the xml ephemerides into separate CASA ephemeris tables for each field, which have the same format as those used by the task **setjy**. Examples can be found in the subdirectory \"data/ephemerides/JPL-Horizons\" in each CASA distribution.

The ephemeris tables are automatically attached to the corresponding field(s) and can be used whenever needed. They have two main use cases:

1.  An ephemeris table is necessary for the *spectral* frame transformation of the visibilities to the source rest frame *permanently* when creating a new MS using the tasks **cvel, cvel2,** or **mstransform,** or *on-the-fly* during imaging using the task **tclean** by setting the parameter *specmode* to \"cubesource\". The ephemeris provides the location of the phase center and the radial velocity of the target.
2.  An ephemeris table is also necessary if your observation has tracked some other phase center but you would like to track the location described by the ephemeris. This can be achieved by setting the parameter *phasecenter* of task **tclean** to the string \"TRACKFIELD\". See the **tclean** documentation for more details.

The ephemerides used by ALMA are originally for the observer location of ALMA (topocentric). They use the ICRS coordinate reference frame and typically have a time spacing of ten or twenty minutes. For the later transformation of the spectral reference frame, however, a geocentric ephemeris is necessary. The **importasdm** task will therefore by default also perform a conversion from the ALMA observer location to the geocenter. This is controlled by the **importasdm** parameter *convert_ephem2geo* which is True by default.

The spectral reference frame of the visibilities in the SDM is always topocentric (TOPO), the observer reference frame. To analyze spectral lines in an ephemeris source, it can be helpful to transform the visibilities to the source rest spectral frame (REST). This is in particular necessary when the velocity of the source varies significantly throughout the observation (which can, e.g., happen if the observation is spread over serveral days). As mentioned above, this offline software Doppler-shift correction can be achieved in two ways, either permanently or on-the-fly. This is described further below.

When an ephemeris is attached to a field of the MS FIELD table, the object position does not correspond to the direction columns of the FIELD table but is retrieved by linearly interpolating from the ephemeris table for the given time. The nominal entry of the direction column then *changes its meaning to an angular offset* with respect to the ephemeris. Thus, if the field center is exactly at the position described by the ephemeris, the nominal entries of the direction column are zero for right ascension and declination. The offset feature of the FIELD table direction column comes into play in the case of a mosaic: if there are a number of fields with nearby positions, the fields can share an ephemeris; they all reference the same ephemeris table via the optional column EPHEMERIS_ID, but have different offsets in their direction column entries.

Because the nominal FIELD table direction column entries do not correspond to the actual object position, one should obtain the object position with the following special tool method:

```
msmd.phasecenter()
```

or the more general:

```
ms.getfielddirmeas()
```

(see the inline CASA help for details on these tools). The default time of the position is taken from the TIME column of the FIELD table.

#### Permanent spectral frame transformation creating a new MS

Either with either the task **cvel** or its faster implementation **cvel2** (which uses internally the same code as the task **mstransform**) or with **mstransform**, a new MS can be created which contains visibilities in the spectral reference frame of the source. All three tasks should produce the same result. As a matter of fact, an online Doppler-shift tracking corresponding to the velocity of the source at the beginning of the observation is applied during observations. This online correction allows one to tune the spectral windows adequately to match the requested rest frequencies, but the labelling of the spectral frame of the raw data remains in TOPO.

The user must set the *outframe* parameter of **cvel**, **cvel2**, or **mstransform** to \"SOURCE\". This will lead to a transformation from the TOPO to the GEO reference frame followed by an additional time-dependent Doppler correction according to the radial velocity of the object as given by its ephemeris.

Such MSes should then be imaged using the setting \"cubedata\" for the parameter *specmode* in **tclean**. The resulting spectral reference frame in the MS is named \"REST\".

#### On-the-fly spectral frame transformation within tclean

If a permanent storage of spectrally transformed visibilities in a new MS is not needed, cubes with the spectral frame of the ephemeris object can also be obtained by letting the task **tclean** perform the frame transformation on-the-fly. This is simply achieved by setting parameter *specmode* to the string \"cubesource\". The resulting cube will also have the reference frame named \"REST\".

 

In summary, with ephemerides included in the ALMA raw data and the added support for this in the **importasdm** task, the user rarely needs to worry about how to obtain the right ephemeris in the right format and how to attach it properly to the MS. This process is transparent and only a few logger messages indicate that it is happening (see CASA Docs pages on [\'Manipulate Ephemeris Objects\'](https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/ephemeris-data/manipulation-of-ephemeris-objects) if a new ephemeris needs to be added to an existing MS). The correct time-dependent positions, radial velocities, and object distances are used in all relevant tasks such as **listobs**, **plotms**, and, as described above, **cvel**, **cvel2**, **mstransform**, and **tclean**. For Solar-System object flux calibrators, the task **setjy** will, however, only extract the nominal position from the SDM ephemeris and otherwise use its internal set of ephemerides since these contain additionally needed object parameters. Care has to be taken when trying to extract the field positions from the FIELD table as the nominal direction column entries will only be offsets (w.r.t. the ephemeris position) when an ephemeris is attached.

As opposed to ALMA data which use a tabulated representation of the ephemerides, VLA data use a polynomial representation of the positions and radial velocities. Also this representation is supported. The polynomial ephemeris is internally tabulated with a default time step of 0.001 days and then processed as in the ALMA case. The **importasdm** parameter *polyephem_tabtimestep* can be used to control the step size of the tabulation.

 

