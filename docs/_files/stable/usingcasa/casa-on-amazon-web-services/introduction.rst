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

   An introduction to Amazon Web Services

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      In this chapter you will learn how to create an account within
      AWS, select appropriate resources for a problem, launch those
      resources, perform any desired processing, return or store
      resulting products, and finally to release the reserved resources
      back to Amazon.

      |image1|

      .. rubric:: Amazon Web Services Introduction
         :name: amazon-web-services-introduction

      `Amazon Web Services (AWS) <https://aws.amazon.com/>`__ is a
      collection of physical assets and software tools for using ad hoc
      computing resources (aka Cloud Computing) within Amazon. The
      combination of a wide range of processing hardware, network
      speeds, storage media and tools allows users to create virtual
      computing platforms tailored to specific problem sizes with
      discrete durations.

      In simplest terms, AWS allows users to create workstations or
      medium sized clusters of computers (ranging from 10's to a few
      1000 nodes) that are essentially identical to the kind of physical
      workstation or small cluster they might have at their home
      institution without the overhead of upfront capital expense,
      space, power or cooling. The full range of offerings from Amazon
      goes well beyond that simple conceptual model but many, if not
      most, are not directly applicable to radio astronomy data
      processing.

      The target audience for this document is the astronomer who wishes
      to run their computations more quickly, would like to know if AWS
      can help accomplish that goal, and what possibilities and
      limitations AWS brings.

      .. rubric:: Applicability to NRAO Data Processing
         :name: applicability-to-nrao-data-processing

      NRAO data products, particularly those from the Atacama Large
      Millimeter Array (ALMA) and the Jansky Very Large Array (JVLA),
      are of sufficient volume (100s to 1000s of GBytes) and compute
      complexity to require processing capabilities ranging from high
      end workstations to small clusters of servers. Additionally
      advanced imaging algorithms typically benefit from more system
      memory than is likely available on standard desktops.

      AWS can facilitate the transfer of data among researchers through
      high speed networks or shared storage. Large scale projects which
      can be decomposed along some axis (e.g. by observation, field,
      frequency, etc) can be processed concurrently across 10s, 100s or
      even 1000s of compute instances.

      .. rubric:: Document Outline
         :name: document-outline

      This document set attempts to walk users through the necessary
      steps to `create an account within
      AWS <https://casa.nrao.edu/casadocs-devel/stable/usingcasa/casa-on-amazon-web-services/account-and-user-setup>`__,
      `select appropriate resources for their
      problem <https://casa.nrao.edu/casadocs-devel/stable/usingcasa/casa-on-amazon-web-services/amazon-machine-images>`__,
      `launch those
      resources <https://casa.nrao.edu/casadocs-devel/stable/usingcasa/casa-on-amazon-web-services/amazon-machine-images>`__,
      `perform any desired
      processing <https://casa.nrao.edu/casadocs-devel/stable/usingcasa/casa-on-amazon-web-services/instances>`__,
      `return or store resulting products to the
      user <https://casa.nrao.edu/casadocs-devel/stable/usingcasa/casa-on-amazon-web-services/storage>`__,
      and finally to release the reserved resources back to Amazon. The
      last step is a critical aspect to the financial viability of
      computing within AWS.  Later sections will cover the potential
      financial benefit and possible pitfalls of utilizing AWS
      resources.

      .. rubric:: Requesting Assistance
         :name: requesting-assistance

      Given the unique nature of AWS resources, please direct any
      questions or comments to
      `nrao-aws@nrao.edu <mailto:nrao-aws@nrao.edu?subject=AWS%20Questions/Comments>`__
      rather than to CASA or Helpdesk personnel.

.. container:: section
   :name: viewlet-below-content-body

.. |image1| image:: https://casa.nrao.edu/casadocs-devel/stable/usingcasa/casa-on-amazon-web-services/aws-logo.jpg/@@images/4d287ee3-0f7e-48d1-93a2-c816cb4d067f.jpeg
   :class: image-inline
   :width: 442px
   :height: 168px
