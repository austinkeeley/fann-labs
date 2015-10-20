# FANN Labs
Some sample FANN projects writen using the Python bindings.

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
The Hello World of FANN projects.


### Notes
The `fann2` Python bindings are not documented because they are really just a swig port of the C++ bindings.  See [the the reference manual page](http://leenissen.dk/fann/html/files/fann_cpp-h.html) for the API.
