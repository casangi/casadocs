#
# stub function definition file for docstring parsing
#

def clearstat():
    r"""
Clear all autolock locks

Parameters


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

    """
    pass
