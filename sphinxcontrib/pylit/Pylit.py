
from typing import Any, Dict
from sphinx.application import Sphinx
from sphinx.domains import Domain
from sphinx.roles import XRefRole

from .PylitCodeBlock import PylitCodeBlock
from .PylitIndex import PylitIndex


class PylitDomain(Domain):
    name = 'pylit'
    label = 'PyLiT: LP for Sphinx'

    directives = {
        'code': PylitCodeBlock,
        'index': PylitIndex,
    }

    roles = {
        'lpref': XRefRole()
    }

    initial_data = {
        'blocks': [],   # list of LP blocks
    }


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_domain(PylitDomain)
