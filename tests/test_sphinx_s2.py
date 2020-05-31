import os
import pytest
from importlib import import_module

PACKAGE = 'sphinxcontrib.pylit'

ROOTDIR = 'sphinx-s2'

def test_extension_import():
    """verify extension can be imported and has a setup function"""
    try:
        mod = import_module(PACKAGE)
    except ImportError:
        return False
    setup = getattr(mod, 'setup', None)
    assert not setup is None


@pytest.mark.sphinx('html', testroot=ROOTDIR, freshenv=True)
def test_sphinx_basic_html(app, status, warning):
    """verify sphinx runs with new extension"""
    app.builder.build_all()
