# simple_execute.py
# Executes an XOR using the neural network that was created by simple.py

import sys
from fann2 import libfann
from frequency import count_frequency

if __name__ == '__main__':

    frequencies = count_frequency(sys.stdin)

    ann = libfann.neural_net()
    ann.create_from_file('language.net')
    print ann.run(frequencies)
