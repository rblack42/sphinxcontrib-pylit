Literate Programming
####################

In 1984, Dr. Donald Knuth decided that software developers needed a new way to
document their code. In Knuth's mind, documentation should be written for the
human reader, like a work of literature. The documentation should take the
reader on a journey through the code, in whatever order makes sense in
explaining the code. The actual code should be presented in small sections
included within the document. Knuth wrote a few tools supporting his ideas,
and those tools actually extract the code described in the document for
processing by conventional development tools.

Knuth's idea did not take off as he wished, but there are many developers who
feel this is the right way to approach explaining code.

In my profession as a Computer Science educator, I have written thousands of
lectures using the Python Sphinx_ tool, and have added some custom extensions
that support a limited for m of Knuth's concepts. This project seeks to expand
my early experiments and present something I think can be very useful, both
in teaching, and in software development.

The **sphinxcontrib-lpblocks** extension allows developers to add blocks of
code with embedded links to other sections of code in a manner very similar to
Knuth's original proposal. In addition, the extension supports adding shell
commands that will extract the code presented so far, and run commands against
that version of the code. Later work might replace earlier code with new
blocks, and again those versions can be processed. This is basically how I
present programming concepts in a classroom, and my lecture notes can be living
documents using this extension.

LPblocks and Github
*******************

There is one minor wrinkle in this idea. Most developers want their code to
be hosted on something like Github_, and managed by Git_. In deciding to document
code using Literate Programming, it is the documentation that is the primary
source to be managed. The code is in that documentation, but must be extracted
for viewing, testing, and even releasing.

That means that a visitor to a project n Github_ will not be able to explore the
code directly. This might be considered a defect in this idea, but it actually
is in keeping with Knuth's original idea. Development should happen in the
documentation, not not be produced as an afterthought!

..  note::

    I have som eideas how to integrate conventionsl Git management with
    Literate Programming. Those ideas may well appear in this project over
    time. Contributions are welcome!



