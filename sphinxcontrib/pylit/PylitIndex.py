from sphinx.domains import Index


class PylitIndex(Index):
    name = 'pylit'
    localname = 'PyLiT Index'
    shortname = 'LPblocks'

    def __init__(self, *args, **kwargs):
        super(PylitIndex, self).__init__(*args, **kwargs)

    def generate(self, docnames=None):
        content = {}
        items = ((name, dispname, typ, docname, anchor)
                 for name, dispname, typ, docname, anchor, prio
                 in self.domain.get_objects())
        items = sorted(items, key=lambda item: item[0])
        for name, dispname, typ, docname, anchor in items:
            lis = content.setdefault("LPblocks", [])
            lis.append((
                dispname, 0, docname,
                anchor,
                docname, ''. typ
            ))
        re = [(k, v) for k, v in sorted(content.items())]
        return (re, True)
