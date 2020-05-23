import pytest
from sphinxcontrib.pylit import utils


@pytest.fixture
def test_inc():
    return utils.inc(2)


def test_inc_result(test_inc):
    assert test_inc == 3
