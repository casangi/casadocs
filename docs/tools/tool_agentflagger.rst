

.. _Description:

Description
   The agentflagger tool performs manual as well as automatic synthesis
   flagging operations within casapy.
   
   The agentflagger tool performs manual as well as automatic
   synthesis flagging operations within casapy. The agentflagger tool
   can operate on one measurement set at a time. 
   
   .. rubric:: Open the Measurement Set or Calibration Table and
      Attach it to the Tool
      
   
   The first thing to do is to open the MS or calibration table and
   attach it to the agentflagger tool. Use the af.open method, which
   requires the MS name and optionally the time interval, over which
   to buffer data before running the algorithm. The time interval is
   set by default to 0.0, which means a 'scan' length. The 'ntime'
   parameter is important for the modes tfcrop, rflag and extend.
   
   *af.open('uid_X002.ms')*
   
   .. rubric:: Select the Data
      
   
   | Once the MS is open, the next step is to select the data. This
     step will use the MS selection tool to select the portion of the
     MS given by the parameters. There are two ways of selecting the
     data:
   | 1) Create a Python dictionary which internally will be
     transformed into a record containing the selection parameters.
   | # Select the whole MS. af.selectdata()
   | Select a portion of the MS using a dictionary. myrecord={
     myrecord['scan']='1~3' myrecord['spw']='0:1~10'
     af.selectdata(myrecord)
   | 2) Parse the parameter names directly to the function.
     *af.selectdata(scan='1~3', spw='0:1~10')*
   
   .. rubric:: Parse the Parameters for the Flagging Mode(s)
      
   
   | Each flagging mode is called an agent. The available agents are:
     manual, clip, quack, shadow, elevation, tfcrop, rflag, extend,
     unflag and summary. Each one of these agents may or may not take
     configuration parameters and data selection parameters. Once the
     desired flagging modes are chosen, it is time to give the
     configuration parameters to the tool. Ommited parameters will
     take default values as defined in each agent. There are two ways
     of parsing the agent's parameters.
   | 1) Using the general method af.parseagentparameters(). Construct
     a dictionary with the parameters for each agent. Each agent's
     parameters should go to a different 'key' of the dictionary.
     Example:
   | # Create a shadow agent: myagents = { myagents['mode'] =
     'shadow' af.parseagentparameters(myagents)
   | # Add a summary agent to the list. myagents = { myagents['mode']
     = 'summary myagents['spwchan] = True
     af.parseagentparameters(myagents)
   | # Add a manual agent to the same internal list of agents.
     myagents = { myagents['mode'] = 'manual' myagents['scan'] =
     '1~3,18~20' af.parseagentparameters(myagents)
   | # Add a clip agent to flag the zero-value data. myagents = {
     myagents['mode'] = 'clip' myagents['clipzeros'] = True
     af.parseagentparameters(myagents) # Add another summary agent to
     the list. myagents = { myagents['mode'] = 'summary
     myagents['spwchan] = True af.parseagentparameters(myagents)
   | 2) The other way to parse agent's parameters is to use the
     convenience functions. The above example would become: *# Create
     a shadow agent: af.parseshadowparameters()
     # Add a summary agent to the list.
     af.parsesummaryparameters(spwchan=True)
     # Add a manual agent to the same internal list of agents.
     af.parsemanualparameters(scan='1~3,18~20')
     # Add a clip agent to flag the zero-value data.
     af.parseclipparameters(clipzeros=True) # Add another summary
     agent to the list. af.parsesummaryparameters(spwchan=True)*
   
   .. rubric:: Initialize the Agents
      
   
   | The above step create a list of the agents that the tool will
     use to process the data. This step will check several parameters
     and apply constraints. It will set the iteration approach to
     COMBINE_SCANS_MAP_ANTENNA_PAIRS_ONLY if the agent is either
     tfcrop or extend and combinescans is set to True. Otherwise it
     will set it to COMPLETE_SCAN_MAP_ANTENNA_PAIRS_ONLY.
   | If the list contains agents that set ntime more than once, this
     method will get the maximum value of ntime and use it for all
     agents.
   | If a tfcrop agent is present, this method will create one agent
     per each polarization available, if correlation is set to ALL.
   | In the same way, if an agent tfcrop, rflag or clip is present,
     the asyncio mechanism will be switched on. *af.init()*
   
   .. rubric:: Run the tool
      
   
   | Run the tool to apply or unapply the flags. The run method takes
     two parameters, writeflags and sequential. The parameter
     writeflags controls whether to write the flags or not to the MS.
     By default it is set to True. The sequential parameter tells to
     apply/unapply the flags in parallel or not. By default it is set
     to True, which means that the agents will run in sequential.
   | The run method gathers several reports, depending on wich agents
     are run. The display and summary agents produce reports that can
     be retrieved from calling the run method. The reports are
     returned via a Python dictionary. *myreports =
     af.run(writeflags=True)* The dictionary returned in 'myreports'
     will contain four reports from the two summary agents that were
     added previously. The first report is the normal summary for
     each selection parameter. The second report gives the antenna
     positions for plotting.
   
   .. rubric:: Destroy the tool
      
   
   Do not forget to destroy and close the tool at the end.
   *af.done()*
   

.. _Examples:

Examples
   ::

      af.parsesummaryparameters(spwchan=True, basecnt=True)
   

.. _Development:

Development
   No additional development details

