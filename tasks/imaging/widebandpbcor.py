#
# stub function definition file for docstring parsing
#

def widebandpbcor(vis, imagename='', nterms=2, threshold='', action='pbcor', reffreq='', pbmin=0.2, field='', spwlist=[''], chanlist=[''], weightlist=['']):
    """
Wideband PB-correction on the output of the MS-MFS algorithm

| WideBand Primary-beam correction. It computes a set of PBs at the specified frequencies, calculates Taylor-coefficient images that represent the PB spectrum, performs a polynomial division to PB-correct the output Taylor-coefficient images from clean(nterms>1), and recompute spectral index (and curvature) using the PB-corrected Taylor-coefficient images

Parameters
----------
vis : string
   Name of measurement set. 
imagename : string
   Name-prefix of multi-termimages to operate on. 
nterms : int
   Number of taylor terms to use
threshold : string
   Intensity above which to re-calculate spectral index 
action : string
   PB-correction (pbcor) or only calc spectral-index (calcalpha)

Other Parameters
----------
reffreq : string
   Reference frequency (if specified in clean)
pbmin : double
   PB threshold below which to not correct
field : string
   Fields to include in the PB calculation
spwlist : intArray
   List of N spw ids
chanlist : intArray
   List of N channel ids
weightlist : doubleArray
   List of N weights (relative)

Notes
-----





   



      The task **widebandpbcor** performs a WideBand Primary-beam
      correction. It computes a set of PBs at the specified frequencies,
      calculates Taylor-coefficient images that represent the PB
      spectrum, performs a polynomial division to PB-correct the output
      Taylor-coefficient images from **clean** or **tclean** (with
      *nterms>1*), and recomputes the spectral index (and curvature)
      using the PB-corrected Taylor-coefficient images. Optionally, it
      is possible to skip the PB-correction and only recalculate the
      spectral index with a different threshold. 

      This is a temporary task, meant for use until a widebandpbcor
      option is enabled from within the tclean task.

      When running widebandpbcor, an output directory named
      'imagename.pbcor.workdirectory' is created, and it is filled
      with an image-cube of the evaluated primary beams at all specified
      frequencies, Taylor-coefficients, and a 'spectral index' due to
      the primary beam. Note that for the actual PB-correction, only the
      Taylor-coefficient images are used.

      For more information about the widebandpbcor task, please see
      the `Wide Band
      Imaging <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/wide-band-imaging>`__ page
      in the Synthesis Imaging section of CASAdocs.  

      .. rubric::  
         :name: section

      .. rubric:: Choosing *spwlist*, *chanlist*, and *weightlist*
         :name: choosing-spwlist-chanlist-and-weightlist

      The basic principles at work here are:

      #. Imaging = fitting a polynomial to a noisy spectrum (with
         weights). The polynomial represents :math:`I_{\nu}` x
         :math:`P_{\nu}`, where :math:`I_{\nu}` is the intensity and
         :math:`P_{\nu}` the primary beam (PB) at frequency :math:`\nu`.
      #. PB model = fitting a polynomial to a collection of PBs at
         different frequencies (with weights). The polynomial represents
         the primary beam :math:`P_{\nu}`.
      #. Dividing the two polynomials via their coefficients.

      Steps (1) and (2) need to be consistent with each other (with
      respect to frequencies used and their weights) to produce FITS
      that when divided give exactly only the sky parameters. Unless you
      use the same math (and code) for both, they won't be exactly
      consistent. The way to minimize differences is to choose a list of
      frequencies (via spws/chans) and weights for widebandpbcor that
      resemble the frequency structure of the data you have used for
      imaging. For example, if you have 3 spws in your data and the
      middle spw has a factor of 10 less weight in the data, then using
      just one channel each from the two outer spws for the PB modeling
      may be close enough to using all 3 spws. Or, you could also
      pick the middle channel of all 3 spws, and assign weights as [1.0,
      0.1, 1.0].

       

      .. rubric:: Parameter descriptions
         :name: parameter-descriptions

      .. rubric:: *vis*
         :name: vis

      Name of input visibility file. Default: none. Examples:
      *vis='ngc5921.ms'.* Only one MS can be specified here, and it must
      contain at-least one timestep of data at all frequencies required
      to calculate the PB spectrum.

      .. note:: **NOTE1**: If the imaging was done using a list of MSs, and any
         one MS covers the entire frequency range, then it will suffice
         to supply only that one MS. This MS is used only to extract
         frequencies at which to compute primary beams before fitting
         Taylor polynomials.

      .. note:: **NOTE2**: In case of multiple MSs that cover different
         frequency ranges, please **split**/**concat** a small fraction
         of the data from each MS to form one single MS that contains
         the full frequency range. This task uses the MS only for
         frequency meta-data.

      .. rubric:: *imagename*
         :name: imagename

      Pre-name of input and output images. Same as in the **clean** or
      **tclean** task. Examples: *imagename = 'run1'*; Restored-images
      (run1.image.tt0, etc.) and residual images (run1.residual.tt0,
      etc... ) must be available on disk.

      .. rubric:: *nterms*
         :name: nterms

      Number of Taylor terms to be used to model the
      frequency-dependence of the primary beam. Examples: *nterms = 2*;
      *nterms* must be less than or equal to the number of frequencies
      specified via spwlist, chanlist and weightlist. *nterms=1* will do
      a standard division by the average PB computed over all specified
      frequencies.

      .. rubric:: *threshold*
         :name: threshold

      Flux level in the restored intensity map, below which to not
      recalculate spectral index. Examples: *threshold = '0.1Jy'*

      .. rubric:: *action*
         :name: action

      Choice of PB-correction with spectral-index recalculation or only
      spectral-index recalculation (using the specified threshold).
      Examples: *action='pbcor'* or *action='calcalpha'*. With
      *action='pbcor'*, the following output images are
      created/overwritten:

      -  imagename.pbcor.workdirectory: This directory contains an image
         cube with PBs at the list of specified frequencies, and
         Taylor-coefficient images that describe the PB spectrum.
      -  imagename.pb.cube: Concatenated cube of PBs
      -  imagename.pb.tt0, tt1, ...: Taylor coefficients describing the
         PB spectrum
      -  imagename.pb.alpha: Spectral index of the PB (for information
         only)
      -  imagename.image.pbcor.tt0,tt1,...: Corrected Taylor
         coefficients
      -  imagename.pbcor.image.alpha: Corrected Spectral Index
      -  imagename.pbcor.image.alpha.error: New error map.

      With *action='calcalpha'*, the following output images are
      created/overwritten

      -  imagename.image.alpha: Corrected Spectral Index
      -  imagename.image.alpha.error: New error map.

      .. rubric:: action='pbcor' expandable parameters
         :name: actionpbcor-expandable-parameters

      .. rubric:: *reffreq*
         :name: reffreq

      Reference frequency about which the Taylor-expansion is defined.
      Examples: reffreq = '1.5GHz'. If left unspecified, it is picked
      from the input restored image. 

      .. note:: **NOTE**: If *reffreq* was specified during task clean to
         produce the images it must be specified here.

      .. rubric:: *pbmin*
         :name: pbmin

      PB gain level below which to not compute Taylor-coefficients or
      apply PB-corrections. Examples: *pbmin = 0.1*

      .. rubric:: *field*
         :name: field

      Field selection for the Primary Beam calculation. Examples: *field
      = '3C291'*. This field selection must be identical to that used in
      **clean** or **tclean**.

      .. rubric:: *spwlist*
         :name: spwlist

      List of SPW ids for which to make separate Primary Beam.

      .. rubric:: *chanlist*
         :name: chanlist

      List of channel ids, within the above SPW ids, at which to make
      PBs. Examples: *spwlist=[0,1,2] chanlist=[32,32,32]*, make PBs at
      frequencies corresponding to channel 32 of spws 0,1 and 2;
      *spwlist=[0,0,0] chanlist=[0,10,20]*, make PBs at frequencies
      corresponding to channels 0, 10, 20 of spw 0.

      Primary beams are computed at these specified frequencies and for
      pointings selected by *field*. Taylor-coefficients that represent
      the PB spectrum are computed from these images.

      .. rubric:: *weightlist*
         :name: weightlist

      List of relative weights to apply to the PBs selected via the
      *spwlist* and *chanlist* parameters. Weights should approximately
      represent the sum-of-weights applicable during imaging each of
      these frequencies. Examples: *weightlist=[0.5,1.0,1.0]*

      The first frequency had less usable data due to flagged RFI, but
      the other two had relatively equal weight. These weights are
      applied to the PB spectrum while computing PB Taylor-coefficients.
      Setting weights to anything other than 1.0 makes a difference only
      with very lop-sided weights.

    """
    pass
