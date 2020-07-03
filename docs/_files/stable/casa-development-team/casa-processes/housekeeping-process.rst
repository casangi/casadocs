.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Housekeeping Process
====================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Process for CASA housekeeping (technical debt elimination) activities

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   --CASA Developer--

   .. container::
      :name: parent-fieldname-text

      The CASA team is currently hampered by "technical debt."  The debt
      is a result of both past insufficient architectual planning and
      the use of development shortcuts made to save time at the expense
      of good software engineering practice.  This process establishes a
      path for paying off the technical debt.

      .. rubric:: Development and Housekeeping
         :name: development-and-housekeeping

      Every six months, the CDG will devote 1 month to housekeeping
      activities.  In the current 6-month release cycle, the first month
      of a new cycle will be devoted to housekeeping.  As with new
      feature development, blocker-level bugs will take precedence over
      housekeeping activities.  Housekeeping work requests, like other
      work requests should be scheduled by estimating the duration of
      the housekeeping activity.  If the activity exceeds 8 days of
      development work, the activity should be reclassified as an Epic. 
      Housekeeping epics should be scheduled in coordination with the
      PM, potentially outside the normal housekeeping window.

      .. rubric:: Housekeeping Schedule
         :name: housekeeping-schedule

      (T0 = start of housekeeping period)

      #. T0 - 2 months: The GL and PM assess CASA housekeeping needs and
         generate new JIRA issues as needed.  Housekeeping issues are
         assigned to developers.  Housekeeping tasks should be assigned
         to every developer.  A developer may be exempt from the
         housekeeping activity only if her/his domain of expertise
         within CASA has no technical debt.
      #. T0 - 1 month: Developers schedule housekeeping issues. 
         Housekeeping work should not exceed 1-month window. 
      #. T0: Developers begin work on housekeeping tasks.  Weekly CDG
         meetings should prioritize discussion of housekeeping issues.
      #. T0 + 1 month: Housekeeping period ends.  The subsequent CDG
         weekly meeting should perform a short retrospective to gather
         developer feedback on the housekeeping process.  Additional
         housekeeping tasks identified during the process should be
         documented using new JIRA issues.  PM assesses accomplishments
         during housekeeping period and complies feedback.
      #. T0 + 2 months: PM generates report on housekeeping activity
         that documents accomplishments, challenges, lessons learned,
         and any proposed process changes.

.. container:: section
   :name: viewlet-below-content-body
