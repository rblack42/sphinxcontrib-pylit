import os
import pytest


ROOTDIR = 'sphinx-s1'

@pytest.mark.sphinx('html', testroot=ROOTDIR, freshenv=True)
def test_sphinx_basic_html(app, status, warning):
    app.builder.build_all()

@pytest.mark.sphinx('latex', testroot=ROOTDIR, freshenv=True)
def test_sphinx_basic_latex(app, status, warning):
    app.builder.build_all()
    texpath = os.path.join(app.outdir, 'test.tex')
    print("TEXPATH: ", texpath)
    tex = open(texpath).read()
    assert 'sphinxcontrib.pylit' in tex

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
