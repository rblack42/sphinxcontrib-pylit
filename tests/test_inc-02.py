import pytest
from sphinxcontrib.pylit import utils

inc_set = [
        '4:5',
        '5:6',
]

@pytest.mark.parametrize('inc_set', inc_set)
def test_inc(inc_set):
    a,b = inc_set.split(':')
    assert utils.incr(int(a)) == int(b)

