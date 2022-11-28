Introduction
============

It is necessary to have a way to track progress of all projects or processes. This document describes the
documentation process for CASA sub-projects that deviate from the standard spiral methodology in a more
"*agile*" direction. The primary goal of this documentation is to document as little as possible while
still providing enough information for someone who is knowledgeable about the project to be able to
understand the current status. All documentation should be written with the expectation that it will
be processed by `Sphinx <https://www.sphinx-doc.org/en/master/>`_.
`Restructured text <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ is preferred.

Terminology
===========

All development tracking is accomplished using GitHub
`projects <https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects>`_ and
`issues <https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues>`_. Each major area
of work will have a separate project within the CASA organization on GitHub. These major areas of work include
things like visualization, infrastructure, calibration, etc. Labels added to each issue within projects
determine the role of a specific issue plays in the project management process. The labels we use are:

story
-----

Work to be done which has impact for users. This may mean that it changes the public interface or it may mean
that a new feature is added. The description included in this ticket should be written from a user's perspective,
and it should be brief (a paragraph to a few paragraphs). This should be a work packet that takes one
to two weeks of full time effort for a single person. More people could be involved, but this should be roughly the
total amount of work described by a single story. **The story description is owned by developers who are working on
the story**. They create it based upon their understanding of the issue and describe the situation from the
perspective of a user. Stories have code reviews and go through a standard verification and validation process
before being merged to the main branch of the project's repository. The story's description should typically be
the documentation that will be copied to `casadocs <https://casadocs.readthedocs.io/en/latest>`_ when the change
is merged.

epic
----

Like a *story*, an issue labeled as an *epic* has an impact on users. However, an epic's impact is much greater
because it involves much more effort. Typically an epic should involve a month or more of work by a single developer
working full time on the epic. More than one developer is likely to work on an epic but a single developer's effort
is used to gauge the sizing of epics VS stories. The division between an epic and a story is somewhat subjective.
Epics are composed of stories and issues (but not other epics). The epic description should be written from a user's
perspective. It should document the new feature in a manner that allows users to use the features developed
as part of the epic. The epic description should can be easily transfer to
`casadocs <https://casadocs.readthedocs.io/en/latest>`_.

**The epic description is owned by the epic owner**. The epic owner represents the user's perspective and are
not involved in the development of the features which the epic implements. The owner writes (and updates) the
description and provides the final word on stories and issues which constitute the epic. When it is time to
merge the epic into the main branch for the sub-project, the epic owner coordinates with the standard
verification and validation process either when the entire epic is merged to the project's main branch or
when individual pieces are merged over time. This coordination will determine how much (if any) validation
is required based on the validation completed as part of the epic's development.

issues
------

All of the project's GitHub `issues <https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues>`_
which do not have an **epic** or **story** label are assumed to be *not user facing*, i.e. they do not affect
the public API. These can be labeled  with other labels to assist with release planning and sorting and
searching by developers. These issues which are not tagged as an epic or a story have a code review, but
they are not validated, except to the extent that they are validated by an **epic owner** when they are a
constituent part of an epic. The typical verification that is done for these is the standard, automatic
verification, but additional verification can be done when needed.


