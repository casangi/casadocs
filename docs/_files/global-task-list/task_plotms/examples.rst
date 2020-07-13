Examples
========

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      NOTE: These examples are not comprehensive, as **plotms** has a
      substantial list of parameters and allowed values!  See the
      `documentation on using
      plotms <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing/using-plotms-to-plot-and-edit-visibilities-and-calibration-tables>`__
      under Data Examination and Editing for details of the task
      parameters and how they correspond to settings in the GUI.

      .. rubric:: Default Plots (unflagged data only)
         :name: default-plots-unflagged-data-only

      All that is really required is a dataset or cal table to plot. 
      The first example will plot Amp vs. Time, the default axes for a
      MeasurementSet.  The second plot will be Tsys vs. Channel, the
      default axes for the cal table type being plotted.  By default,
      *customflaggedsymbol=False* and no flagged data is plotted.  Since
      no averaging or selection is done, **plotms** will plot the entire
      dataset, which could take some time and substantial memory.

      .. container:: casa-input-box

         | plotms(vis='test.ms')
         | plotms(vis='uid___A002_X99c183_X25b6.ms.tsys')

      .. rubric:: Change Default Axis and Datacolumn
         :name: change-default-axis-and-datacolumn

      Here we change the default datacolumn and axes. In the first
      example, *yaxis='amp'* is implied since it is the default.

      .. container:: casa-input-box

         | plotms(vis='test.ms', ydatacolumn='corrected',
           xaxis='channel')
         | plotms(vis='test.ms', xaxis='elevation', yaxis='azimuth')

      .. rubric:: Plot Flagged Data
         :name: plot-flagged-data

      By setting *customflaggedsymbol=True*, **plotms** uses the default
      red circles for the flagged data. In the second example, a custom
      symbol is specified.

      .. container:: casa-input-box

         | plotms(vis='test.ms', customflaggedsymbol=True)
         | plotms(vis='test.ms', customflaggedsymbol=True,
           flaggedsymbolshape='diamond', flaggedsymbolsize=5,
           flaggedsymbolcolor='00ff00', flaggedsymbolfill='mesh3')

      .. rubric:: Plot with Colorized Data
         :name: plot-with-colorized-data

      Note that the colorization overrides the default or custom color
      for all data, unflagged or flagged.  In the following example, all
      data in the MS will be colorized according to its spectral window.

      .. container:: casa-input-box

         plotms(vis='test.ms', customflaggedsymbol=True,
         coloraxis='spw')

      .. rubric:: Plot with Data Selection
         :name: plot-with-data-selection

      Note that all selections are strings, including numerical values. 
      Refer to the documentation on `Data
      Selection <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__
      for an explanation of MeasurementSet selection.  In the second
      example, the *correlation* parameter is used for polarization
      selection on a calibration table, and the result is plotted with
      the default axes Gain Amplitude vs. Time for this cal table type.

      .. container:: casa-input-box

         | plotms(vis='test.ms', field='1', spw='0:3~10', antenna='1&2',
           scan='2~4', corr='XX,YY')
         | plotms(vis='bpphase.gcal', correlation='R')

      .. rubric:: Plot with Iteration
         :name: plot-with-iteration

      The first example plots one plot per page.  The second example
      demonstrates iteration plots on a 2x2 grid.  In the third example,
      all iteration plots are exported with the plotfile name appended
      with the iteration label and index, i.e. test_Scan2.jpg,
      test_Scan3_2.jpg, test_Scan4_3.jpg.

      .. container:: casa-input-box

         | plotms(vis='test.ms', xaxis='freq', iteraxis='baseline')
         | plotms(vis='test.ms', xaxis='freq', iteraxis='baseline',
           gridrows=2, gridcols=2)
         | plotms(vis='test.ms', scan='2~4', iteraxis='scan',
           plotfile='test.jpg', exprange='all')

      .. rubric:: Plot with Averaging
         :name: plot-with-averaging

      In the first example, the *avgtime* value is in seconds.  In the
      second example, the channel numbers plotted on the x-axis
      (*'chan'*) will refer to the binned channels (0-based), not the
      averaged channel number for the bin.  Use the Locate feature to
      find the channel range for each bin.

      .. container:: casa-input-box

         | plotms(vis='test.ms', avgtime='1e8', avgscan=True)
         | plotms(vis='test.ms', xaxis='chan', avgchannel='128')

      .. rubric:: Using On-the-Fly Calibration
         :name: using-on-the-fly-calibration

      The calibration library to apply is contained in the file
      *calibration.txt*.  By default, this sets Calibration to "On" in
      the GUI and applies the cal library; you can select "OFF" but keep
      the callib setting.

      .. container:: casa-input-box

         plotms(vis='ngc5921.ms', xaxis='frequency', yaxis='amp',
         ydatacolumn='corrected', field='N5921_2', antenna='*&*',
         callib='calibration.txt')

      .. rubric:: Overplot Two Datasets on One Plot
         :name: overplot-two-datasets-on-one-plot

      This is **one example** with two **plotms** calls.  Be sure to
      increment *plotindex* and set *clearplots* to False on the second
      call.  Here the second plot is set to a different color.  A legend
      is included to indicate which points represent the Scan axis and
      which are Field points.

      .. container:: casa-input-box

         | plotms(vis='test1.ms', yaxis='scan', showlegend=True,
           legendposition='lowerRight')
         | plotms(vis='test2.ms', yaxis='field', plotindex=1,
           clearplots=False, showlegend=True,
           legendposition='lowerRight', customsymbol=True,
           symbolcolor='00FF00')

      .. rubric:: Plot Two Datasets on One Page
         :name: plot-two-datasets-on-one-page

      Here we use a grid with 2 rows, 1 column, and specify the plot for
      each row.  The first **plotms** call uses the defaults
      *rowindex=0, colindex=0, plotindex=0, clearplots=True*.  In the
      second call we must increment the *plotindex* and *rowindex* (so
      it does not overplot the first plot), and set *clearplots=False*
      so that it keeps the first plot.  We can also export this page
      with two plots.

      .. container:: casa-input-box

         | plotms(vis='test1.ms', yaxis='field', gridrows=2, gridcols=1)
         | plotms(vis='test2.ms', yaxis='field', gridrows=2, gridcols=1,
           rowindex=1, plotindex=1, clearplots=False,
           plotfile='fields.jpg')

      .. rubric:: Saving your plot
         :name: saving-your-plot

      The export format can be indicated in the plotfile name or by
      using the *expformat* parameter.  Allowed extensions include jpg,
      png, pdf, ps, and txt.  Exporting the plot as text produces
      Locate-style output.

      Here the plot will be exported in PNG format, as indicated by the
      plotfile extension:

      .. container:: casa-input-box

         plotms(vis='test.ms', plotfile='test.png')

      Example with *expformat* parameter.  Note that the plotfile name
      is used as given and no extension is added:

      .. container:: casa-input-box

         plotms(vis='ngc5921.ms', plotfile='ngc5921', expformat='jpg')

      When scripting the **plotms** calls, one may want to produce
      plotfiles without a GUI:

      .. container:: casa-input-box

         plotms(vis='test.ms', plotfile='test.jpg', showgui=False)

      With iteration, one may wish to export only the first plot
      (default) or all plots using the *exprange* parameter.  The
      iteration string will be appended to the filename before the
      extension.

      .. container:: casa-input-box

         plotms(vis='ngc5921.ms', iteraxis='baseline',
         plotfile='ngc5921.jpg', exprange='all')

.. container:: section
   :name: viewlet-below-content-body
