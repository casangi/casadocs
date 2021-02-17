

.. _Description:

Description
   Clears all autolocking file locks.
   
   Some tasks (e.g., **browsetable**) need to obtain table locks in
   order to run. Table locks are meant to prevent other tasks from
   running simultaneously on the same table. If a table lock is not
   cleared automatically, the **clearstat** task can be used to clear
   it.
   
   Using **clearstat** may be required if attempting to run another
   task fails and that task indicates that it cannot obtain a lock on
   a file or table.
   

.. _Examples:

Examples
   To run **clearstat**, no parameters need to be specified.

   The basic way to run the task is 
   
   ::
   
      go clearstat()
   
   as this will not change the current task being scrutinized.

   Note that 
   
   ::
   
      clearstat()
   
   will change the current task assignment to **clearstat**, which is
   generally not what is desired.
   

.. _Development:

Development
   No additional development details

