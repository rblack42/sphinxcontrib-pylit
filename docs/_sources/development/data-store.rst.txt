|pylit| Data Store
##################

|pylit| uses a data store modeled after the one used by Git_ t manage
repositories. However, |pylit| does not store entire documents in one piece.
Instead, each source file is decomposed into a list of basic building blocks,
and those blocks are stored.

Obviously, there will be a lot of blocks in any given project. Each block is
written in some language, and can be transformed into a number of different
formats. If the block is to be displayed in print, the basic output formats
determine what transformation needs to be done. The heart of |pylit| is based
on performing the transformations as part of storing the block, and that
transformation does not need to be redone unless the source for that block
changes.

At the risk of losing some readers, we will present the specification of the
|pylit| data store in a formal notation.

..  pylit-oz::

    \begin{schema}{BirthdayBook}
    known: \pset NAME \\
    birthday: NAME \pfun DATE
    \ST
    known = \dom birthday
    \end{schema}


