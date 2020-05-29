Tracing Sphinx_ Domain Directives
#################################

Sphinx_ domains provide a kind of namespace for a collection of directives that
extend Sphinx_. They were designed to support documenting a number of
languages, but can be used to manage other extensions as well.

|pylit| will provide a number of directives that control processing of |RST|
blocks. In order to design a domain for this purpose, we need to figure out how
domains work. That means (unfortunately) spending some time doing that "read
the code" work and trying to decipher what is going on.

Sphinx_ Domain API
******************

Setting up a basic domain is pretty simple. All we need is a class that inherits from the SphinxDOmain class:

..	code-block::	python

	from sphinx.domains import Domain
	

	class PylitDomain(Domain):
		name = 'pylit'
		label = "Literate Programming for Sphinx'

		roles = {
			'pilitref': XRefRole()
		}

		directives = {
			'code': Pylitnode,	
		}

		indices = {
			PylitIndex,
		}

		initial_data = {
			'pylit_blocks': [],




