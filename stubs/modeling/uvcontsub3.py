#
# stub function definition file for docstring parsing
#

def uvcontsub3(vis, fitspw='', combine='', fitorder=0, field='', spw='', scan='', intent='', correlation='', observation=''):
    r"""
An experimental clone of uvcontsub

Parameters
   - **vis** (string) -  [1]_
   - **fitspw** (string='') -  [2]_
   - **combine** (string='') -  [3]_
   - **fitorder** (int=0) -  [4]_
   - **field** ({string, stringArray, int, intArray}='') -  [5]_
   - **spw** (string='') -  [6]_
   - **scan** (string='') -  [7]_
   - **intent** (string='') -  [8]_
   - **correlation** ({string, stringArray}='') -  [9]_
   - **observation** ({string, int}='') -  [10]_


Description


      .. warning:: **ALERT: uvcontsub3** is an experimental task and will
         eventually replace the current **uvcontsub** codewith the
         goal of takingless time and temporary disk space.

      **uvcontsub3**is a task to perform continuum fitting and
      subtraction in the uv plane


      This task estimates the continuum emission by fitting
      polynomials to the real and imaginary parts of the spectral
      windows and channels selected by*fitspw*. This fit represents
      a model of the continuum in all channels.The fitted continuum
      spectrum is subtracted from all channels selected in*spw*, and
      the result (presumably only line emission) is stored in a new
      MS that is always called vis + ".contsub". If an MS with the
      output name already exists, it will be overwritten.


      **uvcontsub3**will read from the CORRECTED_DATA column
      of*vis*if it is present, or DATA if it is not. Whichever
      column is read is presumed to have already been calibrated.


      .. note::

            **WARNING:**Strictly speaking, the**uvcontsub3**model
            is only a good representation of the continuum at the
            phase center. Residuals may be visible for sources far
            away and one may try**imcontsub**in the image domain
            for improved results.

      .. note:: **WARNING** **:** *fitorders*> 1 are strongly
         discouraged because high order polynomials have more
         flexibility, may absorb line emission, and tend to go wild
         at the edges of*fitspw*, which is not what you
         want.default:*0*(constant)


      

   .. rubric:: Parameter descriptions
      

   .. rubric:: *vis*
      

   Name of input MS. Output goes to vis + ".contsub" (will be
   overwritten if already exists)

   *fitspw*

   Selection of spectral windows and channels to use in the fit for
   the continuum, using general`MS selection
   syntax <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__for
   spectral windows, e.g. in spw:chan format (spw ids are required
   but*'*'*can be used) or as frequencies.See the note
   under*combine*. default:*fitspw=''*(all)

   .. warning:: **WARNING:**The *fitspw* selection is based on the channel
      numbers in the uv-data of the input MS file, which are most
      likely different from the channel numbers in the image plane
      after running **tclean**.

   .. rubric:: *combine*
      

   Continuum solutions will break at scan, field, and spw boundaries
   according to*solint.* To allow solutions across these
   boundaries,*combine*can be set to'*spw*', '*scan*', or*'spw,
   scan'. combine* must include*'spw'* ifspw contains spws that
   are not in*fitspw*! default:*''* which is that solutions will
   break at scan, field, and spw

   .. rubric:: *fitorder*
      

   | Polynomial order for the fits of the continuum w.r.t.
     frequency.*fitorders*> 1 are strongly discouraged because high
     order polynomials have more flexibility, may
   | absorb line emission, and tend to go wild at the edges
     of*fitspw*, which is not what you want.default:*0*(constant)

   .. rubric:: *field*
      

   `Field
   selection <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__for
   continuum estimation and subtraction. The estimation and
   subtraction is done for each selected field separately in turn.
   default:*''* (all fields).(See`Data Selection in a
   MeasurementSet <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__)

   .. rubric:: *spw*
      

   Optional per spectral window selection of channels to include in
   the output. See the note under*combine*.The sub-MS output
   spectral windows will be renumbered to start from 0, as
   in**split**. default:*''*(all spws)(See`Data Selection in a
   MeasurementSet <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__)

   .. rubric:: *scan*
      

   Scanid selection. default: *''* (all scans) (See `Data Selection
   in a
   MeasurementSet <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__)

   .. rubric:: *intent*
      

   Selection by scan intent.default:*''*(all intents) (See`Data
   Selection in a
   MeasurementSet <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__)

   .. rubric:: *correlation*
      

   Selection by correlation.default:*''*(all correlations)
   (polarization products)(See`Data Selection in a
   MeasurementSet <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__)

   .. rubric:: *observation*
      

   Selection by observation id.default:*''*(all obs ids)
   (See`Data Selection in a
   MeasurementSet <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__)




Details
   Explanation of each parameter

.. [1] 
   **vis** (string)
      | Name of input MS.  Output goes to vis + ".contsub"
.. [2] 
   **fitspw** (string='')
      | Spectral window:channel selection for fitting the continuum
.. [3] 
   **combine** (string='')
      | Data axes to combine for the continuum estimation (none ('') or spw)
.. [4] 
   **fitorder** (int=0)
      | Polynomial order for the fits
.. [5] 
   **field** ({string, stringArray, int, intArray}='')
      | Select field(s) using id(s) or name(s)
.. [6] 
   **spw** (string='')
      | Spectral window selection for output
.. [7] 
   **scan** (string='')
      | Select data by scan numbers
.. [8] 
   **intent** (string='')
      | Select data by scan intents
.. [9] 
   **correlation** ({string, stringArray}='')
      | Select correlations
.. [10] 
   **observation** ({string, int}='')
      | Select by observation ID(s)

    """
    pass
