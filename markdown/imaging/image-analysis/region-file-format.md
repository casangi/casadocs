

# Region File Format 

Syntax for CASA CRTF Region Files

The CASA region file format provides a flexible, easily edited set of region definitions which are accepted across CASA tasks. Region files may be written by hand or using the CASA **viewer**.

<div class="alert alert-warning">
**ALERT**: Whereas the region format is supported by all the data processing tasks, the viewer implementation is still limited to rectangles, ellipses, and some markers.
</div>

For a file to be recognized as a valid CASA region text file, the first line must contain the string:

    #CRTF

\"CRTF\" stands for \"CASA Region Text Format\". One may also include an optional version number at the end of the string, so it reads \#CRTFv0; this indicates the version of the format definition.

Region files have two different kinds of definitions, \"regions\" and \"annotations\", each of which is one line long. To indicate an annotation, a line must begin with \"ann\". Lines that begin with the comment character (\#) are not considered for processing or display.

The second line of a file may define global parameters that are to be used for all regions and annotations in that file, in which case the line starts with the word \"global\". The parameters set here may also be overridden by keywords in a specific line, in which case the keywords pertain only to that one line.

<div class="alert alert-info">
**NOTE:** All regions are considered by tasks. They will be displayed by visualization tasks as well as used to create masks, etc., as appropriate. Annotations are used by display tasks, and are for visual reference only.
</div>

Some tasks, like **clean**, require that a region cannot be entirely outside the image.

 

# Region Definitions

All regions lines will follow this general arrangement:

    {shape} {additional parameter=value pairs}

The possible parameter/value pairs are described in more detail below. Note that most parameters beyond the shape and its coordinates can be defined globally.

Possible units for coordinates are:

-   *sexagesimal*, e.g. 18h12m24s for right ascension or -03.47.27.1 for declination
-   *decimal degrees*, e.g. 140.0342deg for both RA and Dec
-   *radians*, e.g. 2.37666rad for both RA and Dec
-   *pixels*, e.g. 204pix

Possible units of length are:

-   *degrees*, e.g. 23deg
-   *arcminutes*, e.g. 23arcmin
-   *arcseconds*, e.g. 23arcsec
-   *radians*, e.g. 0.00035rad
-   *pixels*, e.g. 23pix

*Units must always be included when defining a region.* 

<div class="alert alert-info">
**NOTE:** The CASA image analysis tasks will determine how a region is projected on a pixel image. The current CASA definition is that when the center of a pixel is inside the region, the full pixel is considered to be included in the region.  If the center of the pixel is outside the region, the full pixel will be excluded. Note that the CASA viewer behavior is not entirely consistent and for rectangles it assumes that *any* fractional pixel coverage will include the entire pixel. For other supported shapes (ellipses and polygons), however, ithe viewer adheres to the 'center of pixel' definition, consistent with the image analysis tools and tasks. 

For purely single-pixel work regions may not necessarily be the best choice and alternate methods may be preferable to using regions, eg. **ia.topixel**, **ia.toworld**, **ia.pixelvalue**.
</div>

 

# Allowed Shapes

-   **Rectangular box**; the two coordinates are two opposite corners:

```{=html}
<!-- -->
```
    box[[x1, y1], [x2, y2]]

-   **Center box**; \[x, y\] define the center point of the box and \[x_width, y_width\] the width of the sides:

```{=html}
<!-- -->
```
    centerbox[[x, y], [x_width, y_width]]

-   **Rotated box**; \[x, y\] define the center point of the box; \[x_width, y_width\] the width of the sides; rotang the rotation angle:

```{=html}
<!-- -->
```
    rotbox[[x, y], [x_width, y_width], rotang]

-   **Polygon**; there could be many \[x, y\] corners. If parts of the polygon overlap, then the pixels in that overlapping region are taken into account. Note that the last point will connect with the first point to close the polygon:

```{=html}
<!-- -->
```
    poly[[x1, y1], [x2, y2], [x3, y3], ...]

-   **Circle**; center of the circle \[x,y\], r is the radius:

