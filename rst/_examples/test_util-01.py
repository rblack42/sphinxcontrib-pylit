import pytest
from sphinxcontrib.pylit import utils

test_data = [
    [4,5],
    [5,6],
    pytest.mark.xfail([5,4]),
    pytest.mark.xfail([6,5]),
]

@pytest.fixture(params = [
    'incr',

    'decr'
])
def gen_data(request):
    return request.param

@pytest.mark.parametrize("test_data", test_data)
def test_incr(gen_data, test_data):
    print("testing:", gen_data, test_data)

