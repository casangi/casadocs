.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Monitoring
==========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   A critical aspect to the financial viability of computing within AWS

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Instance Monitoring
         :name: instance-monitoring

      | 
      | After a job finishes on an instance, that instance and storage
        are still running and generating charges to the AWS Account Root
        User. Instances and storage known to not be needed can of course
        be shut down. To check whether an instance is in use or not, a
        quick check can be made using the console: Click Instances,
        check the box next to your instance, and select the "Monitoring"
        tab. CPU Utilization is shown. But to be really sure, login to
        the instance and check if your job is finished. If so, you can
        transfer data off the root volume as needed and terminate the
        instance.

      For more information see:
      http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/US_SingleMetricPerInstance.html#d0e6752

      .. rubric:: Storage Monitoring (EBS)
         :name: storage-monitoring-ebs

      After the instance terminates, the instance ID and data volume
      names will continue to show up for several minutes. This can be
      used to find EBS volumes that were attached to the instance. If
      the user does not want their data to remain on EBS, i.e., to
      transfer their EBS volume to another instance or save it for
      later, then terminating the volume at that time makes sense.
      Although, the user might want to preserve the data by copying it
      to S3 or downloading it to a local storage device and then
      terminate the EBS volume.

      .. rubric:: Storage Monitoring (S3)
         :name: storage-monitoring-s3

      If you have data in S3 you may wish to leave it there. If you wish
      to move it to your local storage device, click the cube in the
      upper left of the console, then choose S3. Unfortunately the
      console is clumsy for transferring data. Reading through the
      `Interfaces <https://casa.nrao.edu/casadocs-devel/stable/usingcasa/casa-on-amazon-web-services/interfaces>`__ section
      of this chapter (and the relevant links), specifically on the use
      of the AWS CLI, is therefore recommended. Once the user is done
      with the previously allocated AWS resources, the user can release
      the reserved resources back to Amazon.

.. container:: section
   :name: viewlet-below-content-body
