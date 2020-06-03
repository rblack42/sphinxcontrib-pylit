Development Workflows
#####################

Real-World projects are not managed by one developer, except in those cases
where that developer is working alone on some pet project (like me!) Most
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

The dot at the end of that command tells Git_ to include all changes found in
the project to the staging area. In effect, this command sets up a new version
of the code base. The old version is not modified in any way, only the changes
are in the staging area now.

..  note::

    You can control what gets added to the staging area by specifying files to
    be staged instead of using the dot in the obove command.


Commit Changes
==============

This is the big step. We now decide to create anew version of the code base,
incorporating all of the modifications present in the staging area. Git_ will
record new versions of all new or modified files, and delete references to
deleted files from its bookkeeping records. When the smoke clears, Git_ will
know what makes up the new, current, version of the code base. It will mark the
new version using a hash tag, and record the current time and who made this
commit.

All of this happens at some moment in time, and the commit marks that moment.
If we are unhappy with this new version, we could "back-up" to a previous point
in time, to a previous commit, and restore our working copy to the state it was
in back then. This is a powerful tool for fixing silly work that never should
have been there in the first place.

Pushing Changes
===============

There is a final step, that is really optional at this point.

If the developer has a "master copy" of the code base, living on a server like
Github_, the new version created by a commit should be "pushed" to that
server.

..	code-block::	shell

	$ git push origin master

This command is confusing to beginners. The "origin" is an alias for the remote
server, Github_ in this case. The "master" refers to the developer's working
copy of the project code.

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

Using branches may seem like an unnecessary thing to the lone developer, but in
a team setting it is a powerful tool. It also causes problems in managing that
"merge" moment.

Merging
=======

The idea of the merge seems simple enough. All we want to do is record our branch
code back in the main code. However, that main code may have been modified by
someone while we were working on our branch. When we try to merge there might
be different versions of the same file in the proposed new code base. This is
called a "conflict". Git_ will not try to deal with this problem. Since humans
caused the problem, humans can fix the problem!

Exactly who does the conflict resolution and how is something that leads to
different management styles for different teams. Usually, some lead developer
will be assigned the responsibility for sorting out the mess and making things
smooth again!

Martin Fowler has a nice article on this issues available here:
:cite:`Fowler:2020`

Viewing the History
*******************

Git_ provides several ways to view the timeline of a project. The easiest to
use is just this:

..  code-block::    shell

    $ git log

This will display every commit made on the current branch along with the
message recorded on that commit and who made the change to the code base. This
is not the nicest view of the timeline, though.

Try this instead:

..  code-block:: shell

    $ git log --graph --oneline --decorate

This is more useful when you want a view of the timeline itself.

|LP| and Timelines
******************

One of the goals of this project is to provide a tool that can be used to help
new software developers learn the habits they will need when they start work on
real projects. That means teaching students not just how to put together
correct syntax that can get through the compiler, but also how to use the tools
of the trade effectively to manage their work. They need to learn about
programming editors, documentation tools, code processing tools, and testing
tools. Oh, and Git_! (At least until Git_ falls from dominance!)

How can |pylit| help with that?

Editing
=======

I show my students how to use Vim on their machines. Not to start a flame war,
but Vim is a good choice for beginners, since it can be found almost
everywhere, and can easily be installed on machines that do not provide it
natively (Windoze!). These notes will show Vim, but |pylit| is not tied to that
editor.

|pylit| assumes that the user is comfortable with some editor that can produce
simple code files. That editor can be customized as the user wishes. As long as
the final product is a simple text file (well, maybe encoded into Unicode)
|pylit| can process the resulting file.

All input files will be written in standard |RST| using extensions provided
through Sphinx_. The user should be able to get Sphinx_ running, and be able to
add the :py:mod:`sphinxcontrib-pylit` extension.

When |pylit| process any input file, it creates a hash for that file and
records it in the data store. If the file has previously been submitted and has
not been modified, no processing will occur. If it has been modified, or is
new, |pylit| will break that file into basic blocks and store those in the data
store. |pylit| manages those blocks, not the original files that provided them.
Users can copy and paste sections of text between input files with no
restrictions. |pylit| will see that when it hashes the blocks, and eliminate
excessive processing as it produces its final output products.

..  note::

    No input file will be harmed by submitting it to |pylit|!

Managing the Timeline
=====================

|LP| seems to assume that the product being documented is the final version of
some piece of software. That may have been Knuth's intent, but the goal of
|pylit| is to document the software and the process that led to that final
version. Of course,, to paraphrase da Vinci, "Software is never really
finished, only abandoned!" :cite:`DaVinci:2020`

