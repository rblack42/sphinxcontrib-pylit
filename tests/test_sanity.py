from sphinxcontrib.pylit import utils


def test_answer():
    assert utils.inc(2) == 3


def test_answer2():
    assert utils.inc(5) == 6
