.. container::
   :name: viewlet-above-content-title

Advanced: Interface Framework
=============================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   The mpi4casa parallelization framework and advanced CASA parallel
   processing

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      The CASA parallelization framework, mpi4casa was developed as a
      layer on top of MPI using a client-server model. The Client is the
      master process, driving user interaction, and dispatching user
      commands to the servers. Servers are all the other processes,
      running in the background, waiting for commands sent from the
      client side.

      One use-case of mpi4casa is to run CASA in parallel on a Multi-MS,
      as explained in previous chapters. There are other ways to process
      the data in parallel using mpi4casa without the need to create a
      Multi-MS. For instance, advanced users can benefit from the
      mpi4casa implementation to run multiple task commands in different
      cores or nodes.

       

      .. rubric:: **Initialization**
         :name: initialization

      Start CASA in parallel as explained in previous chapters, using
      mpicasa.

      Import MPICommandClient from mpi4casa *module*

      .. container:: casa-input-box

         from mpi4casa.MPICommandClient import MPICommandClient

      Create an instance of MPICommandClient

      .. container:: casa-input-box

         client = MPICommandClient()

      Set logging policy

      .. container:: casa-input-box

         client.set_log_mode('redirect')

      Initialize command handling services

      .. container:: casa-input-box

         client.start_services()

      .. rubric::  
         :name: section

      .. rubric:: Syntax to send a command request
         :name: syntax-to-send-a-command-request

      .. container:: casa-input-box

         ret =
         client.push_command_request(command,block,target_server,parameters)

      *command:* String containing the Python/CASA command to be
      executed. The command parameters can be included within the
      command in itself also as strings.

      *block*: Boolean to control whether command request is executed in
      blocking mode (True) or in non-blocking mode (False). Default is
      False (non-blocking).

      *target_server*: List of integers corresponding to the server IDs
      to handle the command

      target_server=None: The command will be executed by the first
      available server

      target_server=2: The command will be executed by the server n #2
      as soon as it is available

      target_server=[0,1]: The command will be executed by the servers n
      #2 and #3

      *parameters (Optional):* Alternatively the command parameters can
      be specified in a separated dictionary using their native types
      instead of strings.

      ret (Return Variable):

      In non-blocking mode: It will not block and will return an Integer
      (command ID) to retrieve the command response at a later stage.

      In blocking mode: It will block until the list of dictionaries,
      containing the command response is received.

       

      .. rubric:: Syntax to receive a command result
         :name: syntax-to-receive-a-command-result

      .. container:: casa-input-box

         ret =
         client.get_command_response(command_request_id_list,block)

      *command_request_id_list*: List of Ids (integers) corresponding to
      the commands whose result is to be retrieved.

      *block*: Boolean to control whether command request is executed in
      blocking mode (True) or in non-blocking mode (False).

      ret (Return Variable): List of dictionaries, containing the
      response parameters. The dictionary elements are as follows:

      ‘successful’ (Boolean): indicates whether command execution was
      successful or failed

      ‘traceback’ (String): In case of failure contains the traceback of
      the exception thrown

      ‘ret’: Contains the result of the command in case of successful
      execution

      Example 1:

      Run **wvrgcal** in 2 different MeasurementSets (for instance each
      one corresponding to an Execution Block):

      .. container:: casa-input-box

         | # Example of full command including parameters
         | cmd1 =
           “wvrgcal(vis=‘X54.ms',caltable=‘cal-wvr_X54’,spw=[1,3,5,7])”
         | cmdId1 = client.push_command_request(cmd1,block=False)
         | # Example of command with separated parameter list
         | cmd2 = “wvrgcal()”
         | params2={vis=‘X54.ms',caltable=‘cal-wvr_X54’,spw=[1,3,5,7]}
         | cmdId2 =
           client.push_command_request(cmd2,block=False,parameters=params2)
         | # Retrieve results
         | resultList = client.get_command_response([cmdId1,
           cmdId2],block=True)

      **Note:** *target_server* is not specified because these are
      monolithic state-less commands, therefore any server can process
      them.

      | 
      | Example 2:
      | Use the CASA ms tool to get the data from 2 EBs and apply a
        custom median filter:

      .. container:: casa-input-box

         | # Open MSs
         | client.push_command_request(“tb.open(‘x54.ms’)”,target_server=1)
         | client.push_command_request(“tb.open(‘x220.ms’)”,target_server=2)
         | # Apply median filter
         | client.push_command_request(“data=ms.getcell(‘DATA’,1)”,target_server=[1,2])
         | client.push_command_request(“from scipy import
           signal”,target_server=[1,2])
         | client.push_command_request(“filt_data=signal.medfilt(data)”,target_server=[1,2])
         | # Put filter data back in the MSs
         | client.push_command_request(“tb.putcell(‘DATA’,1,filt_data)”,target_server=[1,2])
         | # Close MSs
         | client.push_command_request(“tb.close(),target_server=[1,2],block=True)

      .. container:: info-box

         NOTE: *target_server* is specified as each command depends on
         the state generated by previous ones; *block* will block only
         on the last commands as all the others will be executed using a
         FIFO queue, meaning the commands will be received in the same
         order they were sent.

       

      Link to first version of the CASA framework development
      `document <https://svn.cv.nrao.edu/view/casa/trunk/gcwrap/python/scripts/mpi4casa/CASA-4.3-MPI-Parallel-Processing-Framework-Installation-and-advance-user-guide.pdf>`__

.. container:: section
   :name: viewlet-below-content-body
