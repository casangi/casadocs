.. container::
   :name: viewlet-above-content-title

AIPS-CASA Dictionary
====================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   CASA tasks equivalent to AIPS tasks

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

       AIPS tasks and their corresponding CASA tasks. Note that this
      list is not complete and there is also not a one-to-one
      translation. 

      +------------+---------------------------+---------------------------+
      |  AIPS Task |  CASA task/tool           |  Description              |
      +============+===========================+===========================+
      | APROPOS    | taskhelp                  | List tasks with a short   |
      |            |                           | description of their      |
      |            |                           | purposes                  |
      +------------+---------------------------+---------------------------+
      | BLCAL      | blcal                     | Calculate a               |
      |            |                           | baseline-based gain       |
      |            |                           | calibration solution      |
      +------------+---------------------------+---------------------------+
      | BLCHN      | blcal                     | Calculate a               |
      |            |                           | baseline-based bandpass   |
      |            |                           | calibration solution      |
      +------------+---------------------------+---------------------------+
      | BPASS      | bandpass                  | Calibrate bandpasses      |
      +------------+---------------------------+---------------------------+
      | CALIB      | gaincal                   | Calibrate gains           |
      |            |                           | (amplitudes and phases)   |
      +------------+---------------------------+---------------------------+
      | CLCAL      | applycal                  | Apply calibration to data |
      +------------+---------------------------+---------------------------+
      | COMB       | immath                    | Combine images            |
      +------------+---------------------------+---------------------------+
      | CPASS      | bandpass                  | Calibrate bandpasses by   |
      |            |                           | polynomial fitting        |
      +------------+---------------------------+---------------------------+
      | CVEL       | cvel/mstransform          | Regid visibility spectra  |
      +------------+---------------------------+---------------------------+
      | DBCON      | concat/virtualconcat      | Concatenate u-v datasets  |
      +------------+---------------------------+---------------------------+
      | DEFAULT    | default                   | Load a task with default  |
      |            |                           | parameters                |
      +------------+---------------------------+---------------------------+
      | FILLM      | importvla                 | Import old-format VLA     |
      |            |                           | data                      |
      +------------+---------------------------+---------------------------+
      | FITLD      | i                         | Import a u-v dataset      |
      |            | mportuvfits/importfitsidi | which is in FITS format   |
      +------------+---------------------------+---------------------------+
      | FITLD      | importfits                | Import an image which is  |
      |            |                           | in FITS format            |
      +------------+---------------------------+---------------------------+
      | FITTP      | exportuvfits              | Write a u-v dataset to    |
      |            |                           | FITS format               |
      +------------+---------------------------+---------------------------+
      | FITTP      | exportfits                | Write an image to FITS    |
      |            |                           | format                    |
      +------------+---------------------------+---------------------------+
      | FRING      | (coming soon)             | Calibrate group delays    |
      |            |                           | and phase rates           |
      +------------+---------------------------+---------------------------+
      | GETJY      | fluxscale                 | Determine flux densities  |
      |            |                           | for other cals            |
      +------------+---------------------------+---------------------------+
      | GO         | go                        | Run a task                |
      +------------+---------------------------+---------------------------+
      | HELP       | help                      | Display the help page for |
      |            |                           | a task (also use          |
      |            |                           | `casa.nra                 |
      |            |                           | o.edu/casadocs <http://ca |
      |            |                           | sa.nrao.edu/casadocs>`__) |
      +------------+---------------------------+---------------------------+
      | IMAGR      | clean/tclean              | Image and deconvolve      |
      +------------+---------------------------+---------------------------+
      | IMFIT      | imfit                     | Fit gaussian components   |
      |            |                           | to an image               |
      +------------+---------------------------+---------------------------+
      | IMHEAD     | vishead                   | View header for u-v data  |
      +------------+---------------------------+---------------------------+
      | IMHEAD     | imhead                    | View header for an image  |
      +------------+---------------------------+---------------------------+
      | IMLIN      | imcontsub                 | Subtract continuum in     |
      |            |                           | image plane               |
      +------------+---------------------------+---------------------------+
      | IMLOD      | importfits                | Import a FITS image       |
      +------------+---------------------------+---------------------------+
      | IMSTAT     | imstat                    | Measure statistics on an  |
      |            |                           | image                     |
      +------------+---------------------------+---------------------------+
      | INP        | inp                       | View task parameters      |
      +------------+---------------------------+---------------------------+
      | JMFIT      | imfit                     | Fit gaussian components   |
      |            |                           | to an image               |
      +------------+---------------------------+---------------------------+
      | LISTR      | listobs                   | Print basic data          |
      +------------+---------------------------+---------------------------+
      | MCAT       | ls                        | List image data files     |
      +------------+---------------------------+---------------------------+
      | MOMNT      | immoments                 | Compute moments from an   |
      |            |                           | image                     |
      +------------+---------------------------+---------------------------+
      | OHGEO      | imregrid                  | Regrids an image onto     |
      |            |                           | another image’s geometry  |
      +------------+---------------------------+---------------------------+
      | PBCOR      | impbcor/widebandpbcor     | Correct an image for the  |
      |            |                           | primary beam              |
      +------------+---------------------------+---------------------------+
      | PCAL       | polcal                    | Calibrate polarization    |
      +------------+---------------------------+---------------------------+
      | POSSM      | plotcal/plotms            | Plot bandpass calibration |
      |            |                           | tables                    |
      +------------+---------------------------+---------------------------+
      | POSSM      | plotms                    | Plot spectra              |
      +------------+---------------------------+---------------------------+
      | PRTAN      | listobs                   | Print antenna locations   |
      +------------+---------------------------+---------------------------+
      | PRTAN      | plotants                  | Plot antenna locations    |
      +------------+---------------------------+---------------------------+
      | QUACK      | flagdata                  | Remove first integrations |
      |            |                           | from scans                |
      +------------+---------------------------+---------------------------+
      | RENAME     | mv                        | Rename an image or        |
      |            |                           | dataset                   |
      +------------+---------------------------+---------------------------+
      | RFLAG      | flagdata                  | Auto-flagging             |
      +------------+---------------------------+---------------------------+
      | SETJY      | setjy                     | Set flux densities for    |
      |            |                           | flux cals                 |
      +------------+---------------------------+---------------------------+
      | SMOTH      | imsmooth                  | Smooth an image           |
      +------------+---------------------------+---------------------------+
      | SNPLT      | plotcal/plotms            | Plot gain calibration     |
      |            |                           | tables                    |
      +------------+---------------------------+---------------------------+
      | SPFLG      | viewer/msview             | Flag raster image of time |
      |            |                           | v. channel                |
      +------------+---------------------------+---------------------------+
      | SPLIT      | split                     | Write out u-v files for   |
      |            |                           | individual sources        |
      +------------+---------------------------+---------------------------+
      | STATWT     | statwt                    | Weigh visibilities based  |
      |            |                           | on their noise            |
      +------------+---------------------------+---------------------------+
      | TASK       | inp                       | Load a task with current  |
      |            |                           | parameters                |
      +------------+---------------------------+---------------------------+
      | TGET       | tget                      | Load a task with          |
      |            |                           | parameters last used for  |
      |            |                           | that task                 |
      +------------+---------------------------+---------------------------+
      | TVALL      | viewer/imview             | Display image             |
      +------------+---------------------------+---------------------------+
      | TVFLG      | viewer/msview             | Flag raster image of time |
      |            |                           | v. baseline               |
      +------------+---------------------------+---------------------------+
      | UCAT       | ls                        | List u-v data files       |
      +------------+---------------------------+---------------------------+
      | UVFIX      | fixvis                    | Compute u, v, and w       |
      |            |                           | coordinates               |
      +------------+---------------------------+---------------------------+
      | UVFLG      | flagdata                  | Flag data                 |
      +------------+---------------------------+---------------------------+
      | UVLIN      | uvcontsub/mstransform     | Subtract continuum from   |
      |            |                           | u-v data                  |
      +------------+---------------------------+---------------------------+
      | UVLSF      | uvcontsub/mstransform     | Subtract continuum from   |
      |            |                           | u-v data                  |
      +------------+---------------------------+---------------------------+
      | UVPLT      | plotms                    | Plot u-v data             |
      +------------+---------------------------+---------------------------+
      | UVSUB      | uvsub                     | Subtracts model u-v data  |
      |            |                           | from corrected u-v data   |
      +------------+---------------------------+---------------------------+
      | WIPER      | plotms                    | Plot and flag u-v data    |
      +------------+---------------------------+---------------------------+
      | ZAP        | rmtables                  | Delete data files         |
      +------------+---------------------------+---------------------------+

       

         .. container:: center

             

         .. container:: caption

             

         .. container:: center

             

.. container:: section
   :name: viewlet-below-content-body
