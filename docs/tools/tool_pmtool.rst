

.. _Description:

Description
   a plotter and interactive flagger for visibility data
   
   The **plotms** tool pm is the suite of functions underlying the
   **plotms** task. **plotms** is a task for plotting and interacting
   with visibility data. A variety of axes choices (including data
   column) along with MS selection and averaging options are
   provided. Flag extension parameters are also available for
   flagging operations in the plotter. 
   
   The most common use of **plotms** is at the task level (details in
   the Global Task List page), but it is possible to access the
   **pm** tool directly, using *set* functions. See the **Methods**
   tab for available functions and the **Examples** tab for a plot
   using the tool interface.
   

.. _Examples:

Examples
   plotms is most commonly invoked as a task with parameters:
   
   ::
   
      plotms(vis='ngc5921.ms', xaxis='channel', yaxis='amp',
      ydatacolumn='corrected', plotfile='ngc5921.jpg')
   
   To create this plot in the tool interface:
   
   ::
   
          pm.setPlotMSFilename('ngc5921.ms')
          pm.setPlotAxes(xAxis='channel', yAxis='amp',
         yDataColumn='corrected')
   
          pm.save('ngc5921.jpg')
   
    
   
   .. warning:: Each tool function call will launch or update the plotms GUI! 
      Be careful with large datasets!
   

.. _Development:

Development
   --CASA Developer--
   
   The code for the plotms tool is in
   **gcwrap/tools/plotms/plotms_cmpt.cc**.  These methods are invoked
   via SWIG from the python task interface, with commands sent to the
   *casaplotms* process by DBus XML messages.  Most of the plotms
   code can be found in **code/plotms**.  See the Global Task List
   Developer page for the plotms task for more information.
   