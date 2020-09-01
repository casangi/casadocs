

# Image Analysis Tools 

Using the toolkit for image analysis.

# Summary

The CASA image analysis module contains an image analysis tool with numerous methods, as well as several higher level tasks. The tasks free users from the burden of resource management, and offer what many consider to be a more user-friendly interface available via the input \<taskname\> CASA command. In many cases, image analysis tasks are really just simple wrappers around analogous tool methods (e.g., the **imcollapse** task is just a relatively simple wrapper around the **ia.collapse**() tool method call), although in some cases, such as with the **imregrid** task, the mapping is not as simple, and much more goes on \"under the hood\" of a task.

 

## Overview of Image Analysis Tool Functionality

At the heart of the image analysis module is the image analysis tool. An image analysis tool provides access to CASA images. Currently only single-precision, floating-point CASA images are supported by all methods in the image analysis tool and complex-valued images are supported by many, but not all, methods.

The default, global image analysis tool is named **ia**. New, initially-unattached image analysis tools can be created via

```
my_new_ia = iatool()
```

Image analysis tools also provide direct (native) access to FITS and Miriad images, although such access is read-only. These foreign formats to CASA format. For optimum processing speed, it is highly recommended to convert foreign formats to CASA images.

It is important to note that many methods return new image analysis tools that are attached to an image that method has created. Even if one does not intend on using this returned tool, it is important to capture it and run **ia.done**() on it or it will continue to use resources unnecessarily, e.g.

```
new_image_tool = ia.collapse("my_collapsed.im")
# do things with new_image_tool and then run done() on it
new_image_tool.done()
```

### Tool Manipulation

-   **ia.close**(): Detach tool from image and perform required clean up.
-   **ia.done**(): Detach tool from image and perform required clean up and optionally removed attached image.
-   **ia.isopen**(): Determines if there is an image attached to the tool.
-   **ia.newimage**(): Create a new image analysis tool using an image.
-   **ia.newimagefromarray**(): Create a new image analysis tool from a numpy array.
-   **ia.newimagefromfile**(): Create a new image analysis tool using an image.
-   **ia.newimagefromfits**(): Create a new image analysis tool using a FITS image.
-   **ia.newimagefromimage**(): Create a new image analysis tool using an image.
-   **ia.newimagefromshape**(): Create a new image analysis tool using an image shape.
-   **ia.open**(): Attach the image analysis tool to the specified image.
-   **ia.type**(): Tool type. Always returns \'image\'.

### FITS Conversion

There is functionality to interconvert between CASA images and FITS files. There is also native access to FITS files.

-   **ia.fromfits**(): Convert a FITS image file to a CASA image
-   **ia.tofits**(): Convert a CASA image to a FITS file.

### ImageCreation

There are various ways to create CASA images from various data structures.

-   **ia.fromarray**(): Create a CASA image from a numpy array of pixel values.
-   **ia.fromshape**(): Create a CASA image of a specified shape.
-   **ia.maketestimage**(): Create a test image from a FITS file in the CASA data repository.

### Image Destruction

-   **ia.remove**(): Delete the attached image from disk.
-   **ia.removefile**(): Delete the specified image from disk.

### Image Interrogation

Various metadata and pixel data can be interrogated.

-   **ia.beamarea**(): Get the image synthesized beam area.
-   **ia.boundingbox**(): Get the bounding rectangular box which circumscribes the specified region.
-   **ia.brightnessunit**(): Get the image brightness unit.
-   **ia.commonbeam**(): For an image with multiple beams, compute the size of the smallest beam that circumscribes all of the image\'s beams.
-   **ia.getchunk**(): Get pixel or mask values from (a specified rectangular region of) an image.
-   **ia.getregion**(): Get pixel or mask values from a specified region of an image.
-   **ia.haslock**(): Determines if the image has a lock associated with it.
-   **ia.history**(): Get the history information from an image.
-   **ia.miscinfo**(): Retrieve \"miscellaneous\" metadata associated with an image.
-   **ia.name**(): Get the image name.
-   **ia.pixelvalue**(): Get the pixel and mask values at a specified location of an image.
-   **ia.restoringbeam**(): Get information about the synthesized beam(s) of an image.
-   **ia.shape**(): Get image shape.
-   **ia.summary**(): Get various metadata of an image.

### Manipulation of Image Metadata

