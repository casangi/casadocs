.. container::
   :name: viewlet-above-content-title

Methods
=======

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task applycal parameters

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-methods

          

         .. container:: param

            constructor **singledishms**

            .. container:: collcontent

               .. container:: methoddesc

                  This is used to construct a singledishms tool
                  instance. The created instance is just like the
                  default one ('sdms') but physically independent from
                  it. This is useful when users want to create their own
                  tool instance inside scripts/modules to avoid possible
                  conflicts that may happen when using the default tool
                  instance from various places.

               .. container:: methodsection

                  Parameters : None

               .. container:: methodsection

                  Example

               .. container:: methodexam

                  Manual tool construction is done this way: ssd =
                  casac.singledishms()

         .. container:: param

            function **open**

            .. container:: collcontent

               .. container:: methoddesc

                  Close the current MeasurementSet and open a new
                  MeasurementSet instead. The current state of sdms is
                  retained, except for the data selection.

               .. container:: methodsection

                  Parameters

               .. container:: parameters2

                  ms_name : undefined

               .. container:: methodparmtable

                  New MeasurementSet to be processed

.. container:: methodsection

   Example

.. container:: methodexam

   sdms.open('m100_sd.ms')

.. container:: param

   function **close**

   .. container:: collcontent

      .. container:: methoddesc

         This is used to close sdms tools. Note that the data is written
         to disk and detached from sdms tool. This is a synonym for
         done.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         sdms.close()

.. container:: param

   function **done**

   .. container:: collcontent

      .. container:: methoddesc

         This is used to close and sdms tools. Note that the data is
         written to disk and detached from sdms tool. This is a synonym
         for close.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         sdms.done()

.. container:: param

   function **name**

   .. container:: collcontent

      .. container:: methoddesc

         Returns the name of the attached MeasurementSet.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         sdms.name()

.. container:: param

   function **subtract_baseline**

   .. container:: collcontent

      .. container:: methoddesc

         Fit baseline and subtract it from selected spectra

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         datacolumn : undefined = data

      .. container:: methodparmtable

         The name of data column to process ('data', 'float_data', or
         'corrected')

Allowed Value(s)

data float_data corrected

.. container:: parameters2

   outfile : undefined

.. container:: methodparmtable

   The name of output MeasurementSet

.. container:: parameters2

   bloutput : undefined

.. container:: methodparmtable

   The name(s) of Baseline to be output

.. container:: parameters2

   dosubtract : undefined = true

.. container:: methodparmtable

   Execute baseline subtraction from the input data

.. container:: parameters2

   spw : any

.. container:: methodparmtable

   Spectral Window Ids (0 relative) to select; -1 interpreted as all

.. container:: parameters2

   blfunc : undefined = poly

.. container:: methodparmtable

   baseline function

.. container:: parameters2

   order : undefined = 5

.. container:: methodparmtable

   polynomial order

.. container:: parameters2

   clip_threshold_sigma : undefined = 3.0

.. container:: methodparmtable

   threshold for clipping in unit of sigma

.. container:: parameters2

   num_fitting_max : undefined = 1

.. container:: methodparmtable

   maximum number of recursive clipping

.. container:: parameters2

   linefinding : undefined = false

.. container:: methodparmtable

   do line finding

.. container:: parameters2

   threshold : undefined = 5.0

.. container:: methodparmtable

   S/N threshold for line finder

.. container:: parameters2

   avg_limit : undefined = 4

.. container:: methodparmtable

   channel averaging for broad lines in line finding

.. container:: parameters2

   minwidth : undefined = 4

.. container:: methodparmtable

   the minimum channel width to detect as a line by line finder

.. container:: parameters2

   edge : undefined = 00

.. container:: methodparmtable

   channels to drop at beginning and end of spectrum in line finding

.. container:: methodsection

   Example

.. container:: methodexam

   sdms.open('m100_sd.ms') sdms.set_selection(field='M100')
   sdms.subtract_baseline(order=3,clip_threshold_sigma=5.0,num_fitting_max=6)

.. container:: param

   function **subtract_baseline_cspline**

   .. container:: collcontent

      .. container:: methoddesc

         Fit baseline and subtract it from selected spectra

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         datacolumn : undefined = data

      .. container:: methodparmtable

         The name of data column to process ('data', 'float_data', or
         'corrected')

