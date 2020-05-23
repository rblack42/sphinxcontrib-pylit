import pytest


@pytest.mark.sphinx('html', testroot='ext-pylit', freshenv=True,
                    confoverrides={'pylit_emit_warnings': True})
def test_pylit(app, status, warning):

    app.builder.build_all()

    # check pylitlist
    content = (app.outdir / 'index.html').read_text()
    print(content)
    assert ('sphinxcontrib.pylit') in content

