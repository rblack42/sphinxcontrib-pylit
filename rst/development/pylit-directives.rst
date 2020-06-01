Basic Pylit Blocks
##################

|pylit| will start off by discussing the  fundamental |LP| block types we will
need. These types are based on Knuth' original |LP| paper.

Named Blocks
************

A key concept in |LP| is that blocks of code should be named in a way that
helps explain what the block is all about. There are no constraints on this
name, it can be any human-readable text chosen by the writer to provide a clue
as to what will be found in the block.


Once we create a named block, we can insert that block elsewhere in our program
code by using either the full text of the chosen name, or an abbreviation
sufficiently long as to uniquely identify the named block we wish to insert.
The point of insertion will appear in another block, set up by special markers
to distinguish this name from the surrounding code. In this version of |pylit|
insertion points will be marked using line comment markers, followed by the
block name enclosed in special markers to avoid possible conflicts with other
comments found in the code.

Basic named code blocks will be identified using a simple Sphinx_ directive.

    * **pylit:code** - start a named code block list.

..  note::

    |pylit| will use a SPhinx_ **Domain** to group directives and avoid
   conflicts with other possible directives in use in a given document.

To make reusing existing components in Sphinx_ simpler, we will extend the
existing **CodeBlock** directive for our first block. The block name will be
provided using the optional **caption** parameter provided with this
directive.

    * **add** - add a block to an existing named block list.

In Knuth's paper, code was written to files for processing by an extraction tool. The name of the file
..  pylit:code::    python
    :caption: Hello World

    def main():
        print("Hello")

    if __name__ == '__main__':
        main)_


..  pylit:index::

    Block 2
