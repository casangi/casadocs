.. container::
   :name: viewlet-above-content-title

clearstat
=========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   clear all autolock locks

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Clears all autolocking file locks.

      Some tasks (e.g., **browsetable**) need to obtain table locks in
      order to run. Table locks are meant to prevent other tasks from
      running simultaneously on the same table. If a table lock is not
      cleared automatically, the **clearstat** task can be used to clear
      it.

      Using **clearstat** may be required if attempting to run another
      task fails and that task indicates that it cannot obtain a lock on
      a file or table.

       

.. container:: section
   :name: viewlet-below-content-body

.. toctree::
   :hidden:
   :maxdepth: 3

   task_clearstat/about
   task_clearstat/examples
