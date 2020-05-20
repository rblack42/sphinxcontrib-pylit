from sphinxcontrib.pylit import incrementer


def test_answer():
    assert incrementer.inc(2) == 3


def test_answer2():
    assert incrementer.inc(5) == 6
