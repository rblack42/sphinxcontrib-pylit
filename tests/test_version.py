from sphinxcontrib.pylit import version


def test_version():
    vstr = ""
    with open("sphinxcontrib/pylit/__init__.py") as f:
        lines = f.readlines()
        for l in lines:
            if "version" in l:
                break

        vstr = l.split('=')[1].strip()[1:-1]

    assert version == vstr
