hanningsmooth
=============

.. container:: documentDescription description

   task description

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      This is the new implementation of **hanningsmooth**.

      .. container:: info-box

         | \* Task **hanningsmooth2** has been renamed to
           **hanningsmooth**.
         | \* Please, update your scripts to call **hanningsmooth**
           instead.

      The new **hanningsmooth** task uses the MSTransform framework
      underneath but keeps roughly the same interface as previous
      version of hanningsmooth.

      This function Hanning smooths the frequency channels with a
      weighted running average. The weights are 0.5 for the central
      channel and 0.25 for each of the two adjacent channels. The first
      and last channels are flagged. Inclusion of a flagged value in an
      average causes that data value to be flagged.

      If the *CORRECTED* data column is requested for an MS that does
      not contain this column, it will use *DATA* to calculate the
      smoothing and save it to *DATA* in the output MS.

      .. container:: alert-box

         WARNING: by default, all visibility columns will be smoothed.

      .. rubric:: Parameter Descriptions
         :name: parameter-descriptions

      .. rubric:: Input and output MeasurementSets
         :name: title0

      The input visibility file (MS or MMS) given by the
      *vis* parameters will be Hanning smoothed and saved in an output
      given by the *outputvis* parameter.

      For example, *vis* = ['ngc5921.ms'] *, output vis* =
      'out_ngc5921.mms'. 

      .. rubric:: Output MS or Multi-MS: keepmms parameter
         :name: output-ms-or-multi-ms-keepmms-parameter

      If *keepmms* = True, a
      `Multi-MS <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/the-multi-ms>`__
      will be created as the output if the input is a Multi-MS(MMS),
      which is the default behaviour. The output Multi-MS will have the
      same partition axis of the input MMS. See the `Parallel
      Processing <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing>`__
      chapter for more information on the MMS format.

      .. rubric:: Data Column parameter
         :name: data-column-parameter

      The parameter *datacolumn* chooses which column to use for the
      processing (case-insensitive). The default is set to all columns
      that exist in the input MS. 

      .. rubric:: Data Selection parameters
         :name: data-selection-parameters

      For more details on how to perform data selection within the MS
      (i.e., selecting by field, SPW, antenna, etc.), see the
      `Visibility Data
      Selection <resolveuid/5e08acd0d7cf4de1ab2a0e2fd34adfc7>`__
      chapter.

.. container:: section
   :name: viewlet-below-content-body

.. toctree::
   :hidden:
   :maxdepth: 3

   task_hanningsmooth/parameters
   task_hanningsmooth/changelog
   task_hanningsmooth/examples
