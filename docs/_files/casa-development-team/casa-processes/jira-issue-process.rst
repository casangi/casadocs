.. container::
   :name: viewlet-above-content-title

JIRA Work Request Management
============================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Process for work request management using JIRA

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   --CASA Developer--

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Background
         :name: background

      In the fall of 2016 the CASA development group (CDG) migrated to a
      `new JIRA server <https://open-jira.nrao.edu/>`__ that is
      integrated with Atlassian software systems
      `Confluence <https://open-confluence.nrao.edu/>`__,
      `BitBucket <https://open-bitbucket.nrao.edu/>`__, and
      `Bamboo <https://open-bamboo.nrao.edu/>`__. This change is
      motivated by the
      `recommendations <https://sharepoint.nrao.edu/dms/CASA%20Docs/Miranda%20Recommendations/EMiranda%20Recommendations.pdf>`__
      provided by an exernal consultant who studied the CDG in 2015. The
      Data Management and Software Department (DMSD) has developed a
      `software development processes
      document <https://staff.nrao.edu/wiki/bin/view/DMS/DMSDevelopmentProcesses>`__
      that describes departmental policies and recommendations for its
      software teams; this document adopts some of the recommendations
      applicable across the department. The CDG JIRA processes follow
      the DMSD processes as much as possible. This document describes
      these processes.

       

      .. rubric:: Issue Types
         :name: issue-types

      The following table describes the issue types allowed in the CASA
      project:

      +----------------------------+----------------------------------------+
      | **Issue Type**             | **Description**                        |
      +----------------------------+----------------------------------------+
      | |image11| Bug              | A request to correct a deviation of    |
      |                            | the system from its specified          |
      |                            | behavior.                              |
      +----------------------------+----------------------------------------+
      | |image12| Feature          | A request to change the current        |
      |                            | specified behavior.  Features should   |
      |                            | always undergo validation testing.     |
      +----------------------------+----------------------------------------+
      | |image13| Engineering Task | An internal change request to improve  |
      |                            | maintainability of the code, perform   |
      |                            | refactoring activities, clean up,      |
      |                            | improve documentation, etc.  An issue  |
      |                            | of this type does not require          |
      |                            | validation (user) testing.             |
      +----------------------------+----------------------------------------+
      | |image14| Epic             | A large, cross functional work request |
      |                            | that requires substantially more       |
      |                            | coordination than other jobs.          |
      +----------------------------+----------------------------------------+
      | |image15| Research Request | A request for new capabilities in      |
      |                            | which either the requestor cannot      |
      |                            | define the expected result or the      |
      |                            | developers are unsure about whether    |
      |                            | the requirement can be implemented.    |
      +----------------------------+----------------------------------------+
      | |Sub-Task| Sub-Task        | Part of a larger issue.                |
      +----------------------------+----------------------------------------+

      For a brief description of JIRA issue types see the `JIRA Concepts
      -
      Issues <https://open-jira.nrao.edu/secure/ShowConstantsHelp.jspa?decorator=popup#IssueTypes>`__
      page. All of the issue types allowed in the CASA project are
      described in detail in the `DMSD software development processes
      document <https://staff.nrao.edu/wiki/bin/view/DMS/DMSDevelopmentProcesses>`__.
      The only exception is the Sub-task issue type, which has been
      turned on for the CASA project to allow other issues to be broken
      down into smaller work assignments. The sub-task issue type uses
      the Feature workflow.

      .. rubric:: Note on Features vs. Epics
         :name: note-on-features-vs.-epics

      Features and Epics are described in the DMSD document in sections
      7.2 and 7.4, respectively. A Feature has low coordination needs
      and is a relatively small, compact change. If the implementation
      requires coordination or will take more than two weeks to develop,
      the request should be characterized as an Epic. Epics are
      typically broken down into sub-tasks.

      .. container:: alert-box

         Bamboo builds:  All appropriately-named branches will be built
         by the Bamboo CI plan.  However, only tickets that are typed in
         JIRA as a Feature (with a feature/CAS-XXXX branch) or a Bugfix
         (with a bugfix/CAS-XXXX branch) will be packaged and tested
         with the Bamboo Branch plans!

      .. rubric:: Issue States
         :name: issue-states

      The following table describes the issue states allowed in the CASA
      project:

      +--------------------+-------------------------+---------------------+
      | **Issue state**    | **Description**         | **Responsible**     |
      +--------------------+-------------------------+---------------------+
      | Open               | Initial state after a   | Component lead      |
      |                    | new ticket is created.  |                     |
      +--------------------+-------------------------+---------------------+
      | Unscheduled        | Ticket has been         | Developer           |
      |                    | accepted but has not    |                     |
      |                    | been scheduled yet.     |                     |
      +--------------------+-------------------------+---------------------+
      | Input Required     | Ticket requires         | Domain expert       |
      |                    | additional information. |                     |
      +--------------------+-------------------------+---------------------+
      | Scheduled          | Ticket is investigated, | Developer           |
      |                    | reproduced, fixed, and  |                     |
      |                    | tested.                 |                     |
      +--------------------+-------------------------+---------------------+
      | Ready to Verify    | Ticket requires         | PM / GL             |
      |                    | additional verification |                     |
      |                    | besides that executed   |                     |
      |                    | by the developer while  |                     |
      |                    | in the Scheduled state. |                     |
      +--------------------+-------------------------+---------------------+
      | Under Verification | Additional verification | Verification tester |
      |                    | tests are executed and  |                     |
      |                    | results reported.       |                     |
      +--------------------+-------------------------+---------------------+
      | Ready to Validate  | Waiting state where     | Validation lead     |
      |                    | ticket is ready to be   |                     |
      |                    | tested by Validator.    |                     |
      +--------------------+-------------------------+---------------------+
      | Under Validation   | Validation test is      | Validation tester   |
      |                    | performed.              |                     |
      +--------------------+-------------------------+---------------------+
      | Resolved           | Developer performs      | Developer           |
      |                    | post-development        |                     |
      |                    | activities, including   |                     |
      |                    | making a pull-request.  |                     |
      +--------------------+-------------------------+---------------------+
      | Completed          | Ticket is ready for     | Build Team          |
      |                    | delivery but has not    |                     |
      |                    | yet been delivered.     |                     |
      +--------------------+-------------------------+---------------------+
      | Closed             | Final state. No more    | None                |
      |                    | work can be done.       |                     |
      +--------------------+-------------------------+---------------------+

      The issue states are described in greater detail in the `DMSD
      software development processes
      document <https://staff.nrao.edu/wiki/bin/view/DMS/DMSDevelopmentProcesses>`__.  

      Under normal conditions an issue cannot be reopened. The reason
      for this restriction lies in the way that the JIRA issue workflow
      is integrated with the revision control system (BitBucket). After
      development activity, an issue is closed when the branch
      associated with the issue has been merged back into the master
      branch. Since there is no way to unmerge a branch, there is
      likewise no way to un-close a ticket. Rather than re-opening a
      ticket, you must create a new ticket.  In exceptional
      circumstances (such as human error) a CASA project administrator
      can reopen a closed ticket.

      .. container:: info-box

         **NOTE**:  It is quite easy to link a new ticket to an old,
         closed ticket.

       

      .. rubric:: Issue Workflows
         :name: issue-workflows

      Each issue type has its own workflow describing the issue states
      allowed and the allowed transitions between states.  We have
      attempted, as much as possible, to minimize the number of clicks
      required to move an issue through the workflow.  The table below
      describes the workflows for each issue type:

      +-----------------------------------+-----------------------------------+
      | **Issue Types**                   | **Workflow Description**          |
      +-----------------------------------+-----------------------------------+
      | |image16| Bug                     | The workflows for these issues    |
      |                                   | contain all states described      |
      | |image17| Feature                 | above.                            |
      |                                   |                                   |
      | |image18| Epic                    |                                   |
      |                                   |                                   |
      | |Sub-Task| Sub-Task               |                                   |
      +-----------------------------------+-----------------------------------+
      | |image19| Engineering Task        | Workflow does not contain         |
      |                                   | validation steps.                 |
      +-----------------------------------+-----------------------------------+
      | |image20| Research Request        | Workflow does not contain         |
      |                                   | verification or validation        |
      |                                   | steps.                            |
      +-----------------------------------+-----------------------------------+

      A graphical rendering of the Bug / Feature / Epic / Sub-Task
      workflow is shown, below:

      |image21|

      When viewing a JIRA ticket, a link is available next to the issue
      status value, "View Workflow". If you click this link you will see
      a graphical description of the workflow for that issue type. The
      graphical workflow includes tool-tips that describe each status
      and transition. For a more detailed discussion of workflows see
      the `DMSD software development processes
      document <https://staff.nrao.edu/wiki/bin/view/DMS/DMSDevelopmentProcesses>`__.

