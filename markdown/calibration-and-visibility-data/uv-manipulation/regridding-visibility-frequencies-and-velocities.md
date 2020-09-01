

# Regrid Frequency/Velocity 

Spectral regridding of the MS (cvel)

Although not strictly a calibration operation, spectral regridding of a MS is available to aid in calibration operations (e.g. continuum subtraction) and preparation for imaging. For this purpose, the **cvel** task has been developed.

The inputs are:

```
#  cvel :: regrid an MS to a new spectral window / channel structure or frame
vis                 =         ''        #  Name of input MeasurementSet
outputvis           =         ''        #  Name of output MeasurementSet
passall             =      False        #  Pass through (write to output MS) non-selected data with
                                        #   no change
field               =         ''        #  Select field using field id(s) or field name(s)
spw                 =         ''        #  Select spectral window/channels
selectdata          =       True        #  Other data selection parameters
timerange           =         ''        #  Range of time to select from data
array               =         ''        #  (sub)array indices
antenna             =         ''        #  Select data based on antenna/baseline
scan                =         ''        #  scan number range

mode                =  'channel'        #   Regridding mode
nchan               =         -1        #  Number of channels in output spw (-1=all)
start               =          0        #  first input channel to use
width               =          1        #  Number of input channels to average
interpolation       =   'linear'        #  Spectral interpolation method

phasecenter         =         ''        #  Image phase center: position or field index
restfreq            =         ''        #  rest frequency (see help)
outframe            =         ''        #  Output frame (not case-sensitive, ''=keep input frame)
veltype             =    'radio'        #  velocity definition
hanning             =      False        #   If true, Hanning smooth data before regridding to remove
                                        #   Gibbs ringing.
```

The key parameters for the operation of **cvel** are the regridding *mode*, the output reference *outframe*, *veltype*, *restfreq* and the standard selection parameters (in particular *spw* and *field*).

The syntax for mode options ('*channel*','*velocity*','*frequency*','*channel_b*') has been made compatible with the respective modes of **clean**. The combination of selected *spw* and *mode* will determine the output channels and spw(s):

```
    spw = '0,1'; mode = 'channel'  
       # will produce a single spw containing all channels in spw 0 and 1  
    spw='0:5~28^2'; mode = 'channel'  
       # will produce a single spw made with channels (5,7,9,...,25,27)  
    spw = '0'; mode = 'channel': nchan=3; start=5; width=4  
       # will produce an spw with 3 output channels  
       # new channel 1 contains data from channels (5+6+7+8)  
       # new channel 2 contains data from channels (9+10+11+12)  
       # new channel 3 contains data from channels (13+14+15+16)  
    spw = '0:0~63^3'; mode='channel'; nchan=21; start = 0; width = 1  
       # will produce an spw with 21 channels  
       # new channel 1 contains data from channel 0  
       # new channel 2 contains data from channel 2  
       # new channel 21 contains data from channel 61  
    spw = '0:0~40^2'; mode = 'channel'; nchan = 3; start = 5; width = 4  
       # will produce an spw with three output channels  
       # new channel 1 contains channels (5,7)  
       # new channel 2 contains channels (13,15)  
       # new channel 3 contains channels (21,23)
```

The simplest use of **cvel** is to shift a single spectral window into an output frame. This is done with *mode='channel'*. For example:

```
cvel(vis='test_w3oh_nohann.ms',
     outputvis ='test_w3oh_nohann_chanbary.ms',
     mode='channel',nchan=-1,start=0,width=1,
     interpolation='linear',
     phasecenter='',
     spw='',
     outframe='BARY')
```

will transform all SPWs into the BARY reference frame. This implies a \"software Doppler tracking\", i.e. the SPW definitions are transformed into the BARY frame and in the different integrations of the dataset, the visibilties are regridded into the transformed SPW accounting for the time-dependencies. E.g. if the original SPWs were in reference frame TOPO and thus the movent of the Earth w.r.t. the source will have smeared out line emission, the new SPWs will be in reference frame BARY and the effects of the movement of the Earth will have been removed but the number of channels will remain the same and the frequency resolution will be maximal. 

