.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Example
=======

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Example usage of sdgaincal

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      There are two ways to generate and apply double-circle gaintable.
      One is to calibrate and apply atmosphere and sky calibrations
      separately, and the other is to apply them on-the-fly during
      double-circle gain calibration. The latter should be more
      efficient. Examples for these two procedures are shown below.

      .. rubric:: Apply atmosphere and sky caltables separately
         :name: apply-atmosphere-and-sky-caltables-separately

      To compute a gaintable and subsequently apply it using
      **applycal**:

      #. Generate the $T_{sky}$ and $T_{sys}$ calibration tables, and
         apply them (**sdcal**)
      #. Split out the corrected column data (**split**)
      #. Generate the double-circle gaincal calibration tables
         (**sdgaincal**)
      #. Apply the double-circle gaincal calibration tables
         (**applycal**)

      In CASA, this looks like the following:

      .. container::

         .. container:: casa-input-box

            | sdcal(infile=inputvis, calmode='ps,tsys,apply')
            | split(vis=inputvis, outputvis=calibratedvis,
              datacolumn='corrected')
            | sdgaincal(infile=calibratedvis, outfile='DCgaintable',
              calmode='doublecircle')
            | applycal(vis=calibratedvis, gaintable='DCgaintable')

      .. container::

         .. rubric:: Apply atmosphere and sky caltables on-the-fly
            :name: apply-atmosphere-and-sky-caltables-on-the-fly

         To compute a gaintable and subsequently apply it using
         **applycal**:

         #. Generate the $T_{sky}$ and $T_{sys}$ calibration tables
            (**sdcal**)
         #. Generate the double-circle gaincal calibration tables by
            applying $T_{sky}$ and $T_{sys}$ calibration tables
            on-the-fly (**sdgaincal**)

            -  You can set *spwmap* and *interp* for each
               pre-application caltable if necessary

         #. Apply the double-circle gaincal calibration tables
            (**applycal**)

         In CASA, this looks like the following:

         .. container::

            .. container:: casa-input-box

               | sdcal(infile=inputvis, calmode='ps', outfile='sky.tbl')
               | sdcal(infile=inputvis, calmode='tsys',
                 outfile='tsys.tbl')
                 sdgaincal(infile=inputvis, applytable=['sky.tbl',
                 'tsys.tbl'],outfile='DCgaintable',
                 calmode='doublecircle')
               | applycal(vis=inputvis, gaintable='DCgaintable')

.. container:: section
   :name: viewlet-below-content-body
