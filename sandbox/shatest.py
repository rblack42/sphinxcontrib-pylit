import hashlib
import base64
import sys

def make_sha(fname):
    try:
        with open(fname) as f:
            data = f.read()
            bdata = base64.b64encode(data)
            nbytes = len(bdata)
            gdata = "blob " + str(nbytes) + "\0" + bdata
            m = hashlib.sha1()
            m.update(gdata)
    except:
        return ""
    return m.hexdigest(), bdata

def main():
    fname = sys.argv[1]
    h,d = make_sha(fname)
    print(h)
    print(d)

if __name__ == '__main__':
	main()
