Configuring Testing
###################


Testing is one of the most important things you can do in developing software.
For a serious project, there are a number of excellent tools available to make
sure you produce high-quality code.

In this project we will use a few popular development tools you might not have
tried before:

    * Unit testing with pytest_.

    * Check test coverage with pytest-cov_

    * Run tests on Linux and Mac using Travis-CI_

    * Run tests on Windows using Appveyor_

    * Check code quality with codeclimate_

    * Test automation with Tox_

All of these systems provide free support for open-source projects. However the
setup to get all of this working is a bit overwhelming for beginners. We will
work through the steps in detail here.

PyTest_
*******

There are a number of testing tools for Python developers. Since this project
is designed to integrate with Sphinx_, we will use PyTest_,  the tool chain used by the
Sphinx_ project. There is a nice extension to PyTest_ available in the Sphinx_
system as well. More on that later.

Installing PyTest_
==================

This step is easy:

..  code-block:: shell

    $ pip install pytest

Once we have this tool installed, we can set up a very simple test to verify
that everything is working.

All tests are contained in Python modules with names beginning with **test_**.
We will place these test files in the **tests** directory. Here is a "sanity**
check:

..  literalinclude::    ../../tests/basics/test_sanity.py
    :caption: tests/test_sanity.py

In order for this test to pass, we need a simple **iunc** function. We will
place this function in our primary project package in the **utils.py** file:

..  literalinclude::    /_examples/utils-01.py
    :caption: sphinxcontrib/pylit/utils.py

PyTest Coverage Checks
**********************

The goal in testing is to make sure all of your code runs as designed. The unit tests we write are designed to exercise the code and verify that each unit of code works properly. Coverage checks watch the tests run and measure the number of lines of code that are actually subjected to some test. The obvious goal should be 100%, but this number is sometimes hard to reach. For PyTest_, there is a simple plugin available to add coverage checking to yout testing tool kit: pytest-cov_.

Installing pytest-cov_
======================

We add this project to our **requirements.txt** file, or run this command;

..  code-block:: shell

    $ pip install pytest-cov

Tou use this plugin, wwe change the test command by adding a few new options:


Travis-CI
*********

Travis-CI_ has been supporting open-source projects for a long time. If you
host your code on Github_ they will check out a fresh version of your code
every time you "push" changes to Github_, then set up a fresh virtual machine
that you can configure, and run tests. If all the tests pass, you will be
issued a "badge" for your project that you can place on your **README.rst** file
for every visitor to see. This is a mark of excellence, and we will set up mode
badges in later steps.

..  note::

    Testing is designed so that you run a set of "unit" tests every time you
    reach a suitable point. If all tests pass when you push your code to
    Github_, the badge will say so. If they fail, the badge will say that as
    well. most cevelopers do not stop working on code until that badge says
    "passing"!

To configure Travis-CI_ we need to add one file to the project. This file is
named **.travis.yml** and ours looks like this:

..  literalinclude::    /_examples/travis-01.yml
    :caption: .travis.yml

Once this file is in your project, you need to go to Travis-CI_ and turn on
testing. You cab register on their site using your Github_ credentials. Under
the "Account" page, you sync your repository list, find this project and flip
the toggle that turns on testing. From that point on, every time you push code
to Github_, Travis-CI will be notified and the testing will begin. Once it
finished, the badge link will update with the results. If you are interested,
you can watch the process on the Travis-CI_ website. Just click on the project
name in the *Dashboard*.

Appveyor
********

Appveyor_ operates much like Travis-CI_, except they spin up Windows virtual machines for testing. Using this system, we can be sure those (ugh) Windows users will find the project usable on their systems.

The setup file we need for this system is pretty simple;

..  literalinclude::    /_examples/appveyor.yml
    :caption: appveyor.yml

Adding Badges
*************

Once you have all of these testing tools set up, you need to modify your README.rst file so the badges show up. Here is the new version I use:

..  literalinclude::    /_examples/README-02.rst
    :caption: README.rst

..  warning::

    All of these new image links refer to my accounts on the various services. you should use your own!

Perhaps we are now ready to start serious development work. Well, maybe!

