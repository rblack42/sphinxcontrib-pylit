import hashlib
import os
import shutil


class DataStore(object):

    def __init__(self, rootdir='.pylit'):
        self.rootdir = rootdir
        if not os.path.isdir(self.rootdir):
            os.makedirs(self.rootdir)

    def delete(self):
        shutil.rmtree(self.rootdir)

    def add_code_block(self, blktype, tag, docname, lineno, content):
        # generate block hash
        nbytes = len(content)
        bdata = blktype + str(nbytes) + "\0" + content
        edata = bdata.encode('utf-8')
        m = hashlib.sha1()
        m.update(edata)
        blkhash = m.hexdigest()

        # write block to repo
        blkdir = blkhash[:2]
        os.makedirs(os.path.join(self.rootdir, blkdir))
        blkname = blkhash[2:]
        blkpath = os.path.join(self.rootdir, blkdir, blkname)
        if os.path.isfile(blkpath):
            print("Block already in store: ", tag)
            return
        print("Block stored in ", blkdir, blkname)
        with open(blkpath, 'w') as fout:
            fout.write(bdata)

        # record block tag in catalog
        treeitem = \
            'tree' + ":" + \
            blkhash + ":" + \
            tag + ":" + \
            docname + ":" + \
            str(lineno) + "\n"
        catalog = os.path.join(self.rootdir, 'catalog')
        with open(catalog, "a") as c:
            c.write(treeitem)