-   **ia.lock**(): Acquire a lock on the attached image.
-   **ia.rename**(): Rename the image.
-   **ia.rotatebeam**(): Rotate the synthesized beam(s) of an image through a specified angle.
-   **ia.setbrightnessunit**(): Set image brightness unit.
-   **ia.sethistory**(): Add history records to an image.
-   **ia.setmiscinfo**(): Set image miscellaneous metadata.
-   **ia.setrestoringbeam**(): Set image synthesized beam(s).
-   **ia.unlock**(): Release the image lock.

### Manipulation of Image Pixel and Pixel Mask Values

-   **ia.calc**(): Replace the pixel values in the attached image with the values determined from the specified LEL expression.
-   **ia.calcmask**(): Compute a pixel mask based on an LEL expression.
-   **ia.insert**(): Insert the pixel values of another image into an image.
-   **ia.maskhandler**(): Manipulate image pixel masks.
-   **ia.modify**(): Modify an image using a model specified by a component list.
-   **ia.putchunk**(): Set pixel values (in a specified rectrangular region) of an image.
-   **ia.putregion**(): Set pixel values in a specified region of an image.
-   **ia.replacemaskedpixels**(): Set masked pixel to a specified value.
-   **ia.set**(): Set pixel or mask values.

### Operations on Images

Various operations can be performed on images which result in new images.

-   **ia.addnoise**(): Add noise to an image.
-   **ia.boxcar**(): Boxcar smooth an image along a specified axis.
-   **ia.decimate**(): Remove planes of an image.
-   **ia.collapse**(): Collapse image along specified axis, computing aggregate function of pixels along that axis.
-   **ia.convolve**(): Convolve an image with an array or with another image.
-   **ia.continuumsub**(): Subtract continuum emission in a spectral line image.
-   **ia.convolve2d**(): Convolve an image with a two-dimensional kernel.
-   **ia.crop**(): Crop pixels from the edge of an image.
-   **ia.fft**(): Fast Fourier Transform (FFT) the image.
-   **ia.hanning**(): Hanning smooth an image along a specified axis.
-   **ia.imagecalc**(): Create an image from an LEL expression.
-   **ia.imageconcat**(): Concatenate multiple images along a specified axis.
-   **ia.makecomplex**(): Create a complex-valued image from two float-valued images representing the real and imaginary values.
-   **ia.pad**(): Pad the edges of an image with pixels.
-   **ia.pv**(): Create a position-velocity image.
-   **ia.pbcor**(): Construct a primary beam corrected image.
-   **ia.rebin**(): Rebin pixel values by specified factors.
-   **ia.regrid**(): Regrid an image to a specified coordinate system.
-   **ia.rotate**(): Rotate the direction coordinate of an image.
-   **ia.sepconvolve**(): Convolve an image with a separable kernel.
-   **ia.subimage**(): Create an image by specifying a region of an image.
-   **ia.transpose**(): Transpose an image.

### Image Analysis

-   **ia.convertflux**(): Interconvert between peak intensity and flux density for a specified Gaussian source.
-   **ia.decompose**(): Decompose complex source into individual two dimensional models.
-   **ia.deconvolvecomponentlist**(): Deconvolve a component list from the restoring beam.
-   **ia.findsources**(): Find strong point sources in an image.
-   **ia.fitcomponents**(): Fit two-dimensional models to the direction plane(s) of an image.
-   **ia.fitprofile**(): Fit one-dimensional models along an axis image.
-   **ia.histograms**(): Compute histograms from the pixel values of an image.
-   **ia.maxfit**(): Find maximum value in the direction coordinate and do a simple parabolic fit.
-   **ia.moments**(): Compute moments of an image.
-   **ia.statistics**(): Compute image statistics using various algorithms.
-   **ia.twopointcorrelation**(): compute two point autocorrelation functions from the image

### Image Coordinates

The coordinate system of an image can be manipulated. Specific coordinate system values can be directly manipulated using the CASA coordinate system tool.

-   **ia.adddegaxes**(): Add degenerate axes to an image\'s coordinate system.
-   **ia.coordmeasures**(): Convert from pixel to world coordinates, and return as a measure.
-   **ia.coordsys**(): Retrieve the image coordinate system as a CASA coordinate system tool.
-   **ia.setcoordsys**(): Replace the image\'s coordinate system with another.
-   **ia.topixel**(): Convert from world to pixel coordinates.
-   **ia.toworld**(): Convert from pixel to world coordinates.

###  Miscellaneous

-   **ia.makearray**(): Create a numpy array of specified shape and value.

 

