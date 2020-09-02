

# Common Task Parameters 

Description of parameters commonly used in Image Analysis tasks

## Common Image Analysis Task Parameters

Certain parameters are present in many image analysis tasks. These include: 

 

### *imagename*

The *imagename* parameter is used to specify the image(s) on which a task should operate.  In most tasks, this will be a string containing the image name, but in some tasks, this can be a list of strings, as for example, in **immath**. Most image analysis tasks accept both CASA images and FITS images, although we recommend working with CASA images. 

 

### *outfile* 

The *outfile* parameter specifies the name (in string format) of the file that the task should output.  This parameter is only present in tasks that produce processed files (typically images) as output.  It will therefore not be present for tasks that return python dictionaries, arrays, or other data types.  

 

### *axes*

The *axes* parameter is used to specify the image axes that the task should operate on, and the user should input a list of integers for this (e.g. \"axes = \[0,1\]\").  CASA images typically have the following axis order (python indices are zero-based): Axis 0 = RA, 1 = DEC, 2 = Stokes parameter, and 3 = Frequency. The **imhead **task can be used to confirm the axis specifications in the data cube of interest, and the axes may differ from the above sequence, particularly when using FITS data cubes or CASA images that were converted from FITS files.  In the examples, we assume the above axis order. 

To obtain statistics across RA and DEC for each velocity channel, the user would run the **imstat** task (**imstat** stands for \"image statistics\") with \"axes = \[0,1\]\".  To obtain statistics over the spectral axis, one would run imstat with *axes = \[3\]*.  

  

### *box, chans, stokes*

The box, chans, and stokes parameters are used to select parts of an image cube for the task to operate on.  If a box is applied, the task will operate only on a specific spatial region (e.g. *box = \'100,100,200,200\'* will only operate on pixels in the range (100,100) \<= (x,y) \<= (200,200) ). If specific channels are specified through chans, the task will select that segment of the spectral axis (e.g. *chans = \'30\~45\'* will operate on channels 30 through 45).  In the same way, stokes selects specific Stokes parameter axes, as e.g. s*tokes = \'I\'*.  Further detail is provided in the \'[Image Selection Parameters](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/image-selection-parameters)\' page.  

 

### *mask* 

The mask parameter tells the task to operate on specific segments of the image cube, as set by a mask.  The input for the mask parameter may be a conditional statement in LEL string format (e.g. *mask = \' \"ngc5921.im \> 0.5\'*, which selects all pixels in that image that have values larger than 0.5 and zeros out all other pixels), or may be a Boolean True/False cube or an Integer zero/non-zero cube. The task will not operate on pixels that are \"masked\", or zeroed out.  See the \'[Image Masks](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/image-masks)\' page for more detail and examples of usage.  


### *stretch* 

This parameter can be True or False, with a default value of False.  Set *stretch = True* when applying a single-plane mask to a full image cube.  As an example, if you have a mask in a single spectral channel image that you wish to apply to all spectral channels in a cube, you would \"stretch\" the mask over all of the channels. The mask can also be stretched over all Stokes parameter planes for polarization images.

 

## Returned Python Dictionaries 

Many image analysis tasks return python dictionaries with information that is also printed to the logger. The dictionaries can be assigned to a variable and then used later for other scripting purposes. In the following the output of imstat is assigned to the python dictionary \'test_stats\':

```
CASA <20>: test_stats=imstat(imagename='test.image')

CASA <21>: test
Out[21]:
{'blc': array([0, 0, 0, 0], dtype=int32),
'blcf': '17:45:40.899, -29.00.18.780, I, 1.62457e+10Hz',
'max': array([ 0.49454519]),
'maxpos': array([32, 32, 0, 0], dtype=int32),
'maxposf': '17:45:40.655, -29.00.15.580, I, 1.62457e+10Hz',
'mean': array([ 0.00033688]),
'medabsdevmed': array([ 0.]),
'median': array([ 0.]),
'min': array([-0.0174111]),
'minpos': array([15, 42, 0, 0], dtype=int32),
'minposf': '17:45:40.785, -29.00.14.580, I, 1.62457e+10Hz',
'npts': array([ 4096.]),
'q1': array([ 0.]),
'q3': array([ 0.]),
'quartile': array([ 0.]),
'rms': array([ 0.00906393]),
'sigma': array([ 0.00905878]),
'sum': array([ 1.37985568]),
'sumsq': array([ 0.3365063]),
'trc': array([63, 63, 0, 0], dtype=int32),
'trcf': '17:45:40.419, -29.00.12.480, I, 1.62457e+10Hz'}
```

A description of how to deal with Python dictionaries is given in \'[Python and CASA](http://casa.nrao.edu/casadocs/stable/usingcasa/python-and-casa#figid-casapythondictionaries)\'.

 

