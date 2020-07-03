.. container::
   :name: viewlet-above-content-title

The Multi-MS
============

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Describing a Multi-MS and how to create one

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Parallel processing using Multi-MS (MMS) in CASA is
         unverified. Please use at own discretion.
         :name: parallel-processing-using-multi-ms-mms-in-casa-is-unverified.-please-use-at-own-discretion.

      .. rubric:: Please consider\ \ `parallel
         imaging <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/parallel-imaging>`__\ \ using
         normal MS as alternative.
         :name: please-consider-parallel-imaging-using-normal-ms-as-alternative.

      .. rubric::  
         :name: section

      .. rubric:: Multi-MS Structure
         :name: multi-ms-structure

      A Multi-MS (MMS) is structured to have a reference MS on the top
      directory and a sub-directory called SUBMSS, which contains each
      partitioned Sub-MS. A Multi-MS can be handled like a normal
      “monolithic” MS. It can be moved and renamed like any other
      directory. CASA tasks that are not MMS-aware can process it like a
      monolithic MS.

      All sub-tables of Sub-MSs are identical, except for the SOURCE and
      HISTORY sub-tables. The reference MS contains links to the
      sub-tables of the first Sub-MS, which is identified by a "0000"
      index on its name. All subsequent Sub-MSs also contain links to
      the sub-tables of the first Sub-MS, except for the SOURCE and
      HISTORY sub-tables. The following is a typical view of the
      reference MS directory of a Multi-MS. Symbolic links have an **@**
      at the end.

      .. container:: terminal-box

         | > ls uid___A002_X30a93d_X43e.ms/
         | ANTENNA@       CALDEVICE@         FIELD@     OBSERVATION@   
           PROCESSOR@         STATE@    SYSPOWER@  WEATHER@
         | ASDM_ANTENNA@  DATA_DESCRIPTION@  FLAG_CMD@  POINTING@      
           SOURCE@            SUBMSS/   table.dat
         | ASDM_CALWVR@   FEED@              HISTORY@   POLARIZATION@  
           SPECTRAL_WINDOW@   SYSCAL@   table.info

       The following is a view of the Sub-MSs directory. The Sub-MS
      names have the MMS name followed by a 4-digit index.

      .. container:: terminal-box

         | > ls uid___A002_X30a93d_X43e.ms/SUBMSS/
         | uid___A002_X30a93d_X43e.ms.0000.ms/
           uid___A002_X30a93d_X43e.ms.0002.ms/
         | uid___A002_X30a93d_X43e.ms.0001.ms/
           uid___A002_X30a93d_X43e.ms.0003.ms/

       Next example shows the second Sub-MS, which has symbolic links to
      all sub-tables except the SOURCE and HISTORY tables. These two
      tables need write-access in several cases when running in
      parallel.

      .. container:: terminal-box

         | > ls –l
           uid___A002_X30a93d_X43e.ms/SUBMSS/uid___A002_X30a93d_X43e.ms.0001.ms/
         | ANTENNA -> ../uid___A002_X30a93d_X43e.ms.0000.ms/ANTENNA/
         | ASDM_ANTENNA ->
           ../uid___A002_X30a93d_X43e.ms.0000.ms/ASDM_ANTENNA/
         | ASDM_CALWVR ->
           ../uid___A002_X30a93d_X43e.ms.0000.ms/ASDM_CALWVR/
         | CALDEVICE -> ../uid___A002_X30a93d_X43e.ms.0000.ms/CALDEVICE/
         | DATA_DESCRIPTION ->
           ../uid___A002_X30a93d_X43e.ms.0000.ms/DATA_DESCRIPTION/
         | FEED -> ../uid___A002_X30a93d_X43e.ms.0000.ms/FEED/
         | FIELD -> ../uid___A002_X30a93d_X43e.ms.0000.ms/FIELD/
         | FLAG_CMD -> ../uid___A002_X30a93d_X43e.ms.0000.ms/FLAG_CMD/
         | HISTORY/
         | OBSERVATION ->
           ../uid___A002_X30a93d_X43e.ms.0000.ms/OBSERVATION/
         | POINTING -> ../uid___A002_X30a93d_X43e.ms.0000.ms/POINTING/
         | POLARIZATION ->
           ../uid___A002_X30a93d_X43e.ms.0000.ms/POLARIZATION/
         | PROCESSOR -> ../uid___A002_X30a93d_X43e.ms.0000.ms/PROCESSOR/
         | SOURCE/
         | SPECTRAL_WINDOW ->
           ../uid___A002_X30a93d_X43e.ms.0000.ms/SPECTRAL_WINDOW/
         | STATE -> ../uid___A002_X30a93d_X43e.ms.0000.ms/STATE/
         | SYSCAL -> ../uid___A002_X30a93d_X43e.ms.0000.ms/SYSCAL/
         | SYSPOWER -> ../uid___A002_X30a93d_X43e.ms.0000.ms/SYSPOWER/
         | table.dat
         | table.f1
         | table.f10
         | .....
         | WEATHER -> ../uid___A002_X30a93d_X43e.ms.0000.ms/WEATHER/

      .. rubric::  
         :name: section-1
         :class: section

      .. rubric:: Multi-MS Creation
         :name: sec511
         :class: section

      .. rubric:: **partition**
         :name: sec512
         :class: subsection

      The partition task is the main task to create a “Multi-MS”. It
      takes an input MeasurementSet and creates an output “Multi-MS”
      based on the data selection parameters.

      The inputs to **partition** are:

      .. container:: casa-input-box

         | CASA <1>: inp partition
         | --------> inp(partition)
         | #  partition :: Task to produce Multi-MSs using parallelism
         | vis                 =         ''        #  Name of input
           MeasurementSet
         | outputvis           =         ''        #  Name of output
           MeasurementSet
         | createmms           =       True        #  Should this create
           a multi-MS output
         |      separationaxis =     'auto'        #  Axis to do
           parallelization across(scan, spw, baseline, auto)
         |      numsubms       =     'auto'        #  The number of
           SubMSs to create (auto or any number)
         |      flagbackup     =       True        #  Create a backup of
           the FLAG column in the MMS.
         | datacolumn          =      'all'        #  Which data
           column(s) to process.
         | field               =         ''        #  Select field using
           ID(s) or name(s).
         | spw                 =         ''        #  Select spectral
           window/channels.
         | scan                =         ''        #  Select data by
           scan numbers.
         | antenna             =         ''        #  Select data based
           on antenna/baseline.
         | correlation         =         ''        #  Correlation: ''
           ==> all, correlation='XX,YY'.
         | timerange           =         ''        #  Select data by
           time range.
         | intent              =         ''        #  Select data by
           scan intent.
         | array               =         ''        #  Select
           (sub)array(s) by array ID number.
         | uvrange             =         ''        #  Select data by
           baseline length.
         | observation         =         ''        #  Select by
           observation ID(s).
         | feed                =         ''        #  Multi-feed
           numbers: Not yet implemented.

      .. rubric:: The createmmsparameter
         :name: sec513
         :class: subsubsection

      The keyword createmmsis by default set to True to create an output
      MMS. It contains three sub-parameters, separationaxis, numsubmsand
      flagbackup. Partition accepts four axes to do separation across:
      ’auto’, ’scan’ ’spw’ or ’baseline’. The default
      separationaxis='auto'will first separate the MS in spws, then in
      scans. It tries to balance the spw and scan content in each Sub-MS
      also taking into account the available fields.

      The baseline axis is mostly useful for Single-Dish data. This axis
      will partition the MS based on the available baselines. If the
      user wants only auto-correlations, she/he should use the antenna
      selection syntax such as antenna='*&&&'together with the baseline
      separation axis. Note that if numsubms='auto', the task will try
      to create as many Sub-MSs as the number of available parallel
      cores used when starting CASA with mpicasa. If the user wants to
      have one Sub-MS for each baseline, he/she should set the
      numsubmsparameter to a number higher than the number of baselines
      to achieve this.

      The user may force the number of “Sub-MSs” in the output MMS by
      setting the sub-parameternumsubms. The default 'auto'is to create
      as many Sub-MSs as the number of engines used when starting CASA
      with mpicasa, in an optimized way.

      The flagbackupsub-parameter will create a backup of the FLAG
      column and save it to the .flagversions file.

      .. rubric:: **importasdm**
         :name: sec514
         :class: subsection

      Task partition has been embedded in task importasdmso that at
      import time the user can already create a MMS. Set the
      parametercreatemmsto True and the output of importasdmwill be a
      MMS created with default parameters.
      Sub-parametersseparationaxisandnumsubmsare also available in
      importasdm. From this point on in the data reduction chain, tasks
      that have been parallelized will run automatically in parallel
      when they see an MMS and tasks that are not parallelized will work
      in the same way as they normally do on a MS.

       

       

.. container:: section
   :name: viewlet-below-content-body
