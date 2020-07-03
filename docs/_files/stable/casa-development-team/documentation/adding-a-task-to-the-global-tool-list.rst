.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Adding a Task (Tool) to the Global Task List (Global Tool List)
===============================================================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Step-by-step instructions on how to correctly add a new Task to the
   Global Task List or a new Tool to the Global Tool List.

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   --CASA Developer--

   .. container::
      :name: parent-fieldname-text

      All tasks are documented within the Global Task List folder.  All
      tools are documented within the Global Tool List folder.  The
      format of task and tool documentation is very similar.  In fact,
      the only difference between the task and tool templates is that
      tools have a "methods" page where tasks have a "parameters" page. 
      The instructions below explain step-by-step how to create new task
      documentation.  When creating new documentation for a tool, follow
      the same steps, but note that the Global Tool List is used in
      place of the Global Task List, and the Method page is used in
      place of the Parameters page.

      .. rubric:: Adding a Folder for the New Task (Tool)
         :name: adding-a-folder-for-the-new-task-tool

      #. Navigate to the Global Task List (Global Tool List) directory
         within CASA Documentation.
      #. Login with your NRAO credentials.
      #. You will find both published and private Tasks (Tools) within
         the directory as a logged in user.
      #. Click ‘Contents’ on the Plone Toolbar.  You will be redirected
         to the Global Task List Contents page within Plone. The
         Contents page will list all published, private, and items
         excluded from navigation within the Global Task List. You
         should see a folder labelled ‘TASK TEMPLATE’ near the top of
         the list on the first page.  TASK TEMPLATE is an unpublished
         folder that contains all of the pages and code currently
         required for documenting a Task in CASA Docs.
      #. Copy the TASK TEMPLATE folder and paste it back into Contents.
         You should now have a copy of TASK TEMPLATE at the bottom of
         the folder contents list.
      #. Rename TASK TEMPLATE to the name of the Task you are
         documenting. Follow the naming conventions listed below:
      #. Click on the new copy of TASK TEMPLATE.  You will enter the new
         TASK TEMPLATE folder.
      #. Click Edit in the Plone Toolbar.
      #. Update the Title field.  The title should be the name of the
         task -- one word and lowercase. Example: applycal's title is
         "applycal".
      #. Update the Summary field with a one-line description of the
         task.  The description should be equivalent to the short
         description used in the *task.*\ xml file.  Example: imcollapse
         task: Collapse image along one axis, aggregating pixel values
         along that axis.
      #. Click on the Settings tab and update the Short Name field.  The
         Short Name should be "task_" + title of the task ("tool_" +
         title of the tool).  Example: applycal's short name is
         "task_applycal"
      #. Click save.
      #. You are now ready to edit the pages within your new Task
         folder. Your new Task documentation folder should have six
         items total: Redirect, Description, Parameters, Changelog,
         Examples, and Developer.
      #. **DO NOT EDIT** the 'Redirect', 'Parameters', or 'Changelog'
         pages in the Task. The 'Redirect' page is a redirect link to
         the Task's Description page for anonymous users. The
         ‘Parameters’ tab is automatically generated from the task XML
         file.   The ‘Changelog’ tab will eventually be automatically
         generated Bamboo pull-request strings.

      .. rubric:: Populating the Description Tab
         :name: populating-the-description-tab

      #. From the task folder view, navigate to the Description tab
         using the buttons at the top of the page.
      #. Select Edit from the plone toolbar.
      #. Leave the title as *Description.*
      #. Set the summary to the one-line description of the task used in
         the task XML file for shortdescription\ *.*
      #. Don't forget to save when your done. 

      .. rubric:: Reviewing the Parameters Tab
         :name: reviewing-the-parameters-tab

      The Parameters tab is automatically generated from the task.xml
      file each evening.  Review the parameters tab and make any
      necessary changes to the xml to make this as informative as
      possible.  Examples on this page should be short and demonstrate
      the syntax of using the parameter.  Not discussing the functioning
      of options etc.

      .. rubric:: Populating the Examples Tab
         :name: populating-the-examples-tab

      #. Navigate to the examples tab using the button at the top of the
         page.
      #. Select Edit from the plone menu
      #. Leave the title as *Examples*
      #. Leave the summary section blank
      #. Populate the Text field with examples.  Use the formatting and
         templates, as well as equations and images to make the examples
         as clear to the user as possible.  The H1 and H2 formats can be
         used to provide jump points for in page navigation.

      .. rubric:: Populating the Developer Tab
         :name: populating-the-developer-tab

      #. Navigate to the Developer tab and select edit as above.
      #. Ensure that the *CASA Developer* option is selected, this means
         that only people that select the **Developer Mode** will see
         this page.
      #. This is the place to document design decision, gotcha's, or
         other implementation details that are useful for the next
         person looking at this task.

      .. rubric::  
         :name: section

      .. rubric:: Populating the Planning Tab
         :name: populating-the-planning-tab

      #. Navigate to the Planning tab and select edit as above. The
         planning tab is used for planned, future development of the
         task and contains documentation of the planned behavior. 
      #. The state of the Planning tab is set to *internal* so only
         logged in users can see it. 

      .. rubric::  
         :name: section-1

.. container:: section
   :name: viewlet-below-content-body
