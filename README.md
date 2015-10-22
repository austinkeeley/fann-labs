# FANN Labs
Some artificial neural network projects written using the FANN Python bindings.

## Instructions

Install libfann

    git clone https://github.com/libfann/fann.git
    cd ./fann
    cmake .
    sudo make install

Install swig, e.g. for Ubuntu,

    sudo apt-get install swig

Install dependencies

    pip install -r requirements.txt


## Labs in the project

### Simple
The "Hello World" of FANN projects. It teaches the computer how to do an XOR
operation.

##### Usage:
Train the network using the data in `xor.data`

    python simple.py

Now you can use the ANN to calculate some XOR operations:

    python simple_execute.py -1 1
    [0.9670711938225884]

Note that it uses `1` and `-1` for `true` and `false` values.

### Language
Teaches an ANN to distinguish between English, French and Polish. This example
comes from the whitepaper [Neural Networks Made Simple](http://fann.sourceforge.net/fann_en.pdf)
by Steffen Nissen.

Some sample texts for training are included for all 3 languages:

* The Star Spangled Banner (English)
* The first paragraph of [Moby Dick](http://americanliterature.com/author/herman-melville/book/moby-dick-or-the-whale/chapter-1-loomings) (English)
* The first paragraph of [Les Misérables](http://www.gutenberg.org/ebooks/17489) (French)
* La Marseillaise (French)
* Poland Is Not Yet Lost (Polish)
* The first paragraph of [Heart of Darkness](http://wolnelektury.pl/katalog/lektura/conrad-jadro-ciemnosci.html)

There is a helper script, `frequency.py` which reads text from stdin and outputs
the frequencies to stdout.  This was used to generate the `frequencies.data` file
(with some manual tweaks to add the correct output lines and the header).

#### Usage:
Train the network using the data in `frequencies.py`

    python language.py

Send character frequencies through the ANN by specifying text on stdin. The first value is the English output weight, the second is the French weight and the third is the Polish weight.

    echo "It was the best of times, it was the worst of times." | python language_execute.py
    [0.9630737634985367, -0.15683674456038033, 0.1289069051856062]

    echo "Sacré bleu! Parlez-vous français?" | python language_execute.py
    [-0.20376557393014816, 0.9150483874823709, 0.42047687812357815]

    echo "Przepraszam. Nie mówię po polsku. Do widzenia." | python language_execute.py
    [-0.12483603819319011, 0.40513661945170565, 0.9251426768015083]

Note that this ANN only uses the 26 character Latin alphabet and ignores any other characters or punctuation.

### Notes
The `fann2` Python bindings are not documented because they are really just a
swig port of the C++ bindings.  See [the the reference manual page](http://leenissen.dk/fann/html/files/fann_cpp-h.html) for the API.
