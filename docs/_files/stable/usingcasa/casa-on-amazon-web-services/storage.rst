.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Storage
=======

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   AWS provides four basic forms of storage that vary by speed,
   proximity to their associated instance (which impacts
   latency/performance), and price.

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      The sections below describe storage in roughly the order of
      proximity to the instance. To first order each, subsequent type
      decreases in both performance and cost with Glacier being the
      slowest and cheapest. EBS may be the most commonly used.

      .. rubric:: Instance Store
         :name: instance-store

      Instance stores are solid state drives physically attached to the
      hardware the instance is running on that are available only on
      certain instance types. (Use of instance stores is beyond the
      scope of this document, although more information is available at
      this AWS page.) It is indirectly the most expensive form of
      storage since instance types with instance store capacity also
      include extra processor cores and memory. Cost effectiveness is a
      function of whether the extra cores and memory are utilized.
      Instance stores do not use redundant hardware. Instance stores
      cannot preserve their data after their instance stops.

      .. rubric:: Elastic Block Storage (EBS)
         :name: elastic-block-storage-ebs

      EBS is connected to instances via high speed networks and is
      stored on redundant hardware. EBS persists independently after a
      compute instance terminates (although it may be set to terminate
      instead). EBS storage can be allocated during the creation of an
      instance, or it may be created separately and attached to an
      existing instance. It may be detached from one instance and
      re-attached to another, which is potentially useful where the
      processing requirements for one stage of processing (e.g.,
      calibration and flagging) are substantially different from a later
      stage (e.g., imaging).

      .. rubric:: Simple Storage Service (S3)
         :name: simple-storage-service-s3

      S3 storage is an object level store (rather than a block level
      store) designed for medium to long-term storage. Most software
      applications like CASA do not interact directly with S3 storage.
      Instead, one of the AWS Interfaces to S3 is used. Typically, S3 is
      used to temporarily store data before moving it to an EBS or
      Instance store volume for processing. Or it is used as long term
      storage for final products. As of this writing, S3 storage costs
      range from $150 - $360 TByte/year, depending on whether data is
      flagged as infrequent access. Longer term storage utilizes Glacier
      storage.

      .. rubric:: Glacier
         :name: glacier

      Glacier is the lowest cost AWS storage. Data within S3 can be
      flagged for migration to glacier where it is copied to tape. As of
      this writing, Glacier storage costs roughly $86 TByte/year.
      Retrival from Glacier takes ~4 hours.

.. container:: section
   :name: viewlet-below-content-body
