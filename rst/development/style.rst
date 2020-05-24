Project Style Rules
###################

You write quality code, right? If so, you follow a set of style rules that
dictate how your code should be presented to readers. That means not just you,
as the developer, but unnamed others who will either study your code for
educational purposes or to maintain it long after you have left the project.

Python forces some style on you with its rules for indentation, but there are
other rules most python developers follow.

We will use the flake8_ tool to verify that all project code satisfies rules
set forth in the Python PEP8 style guide are followed.

We will also use MyPy_ which checks that the newer type annotations on function
parameters and return values are being followed. Notes on these are below.

Flake8_
*******

Flake8_ is a simple tool that checks a variety of style issues. If it finds
problems, it will detail where it found the problem, and basically give you
guudance on how to fix things.

We will integrate running Flake8_ into unit testing so that a "passing" test
includes passing the style guides.

MyPy_
*****

Newer projects are moving toward annotating Python code so that the types of
function parameters, and the return types are marked. These additions are not
necessary, but they enable checking of proper usage of the annotated functions.

The MyPy_ tool will check any annotations included in the project. A companion
tool, Monkeytype_ will scan project code and identify places where the
annotations can be added. Optionally, it can update existing files with proper
annotations.


