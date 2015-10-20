# simple.py
# The simplest ANN we can build using FANN. This teaches the neural network
# how to XOR some boolean values.
#
# This is essentially a Python port of the code at
# http://leenissen.dk/fann/wp/help/getting-started/

from fann2 import libfann


if __name__ == '__main__':
    num_input = 2
    num_output = 1
    num_neurons_hidden = 4
    desired_error = 0.001
    max_epochs = 500000
    epochs_between_reports = 1000

    ann = libfann.neural_net()
    ann.create_standard_array([num_input, num_neurons_hidden, num_output])
    ann.set_activation_function_output(libfann.SIGMOID_SYMMETRIC)
    ann.set_activation_function_hidden(libfann.SIGMOID_SYMMETRIC)

    ann.train_on_file("xor.data", max_epochs, epochs_between_reports, desired_error)

    ann.save("xor.net")
