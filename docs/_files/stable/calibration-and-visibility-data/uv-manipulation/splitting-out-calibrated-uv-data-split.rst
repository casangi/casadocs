.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Split UV-data
=============

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Breaking out a subset of visibility data using split and mstransform

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      The **split** task selects a subset of data from a MeasurementSet
      and creates a new MS with only those selected data.  All of the
      usual selection criteria can be applied (field, spectral window,
      antenna, time range, etc.). Additionally the user can choose to
      select only a single column of data (typically CORRECTED); the
      user may also elect to export all data columns (DATA, MODEL,
      CORRECTED, FLOAT_DATA). If only a single column is selected, it
      will  appear as the DATA column in the output MS, unless the input
      *datacolumn* is set to FLOAT_DATA. In this case the output column
      will also be FLOAT_DATA. This suite of capabilities is of great
      utility for creating smaller MeasurementSets for imaging and
      further analysis. It is also helpful in many circumstances to
      facilitate self-calibration, since the **gaincal** task operates
      from the DATA column. 

       The top-level inputs of **split** are:

      .. container:: casa-input-box

         CASA <1>: inp split
         split :: Create a visibility subset from an existing visibility
         set
         vis           =     ''            # Name of input
         MeasurementSet or Multi-MS
         outputvis     =     ''            # Name of output
         MeasurementSet or Multi-MS
         keepmms       =     True          # If the input is a Multi-MS
         the output will also be a Multi-MS
         field         =     ''            # Select field using ID(s) or
         name(s)
         spw           =     ''            # Select spectral
         window/channels
         scan          =     ''            # Select data by scan numbers
         antenna       =     ''            # Select data based on
         antenna/baseline
         correlation   =     ''            # Correlation: '' ==> all,
         correlation='XX,YY'
         timerange     =     ''            # Select data by time range
         intent        =     ''            # Select data by scan intent.
         array         =     ''            # Select (sub)array by array
         ID number(s)
         uvrange       =     ''            # Select data bt baseline
         length
         observation   =     ''            # Select data by observation
         ID(s).
         feed          =     ''            # Multi-feed numbers: Not yet
         implemented.
         datacolumn    =     'corrected'   # Which data column(s) to
         process
         keepflags     =     True          # Keep \*completely flagged
         rows\* instead of dropping them
         width         =     1             # Number of channels to
         average to form one output channel
         timebin       =     '0s'          # Bin width for time
         averaging

      Usually you will run **split** with *datacolumn=’corrected’* as
      previous operations (e.g. **applycal**) will have placed the
      calibrated data in the *CORRECTED_DATA* column of the MS. This
      will produce a new MS with this *CORRECTED_DATA* in its *DATA*
      column. The modes available in *datacolumn* are:

      .. container:: casa-input-box

         | corrected
         | data
         | model
         | data,model,corrected
         | float_data
         | lag_data
         | float_data,data
         | lag_data,data
         | all
         | #float_data is used for single dish processing

      For example, to split out 46 channels (5-50) from spw 1 of our
      NGC5921 calibrated dataset:

      .. container:: casa-input-box

         | split(vis='ngc5921.usecase.ms',
         | outputvis='ngc5921.split.ms',
         | field='2', # Output NGC5921 data (field 2)
         | spw='0:5~50', # Select 46 chans from spw 0
         | datacolumn='corrected') # Take the calibrated data column

      Starting in CASA 4.6.0, **split2** has been renamed to **split**
      and became the default in CASA. The previous implementation of
      **split** is still available under the name **oldsplit**. The
      interface of both implementations is the same, but the new
      **split** uses the MSTransform framework underneath. See the
      "`Manipulating Visibilities with
      MSTransform <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/uv-manipulation/manipulating-visibilities-with-mstransform>`__"
      chapter for detailed information on mstransform.

       

      | 
      |  

.. container:: section
   :name: viewlet-below-content-body
