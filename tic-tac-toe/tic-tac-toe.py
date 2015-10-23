# tic-tac-toe.py
# Teaches the ANN how to win tic-tac-toe.

from fann2 import libfann


if __name__ == '__main__':
    num_input = 9
    num_output = 9
    num_neurons_hidden = 11
    desired_error = 0.0001
    max_epochs = 500000
    epochs_between_reports = 1000

    ann = libfann.neural_net()
    ann.create_standard_array([num_input, num_neurons_hidden, num_output])
    ann.set_activation_function_output(libfann.SIGMOID_SYMMETRIC)
    ann.set_activation_function_hidden(libfann.SIGMOID_SYMMETRIC)

    ann.train_on_file("gamestates.data", max_epochs, epochs_between_reports, desired_error)

    ann.save("tic-tac-toe.net")
