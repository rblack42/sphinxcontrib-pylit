import os
from sphinxcontrib.pylit.DataStore import DataStore


def test_rootdir_empty():
    ds = DataStore()
    assert os.path.isdir('.pylit')
    ds.delete()


def test__rootdir_specified():
    ds = DataStore('test_repo')
    assert os.path.isdir('test_repo')
    ds.delete()

def test_delete_rootdir():
    ds = DataStore('test_repo')
    assert os.path.isdir('test_repo')
    ds.delete()
    assert not os.path.isdir('test_repo')