Allowed Value(s)

data float_data corrected

.. container:: parameters2

   outfile : undefined

.. container:: methodparmtable

   The name of output MeasurementSet

.. container:: parameters2

   bloutput : undefined

.. container:: methodparmtable

   The name(s) of Baseline to be output

.. container:: parameters2

   dosubtract : undefined = true

.. container:: methodparmtable

   Execute baseline subtraction from the input data

.. container:: parameters2

   spw : any

.. container:: methodparmtable

   Spectral Window Ids (0 relative) to select; -1 interpreted as all

.. container:: parameters2

   npiece : undefined = 5

.. container:: methodparmtable

   cspline npiece

.. container:: parameters2

   clip_threshold_sigma : undefined = 3.0

.. container:: methodparmtable

   threshold for clipping in unit of sigma

.. container:: parameters2

   num_fitting_max : undefined = 1

.. container:: methodparmtable

   maximum number of recursive clipping

.. container:: parameters2

   linefinding : undefined = false

.. container:: methodparmtable

   do line finding

.. container:: parameters2

   threshold : undefined = 5.0

.. container:: methodparmtable

   S/N threshold for line finder

.. container:: parameters2

   avg_limit : undefined = 4

.. container:: methodparmtable

   channel averaging for broad lines in line finding

.. container:: parameters2

   minwidth : undefined = 4

.. container:: methodparmtable

   the minimum channel width to detect as a line by line finder

.. container:: parameters2

   edge : undefined = 00

.. container:: methodparmtable

   channels to drop at beginning and end of spectrum in line finding

.. container:: methodsection

   Example

.. container:: methodexam

   sdms.open('m100_sd.ms') sdms.set_selection(field='M100')
   sdms.subtract_baseline_cspline(npiece=3,clip_threshold_sigma=5.0,num_fitting_max=6)

.. container:: param

   function **subtract_baseline_sinusoid**

   .. container:: collcontent

      .. container:: methoddesc

         Fit baseline and subtract it from selected spectra

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         datacolumn : undefined = data

      .. container:: methodparmtable

         The name of data column to process ('data', 'float_data', or
         'corrected')

Allowed Value(s)

data float_data corrected

.. container:: parameters2

   outfile : undefined

.. container:: methodparmtable

   The name of output MeasurementSet

.. container:: parameters2

   bloutput : undefined

.. container:: methodparmtable

   The name(s) of Baseline to be output

.. container:: parameters2

   dosubtract : undefined = true

.. container:: methodparmtable

   Execute baseline subtraction from the input data

.. container:: parameters2

   spw : any

.. container:: methodparmtable

   Spectral Window Ids (0 relative) to select; -1 interpreted as all

.. container:: parameters2

   addwn : undefined = 0

.. container:: methodparmtable

   additional wave numbers to use

.. container:: parameters2

   rejwn : undefined

.. container:: methodparmtable

   reject specified wave numbers

.. container:: parameters2

   applyfft : undefined = false

.. container:: methodparmtable

   automatically set wave numbers of sinusoids

.. container:: parameters2

   fftmethod : undefined = fft

.. container:: methodparmtable

   method to automatically set wave numbers of sinusoids ['fft']

.. container:: parameters2

   fftthresh : any = 3.0

.. container:: methodparmtable

   threshold to select wave numbers of sinusoids

.. container:: parameters2

   clip_threshold_sigma : undefined = 3.0

.. container:: methodparmtable

   threshold for clipping in unit of sigma

.. container:: parameters2

   num_fitting_max : undefined = 1

.. container:: methodparmtable

   maximum number of recursive clipping

.. container:: parameters2

   linefinding : undefined = false

.. container:: methodparmtable

   do line finding

.. container:: parameters2

   threshold : undefined = 5.0

.. container:: methodparmtable

   S/N threshold for line finder

.. container:: parameters2

   avg_limit : undefined = 4

.. container:: methodparmtable

   channel averaging for broad lines in line finding

.. container:: parameters2

   minwidth : undefined = 4

.. container:: methodparmtable

   the minimum channel width to detect as a line by line finder

.. container:: parameters2

   edge : undefined = 00

.. container:: methodparmtable

   channels to drop at beginning and end of spectrum in line finding

.. container:: methodsection

   Example

