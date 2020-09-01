

# Information Collection 

To better understand real-world usage patterns, quality and reliability, CASA collects runtime telemetry and crash reports from users and sends periodic reports back to NRAO. This information is anonymous with no personal identifiable information (PII) or science data included.

# Telemetry

Telemetry records task usage activity (task name, start time, end time) during CASA runs.  Periodically, these reports will be batched together and sent to NRAO.

You can disable telemetry by adding the following line in \~/.casarc

```
EnableTelemetry: False
```

Telemetry adds log files in the \~/.casa directory and submits the data at CASA startup after a predefined interval. This can be configured in the \~/.casarc file by setting TelemetrySubmitInterval to a desired value in seconds.  The default value is 1 week.

You can change the log file cache directory by setting \"TelemetryLogDirectory\" in \~/.casarc.  

You can also configure a maximum Telemetry log usage with \"TelemetryLogLimit\" (in kilobytes). Casa will check for the logfile size periodically and disable Telemetry when the limit is reached. The check interval can be set with \"TelemetryLogSizeInterval\" (seconds)

Summary of all available options in .casarc:

```
`TelemetryLogDirectory: /tmp`
`TelemetryLogLimit: 1650`
`TelemetryLogSizeInterval: 30`
`TelemetrySubmitInterval: 20`
```

# Crash Reporter

Crash reports are triggered whenever a CASA task terminates abnormally (e.g., unhandled C++ exception, segfault, etc.). The crash reports include:

-   program call stack
-   filesystem mount information
-   CASA log
-   memory information
-   operating system version
-   CPU information

You can disable crash reports by adding the following line in \~/.casarc

```
UseCrashReporter: False
```

 

 

