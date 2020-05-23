Introduction
============

This is the documentation for the |pylit| extension for Sphinx_.

This extension provides support for a variation of Dr. Donald Knuth's |LP|
concepts, extended to also support generation of Git_ code repositories from
the documentation.  This tool was originally written to support production of
lecture materials for Computer Science courses taught for over 10 years by the
author. It was used privately during that time, and is now being released as an
open-source package,

..	note::

    There are several packages listed on PyPi_ with **pylit** in the name. I
    first used this name in 2003 as part of my Computer Science Master's Thesis
    project at Texas State Uniersity, and I registered the **pylit.org** name
    in 2005 :cite:`black:2005`. If this causes confusion, I apologize to the
    others trying to build similar systems.

Features
--------

The |pylit| extensions provide a simple way to embed named code fragments in
|RST| source files. Rather than relying on Sphinx_ include mechanism, these
fragments can be extracted automatically into conventional source code files in
a standard (well, almost) Git_ repository for processing by normal development
tools.

Each fragment can be written in any supported language, and may contain special
comments which identify other named fragments to be included in the produced
source code at the indicated point. This is in keeping with Dr. Knuth's
original concept of |LP|.

What is not supported at the moment is the macro feature of standard |LP|.

A functional Git_ repository can be produced from the embedded source code.
However, the history in this repository will have time stamps that do not
reflect when the code was actually produced. Instead, the history timeline will
be compressed but linearly accurate, based on the current state of the |RST|
files processed by Sphinx_.


The background on how this package came to exist and why it supports the
current feature set is provided in the development notes. See
:ref:`development`.

Prerequisites
-------------

The |pylit| package depends on Sphinx_ and therefore needs at least **Python
3.5** to run. It also requires Git_ to manage repository production from |LP|
source files.


Usage
-----

See :doc:`/usage/quick-start` for installation guide and a quick getting-started reference.

