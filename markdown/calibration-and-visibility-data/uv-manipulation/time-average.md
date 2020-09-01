

# Time average 

Time averaging highlights using mstransform and split

**mstransform** and **split** are both able to perform a weighted time average of data.  In **mstransform** time averaging is accessed by setting *timeaverage = True* and controlled by the resulting sub-parameters of *timeaverage.* Additionally, **mstransform** is able to perform a baseline dependent time average as described in the paper Effects of Baseline Dependent Time Averaging of UV Data by W.D. Cotton [\[1\]](#Bibliography) .

```
# mstransform time average parameters

timeaverage         = True # Average data in time.
     timebin        = '0s' # Bin width for time averaging.
     timespan       = ''   # Span the timebin across scan, state or both.
     maxuvwdistance = 0.0  # Maximum separation of start-to-end baselines that can be included in an average(meters)
```

In **split** time averaging is available via top level parameters *timebin* and *combine*.  The functionality is very similar to that in the old version of split.  However, there are some differences as explained below.

```
 # split time average parameters

timebin   = '0s'   # Bin width for time averaging
combine   = ''     # Span the timebin across scan, state or both
```

<div class="alert alert-warning">
**Warning:** the timebin parameter works based on wall clock time, not integration time.  For example, if each scan is 5 seconds long, and scans are separated by 15 seconds, then timebin=\'25s\' is the minimum value needed to combine data from 2 consecutive scans. One might assume that timebin=\'10s\' should work to combine two 5 second scans, but it does not. This is mostly relevant to single dish data, and when using the tasks like sdtimeaverage or mstransform.
</div>

-   Whereas the old version of split used exclusively the *WEIGHT* column to perform the weighted average, **mstransform** and **split** use both *FLAG* and spectral weights (when present). To be specific *WEIGHT_SPECTRUM* is used when averaring *CORRECTED_DATA*, and *SIGMA_SPECTRUM* is used when averaging the *DATA* column.

-   Also **mstransform** and **split** are able to transform the input *WEIGHT/SIGMA_SPECTRUM* according to the rules of error propagation that apply to a weighted average, which result in an output weight equals to the sum of the input weights. For a detailed reference see, Data Reduction and Error Analysis by Bevington & Robinson [\[2\]](#Bibliography).

-   When **mstransform** and **split** process an ALMA MS and *timebin* is greater than 30s, timespan is automatically set to state, to overcome a limitation of the ALMA ASDM binary dumps.

-   As of version 4.5, **mstransform** and **split** both allow timespan field in addition to scan and state.

-   *maxuvdistance*: In the case of **mstransform**, when *maxuvdistance* is greater than 0 this parameter controls the maximum uv distance allowed when averaging data from the same baseline. It works in conjunction with the *timebin* parameter in the sense that the averaging process is finalized when either *timebin* is completed or *maxuvdistance* is reached. The details of the baseline dependent averaging algorithm are available here:

    <ftp://ftp.cv.nrao.edu/NRAO-staff/bcotton/Obit/BLAverage.pdf>

# Bibliography

1. Effects\ of\ Baseline\ Dependent\ Time\ Averaging\ of\ UV\ Data\ by\ W.D.\ Cotton\ (OBIT\ No.\ 13,\ 2008).\ 
2. Data\ Reduction\ and\ Error\ Analysis\ by\ Bevington\ &\ Robinson\ (3rd\ Ed.,\ McGraw\ Hill,\ 2003)\ 
^

