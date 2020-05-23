from docutils import nodes
from sphinx.domains import Domain
from sphinx.directives import ObjectDescription
from docutils.parsers.rst import directives


class pylit_node(nodes.General, nodes.Element):
    pass


class PyLiTNode(ObjectDescription):

    required_arguments = 1

    option_spec = {
        'language': directives.unchanged
    }


class PyLiTDomain(Domain):
    name = 'pylit'
    label = 'PyLiT Literate'

    directives = {
        'code': PyLiTNode,
    }


def setup(app):
    app.add_domain(PyLiTDomain)
