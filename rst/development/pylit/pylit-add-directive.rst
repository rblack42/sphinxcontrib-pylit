|pylit| Directives
##################

The heart of the **sphinxcqontrib-pylit** system lies the directives that
process |pylit| blocks. Our first task involves collecting a linear list of
block titles. This list is available as soon as Sphinx_ finishes reading in the
stored documents from the **doctrees** directory, and reading any new source
documents. The |pylit| directive must create new nodes for the code blocks we
will be processing later.

Using the standard Sphinx_ **todo** directive as a model, we need to set up a few methods:

First, we set up a simple test that will check the count of **pylit:code** blocks found in the document.
