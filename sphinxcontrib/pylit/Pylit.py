
from typing import Any, Dict
from sphinx.application import Sphinx
from sphinx.domains import Domain
from .PylitCodeBlock import PylitCodeBlock
from .PylitIndex import PylitIndex


class PylitDomain(Domain):
    name = 'pylit'
    label = 'PyLiT: LP for Sphinx'

    directives = {
        'code': PylitCodeBlock,
        'index': PylitIndex,
    }


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_domain(PylitDomain)
