.. container::
   :name: viewlet-above-content-title

Parameters
==========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task parameters

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               project : string = sim

            root prefix for output file names

Example

.. container:: param

   .. container:: parameters2

      dryrun : bool = True

   dryrun=True will only produce the informative report, not run
   simobserve/analyze

Example

.. container:: param

   .. container:: parameters2

      skymodel : string

   model image to observe

Example

.. container:: param

   .. container:: parameters2

      inbright : string

   scale surface brightness of brightest pixel e.g. "1.2Jy/pixel"

Example

.. container:: param

   .. container:: parameters2

      indirection : string

   set new direction e.g. "J2000 19h00m00 -40d00m00"

Example

.. container:: param

   .. container:: parameters2

      incell : string

   set new cell/pixel size e.g. "0.1arcsec"

Example

.. container:: param

   .. container:: parameters2

      incenter : string

   set new frequency of center channel e.g. "89GHz" (required even for
   2D model)

Example

.. container:: param

   .. container:: parameters2

      inwidth : string

   set new channel width e.g. "10MHz" (required even for 2D model)

Example

.. container:: param

   .. container:: parameters2

      complist : string

   componentlist to observe

Example

.. container:: param

   .. container:: parameters2

      compwidth : string = "8GHz"

   bandwidth of components

Example

.. container:: param

   .. container:: parameters2

      setpointings : bool = True

Example

.. container:: param

   .. container:: parameters2

      ptgfile : string = $project.ptg.txt

   list of pointing positions

Example

.. container:: param

   .. container:: parameters2

      integration : string = 10s

   integration (sampling) time

Example

.. container:: param

   .. container:: parameters2

      direction : stringArray

   "J2000 19h00m00 -40d00m00" or "" to center on model

Example

.. container:: param

   .. container:: parameters2

      mapsize : stringArray =

   angular size of map or "" to cover model

Example

.. container:: param

   .. container:: parameters2

      antennalist : stringArray = alma.cycle1.1.cfg aca.cycle1.cfg

   antenna position files of ALMA 12m and 7m arrays

Example

.. container:: param

   .. container:: parameters2

      hourangle : string = transit

   hour angle of observation center e.g. -3:00:00, or "transit"

Example

.. container:: param

   .. container:: parameters2

      totaltime : stringArray = 20min 1h

   total time of observation; vector corresponding to antennalist

Example

.. container:: param

   .. container:: parameters2

      tpnant : int = 0

   Number of total power antennas to use (0-4)

Allowed Value(s)

0 4

Example

.. container:: param

   .. container:: parameters2

      tptime : string = 0s

   total observation time for total power

Example

.. container:: param

   .. container:: parameters2

      pwv : double = 0.5

   Precipitable Water Vapor in mm. 0 for noise-free simulation

Allowed Value(s)

0

Example

.. container:: param

   .. container:: parameters2

      image : bool = True

   image simulated data

Example

.. container:: param

   .. container:: parameters2

      imsize : intArray = 128128

   output image size in pixels (x,y) or 0 to match model

Example

.. container:: param

   .. container:: parameters2

      imdirection : string

   set output image direction, (otherwise center on the model)

Example

.. container:: param

   .. container:: parameters2

      cell : string

   cell size with units or "" to equal model

Example

.. container:: param

   .. container:: parameters2

      niter : int = 0

   maximum number of iterations (0 for dirty image)

Example

.. container:: param

   .. container:: parameters2

      threshold : string = 0.1mJy

   flux level (+units) to stop cleaning

Example

.. container:: param

   .. container:: parameters2

      graphics : string = both

   display graphics at each stage to [screen|file|both|none]

Allowed Value(s)

screen file both none

Example

.. container:: param

   .. container:: parameters2

      verbose : bool = False

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   overwrite files starting with $project

Example

.. container:: section
   :name: viewlet-below-content-body
