.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

CASA Data Repository
====================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Detailed instructions on CASA data repository use

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   --CASA Developer--

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Using the CASA Data Repository
         :name: using-the-casa-data-repository

      The CASA team switched to using
      `Git LFS <https://www.atlassian.com/git/tutorials/git-lfs>`__ for
      maintaining the CASA Data Repository when source code version
      control switched from Subversion to Git. Git LFS permits managing
      large binary files by storing the actual files outside of Git, but
      checking checksum based stubs into Git as a proxy for the actual
      files. This system does work, but it is **prone to accidental
      checkin of the actual binary data**. For this reason, it is
      **crucial that extra care be exercised when committing to the CASA
      Data Repository**. This is because the only way to correct the
      error of pushing binary files committed directly to Git instead of
      through LFS to the Atlassian bitbucket server is by recreating the
      entire Data Repository from scratch.

      **Please follow the steps in "Check Before Committing" below
      before making commits in your local Data Repository clone.**

      .. rubric:: Git Setup
         :name: git-setup

      While no specific changes are required to your Git setup, there
      are some changes which make the checkout of the data repository
      much more convenient because without these changes the default
      credential caching timeout will cause Git LFS to prompt (often) as
      files are downloaded.

      .. rubric:: OSX
         :name: osx

      For OSX, setting the OSX keychain as the credential source allows
      the LFS checkout to proceed without prompting for passwords. This
      can be done with:

      .. code:: p1

         -bash-4.1$ git config --global credential.helper osxkeychain

      .. rubric:: Linux
         :name: linux

      For Linux, there is no facility for general password management so
      the easiest solution for Linux is to increase the credential
      timeout:

      .. code:: p1

         -bash-4.1$ git config --global credential.helper cache
         -bash-4.1$ git config --global credential.helper 'cache --timeout=3600'

      .. rubric:: Git LFS Setup
         :name: git-lfs-setup

      Git LFS is distributed as an add-on to Git, so before you begin to
      use Git Lfs, ensure that it is actually installed. If you run (and
      see) the following:

      .. code:: p1

         -bash-4.1$ git lfs help
         No manual entry for gitlfs
         -bash-4.1$

      It means that Git LFS is not installed on your system, contact
      your local system administrator. Most CASA Linux developers should
      get Git LFS as part of the installation of 'casa-toolset-2' which
      includes Git LFS.

      .. rubric:: Setup Your Git LFS Environment
         :name: setup-your-git-lfs-environment

      LFS is switched on or off by Git users not by something committed
      to the repository. For this reason, you should add LFS to your Git
      environment on any logins that you will use to commit changes to
      the CASA Data Repository. `It is best to set LFS as a global
      option <https://shuhrat.github.io/programming/git-lfs-tips-and-tricks.html>`__
      so tha you do not need to initialize LFS each time you clone the
      data repository. You can do this by running the following commands
      at the bash command line:

      .. code:: p1

         git config --global filter.lfs.required true
         git config --global filter.lfs.clean "git-lfs clean -- %f"
         git config --global filter.lfs.smudge "git-lfs smudge -- %f"
         git config --global filter.lfs.process "git-lfs filter-process"

      It is also possible to set up Git LFS on a per-repository basis.

      .. rubric:: Checking Out the Data Repository
         :name: checking-out-the-data-repository
         :class: p1

      The Data Repository is very large. The actual data content is
      73GB, but a regular checkout (in Subversion or Git) requires a
      disk footprint of 153GB. Therefore the best way to start using the
      CASA Data Repository is to begin with a limited clone:

      .. code:: p1

         git clone --no-checkout https://<USERNAME>@open-bitbucket.nrao.edu/scm/casa/casa-data.git

      Replace "<USERNAME>" with your username. This will clone the
      actual Git files but will not actually fetch the large data files.
      From this starting point, you could:

      #. checkout the minimal data repository that is distributed with
         each binary distribution of CASA
      #. checkout the entire data repository

      These are described in the next two subsections. An alternative to
      this more typical clone of the Data Repository is to clone only
      the LFS stubs for a look under the hood of LFS. This is described
      in the third subsection.

      .. rubric:: Distro Data Repository
         :name: distro-data-repository

      The distro data repository is the minimal subset of the CASA Data
      Repository which is required for CASA to function properly at
      runtime. It can be retrieved (after doing the "no checkout" clone
      command above) like:

      .. code:: p1

         cd casa-data
         git show HEAD:distro | bash

      The CASA distro Data Repository checked out in this way requires
      around 1.5GB of disk space. The `sparse
      checkout <http://stackoverflow.com/questions/4114887/is-it-possible-to-do-a-sparse-checkout-without-checking-out-the-whole-repository>`__
      of the distro data repository actually modifies the cloned state
      so that only a subset of the entire repository is used. You can
      observe how this is done with:

      .. code:: p1

         -bash-4.2$ git show HEAD:distro | head -16
         ##
         ## this file is intended to be used by piping its contents into bash in a
         ## git clone that has been cloned with --no-checkout, see README.md at:
         ##
         ##   https://open-bitbucket.nrao.edu/projects/CASA/repos/casa-data/browse
         ##

         git config core.sparseCheckout true
         cat > .git/info/sparse-checkout <<'EOF'
         ephemerides/*
         geodetic/*
         gui/*
         demo/Images/*
         demo/calibrater/*
         demo/NGC5921.fits
         demo/3C273XC1.fits
         -bash-4.2$ 

      You can use this information to tailor your personal repository to
      include those portion of the data repository which are pertinent
      to the tests which you care about. For example, to add-on the
      unittest directory:

      .. code:: p1

         git clone --no-checkout https://<USERNAME>@open-bitbucket.nrao.edu/scm/casa/casa-data.git casa-distro
         cd casa-distro
         git show HEAD:distro | bash
         echo 'regression/unittest/*' >> .git/info/sparse-checkout
         git checkout

      .. rubric:: Entire Repository
         :name: entire-repository
         :class: p1

      The entire repository can be checked out (after the limited clone
      above) with:

      .. code:: p1

         git clone --no-checkout https://<USERNAME>@open-bitbucket.nrao.edu/scm/casa/casa-data.git
         cd casa-data
         git checkout master

       This checkout will likely take a long time and consume about
      153GB of disk space.

      .. rubric:: Checkout LFS Internals
         :name: checkout-lfs-internals
         :class: p1

      You may wish to have a look at the LFS internals. Typically you
      won't, but this is the only way to confidently check to see if any
      binary files have crept into our LFS-based binary data repository.
      In either case, a way this can be done is with:

      .. code:: p1

         git -c "filter.lfs.smudge=cat" clone https://open-bitbucket.nrao.edu/scm/casa/casa-data.git

      Also, ignore the error message.

      .. rubric:: Committing Changes
         :name: committing-changes
         :class: p1

      Changes can be committed to either the distro repository,
      sparse clone or a complete repository clone. However, if you are
      using a CASA Data Repository clone that you have previously
      cloned, remember to run "git pull" prior to beginning to make
      changes.

      To do this, just check the new files (or replacement files) into
      place, and then add them as normal from the root of your Git
      clone. For example:

      .. code:: p1

         cd casa-data
         cp demo/3DDAT.fits gui

      However, it is important to check to ensure that the change
      registers as expected as we go through the commit. At this point,
      Git will *see* the new file:

      .. code:: p1

         -bash-4.2$ git status -s
         ?? gui/3DDAT.fits
         -bash-4.2$

      but LFS will not:

      .. code:: p1

         -bash-4.2$ git lfs status --porcelain
         -bash-4.2$

      If you need to add a top level directory, you must first add it to
      the .gitattributes file. To do this, execute the command:

      .. code:: p1

         git lfs track "myfolder/**"

      Verify that the contents match the existing directories and then
      commit the .gitattributes file to the repository. Then proceed
      with adding new files as described below.

      Next add the new file from the root of your data repository clone:

      .. code:: p1

         -bash-4.2$ git add gui/3DDAT.fits
         -bash-4.2$

      At this point, both Git and Git LFS should recogize the new file
      for being committed:

      .. code:: p1

         -bash-4.2$ git status -s
         A  gui/3DDAT.fits
         -bash-4.2$
         -bash-4.2$ git lfs status --porcelain
         A  gui/3DDAT.fits 10137600
         -bash-4.2$

      If you **do not** see your changes reflected in the output from
      "lfs status", do not commit your changes because commit files
      reported by "git status" but not reported by "git lfs status" will
      result in binary data being committed directly to Git (as binary
      files) instead of through Git LFS.

       

      With our changes visible to both Git and Git LFS, it is safe to
      commit them:

      .. code:: p1

         -bash-4.2$ git commit -m 'changes which should not be pushed'
         [master 93cc524] changes which should not be pushed
         1 file changed, 3 insertions(+)
         create mode 100644 gui/3DDAT.fits
         -bash-4.2$ 

      The "changes which should not be pushed" comment simply refers to
      the fact that we've just committed a bogus file to our local
      repository which we do not want to be pushed into the bitbucket
      repository shared by all CASA users. With a normal commit to the
      CASA Data Repository, with files which should be shared, it would
      now be safe to push these files up to the server.

      When *deleting files* from the data repository, the deletions will
      not be listed in the "git lfs status --porcelain" output. This is
      because when deleting files the large binary files not deleted
      because they are required when checking out older revisions of the
      data repository.

      .. rubric:: Check Before Committing
         :name: check-before-committing
         :class: p1

      It is very important to check the status of your data repository
      clone before doing a commit of changed files to your local
      repository. Failure to do this (even should you be on a non-master
      branch), could lead to the need to reconstitute the CASA Data
      Repository on the server from scratch.

      This step is simple. As described in the "Committing Changes"
      section, all you need to do is compare the output of:

      .. code:: p1

         git status -s

      and

      .. code:: p1

         git lfs status --porcelain

      to ensure that each reports knowledge of the files that are about
      to be committed. In our example above, the interaction looked
      like:

      .. code:: p1

         -bash-4.2$ git status -s
         A  gui/3DDAT.fits
         -bash-4.2$
         -bash-4.2$ git lfs status --porcelain
         A  gui/3DDAT.fits 10137600
         -bash-4.2$

      When *deleting files* from the data repository, the deletions will
      not be listed in the "git lfs status --porcelain" output.

      .. rubric:: Check Before Pushing Upstream
         :name: check-before-pushing-upstream
         :class: p1

      Double check that your files are managed by LFS. One way to do
      this is to use LFS ls-files. For example:

      git lfs ls-files \| 
      stakeholders/alma/E2E6.1.00034.S_tclean.ms/SYSPOWER/table.dat

      ``Another, and perhaps more robust verification is to compare the file size in Git to the actual file size on disk.``

      ``In this example the file size on disk is 2283 bytes but the size reported by Git is only 129 bytes. This means that the binary is indeed managed by LFS.``

      ::

         ls -l  stakeholders/alma/E2E6.1.00020.S_tclean.ms/ASDM_RECEIVER/table.dat

         -rw-r--r-- 1 username group 2283 Mar  4 15:09 stakeholders/alma/E2E6.1.00020.S_tclean.ms/ASDM_RECEIVER/table.dat

      ::

         git ls-tree master -rl | grep  stakeholders/alma/E2E6.1.00020.S_tclean.ms/ASDM_RECEIVER/table.dat

         100644 blob c995547dd417f4def10d38d969fe94a6aff9563d     129    stakeholders/alma/E2E6.1.00020.S_tclean.ms/ASDM_RECEIVER/table.dat
          

      .. rubric:: Further Reading
         :name: further-reading
         :class: p1

      -  `Backing Up an LFS
         repository <https://help.github.com/enterprise/2.8/user/articles/duplicating-a-repository/#mirroring-a-repository-that-contains-git-large-file-storage-objects>`__
      -  `Tips and Trick for
         LFS <https://shuhrat.github.io/programming/git-lfs-tips-and-tricks.html>`__
      -  `Atlassian LFS
         Tutorial <https://www.atlassian.com/git/tutorials/git-lfs>`__
      -  `LFS homepage <https://git-lfs.github.com>`__
      -  `Check if a file is managed by
         LFS <https://github.com/git-lfs/git-lfs/issues/2748>`__

      .. rubric:: Updating the Observatories table
         :name: updating-the-observatories-table
         :class: p1

      | On occasion the Observatories table needs to be updated.
      | This can be done using the TableBrowser tool in casa. The tool
        can be launched
      | with "browsetable" command in Casa.
      | The Observatories table is under "geodetic" folder in the
        casa-data repository.
      | In Table Browser:
      | 1) In the "Edit" menu, select the topmost "Edit Table" button.
        This will enable table editing.
      | 2) Click on Edit -> Insert Rows .... select 1 row to be appended
      | 3) A new row will appear at the bottom of the table. Add all of
        the required values.
      | 4) Click on File -> close Table
      | 5) Exit casabrowser
      | 6) Rerun "casabrowser Observatories" or "browsetable" to make
        sure that the values you added got saved properly. Exit Casa.
      | 7) Commit the changes back to the casa-data repository.
      | The table has the following fields.
      | MJD: The Modified Julian Date when the Observatory position was
        measured. If the date of the measurements is not available the
        date of the update request should typically suffice.
      | NAME: Observatory name
      | Type: WGS84 or ITRS
      | Long: Required
      | Lat: Required
      | Height: Required
      | X: Optional. Default 0.
      | Y: Optional. Default 0.
      | Z: Optional. Default 0.
      | Source: The name of the requestor
      | Comment:
      | AntennaResponses:
      | Sometimes both ITRS and WGS84 values are provided but only one
        or the other is used/required. The additional values will be
        used for reference only.
      | Use the process described in the previous segments to push the
        changes to the data repository.

      Notes about conversion from Kumar:

      | There is a conversion tool in CASA (me.measure) but you have to
        do some geometry to get the XYZ for ITRF
      | This is what i did..
      | #Given wgspos
      | wgspos={'m0': {'unit': 'rad', 'value': 0.10311260074377},'m1':
        {'unit': 'rad', 'value': 0.77900832891464},'m2': {'unit': 'm',
        'value': 2560.0},'refer': 'WGS84','type': 'position'}
      | ##convert it to ITRF
      | itpos=me.measure(wgspos, 'ITRF')
      | but sadly casa reports the itrf values as spherical coordinated
        theta, phi, R  or (m0, m1, m2) below and not x,y,z
      | CASA <26>: itpos
      | Out[26]:
      | {'m0': {'unit': 'rad', 'value': 0.10311260074376997},
      |  'm1': {'unit': 'rad', 'value': 0.7756516780842643},
      |  'm2': {'unit': 'm', 'value': 6370186.160484446},
      |  'refer': 'ITRF',
      |  'type': 'position'}
      | Then you get X, Y, Z by using
      | X=cos(theta)*cos(phi)*R
      | Y=sin(theta)*cos(phi)*R
      | Z=sin(phi)*R

       

       

.. container:: section
   :name: viewlet-below-content-body
