import pytest
from sphinxcontrib.pylit import utils

test_data = [
    (4,5),
    (5,6),
]

@pytest.fixture(params = [
    'utils.incr',
    'utils.decr',
])
def gen_func(request):
    return request.param

@pytest.mark.parametrize('data', test_data)
def test_incr(gen_func, data):
    v1 = data[0]
    v2 = data[1]
    func = eval(gen_func)
    if gen_func.endswith('incr'):
        assert func(v1) == v2
    else:
        assert func(v2) == v1

