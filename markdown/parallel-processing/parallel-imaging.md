

# Parallel Imaging 

Parallel imaging in tclean

The parallelization of imaging is achieved through task **tclean**. The parallelization itself is tied closely to the major-minor cycles of the imager and follows a different approach of that used by other tasks. The parallelization inside **tclean** does not need the MS to be partitionted into a Multi-MS. It will work in the same way if the input is an MS or MMS. But in order to run **tclean** in parallel it is necessary to launch CASA with **mpicasa**, in the same way as for other tasks. One extra step necessary to run **tclean** in parallel is to set the parameter *parallel=True*. All the details of the parallelization are described in the section mentioned above.

<div class="alert alert-info">
Parallel imaging on an MS file (rather than MMS file) in tclean is an official mode of operations in the ALMA pipeline since Cycle-6, and officially endorsed by CASA as per CASA 5.4. We recommend users interested in parallel processing to use this mode of operation. For large data products, the imaging step often dominates the overall runtime, as well as the advantages that can be achieved with parallelization (see [CASA Memo 5](https://casa.nrao.edu/casadocs-devel/stable/memo-series/casa-memos)). Processing Multi-MS files, either for imaging or calibration, remains at the discretion of the user.
</div>

 

 

 

 

 

