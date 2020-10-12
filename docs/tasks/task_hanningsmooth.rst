

.. _Description:

Description
   task description
   
   This is the new implementation of **hanningsmooth**.
   
   .. note:: | \* Task **hanningsmooth2** has been renamed to
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
   
   .. warning:: WARNING: by default, all visibility columns will be smoothed.
   
   .. rubric:: Parameter Descriptions
      
   
   .. rubric:: Input and output MeasurementSets
      
   
   The input visibility file (MS or MMS) given by the
   *vis* parameters will be Hanning smoothed and saved in an output
   given by the *outputvis* parameter.
   
   For example, *vis* = ['ngc5921.ms'] *, output vis* =
   'out_ngc5921.mms'. 
   
   .. rubric:: Output MS or Multi-MS: keepmms parameter
      
   
   If *keepmms* = True, a
   `Multi-MS <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/the-multi-ms>`__
   will be created as the output if the input is a Multi-MS(MMS),
   which is the default behaviour. The output Multi-MS will have the
   same partition axis of the input MMS. See the `Parallel
   Processing <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing>`__
   chapter for more information on the MMS format.
   
   .. rubric:: Data Column parameter
      
   
   The parameter *datacolumn* chooses which column to use for the
   processing (case-insensitive). The default is set to all columns
   that exist in the input MS. 
   
   .. rubric:: Data Selection parameters
      
   
   For more details on how to perform data selection within the MS
   (i.e., selecting by field, SPW, antenna, etc.), see the
   `Visibility Data
   Selection <resolveuid/5e08acd0d7cf4de1ab2a0e2fd34adfc7>`__
   chapter.
   

.. _Examples:

Examples
   

.. _Development:

Development
   task developer
   
   --CASA Developer--
   
   The following information was in the inline help for hanningsmooth
   but is now being maintained in one place in the Visibility Data
   Selection chapter, so a link has been added to those pages. It has
   been deleted from the Description tab for now and included below
   for reference in case it's needed, once a comprehensive plan has
   been established for all task pages with this issue. 
   
    
   
   |     --- Data selection parameters ---
   |     
   |     field -- Select field using field id(s) or field name(s).
   |              [run listobs to obtain the list iof d's or names]
   |         default: ''=all fields If field string is a non-negative
   |            integer, it is assumed to be a field index
   |            otherwise, it is assumed to be a field name
   |            field='0~2'; field ids 0,1,2
   |            field='0,4,5~7'; field ids 0,4,5,6,7
   |            field='3C286,3C295'; fields named 3C286 and 3C295
   |            field = '3,4C*'; field id 3, all names starting with
     4C
   |     spw -- Select spectral window/channels
   |         default: ''=all spectral windows and channels
   |            spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
   |            spw='&lt;2';  spectral windows less than 2 (i.e. 0,1)
   |            spw='0:5~61'; spw 0, channels 5 to 61
   |            spw='0,10,3:3~45'; spw 0,10 all channels, spw 3 -
     chans 3 to 45.
   |            spw='0~2:2~6'; spw 0,1,2 with channels 2 through 6 in
     each.
   |            spw = '*:3~64'  channels 3 through 64 for all sp id's
   |                    spw = ' :3~64' will NOT work.
   |                NOTE: mstransform does not support multiple
     channel ranges per
   |                      spectral window (';').
   |     scan -- Scan number range
   |         default: ''=all
   |     antenna -- Select data based on antenna/baseline
   |         default: '' (all)
   |             Non-negative integers are assumed to be antenna
     indices, and
   |             anything else is taken as an antenna name.
   |         examples:
   |             antenna='5&amp;6': baseline between antenna index 5
     and index 6.
   |             antenna='VA05&amp;VA06': baseline between VLA
     antenna 5 and 6.
   |             antenna='5&amp;6;7&amp;8': baselines 5-6 and 7-8
   |             antenna='5': all baselines with antenna 5
   |             antenna='5,6,10': all baselines including antennas
     5, 6, or 10
   |             antenna='5,6,10&amp;': all baselines with \*only\*
     antennas 5, 6, or
   |                                    10.  (cross-correlations
     only.  Use &amp;&amp;
   |                                    to include autocorrelations,
     and &amp;&amp;&amp;
   |                                    to get only
     autocorrelations.)
   |             antenna='!ea03,ea12,ea17': all baselines except
     those that
   |                                        include EVLA antennas
     ea03, ea12, or
   |                                        ea17.
   |     correlation -- Correlation types or expression.
   |         default: '' (all correlations)
   |         example: correlation='XX,YY'
   |     timerange -- Select data based on time range:
   |         default: '' (all); examples,
   |            timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
   |            Note: if YYYY/MM/DD is missing date, timerange
     defaults to the
   |            first day in the dataset
   |            timerange='09:14:0~09:54:0' picks 40 min on first day
   |            timerange='25:00:00~27:30:00' picks 1 hr to 3 hr
     30min
   |            on next day
   |            timerange='09:44:00' data within one integration of
     time
   |            timerange='&gt;10:24:00' data after this time
   |     array -- (Sub)array number range
   |         default: ''=all
   |     uvrange -- Select data within uvrange (default units meters)
   |         default: ''=all; example:
   |             uvrange='0~1000klambda'; uvrange from 0-1000
     kilo-lambda
   |             uvrange='&gt;4klambda';uvranges greater than 4
     kilo-lambda
   |             uvrange='0~1000km'; uvrange in kilometers
   |     observation -- Select by observation ID(s)
   |         default: ''=all
   |     feed -- Selection based on the feed - NOT IMPLEMENTED YET
   |         default: ''=all
   |     
   |     datacolumn -- Which data column to use for processing
     (case-insensitive).
   |         default: 'all'; whichever of the visibility data columns
     that are present.
   |         options: 'data', 'model', 'corrected',
     'all','float_data', 'lag_data'.
   |     
   |         example1: datacolumn='data'; it will smooth the input
     DATA column and save the
   |                   smoothed data in DATA of the output MS.
   |         example2: datacolumn='corrected'; it will smooth the
     input CORRECTED_DATA column
   |                   and save the smoothed data in DATA of the
     output MS.
   |         example3: datacolumn='all', where the input MS has
     DATA,CORRECTED_DATA,MODEL_DATA.
   |                   It will smooth all three columns and save the
     smoothed data in
   |                   DATA, CORRECTED_DATA and MODEL_DATA of the
     output MS.
   