import pytest
from sphinxcontrib.pylit import utils

inc_set = [
        [4,5],
        [5,6],
]

@pytest.mark.parametrize('inc_set', inc_set)
def test_inc(inc_set):
    v1 = inc_set[0]
    v2 = inc_set[1]
    assert utils.incr(v1) == v2

