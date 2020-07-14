msuvbin
=======

.. container:: documentDescription description

   task description

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. container:: alert-box

         **WARNING**: This task is currently experimental.

      .. rubric:: Summary
         :name: summary

      **msuvbin** is a uv gridding task. It is primarily designed to be
      used for large volumes of data from multiple observing epochs that
      need to be imaged together in order to obtain a final image
      product for the target source or field of interest. One way of
      proceeding with such large multi-epoch data is to image each epoch
      separately and average the images afterward. Instead, **msuvbin**
      averages the visibilities on a common uv grid, then the resulting
      data product can be imaged using the task **clean** or **tclean**.
      Averaging such uv data into a common uv grid first has several
      conveniences and advantages, such as easily doing the proper
      weighted average. More details on this task can be found in the
      `EVLA Memo
      198 <https://library.nrao.edu/public/memos/evla/EVLAM_198.pdf>`__, which
      explains the current implementation in **msuvbin** and its
      limitations. In particular, note the issue/limitation of creating
      a uv grid with wprojection and then using Cotton-Schwab major
      cycles to image it; see the EVLA Memo 198 for more details.

       

      .. rubric:: Parameter descriptions
         :name: parameter-descriptions

      .. rubric:: *vis*
         :name: vis

      Name of input visibility file

      .. rubric:: *field*
         :name: field

      Field name list; note that this position will define the phase
      center of the output uv grid

      .. rubric:: *spw
         *
         :name: spw

      Spectral window selection

      .. rubric:: *taql* 
         :name: taql

      TaQl expression for data selection (see  `Data Selection in a
      Measurement
      Set <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__  or `CASAcore NOTE
      199: Table Query
      Language <https://casacore.github.io/casacore-notes/199.html>`__  for
      more information)

      .. rubric:: *outvis*
         :name: outvis

      Name of output grid

      .. rubric:: *phasecenter*
         :name: phasecenter
         :class: p1

      Phase center of the grid, to be used when the phase center of the
      selected field is not the desired output phase center.
      Example: phasecenter='J2000 18h03m04 -20d00m45.1'

      .. rubric:: *nx*
         :name: nx

      Number of pixels along the x axis of the grid. Default: 1000

      .. rubric:: *ny*
         :name: ny

      Number of pixels along the y axis of the grid. Default: 1000

      .. rubric:: *cell*
         :name: cell

      Cellsize of the grid (given in sky units). Default: '1arcsec'

      .. rubric:: *ncorr*
         :name: ncorr

      Number of correlation/polarization plane in uv grid (allowed 1, 2,
      4). For example, if the input data set has the correlations RR and
      LL, and *ncorr* =1, then the output uv grid will be written as
      Stokes I. If *ncorr=* 2, then the output grid will have both the
      RR and LL correlations. Default: 1

      .. rubric:: *nchan*
         :name: nchan

      Number of spectral channels in the output uv grid. Default: 1

      .. rubric:: *fstart*
         :name: fstart

      Frequency of the first channel. Default: '1GHz' (the user needs to
      give a useful input here)

      .. rubric:: *fstep*
         :name: fstep

      Width of spectral channel. Default: '1kHz'

      .. rubric:: *wproject*
         :name: wproject

      Do wprojection correction while gridding. Default: False

      .. rubric:: *memfrac*
         :name: memfrac

      Controls how much of computer's memory is available for gridding.
      Default=0.5

       

.. container:: section
   :name: viewlet-below-content-body

.. toctree::
   :hidden:
   :maxdepth: 3

   task_msuvbin/changelog
   task_msuvbin/examples
