saveinputs
===========

.. currentmodule:: casashell

.. function:: saveinputs(taskname=None, filename=None)

   Save current task parameters to file

   Parameters
      - **taskname** (*obj* or *None*) - task object, None will use current default
      - **filename** (*string* or *None*) - output file name, None will use current default

   Description
      The ``saveinputs`` command will save the current values of a given task parameters to a
      Python (plain ascii) file. It can take up to two arguments, e.g. ::

         saveinputs(taskname, outfile)

      The first is the usual taskname parameter. The second is the name for the output Python file.
      If there is no second argument, for example, ::

         saveinputs('clean')

      a file with name \<taskname\>.saved (in this case 'clean.saved' will be created or overwritten
      if extant. If invoked with no arguments, e.g. ::

         saveinputs

      it will use the current values of the taskname variable (as set using ``inp <taskname>`` or
      ``default <taskname>``). You can also use the taskname global parameter explicitly, ::

         saveinputs(taskname, taskname+'_1.save')

      For example, starting from default values ::

         CASA <1>: default('listobs')
         CASA <2>: vis='ngc5921.demo.ms'
         CASA <3>: saveinputs
         CASA <4>: !more 'listobs.saved'
         taskname = "listobs"
         vis = "ngc5921.demo.ms"
         selectdata = True
         spw = ""
         field = ""
         antenna = ""
         uvrange = ""
         timerange = ""
         correlation = ""
         scan = ""
         intent = ""
         feed = ""
         array = ""
         observation = ""
         verbose = True
         listfile = ""
         #listobs(vis="ngc5921.demo.ms",selectdata=True,spw="",field="",
         antenna="",uvrange="",timerange="",correlation="",scan="",intent="",
         feed="",array="",observation="",verbose=True,listfile="")

      An example save to a custom named file: ::

         saveinputs('listobs','ngc5921_listobs.par')

