Project Setup
#############

..	include::	/header.inc

Step 1: Pick a project name
***************************

This project provides a Sphinx_ extension that supports a form of Knuth's |LP|.
Most Sphinx_ extensions are created in the **sphinxcontrib** namespace, so this
project name will be **sphinxcontrib-pylit**.

..	note::

    There are several packages listed on PyPi_ with **pylit** in the name. I
    first used this name in 2003 as part of my Computer Science Master's Thesis
    project at Texas State Uniersity, and I registered the **pylit.org** name
    in 2005 :cite:`black:2005`. If this causes confusion, I apologize to the others trying to
    build similar systems.

Step 2: Create Project Directories
**********************************

We begin work on this project by setting up a simple file structure:

Package Structure
=================

We create an empty Python package for the project as follows:

..	code-block:: shell

	$ mkdir -p sphinxcontrib-pylit/sphinxcontrib/pylit
	$ cd sphinxcontrib-pylit
	$ touch sphinxcontrib/__init__.py
	$ touch sphinxcontrib/pylit/__init__.py

The last two commands create empty **__init__.py** files to identify these
directories as *packages* for Python.

Project Documentation
=====================

We will be documenting this project using Sphinx_ and hosting the documentation
in Github_. The setup I use to do this places all Sphinx_ source files under a
**rst** directory, and the output HTML files are generated in a **docs**
directory. This makes publishing the final HTML files on Github_ very simple:

..	code-block:: shell

	* cd sphinxcontrib-pylit
	* mkdir rst
	$ mkdir docs
    $ touch docs/.nojekyll

That last line stops github_ from trying to process our web pages using Jekyll.

Project Testing
===============

Next, we will be testing the code as it is developed using pytest_. All test
code will be placed under a **tests** directory.

..	code-block:: shell

    $ mkdir tests

Step 3: Git_ Setup
******************

I recommend Git_ as your *source code contro* system, and Github_ as the server
to host your public view of the project code. I have long used these free
tools my Computer Science classes.

Local Git_ setup
================

Begin by placing this project under Git_ management. From the project root
directory, do this:

..  code-block:: shell

    $ git init

    The creates a hidded **.git** directory used by Git_ to manage your project.

Standard Project Files
======================

It is traditional to set up a few basic files in the project root directory.
Here are the files I always set up:

README.rst
----------

This file will appear on Github_ when visitors browse your project. At the very
least, it should provide some basic information about the project.

..  literalinclude::    /_examples/README-01.rst
    :caption: README.rst

.gitignore
----------

The **.gitignore** file keeps files we do not want to track with Git_ out of
the set of files we will maintain on Github_. The line sin this file identify
file patterns and directories to ignore.

..  literalinclude::   /_examples/gitignore-01
    :caption: .gitignore

PyPi_ Setup
***********

This project will be released on PyPi_ which is where most Python public projects are found. In order to use the standard **pip** tool to install this project package, we need to add a **setup.py** file and tweak our **.gitignore** file.

..  note::

    These steps are detailed in `Minimal Structure`_.

Here is a start on the **setup.py** file:

..  literalinclude::   /_examples/setup-01.py
