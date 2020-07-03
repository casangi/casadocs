.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Examples
========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   importatca task examples

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Reading a pre-CABB ATCA archive file (RPFITS format)
         :name: reading-a-pre-cabb-atca-archive-file-rpfits-format

      .. container:: casa-input-box

         importatca(['2001-01-02_1*.C999','2001-01-03_0*.C999'],'c999.ms',options='birdie,reweight',edge=10)

      Imports a number of ATCA RPFITS-format data sets into a CASA
      measurement set. We are applying birdie flagging and lag spectrum
      re-weighting (as appropriate for old 33 channel continuum data),
      as well as flagging the 10% edge channels.

       

      .. rubric:: Reading an ATCA/CABB archive file (RPFITS format)
         :name: reading-an-atcacabb-archive-file-rpfits-format

      .. container:: casa-input-box

         importatca(['2012-10-25_0707.C2728'],'c2728.ms',options='noac',spw=2,edge=5)

      Imports a CABB RPFITS file, throwing away the auto-correlations
      and the 5% edge channels and selecting only the second
      simultaneous frequency band.

       

.. container:: section
   :name: viewlet-below-content-body
