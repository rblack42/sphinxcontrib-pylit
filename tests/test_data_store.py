import os
import sphinxcontrib.pylit as pylit


def test_rootdir_empty():
    ds = pylit.DataStore()
    assert os.path.isdir('.pylit')
    ds.delete()


def test__rootdir_specified():
    ds = pylit.DataStore('test_repo')
    assert os.path.isdir('test_repo')
    ds.delete()

def test_delete_rootdir():
    ds = pylit.DataStore('test_repo')
    assert os.path.isdir('test_repo')
    ds.delete()
    assert not os.path.isdir('test_repo')
