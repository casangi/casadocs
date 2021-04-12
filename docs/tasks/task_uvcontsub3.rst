

.. _Description:

Description
   .. warning:: **ALERT: uvcontsub3** is an experimental task and will
      eventually replace the current **uvcontsub** code with the
      goal of taking less time and temporary disk space.
   
   **uvcontsub3** is a task to perform continuum fitting and
   subtraction in the uv plane
   
   This task estimates the continuum emission by fitting
   polynomials to the real and imaginary parts of the spectral
   windows and channels selected by *fitspw*. This fit represents
   a model of the continuum in all channels. The fitted continuum
   spectrum is subtracted from all channels selected in *spw*, and
   the result (presumably only line emission) is stored in a new
   MS that is always called vis + ".contsub". If an MS with the
   output name already exists, it will be overwritten.
   
   **uvcontsub3** will read from the CORRECTED_DATA column
   of *vis* if it is present, or DATA if it is not. Whichever
   column is read is presumed to have already been calibrated.
   
   .. note::
   
         **WARNING:** Strictly speaking, the **uvcontsub3** model
         is only a good representation of the continuum at the
         phase center. Residuals may be visible for sources far
         away and one may try **imcontsub** in the image domain
         for improved results. 
   
   .. note:: **WARNING** **:** * fitorders* > 1 are strongly
      discouraged because high order polynomials have more
      flexibility, may absorb line emission, and tend to go wild
      at the edges of *fitspw*, which is not what you
      want. default: *0* (constant)
   

   .. rubric:: Parameter descriptions
   
   *vis*
   
   Name of input MS. Output goes to vis + ".contsub" (will be
   overwritten if already exists)
   
   *fitspw*
   
   Selection of spectral windows and channels to use in the fit for
   the continuum, using general `MS selection
   syntax <../../notebooks/visibility_data_selection.ipynb>`__ for
   spectral windows, e.g. in spw:chan format (spw ids are required
   but '\*' can be used) or as frequencies. See the note
   under *combine*. default: *fitspw=''* (all)
   
   .. warning:: **WARNING:** The *fitspw* selection is based on the channel
      numbers in the uv-data of the input MS file, which are most
      likely different from the channel numbers in the image plane
      after running **tclean**. 
   
   *combine*
   
   Continuum solutions will by default break at scan, field, and spw
   boundaries.  To allow solutions across spw boundaries, *combine*
   can be set to '*spw*'. '*combine*' must include *'spw'* if spw
   contains spws that are not in *fitspw*!  default: '' which is that
   solutions will break at scan, field, and spw

   .. warning:: **WARNING:** uvcontsub3 (deliberately) does not
                support combination by anything except '*spw*'. Other
                combination options supported in uvcontsub, '*scan*',
                or '*spw*', are not supported in this experimental
                uvcontsub3 version. Also, combination by spw is only
                expected to work correctly for spws with the same
                number of channels.
   
   *fitorder*
   
   Polynomial order for the fits of the continuum w.r.t.
   frequency. *fitorders* > 1 are strongly discouraged because high
   order polynomials have more flexibility, may
   absorb line emission, and tend to go wild at the edges
   of *fitspw*, which is not what you want. default: *0* (constant)
   
   *field*

   Field selection for
   continuum estimation and subtraction. The estimation and
   subtraction is done for each selected field separately in turn.
   default: ''  (all fields).
   
   *spw*

   Optional per spectral window selection of channels to include in
   the output. See the note under *combine*. The sub-MS output
   spectral windows will be renumbered to start from 0, as
   in **split**. default: '' (all spws)

   *scan*

   Scan id selection. default: '' (all scans)

   *intent*

   Selection by scan intent. default: '' (all intents)

   *correlation*
   
   Selection by correlation. default: '' (all correlations)
   (polarization products)

   *observation*
   
   Selection by observation id. default: '' (all obs ids)


.. _Examples:

Examples
   **Example 1:**
   
   Subtract the continuum of channels 10~100 and 300~350 in spw 0
   (assuming that the line is in channels 101~299). Note that we also
   exclude edge channels, e.g. the first 9 channels. We use a
   fitorder of 0 (default). 
   
   ::
   
      uvcontsub3(vis='myMS.ms',fitspw='0:10~100;300~350')
   

.. _Development:

Development
   No additional development details

