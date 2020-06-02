import pytest
from sphinxcontrib.pylit import utils

test_data = [
    [4,5],
    [5,6],
]

@pytest.fixture(params = test_data)
def gen_data(request):
    return request.param

def test_inc(gen_data):
    v1 = gen_data[0]
    v2 = gen_data[1]
    assert utils.incr(v1) == v2

