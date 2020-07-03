.. container::
   :name: viewlet-above-content-title

Obtaining and Installing
========================

.. container::
   :name: viewlet-below-content-title

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      A full installation of CASA including custom python environment is
      available as a Linux (.tar) or Mac (.dmg) file from our
      `Downloads <http://casa.nrao.edu/casa_obtaining.shtml>`__ page
      (http://casa.nrao.edu/casa_obtaining.shtml)

      The CASA 6.x series is also available as modular packages, giving
      users the flexibility to build CASA tools and tasks in their own
      Python environment. This includes the casatools, casatasks, and
      casampi modules, allowing for core data processing capabilities in
      parallel.

      The CASA 5 and 6 versions in each release share the same C++
      source code producing equivalent scientific output.  Both versions
      are intended to be nearly identical in functionality and output
      and thus share the same documentation found here. 

      .. container:: info-box

         CASA 5 will be supported alongside CASA 6 for three release
         cycles (6.0/5.6, 6.1/5.7, and 6.2/5.8).  5.8 will be the last
         CASA 5 release

       

      .. rubric:: Full Installation of CASA 5 and 6
         :name: full-installation-of-casa-5-and-6

      **On Linux:** 

      #. Download the .tar file and place it in a work directory (e.g.
         ~/casa)

      #. From a Linux terminal window, expand the file:

         .. container:: terminal-box

            $ tar -xzvf casa-release-xyz.tar.gz

      #. Start CASA

         .. container:: terminal-box

            $ ./casa-release-xyz/bin/casa

      #. The one caveat is that CASA on Linux currently will not run if
         the Security-Enhanced Linux option of the linux operating
         system is set to enforcing. For the non-root install to work,
         SElinux must be set to disabled or permissive (in
         ``/etc/selinux/config``) or you must run (as root):

         .. container:: terminal-box

            setsebool -P allow_execheap=1

          Otherwise, you will encounter errors like:

         .. container:: casa-output-box

            error while loading shared libraries:
            /opt/casa/casa-20.0.5653-001/lib/liblapack.so.3.1.1: cannot
            restore segment prot after reloc: Permission denied

      The non-root installation is thought to work on a wide variety of
      linux platforms. Check the list of operating systems
      `here <https://casa.nrao.edu/../casa_obtaining.shtml>`__ for the
      officially supported OSs. Other platforms may work, too, but we do
      not regularly test those.  An unofficial Knowledge Base article on
      installing CASA on Ubuntu or Debian can be found
      `here <https://casa.nrao.edu/casadocs-devel/stable/memo-series/casa-knowledgebase/installing_casa_ubuntu_debian.pdf>`__.

       

      **On Macintosh:**

      #. Download the .dmg disk image file
      #. Double click on the disk image file (if your browser does not
         automatically open it).
      #. Drag the CASA application to the *Applications* folder of your
         hard disk.
      #. Eject the CASA disk image.
      #. Double click the CASA application to run it for the first time.
         If the OS does not allow you to install apps from non-Apple
         sources, please Change the settings in "System Preferences->
         Security & Privacy -> General" and "Allow applications
         downloaded from: Mac App store and identified developers".
      #. Optional: Create symbolic links to the CASA version and its
         executables (Administrator privileges are required), which will
         allow you to run ``casa``, ``casaviewer``, ``casaplotms``, etc.
         from any terminal command line. To do so, run 

         .. container:: casa-input-box

            !create-symlinks 

       

      .. rubric:: Modular Installation of CASA 6
         :name: modular-installation-of-casa-6

      Pip wheels for casatools and casatasks are available as Python 3
      modules from the public PyPI server
      `casa-pip.nrao.edu <http://casa-pip.nrao.edu>`__. This allows
      simple installation and import in to standard Python 3.6
      environments. The casatools wheel is necessarily a binary wheel so
      there may be some compatibility issues for some time as we work
      toward making wheels available for important Python
      configurations. Initially, we are targeting Python 3.6 as provided
      by RedHat for our wheel production, with RH6 and RH7 as official
      supported platforms. We have had some success on other Linux-based
      platforms as well, but we do not recommend the use of Conda until
      compatibility with Conda is better understood.

      The following prerequisites must be present on the host machine
      before installing CASA:

      #. Python 3.6
      #. libgfortran3 (yum or apt-get install)

      Installation instructions are as follows (from a Linux terminal
      window):

      *NRAO Systems Only: you must run
      "source /opt/local/bin/enable-python36" (no quotes) first*

      .. container:: terminal-box

         $ python3 -m venv casa6

         $ source casa6/bin/activate

         (casa6) $ pip install
         --index-url https://casa-pip.nrao.edu/repository/pypi-casa-release/simple
         casatools

         (casa6) $ pip install --index-url
         https://casa-pip.nrao.edu/repository/pypi-casa-release/simple
         casatasks

      Start CASA and sanity check:

      .. container:: terminal-box

         (casa6) $ python

         | Python 3.6.9 (default, Nov 7 2019, 10:44:02)
         | [GCC 8.3.0] on linux
         | Type "help", "copyright", "credits" or "license" for more
           information.
         | >>> import casatasks
         | >>> help(casatasks)

      To exit the python venv, type deactivate from the terminal. 
      However, the rest of this documentation **assumes the venv is
      active** (to reactivate, type source casa6/bin/activate)

      The use of python3 venv is a simple built-in method of
      containerizing the pip install such that multiple versions of CASA
      6.x can be kept on a single machine in different environments. In
      addition, CASA is built and tested using standard (python 3.6)
      libraries which can be replicated with a fresh venv, keeping the
      libraries needed for CASA isolated from other libraries which may
      already be installed on your machine.

      With the pip installation, CASA may be used in a standard Pythonic
      manner. Examples can be found in `this Jupyter
      Notebook <https://colab.research.google.com/github/casangi/examples/blob/master/casa6/CASA6_demo.ipynb>`__.

      .. container:: alert-box

         **WARNING:** The pip-wheel modules for CASA Viewer and the
         plotms, as well as other GUIs, are unvalidated. They are
         included in the full tar-file distribution, and we recommend to
         use of the tar-file for these GUIs. We also recommend to use
         the tar-file for add-on ALMA tools/tasks, such as wvrgcal.
         Additional testing is being performed to ensure that the
         pip-wheels for the GUIs and add-on ALMA tools/tasks can be
         reliably offered as stand-alone modules in a subsequent CASA 6
         release.

       

      .. rubric:: Parallel Processing Installation
         :name: parallel-processing-installation

      The casampi package provides the
      task-level `MPI <https://en.wikipedia.org/wiki/Message_Passing_Interface>`__ parallelization
      infrastructure of CASA.  The casatasks module detects when casampi
      is available and enables the parallel processing capabilities of
      CASA. Advanced users may also access the casampi package directly
      to build new or custom parallelization schemes.

      The full installation of CASA includes the MPI package and no
      further action is necessary. 

      For the modular installation of individual packages in to a
      standard python environment, ensure that openmpi is installed on
      the host machine (RHEL: yum install openmpi-devel, Ubuntu: apt-get
      install libopenmpi-dev), then perform the following commands(from
      the venv in a Linux terminal after the previous installation of
      casatools and casatasks):

      NRAO systems only: contact the helpdesk to install casa-toolset-3,
      then run the command following command: export
      PATH=/opt/casa/03/bin:$PATH

      .. container:: terminal-box

         (casa6) $ pip install wheel

         (casa6) $ pip install --index-url
         https://casa-pip.nrao.edu/repository/pypi-casa-release/simple
         casampi

      Sanity check (from Linux terminal):

      .. container:: terminal-box

         (casa6) $ echo "from casampi.MPIEnvironment import
         MPIEnvironment; print('working?',
         MPIEnvironment.is_mpi_enabled)" > test.py

         (casa6) $ mpirun -q -n 2 python test.py

      observe two instances of "working? True"

       

      .. rubric:: Jupyter Notebooks and Google Colab
         :name: jupyter-notebooks-and-google-colab

      .. container::

         .. container::

            .. container::

               Jupyter notebooks are ideally suited for code tutorials,
               exploration, and collaborative development. Together with
               Google Colaboratory, which hosts Jupyter notebooks on
               free virtual hardware in the cloud, the door is opened to
               powerful new ways of developing and sharing software.
               CASA 6 casatools and casatasks modules are compatible
               with the Google Colab environment.  The CASA team is
               working towards making additional modules compatible in
               the future as well as introducing new Jupyter-based
               CASAguide tutorials.

               An example of a Jupyter notebook that explains
               installation and usage of CASA 6 is available
               `here <https://colab.research.google.com/github/casangi/examples/blob/master/casa6/CASA6_demo.ipynb>`__.

       

      .. rubric:: CASA Tool Names
         :name: casa-tool-names

      From the CASA 6 command line, the tools can be listed with
      '*toolhelp( )'*  and the tasks can be listed with '*taskhelp( )*'.
      In CASA 5, the tools had a certain name when imported from the
      **casac** module, and another name when used from the CASA 5
      command line. In addition, one instance of each tool was
      pre-constructed and available for the user at the command line.
      The table below lists the tool naming in CASA 5 and CASA 6. In
      CASA 6, all of the CASA 5 names (e.g. imtool, im, etc.) are
      available for the user at the CASA 5 command line, but otherwise,
      the CASA 6/casac names are used by default. It is easy to import
      the CASA 6 tool with whatever name you like with:

      >>> from casatools import imager as imtool

      .. container:: table-wrap

      .. container:: table-wrap

         ============= ================= ===============
         CASA 6/casac  CASA 5/Class/Ctor CASA 5 instance
         imager        imtool            im
         calibrater    cbtool            cb
         ms            mstool            ms
         quanta        qatool            qa
         table         tbtool            tb
         agentflagger  aftool            af
         measures      metool            me
         image         iatool            ia
         imagepol      potool            po
         simulator     smtool            sm
         componentlist cltool            cl
         coordsys      cstool            cs
         regionmanager rgtool            rg
         spectralline  sltool            sl
         vpmanager     vptool            vp
         msmetadata    msmdtool          msmd
         functional    fntool            fn
         imagemetadata imdtool           imd
         atmosphere    attool            at
         calanalysis   catool            ca
         mstransformer mttool            mt
         singledishms  sdmstool          sdms
         ============= ================= ===============

       

      | 

.. container:: section
   :name: viewlet-below-content-body
