# language.py
# A Python port of the language example from the whitepaper "Neural Networks
# Made Simple" (http://fann.sourceforge.net/fann_en.pdf).

from fann2 import libfann


if __name__ == '__main__':
    num_input = 26
    num_output = 3
    num_neurons_hidden = 13
    desired_error = 0.001
    max_epochs = 500000
    epochs_between_reports = 1000

    ann = libfann.neural_net()
    ann.create_standard_array([num_input, num_neurons_hidden, num_output])
    ann.set_activation_function_output(libfann.SIGMOID_SYMMETRIC)
    ann.set_activation_function_hidden(libfann.SIGMOID_SYMMETRIC)

    ann.train_on_file("frequencies.data", max_epochs, epochs_between_reports, desired_error)

    ann.save("language.net")
