|TDD| of Sphinx_ Extensions
###########################

We are going to start development of the |pylit| extension using the basic
concepts of |TDD|.

sphinx-testing
**************

The Sphinx_ source code includes an extensive unit testing system, but that
system is largely undocumented (silly!) Instead, you are left to dig through
the testing system to figure out how to build something. In our case, we will
start off with the smallest test of a new extension we can concoct, and try to
get a test running using the SPhinx_ testing tools.

conftest.py
===========

PyTest_ can use code in a **conftest.py** file living in a test directory to
configure all tests found in that directory. In the Sphinx_ source code, there
is a example file we will copy into a sphinx test directory we will name
**tests/extensions**.

..  code-block:: shell

    $ mkdir -p tests/extensions

Copy the **conftest.py** file from the Sphinx source test directory (**tests**)
into the **extensions** directory.

Then we need a **roots** directory where we will place example |RST| files used
for each test.

..  code-block:: shell

    $ mkdir -p tests/extensions/roots




