

# Revision Control Using git 

Instructions on how to use git for revision control

\--CASA Developer\--

# Introduction

The CASA development group uses Bitbucket for revision control. Under the hood, Bitbucket employs git but is also integrated with JIRA, Bamboo (for continuous integration), and Confluence (wiki-like documentation).  This article explains the basics of revision control using BitBucket and git. For information on advanced BitBucket options, look for the question mark icon from any screen in the BitBucket web interface. Advanced information on git is widely available on the Web. The description below is for following the default workflow with the simplest command use.

# 1. Clone the repository: git clone

To do CASA development, you will need to get a copy of the CASA repository on your local machine. In the git revision control model, you will make a \'clone\' of the repository on the BitBucket server. The clone is effectively a local \'working copy\' of the code with its own git repository and a remote connection called \'origin\' pointing back to the original Bitbucket repository. You can edit files and commit changes in your cloned copy, then periodically push committed changes back to origin as well as pull changes from origin to the local repository.

To clone the repository:

```
git clone --recursive https://open-bitbucket.nrao.edu/scm/casa/casa6.git
```

You now have a local copy of the repository and a \'working tree\' of code on which you can do your work. You can run simple commands to get information about your local repository:

```
cd casa6
git branch
git status
git log
```

*git branch* lists the branches in the local repository, with the active branch indicated by **\***. After cloning, you will have only the master branch. *git status* indicates the active branch then lists the files which are *staged*, *unstaged*, and *untracked* (see section on [committing changes](#3--commit-code-changes--git-status--git-add--git-commit) below). *git log* lists the commits in the active branch with the commit ID, author, date, and message.

<div class="alert alert-info">
**NOTE**: Log output is paged automatically and does not need to be piped to a command such as \'more\'.
</div>

 

# 2. Create a new branch: git checkout

<div class="alert alert-warning">
**ALERT**: Never develop on the master branch!
</div>

It is possible to create a branch in your local git repository and push it to origin, but you can also create the branch from JIRA.  Work should be done on a separate branch for an individual ticket or a group of tickets. To create the branch for your work:

1.  Start from the appropriate JIRA ticket.
2.  Click \"Create branch\" in the development section to the right. This will take you to the Bitbucket Create Branch form.
3.  Use the default repository casa/casa, select branch type Custom (no prefix) and branch from the default \'master\' unless you will be patching the release branch. Set the branch name to the JIRA ticket number (e.g. \"CAS-1234\").
    <div class="alert alert-info">
    **IMPORTANT**: The default name includes the ticket\'s title but use the ticket number only**;** delete everything after the ticket number so that the CASA build and test process works properly. You can also create branches that do not start with \"CAS-\" prefix. Those branches will not trigger the standard build tests. An exception to this is the pull request build and test which will run regardless of the branch name. If you have an urgent and sufficiently independent change (f.e. unit test bug that only showed in master) you can create a branch with \"hotfix/\" prefix. This will bypass most of the automated tests but will still run the standard pull request build and test suite.    
    </div>
4.  Click \"Create Branch.\"

Now you need to add the new branch to your local repository so that you can begin using it. In your local repository, use the *git checkout \<branch\>* command to switch to a different branch. If the branch is not in the local repository, git will automatically look for it in origin, add it to your local repository, and track it with the same branch in origin (for [push](#push-changes-to-origin) and [pull](#pull-changes-from-origin--update-your-local-repository-)).

```
git fetch origin
git checkout CAS-1234
git branch
```

First use *git fetch origin* to update the list of remote branches. Then use *git checkout* to switch to the new branch. You can use *git branch* to verify that you now have the requested branch and that it is the active one.  Now you are ready to develop on your branch.

For more information about checking out new or existing branches, see the section on [git checkout](#7--switch-branches).

 

# 3. Commit code changes: git status, git add, git commit

<div class="alert alert-warning">
**ALERT**: Remember that git status and git commit act on your local repository only!
</div>

After you have edited existing files or added new ones, you may want to commit the changes to your repository. In other revision control systems, the commit command adds all of the modified files in your working directory to the repository.  In git, you can select files to be committed together. For example, if you have three modified files in your repository that implement a bug fix and a new feature, you can commit two files for the bug fix separately from the third file for the feature. Therefore, the commit is actually a *changeset*, all of the files that implement a specific change. If the commit is unsuccessful because there is a conflict between one of your modified files and the repo version, the changeset fails rather than committing some files but not others.

First, you need to know which files have been changed or added. Use *git status* to list the files that differ from your local repository. These files can have three states: *staged, unstaged,* and *untracked.* In addition, git status lets you know if the files are modified or new.

#### staged: \"Changes to be committed\"

These files are tracked by git and have been added to the staging area with *git add*. Using *git commit* will add these changes to the repository. If you change your mind and do not want to commit a file yet, the *git status* output includes the git command to unstage a file: *git reset HEAD \<file\>*.

#### unstaged: \"Changes not staged for commit\"

These files are tracked by git and are modified but will not be committed with the next *git commit****. ***Perhaps this is what you want, as the files are not ready for commit or you do not want them in the next changeset. Again, the *git status* output includes the git commands to change the file\'s status: use *git add \<file\>* to add the files to the staging area, or use *git checkout \-- \<file\>* to discard the changes and go back to the repository version (revert). 

<div class="alert alert-info">
Note the double-minus after this *git checkout* command, which indicates the argument is a file not a branch.
</div>

#### untracked: \"Untracked files\"

These are files that git does not know about. They could be new code files, artifacts of building or testing your code, swap files if you have files open for editing, etc. If you want to add the file to the git repository, simply use *git add \<file\>*.

#### Nothing to commit

As you would expect, the files which match the repository version are not listed in *git status*. If all files in the working directory match the local repository and there are no untracked files, *git status* will return the message \"nothing to commit, working directory clean\".

Sample commit session:

1.  Edit file1, file2, and file3, and add file4. You want to commit file1 and file2 together as one changeset, then commit file3 and file4 as a separate changeset.
2.  *git status** *** \# indicates that file1, file2, and file3 are *unstaged* (\"Changes not staged for commit\"), and file4 is *untracked* (\"Untracked files\").
3.  *git add file1 file2*   \# *stage* files for first changeset
4.  *git commit** *** \# puts you into an editor for the commit message, with a list of files to be committed
5.  *git status** *** \# indicates that file3 is *unstaged*, file4 is *untracked*
6.  *git add file4*  \# add file4 to the files tracked by git; file4 is now *staged*, file3 is *unstaged*
7.  *git commit -a** *** \# commits all modified files (*staged* and *unstaged*), in this case file3 and file4. Alternatively, you could use git add file3; git commit.

Remember that unlike a centralized revision control system such as svn, *git commit* saves the changes to your local repository only. The origin is unchanged until you use [git push](#4--push-changes-to-origin).  In addition, the changes are committed on this branch only; if you [switch branches](#7--switch-branches), *git log* will not show this commit.

## 3.1 Remove a file from git

<div class="alert alert-warning">
**ALERT:** *git rm* removes the file from your repository AND your working tree!
</div>

Perhaps you are pruning deprecated code from your code tree, or you accidentally added a new file to git. git lets you remove a file with *git rm \<file\>*.

1.  You want to remove a tracked file. Simply use *git rm \<file\>* to let git know that you want to delete this file from the repository; the file will be *staged* in *git status* as \"Changes to be committed\" with the label \"deleted\". Use *git commit* to complete the removal.
2.  You added a new (untracked) file with *git add* (now it is *staged* with the label \"new file\"), but you do not want it. Simply use *git rm* *\<file*\>. You do not need to commit this time.

Remember, *git rm* doesn\'t just untrack the file, it removes the file from your directory! However, like all commits, the removal of a tracked file is on the active branch only; if you [switch branches](#7--switch-branches), the file may be restored in the new active branch.

## 3.2 Compare your repository to origin

Remember, *git status* reflects the state of your working tree with respect to your local repository.  Let\'s say your working directory has \"nothing to commit\", so all of your code changes have been committed.  But what is the status of your repository compared with origin?  Remember that for tracked branches *git status* will tell you if you are ahead or behind the remote branch, for example:

```
<div>

$ git status

</div>

<div>

On branch master

</div>

<div>

Your branch is behind 'origin/master' by 3 commits, and can be fast-forwarded.

</div>

<div>

  (use "git pull" to update your local branch)

</div>

<div>

nothing to commit, working directory clean

</div>
```

In this example,there are 3 commits in origin/master that are not in your local master branch.  You are helpfully told to use *git pull* to update your branch, but you may want to see what you would get before you do the pull and possibly postpone this step until later.

1\. Fetch the remote (origin) to update your references.  You may want to run *git status* again to see if the information changes.

```
$ git fetch origin

$ git status
```

2\. Use **double-dot notation** to see what commits are in your branch but not in master (what you would push):

```
$ git log origin/master..master
```

3\. Use **double-dot notation** to see what commits are in master but not in your branch (what you would pull):

```
$ git log master..origin/master
```

4\. If you are on the branch you want to compare, you can leave that part out:

```
$ git log origin/master..

$ git log ..origin/master
```

5\. To do it all at once, use **\--left-right** with **triple-dot notation**.  The commits with \'\<\' refer to the branch listed first, to the left of the triple-dots, and \'\>\' refers to the branch listed second, on the right.  The following example shows that F and E are only on origin/master, and D and C are only on the local master.  These letters represent git log entries with commit ID, author, date, and message.

```
$ git log --left-right origin/master...master

< F

< E

> D

> C
```

# 4. Push changes to origin: git push

You have changed your code and committed changes, but these changes are in your local repository only. When you are ready to save your code changes in the remote repository, use *git push \<remote\> \<branch\>* to update the branch in origin.

Pushing changes to origin trigger a CI build and level 1 test of your branch by Bamboo. Make sure the CI plan is successful before changing your JIRA ticket status to \"Ready to Verify\" or \"Ready to Validate.\"

1.  Make sure you are on the branch you want to push: *git branch*
2.  If not, check out the desired branch: *git checkout \<branch\>*
3.  Push committed changes to origin: *git push origin \<branch\>*
4.  You may be prompted for your username/password for Bitbucket.
5.  A message is returned indicating whether the push was successful.

 

# 5. Pull changes from origin (update your local repository): git pull

If you think a branch has been updated in origin, by another developer on the development branch or by pull requests or casacore updates on the master branch, you can merge these changes to your local repository with *git pull \<remote\> \<branch\>*.  This command is shorthand for *git fetch origin* then *git merge \<branch\>*.

1.  Make sure you are on the branch you want to pull:  *git branch*
2.  If not, check out the desired branch:  *git checkout \<branch\>*
3.  Pull changes from origin:  *git pull origin \<branch\>*
4.  This updates the commits in the log:  *git log*

 

# 6. Make a pull request (merge changes to the master or release branch)

When your JIRA ticket is Resolved, you can merge your branch into the master branch on the Bitbucket server by creating a pull request. If some time has passed since you created the branch or merged master into it, you should update the branch before the pull request as shown in [this section](#update-branch-with-master-and-submodule-changes) , push to origin, and let the CI and Branch Package plans run in Bamboo.  After the branch package and tests are successful, you must initiate a pull request to inform the reviewers that your branch is ready to be merged into the master branch.

In the JIRA ticket, there is a \'Development\' section on the right, which lists branches, commits, and builds. Click on the \"branch\" link, which will open a list of the branches created from the ticket (most likely only one). For the branch you wish to merge, click \"Create pull request\" in the \'Action\' column.

Complete the Bitbucket \"Create pull request\" form, which already has the branch name as the Title and commit messages as the Description.  If the ticket requires release notes for this change, add a \"Release Notes:\" section at the end of the Description.

You can also add \"Tools:\" and \"Tasks:\" segments after \"Release Notes:\". These should contain a list of tasks and tools that are affected by the pull request.

So the layout of the pull request is:

    General pull request information

    Release Notes:

    Everything after release notes is included in the plone documentation.

    Tools: tool1, tool2

    Tasks: task1, task2

<div class="alert alert-warning">
Review the **Diff** and **Commits** tabs at the bottom to ensure that only your changes are listed.  If other files are included, you may be reverting others\' code changes from your outdated branch.  It is easier to fix this now than after the branch is merged into master!
</div>

Click \"Create\".  You may also \"Cancel\" if you need to fix something after your review.  Once the pull request is created, Bamboo will launch the PR Build plan, which checks out master, merges your branch into it, builds it, and runs a test suite.  The pull request reviewers will generally wait until this test completes before approving and merging your pull request.  Please be patient, as these tests can take \~10 hours to run.

Once the pull request is approved and merged, the workflow is complete and your ticket\'s status can be changed to \"Complete\".

If a pull request is approved and merged but the master test suite fails due to your change,  you will need to create a new ticket to fix the failing test. In extreme cases **your pull request may be reverted** in a new pull request, in order to restore master to a good state.  Your pull request is reverted as a whole, not just the part that caused a test to fail.  To reapply these changes:

-   Make a new ticket and branch for the fix
-   Find the commit ID of the **reversion** pull request using *git log*.
-   Run *git revert \<commit ID\>* to reapply the changes in your first pull request.
-   Add your fix, commit, etc., and create a new pull request when the builds and tests succeed.

 

# 7. Switch branches: git checkout

The normal workflow is to work on one ticket at a time until completion as detailed above, but it could happen that you need to switch to another task before it is done. Examples include: (1) a more urgent bugfix comes up that needs your immediate attention; (2) input is required before further progress can be made, so you want to begin work on another issue; or (3) you need to update from master before continuing. In these cases, you will want to switch to another branch.

#### Checkout with clean working directory

To make a different branch active, simply use* git checkout*, as you did with the new branch above:

```
git status  # working directory clean
git checkout CAS-1245
```

If the branch is already in your local repository, git will make it the active branch. If not, git will find the branch in the origin, add it to the local repo, and switch to it. The switch happens instantly if your working directory is clean (\"nothing to commit\", as explained in the [section on commit](#commit-code-changes)). Some source files will probably change with this branch change, so you may want to recompile your code to make a new build.

The checkout may change to a different casacore reference, so it is good practice to run *git status* after a checkout to see if casacore is modified.  This means that the code in the casacore code tree does not match the casacore reference stored in the branch.  To sync the code tree with the reference, use *git submodule update*:

```
git status

     modified: casacore (new commits)

git submodule update  # now code contains new commits in casacore and matches the reference
```

However, if the active branch has an older version of casacore, you may want to [merge master](#update-branch-with-master-and-submodule-changes) to update it rather than revert the code.

#### Checkout with dirty working directory

If, however, you do have modified files in your branch (the working directory is \'dirty\'), git will return an error such as:

```
error: Your local changes to the following files would be overwritten by checkout:
      code/file1
Please, commit your changes or stash them before you can switch branches.
Aborting
```

Along with the error, git gives you the helpful advice to [commit](#commit-code-changes) your changes or [stash](#stash-changes) them.  After running one of these commands, you have a clean working directory and can proceed with the checkout as shown above.

# 8. Stash changes: git stash

What if you need to save changes but they are not ready to commit? This could happen if you want to switch branches but you have modified files, if you want to try an alternate approach but be able to retrieve the current implementation later, or you want to apply the changes to another branch instead. You can use *git stash*.

*git stash* stores a record of the current state of your working directory on a stack, then reverts the working directory to a clean state (the last commit). To see the stashes you currently have, use *git stash list* which shows the stash name (stash@{0}, stash@{1}, etc., with 0 being the top), the branch you were on when you stashed, and the last commit the stash is based on (i.e. what your working directory was reverted to).

To retrieve your changes, use *git stash pop \<stash\>** ***(apply the changes and remove the stash from the stack) or *git stash apply \<stash\>* (apply the changes and leave the stash on the stack). If the stash argument is not used, git pops/applies the top of the stack.  Notice that there is one stash stack for all of the branches in the repository and you apply the changes to the current active branch. Therefore you can pop the stash to the same or a different branch than it came from; this may or may not be what you intended so be careful. Popping the stash could result in conflicts when the changes are applied.

#### Sample git stash session

```
git checkout CAS-1234
vi file1.cc
git stash  # file1.cc changes go on stack, file1.cc is reverted
git checkout CAS-1235 # develop and commit on another branch
git checkout CAS-1234 # with this branch's repo version of file1.cc
git stash pop  # get modified file1.cc back, continue work
```

<div>

 

</div>

# 9. Update branch with master (or another branch) and submodule changes: git merge

Before a pull request, you should update your branch to check for conflicts and build errors, which should be resolved locally. This involves merging an updated local master into the local branch.

<div class="alert alert-warning">
**ALERT**: Remember that the active branch is the one being changed!
</div>

#### Sample session to merge master and resolve conflicts

Start with a clean working directory in the branch you are working in; if it is not, commit or stash your changes.

```
git checkout master
git pull origin master
```

At this point, running *git status* may indicate that casacore is modified and not staged for commit, perhaps with new commits. To resolve this, run

```
git submodule update
```

to get your master branch on track. Then continue in your development branch:

```
git checkout CAS-1234
git merge master  # this merges master into CAS-1234, including casacore reference
    
# To resolve conflicts
vi file1  # edit file with conflicts
git add file1
git commit -a

git submodule update # if casacore is modified by merge
git push origin CAS-1234 # if you want to update the branch in origin
```

<div class="alert alert-info">
**NOTE**: You may follow this procedure at any time in your local repository (with the optional final push), in order to work with updated code while developing your branch and to handle potential merge conflicts.

You may also follow this procedure to merge any branch (not just master) into any other branch as needed.
</div>

For updates to the casacore submodule, [section below](#when-a-feature-requires-both-casacore-and-casa-change).

 

# 10. Delete the branch from your repository (optional): git branch -d

This step is not required by the workflow, but is something you will probably want to do once your work on the branch is complete, i.e. the pull request has been done and the JIRA ticket is Complete. Otherwise, the list returned by *git branch* will get mighty long. Deleting a branch is easy, and should you find you need the branch again, you can always get it from origin with *git checkout*.

1.  Make sure you are not on the branch you want to delete, e.g. *git checkout master.*
2.  Delete the branch, *git branch -d \<branch\>*. If git complains that the branch was not fully merged, you can use -D to force the delete.
3.  Use *git branch* to verify that the branch is no longer listed.

#  

# 11. When a feature requires both casacore and casa change

 

1\. Create a Casacore fork in GitHub

2\. Create a Casa branch in BitBucket

3\. Clone the repository and checkout your branch

`git clone --recursive https://open-bitbucket.nrao.edu/scm/casa/casa.git`

`cd casa`

`git checkout CAS-1234`

4\. Create a casacore branch

`cd casacore`

`git checkout master`

`git pull`

`git branch mycasacorefeature`

`git checkout mycasacorefeature`

5\. Make your changes in casacore

6\. Make your changes in the rest of the branch

7\. Test locally

8\. Push the Casacore changes to your fork in GitHub

`cd casa/casacore`

`git remote add mycasacore https://github.com/vsuorant/casacore`

`git push mycasacore mycasacorefeature`

9\. Create a pull request in GitHub

10\. Wait for the pull request to be applied (you must wait since the master submodule doesn\'t know about your fork, so you can\'t point the submodule there)

11\. Update the submodule reference in your branch

`cd casa `

`git checkout CAS-1234`

`cd casacore`

`git checkout master`

`git pull`

`cd ..`

`git add casacore`

`git commit --amend (this will amend your latest commit. If you would rather have a separate commit, leave the --amend out)`

12\. Push your changes to BitBucket

`git push origin CAS-1234`

 

# 11.1 Switching Casacore remotes and branches

Sometimes you need or want to add more remotes for Casacore changes. To add a remote do:

    git remote add mycasacore https://github.com/vsuorant/casacore

If you want to make your casacore master \"track\" the master in the new remote, do the following:

    git fetch mycasacore

    git checkout -B master central-casacore/master

#  

# 12. Creating a patch for both release and master branches

#### Option 1: Branch both master and release

1\. Create a branch from release/\<version number\> with your Jira ticket number.

2\. Make your changes and push the branch to Bitbucket for testing.

3\. Create another Jira ticket to backport the changes to master, branch from master using the new Jira ticket number, copy your changes there and push to bitbucket for testing.

4\. Create pull requests from both branches.

#### Option 2: Create single branch that is mergeable to both master and release

When creating a patch that can be applied in both the master and prerelease (or any other branch), it is useful to find the last common ancestor of the branches. Using the common ancestor will prevent unwanted changes from getting applied from one branch to another. Use the following steps to create a branch that can be applied in both branches.

1\. Find the last common ancestor and create a branch based on it.

    git checkout -b bugfix/myjiraticket `git merge-base origin/release/5.0.0 origin/master` 

2\. Commit your changes to your bugfix branch and push your branch to Bitbucket.3. Wait for all of the build/test tasks to complete.4. Create a pull request to both release/5.0.0 and master`. `

 

 

