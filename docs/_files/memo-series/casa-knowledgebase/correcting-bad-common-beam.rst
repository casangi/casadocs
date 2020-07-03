.. container::
   :name: viewlet-above-content-title

Correcting bad common beam
==========================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   This script re-calculates the common beam by discarding certain
   channels where the point-spread-function (PSF) or 'beam' deviates
   substantially from those of the other channels.

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      It can happen that an MS contains one or more channels for which
      the point-spread-function (PSF) or ‘beam’ deviates a lot from
      those of the other channels. This can be the result of substantial
      flagging, missing data, or other factors. When making a data cube
      with *restoringbeam='common'*, these "outlier" channels can create
      a common beam that does not reflect the beam for the bulk of the
      channels.

      `This example_robust_common_beam.py
      script <https://casa.nrao.edu/../Data/Scripts/example_robust_common_beam.py>`__
      will correct the common beam by detecting and/or flagging outliers
      channels in the calculation of the common beam. The outlier
      channels are identified as those channels for which the area of
      those beams deviate from the median beam by a user-specified
      factor in computation of the median area beam. The script will do
      the following:

      -  Run tclean with niter=0
      -  Detect/flag outliers in chan beams
      -  Use the remaining beams with ia.commonbeam() to get a new
         commonbeam
      -  Specify this explicitly to tclean in the subsequent niter>0
         run.

      The attach script primarily demonstrates the solution of  iter0 ->
      calc_good_beam -> specify_restoringbeam_in_iter1 along with
      tclean. If the new commonbeam is not larger than all the bad
      beams, then the iter0 tclean run's restoration step will throw
      warnings for all channels that cannot be convolved to the new
      common beam. 

      The functionality provided by this script is not yet implemented
      in the commonbeam method of the image analysis tool
      (*ia.commonbeam*).

      Please note that the script is based on an ALMA test-data that was
      used for characterizing the problem in pipeline processing at the
      NAASC (JIRA ticket PIPE-375). Parameters have to be adjusted for
      each use case, including heuristics to detect outlier channels and
      what to substitute the 'bad' beams with.

.. container:: section
   :name: viewlet-below-content-body
