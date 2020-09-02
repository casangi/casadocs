

# Spectral Line Imaging 

Specific topics for spectral line imaging including spectral coordinates and spectral reference frames

# Spectral coordinates and frame

In spectral line imaging, the spectral coordinates are defined by the user inputs. The relevant **tclean** parameters are the data selection parameters and image cube defining parameters:  *start, width,* *nchan,* and *outframe*.  The task attempts to adjust the inputs so that the data selection matches the defined cube.

The **tclean** tasks provide *start* and *width* parameters can be specified in channel index, frequency, or velocity. In **tclean** task, spectral mode is turned on by *specmode=\'cube\'* and its specific mode (channel, frequency, or velocity) is automatically determined from the units of the sub-parameters (*start*, *width*). Mixed specifications are currently not allowed (e.g. *start=\'5\'* and *width = \'10km/s\'* ) in **tclean**.

The underlying imaging code (FTMachine) uses to a fixed spectral reference frame (LSRK) internally. However, the user can specify an outframe so that the output cube image is relabeled to the user specified frame. If the outframe is unspecified, it defaults to LSRK. Continuum images are always labeled in LSRK. Note that tools like the Viewer can also apply on-the-fly conversions to relabel frequencies in frames other than what is in the image header. The masks (imregrid, imreframe, and exportfits) can also explicitly change the reference frame, and in some cases, regrid the channels.

## Spectral Reference Frame

CASA (CASACORE Measures) uses the frequency frames defined in the Reference material section \"[Spectral Frames](https://casa.nrao.edu/casadocs-devel/stable/memo-series/reference-material/spectral-frames)\". Data is typically observed in the topocentric observatory frame (TOPO) at a fixed sky frequency. Any observed line, however, will change its topocentric frequency as a function of time.  Note that for TOPO (as well as GEO) reported frequencies, the grid of output images uses the first time stamp of the observations.

When applying Doppler corrections, the data is typically regridded to the Local Standard of Rest Kinematic (LSRK, CASA default) or the sun-earth barycentric (BARY) frame, which can be specified in the *outframe* parameter. Both of  these parameters require the rest frequency of a spectral line (*restfreq* parameter).

In addition, a velocity definition (*veltype* parameter, sometimes referred to as Doppler type) is required. This parameter is typically either RADIO (CASA default) or OPTICAL. Note that those definitions are identical at $v=0$ but increasingly differ  at larger velocity values. A full list of supported velocitiy definitions is given in the Reference material section \"[Spectral Frames](https://casa.nrao.edu/casadocs-devel/stable/memo-series/reference-material/spectral-frames)\".

# Mapping between Data Channels and Image Channels

During the gridding process, the **tclean** task makes a choice about how to map data channels to image channels, based on the channelization encoded in the MS and the user-specified image channelization. The mapping between data channels and imager channels may vary depending on the following:

1.  If the user-specified \'start\' frequency is not at a data channel boundary, the visibility data and weights are interpolated and then evaluated at the centers of the shifted frequency grid. 
2.  When image channels are wider than data channels, visibilities and weights are binned and gridded via multi-frequency synthesis (MFS) within each image channel.
3.  On-the-fly software Doppler tracking can also be done as a time-dependent frequency relabeling of the data channels, before interpolation and binning choices are made.

Usually, a combination of these three operations are performed during gridding. There are also special cases where only some or none of them apply. This behavior is consistent between the old and new Imager code (i.e., **clean** and **tclean**).

The *interp* parameter chooses the interpolation scheme to be used during the gridding process. The choices are currently \'*nearest\'*, \'*linear\'*, and \'*cubic\'*.

-   *\'nearest\' *just picks the value of the nearest data channel.
-   \'*linear*\' will interpolate the data channel to a channel width that is an integral number of channels that fits in an image channel. For example, if the image channel is 3.14x the width of the original data channel, then interpolation will interpolate the data and weights to 3 channels with a width of 3.14/3.0 times the original width of the data channel.The linear gridder will use the 2 adjacent original data channel to interpolate.
-   \'*cubic*\' works the same as \'linear\', but with the nearest 4 instead of 2 data channels.

<div class="alert alert-warning">
**Warning:** in CASA version earlier than 5.6, the interpolated channels were ensure to be aligned with the edge of the image channel. This could cause channels to be dropped at the edges of data chuncks, causing different sensitivities at the edge of the chunkcs (which can be particularly problematic when chanchunk >1 or in parallel processing). In CASA 5.6, this has been resolved, and the interpolated channels data now align with the center of the image channel.
</div>

 

