

# Introduction 

An introduction to simulating observations in CASA

The capability of simulating observations and data sets from VLA, ALMA, and other existing and future observatories is an important use-case for CASA. This not only allows the user to get an idea of the capabilities of these instruments for doing science, but also provides benchmarks for the performance and utility of the software to process "realistic" data sets (with atmospheric and instrumental effects). Simulations can also be used to tune parameters of the data reduction and therefore help to optimize the process. CASA can calculate visibilities (create a MeasurementSet) for any interferometric array, and calculate and apply calibration tables representing some of the most important corrupting effects. 

Tasks available for simulating observations are:

-   **simobserve** --- simulate and create custom synthetic MeasurementSets for an interferometric or total power observation
-   **simanalyze** --- image and analyze simulated data set, including diagnostic images and plots
-   **simalma** --- simulate an ALMA observation including multiple configurations of the 12-m interferometric array, the 7-m ACA, and total power measurements by streamlining the capabilities of both **simobserve** and **simanalyze**

<div class="alert alert-info">
**Inside the Toolkit:** The simulator methods are in the **simulator** tool **sm**. Many of the other CASA tools are helpful when constructing and analyzing simulations. Following general CASA practice, the greatest flexibility and functionality is available in the Toolkit, and the most commonly used procedures are bundled for convenience into the tasks.
</div>

<div class="alert alert-info">
**Utility functions**: The **simutil** python class contains numerous utility methods which can be used to facilitate simulations, especially when using the Toolkit.
</div>

Simulating interferometric observations using the **simobserve** and **simanalyze** tasks proceeds in the following steps:

1\. Make a model image or component list. The model is a representation of the sky brightness distribution that you would like to simulate observing (details on model specification in the **simobserve** documentation).

2\. Use the **simobserve** task to create a MeasurementSet (uv data) that would be measured by a telescope observing the specified input model of sky brightness. **simobserve** can also introduce corruption modeling thermal noise or atmospheric effects. The task can be called multiple times to generate e.g., observations from the same model using different array configurations. **simobserve** can also simulate total power observations, which can be combined with interferometric data in **simanalyze**.

3\. Image (grid, invert, and deconvolve) the simulated observation(s) with the **simanalyze** task. **simanalyze** can also compare the simulated image with your input (convolved with the output clean beam) and then calculate a \"fidelity image\" that indicates how well the simulated output matches the convolved input image.  Alternately, you can create an image yourself with the **tclean** task, and then use **simanalyze** to compare that to the sky model input.

ALMA users, especially those less familiar with CASA, are encouraged to use the **simalma** task, which provides additional information on the multiple **simobserve** and **simanalyze** calls required to simulate an ALMA observation which may consist of 12m interferometric, 7m interferometric, and 12m total power data, and attempts to provide useful feedback on those different observation components, to help the user better understand the observing considerations. 

More simulation examples can be found in the CASA guides <http://casaguides.nrao.edu>, under "Simulating Observations in CASA". It is possible to run the steps independently and optionally, as long as you follow the **simobserve** and **simanalyze** conventions about filenames.

<div class="alert alert-info">
**Tip**: A list of antenna configuration files known to CASA is linked from the simulation CASA guides. On Unix, Linux, and Mac computers, you can usually also find this list yourself by typing, for instance, \"locate alma.cycle4.1.cfg\" and looking at other files in that directory.
</div>

 

