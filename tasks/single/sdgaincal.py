#
# stub function definition file for docstring parsing
#

def sdgaincal(infile, calmode='doublecircle', radius='', smooth=True, antenna='', field='', spw='', scan='', intent='', applytable='', interp='', spwmap=[''], outfile='', overwrite=False):
    r"""
 MS SD gain calibration task

Parameters
   - **infile** (string) - name of input SD dataset (must be MS)
   - **calmode** (string) - gain calibration mode ("doublecircle")
   - **antenna** (string) - select data by antenna name or ID, e.g. "PM03"
   - **field** (string) - select data by field IDs and names, e.g. "3C2*" ("" = all)
   - **spw** (string) - select data by spw IDs (spectral windows), e.g., "3,5,7" ("" = all)
   - **scan** (string) - select data by scan numbers, e.g. "21~23" (""=all)
   - **applytable** (variant) - (List of) sky and/or tsys tables for pre-application
   - **outfile** (string) - name of output caltable
   - **overwrite** (bool) - overwrite the output file if already exists [True, False]

Subparameters
   .. raw:: html

      <details><summary><i> calmode = doublecircle </i></summary>

   - **radius** (variant='') - radius of central region to be used for calibration
   - **smooth** (bool=True) - smooth data or not

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> applytable != '' </i></summary>

   - **interp** (variant='') - Interp type in time[,freq], per gaintable. default==linear,linear
   - **spwmap** (intArray=-1) - Spectral window mappings to form for applytable(s)

   .. raw:: html

      </details>


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
         :name: configurable-inputs-control-the-calibration-mode-selection-parameters-and-output-behavior

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

      | 
      |


   Bibliography
         :sup:`1. Phillips et al, 2015. Fast Single-Dish Scans of the
         Sun Using
         ALMA.` `PDF <http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?2015ASPC..499..347P&amp;data_type=PDF_HIGH&amp;whole_paper=YES&amp;type=PRINTER&amp;filetype=.pdf>`__ `<#ref-cit1>`__

    """
    pass
