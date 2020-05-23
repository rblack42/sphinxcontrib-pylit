from sphinxcontrib.pylit.meta import version

VERSION = 'sphinxcontrib/pylit/meta.py'

def test_version():
    vstr = ""
    with open(VERSION) as f:
        lines = f.readlines()
        for l in lines:
            if "version" in l:
                break

        vstr = l.split('=')[1].strip()[1:-1]

    assert version == vstr
