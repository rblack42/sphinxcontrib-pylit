.. _dev-extensions:

Developing the PyLiT extension
==============================

The configuration file itself can be treated as an extension if it contains a
``setup()`` function.  All other extensions to load must be listed in the
:confval:`extensions` configuration value.


The PyLiT API
-------------

.. toctree::
   :maxdepth: 2

   domainapi
   pylitdomain