# Software Doppler Tracking Options

For the purpose of this document, a time independent frame is a frame in which the source observed has not changed its velocity over the period of time of the observation. A time dependent frame is one in which the observed source has changed its velocity during the observation period. If datasets from different epochs are combined during imaging, the relevant period of time to consider is the entire range spanned by all datasets.

The following descriptions are specific to the task based on new imager, **tclean**.

There are three software Doppler tracking options, which will be controlled at the task level. Individual parameters are described in the parameter tab for **tclean** task page.

## *specmode=\'cube\'*

Converts data frequencies to the time-independent spectral frame (default: LSRK).

Output image base frame : specified frame in *outframe*

In this mode, data frequencies are read from the input MS(es), and compared with image channel bin frequencies (also in LSRK) to decide which data channels go into which image channel bins. This process is a time-dependent relabeling of data frequencies. The result aligns the frequencies of spectral lines from astrophysical sources taken at different times and thus with different observed frequencies.   The relevant user parameters are: *start, width, nchan, outframe, veltype, restfreq*.

Internally, this mode converts the data to LSRK frequencies before gridding and after gridding converts them to the outframe to construct an appropriate output CASA image.   Note that for TOPO and GEO, which are actually time-dependent frames, the conversion layer encodes a specific time at which the conversion is valid. The convention in \'**clean**\' is the start epoch of the dataset, but this time can be changed via the **imreframe** task with *outframe=\'topo\'*.  

## *specmode=\'cubedata\'*

Produces a one-to-one mapping between data channels and image channels.

Output image base frame : REST, UNDEFINED  

In this mode, no time-dependent frequency frame transformations are done during gridding/binning. In this case, data frequencies are read from the input MS(es) and compared directly with image frequencies. If the data has been observed in a time-dependent frame (e.g., TOPO), this mode will not align the frequencies of spectral lines from astrophysical sources taken at different times and thus with different observed frequencies. Only local signals  at a fixed frequency such as RFI will remain aligned, for example terrestrial RFI in case of TOPO data.

The relevant user parameters are *start, width, nchan, veltype, restfreq*.

For this mode, *outframe* is not an option as *start, veltype, restfreq* will be interpreted literally to construct the frequency grid, with no further conversions.

## (To be implemented) *specmode=\'cubesrc\'*

Convert data frequencies to the SOURCE frame.

 Output image base frame : SOURCE  

If the FIELD table of the source being imaged contains ephemeris information, a time-dependent relabeling of the data frequencies (software Doppler tracking) is done to make spectral lines stationary in the moving source frame.  If the FIELD table of the source being imaged does not contain ephemeris information (i.e. the source is not a solar system object), the software Doppler tracking will follow a conversion to LSRK. In addition, a systemic velocity has to be specified with respect to a spectral frame, which will be recorded in the image.

 The relevant user parameters are: *start, width, nchan, frame, veltype, restfreq, sysvel, sysvelframe*. The base frame of the output image will always be SOURCE. The *sysvel* and *sysvelframe* parameters represent the systemic velocity with respect to a specific frame that will be embedded in the coordinate system. These two parameters are ignored if the ephemeris information is available. This is the only mode that allows the *start and width* parmaeters to be specified in *outframe=\'SOURCE\'* in addition to other standard frames.

## *mode=\'mfs\'*

Multi-frequency synthesis, where there is only one large image channel. This will always be in LSRK, with the image frequency coordinates decided by the spw data selection parameter.

#  Imaging a pre-Doppler-tracked Data Set

An MS output by **cvel** or **mstransform** will be treated the same way as any other MS observed directly in the frame that the MS is labeled with.

1.  A dataset that has been relabeled in a time-independent frame ( LSRK, LSRK, BARY, etc\.... ) using **mstransform** can use *mode=\'cube\'*. The base frame of the output image will be based the input parameters. If the MS is already in a time-independent frame, the code will detect that no additional time-dependent frequency shifts are required. A similar situation holds for datasets labeled in the SOURCE frame when *mode=\'cubesrc\'* is used.
2.  A dataset that needs channel binning/gridding with no extra time-dependent frequency transformations should use *mode=\'cubedata\'* and the output frame will be 'UNDEFINED'. For example, when an MS has already been transformed into a time-dependent frame and the user wants to image the data as is.
3.  If the MS has been relabeled \'REST\' using **mstransform**, the base frame of the output image will be \'REST\'. This method is another way to generate images with no extra time-dependent frequency transformations.

