from docutils import nodes
from sphinx.domains import Domain
from sphinx.directives import ObjectDescription
from docutils.parsers.rst import directives


class pylit_node(nodes.General, nodes.Element):
    """Create a pylit node type"""
    pass


class PyLiTNode(ObjectDescription):
    """Manage pylit nodes"""

    required_arguments = 1

    option_spec = {
        'language': directives.unchanged
    }


class PyLiTDomain(Domain):
    """Create the pylit domain"""
    name = 'pylit'
    label = 'PyLiT Literate'

    directives = {
        'code': PyLiTNode,
        'add': PyLiTNode,
        'file': PyLiTNode,
        'shell': PyLiTNode,
    }


def setup(app):
    """Register the pylit domain"""
    app.add_domain(PyLiTDomain)
