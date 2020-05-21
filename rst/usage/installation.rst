..  include::   /references.inc

..  installation:

=================
Installing PyLiT
=================

.. contents::
   :depth: 1
   :local:
   :backlinks: none

.. highlight:: console

Overview
--------

|pylit| is written in `Python`__ and supports Python 3.5+.

__ https://docs.python-guide.org/


.. _install-pypi:

Installation from PyPI
----------------------

:mod:`sphinxcontrib-pylit` is published on the `Python Package Index
<https://pypi.org/project/Sphinx/>`_.  The preferred tool for installing
packages from *PyPI* is :command:`pip`.  This tool is provided with all modern
versions of Python.

On Linux or MacOS, you should open your terminal and run the following command.

::

   $ pip install -U sphinx

On Windows, you should open *Command Prompt* (:kbd:`⊞Win-r` and type
:command:`cmd`) and run the same command.

.. code-block:: doscon

   C:\> pip install -U sphinx

After installation, type :command:`pylit --version` on the command
prompt.  If everything worked fine, you will see the version number for the
Sphinx package you just installed.

Installation from *PyPI* also allows you to install the latest development
release.  You will not generally need (or want) to do this, but it can be
useful if you see a possible bug in the latest stable release.  To do this, use
the ``--pre`` flag.

::

   $ pip install -U --pre pylit6



Installation from source
------------------------

You can install |pylit| directly from a clone of the `Git repository`__.  This
can be done either by cloning the repo and installing from the local clone, on
simply installing directly via :command:`git`.

::

   $ git clone https://github.com/sphinx-doc/sphinx
   $ cd sphinx
   $ pip install .

::

   $ pip install git+https://github.com/rblack42/pylit8

You can also download a snapshot of the Git repo in either `tar.gz`__ or
`zip`__ format.  Once downloaded and extracted, these can be installed with
:command:`pip` as above.

.. highlight:: default

__ https://github.com/rblack42/pylit8
__ https://github.com/rblack42/pylit8/archive/master.tar.gz
__ https://github.com/rblack42/pylit8/archive/master.zip