# Parameters for Spectral-Axis Image Defination

## *nchan*

Number of channels in output cube image.

## *start*

The first channel of the cube image. The units of *start* will decide whether the user means \'channel index\', \'frequency\' or \'velocity\':

-   *start=3* : channel 3 of the first spw in the selected list (irrespective of channels selected using the \'spw\' parameter)  
-   *start=\'1.2GHz\'* : start frequency. The output channels are equidistant in frequency.
-   * start=\'15 km/s\'* : start velocity.   if *veltype=\'RADIO\'*, channels are equidistant in both frequency and velocity.   If *veltype=\'OPTICAL\' or  \'Z\',* the channels are equidistant in velocity but not in frequency.  Also see *veltype* section below.

## *width*

The channel width of the resulting image cube. If *width* has units, it has to be the same units as start. If specified as an integer, it is taken as N times the width of a single data channel. For irregular channels in either frequency or velocity, a reasonable default for the width of a single data channel will be calculated.  

*If start* is* *specified in velocity and the *width* is not specified (default), then the output image will be ascending velocities (or descending frequencies) with the velocity specified in *start* as the first image channel. Also note that since the channel frequencies in the MS can be descending or ascending order, the  appropriate sign (\"+\" or \"-\" although \"+\" can be omitted) should be used for the width when the frequency or velocity specification is used to avoid any confusion.

## *outframe*

Spectral reference frame in which to interpret *start*. This is also the frame to which the base frame of the cube image will be set for *mode=\'cube\'*. For *mode=\'cubesrc\'*, the option of specifying start in the SOURCE frame will also be allowed.

## *veltype*

Velocity option in which to interpret start if units are \'km/s\' : 

-   RADIO: velocity in \'radio definition\': $\frac{v_{rad}}{c} = 1 - \frac{f}{f_{0}} = \frac{z}{1+z}$
-   OPTICAL: velocity in \'optical definition\': $\frac{v_{opt}}{c} = \frac{f_{0}}{f} - 1 = z$
-   Z:  the same as OPTICAL
-   RATIO: $\frac{v}{c}=\frac{f}{f_{0}}$  \* This is accepted but there will be no real interpretation of the velocity of this type.
-   BETA: relativistic definition: $\frac{v}{c}=\frac{1-\left(\frac{f}{f_{0}}\right)^2}{1+\left(\frac{f}{f_{0}}\right)^2}$
-   GAMMA: $ \frac{v}{c}=\frac{1}{\sqrt{1-BETA^2}} = 1 - \frac{1+\left(\frac{f}{f_{0}}\right)^2}{2\frac{f}{f_{0}}}$ \* This is accepted but there will be no real interpretation of the velocity of this type.

## *restfreq*

A vector of rest frequencies, which will be encoded in the output image. If this parameter is left empty, the list of rest frequencies encoded in the SOURCE table corresponding to the field being imaged will be used. The first rest frequency in the list will be used to interpret *start* when its units indicate a velocity specification.

## *sysvel*

Systemic velocity of a source (only for *mode=\'cubesrc\'*)

## *sysvelframe*

Frequency frame with respect to which the systemic velocity is specified (only for *mode=\'cubesrc\'*)

## *interpolation*

Relevant when image channel widths \> data channel widths and/or *start* is offset from the data start. This parameter is used irregardless of whether time-dependent frame conversions happen or not. It is not used **only **when *start* and *width* are aligned between the data channels and image channels and no time-dependent frequency relabeling is needed.

## *chanchunks *

For large image cubes, the gridders can run into memory limits as they loop over all available image planes for each row of data accessed. To prevent this problem, we can grid subsets of channels in sequence so that at any given time only part of the image cube needs to be loaded into memory. This parameter controls the number of chunks to split the cube into.

## *perchanweightdensity*

When calculating weight density for Briggs style weighting in a cube, this parameter determines whether to calculate the weight density for each channel independently or a common weight density for all of the selected data (the default). This parameter has no meaning for continuum (*specmode=\'mfs\'*) imaging but for cube imaging *perchanweightdensity=True* is a recommended alternative option that provides more uniform sensitivity per channel for cubes, but with generally larger psfs than the *perchanweightdensity=False*. See the **tclean** task pages for more information.

 

<div class="alert alert-info">
**NOTE on data selection via 'spw'**

The user should select a range larger than what the image will need, and not try to fine-tune the list of channels. The channel mapping and binning process will pick and grid only those data channels that actually map into image channels. This process is already optimized for performance.
</div>

<div class="alert alert-info">
**Note on image channel order of the output cube
**

The *start* parameter defines the spectral coordinate of the first image channel while the sign of *width* parameter controls direction of the increment along the spectral axis. If *width* is unspecified, and if *start* is defined as a velocity or frequency, the image channels will be ordered such that it always increases in value in the unit specified in *start* with increasing channel number. This is regardless of whether spectral axis order of the input visibility data is increasing or decreaseing in frequency. For example, start='-15km/s' with result in the image with channel 0 being -15km/s and becomes more positive as the image channel number increases. For *start* specified in channel (e.g. start=5)  with an unspecified *width*, image channel frequency axis order will depend on the frequency order of the input visibility data. For a full control of the spectral axis order in the output image, the user is encouraged to set *width*.
</div>


# Using Output Images from tclean

Images from **tclean** will have LSRK or another frame specified in outframe or SOURCE or UNDEFINED or REST as the base frame. The spectral axis of the base frame is always encoded in frequency in the output images. A regularly spaced set of frequencies is represented by the *start*/*width*/*nchan* parameters are listed in the image header. An irregularly spaced set of frequencies is encoded as a tabular axis.

## Conversion Layer of the Spectral Reference Frame

One can attach a conversion layer for a different spectral referance frame to the image using the **imreframe** task or a tool script that uses cs.setconversiontype() on top of the base frame.

The Viewer will, by default, will display in the base frame of the image if no conversion layer is attached. However, if the conversion layer is attached, it will honor the frame in the conversion layer and relabel image frequencies on-the-fly while displaying the spectral coordinate. The Viewer also has options to temporarily change the frame to any frequency frame or velocity convention with or without the conversion layer.

Note that conversion layers from LSRK to TOPO/GEO (time-independent frame to time-dependent frame) will be tied to one particular time during the observation. Our convention is the start time of the dataset being imaged.  Tool level scripts using the imageanalysis (ia) and coordinatesystem (cs) modules can be used to extract lists of frequencies or velocities in any spectral frame and velocity convention. Within a conversion layer, the commands csys = ia.coordsys(); csys.toworld( \[0,0,0,5\] ) will give the frequency of channel 5 in the frame of the conversion layer. With no conversion layer, it will list channel 5 in the base frame of the image ( i.e. LSRK ). Velocities can be read out using csys helper functions, e.g., csys.(set)restfrequency(XXX); csys.frequencytovelocity( 1.5, \'GHz\', \'RADIO\', \'km/s ) . Several other spectral axis relabeling options are possible in combination with the measured (me) module.  

CASA Images can finally be exported to the FITS format, during which frame conversions are hard-coded.

Image channels can be regridded using the imregrid task, if the user needs an explicit regrid instead of only frequency-axis relabeling.

 

# Notes on the Frequency Frame Conversions

Conversion between the different types is done with the standard MeasConvert class (MFrequency::Convert, MRadialVelocity::Convert, MDoppler::Convert). This is what is encoded in the conversion layer of CASA Images.

Some conversions are only possible if the following frame information is available:

1.  Conversion to/from REST needs Radial Velocity information. The *sysvel* parameter in *mode=\'cubesrc\'* will be used for this. For an MS already at REST, no conversions are needed.
2.  Conversion to/from TOPO and GEO needs Epoch information. This is set in the conversion layer for *mode=\'cube\'* as the start time of the MS (after the data selections are applied) and can be modified via the **imreframe** task with *outframe=\'TOPO\'* or *\'GEO\'* and subparameter epoch.
3.  Conversion to/from TOPO needs Position information. This is read from the input MS, or Image header.
4.  All conversions need Direction information. This is the image center from the Image header.

<div class="alert alert-warning">
**Alert:** Conversion between the different frequencies can, due to relativistic effects, only be done approximately for very high (order c) radial velocities. Rather than convert between frequencies, a better approach would be to start from radial velocities and a rest frequency.
</div>

<div class="alert alert-warning">
**Alert:** For large radial velocities (of order c), the conversions are not precise, and not completely reversable, due to unknown transverse velocities, and the additive way in which corrections are done. They are correct to first order with respect to relativistic effects.
</div>

