

# Iteration Control 

Iteration controls and diagnostics

# Major and Minor Cycles

The CASA Imager implements its iterative optimization in two nested loops, Major and Minor cycles, as described in the [Overview](https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/imaging-overview). 

 

# Iteration Controls

## loop gain

For each component selected in the CLEAN minor cycle, the response of only a fraction of the flux is subtracted out at each step. This is controlled by a loop gain $\gamma$ which is multiplied with the amplitude of the latest flux component before the residual image is updated. This fraction represents a step size used in steepest descent algorithms to counter the effect of imperfect update directions. For a point source, the residual left on the dirty image is $(1-\gamma)^{N_{CL}}$.

Loop gain is typically set at a default of 0.1. As a general rule of thumb, if the sky model being fitted to the data is a good match for the structure being imaged, a higher loop gain is tolerated. MS-Clean with appropriate scale sizes is one example. On the other hand, point source CLEAN applied to extended emission will require a very small loop gain to make adequate progress. 

 

## Stopping Criteria

True convergence is not very easy to define or identify in practice. This is largely because of the logarithmic convergence typical of chi-square minimization or the presence of artifacts that may prevent true convergence but which would still allow imaging at a quality adequate for subsequent analysis. Imaging algorithms therefore have stopping criteria to decide when to pause a set of minor cycle iterations and to perform a major cycle as well as when to stop iterations altogether.

### Reasons for stopping

#### Threshold

The standard stopping criterion is a threshold on the peak brightness in the residual image. When artifacts do not dominate the residuals, such a threshold is a robust way of terminating a run. A global stopping threshold is usually related to the theoretically expected rms (typically $5\sigma$). A stopping threshold to trigger a major cycle is usually related to the height of the strongest sidelobe of the strongest source. The rationale behind this choice is to expect errors in the subtraction of the contributions of flux components during the minor cycle (due to approximations such as the beam patch size) and to prevent spurious new components from being added to the model.

#### Niter

A simple stopping criterion is the total number of iterations (individual minor cycle steps). In the presence of artifacts, it is used if one wants to explicitly stop imaging early to prevent divergence or to truncate iterations once they reach the point of diminishing returns. It is usually used as an over-ride for the more natural stopping criteria of thresholding.

#### Non-Convergence

When the data do not exactly conform to what the algorithm is solving for, true convergence and theoretical noise estimates will not be reached. Some symptoms of non convergence include the residual image saturating in rms value or peak residual with no significant changes across minor and major cycle iterations. Of course, increases in absolute model flux that persist could signal divergence.

 

### Implementation of stopping criteria in **tclean**

User Parameters :   *niter*, *cycleniter*, *threshold, nsigma*

Internally calculated controls : *cyclethreshold*

#### Minor Cycle Stopping Criteria

After a major cycle is complete, and before the minor cycle iterations begin, a *cycleniter* and *cyclethreshold* are computed and used as controls to terminate the minor cycle iterations and trigger the next major cycle. A major cycle is triggered (or minor cycle iterations are skipped) when any one of the following criteria are satisfied.

\(0\) The mask for the current plane is all False.

\(1\) Iteration limit :  *cycleniter* = min ( niter - iterdone ,  *cycleniter* )

*cyclethreshold* is internally computed and used as a major cycle trigger. It is related what fraction of the PSF can be reliably used during minor cycle updates of the residual image. By default the minor cycle iterations terminate once the peak residual reaches the first sidelobe level of the brightest source.

\(2\) Threshold :  *cyclethreshold* is computed as follows using the settings in parameters *cyclefactor*, *minpsffraction*, *maxpsffraction*, *threshold, nsigma* :

psf_fraction = max_psf_sidelobe_level \* *cyclefactor*psf_fraction = max(psf_fraction, *minpsffraction*);psf_fraction = min(psf_fraction, *maxpsffraction*);*cyclethreshold* = peak_residual \* psf_fraction         \# The peak residual is computed within the current mask.*cyclethreshold* = max( *cyclethreshold*, *threshold* )

Further, if *nsigma* (a multiplicative factor of *rms* noise) is specified (\>0.0), the n-sigma based threshold is calculated for each image plane.  The threshold per image plane is calculated using the median absolute deviation (MAD) as follows:

nsigma_threshold = *nsigma* \* robustRMS   (where robustRMS = 1.4826 \* MAD)

and then, the *cyclethreshold* calculated above is further evaulated as

*cyclethreshold* = max(*cyclethreshold*, nsigma_threshold)

\(3\) Zero iterations performed in the minor cycle.

