

# Advanced: flagdata 

Advanced Information on flagdata. C++ code infrastructure\...

\--CASA Developer\--

For advanced information about some parts of flagdata please visit:

[http://www.aoc.nrao.edu/\~rurvashi/FlaggerDocs/FlaggerDocs.html](http://www.aoc.nrao.edu/~rurvashi/FlaggerDocs/FlaggerDocs.html)

In progress\...

 

## 1.1 C++ Infrastructure

 

### Main Classes

1.  AgentFlagger: The top-level AgentFlagger class that connects all of the following together, and defines the C++ user-interface for the agentflagger. This is the class used by the tool layer.

2.  FlagDataHandler : A top level class defining the data handling interface for the flagging module.

3.  FlagMSHandler: - TBD

4.  FlagCalTableHandler: - TBD

5.  FlagAgentBase: base class that defines the behaviour of all flagging agents and contains agent-level data-selection, etc. The main functions to be implemented by derived classes are setAgentParameters(), preProcessBuffer(), computeAntennaPairFlags() or computeRowFlags(), getReport() .

    List of available Flag Agents :

    1.  FlagAgentManual : Flag/Unflag based on data-selections. The only processing done by this agent is to set the flags for all data it sees to True if the operation is to flag, and to False to unflag. A boolean parameter apply determines whether to flag (apply=True) or unflag (apply=False). By default it is set to True.

    2.  FlagAgentQuack : Flag time-ranges at the beginning and/or end of scans. Uses the YYY iteration-mode.

    3.  FlagAgentElevation : Flag time-ranges based on source elevation. Uses the YYY iteration-mode.

    4.  FlagAgentShadow : For each timestep, flag antennas that are shadowed by any other antenna. Antennas to be flagged are chosen and marked in the preProcess() stage. Rows are flagged in computeRow(), and this agent uses the YYY iteration-mode.

    5.  FlagAgentExtension : Read and extend flags along specified axes, within the current chunk. Uses the YYY iteration-mode.

    6.  FlagAgentClip : Flag based on a clip threshold and visExpression. Find and flag NaNs and Infs. Uses the YYY iteration-mode.

    7.  FlagAgentTimeFreqCrop : The TFCrop algorithm is run per baseline, via FlagAgentTimeFreqCrop::computeAntennaPairFlags()

    8.  FlagAgentRFlag : The RFlag algorithm. Implements multiple passes through each chunk via the passIntermediate() and passFinal() mechanism.

    9.  FlagAgentSummary : Flag counts are accumulated in computeRow() and packaged into a Record in getResult().

    10. FlagAgentDisplay : Visibilities are read and displayed from computeAntennaPair(). Navigation-buttons control the order in which the framework iterates through baselines.

    11. FlagAgentAntennaIntegrations - TBD

     

6.  The FlagReport class allows each flag agent to build and return information (summary counts, reports as plots, etc) to the user (and/or) to the display agent for end-of-MS reports.

###  Control Flow

![55045d458766e4fad0872ad6a034931be98c7555](media/55045d458766e4fad0872ad6a034931be98c7555.png)

### Performance and Optimizations

There are several performance-optimization choices that can be made. Some of these are under the users control, and some have automated heuristics.

#### List mode

It helps to combine multiple flag commands into a single run ONLY if most of the commands require the same data to be read. The goal is to read data once, apply multiple flag commands, and write flags once.

1.  Manual-flag commands read only meta-data.
2.  Shadow, elevation read meta-data + processing to calculate uvw, azel.
3.  Clip reads visibilities.
4.  tfcrop and rflag read visibilities and flags
5.  Extend, summary read flags

#### Data Pre-selection

If only a subset of the Measurement Set is to be traversed for flag-calculation, it helps to pre-select and iterate through only that section of the MS. When flagdata is run in list mode, there is a second level of selection per agent (command) that ensures that each agent sees only its correct subset of the data.

#### Asynchronous I/O

Asynchronous I/O is a data-access optimization that applies when iterating through the dataset in chunks. It uses multi-threading to pre-read the next chunk of data from disk while the current chunk is being processed.

The user has the option of enabling asynchronous I/O by setting the following variables in the **.casarc** file.

    VisibilityIterator.async.enabled: true     # if present and set to false then async i/o will work
    VisibilityIterator.async.nBuffers: 2       # the default value is two
    VisibilityIterator.async.logFile: stderr   # Send async i/o debug log messages to this file
                                               # if not present or file is invalid then no logging occurs
    VisibilityIterator.async.logLevel: 2       # Level of log messages to output (two is good, too); defaults to 1

    FlagDataHandler.asyncio: true              # True : enable async-IO for the flagger (clip,tfcrop,rflag)
    FlagDataHandler.slurp: true                # True : enable ??
    FlagAgent.background: true                 # True : enable threading mode

Asynchronous I/O helps only when data I/O dominates the total cost. For our current list of agents/algorithms, this helps only for agents that read visibilities. Therefore asynchronous I/O is activated only if clip or tfcrop or rflag are present in the flag-command list.

 

 

