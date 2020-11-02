

.. _Description:

Description
   **sdgaincal** computes and removes a time-dependent gain variation
   in single-dish data on a per-spectral-window and per-antenna
   basis. Presently the task operates only on data taken with the
   ALMA fast-mapped, double-circle observation modes `[1] <#cit1>`__
   . This task exploits the fact that the double-circle mode observes
   the same position in the center of the mapped field, approximately
   circular every sub-cycle, and normalizes the gains throughout the
   entire dataset, relative to the measured brightness at the center
   position.
   
   .. note:: Info: This gain calibration task is done independently of, and
      following, the atmosphere (i.e. :math:`T_{sys}`) and sky
      calibration steps applied through the **sdcal** task.
      Alternative way to apply these caltables is to utilize
      pre-application capability of **sdgaincal** task. This can be
      done by feeding caltables into the task using *applytable*
      parameter. You can specify spw mapping and interpolation method
      via *spwmap* and *interp*, respectively. Usage for these
      parameters are exactly same as **applycal**.
   
   .. rubric:: Configurable inputs control the calibration mode,
      selection parameters, and output behavior:
      
   
   Presently, this task has only one calibration mode:
   *calmode=*'*doublecircle*'.
   
   The size of the region that CASA regards as "the center" is
   user-configurable via the expandable '*radius*' (in arcsec)
   parameter (under '*calmode*').  The default is to use the size of
   the primary beam. The data can also be smoothed in the time
   domain, prior to computation of the gain variation. Selection is
   by specral window/channels, field IDs, and antenna through the
   *spw*, *field,* and *antenna* selection parameters. The default is
   to use all data for the gain calibration. The caltable can be
   output with the '*outfile*' parameter.
   
   .. rubric::  Bibliography

   :sup:`1. Phillips et al, 2015. Fast Single-Dish Scans of the
   Sun Using
   ALMA.` `PDF <http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?2015ASPC..499..347P&amp;data_type=PDF_HIGH&amp;whole_paper=YES&amp;type=PRINTER&amp;filetype=.pdf>`__ `<#ref-cit1>`__
   

.. _Examples:

Examples
   There are two ways to generate and apply double-circle gaintable.
   One is to calibrate and apply atmosphere and sky calibrations
   separately, and the other is to apply them on-the-fly during
   double-circle gain calibration. The latter should be more
   efficient. Examples for these two procedures are shown below.
   
   .. rubric:: Apply atmosphere and sky caltables separately
      
   
   To compute a gaintable and subsequently apply it using
   **applycal**:
   
   #. Generate the :math:`T_{sky}` and :math:`T_{sys}` calibration
      tables, and apply them (**sdcal**)
   #. Split out the corrected column data (**split**)
   #. Generate the double-circle gaincal calibration tables
      (**sdgaincal**)
   #. Apply the double-circle gaincal calibration tables
      (**applycal**)
   
   In CASA, this looks like the following:
   
   ::
   
      sdcal(infile=inputvis, calmode='ps,tsys,apply')
      split(vis=inputvis, outputvis=calibratedvis,
      datacolumn='corrected')
      sdgaincal(infile=calibratedvis, outfile='DCgaintable',
      calmode='doublecircle')
      applycal(vis=calibratedvis, gaintable='DCgaintable')
   
   .. rubric:: Apply atmosphere and sky caltables on-the-fly
      
   
   To compute a gaintable and subsequently apply it using
   **applycal**:
   
   #. Generate the :math:`T_{sky}` and :math:`T_{sys}` calibration
      tables (**sdcal**)
   #. Generate the double-circle gaincal calibration tables by
      applying :math:`T_{sky}` and :math:`T_{sys}` calibration
      tables on-the-fly (**sdgaincal**)
   
      -  You can set *spwmap* and *interp* for each
         pre-application caltable if necessary
   
   #. Apply the double-circle gaincal calibration tables
      (**applycal**)
   
   In CASA, this looks like the following:
   
   ::
   
      sdcal(infile=inputvis, calmode='ps', outfile='sky.tbl')
      sdcal(infile=inputvis, calmode='tsys',
      outfile='tsys.tbl')
      sdgaincal(infile=inputvis, applytable=['sky.tbl',
      'tsys.tbl'],outfile='DCgaintable',
      calmode='doublecircle')
      applycal(vis=inputvis, gaintable='DCgaintable')
   

.. _Development:

Development
   None
   
   