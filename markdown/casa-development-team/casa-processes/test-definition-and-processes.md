

# Automated Test Definitions 

A comprehensive description of automated tests classes

\--CASA Developer\--

# Test Suite Definitions

## c++ Unit Tests

These tests are focused exclusively on verifying c++ code changes. These tests should be run automatically at each autonomously initiated compilation of the software. There should also be a capability to manually run these tests by a developer (particularly on their own local copy of the repo) on demand.

## Smoke Tests

These are very quick python level tests. They should not collectively run for more then a few minutes. These should be run following any automated initiated build on either the trunk (master repo) or any feature branch, following a successful completion of the c++ Unit Tests. There should be a capability to initate these manually on a developers own copy of the repo.

## Test Suite 1 (TS1)

Mostly consisting of slightly longer running python verification tests (compared to the Smoke Tests), and some validation tests. TS1 should be run anytime a developer commits a change to the Feature Branch (following the subsequent automated build, passing both c++ Unit Tests and Smoke Tests), or if an approved change in the trunk (master repo) has been pushed to the Feature Branch. These tests should have a total duration of a half hour or so.

## Test Suite 2 (TS2)

Before validation by the scientist on a feature branch, TS2 is run to ensure some rudimentry validation is good (roughly in line with a current Stable tarball). Should these tests fail, the JIRA ticket associated with it should no longer be \"Ready To Verify\", and the developer of the feature branch should be notified. These tests should run collectively for no more then an hour or so.

## Test Suite 3 (TS3)

TS3 consists of long running validation or regression tests that will exercise the python, as well as exercise the underlying c++. This may take a number of hours to run (though less then 12). This test suite will be run every couple of days, and only if there have been updates to the trunk (master repo). In principle these tests will have to all pass in order for there to be a new package created.

 

# Test Category Definition

## c++ Unit Tests

These are small scale tests which test parts of the c++ code. Unit tests declared in the module level CMakeLists.txt file are built and executed as part of the commit level builds. There is documentation available on how to do this in CASA here: <https://safe.nrao.edu/wiki/bin/view/Software/CASA/CasaInterimUnitTesting>. This goes in to more detail on these particular tests. Also, the current status of the latest c++ unit test runs can be seen here: <http://www.aoc.nrao.edu/~jjacobs/casaCodeTestDefinitionsStatus.html>. This table can be broken down by: first column (Tests) is number of unit tests known to the build system, the second (Legacy) is the number using the legacy (old, unused) tests, third column (Current) are those units tests using the new macros (and are live), and the final column is the ((number of current tests)/(total number of tests))\*100. Or, the third column, divided by the first column times 100. Ideally we want the last column to be unity. 

## Functional Tests

Functional tests are typically small tests collected under a single larger executed test. It can return a true or false result for each constituent test. These usually focus on basic functions (typically a level below tasks, but not always). 

## Regression Tests

### Legacy Regression Tests

This covers all those regression tests that are currently in place, and a single test returns a single true or false, depending on its passing or failing.

### CASAGuides

Several tests in the framework are actively created based on the maintained [CASA guides](https://casaguides.nrao.edu/index.php/Main_Page), both for ALMA (<https://casaguides.nrao.edu/index.php/ALMAguides>) and the EVLA (<https://casaguides.nrao.edu/index.php/Karl_G._Jansky_VLA_Tutorials>). They tend to run long, but provide very high level results on the health of the code.

### Parallel Processing Tests

These are the tests specifically designed to exercise the high performance computing infrastructure in CASA. Ideally they exercise multiple processors across nodes in a cluster. This is not to be confused with tests which may test features that take advantage of parallel processing, as these tests are focused on the parallel processing infrastucture. The following [section](https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/testing-using-multi-ms) explains how to create Multi-MS for tests and how to execute them.

### Pipeline Tests 

Having pipeline installed is a prerequisite for these tests. Beyond that, these tests exercise the heuristics found in pipeline, in addition to making sure pipeline is working in that particular version of CASA. 

Page that defines which tests fit in to which Test Suites: <https://safe.nrao.edu/wiki/bin/view/Software/CASA/ContinuousIntegrationTestDiscussionForBamboo>