.. container:: section
   :name: viewlet-below-content-body

.. |image1| image:: https://open-jira.nrao.edu/secure/viewavatar?size=xsmall&avatarId=10303&avatarType=issuetype
   :width: 16px
   :height: 16px
.. |image2| image:: https://open-jira.nrao.edu/secure/viewavatar?size=xsmall&avatarId=10310&avatarType=issuetype
   :width: 16px
   :height: 16px
.. |image3| image:: https://open-jira.nrao.edu/secure/viewavatar?size=xsmall&avatarId=10321&avatarType=issuetype
   :width: 16px
   :height: 16px
.. |image4| image:: https://open-jira.nrao.edu/images/icons/issuetypes/epic.svg
   :width: 16px
   :height: 16px
.. |image5| image:: https://open-jira.nrao.edu/secure/viewavatar?size=xsmall&avatarId=10322&avatarType=issuetype
   :width: 16px
   :height: 16px
.. |Sub-Task| image:: https://open-jira.nrao.edu/secure/viewavatar?size=xsmall&avatarId=10316&avatarType=issuetype
   :width: 16px
   :height: 16px
.. |image6| image:: https://open-jira.nrao.edu/secure/viewavatar?size=xsmall&avatarId=10303&avatarType=issuetype
   :width: 16px
   :height: 16px
