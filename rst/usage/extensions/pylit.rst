:mod:`sphinxcontrib.pylit` -- Support for Literate Programming
==============================================================

..  include::   /references.inc

..  module::    sphinxcontrib.pylit
    :synopsis: Allow an extended form of |LP| in documents.
..  moduleauthod: |author|

..  versionadded:   0.1

This extension creates a Sphinx domain with these new directives:

..  rst:directive:: pylit.code

    This directive marks the starting block of a list of code blocks. This list can be extended using the :rst:dir:`pylit.add` directive (see below).

..  rst:directive:: pylit:add

    This directive references a previously defined code |LP| block. The code in this block is appended to the list of blocks currently contained in the named code block.

..  rst:directive:: pylit.file

    Use this directive to identify a new file containing the named code block
    list. the code written to this file will include the current list of blocks contained in the nammed |LP| block.


..  rst::directive::    pylit.shell

    Execute commands in a shell rooted in the develpment directory, with all code defined at this point in the documentation.
