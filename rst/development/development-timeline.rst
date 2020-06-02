Development Workflows
#####################

Real-World projects are not managed by one developer, except in those cases
where that developer is working alone on some pet project (like me!) MOst
projects are team efforts, meaning many developers are working on the same code
base at the same time. This could lead to chaos, if the code base is not being
managed somehow.

Modern source code management tools like Git_ provide the management tools
needed, but do not impose a management methodology on the team. Instead, each
team adopts some approach to dealing with merging work done by each developer
into the "master" copy of the code base. 

Let's start off with a single developer creating a project and talk about the
changes made to the code base.

Project Setup
*************

Development always begins (or it should) with setting up a work area and
creating a Git_ repository to manage the work:

..	code-block::	shell

	$ mkdir new-project
	$ cd new-project
	$ git init

At this point, we have an empty workspace, and a hidden **.git** directory that
will be used by Git_ to track work done on the files living in this directory.

Timelines
*********

Development happens over time. A developer sits down at a workstation and
creates something related to the project. That something may be source code, or
it may be documentation. At the end of that session, the changes to the code
must be recorded. This is easy with Git_. 

What Changed?
=============

The developer can run:

..	code-block::	shell

	$ git status

What will be displayed is a list of all files changed by the work session. That
will include new files created, files deleted, and files modified 

Staging Changes
===============

Next, the developer "stages" those changes by doing this:

..	code-block::	shell

	$ git add .

The dot at the end of that command tells Git_ to include all changes found in the project to the staging area. In effect, this command sets up a new version of the code base. The old version is not modified in any way, only the changes are in the staging area now.

Commit Changes
==============

This is the big step. We now decide to create anew version of the code base, incorporating all of the modifications present in the staging area. Git_ will record new versions of all new or modified files, and delete references to deleted files from its bookkeeping records. When the smoke clears, Git_ will know what makes up the new, current, version of the code base. 

All of this happens at some momen tin time, and the commit marks that moment. If we are unhappy with this new version, we could "back-up" to a previous point in time, to a previous commit, and restore our working copy to the state it was in back then. This is a powerful tool for fixing silly work that never should have been there in the first place.

Pushing Changes
===============

There is a ifnal step, that is really optional at this point.

If the developer has a "master copy" of the code base, living on a server like Github_, the new version created by a commit should be "pushed" to theat server. 

..	code-block::	shell

	$ git push origin master

This command is confusing to beginners. The "origin" is an alias for the remote server, Github_ in this case> The "master" refers to the developers working copy of the project code. 

Branches
********

Git_ makes it easy to create a *branch* in the development timeline. For a
single developer, a branch represents the start of work on an idea that may, or
may not, make its way into the code base at some point. The assumption is that
the main code base is in good shape, and we do not want our experiment to mess
that up. If we like the results of our experiment, eventually we will "merge"
that work into the main code base. If we do not like the results of our
experiment, we can simply stop work on that branch and try something else. The
abandoned work could be thrown out, or just left sitting there for future
reference.

What 