.. |image7| image:: https://open-jira.nrao.edu/secure/viewavatar?size=xsmall&avatarId=10310&avatarType=issuetype
   :width: 16px
   :height: 16px
.. |image8| image:: https://open-jira.nrao.edu/secure/viewavatar?size=xsmall&avatarId=10321&avatarType=issuetype
   :width: 16px
   :height: 16px
.. |image9| image:: https://open-jira.nrao.edu/images/icons/issuetypes/epic.svg
   :width: 16px
   :height: 16px
.. |image10| image:: https://open-jira.nrao.edu/secure/viewavatar?size=xsmall&avatarId=10322&avatarType=issuetype
   :width: 16px
   :height: 16px
.. |image11| image:: https://open-jira.nrao.edu/secure/viewavatar?size=xsmall&avatarId=10303&avatarType=issuetype
   :width: 16px
   :height: 16px
.. |image12| image:: https://open-jira.nrao.edu/secure/viewavatar?size=xsmall&avatarId=10310&avatarType=issuetype
   :width: 16px
   :height: 16px
.. |image13| image:: https://open-jira.nrao.edu/secure/viewavatar?size=xsmall&avatarId=10321&avatarType=issuetype
   :width: 16px
   :height: 16px
.. |image14| image:: https://open-jira.nrao.edu/images/icons/issuetypes/epic.svg
   :width: 16px
   :height: 16px
.. |image15| image:: https://open-jira.nrao.edu/secure/viewavatar?size=xsmall&avatarId=10322&avatarType=issuetype
   :width: 16px
   :height: 16px
.. |image16| image:: https://open-jira.nrao.edu/secure/viewavatar?size=xsmall&avatarId=10303&avatarType=issuetype
   :width: 16px
   :height: 16px
.. |image17| image:: https://open-jira.nrao.edu/secure/viewavatar?size=xsmall&avatarId=10310&avatarType=issuetype
   :width: 16px
   :height: 16px
.. |image18| image:: https://open-jira.nrao.edu/images/icons/issuetypes/epic.svg
   :width: 16px
   :height: 16px
.. |image19| image:: https://open-jira.nrao.edu/secure/viewavatar?size=xsmall&avatarId=10321&avatarType=issuetype
   :width: 16px
   :height: 16px
.. |image20| image:: https://open-jira.nrao.edu/secure/viewavatar?size=xsmall&avatarId=10322&avatarType=issuetype
   :width: 16px
   :height: 16px
.. |image21| image:: https://casa.nrao.edu/casadocs-devel/stable/casa-development-team/casa-processes/bug-workflow.png/@@images/2dd5f466-8ef3-45dd-9d24-2604ba2503a0.png
   :class: image-inline
   :width: 396px
   :height: 313px
