.. container::
   :name: viewlet-above-content-title

Amazon Machine Images
=====================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   An Amazon Machine Image (AMI) provides the information required to
   launch an instance, which is a virtual server in the cloud

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Overview
         :name: overview

      An AMI is an object that encapsulates a base OS image (e.g., Red
      Hat Enterprise Linux, CentOS, Debian), any 3rd party software
      packages (e.g., CASA, SciPy) and any OS level run time
      modifications (e.g., accounts, data, working directories). Since
      an AMI is a discrete object, it can be mapped onto differing
      hardware instances to provide a consistent work environment
      independent of the instance's number of processors, available
      memory, or total storage space.

      The NRAO provides a set of pre-made images based on the standard
      Amazon image, which include specific release versions of CASA and
      Python and AWS's command line interface (CLI) and application
      programming interface (API). The appropriate AMI can be used to
      start an image with operating system and software ready to run
      CASA.

      .. rubric:: Finding an NRAO AMI
         :name: finding-an-nrao-ami

      You can search for NRAO AMIs `using the
      console <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html#finding-an-ami-console>`__.

      -  From the navigation bar in the upper right, change your region
         to be "US West (Oregon)"
      -  Open the AWS Console and click on "EC2 Dashboard".
      -  Click on "AMIs" to bring up the interface for selecting AMIs.
      -  The AMI selection interface by default displays only AMIs
         "Owned by me". Change it to "Public Images".
      -  Narrow this long list to only NRAO images.

         -  Click in the box to the right of the magnifying glass.
         -  A menu listing "Resource Attributes" will pop up below the
            box you clicked on. Ignore it and type "NRAO" in the box and
            press the Enter key.

      -  The list of AMIs has been narrowed to NRAO AMIs only.
      -  New NRAO AMIs will be released periodically.

      .. rubric:: Using an AMI
         :name: using-an-ami

      Click the box next to the AMI you want. Click Launch. The
      `Instances <https://casa.nrao.edu/casadocs-devel/stable/usingcasa/casa-on-amazon-web-services/instances>`__
      section of this document covers starting instances.

      .. rubric:: Geographic Locales
         :name: geographic-locales

      AWS has the concept of `Regions and
      Zones <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html>`__
      in which Instances, EBS volumes, S3 buckets, and other resources
      are run. So an S3 bucket may be in region us-west-2 and not
      directly accessible if another IAM User is currently using
      us-east-1. However, a user may select the region they run in. And
      users may also duplicate some resouces across regions if access
      latency is the concern. To find the latency from your computer to
      all the AWS regions, try the cloudping tool:
      http://www.cloudping.info.

      .. rubric:: AMIs are Region-specific
         :name: amis-are-region-specific

      An AWS AMI User can only use AMIs stored in its region. However,
      `copying an
      AMI <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/CopyingAMIs.html#ami-copy-steps>`__
      to another region is straightforward. The copy gets a new AMI-ID,
      so it effectively becomes a new AMI; the original AMI-ID is
      appended to the new AMI's "Description". The new AMI always starts
      out private and may need to be made public. (It takes about 15
      minutes after making an AMI public for it to show up in a search.)
      In every other way, it is a duplicate of the original.

      To make the image public, select the AMI and from the "Actions"
      menu and pick "Modify Image Permissions". As in this image select
      "Public" and click Save.

.. container:: section
   :name: viewlet-below-content-body
