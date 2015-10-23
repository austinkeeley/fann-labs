# tic-tac-toe_execute.py
# Determines the best next move in a game of tic-tac-toe using an ANN

import sys
from fann2 import libfann

if __name__ == '__main__':

    if len(sys.argv) is not 10:
        print 'Usage: python tic-tac-toe_execute.py <game state>'
        exit()

    gamestate = [int(x) for x in sys.argv[1:]]

    print gamestate

    ann = libfann.neural_net()
    ann.create_from_file('tic-tac-toe.net')
    result = ann.run(gamestate)

    for x in xrange(len(result)):
        print result[x],
        print '\t',
        if (x+1) % 3 is 0:
            print
