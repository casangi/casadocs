saveinputs
===========

.. currentmodule:: casashell

.. function:: saveinputs(taskname=None, outfile=None)

   Save current task parameters to file. If given a taskname, sets taskname as the current active (default) task.

   Parameters
      - **taskname** (*obj*, *string*, or *None*) - task object or task name. None will use current active (default) task.
      - **outfile** (*string* or *None*) - output file name, None will use current active (default) taskname.

   Description
      The ``saveinputs`` command will save the current values of a given task parameters to a
      Python (plain ascii) file. It can take up to two arguments, e.g. ::

         saveinputs(taskname, outfile)

      The first is the usual taskname parameter. The second is the name for the output Python file.
      If there is no second argument, for example, ::

         saveinputs('clean')

      a file with name \<taskname\>.last (in this case 'clean.last' will be created or overwritten
      if extant. If invoked with no arguments, e.g. ::

         saveinputs

      it will use the current active taskname (for example as set using ``inp <taskname>`` or
      ``default <taskname>``).
      
      For example, starting from default values ::

         CASA <1>: default('listobs')
         CASA <2>: vis=''
         CASA <3>: saveinputs
         CASA <4>: !more 'listobs.last'
         vis = 'ngc5921.demo.ms'
         selectdata = True
         spw = ''
         field = ''
         antenna = ''
         uvrange = ''
         timerange = ''
         correlation = ''
         scan = ''
         intent = ''
         feed = ''
         array = ''
         observation = ''
         verbose = True
         listfile = ""
         listunfl = False
         cachesize = 50.0
         overwrite = False
         #listobs(vis='',selectdata=True,spw='',field='',antenna='',uvrange='',
         timerange='',correlation='',scan='',intent='',feed='',array='',
         observation='',verbose=True,listfile='',listunfl=False,cachesize=50.0,
         overwrite=False )
         
      An example save to a custom named file: ::

         saveinputs('listobs','ngc5921_listobs.par')

