caltabconvert -- Convert old-style caltables into new-style caltables. -- utility task
=======================================

Description
---------------------------------------

This task converts old-style (up to CASA 3.3.0) caltables into
new-style (CASA 3.4.0 and later) caltables. It is provided as a
convenience and is strictly temporary.  The information transferred
should be enough for most calibration purposes.  BPOLY and GSPLINE
versions are not supported. Only simple bugs will be fixed. If there
are other issues, it is suggested that a new-style caltable be created
directly.



Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - caltabold
     - :code:`''`
     - Name of the old-style caltable
   * - vis
     - :code:`''`
     - Name of the visibility file (MS) associated with the old-style caltable.
   * - ptype
     - :code:`'complex'`
     - Type of data in the new-format caltable ("complex" or "float"; default is "complex").
   * - caltabnew
     - :code:`''`
     - Name of the new-style caltable.  If not specified, the suffix ".new" is appended to the name of old-style caltable.


Parameter Explanations
=======================================



caltabold
---------------------------------------

:code:`''`

Name of the old-style caltable.
                     Default: none

                        Example: caltabold='gronk.g0'



vis
---------------------------------------

:code:`''`

Name of the visibility file (MS) associated with the
old-style caltable.
                     Default: none

                        Example: 'blurp.ms'



ptype
---------------------------------------

:code:`'complex'`

Type of data in the new-format caltable.
                     Default: "complex"
                     Options: "complex" or "float"

                     Note: The old-style caltables do not have this
		     information, so it is imperative that users get
		     it correct.  "complex" refers to caltables that
		     have complex gains (e.g., produced by gaincal,
		     bpcal, etc.). "float" refers to caltables that
		     real numbers such as delays (e.g., produced by
		     gencal).



caltabnew
---------------------------------------

:code:`''`

Name of the new-style caltable.  
                     Default: '' (the suffix ".new" is appended to the
		     name of old-style caltable)