\(4\) Divergence :  If the peak residual increases from the previous peak residual by more than 10%.

(currentPeak - prevPeak)/(prevPeak) \> 0.1

In all situations, the reason for stopping is printed in the logger, per image plane (e.g. per channel).

 

#### Global Stopping Criteria

After each major cycle, peak residuals (with and without masks) are evaluated and compared with the following criteria to decide if any more minor cycle iterations are needed or not. Any one of the following conditions will trigger termination of the imaging run.

(1)Total number of iterations \>= *niter* 

Currently iterations are counted across all image planes, including channels. In the future it will be modified to apply to one plane at a time.

\(2\) peak residual within the mask \< *threshold  * ( or the peak reasidual value differs within one part in 100 to the threshold value)**

\(3\) The mask is blank for all planes (either due to user edits or automasking)

\(4\) No change in the peak residual from the previous major cycle. This would imply that the minor cycle in between did nothing.

\(5\) peak residual within the mask \< max(nsigma thresholds across image planes)  (or the peak reasidual value differs within one part in 100 to the maximum nsigma threshold value)**

\(6\) Divergence 1 : A large relative increase of peak residual across a single major cycle. This catches sudden strong divergence.

   ( PeakRes - PrevPeakRes ) / PrevPeakRes \> 3.0    (where peak residual is computed over the entire image, ignoring the clean mask)

\(7\) Divergence 2 : A relative increase of 3 times in the peak residual from the minimum recorded so far.  This catches slow divergence.

   ( PeakRes - MinPeakRes ) / MinPeakRes \> 3.0   (where peak residual is computed over the entire image, ignoring the clean mask)

 

In all situations, the reason for stopping is printed in the logger.

When nsigma threshold is activated (nsgima\>0.0), since nsigma threshold values varies across image planes, the global exit condition that satifies in that case, can be combination of (5) and any other valid exit criteria.

(In addition to the above, a warning message is printed in the logger if the  peak residual within the clean mask increases by a factor of 2, but no actions are taken.) 

 

# Runtime editing of Iteration Controls

When **tclean** is run with *interactive=True*, a viewer GUI opens to allow the drawing and display of masks on residual images, and also displays and allows the modification of the following iteration control parameters : *iterations left*, *cycleniter*, *cyclethreshold*, *threshold*.

Of these parameters*, iterations left,* and *cyclethreshold* are internally updated after each major cycle and then displayed in case the user wishes to edit them.

-   The field *iterations left* is auto-calculated as niter-iterdone.  If this field is hand-edited, it is taken as \'*niter*\' and the next updated value is this new niter-iterdone. 
-   The *cyclethreshold* field is auto-updated based on the peak residual at the end of the latest major cycle. If *cyclethreshold* is hand-edited, the user-set value applies to only the current set of minor cycle iterations and the auto-calculation resumes from the next major cycle. 

<div class="alert alert-info">
**Note:** Interactive **tclean** only works when a region or mask is selected in the CASA Viewer. If the entire image should be cleaned, please draw a box around the entire image. There is a known bug that when a region is first selected, and then de-selected to produce an empty mask (filled with zeros), the CASA Viewer that runs interactive tclean will still allow you to proceed, and tclean will detect an empty mask and stop. Please always mark a region/mask to continue interactive tclean, and do not forget to double-click inside the green contours to select the region.
</div>

<div class="alert alert-info">
**Note** : In casa5, the auto-calculated cyclethreshold is always displayed as 0, but hand-edited values are still honored.   In the end, the logger contains all the information about what got used, and it has been tested that iteration control and imaging proceeds as expected.
</div>

<div class="alert alert-info">
**Note**: In casa6, the auto-calculated cyclethreshold is correctly displayed in the GUI. However, hand-edited cyclethresholds do not change in the GUI until two major cycles later. However, here too, the logger contains the most accurate information about what was used, and the expected behaviour (of hand-edited cyclethresholds applying to only the current minor cycles) is seen and has been tested. Therefore, iteration control and imaging will proceed as expected.
</div>

<div class="alert alert-info">
**Note** : Threshold information via the GUI must contain units.  '0.5Jy' will work but '0.5' on its own will not.
</div>

 

# Returned Dictionary

When the **tclean** task is run as a python command, it can produce a return value (by setting *interactive=1/0* instead of True/False).  This dictionary contains a summary of the run with information such as number of iterations done, number of major cycles, peak residual at each major cycle boundary and at which iteration count this occured, metadata to index this information for multiple image fields, channels, and stokes planes, a stopcode to indicate the reason for termination of the run (global termination criterion). This dictionary can be used for scripting.

 

