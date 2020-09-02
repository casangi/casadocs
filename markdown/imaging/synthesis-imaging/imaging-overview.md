

# Introduction 

Introduction to Synthesis Imaging: Measurement Equation, Iterative $\chi^2$ minimization, Major and Minor cycles, Algorithm Options, etc.

This section describes the framework used by CASA for interferometric image reconstruction

# Concept :

Image reconstruction in radio interferometry is the process of solving the linear system of equations $\vec{V} = [A] \vec{I}$, where $\vec{V}$ represents visibilities calibrated for direction independent effects, $\vec{I}$ is a list of parameters that model the sky brightness distribution (for example, a image of pixels) and $[A]$ is the measurement operator that encodes the process of how visibilities are generated when a telescope observes a sky brightness $\vec{I}$.  $[A]$ is generally given by $[S_{dd}][F]$ where $[F]$ represents a 2D Fourier transform, and $[S_{dd}]$ represents a 2D spatial frequency sampling function that can include direction-dependent instrumental effects. For a practical interferometer with a finite number of array elements, $[A]$ is non-invertible because of unsampled regions of the $uv$ plane. Therefore, this system of equations must be solved iteratively, applying constraints via various choices of image parameterizations and instrumental models.

 

# Implementation ( major and minor cycles ):

Image reconstruction in CASA comprises an outer loop of *major cycles* and an inner loop of *minor cycles*. The major cycle implements transforms between the data and image spaces and the minor cycle operates purely in the image domain. Together, they implement an iterative weighted $\chi^2$ minimization process that solves the measurement equation.

 

![26ad14d4f63ff633dbd5d9e92d40a5059ab46a67](media/26ad14d4f63ff633dbd5d9e92d40a5059ab46a67.png){.image-inline width="635" height="347"}

>Iterative Image Reconstruction - Major and Minor Cycles
  

 

The data to image transform is called the *imaging* step in which a pseudo inverse of $[S_{dd}][F]$ is computed and applied to the visibilities. Operationally, weighted visibilities are convolutionally resampled onto a grid of spatial-frequency cells, inverse Fourier transformed, and normalized. This step is equivalent to calculating the normal equations as part of a least squares solution. The image to data transform is called the *prediction* step and it evaluates the measurement equation to convert a model of the sky brightness into a list of model visibilities that are later subtracted from the data to form residual visibilities. For both transforms, direction dependent instrumental effects can be accounted for via carefully constructed convolution functions.

Iterations begin with an initial guess for the image model.  Each major cycle consists of the prediction of model visibilities, the calculation of residual visibilities and the construction of a residual image. This residual image contains the effect of incomplete sampling of the spatial-frequency plane but is otherwise normalized to the correct sky flux units. In its simplest form, it can be written as a convolution of the true sky image with a point spread function. The job of the minor cycle is to iteratively build up a model of the true sky by separating it from the point spread function. This step is also called *deconvolution* and is equivalent to the process of solving the normal equations as part of a least squares solution. Different reconstruction algorithms can operate as minor cycle iterations, allowing for flexibility in (for example) how the sky brightness is parameterized. The imaging step can be approximate in that several direction dependent effects, especially baseline, frequency or time-dependent ones can sometimes  ignored, minor cycles can be approximate in that they use only PSF patches and do not try to be accurate over the entire image, but the prediction step of the major cycle must be as accurate as possible such that model components are converted to visibilities by including all possible instrumental effects.

<div class="alert alert-info">
**Basic Sequence of Imaging Logic:**

Data : Calibrated visibilities, data weights, UV sampling function
Input : Algorithm and iteration controls (stopping threshold, loop gain,...)
Output : Model Image, Restored Image, Residual Image,...

Initialize the model image
Compute the point spread function
Compute the initial residual image
While ( not reached global stopping criterion )             /* Major Cycle */
{
    While ( not reached minor-cycle stopping criterion )    /* Minor Cycle */
    {
        Find the parameters of a new flux component
        Update the model and residual images
    }
    Use current model image to predict model visibilities
    Calculate residual visibilities (data - model)
    Compute a new residual image from residual visibilities
}
Convolve the final model image with the fitted beam and add to the residual image
</div>


# Algorithmic Options :

Within the CASA implementation, numerous choices are provided to enable the user to fine-tune the details of their image reconstruction. Images can be constructed as spectral cubes with multiple frequency channels or single-plane wideband continuum images. One or more sub images may be defined to cover a wide field of view without incurring the computational expense of very large images. The iterative framework described above is based on the Cotton-Schwab Clean algorithm [\[3\]](#Bibliography), but variants like Hogbom Clean [\[1\]](#Bibliography) and Clark Clean [\[2\]](#Bibliography) are available as subsets of this framework. The major cycle allows controls over different data weighting schemes [\[10\]](#Bibliography) and convolution functions that account for wide-field direction-dependent effects during imaging and prediction \[[\[6\]](#Bibliography), [\[7\]](#Bibliography) , [\[8\]](#Bibliography)\]. Deconvolution options include the use of point source vs multi-scale image models [\[4\]](#Bibliography) , narrow-band or wide-band models [\[5\]](#Bibliography), controls on iteration step size and stopping criteria, and external constraints such as interactive and non-interactive image masks. Mosaics may be made with data from multiple pointings, either with each pointing imaged and deconvolved separately before being combined in a final step, or via a joint imaging and deconvolution [\[9\]](#Bibliography). Options to combine single dish and interferometer data during imaging also exist. More details about these algorithms can be obtained from \[[\[10\]](#Bibliography), [\[11\]](#Bibliography), [\[12\]](#Bibliography), [\[13\]](#Bibliography)\] 

 

 

# References :

 

# Bibliography

1. J.\ A.\ Hogbom\ 1974\ (
2. B.\ G.\ Clark\ 1980\ (
3. F.\ R.\ Schwab,\ 1984\ (
4. T.\ J.\ Cornwell,\ 2008\ (
5. U.Rau,\ 2011\ (
6. T.\ J.\ Cornwell,\ 2008\ (
7. S.\ Bhatnagar,\ 2008\ (
8. S.Bhatnagar,\ 2013\ (
9. T.\ J.\ Cornwell,\ 1988\ (
^\ ^10.\ Briggs\ D.S.\ 1999\ ([Astron.\ Soc.\ Pac.\ Conf.\ Ser.](http://www.aspbooks.org/publications/180/127.pdf))\ [↩](#ref-cit10 "Jump back to citation 10 in the text.")^\ ^11.\ Cornwell,\ T.J\ 1999\ ([Astron.\ Soc.\ Pac.\ Conf.\ Ser.](http://www.aspbooks.org/publications/180/151.pdf))\ [↩](#ref-cit11 "Jump back to citation 11 in the text.")^\ ^12.\ Cornwell,\ T.J.,\ \"The\ Generic\ Interferometer:\ II\ Image\ Solvers\'\',\ Aips++\ note\ 184.\ Aug\ 1995\ [↩](#ref-cit12 "Jump back to citation 12 in the text.")^\ ^13.\ U.Rau,\ 2009\ ([IEEE](http://ieeexplore.ieee.org/document/5109712/))\ [↩](#ref-cit13 "Jump back to citation 13 in the text.")^