## Overview of Image Analysis Tasks

### FITS Conversion

-   **exportfits**: Convert a CASA image to a FITS image.
-   **importfits**: Convert a FITS image to a CASA image.

### Interrogation and Manipulation of Image Metadata

-   **imhead**: Summarize, interrogate, and modify image metadata
-   **imhistory**: List and append records to image history.

### Operations on Images

Various operations can be performed on images which result in new images.

-   **imcollapse**: Collapse image along specified axis, computing aggregate function of pixels along that axis.
-   **imcontsub**: Subtract continuum emission in a spectral line image.
-   **immath**: Perform mathematical operations upon images.
-   **immoments**: Compute image moments.
-   **impbcor**: Construct a primary beam corrected image.
-   **impv**: Create a position-velocity image.
-   **imrebin**: Rebin pixel values by specified factors.
-   **imregrid**: Regrid an image to a specfied coordinate system.
-   **imsmooth**: Perform various two-dimensional convolutions.
-   **imsubimage**: Create an image by specifying a region of an image.
-   **imtrans**: Transpose an image.
-   **specsmooth**: Perform various one-dimensional convolutions.

### Image Analysis

-   **imfit**: Fit two-dimensional models to the direction plane(s) of an image.
-   **imstat**: Compute image statistics using various algorithms.
-   **imval**: Interrogate pixel values.
-   **rmfit**: Compute rotation measure.
-   **specfit**: Fit one-dimensional models along a specified axis of an image.
-   **specflux**: Report spectral profile and calculate spectral flux over a user-specified region.
-   **spxfit**: Fit spectral index models along a specified axis of an image.

 

# General

A persistent CASA image is stored on disk. Several files and subdirectories containing the image pixel data, mask data, and metadata are stored in a directory. The name of that directory is the name of the image.To access an existing persistent image, use the **ia.open**() method:

```
ia.open("my.im")
```

When you are finished with the image, it is important to close the tool so it no longer uses system resources:

```
ia.close()
```

It is also possible to create temporary images, which, if small enough, are stored completely in memory and destroyed when the user is finished with them. Creating such images is usually accomplished by running one of the image creation methods, and leaving the name of the output image blank (this is usually the default). So, for example, to create an image of a specified shape, one might run:

```
ia.fromshape(shape=[20,20,20])
```

As with persistent images, it is important to close the image analysis tool when finished with temporary images. In this case, the temporary image will be destroyed.

Persistent images can, in principle, be stored in a variety of ways. For example, the image could be stored row by row; this is the way that most older generation packages store images. It makes for very fast row by row access, but very slow in other directions (e.g. extract all the profiles along the third axis of an image). A CASA image is stored with what is called tiling. This means that small multi-dimensional chunks (a tile) are stored sequentially. It means that row by row access is a little slower, but access speed is essentially the same in all directions.

Here are some simple examples using image tools.

```
#access the CASA "test" FITS image and write it to a CASA image named "zz"
ia.maketestimage('zz',overwrite=true)
```

```
# print a summary to the logger and capture the summary metadata in variable "summary"
summary = ia.summary()
```

```
# evaluate image statistics and save the stats info to a variable called "stats"
stats = ia.statistics()
```

```
# create a rectangular region using the rg tool
box = rg.box([10,10], [50,50])
```

```
# create a subimage of that region, and name the resulting image "zz2"
# capture the new image tool attached to "zz2" in the variable "im2"
im2 = ia.subimage('zz2', box, overwrite=true)
```

```
# get statistics for zz2 and store the results in the variable "stats2"
stats2 = im2.statistics()
```

```
print "CLEANING UP OLD zz2.amp/zz2.phase IF THEY EXIST. IGNORE WARNINGS!"
ia.removefile('zz2.amp')
ia.removefile('zz2.phase')
# FFT subimage and store amp and phase
im2.fft(amp='zz2.amp',phase='zz2.phase')
```

```
# close image tools
im2.close()
ia.close()
```

 

# Foreign Images

The image analysis tool also provides native, read-only access to some foreign image formats. Presently, these are FITS (Float, Double, Short and Long pixel values are supported) and Miriad. This means that you don\'t have to convert the file to native CASA format in order to access the image. For example:

