import hashlib
import base64
import os
import shutil


class DataStore(object):

    def __init__(self, rootdir = '.pylit'):
        self.rootdir = rootdir
        if not os.path.isdir(self.rootdir):
            os.makedirs(self.rootdir)

    def delete(self):
        shutil.rmtree(self.rootdir)
