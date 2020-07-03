.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Documentation Validation
========================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Process for validation of user documentation (content review)

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: **Before You Start
         **
         :name: before-you-start

      #. Make sure you log into plone so that any pages currently marked
         "private" are visible to you.
      #. Please locate and review the current (4.7.0) inline help and
         any current online help page (`CASA Task Reference
         Manual <https://casa.nrao.edu/docs/TaskRef/TaskRef.html>`__,
         `CASA Toolkit Reference
         Manual <https://casa.nrao.edu/docs/CasaRef/CasaRef.html>`__)
         for tasks and tools, and the relevant section of the `CASA
         Cookbook  <https://casa.nrao.edu/casa_cookbook.pdf>`__ for
         chapters, for context for the assigned documentation review.
      #. Take a quick tour of plone by clicking the wrench in the upper
         right corner --> "Tutorials" --> "Introduction". It will show
         you several messages pointing out the different features of
         plone.

      .. rubric:: **Testing Plan**
         :name: testing-plan

      .. rubric:: Editorial Content and Style
         :name: editorial-content-and-style

      Note: Validators should plan to make minor document changes
      directly to the document. Extensive changes should be reported
      back to the author using the appropriate JIRA ticket.

      .. rubric:: Basic things
         :name: basic-things

      #. Identify and correct typos, spelling, and grammatical mistakes.
      #. Confirm that all hyperlinks work properly.
      #. Does the content conform to common writing best practices (use
         of consistent tense, personal pronouns, etc.)?

      .. rubric:: Internal consistency
         :name: internal-consistency

      #. Throughout the text, please make sure that the following terms
         are used correctly (i.e., "MeasurementSet" is correct, not
         "Measurement Set"):

         -  MeasurementSet,
         -  Multi-MS,
         -  Sub-MS,
         -  MS,
         -  MMS

      #. If you are reviewing a Chapter, please make sure that links to
         subpages on the "front" page (where all of the subpages are
         listed) each contain a one-line description of that subpage's
         content. Links to the tasks and tools do not need this. For
         example, see the `Single Dish Calibration chapter front
         page <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/single-dish-calibration>`__.
         If the descriptions are missing, please add one.  

      .. rubric:: Document hierarchy
         :name: document-hierarchy

      #. Is the location of this document in the plone hierarchy
         sensible?
      #. Does the page fit in well with chapters that come before and
         after it?

      .. rubric:: Scientific/Relevant User Content
         :name: scientificrelevant-user-content

      .. rubric:: Completeness
         :name: completeness

      #. For validating pages in the Global Task List or Global Tool
         List, when you type "inp taskname" in CASA, is every parameter
         that is listed documented to the same extent in plone? Please
         refer back to CASA 4.7 to see the pre-plone-migration versions
         of the inline help files. Between the "Description" and
         "Parameters" tabs, are there adequate explanations for every
         parameter in the task?
      #. Has old, non-relevant text that refers to earlier CASA versions
         been removed?
      #. We need to compile references to specific tasks and tools in
         each Documentation Chapter, which should appear as links within
         the Chapter. These should already be set up, but if there are
         additional links that are necessary, please create them within
         the Chapter folder following the existing examples. 

      .. rubric:: Larger picture
         :name: larger-picture

      #. Does the documentation make sense from a CASA user's point of
         view? Is it complete?
      #. Has all information that is relevant been ported from the
         inline and online help (for tasks/tools) and CASA Cookbook (for
         chapters) to the plone page?
      #. If you are reading a task/tool page, are the examples relevant?
         Should there be more (or fewer) examples? Please make
         suggestions if you think something is missing.
      #. If you are reading a chapter, is the balance correct between
         the information found in the chapter text and that found linked
         in the relevant tasks and tools? Please make suggestions if you
         think something is missing. 

.. container:: section
   :name: viewlet-below-content-body
