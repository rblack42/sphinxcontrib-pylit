Project Setup
#############


Step 1: Pick a project name
***************************

This project provides a Sphinx_ extension that supports a form of Knuth's |LP|.
Most Sphinx_ extensions are created in the **sphinxcontrib** namespace, so this
project name will be **sphinxcontrib-pylit**.


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

    The creates a hidden **.git** directory used by Git_ to manage your project.

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
the set of files we will maintain on Github_. The lines in this file identify
file patterns and directories to ignore.

..  literalinclude::   /_examples/gitignore-01
    :caption: .gitignore

PyPi_ Setup
***********

This project will be released on PyPi_ which is where most Python public
projects are found. In order to use the standard **pip** tool to install this
project package, we need to add a **setup.py** file and tweak our
**.gitignore** file.

..  note::

    These steps are detailed in `Minimal Structure`_. You must also register on
    PyPi_ to use their system.

Here is a start on the **setup.py** file:

..  literalinclude::   /_examples/setup-01.py

With this file in place, we can register the project on PyPi_ and make sure the
project name is available. PyPi_ now uses a new tool, **twine** to manage
uploading projects. Here are the commands use to set things up:

..  code-block:: shell

    $ pip install twine
    $ python setyp.py build sdist bdist_wheel
    $ twine upload -r testpypy dist/*

This uploads the project tot he **testpypi** website. If things look good
there, we can do an "official" upload as follows:

..  code-block:: shell

    $ twine upload dist/*

Once you complete this step, your project is properly registered on the PyPi_
system and users can use **pip** to install the project code.

Finally, we need to add a few more settings to the **.gitignore** file to keep
directories used in  publishing the project on PyPi_ out of our repository:

..  literalinclude::    /_examples/gitignore-02
    :caption: .gitignore

Now, we are ready for some testing work!
