from __future__ import print_function

from __init__ import run_server, MinimalClient
from time import time
import sys

class Geronimo(object):
    def __init__(self):
        super(Geronimo, self).__init__()

    def greet(self, name=None):
        if name is None:
            name = 'stranger'
        return "Hello, {}!".format(name)

    def err(self):
        raise Exception()

def server():
    g = Geronimo()
    run_server(g, pickle_protocol=2)

def client():
    cl = MinimalClient(Geronimo, pickle_protocol=2)

    start = time()
    r = cl.greet(name='John')
    delta = time() - start
    print('{:.1e}'.format(delta), r)

if __name__ == '__main__':
    try:
        mode = sys.argv[1]
    except IndexError:
        mode = None

    if mode == 'server':
        server()
    elif mode == 'client':
        client()
    else:
        print('USAGE: python test.py [client|server]')
        exit(1)
