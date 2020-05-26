import pytest


@pytest.mark.sphinx('html', testroot='sphinx', freshenv=True)
def test_pylit(app, status, warning):

    app.builder.build_all()

    # check pylitlist
    content = (app.outdir / 'index.html').read_text()
    print(content)
    assert ('sphinxcontrib.pylit') in content

