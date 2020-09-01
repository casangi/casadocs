

# Region Files 

CASA Region Text Files usage and definition

## Regions (*region*)

The *region* parameter points to a CASA region which can be directly specified or listed in a ImageRegion file. An ImageRegion file can be created with the CASA viewer's region manager, or directly using the [CASA region file (crtf) syntax](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/region-file-format). Typically ImageRegion files will have the suffix \".crtf\" for CASA Region Text Format.

For example:

```
region='circle[[18h12m24s, -23d11m00s], 2.3arcsec]'
```

or

```
region='myimage.im.crtf'
```

to specify a region file. For the most part, the *region* parameter in tasks only accepts strings (e.g. file names, region shape descriptions) while the *region* parameter in **ia** tool methods only accepts python region dictionaries (e.g. produced using the **rg** tool).

 

<div class="alert alert-warning">
**Alert:** When both the *region* parameter and any of *box*/*chans*/*stokes* are specified simultaneously, the task may perform unwanted selections. While it is safest to only specify one of these (sets of) parameters, the following rules apply:
</div>

For image analysis tasks and tool methods which also accept the box, chans, and/or stokes parameters, the following rules apply if the region parameter is specified:

-   If region is specified as a python dictionary (eg such as various rg tool methods return), a binary region file, or a region-in-image, then it is not permissable to specify any of the box, chans, or stokes parameters.
-   If the region parameter is specified to be a CRTF file name, or a CRTF region    string, the following rules apply:    -   If box is specified, the resulting selection is the union of the box specification with any regions in the CRTF file/string. This is the equivalent of translating the box specification into the equivalent \"box\" CRTF specification and prepending that specification to the specified CRTF file/string in the region parameter.
    -   If chans is specified, it must be able to be represented as a single contiguous range of channels. In this case, the chans specification overrides any global or per-region range specification in the CRTF file/string, and is used as the global spectral range selection for all regions in the CRTF file/string.
    -   If stokes is specified, this specification overrides any global or per-region corr specification in the CRTF file/string, and is used as the global correlation selection for all regions in the CRTF file/string.

<div class="alert alert-info">
**NOTE:** The CASA image analysis tasks will determine how a region is projected on a pixel image. The current CASA definition is that when the center of a pixel is inside the region, the full pixel is considered to be included in the region.  If the center of the pixel is outside the region, the full pixel will be excluded. Note that the CASA viewer behavior is not entirely consistent and for rectangles it assumes that *any* fractional pixel coverage will include the entire pixel. For other supported shapes (ellipses and polygons), however, ithe viewer adheres to the \'center of pixel\' definition, consistent with the image analysis tools and tasks. 

For purely single-pixel work regions may not necessarily be the best choice and alternate methods may be preferable to using regions, eg. **ia.topixel**, **ia.toworld**, **ia.pixelvalue**.
</div>

<div class="alert alert-warning">
**ALERT:** Some region file specifications are not recognized by the viewer, the viewer only supports rectangles (box), ellipses, and polygons.
</div>

 

 

 

