tput
=====


.. currentmodule:: casashell

.. function:: tput(taskname=None, outfile='')

   Save the current parameter values of a task to a file. If given a taskname, sets taskname as the 
   current active (default) task.

   Parameters
      - **taskname** (*obj*, *string*, or *None*) - task object or task name. None will use current active (default) task.
      - **outfile** (*string*) - output file name. default: <taskname>.last example: savefile='tclean.orion'

   Description
   
      The ``tput`` command will save the current parameter values of a task to a
      Python (plain ascii) file. It can take up to two arguments, e.g. ::

         tput(taskname, outfile)

      The first is the usual taskname parameter. The second is the name for the output Python file.
      If there is no second argument, for example, ::

         tput('tclean')

      a file with name \<taskname\>.last (in this case 'tclean.last' will be created or overwritten
      if extant. If invoked with no arguments, e.g. ::

         tput

      it will use the current active taskname (for example as set using ``inp <taskname>`` or
      ``default <taskname>``).
      
      ``saveinputs`` is a synonym for ``tput``
      
      For example, starting from default values ::

         CASA <1>: default('listobs')
         CASA <2>: tput
         CASA <3>: !more 'listobs.last'
         vis = ''
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

         tput('listobs','ngc5921_listobs.par')

 
      This is a counterpart to ``tget``. Typing ``tput`` without a taskname will save the values of the inputs 
      for the current active (default) task.

      Adding a task name, e.g. ``tput <taskname>`` will save the values for the specified task.
      For example, ::

         default('gaincal') #set current task to gaincal and default
         tget #read saved inputs from gaincal.last (or gaincal.saved)
         inp() #see these inputs!
         vis = 'new.ms' #change the vis parameter
         tput #save back to the gaincal.last file for later use

