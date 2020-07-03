.. container::
   :name: viewlet-above-content-title

Developer
=========

.. container::
   :name: viewlet-below-content-title

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   --CASA Developer--

   .. container::
      :name: parent-fieldname-text

      Plotms is a GUI plotter based on Qt and Qwt for making X-Y plots
      of measurement sets and calibration tables.  It can be started as
      a task (**plotms**) or tool (**pm**) within CASA, or as a
      standalone app (**casaplotms**) from the shell prompt.  All
      available options should be accessible from both the task/tool
      arguments and GUI text boxes, check boxes, etc.

      .. rubric:: C++ layers
         :name: c-layers

      The main C++ code body for plotms is in **code/plotms**.  This
      directory contains several subdirectories:

      -  **app** - standalone casaplotms executable, which launches the
         PlotMSApp controller.
      -  **PlotMS** - highest level code for the main controller, DBus
         interface, constants and enums.  Classes are also defined to
         save plotms parameters for averaging, calibration, export,
         flagging, iteration, plotting, selection, and transformations.
      -  **Client** - factory and classes for GUI and scripted clients
      -  **Threads** - includes BackgroundThreads and ThreadControllers
         for caching the data, drawing the plots, and exporting the plot
         files. Plotms uses threads for speed and as a means to return
         control to the user.  
      -  **Data** - classes to load the cache for measurement sets
         (using VIVB2) and calibration tables (using CTIter), as well as
         utility classes to estimate the required memory, average the
         data (soon to be moved to the VIVB2 layered architecture), and
         index the cached data for flagging and locating data.
      -  **Plots** - classes to organize one or more plots and pages, as
         well as the display parameters for plotting.
      -  **Gui, GuiTabs, Actions** - handles the GUI layout (tabs,
         buttons, etc.) and interactions with the user (signals and
         slots).

      The plotms GUI is built on base classes specifically for using Qt
      in CASA (**code/casaqt**) and for a generic plotter
      (**code/graphics/GenericPlotter**) in case a different package is
      chosen to be used instead of Qt.  **Gotcha:** some Qt
      functionality is unaccessible since the types are abstracted to
      the base classes in GenericPlotter.  For basic non-comprehensive
      UML diagrams, see
      `PlotmsDocs. <https://safe.nrao.edu/wiki/bin/view/Main/PlotMSDocs>`__

      .. rubric:: Python layer
         :name: python-layer

      Within CASA, **plotms** is set up like other tasks.  Briefly, the
      parameters and allowed values are defined in
      **gcwrap/tasks/plotms.xml**, and the starting point to process the
      parameters and launch the casaplotms process (with or without the
      GUI) is **gcwrap/python/scripts/task_plotms.py. ** It is important
      to keep the GUI and the task arguments in sync, so that all
      functionality is available in either case.  Unfortunately, the
      result is a very long list of plotms parameters.

      The python code has a SWIG interface to the C++ **pm** tool
      methods defined in **gcwrap/tools/plotms/plotms_cmpt.cc**.  This
      component handles setting the arguments in the plotms code
      described above via DBus XML calls (see
      **code/plotms/PlotMS/PlotMSDBusApp.cc**), then starts the plotting
      with a call to update().

      Once update() is called, control returns to the casa session and
      the log contains the message "End Task: plotms".  However, the
      cache thread and then the draw thread continue to make the plot,
      so additional plotms output appears in the log even after the task
      supposedly ended.

      .. rubric:: Plotms tests
         :name: plotms-tests

      Python regression tests for all of the plotms parameters and some
      bug fixes are in **gcwrap/python/scripts/tests/test_plotms.py**. 
      There are test classes within this suite for:  basic plots,
      averaging, axes options, calibration, calibration tables, display
      options, grid options, iteration, selection, transformations, and
      combinations of these ("multi").  The entire suite takes over 10
      minutes to run, so it is useful to run a single test or subset of
      tests (for example, "runUnitTest.py
      test_plotms['test_averaging']").

      Google tests, with suffix **\_GT**, have been added in
      **code/plotms/test/**.  These tests generally load the cache and
      check the values.  Some legacy C++ tests are also in this
      directory, with prefix **d**.  They can be compiled and run
      manually as "demo" tests and can be useful for creating the google
      tests.

      .. rubric:: Debugging
         :name: debugging

      Whether you run a plotms command in a casa session or run
      *casaplotms *\ from the command line, a casaplotms process is
      started and continues to run until you exit the casa session (for
      plotms) or the plotms GUI (for casaplotms).  This makes debugging
      with gdb/ddd very easy, as you can run plotms (with arguments
      which work or even no arguments, in order to start the process),
      attach the PID in the debugger, then set breakpoints and run
      plotms with the failing arguments.

      In the unlikely event of a segmentation fault producing a core
      file, use *gdb casaplotms core.XXXX* and look at the backtrace. 
      When debugging a tarball, the executable is (for example)
      *casa-prerelease-5.0.0-112.el6/lib/casa/bin/casaplotms,* not the
      path returned by 'which casaplotms', *bin/casaplotms,* which is a
      perl script.

      **Gotcha:** When new third-party libraries are used in a CASA
      release (e.g. devtoolset-4 in release 5.0), including the
      compiler, the system gdb may be incompatible with your build.  The
      result is a gdb seg fault when running gdb on a core file or
      setting a breakpoint in gdb with an attached casaplotms process. 
      In this case, use the gdb executable in the third-party libraries
      (e.g. devtoolset-4/root/usr/bin/gdb), which was compiled with the
      same compiler.

.. container:: section
   :name: viewlet-below-content-body
