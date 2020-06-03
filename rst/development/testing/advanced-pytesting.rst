Advanced PyTesting
##################

Since the |pylit| application will integrate with Sphinx_ we need to figure out
how Sphinx_ works internally. This can be done by cloning the application from
Github_. There is a bit of documentation there that will help, but it is mostly
"what" documentation that helps you explore the code. Sadly, when you want to
know details you run smack into "just read the code", which means the "why"
documentation is missing. This is silly for a tool that supports documentation
(IMHO)!

There is something useful in the source code, though.  Sphinx_ has a nice set
of unit tests, and those tests use a feature of PyTest that can help us write
better code.

PyTest_ Fixtures
****************

A *Fixture* is a function that will be called before a test is run by PyTest_.
We can use this feature to set up data to be used in the test.

Creating a Fixture:

..  literalinclude::    /_examples/test_inc-01.py
    :caption: tests/test_inc.py

While this may not seem like much of an addition to testing, it gets more
powerful when you use parameterized fixtures.

..  literalinclude::    /_examples/test_inc-02.py
    :caption: tests/test_inc.py

Here, we set up a list if test values and expected results. In this example,
the list is just strings, but more complex Python structures can be set up.


..  literalinclude::    /_examples/test_inc-03.py
    :caption: tests/test_inc.py


Here the parameter list is a list of integers. The first value will be tested,
and the second value is the expected result.

We can also parameterize the fixture:

..  literalinclude::    /_examples/test_inc-04.py
    :caption: tests/test_inc.py

There is much more to learn about using fixtures and marks in PyTest_, but this
will get us started.




