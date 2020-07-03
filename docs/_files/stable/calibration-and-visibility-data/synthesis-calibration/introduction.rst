.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Introduction
============

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Summary of Calibration tasks, and the Outline and Philosophy of
   (synthesis) calibration

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      This chapter explains how to calibrate interferometer data within
      the CASA task system.  Calibration is the process of determining
      the net complex correction factors that must be applied to each
      visibility in order to make them as close as possible to what an
      idealized interferometer would measure, such that when the data is
      imaged an accurate picture of the sky is obtained.  This is not an
      arbitrary process, and there is a philosophy behind the CASA
      calibration methodology.  For the most part, calibration in CASA
      using the tasks is not too different than calibration in other
      packages such as AIPS or Miriad.

      .. rubric:: Calibration tasks
         :name: calibration-tasks

      .. container:: alert-box

         **Alert:** The calibration table format changed in CASA 3.4. 
         CASA 4.2 is the last version that will support the
         **caltabconvert** function that provides conversions from the
         pre-3.4 caltable format to the modern format; it will be
         removed for CASA 4.3.  In general, it is best to recalculate
         calibration using CASA 3.4 or later.

      .. container:: alert-box

         **Alert:** In CASA 4.2 the *gaincurve* and *opacity* parameters
         have been removed from all calibration tasks (as advertised in
         4.1).  These calibration types are supported via the gencal
         task.

      .. container:: alert-box

         **Alert:** As part of continuing development of a more flexible
         and improved interface for specifying calibration for apply, a
         new parameter has been introduced in **applycal** and the
         solving tasks: *docallib*.  This parameter toggles between use
         of the traditional calibration apply parameters ( *gaintable*,
         *gainfield*, *interp*, *spwmap*, and *calwt*), and a new
         *callib* parameter which currently provides access to the
         *experimental* Cal Library mechanism, wherein calibration
         instructions are stored in a file.  The default remains
         *docallib=False* in CASA 4.5, and this reveals the traditional
         apply parameters which continue to work as always, and the
         remainder of this chapter is still written using
         *docallib=False*.  Users interested in the Cal Library
         mechanism's flexibility are encouraged to try it and report any
         problems;
         see `here <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/cal-library-syntax>`__
         for information on how to use it, including how to convert
         traditional applycal to Cal Library format.  Note also that
         **plotms** and **mstransform** now support use of the Cal
         Library to enable on-the-fly calibration when plotting and
         generating new MSs.

      The standard set of calibration solving tasks (to produce
      calibration tables) are:

      -  **bandpass** --- complex bandpass (B) calibration solving,
         including options for channel-binned or polynomial solutions
      -  **gaincal** --- complex gain (G,T) and delay (K) calibration
         solving, including options for time-binned or spline solutions
      -  **polcal** --- polarization calibration including leakage,
         cross-hand phase, and position angle
      -  **blcal** --- *baseline-based* complex gain or bandpass
         calibration

      There are helper tasks to create, manipulate, and explore
      calibration tables:

      -  **applycal** --- Apply calculated calibration solutions
      -  **clearcal** --- Re-initialize the calibration for a visibility
         dataset
      -  **fluxscale** --- Bootstrap the flux density scale from
         standard calibration sources
      -  **listcal** --- List calibration solutions
      -  **plotcal** --- Plot calibration solutions
      -  **plotbandpass** --- Plot bandpass solutions
      -  **setjy** --- Compute model visibilities with the correct flux
         density for a specified source
      -  **smoothcal** --- Smooth calibration solutions derived from one
         or more sources
      -  **calstat** --- Statistics of calibration solutions
      -  **gencal** --- Create a calibration tables from metadata such
         as antenna position offsets, gaincurves and opacities
      -  **wvrgcal** --- Generate a gain table based on Water Vapor
         Radiometer data (for ALMA)
      -  **uvcontsub** --- Carry out uv-plane continuum fitting and
         subtraction

      .. rubric:: The Calibration Process
         :name: the-calibration-process

      A work-flow diagram for CASA calibration of interferometry data is
      shown in the following figure.  This should help you chart your
      course through the complex set of calibration steps.  In the
      following sections, we will detail the steps themselves and
      explain how to run the necessary tasks and tools.

      |image1|

       

      +---------+-----------------------------------------------------------+
      | Type    | Figure 1                                                  |
      +---------+-----------------------------------------------------------+
      | ID      | CASA_cal_flow                                             |
      +---------+-----------------------------------------------------------+
      | Caption | Flow chart of synthesis calibration operations. Not shown |
      |         | are use of table manipulation and plotting tasks:         |
      |         | **plotcal** and **smoothcal**                             |
      +---------+-----------------------------------------------------------+

       

      The process can be broken down into a number of discrete phases:

      -  **Calibrator Model Visibility Specification** --- set model
         visibilities for calibrators, either unit point source
         visibilities for calibrators with unknown flux density or
         structure (generally, sources used for calibrators are
         approximately point-like), or visibilities derived from *a
         priori* images and/or known or standard flux density values. 
         Use the **setjy** task for calibrator flux densities and
         models.
      -  **Prior Calibration** --- set up previously known calibration
         quantities that need to be pre-applied, such antenna
         gain-elevation curves, atmospheric models, delays, and antenna
         position offsets.  Use the **gencal** task for antenna position
         offsets, gaincurves, antenna efficiencies, opacity, and other
         prior calibrations
      -  **Bandpass Calibration** --- solve for the relative gain of the
         system over the frequency channels in the dataset (if needed),
         having pre-applied the prior calibration. Use the **bandpass**
         task
      -  **Gain Calibration** --- solve for the gain variations of the
         system as a function of time, having pre-applied the bandpass
         (if needed) and prior calibration. Use the **gaincal** task
      -  **Polarization Calibration** --- solve for polarization leakage
         terms and linear polarization position angle. Use the
         **polcal** task.
      -  **Establish Flux Density Scale** --- if only some of the
         calibrators have known flux densities, then rescale gain
         solutions and derive flux densities of secondary calibrators. 
         Use the **fluxscale** task
      -  **Smooth** --- if necessary smooth calibration using the
         **smoothcal** task.
      -  **Examine Calibration** --- at any point, you can (and should)
         use **plotcal** and/or **listcal** to look at the calibration
         tables that you have created
      -  **Apply Calibration to the Data** --- Corrected data is formed
         using the **applycal** task, and can be undone using
         **clearcal**
      -  **Post-Calibration Activities** --- this includes the
         determination and subtraction of continuum signal from line
         data (**uvcontsub**), the splitting of data-sets into subsets
         (**split**, **mstransform**), and other operations (such as
         simple model-fitting: **uvmodelfit**).

      The flow chart and the above list are in a suggested order. 
      However, the actual order in which you will carry out these
      operations is somewhat fluid, and will be determined by the
      specific data-reduction use cases you are following.  For example,
      you may need to obtain an initial gain calibration on your
      bandpass calibrator before moving to the bandpass calibration
      stage.  Or perhaps the polarization leakage calibration will be
      known from prior service observations, and can be applied as a
      constituent of prior calibration.

      .. rubric:: Calibration Philosophy
         :name: calibration-philosophy

      Calibration is not an arbitrary process, and there is a
      methodology that has been developed to carry out synthesis
      calibration and an algebra to describe the various corruptions
      that data might be subject to: the Hamaker-Bregman-Sault
      Measurement Equation (ME),
      described `here. <https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals/the-measurement-equation-calibration>`__  
      The user need not worry about the details of this mathematics as
      the CASA software does that for you.  Anyway, it's just matrix
      algebra, and your familiar scalar methods of calibration (such as
      in AIPS) are encompassed in this more general approach.

      There are a number of \``physical'' components to calibration in
      CASA:

      -  **data** --- in the form of the MeasurementSet (MS).  The MS
         includes a number of columns that can hold calibrated data,
         model information, and weights
      -  **calibration tables** --- these are in the form of standard
         CASA tables, and hold the calibration solutions (or
         parameterizations thereof)
      -  **task parameters** --- sometimes the calibration information
         is in the form of CASA task parameters that tell the
         calibration tasks to turn on or off various features, contain
         important values (such as flux densities), or list what should
         be done to the data.

      At its most basic level, Calibration in CASA is the process of
      taking "uncalibrated" **data**, setting up the operation of
      calibration tasks using **task parameters**, solving for new
      **calibration tables**, and then applying the calibration tables
      to form "calibrated" **data**.  Iteration can occur as necessary,
      e.g., to re-solve for an eariler **calibration table** using a
      better set of prior calibration, often with the aid of other
      non-calibration steps (e.g. imaging to generate improved source
      models for "self-calibration").

      The calibration tables are the currency that is exchanged between
      the calibration tasks.  The "solver" tasks (**gaincal**,
      **bandpass**, **blcal**, **polcal**) take in the MS (which may
      have a calibration model attached) and previous calibration
      tables, and will output an "incremental" calibration table (it is
      incremental to the previous calibration, if any).  This table can
      then be smoothed using **smoothcal** if desired.

      The final set of calibration tables represents the cumulative
      calibration and is what is applied to correct the data using
      **applycal**. It is important to keep track of each calibration
      table and its role relative to others.  E.g., a provisional gain
      calibration solution will usually be obtained to optimize a
      bandpass calibration solve, but then be discarded in favor of a
      new gain calibration solution that will itself be optimized by use
      of the bandpass solution as a prior; the original gain calibration
      table should be discarded in this case.   On the other hand, it is
      also permitted to generate a sequence of gain calibration tables,
      each *relative* to the last (and any other prior calibration
      used); in this case all relative tables should be carried forward
      through the process and included in the final **applycal**.  It is
      the user's responsibility to keep track of the role of and
      relationships between all calibration tables.  Depending on the
      complexity of the observation, this can be a confusing business,
      and it will help if you adopt a consistent table naming scheme. 
      In general, it is desirable to minimize the number of different
      calibration tables of a specific type, to keep the overall process
      as simple as possible and minimize the computational cost of
      applying them, but relative calibraition tables may sometimes be
      useful as an aid to understanding the origin and properties of the
      calibration effects.  For example, it may be instructive to obtain
      a short time-scale gain calibraiton relative to a long time-scale
      one (e.g., obtained from a single scan) to approximatly separate
      electronic and atmospheric effects.  Of course, calibration tables
      of different types are necessarily relative to each other (in the
      order in which they are solved).

.. container:: section
   :name: viewlet-below-content-body

.. |image1| image:: https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration/casa_calib.png/@@images/96d0de27-1e0a-44e4-9e46-952e0dbdac67.png
   :class: image-inline
