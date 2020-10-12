

.. _Description:

Description
   applycal task: Apply calibrations solution(s) to data
   
   .. rubric:: Overall Description
      
   
   | The calibration analysis (ca) tool is a standardized interface
     to the new format (CASA 3.4 and later) calibration tables. It is
     designed to handle all types of tables, e.g., gain, bandpass,
     Tsys, etc. The ca tool takes advantages of newly implemented
     features in the CASA C++ code tree, e.g., iteration and
     parameter selection, which means that calibration tables can be
     accessed in a manner very similar to measurement sets.
   | The ca tool was originally designed to facilitate getting and/or
     processing data from an entire calibration table in an organized
     fashion so that the information could be written to other files.
     Additional features, e.g. introspective member functions, were
     added so that scripters and general users can easily employ the
     ca tool without using iteration (get one piece of data at a
     time).
   | Like the imaging tool (im), image analysis tool (ia),
     calibration tool (cb), etc., a native calibration analysis tool
     (ca) is created when CASA starts up. Other instances of the
     calibration analysis tool can be created, if required, using the
     command:
   | \\begin{center from casac import casac caLoc =
     casac.calanalysis() \\end{center
   
   .. rubric:: Open/Close Member Functions
      
   
   | The purpose of the open() and close() member functions is
     obvious, i.e., they open and close the new format calibration
     table. Each ca tool instance can have only one open table. If no
     table has been opened, the other member functions don't return
     anything.
   | The member function definitions are:
   | ca.open( '' ) - This member function opens the calibration
     table. If successful True is returned, otherwise False is
     returned.
   | ca.close() - This member function closes the calibration table.
     If a table was open True is returned, otherwise False is
     returned.
   
   .. rubric:: Introspective Member Functions
      
   
   | The introspective member functions provide information about the
     shape and contents of the file. For example, the numchannel()
     member function returns the number of channels corresponding to
     each spectral window. Also, the field() member function returns
     the field names or numbers. With this information, users can
     easily select and keep track of limited regions of the
     calibration table, even from the command line, by minimizing the
     number of iterations.
   | The member function definitions are:
   | ca.antenna( name=True ) - This member function returns the
     antenna numbers or names as a python list of strings.
   | ca.calname() - This member function returns the new format
     calibration table name as a python string.
   | ca.feed() - This member function returns the feed names as a
     python list of strings ('X', 'Y' for linear; 'R', 'L' for
     circular; 'S' for "scalar", when the calibration solutions are
     performed simultaneously for both polarizations). If the basis
     is unknown, then the basis functions are '1' and '2'. This
     kludge was added to handle incomplete calibration tables.
   | ca.field( name=True ) - This member function returns the field
     numbers or names as a python list of strings.
   | ca.freq() - This member function returns the frequencies in the
     table as a python dictionary (the keys are the spectral window
     numbers and the elements are numpy float arrays containing the
     frequencies).
   | ca.msname() - This member function returns the parent
     measurement set name as a python string.
   | ca.numantenna() - This member function returns the number of
     antennas as a python integer.
   | ca.numchannel() - This member function returns the number of
     channels for each spectral window as a list of python integers.
   | ca.numfeed() - This member function returns the number of feeds
     as a python integer.
   | ca.numfield() - This member function returns the number of
     fields as a python integer.
   | ca.numspw() - This member function returns the number of
     spectral windows as a python integer.
   | ca.numtime() - This member function returns the number of times
     as a python integer.
   | ca.partype() - This member function returns the parameter column
     type ('Float' or 'Complex').
   | ca.polbasis() - This member function returns the polarization
     basis ('L' for linear or 'C' for circular). If the basis is
     unknown, 'U' is returned. This kludge was added to handle
     incomplete calibration tables.
   | ca.spw( name=True ) - This member function returns the spectral
     window numbers or names as a python list of strings.
   | ca.time() - This member function returns the times as a python
     list of floats (in units of MJD seconds). In the future, date
     strings will be available.
   | ca.viscal() - This member function returns the type of new
     formation calibration table as a python string. For example 'B'
     is a bandpass table, 'G' is a gain table, etc.
   
   .. rubric:: Process Member Functions
      
   
   | The process member functions process data. As of CASA 3.4, there
     are two: get() and fit(). The get() member function iterates
     through the calibration table and returns the selected data. The
     fit() member function does the same as the get() member function
     and returns the fits as well. Tables with complex parameters are
     converted to either amplitudes or phases.
   | The get() and fit() member functions employ two levels of
     iteration. The first level involves field, antenna 1, and
     antenna2 (slowest to fastest). The data for each first-level
     iteration are placed in a cube whose dimensions are feed x
     frequency x time. Two of these dimensions represent the second
     level of iteration. The feed axis is always an iteration axis,
     and the user can select either frequency or time as the other
     one.
   | In addition to providing a logical way of getting data, this
     two-level iteration scheme also allows users to fit along the
     non-iteration axis. For example, a fit can be peformed along the
     frequency axis for each iteration of the selected field, antenna
     1, antenna 2, feed, and time.
   
   .. rubric:: Inputs
      
   
   | As mentioned above, the selection syntax originally designed for
     measurement sets has been implemented in the ca tool. It is
     available for feed, antenna 1 and 2, and spectral window with
     channel. For more information, consult the selection
     documentation. Their argument lists are:
   | ca.get( field='', antenna='', timerange=[], spw='', feed='',
     axis='TIME', ap='AMPLITUDE', norm=True, unwrap=True, jumpmax=0.0
     )
   | ca.fit( field='', antenna='', timerange=[], spw='', feed='',
     axis='TIME', ap='AMPLITUDE', norm=True, unwrap=True,
     jumpmax=0.0, order='AVERAGE', type='LSQ', weight=False )
   | '*' is equivalent to ''. Both numbers and names can be used for
     field, antenna, and spw. Names have not been implemented in
     present EVLA and ALMA datasets for some quantities. Check if
     they are available using the introspective methods.
   | The least-squares fit is quite standard. The robust fit, which
     minimizes the effects of outliers, is experimental. Robust fits
     are simple to compute, but they don't provide parameter
     variances and covariances. To minimize outliers and obtain
     (co)variances, the following algorithm is used:\newline \\indent
     - Calculate the least-squares fit.\newline \\indent - Using the
     fit parameters from the least squares fit as starting values,
     perform the robust fit (which is essentially a zero-finding
     algorithm). \\newline \\indent - Flag all outliers with
     residuals greater than 5 times the mean deviation. These flags
     are actually returned, so they can be applied elsewhere.
     \\newline \\indent - Recalculate the least-squares fit without
     the outliers.
   | Arguments for get() and fit():
   | field = A comma-delimited string or a python list of strings
     containing the fields. E.g., field = '0,1'. The default is ''
     (all fields).
   | antenna = A comma- and semi-colon- delimited string containing
     the antenna 1s and antenna 2s. E.g, antenna = '3,4,5'. The
     default is '' (all antenna 1s and antenna 2s).
   | timerange = A python list of floats of length two containing the
     start and stop times in MJD seconds. Date strings will be
     implemented in a future release when they are implemented in the
     selection C++ code. E.g., timerange = [456123.0,456456.0]. The
     default is [min MJD, max MJD]. For convenience, the MJD times
     can be obtained from the time() instrospective method.
   | spw = A comma- and semi-column- delimited string containing the
     spectral window and channel selection. E.g., spw =
     '0:4~20;25~59,2:10~30,6'. The default is '' (all spectral
     windows and channels).
   | feed = A comma-delimited string or python list of strings
     containing the feed names ('X', 'Y', 'R', 'L', or 'S' [scalar]).
     E.g., feed='X,Y'. The default is '' (all feeds).
   | axis = A python string containing the user-defined iteration
     axis ('TIME' or 'FREQ'). E.g., axis='FREQ'. The default is
     'TIME' (the frequency axis is a non-iteration axis).
   | ap = A python string containing the amplitude/phase selection
     ('AMPLITUDE' or 'PHASE'). E.g., ap = 'PHASE'. The default is
     'AMPLITUDE'. It is ignored if the parameters in the calibration
     table are real.
   | norm = A python boolean which determines whether amplitudes are
     normalized for each iteration. E.g., norm = False. The default
     is True. It is ignored if the parameters in the calibration
     table are real or ap = 'PHASE'.
   | unwrap = A python boolean which determines whether phases are
     unwrapped for each iteration. E.g., unwrap = False. The default
     is True. It is ignored if the parameters in the calibration
     table are real or ap = 'AMPLITUDE'.
   | jumpmax = A python float which determines the maximum phase jump
     near +/- PI before unwrapping is performed. E.g., jumpmax = 0.1.
     The default is 0.0. It is ignored if the parameters in the
     calibration table are real or ap = 'AMPLITUDE'. If the
     non-iteration axis is frequency:\newline \\indent - if jumpmax
     == 0.0, use fringe fitting (only available when the
     non-iteration axis is time).\newline \\indent - if jumpmax !=
     0.0, use simple unwrapping (same algorithm as used when the
     non-iteration axis is time or frequency).
   | Arguments for fit() only:
   | order = A python string containing the fit order ('AVERAGE',
     'LINEAR', or 'QUADRATIC'). E.g., order = 'LINEAR'. The default
     is 'AVERAGE'. 'QUADRATIC' is not available when the fit type is
     'ROBUST'.
   | type = A python string containing the fit type ('LSQ' or
     'ROBUST'). E.g., type = 'ROBUST'. The default is 'LSQ'. The
     robust fit, which minimizes the effects of outliers, is
     experimental. Robust fits are simple to compute, but they don't
     provide parameter variances and covariances. To minimize
     outliers and obtain (co)variances, the following algorithm is
     used:\newline \\indent - Calculate the least-squares
     fit.\newline \\indent - Using the fit parameters from the least
     squares fit as starting values, perform the robust fit (which is
     essentially a zero-finding algorithm). \\newline \\indent - Flag
     all outliers with residuals greater than 5 times the mean
     deviation. These flags are actually returned, so they can be
     applied elsewhere. \\newline \\indent - Recalculate the
     least-squares fit without the outliers.
   | weight = A python boolean which determines whether weights are
     applied. E.g., weight = True. The default is False.
   
   .. rubric:: Outputs
      
   
   | The get() and fit() member function return dictionaries of
     dictionaries. They both return this information (the '\#'
     represents the iteration number):
   | ['\#']['field'] = The python string containing the field number.
   | ['\#']['antenna1'] = The python string containing the antenna 1
     number.
   | ['\#']['antenna2'] = The python string containing the antenna 2
     number.
   | ['\#']['feed'] = A python string containing the feed.
   | ['\#']['value'] = The numpy float array containing the
     parameters (either along the time or frequency axis) from the
     new format calibration table (if the table contains complex
     numbers, these numbers are either amplitudes or phases).
   | ['\#']['valueErr'] = The numpy float array containing the
     parameter errors (either along the time or frequency axis) from
     the new format calibration table (if the table contains complex
     parameters, these numbers are either amplitude or phase errors).
   | ['\#']['flag'] = The numpy boolean array containing the
     parameter flags.
   | ['\#']['abscissa'] = The python string containing the name of
     the non-iteration axis ('frequency' or 'time').
   | ['\#']['frequency'] = The numpy float array containing the
     frequencies. If the frequency axis is not an iteration axis, the
     frequencies correspond to the values, value errors, and flags.
     If the frequency axis is an iteration axis, this array has only
     one value.
   | ['\#']['time'] = The numpy float array containing the times. If
     the time axis is not an iteration axis, the times correspond to
     the values, value errors, and flags. If the time axis is an
     iteration axis, this array has only one value.
   | ['\#']['rap'] = The python string containing 'REAL',
     'AMPLITUDE', or 'PHASE', describing the values and their errors.
   | ['\#']['norm'] = The python boolean determining whether the
     amplitudes are normalized per iteration or not. It is not
     present for 'REAL' or 'PHASE' data.
   | ['\#']['unwrap'] = The python boolean determining whether the
     phases are unwrapped per iteration or not. It is not present for
     'REAL' or 'AMPLITUDE' data.
   | ['\#']['jumpmax'] = The python float containing the maximum
     phase jump near +/- PI before unwrapping is performed. It is not
     present for 'REAL' or 'AMPLITUDE' data. If the non-iteration
     axis is 'frequency':\newline \\indent - if jumpmax == 0.0,
     fringe fitting was used (only available when the non-iteration
     axis is time).\newline \\indent - if jumpmax != 0.0, simple
     unwrapping was unused (same algorithm as used when the
     non-iteration axis is time or frequency).
   | In addition to these entries, the fit() member function returns
     these:
   | ['\#']['order'] = The python string describing the fit order
     ('AVERAGE', 'LINEAR', or 'QUADRATIC'). 'QUADRATIC' is not
     available for 'ROBUST' fitting.
   | ['\#']['type'] = The python string containing the fit type
     ('LSQ' or 'ROBUST').
   | ['\#']['weight'] = The python boolean determining whether the
     fit was weighted or not.
   | ['\#']['validFit'] = The python boolean telling whether the fit
     was valid or not.
   | ['\#']['pars'] = The numpy float array containing the fit
     parameters.
   | ['\#']['vars'] = The numpy float array containing the fit
     parameter variances.
   | ['\#']['covars'] = The numpy float array containing the fit
     parameter covariances (par0-par1, par0-par2, ..., par1-par2).
   | ['\#']['redChi2'] = The python float containing the reduced chi2
     (set to 1.0 for unweighted fits).
   | ['\#']['model'] = The numpy float array containing the model
     versus the abscissae.
   | ['\#']['res'] = The numpy float array containing the fit
     residuals versus the absicissae.
   | ['\#']['resMean'] = The python float containing the mean of the
     residuals.
   | ['\#']['resVar'] = The python float containing the variance of
     the residuals.
   

.. _Examples:

Examples
   

.. _Development:

Development
   --CASA Developer--
   