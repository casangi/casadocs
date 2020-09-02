

# Recalculate UVW Values 

How to recalculate uvw values using fixvis

Sometimes the u,v,w coordinates of a MeasurementSet are not recorded correctly by the correlator. For instance, if the catalog position of a phase calibrator is in error, the control system will place the phase center on this erroneous position. Although the actual wavefront from the quasar will not be coming from the phase center, the normal calibration process will adjust all the phases to place the quasar there (because the default model is a point source at the phase center), which will yield science target images with wrong absolute positions.

To fix this problem, you can use **fixvis** to shift the raw data on the phase calibrator to have the correct phase center so that your science target will then come out with the correct position. This technique was used in the [Band 9 ALMA SV data on IRAS16293](https://casaguides.nrao.edu/index.php/IRAS16293_Band9_-_Calibration_for_CASA_4.0).

One useful feature of **fixvis** is that it can change the phase center of a MeasurementSet. This can be done with absolute coordinates or using offsets. An example is:

```
fixvis(vis='ngc3256.ms',outpuvis='ngc3256-fixed.ms',field='NGC3256', phasecenter='J2000 10h27m51.6s -43d54m18s')
```

which will recalculate the u,v,w coordinates relative to the new phase center for the field 'NGC3256'. Invoking **fixvis** as follows will instead re-calculate the (u,v,w) values using the existing phase center in the FIELD table of the MS \-- 

```
fixvis(vis='ngc3256.ms',outpuvis='ngc3256-fixed.ms',field='NGC3256')
```

Other parameters **fixvis** accepts are as follows \-- 

```
fixvis :: Recalculates (u, v, w) and/or changes Phase Center

vis = '' #Name of the input visibility set.

outputvis = '' #Name of the output visibility set. (Can be the same #as vis.)

field = '' #Fields to operate on. = all.

refcode = '' #reference frame to convert UVW coordinates to

reuse = True #base UVW calculation on the old values?

phasecenter = '' #use this direction as phase center
```

 

