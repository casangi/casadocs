oldhanningsmooth -- Hanning smooth frequency channel data to remove Gibbs ringing -- manipulation task
=======================================

Description
---------------------------------------


    T H I S   T A S K   I S    D E P R E C A T E D
    I T   W I L L   B E   R E M O V E D   S O O N

    This function Hanning smoothes the frequency channels with
    a weighted running average. The weights are 0.5 for the central
    channel and 0.25 for each of the two adjacent channels. The first
    and last channels are flagged.
    Inclusion of a flagged value in an average causes that data value
    to be flagged.
    If an 'outputvis' filename is given, the task will copy the input file to the
    output file name first, including all columns that are present in the input MS.
    After that step it will smooth the column(s) as requested in the 'datacolumn' parameter.
    Alternatively, if no 'outputvis' is specified, oldhanningsmooth will work directly on the
    input visibility file.
    If the 'CORRECTED' data column is requested for an MS that does not contain this column,
    it will be filled from the 'DATA' column and then smoothed.

    WARNING: by default, all visibility columns will be smoothed. This will
             modify the DATA column of the output MS in order to make sure that
             later gaincal will work on the smoothed data, e.g. as part of self-cal.

    


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - vis
     - :code:`''`
     - 
   * - datacolumn
     - :code:`'all'`
     - 
   * - outputvis
     - :code:`''`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file (MS)


datacolumn
---------------------------------------

:code:`'all'`

the name of the MS column into which to write the smoothed data


outputvis
---------------------------------------

:code:`''`

name of the output visibility file (MS)




