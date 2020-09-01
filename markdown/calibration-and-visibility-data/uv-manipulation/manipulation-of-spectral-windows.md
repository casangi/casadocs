

# Manipulate spectral windows 

How to combine, separate, and Hanning smooth spectral windows in mstransform

## Combination of spectral windows

Both **mstransform** and **cvel2** are able to combine SPWs (in **mstransform** by specifying *combinespws = True* and in **cvel2** by default). The algorithm is in general the same as the old **cvel**, however, there are two significant differences in the new framework:

-   **mstransform** is able to only combine SPWs, only regrid each SPW separately or to combine all SPWs and **regrid** them together. The details about independent regridding operations are explained in the following sections. For instance, if you wish to do channel averaging while regridding in **mstransform**, please see the [section on channel averaging](https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/uv-manipulation/channel-average). 
-   **mstransform** and **cvel2** automatically detect combination of SPWs with different exposure, and use the *WEIGHT* column (or *WEIGHT_SPECTRUM* if available) in addition to the geometrical factors to calculate the combined visibility in the overlapping regions.

<div class="alert alert-warning">
**Alert:** For the time being, **mstransform** is not able to combine SPWs with different numbers of channels. This is a limitation in the Visibility Iterator (VI/VB2) layer of CASA.
</div>

The output MS created by **mstransform** and **cvel2** has a uniform binning in spectral axis. If the *width* parameter is not specified then the size of the input bin corresponding to the lowest absolute frequency will be used as the size of the output bin, where the lowest absolute frequency is retrieved from the full list of spectral bins for all the input SPWs (after selection). Remember that in some cases, especially after certain data selection, the lowest frequency might not be part of the first input SPW ID.

Note that when combining SPWs which have different polarization settings only the common polarizations to all SPWs will be part of the output MS.

## Separation of spectral windows

A completely new feature in **mstransform** is the ability to separate an input SPW into several ones, or to combine various input SPWs into a single one with a uniform grid (resolving overlaps or gaps) to then separate it in several output SPWs. This option is activated under the regridding section (therefore by specifying *regridms = True*), together with the *nspw* parameter which when bigger than 1 implies that the input SPW or combination of input SPWs should be separated:

```
#In CASA
regridms = True  # Regrid the MS to a new spw,
    nspw = 1     # Number of output spws to create in output MS.
```

Internally, the framework will combine the selected spws before separating them so that channel gaps and overlaps are taken into account. This sub-parameter will create a regular grid of spws in the output MS. If nchan is set, it will refer to the number of output channels in each of the separated spws.

## Hanning smoothing

Both **mstransform** and **hanningsmooth** are able to perform hanning smoothing (in **mstransform** by specifying *hanning = True* and in **hanningsmooth** by default).  For details on hanning smoothing please refer to the [section on Hanning Smoothing](https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/uv-manipulation/hanning-smoothing-of-uv-data-hanningsmooth) and the **hanningsmooth **task documentation linked here. Please note that both **mstransform **and **hanningsmooth** will create a new MS (i.e. do not have an option to do in-place hanning smoothing). This is the only difference with respect to the old **hanningsmooth** task that existed in previous versions of CASA.  

Note that straightforward channel averaging can be done as described in the [section on channel averaging](https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/uv-manipulation/channel-average).

