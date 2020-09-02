

# Polarization Calibration 

Solving for instrumental polarization

Instrumental polarization calibration is necessary because the polarizing hardware in the receiving system will, in general, be impure and non-orthogonal at a level of at least a few percent.  These instrumental polarization errors are antenna-based and generally assumed constant with time, but the algebra of their effects is more complicated than the simple \~scalar multiplicative gain calibration.  Also, the net gain calibration renders the data in an arbitrary cross-hand phase frame that must also be calibrated.   The **polcal** task provides support for solving for instrumental polarization (poltype=\'Df\' and similar) and cross-hand phase (\'Xf\').   Here we separately describe the heuristics of solving for instrumental polarization for the circular and linear feed bases.  

# Polarization Calibration in the Circular Basis

Fundamentally, with good ordinary gain and bandpass calibration already in hand, good polarization calibration must deliver both the instrumental polarization and position angle calibration. An unpolarized source can deliver only the first of these, but does not require parallactic angle coverage. A polarized source can only also deliver the position angle calibration if its polarization position angle is known a priori. Sources that are polarized, but with unknown polarization degree and angle, must always be observed with sufficient parallactic angle coverage (which enables solving for the source polarization), where \"sufficient\" is determined by SNR and the details of the solving mode.

These principles are stated assuming the instrumental polarization solution is solved using the \"linear approximation\" where cross-terms in more than a single product of the instrumental or source polarizations are ignored in the [Measurement Equation](https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals/the-measurement-equation-calibration).  A more general non-linearized solution, with sufficient SNR, may enable some relaxation of the requirements indicated here, and modes supporting such an approach are currently under development.

For instrumental polarization calibration, there are 3 types of calibrator choice, listed in the following table:

  Cal Polarization   PA Coverage   Poln Model?   *poltype*     Result
  ------------------ ------------- ------------- ------------- -----------------------
  Zero               any           Q=U=0         *\'Df\'*      D-terms only
  Unknown            2+ scans      ignored       *\'Df+QU\'*   D-terms and Q,U
  Known, non-zero    2+ scans      Set Q,U       *\'Df+X\'*    D-terms and Pos Angle

Note that the parallactic angle ranges spanned by the scans in the modes that require this should be large enough to give good separation between the components of the solution. In practice, 60 degrees is a good target.

Each of these solutions should be followed with a \'Xf\' solution on a source with known polarization position angle (and correct fractional Q+iU in the model).

The **polcal** task will solve for the \'Df\' or \'Xf\' terms using the model visibilities that are in the model attached to the MS. Calibration of the parallel hands must have already been obtained using **gaincal** and **bandpass** in order to align the amplitude and phase over time and frequency. This calibration must be supplied through the *gaintable* parameters, but any caltables to be used in **polcal** must agree (e.g. have been derived from) the data in the DATA column and the FT of the model. Thus, for example, one would not use the caltable produced by **fluxscale** as the rescaled amplitudes would no longer agree with the contents of the model.

Be careful when using resolved calibrators for polarization calibration.  A particular problem is if the structure in Q and U is offset from that in I. Use of a point model, or a resolved model for I but point models for Q and U, can lead to errors in the \'Xf\' calibration. Use of a *uvrange* will help here. The use of a full-Stokes model with the correct polarization is the only way to ensure a correct calibration if these offsets are large.

### A note on channelized polarization calibration

When your data has more than one channel per spectral window, it is important to note that the calibrator polarization estimate currently assumes the source polarization signal is coherent across each spectral window. In this case, it is important to be sure there is no large cross-hand delay still present in your data. Unless the online system has accounted for cross-hand delays (typically intended, but not always achieved), the gain and bandpass calibration will only correct for parallel-hand delay residuals since the two polarizations are referenced independently. Good gain and bandpass calibration will typically leave a single cross-hand delay (and phase) residual from the reference antenna.  Plots of cross-hand phases as a function of frequency for a strongly polarized source (i.e., that dominates the instrumental polarization) will show the cross-hand delay as a phase slope with frequency. This slope will be the same magnitude on all baselines, but with different sign in the two cross-hand correlations. This cross-hand delay can be estimated using the *gaintype=\'KCROSS\'* mode of **gaincal** (in this case, using the strongly polarized source *3C286*):

```
   gaincal(vis='polcal_20080224.cband.all.ms',
           caltable='polcal.xdelcal',
           field='3C286',
           solint='inf',   
           combine='scan',
           refant='VA15',
           smodel=[1.0,0.11,0.0,0.0],       
           gaintype='KCROSS',       
           gaintable=['polcal.gcal','polcal.bcal'])
```

Note that *smodel* is used to specify that *3C286* is polarized; it is not important to specify this polarization stokes parameters correctly in scale, as only the delay will be solved for (not any absolute position angle or amplitude scaling). The resulting solution should be carried forward and applied along with the gain (.gcal) and bandpass (.bcal) solutions in subsequent polarization calibration steps.

### Circular Basis Example

In the following example, we have a MS called *polcal_20080224.cband.all.ms* for which we already have bandpass, gain and cross-hand delay solutions.  An instrumental polarization calibrator with unknown linear polarization has been observed.  We solve for the instrumental polarization and source linear polarization with **polcal** using *poltype=\'Df+QU\'* as follows:

```
polcal(vis= 'polcal_20080224.cband.all.ms',
       caltable='polcal.pcal',
       field='2202+422',       
       solint='inf',   
       combine='scan',
       preavg=300.0,       
       refant='VA15',       
       poltype='Df+QU',       
       gaintable=['polcal.gcal','polcal.bcal','polcal.xdelcal])
```

This run of **polcal** assumes that the model stored in the MS for *2202+422* is the one that was used to obtain the net gain calibration stored in *polcal.gcal* (i.e., we have not substituted a fluxscale result, which would create an inconsistent scale). 

Alternatively, if we have an instrumental polarization calibrator that we know is unpolarized, we run polcal with poltype=\'Df\':

```
polcal(vis='polcal_20080224.cband.all.ms',
       caltable='polcal.pcal',
       field='0319+415',
       refant='VA15',       
       poltype='Df',       
       gaintable=['polcal.gcal','polcal.bcal','polcal.xdelcal])
```

In general, if there is more than one calibrator suitable for instrumental polarization calibration, it is useful to obtain a solution from each of them, and compare results.  The instrumental polarization should not vary with field, of course.  Note that it is not yet possible to effectively use *combine=\'field\'* for instrumental polarization calibration solves with **polcal**, unless the prior models for all fields are set to the correct apparent linear polarization for each.

Having obtained the instrumental polarization calibration, we solve for the cross-hand phase using the flux density calibrator (for which the instrinsic linear polarization is known):

```
polcal(vis='polcal_20080224.cband.all.ms',
       caltable= 'polcal.polx',
       field='0137+331',
       refant='VA15',       
       poltype='Xf',
       smodel=[1.0,-0.0348,-0.0217,0.0],       #the fractional Stokes for 0137+331 (3C48)
       gaintable=['polcal.gcal','polcal.bcal','polcal.xdelcal','polcal.pcal'])
```

Note that the correct fractional polarization has been specified for *0137+331*.  It is not necessary to use the correct absolute total and linearly polarized flux densities here, since the Xf calibration is entirely phase-like.

 

# Polarization Calibration in the Linear Feed Basis

CASA now supports instrumental polarization calibration for the linear feed basis at a level that is practical for the general user. Some details remain to be implemented with full flexibility, and much of what follows will be streamlined in future releases.

Calibrating the instrumental polarization for the linear feed basis is somewhat more complicated than the circular feed basis because the polarization effects (source and instrument) appear in all four correlations at first or zeroth order (whereas for circular feeds, the polarization information only enters the parallel hand correlations at second order). As a result, e.g., the time-dependent gain calibration will be distorted by any non-zero source polarization, and some degree of iteration will be required to isolate the gain calibration if the source polarization is not initially known. These complications can actually be used to advantage in solving for the instrumental calibration; in can be shown, for example, that a significantly linearly polarized calibrator enables a better instrumental polarization solution than an unpolarized calibrator.

In the following example, we show the processing steps for calibrating the instrumental polarization using a strongly (\>5%) polarized point-source calibrator (which is also the time-dependent gain calibrator) that has been observed over a range of parallactic angle (a single scan is not sufficient). We assume that we have calibrated the gain, bandpass, and cross-hand delay as described [elsewhere](https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration/gain-calibration), and that the gain calibration was obtained assuming the calibrator was unpolarized.

###  Linear Basis Example

First, we import some utility functions from the CASA recipes area:

```
from recipes.almapolhelpers import *
```

 

Our MS in this example is called *polcal_linfeed.ms*.  We begin by assuming we already have a bandpass calibration result (obtained by conventional means) stored in *polcal.bcal*.  We first solve for a time-dependent gain solution on the instrumental polarization calibrator, which we expect to be significantly polarized, but for which we do not yet have a polarization model:

```
gaincal(vis='polcal_linfeed.ms',
        caltable='polcal.gcal',  
        field='1',                 #the instrumental polarization calibrator
        solint='int',             
        smodel=[1,0,0,0],          #assume zero polarization
        gaintype='G',       
        gaintable=['polcal.bcal'],
        parang=T)                  #so source poln properly rotated
```

Since the gain calibrator was assumed unpolarized, the time-dependent gain solutions contain information about the source polarization. This can be seen by plotting the amp vs. time for this cal table using *poln=\'/\'.*  The antenna-based polarization amplitude ratios will reveal the sinusoidal (in parallactic angle) function of the source polarization. Run the utility method **qufromgain** to extract the apparent source polarization estimates for each spw:

```
qu=qufromgain('polcal.gcal')
```

The source polarization reported for all spws should be reasonably consistent. This estimate is not as good as can be obtained from the cross-hands (see below) since it relies on the gain amplitude polarization ratio being stable which may not be precisely true.  However, this estimate will be useful in resolving an ambiguity that occurs in the cross-hand estimates.

Next we estimate both the XY-phase offset and source polarization from the cross-hands. The XY-phase offset is a spectral phase-only bandpass relating the X and Y systems of the reference antenna.  If the XY-phase is solved for in a channel-dependent manner (as below), it is strictly not necessary to have solved for the cross-hand delay as described above, but it does not hurt, as it allows reasonably coherent channel averages for data examination (we assume below that we have obtained the cross-hand delay solution at this stage). The source polarization occurs in the cross-hands as a sinusoidal function of parallactic angle that is common to both cross-hands on all baselines (for a point-source). If the XY-phase bandpass is uniformly zero, then the source linear polarization function will occur entirely in the real part of the cross-hand visibilities. Non-zero XY-phase has the effect of rotating the source linear polarization signature partially into the imaginary part, where circular (and instrumental) polarization occur (cf. the circular feed basis where the cross-hand phase merely rotates the position angle of linear polarization). The following **gaincal** solve averages all baselines together and first solves for a channelized XY-phase (the slope of the source polarization function in the complex plane in each channel), then corrects the slope and solves for a channel-averaged source polarization. This calibration is obtained using *gaintype=\'XYf+QU\'* in **gaincal**:

```
gaincal(vis='polcal_linfeed.ms',
        caltable='polcal.xy0amb',  #possibly with 180deg ambiguity
        field='1',                 #the calibrator
        solint='inf',   
        combine='scan',
        preavg=200.0,              #minimal parang change
        smodel=[1,0,1,0],          #non-zero U assumed
        gaintype='XYf+QU',       
        gaintable=['polcal.gcal','polcal.bcal','polcal.xdelcal])  #all prior calibration
```

Note that we imply non-zero Stokes U in *smodel*; this is to enforce the assumption of non-zero source polarization signature in the cross-hands in the ratio of data and model. This solve will report the center-channel XY-phase and apparent Q,U for each spw. The Q,U results should be recognizable in comparison to that reported by **qufromgain** above. However, since the XY-phase has a 180 degree ambiguity (you can rotate the source polarization signature to lie entirely in the visibility real part by rotating clockwise or counter-clockwise), some or all spw Q,U estimates may have the wrong sign. We correct this using the **xyamb** utility method, using the *qu* obtained from *qufromgain* above (which is not ambiguous):

```
S=xyamb(xy='polcal.xy0amb',qu=qu,xyout='polcal.xy0')
```

The python variable *S* now contains the mean source model (Stokes I =1; fractional Q,U; V=0) that can be used in a revision of the gain calibration and instrumental polarization calibration.

Next we revise the gain calibration using the full polarization source model:

```
gaincal(vis='polcal_linfeed.ms',
        caltable='polcal.gcal1',  
        field='1',        
        solint='int',             
        smodel=S,                  #obtained from xyamb
        gaintype='G',       
        gaintable=['polcal.bcal'],
        parang=T)                  #so source poln properly rotated
```

Note that *parang=T* so that the supplied source linear polarization is properly rotated in the parallel-hand visibility model. This new gain solution can be plotted with *poln=\'/\'* as above to show that the source polarization is no longer distorting it. Also, if **qufromgain** is run on this new gain table, the reported source polarization should be statistically indistinguishable from zero.

 Finally, we can now solve for the instrumental polarization:

```
 polcal(vis= 'polcal_linfeed.ms',
        caltable='polcal.dcal',
        field='1',
        solint='inf',
        combine='scan',
        preavg=200,
        poltype='Dflls',      #freq-dep LLS solver
        refant='',            #no reference antenna
        smodel=S,
        gaintable=['polcal.gcal1','polcal.bcal','polcal.xdelcal','polcal.xy0'])
```

Note that no reference antenna is used since this solve will produce an absolute instrumental polarization solution that is registered to the assumed source polarization (*S*) and prior calibrations. Applying a refant (referring all instrumental polarization terms to a reference antennas X feed, which would then be assumed perfect) would, in fact, discard valid information about the imperfections in the reference antennas X feed. (Had we used an unpolarized calibrator, we would not have a valid xy-phase solution, nor would we have had access to the absolute instrumental polarization solution demonstrated here.)

A few points:

-   Since the gain, bandpass, and XY-phase calibrations were obtained prior to the instrumental polarization solution and maybe distorted by it, it is generally desirable to re-solve for them using this instrumental polarization solution as a prior calibration. In effect, this means iterating the sequence of calibration steps using all of the best of the available information at each stage, including the source polarization (and *parang=T*). This is a generalization of traditional self-calibration.
-   If the source linear polarization fraction and position angle is known *a priori*, the processing steps outlined above can be amended to use that source polarization assertion in the gain and instrumental calibration solves from the start. The *qufromgain* method is then not needed (but can be used to verify assumptions), the **gaincal(***\...,gaintype=XYf+QU,\...***)** should not be altered (parallactic angle coverage is still required!), and the **xyamb** run should use the *a priori* polarization for *qu*. If there is likely to be a large systematic offset in the mean feed position angle, iteration of the gain, bandpass, and instrumental polarization terms is required to properly isolate the calibration effects.
-   Note that the above process does not explicitly include a position angle calibration. In effect, the estimated source polarization sets the mean feed position angle as the reference position angle, and this is usually within a degree or so of optimal for linear feeds. If your mean X feed position angle is not 0 degrees, and your MS does not account for the offset in its FEED subtable, be careful in your interpretation of the final position angle. Currently, the circular feed-specific position angle calibration modes of **polcal(**\...,*poltype=\'Xf\',\...***)** will not properly handle the linear feed basis; this will be fixed in a future release.    

