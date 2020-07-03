.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Example Using CASA
==================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Tutorial of CASA on AWS

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Overview of Using CASA on AWS
         :name: overview-of-using-casa-on-aws

      Amazon Web Services (AWS) allows researchers to use instances for
      NRAO data processing. This section presents readying an Instance
      to process a data set with CASA. The CASA tutorial will be used as
      a demonstration of running CASA on AWS.

      .. rubric:: Choose an Instance
         :name: choose-an-instance

      The tutorial does not require an instance with a lot of CPU and
      RAM. Per the `hardware requirements
      page <https://casa.nrao.edu/casadocs-devel/stable/usingcasa/hardware-requirements>`__
      section on memory: 500MB per core is adequate. An m4.xlarge is
      more than adequat and costs $0.24/hour. It has 2 cores and 16 GB
      RAM. A smaller instance such as m4.large would probably work as
      well, except it has 1 core and could not run things in parallel.

      .. rubric:: Get Ready to Start an Instance
         :name: get-ready-to-start-an-instance

      Follow the directions on the `AMI
      page <https://casa.nrao.edu/casadocs-devel/stable/usingcasa/casa-on-amazon-web-services/amazon-machine-images>`__
      to locate an NRAO AMI. Select the AMI, and from the Actions menu,
      choose Launch. Select the m4.xlarge image type, which, as
      mentioned above, should be adequate for the tutorial at 2 cores
      and 8 GB/core. After that, we often press the "Review and Launch"
      button to skip to the end of the process. However, we need to add
      some storage first.

      .. rubric:: Start an Instance with Some Extra Storage Space
         :name: start-an-instance-with-some-extra-storage-space

      Select "4. Add Storage" at the top. You can see the root volume is
      by default 8 GB. For the tutorial, we might get by with 8 GB, but
      enlarging the root volume will remove any doubt. Change 8 to 1024
      (the upper limit for the root volume). You might notice a checkbox
      called "Delete on Termination". For root volumes, this is the
      default. Unchecking it causes the root volume to persist after
      shutdown of the instance. The charges for storing a terminated
      instance are minimal compared to the charge for a running one. The
      user (or a coworker with adequate privileges) can mount the EC2
      volme on another instance. After making this selection, click
      Review and Launch. Then click "Launch". You are asked for the ssh
      key pair that will allow ssh access to the instance you are about
      to start. If possible, use an existing key pair. Click Launch to
      start the instance.

      .. rubric:: Logging into Your Instance
         :name: logging-into-your-instance

      Once the instance has had a couple of minutes to start, you can
      see in the instances screen the running (and recently terminated)
      instances. Your instance is identifiable by the Key Name and the
      fact that under Status Checks it says "Initializing." Copy the
      external IP address and login to the instance: ssh -i
      ~/.ssh/mykeyname.pem centos@my-IP-address.  If your login is not
      immediate, try again in a minute or so.

      Using an NRAO AMI to start an instance brings up an instance with
      CASA already installed. Everything you need to run CASA should be
      there except for the data, which will be downloaded directly to
      the instance in the next step.

      .. rubric:: Downloading the Data
         :name: downloading-the-data

      In this example we'll be using the `VLA high frequency Spectral
      line
      tutorial <https://casaguides.nrao.edu/index.php?title=VLA_high_frequency_Spectral_Line_tutorial_-_IRC%2B10216>`__.

      You can bring up that page in a browser on your host computer,
      there's no need to launch a browser on the AWS instance.

      Section 2 "Obtaining the Data" of the tutorial lists the URL where
      the data can be found and is repeated below.  Once you've logged
      into your instance you can retreive and unpack the data with the
      commands below.  If you've attached a seperate storage device to
      the instance you should cd to where it was mounted to ensure the
      data is written to that device.  See the `storage
      section <https://casa.nrao.edu/casadocs-devel/stable/usingcasa/casa-on-amazon-web-services/storage>`__
      for more details.

      .. container:: terminal-box

         wget
         http://casa.nrao.edu/Data/EVLA/IRC10216/day2_TDEM0003_10s_norx.tar.gz

         .. container::

            .. container::

               tar xf day2_TDEM0003_10s_norx.tar.gz

      .. rubric:: Launching and Running CASA
         :name: launching-and-running-casa

      Typing 'casa' in the terminal will start the pre-installed version
      of casa. The first time it is run, it will take a few minutes to
      initialize. An Ipython interpreter for CASA will eventually open,
      ready for commands to CASA. (The CASA log window should display as
      well.)

      .. rubric:: Display the antenna map
         :name: display-the-antenna-map

      .. container:: casa-input-box

         | #In CASA
         | plotants(vis='day2_TDEM0003_10s_norx',figfile='ant_locations.png')

      .. rubric:: Plot the MeasurementSet, amplitude vs. uv-distance
         :name: plot-the-measurementset-amplitude-vs.-uv-distance

      .. container:: casa-input-box

         plotms(vis='day2_TDEM0003_10s_norx',field='3',
         xaxis='uvdist',yaxis='amp',correlation='RR,LL',
         avgchannel='64',spw='0~1:4~60', coloraxis='spw')

      .. rubric:: Flag data
         :name: flag-data

      .. container:: casa-input-box

         flagdata(vis='day2_TDEM0003_10s_norx', mode='list',
         inpfile=["field='2,3' antenna='ea12'
         timerange='03:41:00~04:10:00'", "field='2,3'
         antenna='ea07,ea08' timerange='03:21:40~04:10:00' spw='1'"])

      .. rubric:: Transfer data
         :name: transfer-data

      When you are done with your instance and want to move the data on
      its root volume to your local storage, you can use scp -r or rsync
      -a .

.. container:: section
   :name: viewlet-below-content-body
