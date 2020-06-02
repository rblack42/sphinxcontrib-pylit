from sphinxcontrib.pylit import utils


def test_answer():
    assert utils.incr(2) == 3


def test_answer2():
    assert utils.decr(6) == 5