Mode *channel* is intended to not change the frequency resolution beyond the reference frame transformation or at least only change the resolution in units of whole channels. For most scientific applications we recommend using the *mode='velocity''* and *mode='frequency'* options, as it is easiest to determine what the resulting channel width will be in terms of velocity or frequency bandwidth. For example:

```
cvel(vis='test_w3oh_nohann.ms',
     outputvis ='test_w3oh_nohann_cvellsrk.ms',
     mode='velocity',nchan=45,start='-35.0km/s',width='-0.55km/s',
     interpolation='linear',
     phasecenter='',
     spw='',
     restfreq='1665.4018MHz',
     outframe='LSRK')

cvel(vis='test_w3oh_nohann.ms',
     outputvis ='test_w3oh_nohann_cvelbary.ms',
     mode='velocity',nchan=45,start='-35.0km/s',width='-0.55km/s',
     interpolation='linear',
     phasecenter='',
     spw='',
     restfreq='1665.4018MHz',
     outframe='BARY')
```

will transform a MS into the LSRK and BARYcenter frames respectively.

The sign of the *width* parameter determines whether the channels run along increasing or decreasing values of frequency or velocity (i.e. if the cube is reversed or not).

<div class="alert alert-info">
**Info:** in order to permit the calculation of velocities from the internally stored frequencies, you need to provide a rest frequency in parameter *restfreq* when you operate in mode \'velocity\'. This rest frequency will not be stored with the MS (as opposed to the rest frequency which you provide to the *clean* task which is subsequently stored with the image).
</div>

The intent of **cvel** regridding is to transform channel labels and the visibilities to a spectral reference frame which is appropriate for the science analysis, e.g. from *TOPO* to *LSRK*, e.g. to correct for Doppler shifts throughout the time of the observation. Naturally, this will change the shape of the spectral features to some extent. According to the Nyquist theorem you should oversample a spectrum with twice the numbers of channels to retain the shape. Based on some tests, however, we recommend to observe with at least 3-4 times the number of channels for each significant spectral feature (like 3-4 channels per linewidth). This will minimize regridding artifacts in **cvel**.

If **cvel** has already established the grid that is desired for the imaging, clean should be run with the default *channel* mode (*width=1*). This will avoid additional regridding in **clean**. Hanning smoothing is optionally offered in **cvel**, but tests have shown that already the regridding process itself, if it involved a transformation from *TOPO* to a non-terrestrial reference frame, implies some smoothing (due to channel interpolation) such that Hanning smoothing may not be necessary.

The interpolation method **fftshift** calculates the transformed visibilities by applying a FFT, then a phase ramp, and then an inverse FFT. Note that if you want to use this interpolation method, your frequency grid needs to be equidistant, i.e. it only works in mode velocity with *veltype=radio*, in mode frequency, and in mode channel (in the latter only if the input grid is itself equidistant in frequency). Note also that, as opposed to all other interpolation methods, this method will apply a constant (frequency-independent) shift in frequency which is not fully correct in the case of large fractional bandwidth of the given spectral window.

The task **cvel** can also be used to transform spectral windows into the rest frame of the ephemeris object by setting the parameter *outframe* to "SOURCE" as in the following example:

```
cvel(vis='europa.ms', outputvis='cvel_europa.ms', outframe='SOURCE')
```

This will make **cvel** perform a transformation to the GEO reference frame followed by an additional Doppler correction for the radial velocity given by the ephemeris for the each field. (Typically, this should happen after calibration and after splitting out the spectral widows and the target of interest). The result is an MS with a single combined spectral window in reference frame REST. From this frame, further transformations to other reference frames are not possible.

