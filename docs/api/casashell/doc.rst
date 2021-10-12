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
      However, given the complexity of many tasks, with lengthy descriptions, images, table, 
      and large numbers of parameters and subparameters (not a standard Python feature), the 
      web-based casadocs API documentation provides more functionality.
      
      The doc command will open the OS default browser and direct it to the casadocs page for
      the given task name.
      
      When the topic is a tool with API documentation the doc command will direct the browser
      to the casadocs page for the given tool name. Not all CASA tools have API documentation.
      
      Using "start" for the topic will direct the browser to the top of the CASA documentation.
      
      An empty argument, "toc", or an unrecognized topic directs the browser to the casatasks 
      API page.
      
      The version argument can be used to direct doc to use something other than the 
      documentation for the version of CASA being used. Version strings typically look like 
      "v6.4.1" with the numbers corresponding to the first 3 elements of the ctsys.version() value.
      A value of "latest" will be used to find the documentation of the most recent version of 
      casadocs and "stable" will be used to find the document of the most recent release. The "latest"
      version is typically the version under development. 
      
      If the documentation for the current version can not be found, doc will try and use the
      latest CASA documentation. If the documentation for a specific verison is requested and can
      not be found, doc will not use the "latest" version and the user will be directed to the 
      top of the casa site. A warning message is printed when doc can not use the
      documentation for the requested release.
      If the documentation for the current release can not be found, doc will try and use the
      latest CASA documentation. A warning message is printed when doc can not use the
      documentation for the current release.
      
