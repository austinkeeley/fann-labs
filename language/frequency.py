# frequency.py
# Counts letter frequencies from stdin and produces a FANN training data block.
#
# Usage:
#   python frequency.py < training/english.txt
#
import sys

NUM_CHARACTERS = 26

def count_frequency(text):
    buf = ''
    for line in text:
        buf += line.lower()

    counts = [0 for x in xrange(NUM_CHARACTERS)]
    total = 0

    for character in buf:
        value = ord(character) - 97
        if value >= 0 and value < NUM_CHARACTERS:
            counts[value] = counts[value] + 1
            total = total + 1

    frequencies = [float(counts[x]) / total for x in xrange(NUM_CHARACTERS)]
    return frequencies


if __name__ == '__main__':

    buf = ''
    for line in sys.stdin:
        buf += line.lower()

    counts = [0 for x in xrange(NUM_CHARACTERS)]
    total = 0

    for character in buf:
        value = ord(character) - 97
        if value >= 0 and value < NUM_CHARACTERS:
            counts[value] = counts[value] + 1
            total = total + 1

    frequencies = [float(counts[x]) / total for x in xrange(NUM_CHARACTERS)]
    for frequency in frequencies:
        print frequency,
        print ' ',
