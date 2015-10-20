# simple_execute.py
# Executes an XOR using the neural network that was created by simple.py

import sys
from fann2 import libfann

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print 'Usage: python simple_execute.py arg1 arg2'
        exit()

    arg1 = int(sys.argv[1])
    arg2 = int(sys.argv[2])

    ann = libfann.neural_net()
    ann.create_from_file('xor.net')
    print ann.run([arg1, arg2])