.. container:: methodexam

   sdms.open('m100_sd.ms') sdms.set_selection(field='M100')
   sdms.subtract_baseline(order=3,clip_threshold_sigma=5.0,num_fitting_max=6)

.. container:: param

   function **subtract_baseline_variable**

   .. container:: collcontent

      .. container:: methoddesc

         Fit baseline and subtract it from selected spectra. Fit
         parameters for each spectrum are obtained from a text file.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         datacolumn : undefined = data

      .. container:: methodparmtable

         The name of data column to process ('data', 'float_data', or
         'corrected')

Allowed Value(s)

data float_data corrected

.. container:: parameters2

   outfile : undefined

.. container:: methodparmtable

   The name of output MeasurementSet

.. container:: parameters2

   bloutput : undefined

.. container:: methodparmtable

   The name(s) of Baseline to be output

.. container:: parameters2

   dosubtract : undefined = true

.. container:: methodparmtable

   Execute baseline subtraction from the input data

.. container:: parameters2

   spw : any

.. container:: methodparmtable

   Spectral Window Ids (0 relative) to select; -1 interpreted as all

.. container:: parameters2

   blparam : undefined

.. container:: methodparmtable

   The name of text file that stores fit parameters for each spectrum of
   selected MS

.. container:: parameters2

   verbose : undefined = false

.. container:: methodparmtable

   Print fitting parameters of each spectrum to logger

.. container:: methodsection

   Example

.. container:: methodexam

   sdms.open('m100_sd.ms') sdms.set_selection(field='M100')
   sdms.subtract_baseline_variable('m100_fitparam.txt')

.. container:: param

   function **apply_baseline_table**

   .. container:: collcontent

      .. container:: methoddesc

         For each row of given baseline table, read baseline parameters,
         construct baseline, then subtract it from the corresponding
         spectrum in the MS.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         bltable : undefined

      .. container:: methodparmtable

         The name of input Baseline Table

.. container:: parameters2

   datacolumn : undefined = data

.. container:: methodparmtable

   The name of data column to process ('data', 'float_data', or
   'corrected')

Allowed Value(s)

data float_data corrected

.. container:: parameters2

   spw : any

.. container:: methodparmtable

   Spectral Window Ids (0 relative) to select; -1 interpreted as all

.. container:: parameters2

   outfile : undefined

.. container:: methodparmtable

   The name of output MeasurementSet

.. container:: methodsection

   Example

.. container:: methodexam

   sdms.open('m100_sd.ms') sdms.set_selection(field='M100')
   sdms.apply_baseline_table('m100_sd.bltable')

.. container:: param

   function **fit_line**

   .. container:: collcontent

      .. container:: methoddesc

         Fit line profile to selected spectra and obtain the best-fit
         parameter values

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         datacolumn : undefined = data

      .. container:: methodparmtable

         The name of data column to process ('data', 'float_data', or
         'corrected')

Allowed Value(s)

data float_data corrected

.. container:: parameters2

   spw : any

.. container:: methodparmtable

   Spectral Window Ids (0 relative) to select; -1 interpreted as all

.. container:: parameters2

   pol : any

.. container:: methodparmtable

   Select data by polarization(s)

.. container:: parameters2

   timebin : undefined

.. container:: methodparmtable

   Bin width for time averaging

.. container:: parameters2

   timespan : undefined

.. container:: methodparmtable

   Span the timebin across 'scan', 'state', 'field', or a combination of
   them (e.g., 'scan,state')

.. container:: parameters2

   polaverage : undefined

.. container:: methodparmtable

   polarization averaging mode ('', 'stokes', or 'geometric')

Allowed Value(s)

stokes geometric

.. container:: parameters2

   fitfunc : undefined = gaussian

.. container:: methodparmtable

   Function of line profile

Allowed Value(s)

gaussian lorentzian

.. container:: parameters2

   nfit : undefined = 0

.. container:: methodparmtable

   Comma-separated numbers of gaussian/lorentzian lines to fit in
   maskline region. ignored when linefinding=true.

.. container:: parameters2

   linefinding : undefined = false

.. container:: methodparmtable

   do line finding

.. container:: parameters2

   threshold : undefined = 5.0

.. container:: methodparmtable

   S/N threshold for line finder

.. container:: parameters2

   avg_limit : undefined = 4

.. container:: methodparmtable

   channel averaging for broad lines in line finding

.. container:: parameters2

   minwidth : undefined = 4

