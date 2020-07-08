.. container::
   :name: viewlet-above-content-title

Parameters
==========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task applycal parameters

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               infiles : stringArray

            a list of names of input SD Measurementsets (only MS is
            allowed for this task)

Example

.. container:: param

   .. container:: parameters2

      outfile : string

   name of output image

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   overwrite the output file if already exists [True, False]

Example

.. container:: param

   .. container:: parameters2

      field : string stringArray

   select data by field IDs and names, e.g. "3C2*" (""=all)

Example

.. container:: param

   .. container:: parameters2

      spw : string stringArray

   select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all)

Example

.. container:: param

   .. container:: parameters2

      antenna : string stringArray

   select data by antenna names or IDs, e.g, "PM03" ("" = all antennas)

Example

.. container:: param

   .. container:: parameters2

      scan : string stringArray

   select data by scan numbers, e.g. "21~23" (""=all)

Example

.. container:: param

   .. container:: parameters2

      intent : string stringArray = OBSERVE_TARGET#ON_SOURCE

   select data by observational intent, e.g. "*ON_SOURCE*" (""=all)

Example

.. container:: param

   .. container:: parameters2

      mode : string = channel

   spectral gridding type

Allowed Value(s)

channel frequency velocity

Example

.. container:: param

   .. container:: parameters2

      nchan : int = -1

   number of channels (planes) in output image (-1=all)

Example

.. container:: param

   .. container:: parameters2

      start : string int = 0

   start of output spectral dimension, e.g. "0", "110GHz", "-20km/s"

Example

.. container:: param

   .. container:: parameters2

      width : string int = 1

   width of output spectral channels

Example

.. container:: param

   .. container:: parameters2

      veltype : string = radio

   velocity definition

Allowed Value(s)

radio optical true relativistic RADIO OPTICAL TRUE RELATIVISTIC

Example

.. container:: param

   .. container:: parameters2

      outframe : string

   velocity frame of output image (""=current frame or LSRK for
   multiple-MS inputs)

Allowed Value(s)

lsrk lsrd bary geo topo galacto lgroup cmb LSRK LSRD BARY GEO TOPO
GALACTO LGROUP CMB

Example

.. container:: param

   .. container:: parameters2

      gridfunction : string = BOX

   gridding function for imaging (see description in help)

Allowed Value(s)

BOX PB SF GAUSS GJINC box pb sf gauss gjinc

Example

.. container:: param

   .. container:: parameters2

      convsupport : int = -1

   convolution support for gridding

Example

.. container:: param

   .. container:: parameters2

      truncate : string int double = -1

   truncation radius for gridding

Example

.. container:: param

   .. container:: parameters2

      gwidth : string int double = -1

   HWHM for gaussian

Example

.. container:: param

   .. container:: parameters2

      jwidth : string int double = -1

   c-parameter for jinc function

Example

.. container:: param

   .. container:: parameters2

      imsize : intArray doubleArray

   x and y image size in pixels, e.g., [64,64]. Single value: same for
   both spatial axes ([] = number of pixels to cover whole pointings in
   MSes)

Example

.. container:: param

   .. container:: parameters2

      cell : string stringArray doubleArray

   x and y cell size, (e.g., ["8arcsec","8arcsec"]. default unit arcmin.
   ("" = 1/3 of FWHM of primary beam)

Example

.. container:: param

   .. container:: parameters2

      phasecenter : undefined

   image center direction: position or field index, e.g., "J2000
   17:30:15.0 -25.30.00.0". ("" = the center of pointing directions in
   MSes)

Example

.. container:: param

   .. container:: parameters2

      projection : string = SIN

   map projection type

Allowed Value(s)

SIN CAR TAN SFL sin car tan sfl

Example

.. container:: param

   .. container:: parameters2

      ephemsrcname : string

   ephemeris source name, e.g. "MARS"

Example

.. container:: param

   .. container:: parameters2

      pointingcolumn : string = direction

   pointing data column to use

Allowed Value(s)

target pointing_offset source_offset encoder direction TARGET
POINTING_OFFSET SOURCE_OFFSET ENCODER DIRECTION

Example

.. container:: param

   .. container:: parameters2

      restfreq : string double

   rest frequency to assign to image, e.g., "114.5GHz"

Example

.. container:: param

   .. container:: parameters2

      stokes : string

   stokes parameters or polarization types to image, e.g. "I", "XX"

Example

.. container:: param

   .. container:: parameters2

      minweight : double = 0.1

   Minimum weight ratio to the median of weight used in weight
   correction and weight beased masking

Allowed Value(s)

0

Example

.. container:: param

   .. container:: parameters2

      brightnessunit : string

   Overwrite the brightness unit in image (\'\' = respect the unit in
   MS) [\'K\' or \\'Jy/beam\']

Allowed Value(s)

K Jy/beam

Example

.. container:: param

   .. container:: parameters2

      clipminmax : bool = False

   Clip minimum and maximum value from each pixel. Note the benefit of
   clipping is lost when the number of integrations contributing to each
   gridded pixel is small, or where the incidence of spurious datapoints
   is approximately or greater than the number of beams (in area)
   encompassed by expected image.

Example

.. container:: section
   :name: viewlet-below-content-body
