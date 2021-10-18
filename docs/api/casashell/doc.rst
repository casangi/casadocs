doc
========

.. currentmodule:: casashell


.. function:: doc(topic, version)

   Open a web browser pointing to the location of the given named task or tool API documentation

   Parameters
      - **topic** (*string*) - name of task or tool or "start" or "toc"
      - **version** (*string*) - a casadocs version string, defaults to the casa version being used


   Description
      Each task has built in inline help that can be seen with the standard Python help command. 
      However, given the complexity of many tasks, with lengthy descriptions, images, tables, 
      and large numbers of parameters and subparameters (not a standard Python feature), the 
      web-based casadocs API documentation provides more functionality.
      
      The doc command will open the OS default browser and direct it to the casadocs page for
      the given task name.
      
      When the topic is a tool with API documentation the doc command will direct the browser
      to the casadocs page for the given tool name. Not all CASA tools have API documentation.
      
      Using "start" for the topic will direct the browser to the top of the CASA documentation.
      
      An empty argument, "toc", or an unrecognized topic directs the browser to the casatasks 
      API page.
            
      If the documentation for the current version can not be found, doc will try and use the
      CASA documentation for the "latest" version. If no documentation can be found doc will direct
      the browser to the CASA home page. **Note**: "latest" is the most recent version of the
      documentation and typically corresponds to the version under development (not yet released).
      
      A warning message is printed when doc can not use the documentation for the current release.
      
      The **version** argument can be used to direct doc to use something other than the 
      documentation for the version of CASA being used. Version strings typically look like 
      "v6.4.1" with the numbers corresponding to the first 3 elements of the ctsys.version() value.
      A value of "latest" is used to find the documentation of the most recent version of 
      casadocs and "stable" is used to find the documentation of the most recent release. 
      
      If the documentation for a specific verison is requested and can not be found, the browser will 
      be directed to the top of the CASA site. 
      
      A warning message is printed when doc can not use the documentation for the requested release.
      
      
