Tracing Sphinx_ Domain Directives
#################################

Sphinx_ domains provide a kind of namespace for a collection of directives that
extend Sphinx_. They were designed to support documenting a number of
languages, but can be used to manage other extensions as well.

|pylit| will provide a number of directives that control processing of |RST|
blocks. In order to design a domain for this purpose, we need to figure out how
domains work. That means (unfortunately) spending some time doing that "read
the code" work and trying to decipher what is going on.

We begin building a new domain for Sphinx by setting up the basic class. This
domain will be named **pylit** and will support one **code** directive to get
started.

The package we are building is named **sphinxcontrib-pylit**, and can be
imported using **sphinxcontrib.pylit**. Our starting directory structure is set
up first:

..  code-block:: shell

    $ mkdir -p sphinxcontrib.pylit
    $ touch sphinxcontrib/__init__.py
    $ touch sphinxcontrib/pylit/__init__.py

Sphinx Startup
**************

When Sphinx first starts an instance of the **Application** class is created. Part
of that process sets up a **registry** where application data is stored. After
loading all built-in extensions, the user defined extensions found in the
configuration file are imported and recorded in the registry.

The extension loading process first check to see if this extension has already
been loaded. If not, it tries to import the named extension. If that works, it
checks to see if a **setup** function exists in the extension and that routine
is called with the current application instance as a parameter. The **setup**
function can return a **metadata** dictionary or **None**. Once all of this
succeeds, the new extension is recorded in **app.extensions** along with all
other built-in and user extensions. The new entry is an instance of the
**Extension** class.

The sequence of calls to perform all of this is as follows:

..  code-block:: text

    application
        __init__.py ->
            self.registry =SphinxComponentRegistry()
            for extension in self.config.extensions:
                self.setup_extension(extension)
        setup_extension(extension)
            self.registry.load_extension(self, extension)

    registry
        load_extension(app, extension)
            mod = import_module(extension)
            setup = getattr(mod, 'setup', None)
            meta = setup(app)
            app.extensions[extension] = Extension(extension, mod **metadata)

    extension object
        self.name = extension name
        self.mod the imported module
        self.metadata
        self.version if any

A simple test of proper extension setup would involve checking that the new
extension is imported and listed in the app.extensions list.


Sphinx_ Domain API
******************

Setting up a basic domain is pretty simple. All we need is a class that
inherits from the **SphinxDomain** class:

..	pylit:code::	python

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



In the extension **setup** function, any defined domains are loaded through
**app.add_domain()** method.



