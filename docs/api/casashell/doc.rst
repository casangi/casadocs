doc
========

.. currentmodule:: casashell


.. function:: doc(taskname)

   Open a web browser pointing to the location of the given taskname API documentation

   Parameters
      - **taskname** (*string*) - name of task

   Description
      Each task has built in inline help that can be seen with the standard Python help command. 
      However, given the complexity of many tasks, with lengthy descriptions, images, table, 
      and large numbers of parameters and subparameters (not a standard Python feature), the 
      web-based casadocs API documentation provides more functionality.
      
      The doc command will open the OS default browser and direct it to the casadocs page for
      the given task name.
      