.. container:: methodparmtable

   the minimum channel width to detect as a line by line finder

.. container:: parameters2

   edge : undefined = 00

.. container:: methodparmtable

   channels to drop at beginning and end of spectrum in line finding

.. container:: parameters2

   tempfile : undefined

.. container:: methodparmtable

   The name of temporary file to keep fitting results

.. container:: parameters2

   tempoutfile : undefined

.. container:: methodparmtable

   The name of temporary ms file

.. container:: methodsection

   Example

.. container:: methodexam

   sdms.open('m100_sd.ms') sdms.set_selection(field='M100')
   sdms.fit_line(fitfunc='gauss',spw='0:1000~2000;4000~5000',nfit=[1,1])

.. container:: param

   function **set_selection**

   .. container:: collcontent

      .. container:: methoddesc

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         spw : any

      .. container:: methodparmtable

         Spectral Window Ids (0 relative) to select; -1 interpreted as
         all

.. container:: parameters2

   field : any

.. container:: methodparmtable

   Field Ids (0 relative) or Field names (msselection syntax and
   wilcards are used) to select

.. container:: parameters2

   antenna : any

.. container:: methodparmtable

   Antenna Ids (0 relative) or Antenna names (msselection syntax and
   wilcards are used) to select

.. container:: parameters2

   timerange : any

.. container:: methodparmtable

   Limit data selected to be within a given time range. Syntax is
   defined in the msselection link

.. container:: parameters2

   scan : any

.. container:: methodparmtable

   Limit data selected on scan numbers. Syntax is defined in the
   msselection link

.. container:: parameters2

   observation : any

.. container:: methodparmtable

   Select data by observation ID(s). Syntax is the same as for scan
   numbers.

.. container:: parameters2

   polarization : any

.. container:: methodparmtable

   Select data by polarization(s)

.. container:: parameters2

   beam : any

.. container:: methodparmtable

   Beam Ids (0 relative) to select; CURRENTLY NOT AVAILABLE!!!

.. container:: parameters2

   intent : any

.. container:: methodparmtable

   Select data by intent(s)

.. container:: parameters2

   taql : undefined

.. container:: methodparmtable

   For the TAQL experts, flexible data selection using the TAQL syntax

.. container:: parameters2

   reindex : undefined = true

.. container:: methodparmtable

   Re-index indices in subtables based on data selection

.. container:: methodsection

   Example

.. container:: methodexam

   sdms.set_selection(field='M100', spw='3,5')

.. container:: param

   function **smooth**

   .. container:: collcontent

      .. container:: methoddesc

         NOTE: currently only Gaussian kernel is supported.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         type : undefined = gaussian

      .. container:: methodparmtable

         Smoothing kernel type

Allowed Value(s)

gaussian

.. container:: parameters2

   width : undefined = 0.0

.. container:: methodparmtable

   Smoothing kernel width

.. container:: parameters2

   datacolumn : undefined = data

.. container:: methodparmtable

   The name of data column to process ('data', 'float_data', or
   'corrected')

Allowed Value(s)

data float_data corrected

.. container:: parameters2

   outfile : undefined

.. container:: methodparmtable

   The name of output MeasurementSet

.. container:: methodsection

   Example

.. container:: methodexam

.. container:: param

   function **importasap**

   .. container:: collcontent

      .. container:: methoddesc

         Import ASAP Scantable data to MeasurementSet.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         infile : undefined

      .. container:: methodparmtable

         The name of input ASAP Scantable

.. container:: parameters2

   outfile : undefined

.. container:: methodparmtable

   The name of output MeasurementSet

.. container:: parameters2

   parallel : undefined = false

.. container:: methodparmtable

   Turn on parallel execution

.. container:: methodsection

   Example

.. container:: methodexam

.. container:: param

   function **importnro**

   .. container:: collcontent

      .. container:: methoddesc

         Import NOSTAR data to MeasurementSet.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         infile : undefined

      .. container:: methodparmtable

         The name of input NOSTAR data

.. container:: parameters2

   outfile : undefined

.. container:: methodparmtable

   The name of output MeasurementSet

.. container:: parameters2

   parallel : undefined = false

.. container:: methodparmtable

   Turn on parallel execution

.. container:: methodsection

   Example

.. container:: methodexam

.. container:: section
   :name: viewlet-below-content-body
