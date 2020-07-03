.. container::
   :name: viewlet-above-content-title

Control & Configuration
=======================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Starting CASA with MPI and requirements for running CASA in parallel.
   The mpi4casa framework.

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Requirements
         :name: sec516
         :class: subsection

       CASA can be run in parallel on a cluster of computer nodes or on
      a single multi-core computer. In the multi-node case, the
      following requirements are necessary for all nodes to be included
      in the cluster. Users with access to a cluster will not need to do
      these settings, but it is still useful to be aware of the
      configuration:

      -  Password-less ssh access from the client (user) machine into
         all the nodes to be included in the cluster.

         .. container:: info-box

            NOTE: This is not necessary when using only localhost, i.e.
            if the cluster is deployed only on the machine where CASA is
            running.

      -  All the input files must be located in a shared file-system,
         accessible from all the nodes comprising the cluster, and
         mounted in the same path of the file-system.
      -  Mirrored CASA installation with regards to the CASA
         installation in the client (user) machine, so that the
         following environmental variables are pointing to valid
         installations: PATH, LD_LIBRARY_PATH, IPYTHONDIR, CASAPATH,
         CASAARCH, PYTHONHOME, \__CASAPY_PYTHONDIR, PGPLOT_DEV,
         PGPLOT_DIR, PGPLOT_FONT. This is usually achieved by having the
         CASA installation on a shared file-system.

       

      .. rubric:: Configuration and Start-Up
         :name: sec517
         :class: subsection

       The main library used in CASA (4.4+) to achieve parallelization
      is the Message Passing Interface (MPI) and in particular
      the\ `OpenMPI <http://www.open-mpi.de/>`__\ implementation. MPI is
      already included in the CASA distribution so that users do not
      need to install it. The CASA distribution comes with a wrapper of
      the MPI executor, which is called mpicasa. This wrapper does
      several settings behind the scenes in order to properly configure
      the environment to run CASA in parallel.

      The collection of CASA processes which will run the jobs from
      parallelized tasks, is set up via mpicasa. The simplest example is
      to run CASA in parallel on the localhostusing the available cores
      in the machine. A typical example would be to run CASA on a
      desktop with 16 cores such as the following example:

      .. container:: terminal-box

         path_to_casa/mpicasa -n 16 path_to_casa/casa <casa_options>

      Where:

      1. mpicasa: Wrapper around mpirun, which can be found in the casa
         installation directory. Example:
         /home/user/casa-release-4.5.0-el6/bin
      2. -n : MPI option to get the number of processes to run.
      3. 16: The number of cores to be used in the localhost machine.

         .. container:: info-box

            NOTE:MPI uses one process as the MPI Client, which is where
            the user will see messages printed in the terminal or in the
            logger. The other processes are used for the parallel work
            and are called MPI Servers. Because of this, usually we give
            number_of_processes + 1.

      4. casa: Full path to the CASA executable, casa.
      5. casa_options: CASA options such as: -c, –nogui, –log2term, etc.

      .. container:: info-box

         NOTE: when several versions of CASA are available in the PATH,
         there is the risk that the executable mpicasa and other
         executables used by CASA, such as casaplotms or asdm2MS, would
         be picked from one of those different versions instead of the
         "path_to_casa/casa" version that we want to run. This is
         typically the case in data reduction clusters where either the
         default environment or user setup scripts set the PATH to point
         to the latest release of CASA, for example. In such cases, it
         is safer to make sure in advance that the first version found
         in the PATH is the right one, with a command like this (bash),
         as explained in the CASA distribution README:

         *export PATH=path_to_casa/bin:$PATH*

      It is also possible to use other nodes, which can form a
      “cluster”. Following the requirements given above, replace the
      “-n” option of mpicasawith a “\ -hostfile host_file\ ”, as shown
      below:

      .. container:: terminal-box

         mpicasa -hostfile <host_file> path_to_casa/casa <casa_options>

      Where:

      1. host_file: It is a text file containing the name of the nodes
         forming the cluster and the number of cores to use in each one
         of the nodes.

      Example:

      .. container:: center

         .. code:: verbatim

            orion slots=5
            antares slots=4
            sirius slots=4

      The above configuration file will set up a cluster comprised of
      three nodes (orion, antares and sirius), deploying the cores per
      node as follows: At host “orion” up to 5 cores will be deployed
      (including the MPI Client). If the processing requires more cores,
      it will take them from “antares” and once all the 4 engines in
      “antares” are used, it will use up to 4 cores in “sirius”.

       

      To run CASA in interactive mode (without the "-c" option) the user
      needs to first login to the desired computer node with X11
      forwarding. This is achieved with the command    ssh -XY <node>,
      where <node> is the hostname of the computer where he/she wants to
      run CASA.   

      .. container:: terminal-box

         mpicasa -n <number_of_processes> path_to_casa/casa

      This will open an xterm window for the interactive work. To get
      help do:

      .. container:: terminal-box

         mpicasa --help

.. container:: section
   :name: viewlet-below-content-body
