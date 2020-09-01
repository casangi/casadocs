

# Work Request Scheduling 

Process for scheduling CASA work requests

\--CASA Developer\--

The work scheduling processes consists of two basic steps: duration estimation and activity scheduling.

## Duration Estimates

Developers should estimate the development duration of Bugs, Features, Engineering Tasks, Research Requests, and Sub-tasks.  These 5 issue types should have durations of 2 weeks or less.  Any issue requiring more than 2 weeks of effort should be converted to an Epic and assigned to the PM for estimation and scheduling.  To simplify the estimation and scheduling process, developers are encouraged to reserve one day per week for miscellaneous tasks (team meetings, helping a colleague, etc.).  Thus, an issue scheduled to last 2 weeks would take 8 ideal working days of effort.  The reserved 1 day per week also provides a buffer for the scheduled tasks.

## Activity Scheduling

The CDG will use as soon as possible (ASAP) scheduling to favor predictability of development effort.  This means that new issues are scheduled for work after all previously scheduled tasks.  This will allow better coordination with scientists by providing advanced notification of when the development work will be completed.  Expediting of tasks (scheduling a new issue before a previously scheduled task) is allowed only by approval of the GL.  Developers are responsible for scheduling Bug, Feature, Engineering Task, and Research Requests.  The PM is responsible for scheduling Epics.

The CDG currently has a large backlog of work recorded in JIRA tasks.  True ASAP scheduling would require that the backlog be fully scheduled.  To avoid unnecessary effort, a gradual approach will be applied instead, where the backlog is scheduled 2 months in advance until the team retrospective in Q3 FY17.  During this time, the team will work toward improved estimation accuracy.  A plan for moving toward true ASAP scheduling will be included in the process improvement plan delivered in Q4.

Each developer should have one issue scheduled at any given time.  In other words, developers should prioritize the currently scheduled issue above all not-currently-scheduled issues.  Only blocker-priority issues will preempt a scheduled task.  When a developer\'s work on an issue is waiting on another resource (e.g. waiting on a response from a scientist, or waiting for a build and test cycle to complete) it is acceptable to work on another issue.

<div class="alert alert-info">
As a convenience, a JIRA filter, [Scheduled Issues this Week](https://open-jira.nrao.edu/issues/?filter=10503), has been created that shows a developer\'s scheduled issues for the week.  It is easy to subscribe to this filter by clicking \"Details\" and \"New Subscription\" and receive a weekly email summarizing all scheduled tasks for the week.
</div>

When a JIRA issue is transitioned to the Scheduled state, the development start and end dates should be set.  This adds the issue to the CASA team calendar.  Issues can be rescheduled by changing the development start and end dates in JIRA or by clicking and dragging using the team calendar.  Each developer should have only one task scheduled at any given time.  A simultaneously scheduled parent and child ticket could be an exception to this rule.  The currently scheduled issue has priority over all other work, with the exception of blocker issues.

 