```
# Assumes environment variable is set
pathname = os.environ.get("CASAPATH")
pathname = pathname.split()[0]
datapath1 = pathname + "/data/demo/Images/imagetestimage.fits"
# Access FITS image
ia.open(datapath1)
ia.close()
# Access Miriad image
ia.open('im.mir')
ia.close()
# create a new image tool attached to the FITS image
ims = ia.newimagefromimage(infile=datapath1)
# create a region record representing the inner quarter of an image
innerquarter=rg.box([0.25,0.25],[0.75,0.75],frac=true)
# create a subimage of the inner quarter of the FITS image
subim = ims.subimage(region=innerquarter)
# done with the tools, release resources
ia.close()
ims.close()
```

In general, any parameter to a task or a tool method which accepts an image name will support CASA, FITS, or Miriad images.

There are some performance penalties of which you should be aware. First, because CASA images are tiled (see above), performance is the same regardless of how the images are accessed. In contrast, FITS and Miriad images are not tiled. This means that the performance when accessing these types of images will be poorer for certain operations. e.g., extracting a profile along the third axis of an image. Second, for FITS images, masked values are indicated via a \"magic value\'\'. This means that the mask is worked out on the fly every time the image is accessed.

If you find performance is poor or if you want a writable image, then use appropriate tool methods to convert the foreign format image to a CASA image.

 

# Virtual Images

It is possible to have an image analysis tool that is not associated with a single persistent image; these are called \"virtual\'\' images. For example, with **ia.imagecalc**(), one can create an expression which may contain many images. You can write the result of the expression to a persistent image, but if you wish, you can also just maintain the expression, evaluating it each time it is needed - nothing is ever written out to disk in this case. There are other image methods like this (the documentation for each one explains what it does). The rules are:

-   If you specify the *outfile* or equivalent parameter, then the output image is always persistent with the name specified.
-   If you leave the *outfile* or equivalent parameter unset, then if possible, a virtual image will be created. Sometimes this virtual image will be an expression as in the example above (i.e. it references other images) or a temporary image in memory, or a temporary image on disk. The **ia.summary**() method will list the type of image. When you **ia.close**() that image tool, the virtual image will be destroyed.
-   If you leave the *outfile* or equivalent parameter unset, and the called method cannot create a virtual image, it will create a persistent image with a name of its choice (sometimes input plus function name).
-   A virtual image can always be written to disk as a persistent image with the **ia.subimage**() method.

 

# Coordinate Systems

An image contains a coordinate system. A coordinate system tool is used to manipulate a coordinate system. An image tool allows you to recover the coordinate system into a coordinate system tool via the **ia.coordsys**() method. You can set a new image coordinate system with the **ia.setcoordsys**() method.

You can do some basic world to pixel and vice versa coordinate transformations via the image tool **ia.topixel**(), **ia.toworld**(), and **ia.coordmeasures**() methods.

 

# Lattice Expression Language (LEL)

LEL allows you to create mathematical expressions involving images. For example, add the corresponding pixel values of two images, or multiply the miniumum value of one image by the square root of the pixel values of another image. The LEL syntax is quite rich and is described in detail on the [Lattice Expression Language](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/lattice-expression-language-lel) pages.

<div class="alert alert-info">
**IMPORTANT NOTE**: Image names which contain \"special\" characters (eg, \"+\", \"-\", etc) must be properly escaped. See the *Lattice names* subsection of the *Expressions* section in the aforementioned document for details.
</div>

To produce an image that is the result of an LEL computation, use the **ia.calc**() or **ia.imagecalc**() image analysis tool methods. Here are some examples.

In this example the image analysis tool is attached to the persistent image named \"zz\". This image\'s name is used in an LEL expression which adds the pixel values of that image to the sine of the pixel values of that image (for trigonometric LEL functions, pixel values are taken to be in radians). Note that the **ia.calc**() method overwrites the pixel values of the attached image with the values computed by the LEL expression. To create a new image without overwriting the pixel values of the image associated with the image tool, use the **ia.imagecalc**() method.

```
ia.maketestimage('zz', overwrite=true)
# Make the minimum value zero
ia.calc('zz + min(zz)')
ia.close()
```

This example demonstrates ways of dealing with image names which have special characters.

```
ia.maketestimage("test-im", overwrite=true)
# escape special characters using a ""
im1 = ia.imagecalc(pixels='test-im + 5')
# or surround the entire image name with quotes
im2 = ia.imagecalc(pixels='"test-im" + 5')
# or
im3 = ia.imagecalc(pixels="'test-im' + 5")
im1.close()
im2.close()
im3.close()
ia.close()
```

 

# Region Selection