```{=html}
<!-- -->
```
    circle[[x, y], r]

-   **Annulus**; center of the circle is \[x, y\], \[r1, r2\] are inner and outer radii:

```{=html}
<!-- -->
```
    annulus[[x, y], [r1, r2]]

-   **Ellipse**; center of the ellipse is \[x, y\]; semi-major and semi-minor axes are \[bmaj, bmin\]; position angle of the major axis is pa:

```{=html}
<!-- -->
```
    ellipse[[x, y], [bmaj, bmin], pa]

 

# Annotation Definitions

In addition to the definitions for regions, above, the following are always treated as annotations:

-   **Line**; coordinates define the end points of the line:

```{=html}
<!-- -->
```
    line[[x1, y1], [x2, y2]]

-   **Vector**; coordinates define end points; second coordinate pair is location of tip of arrow:

```{=html}
<!-- -->
```
    vector[[x1, y1], [x2, y2]]

-   **Text**; coordinates define leftmost point of text string:

```{=html}
<!-- -->
```
    text[[x, y], ’my text’]

-   **Symbol**; coordinates define location of symbol (see [below](#fonts-and-symbols) for a list of allowed symbols):

```{=html}
<!-- -->
```
    symbol[[x, y], {symbol}]

 

# Global Definitions

Definitions to be used throughout the region file are placed on a line beginning with \'global\', usually at the top of the file. These definitions may also be used on any individual region or annotation line; in this case, the value defined on that line will override the predefined global (but only for that line). If a 'global' line occurs later in the file, subsequent lines will obey those definitions.

-   *Coordinate reference frame*:
    -   Possible values: J2000, JMEAN, JTRUE, APP, B1950, B1950_VLA, BMEAN, BTRUE, GALACTIC, HADEC, AZEL, AZELSW, AZELNE, AZELGEO, AZELSWGEO, AZELNEGEO, JNAT, ECLIPTIC, MECLIPTIC, TECLIPTIC, SUPERGAL, ITRF, TOPO, ICRS
    -   Default: image value

```{=html}
<!-- -->
```
    coord = J2000

Frequency/velocity axis:

-   Possible values: REST, LSRK, LSRD, BARY, GEO, TOPO, GALACTO, LGROUP, CMB
-   Default: image value

```{=html}
<!-- -->
```
    frame=TOPO

-   Frequency/velocity range:
    -   Possible units: GHz, MHz, kHz, km/s, Hz, channel, chan (=channel)
    -   Default: image range

```{=html}
<!-- -->
```
    range=[min, max]

-   Correlation axis:
    -   Possible values: I, Q, U, V, RR, RL, LR, LL, XX, XY, YX, YY, RX, RY, LX, LY, XR, XL, YR, YL, PP, PQ, QP, QQ, RCircular, LCircular, Linear, Ptotal, Plinear, PFtotal, PFlinear, Pangle
    -   Default: all planes present in image

```{=html}
<!-- -->
```
    corr=[X, Y]

-   Velocity calculation:
    -   Possible values: RADIO, OPTICAL, Z, BETA, GAMMA
    -   Default: image value

```{=html}
<!-- -->
```
    veltype=RADIO

-   Rest frequency:
    -   Default: image value

```{=html}
<!-- -->
```
    restfreq=1.42GHz

-   Line characteristics:
    -   Possible values: any line 
<!-- -->
```
    linewidth=1
    line
<!-- -->
```
    symsize = 1
    symthick = 1

-   Region, symbol, and text color:
    -   Possible values: any color recognized by matplotlib, including hex values
    -   Default:

```{=html}
<!-- -->
```
    color=green
    color=red

-   Text font characteristics:
    -   Possible values: see [below](#allowed-fonts)
    -   'usetex' is a boolean parameter that determines whether or not the text line should be interpreted as LaTeX, and would require working LaTeX, dvipng, and Ghostscript installations (equivalent to the text.usetex parameter in matplotlib).

```{=html}
<!-- -->
```
    font=Helvetica
    fontsize=10pt 
    font
<!-- -->
```
    labelpos=’right’

-   Label color:
    -   Default: color of associated region.
    -   Allowed values: same as values for region colors.

```{=html}
<!-- -->
```
    labelcolor=’green’

-   Label offset:
    -   Default: \[0,0\].
    -   Allowed values: any positive or negative number, in units of pixels.

```{=html}
<!-- -->
```
    labeloff=[1, 1]

 

# Allowed Additional Parameters

These must be defined per region line:

-   *Labels*: text label for a region; should be placed so text does not overlap with region boundary

```{=html}
<!-- -->
```
    label=’string’

-   *\"OR/NOT\" operators*: A \"+\" at the beginning of a line will flag it with a boolean \"OR\" (default), and a \"-\" will flag it with a boolean \"NOT\". Overlapping regions will be treated according to their sequence in the file; i.e., ((((entireImage OR line1) OR line2) NOT line3) OR line4). This allows some flexibility in building \"non-standard\" regions. Note that a task (e.g., clean) will still consider all lines: if one wishes to remove a region from consideration, it should be commented out (\"\#\").
-   Default: OR (+)

 

# Examples

A file with both global definitions and per-line definitions:

    #CRTFv0
    global coord=B1950_VLA, frame=BARY, corr=[I, Q], color=blue

    # A simple circle region:
    circle[[18h12m24s, -23d11m00s], 2.3arcsec]

    # A box region, this one only for annotation:
    ann box[[140.0342deg, -12.34243deg], [140.0360deg, -12.34320deg]]

    # A rotated box region, for a particular range of velocities:
    rotbox[[12h01m34.1s, 12d23m33s], [3arcmin, 1arcmin], 12deg], range=[-1240km/s, 1240km/s]

    # An annular region, overriding some of the global defaults:
    annulus[[17h51m03.2s, -45d17m50s], [4.12deg, 0.10deg]], corr=[I,Q,U,V], color=red, label=’My label here’

    # Cuts an ellipse out of the previous regions, but only for Q and a particular frequency range:
    -ellipse[[17:51:03.2, -45.17.50], [1.34deg, 0.25deg], 45rad], range=[1.420GHz, 1.421GHz], corr=[Q], color=green, label=’Removed this’

    # A diamond marker, in J2000 coordinates:
    symbol[[32.1423deg, 12.1412deg], D], linewidth=2, coord=J2000, symsize=2

 

# Fonts and Symbols

## Allowed Symbols

  -------------------------------------------------------------------- -----------------------------------------------------
  \'.\'                                                                point marker 
  \',\'                                  pixel marker
  \'o\'                                  circle marker
  \'v\'                                  triangle_down marker
  \'\^\'                                 triangle_up marker
  \'\<\'   triangle_left marker
  \'\>\'   triangle_right marker
  \'1\'                                  tri_down marker
  \'2\'                                  tri_up marker
  \'3\'                                  tri_left marker
  \'4\'                                  tri_right marker
  \'s\'                                  square marker
  \'p\'                                  pentagon marker
  \'\*\'                                 star marker
  \'h\'                                  hexagon1 marker
  \'H\'                                  hexagon2 marker
  \'+\'                                  plus marker
  \'x\'                                  x marker
  \'D\'                                  diamond marker
  \'d\'                                  thin_diamond marker
  \'\|\'                                 vline marker
  \'\_\'                                 hline marker
  -------------------------------------------------------------------- -----------------------------------------------------


## Allowed Fonts

### Allowed Fonts for Linux

\"Century Schoolbook L\", \"Console\", \"Courier\", \"Courier 10 Pitch\", \"Cursor\", \"David CLM\", \"DejaVu LGC Sans\", \"DejaVu LGC Sans Condensed\", \"DejaVu LGC Sans Light\", \"DejaVu LGC Sans Mono\", \"DejaVu LGC Serif\", \"DejaVu LGC Serif Condensed\", \"Dingbats\", \"Drugulin CLM\", \"East Syriac Adiabene\", \"Ellinia CLM\", \"Estrangelo Antioch\", \"Estrangelo Edessa\", \"Estrangelo Nisibin\", \"Estrangelo Nisibin Outline\", \"Estrangelo Talada\", \"Fangsong ti\", \"Fixed \[Sony\]\", \"Fixed \[Eten\]\", \"Fixed \[Misc\]\", \"Fixed \[MNKANAME\]\", \"Frank Ruehl CLM\", \"fxd\", \"Goha-Tibeb Zemen\", \"goth_p\", \"Gothic \[Shinonome\]\", \"Gothic \[mplus\]\", \"hlv\", \"hlvw\", \"KacstArt\", \"KacstBook\", \"KacstDecorative\", \"KacstDigital\", \"KacstFarsi\", \"KacstLetter\", \"KacstPoster\", \"KacstQura\", \"KacstQuraFixed\", \"KacstQuran\", \"KacstTitle\", \"KacstTitleL\", \"Liberation Mono\", \"Liberation Sans\", \"Liberation Serif\", \"LKLUG\", \"Lohit Bengali\", \"Lohit Gujarati\", \"Lohit Hindi\", \"Lohit Kannada\", \"Lohit Malayalam\", \"Lohit Oriya\", \"Lohit Punjabi\", \"Lohit Tamil\", \"Lohit Telugu\", \"LucidaTypewriter\", \"Luxi Mono\", \"Luxi Sans\", \"Luxi Serif\", \"Marumoji\", \"Miriam CLM\", \"Miriam Mono CLM\", \"MiscFixed\", \"Monospace\", \"Nachlieli CLM\", \"Nimbus Mono L\", \"Nimbus Roman No9 L\", \"Nimbus Sans L\", \"Nimbus Sans L Condensed\", \"PakTypeNaqsh\", \"PakTypeTehreer\", \"qub\", \"Sans Serif\", \"Sazanami Gothic\", \"Sazanami Mincho\", \"Serif\", \"Serto Batnan\", \"Serto Jerusalem\", \"Serto Jerusalem Outline\", \"Serto Mardin\", \"Standard Symbols L\", \"sys\", \"URW Bookman L\", \"URW Chancery L\", \"URW Gothic L\", \"URW Palladio L\", \"Utopia\", \"Yehuda CLM\"

### Allowed Fonts for MacOS X

\"Abadi MT Condensed Light\", \"Adobe Caslon Pro\", \"Adobe Garamond Pro\", \"Al Bayan\", \"American Typewriter\", \"Andale Mono\", \"Apple Braille\", \"Apple Chancery\", \"Apple LiGothic\", \"Apple LiSung\", \"Apple Symbols\", \"AppleGothic\", \"AppleMyungjo\", \"Arial\", \"Arial Black\", \"Arial Hebrew\", \"Arial Narrow\", \"Arial Rounded MT Bold\", \"Arial Unicode MS\", \"Arno Pro\", \"Ayuthaya\", \"Baghdad\", \"Baskerville\", \"Baskerville Old Face\", \"Batang\", \"Bauhaus 93\", \"Bell Gothic Std\", \"Bell MT\", \"Bernard MT Condensed\", \"BiauKai\", \"Bickham Script Pro\", \"Big Caslon\", \"Birch Std\", \"Blackoak Std\", \"Book Antiqua\", \"Bookman Old Style\", \"Bookshelf Symbol 7\", \"Braggadocio\", \"Britannic Bold\", \"Brush Script MT\", \"Brush Script Std\", \"Calibri\", \"Calisto MT\", \"Cambria\", \"Candara\", \"Century\", \"Century Gothic\", \"Century Schoolbook\", \"Chalkboard\", \"Chalkduster\", \"Chaparral Pro\", \"Charcoal CY\", \"Charlemagne Std\", \"Cochin\", \"Colonna MT\", \"Comic Sans MS\", \"Consolas\", \"Constantia\", \"Cooper Black\", \"Cooper Std\", \"Copperplate\", \"Copperplate Gothic Bold\", \"Copperplate Gothic Light\", \"Corbel\", \"Corsiva Hebrew\", \"Courier\", \"Courier New\", \"Curlz MT\", \"DecoType Naskh\", \"Desdemona\", \"Devanagari MT\", \"Didot\", \"Eccentric Std\", \"Edwardian Script ITC\", \"Engravers MT\", \"Euphemia UCAS\", \"Eurostile\", \"Footlight MT Light\", \"Franklin Gothic Book\", \"Franklin Gothic Medium\", \"Futura\", \"Garamond\", \"Garamond Premier Pro\", \"GB18030 Bitmap\", \"Geeza Pro\", \"Geneva\", \"Geneva CY\", \"Georgia\", \"Giddyup Std\", \"Gill Sans\", \"Gill Sans MT\", \"Gill Sans Ultra Bold\", \"Gloucester MT Extra Condensed\", \"Goudy Old Style\", \"Gujarati MT\", \"Gulim\", \"GungSeo\", \"Gurmukhi MT\", \"Haettenschweiler\", \"Harrington\", \"HeadLineA\", \"Hei\", \"Heiti SC\", \"Heiti TC\", \"Helvetica\", \"Helvetica CY\", \"Helvetica Neue\", \"Herculanum\" \"Hiragino Kaku Gothic Pro\", \"Hiragino Kaku Gothic ProN\", \"Hiragino Kaku Gothic Std\", \"Hiragino Kaku Gothic StdN\", \"Hiragino Maru Gothic Pro\", \"Hiragino Maru Gothic ProN\", \"Hiragino Mincho Pro\", \"Hiragino Mincho ProN\", \"Hiragino Sans GB\", \"Hobo Std\", \"Hoefler Text\", \"Impact\", \"Imprint MT Shadow\", \"InaiMathi\", \"Kai\", \"Kailasa\", \"Kino MT\", \"Kokonor\", \"Kozuka Gothic Pro\", \"Kozuka Mincho Pro\", \"Krungthep\", \"KufiStandardGK\", \"Letter Gothic Std\", \"LiHei Pro\", \"LiSong Pro\", \"Lithos Pro\", \"Lucida Blackletter\", \"Lucida Bright\", \"Lucida Calligraphy\", \"Lucida Console\", \"Lucida Fax\", \"Lucida Grande\", \"Lucida Handwriting\", \"Lucida Sans\", \"Lucida Sans Typewriter\", \"Lucida Sans Unicode\", \"Marker Felt\", \"Marlett\", \"Matura MT Script Capitals\", \"Meiryo\", \"Menlo\", \"Mesquite Std\", \"Microsoft Sans Serif\", \"Minion Pro\", \"Mistral\", \"Modern No. 20\", \"Monaco\", \"Monotype Corsiva\", \"Monotype Sorts\", \"MS Gothic\", \"MS Mincho\", \"MS PGothic\", \"MS PMincho\", \"MS Reference Sans Serif\", \"MS Reference Specialty\", \"Mshtakan\", \"MT Extra\", \"Myriad Pro\", \"Nadeem\", \"New Peninim MT\", \"News Gothic MT\", \"Nueva Std\", \"OCR A Std\", \"Onyx\", \"Optima\", \"Orator Std\", \"Osaka\", \"Papyrus\", \"PCMyungjo\", \"Perpetua\", \"Perpetua Titling MT\", \"PilGi\", \"Plantagenet Cherokee\", \"Playbill\", \"PMingLiU\", \"Poplar Std\", \"Prestige Elite Std\", \"Raanana\", \"Rockwell\", \"Rockwell Extra Bold\", \"Rosewood Std\", \"Sathu\", \"Silom\", \"SimSun\", \"Skia\", \"Stencil\", \"Stencil Std\", \"STFangsong\", \"STHeiti\", \"STKaiti\", \"STSong\", \"Symbol\", \"Tahoma\", \"Tekton Pro\", \"Thonburi\", \"Times\", \"Times New Roman\", \"Trajan Pro\", \"Trebuchet MS\", \"Tw Cen MT\", \"Verdana\", \"Webdings\", \"Wide Latin\", \"Wingdings\", \"Wingdings 2\", \"Wingdings 3\", \"Zapf Dingbats\", \"Zapfino\"

 

