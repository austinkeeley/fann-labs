# simple_execute.py
# Executes an XOR using the neural network that was created by simple.py

import sys
from fann2 import libfann

if __name__ == '__main__':

    buf = ''
    for line in sys.stdin:
        buf += line

    print buf
