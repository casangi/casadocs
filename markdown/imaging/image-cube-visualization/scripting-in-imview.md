

# Scripting using imview 

Plotting to a file without invoking the Viewer GUI

# Image Viewer (imview)

The **imview** task offers scriptable access to many **viewer** options. This enables the production of customized plots without invoking the GUI and allows one to open the **viewer** to a carefully selected state.

**imview** has the following inputs:

```
#imview :: View an image
raster      =    {}     #(Optional) Raster filename (string)
                        #or complete raster config
                        #dictionary. The allowed dictionary
                        #keys are file (string), scaling
                        #(numeric), range (2 element numeric
                        #vector), colormap (string), and
                        #colorwedge (bool).
contour     =    {}     #(Optional) Contour filename (string)
                        #or complete contour config
                        #dictionary. The allowed dictionary
                        #keys are file (string), levels
                        #(numeric vector), unit (float), and
                        #base (float).
zoom        =    1      #(Optional) zoom can specify
                        #intermental zoom (integer), zoom
                        #region read from a file (string) or
                        #dictionary specifying the zoom
                        #region. The dictionary can have two
                        #forms. It can be either a simple
                        #region specified with blc (2 element
                        #vector) and trc (2 element vector)
                        #[along with an optional coord key
                        #("pixel" or "world"; pixel is the
                        #default) or a complete region
                        #rectangle e.g. loaded with
                        #"rg.fromfiletorecord( )". The
                        #dictionary can also contain a
                        #channel (integer) field which
                        #indicates which channel should be
                        #displayed.
axes        =    -1     #(Optional) this can either be a
                        #three element vector (string) where
                        #each element describes what should
                        #be found on each of the x, y, and z
                        #axes or a dictionary containing
                        #fields "x", "y" and "z" (string).
out         =    {}     #(Optional) Output filename or
                        #complete output config dictionary.
                        #If a string is passed, the file
                        #extension is used to determine the
                        #output type (jpg, pdf, eps, ps, png,
                        #xbm, xpm, or ppm). If a dictionary
                        #is passed, it can contain the
                        #fields, file (string), scale
                        #(float), dpi (int), or orient
                        #(landscape or portrait). The scale
                        #field is used for the bitmap formats
                        #(i.e. not ps or pdf) and the dpi
                        #parameter is used for scalable
                        #formats (pdf or ps).
```

The *raster* and *contour* parameters specify which images to load and how these images should be displayed. These parameters take python dictionaries as inputs. The fields in these dictionaries specify how the image will be displayed.

An example call to **imview** looks like this:

```
imview(raster={'file': 'ngc5921.clean.image','range': [-0.01,0.03],'colormap': 'Hot Metal 2','scaling': -1},
      contour={'file': 'ngc5921.clean.image'},
      axes={'x':'Declination'},
      zoom={'channel': 7, 'blc': [75,75], 'trc': [175,175],'coord': 'pixel'},
      out='myout.png')
```

The argument to *raster* is enclosed in the curly braces { }. Within these braces are a number of \"key\":\"value\" pairs. Each sets an option in the **viewer**, with the GUI parameter to set defined by the \"key\" and the value to set it to defined by \"value.\" In the example above, file='ngc5921.clean.image' sets the file name of the raster image, range= \[-0.01,0.03\] sets the range of pixel values used for the scaling.

*contour* works similarly to *raster* but can accept multiple dictionaries in order to produce multiple contour overlays on a single image. To specify multiple contour overlays, simply pass multiple dictionaries (comma delimited) in to the *contour* argument:

```
contour={'file': 'file1.image', 'levels': [1,2,3] }, {'file': 'file2.image', 'levels': [0.006, 0.008, 0.010] }
```

*zoom* specifies the part of the image to be shown. The example above specifies a channel as well as the top right corner \"trc\" and the bottom left corner \"blc\" of the region of interest.

*axes* defines what axes are shown. By default, the viewer will show 'x':'Right Ascension', 'y':'Declination' but one may also view position-frequency images.

*out* defines the filename of the output, with the extension setting the file type.

Currently, the following parameters are supported:

```
raster  -- (string) image file to open
           (dict)   file (string)     => image file to open
                    scaling (float)   => scaling power cycles
                    range (float*2)   => data range
                    colormap (string) => name of colormap
                    colorwedge (bool) => show color wedge?
contour -- (string) file to load as a contour
           (dict)   file (string)     => file to load
                    levels (float*N)  => relative levels
                    base (numeric)    => zero in relative levels
                    unit (numeric)    => one in the relative levels
zoom    -- (int)    integral zoom level
           (string) region file to load as the zoom region
           (dict)   blc (numeric*2)   => bottom left corner
                    trc (numeric*2)   => top right corner
                    coord (string)    => pixel or world
                    channel (int)     => channel to display
           (dict)   <region record>   => record loaded
                                         e.g., rg.fromfiletorecord( )
axes    -- (string*3) dimension to display on the x, y, and z axes
           (dict)   x                 => dimension for x-axes
                    y                 => dimension for y-axes
                    z                 => dimension for z-axes
out     -- (string) file with a supported extension
                    [jpg, pdf, eps, ps, png, xbm, xpm, ppm]
           (dict)   file (string)     => filename
                    format (string)   => valid ext (filename ext overrides)
                    scale (numeric)   => scale for non-eps, non-ps output
                    dpi (numeric)     => dpi for eps or ps output
                    orient (string)   => portrait or landscape
```

Examples are also found in help **imview**.

 

# Scripting using the viewer tool

The **viewer** tool may also be used to generate simple figures that can be directly saved to an output image file format (png, jpg, etc). Below is an example.

```
def dispimage(imname=''): 
    qq = viewertool() 
    qq.load(imname) 
    qq.datarange(range=[-0.01,1.1]) 
    qq.colormap(map='Rainbow 3') 
    qq.colorwedge(show=True) 
    qq.zoom(blc=[100,150], trc=[600,640]) 
    qq.output(device='fig_trial.png',format='png') 
    qq.close()
```

Note that only basic controls are available via the **viewertool** interface. For additional customization via a script, please see the following section describing \"Using Viewer state files within a script\". 

 

# Using Viewer state files within a script 

In order to access the full flexibility of the GUI interface in customizing the **viewer** settings and display options, a hand-crafted **viewer** state can be saved, edited, and subsequently restored/rendered via a script that then allows the saving of the figure to a file on disk.

For example:

Step 1 : Customize the **viewer** by hand. For example, choose to open an image, customize the display data ranges, choose a colormap, change axis label properties, change the units of the movie axis label, edit the panel background color, adjust margins and and resize the panel window.

Step 2 : Click on the \"save viewer state\" button on the top control panel of the **viewer**. This will save a .rstr file, which is an xml file containing a complete description of the current state of the **viewer**.  

Step 3 : Edit the text xml file as required. The simplest operation is to search and replace the name of the CASA image being opened. More complex editing can be done via stand-alone editing scripts perhaps using standard python xml parser/editing packages.

Step 4 : Restore the state of the **viewer** from the edited xml .rstr file, using the **viewertool** as follows to subsequently save a .png figure to disk.

```
CASA <1>: vx = viewertool()
CASA <2>: x = vx.panel('mystate.rstr')
CASA <3>: vx.output('myfig.png',panel=x)
```

(There are two interactive ways to restore the **viewer** state as well. The first is by starting up the **viewer** with no image chosen, and then clicking on the \"restore viewer state\" button and choosing this .rstr file to open. Alternately, the **casaviewer** can itself be opened by supplying this .rstr file as the \'image\' to open.)

 

