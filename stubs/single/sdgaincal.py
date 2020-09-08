#
# stub function definition file for docstring parsing
#

def sdgaincal(infile, calmode='doublecircle', radius='', smooth=True, antenna='', field='', spw='', scan='', intent='', applytable='', interp='', spwmap=[''], outfile='', overwrite=False):
    r"""
 MS SD gain calibration task

Parameters
   - infile_ (string) - name of input SD dataset (must be MS)
   - calmode_ (string='doublecircle') - gain calibration mode ("doublecircle")

      .. raw:: html

         <details><summary><i> calmode = doublecircle </i></summary>

      - radius_ (variant='') - radius of central region to be used for calibration
      - smooth_ (bool=True) - smooth data or not

      .. raw:: html

         </details>
   - antenna_ (string='') - select data by antenna name or ID, e.g. "PM03"
   - field_ (string='') - select data by field IDs and names, e.g. "3C2*" ("" = all)
   - spw_ (string='') - select data by spw IDs (spectral windows), e.g., "3,5,7" ("" = all)
   - scan_ (string='') - select data by scan numbers, e.g. "21~23" (""=all)
   - applytable_ (variant='') - (List of) sky and/or tsys tables for pre-application
   - outfile_ (string='') - name of output caltable
   - overwrite_ (bool=False) - overwrite the output file if already exists [True, False]


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
   parameter (under '*calmode*'). The default is to use the size of
   the primary beam. The data can also be smoothed in the time
   domain, prior to computation of the gain variation. Selection is
   by specral window/channels, field IDs, and antenna through the
   *spw*, *field,* and *antenna* selection parameters. The default is
   to use all data for the gain calibration. The caltable can be
   output with the '*outfile*' parameter.

   | 
   |


   Bibliography
      :sup:`1. Phillips et al, 2015. Fast Single-Dish Scans of the
      Sun Using
      ALMA.` `PDF <http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?2015ASPC..499..347P&amp;data_type=PDF_HIGH&amp;whole_paper=YES&amp;type=PRINTER&amp;filetype=.pdf>`__ `<#ref-cit1>`__




Details
   Explanation of each parameter

.. _infile:

   .. rubric:: infile

   | name of input SD dataset (must be MS)

.. _calmode:

   .. rubric:: calmode

   | gain calibration mode

.. _radius:

   .. rubric:: radius

   | radius of central region to be used for calibration

.. _smooth:

   .. rubric:: smooth

   | smooth data or not

.. _antenna:

   .. rubric:: antenna

   | select data by antenna name or ID, e.g. "PM03"

.. _field:

   .. rubric:: field

   | select data by field IDs and names, e.g. "3C2*" ("" = all)

.. _spw:

   .. rubric:: spw

   | select data by spw IDs (spectral windows), e.g., "3,5,7" ("" = all)

.. _scan:

   .. rubric:: scan

   | select data by scan numbers, e.g. "21~23" (""=all)

.. _intent:

   .. rubric:: intent

   | select data by observation intent, e.g. "OBSERVE_TARGET#ON_SOURCE" (""=all)

.. _applytable:

   .. rubric:: applytable

   | (List of) sky and/or tsys tables for pre-application

.. _interp:

   .. rubric:: interp

   | Interp type in time[,freq], per gaintable. default==linear,linear

.. _spwmap:

   .. rubric:: spwmap

   | Spectral window mappings to form for applytable(s)
   |                      Only used if callib=False
   |                      default: [] (apply solutions from each calibration spw to
   |                      the same MS spw only)
   |                      Any available calibration spw can be mechanically mapped to any 
   |                       MS spw. 
   |                      Examples:
   |                         spwmap=[0,0,1,1] means apply calibration 
   |                           from cal spw = 0 to MS spw 0,1 and cal spw 1 to MS spws 2,3.
   |                         spwmap=[[0,0,1,1],[0,1,0,1]] (use a list of lists for multiple
   |                           applytables)

.. _outfile:

   .. rubric:: outfile

   | name of output caltable

.. _overwrite:

   .. rubric:: overwrite

   | overwrite the output file if already exists


    """
    pass