A region designates a subset of pixels in the image in which one is interested. The region is selected based on coordinate information. Such a selection complements on-the-fly masks in which pixels are selected based on a mathematical expression which is tested against their values (see below). Regions may be specified in several ways. The region manager tool (default **rg**) has several methods for generating regions. These methods generally return a dictionary representation of a region which can be used as input for the *region* parameter in various image analysis tool methods and tasks. A region can also be specified by the *box*/*chans*/*stokes* selection parameters in tasks and tool methods which accept them. Regions can also be specified in a special format known as CASA region text format. This format allows for specifying of various region shapes and spectral and polarization extents. This specification can be placed in a file, and in this case, the *region* parameter can be set to the name of that file and the region information will be extracted. Alternatively, the *region* parameter can be set directly to the CRTF specification. The complete CRTF specification can be found in the \"[Region File Format](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/region-file-format)\" section.

 

# Pixel Masks

A pixel mask is a set of boolean values which have a one-to-one correspondence with image pixels. A value of True indicates that pixel is \"good\" (i.e., should be used in computations), while a value of False indicates that pixel is \"bad\". For example, blanked pixels in a FITS image are treated as \"bad\" by CASA. When such a file is imported into a CASA image, a pixel mask is created to reflect the badness of blanked pixels in the FITS image. For persistent CASA images, pixel masks are stored in the same directory in which other image information is stored.

If an image does not have a pixel mask associated with it, all of its pixels are treated as good by CASA.

A CASA image may contain any number of pixel masks and these masks can be managed via the **ia.maskhandler**() image analysis tool method. If an image contains multiple pixel masks, only a maximum of one mask will be used during a run of a task or tool method. This pixel mask is known as the \"default\" pixel mask. The default pixel mask can be set by running **ia.maskhandler**(*set=\"pixelmaskname\"*). You can also indicate that none of the image pixel masks should be applied by running **ia.maskhandler**(*set=\"\"*). In this case, all pixels are considered to be good. Pixel masks can also be viewed in the output of the **ia.summary**() image analysis tool method and **imhead** task output.

The **ia.putregion**() image analysis tool method run with *usemask=True* can be used to change the values of the default pixel mask. The image analysis tool method **ia.set**() can also be used to set the values of the default pixel mask. The image analysis tool method **ia.calcmask**() can be used to create a new pixel mask based on a boolean LEL expression.

 

# On The Fly Pixel Masks

Most image analysis tool methods and tasks accept a parameter named *mask*, which represents an OTF (on-the-fly) pixel mask that is computed for use by only that tool method or task (the exception being the **ia.calcmask**() image analysis tool method in which case a persistent pixel mask is attached to the image; see previous section). This parameter may be specified in one of two ways:

1.  As an LEL boolean expression, or
2.  as a single image name, in which case, pixel values \>= 0.5 are treated as True (good) values, and all others are treated as False.

If the image has a default pixel mask, the mask used in the computation is the logical AND of the OTF pixel mask and default pixel mask. For example:

```
ia.maketestimage('zz', overwrite=true)
# create default pixel mask for which only positive valued pixels are good
ia.calcmask("zz>0")
# compute statistics by specifying an OTF mask, which gets ANDed with
# the default pixel mask, effectively making only pixels with values between 0 and 1 "good"
# for the statistics computation
stats = ia.statistics(mask="zz < 1")
ia.close()
```

The mask expression must in general conform in shape and coordinates with the input image.

A useful LEL function to use in conjunction with the *mask* parameter is **indexin**(). This enables the user to specify a mask based upon selected pixel coordinates or indices rather than image values. For example:

```
ia.fromshape(shape=[20])
# only pixels in the specified planes along the specified axis are considered good.
# prints [False False False False True True True True True True False False False False True False False False True True]
print ia.getregion(mask='indexin(0, [4:9, 14, 18:19])',getmask=true)
ia.close()
```

 

# Regions As Pixel Masks

Regions, which have previously been discussed, are just another form of an OTF pixel mask, and in fact, if one specifies the *region* and *mask* parameters simultaneously, and the associated image also has a default pixel mask, all these three types of pixel masks are just ANDed together to form the pixel mask that is used in the resulting computation. One can even convert a region specification into a persistent pixel mask by specifying the *region* parameter in e.g., the **ia.fromimage**() image analysis tool method. The created image will have a default pixel mask that is a representation of the region specified (if the initial image had a default pixel mask, then that will be ANDed with the region specification to form the default pixel mask of the resulting image).

 

