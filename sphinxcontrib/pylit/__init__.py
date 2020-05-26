from typing import Any, Dict, List, Tuple
from typing import cast

from docutils import nodes
from docutils.nodes import Element, Node
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.admonitions import BaseAdmonition

import sphinx
from sphinx.application import Sphinx
from sphinx.domains import Domain
from sphinx.environment import BuildEnvironment
from sphinx.errors import NoUri
from sphinx.locale import _
from sphinx.util import logging, texescape
from sphinx.util.docutils import SphinxDirective, new_document
from sphinx.writers.html import HTMLTranslator
from sphinx.writers.latex import LaTeXTranslator

logger = logging.getLogger(__name__)


class pylit_node(nodes.Admonition, nodes.Element):
    pass


class pylitlist(nodes.General, nodes.Element):
    pass


class Pylit(BaseAdmonition, SphinxDirective):
    """
    A pylit entry, displayed (if configured) in the form of an admonition.
    """

    node_class = pylit_node
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'class': directives.class_option,
        'name': directives.unchanged,
    }

    def run(self) -> List[Node]:
        if not self.options.get('class'):
            self.options['class'] = ['admonition-pylit']

        (pylit,) = super().run()  # type: Tuple[Node]
        if isinstance(pylit, nodes.system_message):
            return [pylit]
        elif isinstance(pylit, pylit_node):
            pylit.insert(0, nodes.title(text=_('Pylit')))
            pylit['docname'] = self.env.docname
            self.add_name(pylit)
            self.set_source_info(pylit)
            self.state.document.note_explicit_target(pylit)
            return [pylit]
        else:
            raise RuntimeError  # never reached here


class PylitDomain(Domain):
    name = 'pylit'
    label = 'pylit'

    @property
    def pylits(self) -> Dict[str, List[pylit_node]]:
        return self.data.setdefault('pylits', {})

    def clear_doc(self, docname: str) -> None:
        self.pylits.pop(docname, None)

    def merge_domaindata(self, docnames: List[str], otherdata: Dict) -> None:
        for docname in docnames:
            self.pylits[docname] = otherdata['pylits'][docname]

    def process_doc(self, env: BuildEnvironment, docname: str,
                    document: nodes.document) -> None:
        pylits = self.pylits.setdefault(docname, [])
        for pylit in document.traverse(pylit_node):
            env.app.emit('pylit-defined', pylit)
            pylits.append(pylit)


class PylitList(SphinxDirective):
    """
    A list of all pylit entries.
    """

    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}  # type: Dict

    def run(self) -> List[Node]:
        # Simply insert an empty pylitlist node which will be replaced later
        return [pylitlist('')]


class PylitListProcessor:
    def __init__(
                self, app: Sphinx,
                doctree: nodes.document,
                docname: str) -> None:
        self.builder = app.builder
        self.config = app.config
        self.env = app.env
        self.domain = cast(PylitDomain, app.env.get_domain('pylit'))

        self.process(doctree, docname)

    def process(self, doctree: nodes.document, docname: str) -> None:
        pylits = sum(self.domain.pylits.values(), [])  # type: List[pylit_node]
        document = new_document('')
        for node in doctree.traverse(pylitlist):
            if node.get('ids'):
                content = [nodes.target()]  # type: List[Element]
            else:
                content = []

            for pylit in pylits:
                # Create a copy of the pylit node
                new_pylit = pylit.deepcopy()
                new_pylit['ids'].clear()

                # (Recursively) resolve references in the pylit content
                #
                # Note: To resolve references, it is needed to
                # wrap it with document node
                document += new_pylit
                self.env.resolve_references(
                        document,
                        pylit['docname'],
                        self.builder)
                document.remove(new_pylit)
                content.append(new_pylit)

                pylit_ref = self.create_pylit_reference(pylit, docname)
                content.append(pylit_ref)

            node.replace_self(content)

    def create_pylit_reference(
            self, pylit: pylit_node,
            docname: str) -> nodes.paragraph:
        description = (_(
                '(The <<original entry>> is located in %s, line %d.)') %
                (pylit.source, pylit.line))

        prefix = description[:description.find('<<')]
        suffix = description[description.find('>>') + 2:]

        para = nodes.paragraph(classes=['pylit-source'])
        para += nodes.Text(prefix, prefix)

        # Create a reference
        linktext = nodes.emphasis(_('original entry'), _('original entry'))
        reference = nodes.reference('', '', linktext, internal=True)
        try:
            reference['refuri'] = \
                    self.builder.get_relative_uri(docname, pylit['docname'])
            reference['refuri'] += '#' + pylit['ids'][0]
        except NoUri:
            # ignore if no URI can be determined, e.g. for LaTeX output
            pass

        para += reference
        para += nodes.Text(suffix, suffix)

        return para


def visit_pylit_node(self: HTMLTranslator, node: pylit_node) -> None:
    self.visit_admonition(node)


def depart_pylit_node(self: HTMLTranslator, node: pylit_node) -> None:
    self.depart_admonition(node)


def latex_visit_pylit_node(self: LaTeXTranslator, node: pylit_node) -> None:
    self.body.append('\n\\begin{sphinxadmonition}{note}{')
    self.body.append(self.hypertarget_to(node))

    title_node = cast(nodes.title, node[0])
    title = texescape.escape(title_node.astext(), self.config.latex_engine)
    self.body.append('%s:}' % title)
    node.pop(0)


def latex_depart_pylit_node(self: LaTeXTranslator, node: pylit_node) -> None:
    self.body.append('\\end{sphinxadmonition}\n')


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_node(pylitlist)
    app.add_node(pylit_node,
                 html=(visit_pylit_node, depart_pylit_node),
                 latex=(latex_visit_pylit_node, latex_depart_pylit_node),
                 text=(visit_pylit_node, depart_pylit_node),
                 man=(visit_pylit_node, depart_pylit_node),
                 texinfo=(visit_pylit_node, depart_pylit_node))

    app.add_directive('pylit', Pylit)
    app.add_directive('pylitlist', PylitList)
    app.add_domain(PylitDomain)
    app.connect('doctree-resolved', PylitListProcessor)
    return {
        'version': sphinx.__display_version__,
        'env_version': 2,
        'parallel_read_safe': True
    }
