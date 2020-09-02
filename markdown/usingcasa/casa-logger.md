

# Logging 

Detailed description of the CASA logger

# **Logging your session**


The output from CASA commands is sent to the file casa-YYYYMMDD-HHMMSS.log in your local directory, where YYYYMMDD-HHMMSS are the UT date and time when CASA was started up. New starts of CASA create new log files.

[ ![cde9d5a8ce1cfeb84295afa1b539d64fafe3213d](media/cde9d5a8ce1cfeb84295afa1b539d64fafe3213d.png){width="900" height="353"}]{

>The CASA Logger GUI window under Linux. Note that under MacOSX a stripped down logger will instead appear as a Console.
  

The output contained in casa-YYYYMMDD-HHMMSS.log *i*s also displayed in a separate window using the **casalogger**. Generally, the logger window will be brought up when CASA is started. If you do not want the logger GUI to appear, then start casa using the *\--nologger* option,

```
 casa --nologger
```

which will run CASA in the terminal window. See [Starting CASA](https://casa.nrao.edu/casadocs-devel/stable/old-pages/starting-casa) for more startup options.

<div class="alert alert-warning">
**ALERT:** Due to problems with Qt , the GUI qtcasalogger is a different version on MacOSX and uses the Mac Console. This still has the important capabilities such as showing the messages and cut/paste. The following description is for the Linux version and thus should mostly be disregarded on OSX. On the Mac, you treat this as just another console window and use the usual mouse and hot-key actions to do what is needed.
</div>

The CASA logger window for Linux is shown in the [figure above](http://casa.nrao.edu/casadocs/stable/usingcasa/casa-logger#figid-loggerfiggui). The main feature is the display area for the log text, which is divided into columns. The columns are:

-   *Time* --- the time that the message was generated. Note that this will be in local computer time (usually UT) for casa generated messages, and may be different for user generated messages;
-   *Priority* --- the Priority Level (see below) of the message;
-   *Origin* --- where within CASA the message came from. This is in the format Task::Tool::Method (one or more of the fields may be missing depending upon the message);
-   *Message* --- the actual text.

![be077f88660e4fd271021e4d643915e0e53acc68](media/be077f88660e4fd271021e4d643915e0e53acc68.png){width="900" height="353"}

>The CASA Logger GUI window under Linux. Note that under MacOSX a stripped down logger will instead appear as a Console.
  

[ ![230a345b508be96e7bc81d5cb1f7e9bdecfc114f](media/230a345b508be96e7bc81d5cb1f7e9bdecfc114f.png){width="900" height="353"}]{

>Using the casalogger Filter facility. The log output can be sorted by Priority, Time, Origin, and Message. In this example we are filtering by Origin using 'clean', and it now shows all the log output from the clean task.
  

 

The casalogger GUI has a range of features, which include:

-   *Search* --- search messages by entering text in the Search window and clicking the search icon. The search currently just matches the exact text you type anywhere in the message. See Figure [above](http://casa.nrao.edu/casadocs/stable/usingcasa/casa-logger#figid-loggerfiggui) for an example.
-   *Filter* --- a filter to sort by message priority, time, task/tool of origin, and message contents. Enter text in the *Filter* window and click the filter icon to the right of the window. Use the pull-down at the left of the *Filter* window to choose what to filter. The matching is for the exact text currently (no regular expressions). See Figure [above](http://casa.nrao.edu/casadocs/stable/usingcasa/casa-logger#figid-loggerfigfilter) for an example.
-   *View* --- show and hide columns (*Time, Priority, Origin, Message*) by checking boxes under the *View* menu pull-down. You can also change the font here.
-   *Insert Message* --- insert additional comments as "notes" in the log. Enter the text into the "I*nsert Message*" box at the bottom of the logger, and click on the *Add* (+) button, or choose to enter a longer message. The entered message will appear with a priority of "*NOTE*" with the Origin as your username. See Figure [below](http://casa.nrao.edu/casadocs/stable/usingcasa/casa-logger#figid-loggerfiginsert) for an example.
-   *Copy* --- left-click on a row, or click-drag a range of rows, or click at the start and *shift click* at the end to select. Use the *Copy* button or *Edit* menu *Copy* to put the selected rows into the clipboard. You can then (usually) paste this where you wish.
-   *Open* --- There is an Open function in the File menu, and an Open button, that will allow you to load old casalogger files.

<div class="alert alert-warning">
**Alert:** Messages added through *Insert Message* will currently not be inserted into the correct (or user controllable) order into the log. *Copy*  does not work routinely in the current version. It is recommended to open the casa-YYYYMMDD-HHMMSS.log file in a text editor, to grab text.
</div>

[ ![507e2d4b51f64aef893603257c48a890f830c47c](media/507e2d4b51f64aef893603257c48a890f830c47c.png){width="900" height="353"}]{

>CASA Logger - Insert facility: The log output can be augmented by adding notes or comments during the reduction. The file should then be saved to disk to retain these changes.
  

Other operations are also possible from the menu or buttons. Mouse "flyover" displays a tooltip describing the operation of buttons.

It is possible to change the name of the logging file. By default it is 'casa-YYYYMMDD-HHMMSS.log'. But starting CASA with the option *\--logfile *will redirect the output of the logger to the file 'otherfile.log' (see also Page on \"[Starting CASA](https://casa.nrao.edu/casadocs-devel/stable/old-pages/starting-casa)\").

```
casa --logfile otherfile.log
```

The log file can also be changed during a CASA session. Typing:

```
casalog.setlogfile('otherfile.log')
```

will redirect the output to the 'otherfile.log*'* file. However, the logger GUI will still be monitoring the previous 'casa-YYYYMMDD-HHMMSS.log' file. To change it to the new file, go on *File - Open* and select the new log file, in our case 'otherfile.log*'*.


# **Startup options for the logger** 

One can specify logger options at the startup of casa on the command line:

```
casa <logger options>
```

The options are described in \"[Starting CASA](https://casa.nrao.edu/casadocs-devel/stable/old-pages/starting-casa)\". For example, to inhibit the a GUI and send the logging messages to your terminal, do

```
casa --nologger --log2term
```

while

```
casa --logfile mynewlogfile.log
```

will start CASA with logger messages going to the file mynewlogfile.log. For no log file at all, use:

```
casa --nologfile
```

 

# **Setting priority levels in the logger** 

**Logger** messages are assigned a Priority Level when generated within CASA. The current levels of Priority are:

1.  *SEVERE* --- errors;
2.  *WARN* --- warnings;
3.  *INFO* --- basic information every user should be aware of or has requested;
4.  *INFO1* --- information possibly helpful to the user;
5.  *INFO2* --- details for advanced users;
6.  *INFO3* --- continued details;
7.  *INFO4* --- lowest level of non-debugging information;
8.  *DEBUGGING* --- most "important" debugging messages;
9.  *DEBUG1* --- more details;
10. *DEBUG2* --- lowest level of debugging messages.

The "debugging" levels are intended for the developers use. 

<div class="alert alert-info">
**Inside the Toolkit:**

The **casalog** tool can be used to control the logging. In particular, the **casalog.filter** method sets the priority threshold. This tool can also be used to change the output log file, and to post messages into the logger.

There is a threshold for which these messages are written to the casa-YYYYMMDD-HHMMSS.log file and are thus visible in the logger. By default, only messages at level *INFO* and above are logged. The user can change the threshold using the **casalog.filter** method. This takes a single string argument of the level for the threshold. The level sets the lowest priority that will be generated, and all messages of this level or higher will go into the casa-YYYYMMDD-HHMMSS.log file.

Some examples:

casalog.filter('INFO')           #the default
casalog.filter('INFO2')          #should satisfy even advanced users
casalog.filter('INFO4')          #all INFOx messages
casalog.filter('DEBUG2')         #all messages including debuggingcasalog.

**WARNING:** Setting the threshold to DEBUG2 will put lots of messages in the log!
</div>

 

