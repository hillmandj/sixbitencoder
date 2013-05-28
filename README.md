This is a basic sixbit encoder with predefined encodings. It is a much simpler and less efficient compression algorithm when compared to the huffman encoder. If there is an item in data.dat (the original file that is meant to be compressed) the program will crash, whereas in the huffman encoder, encodings are automatically generated via the use of a binary tree and recursive functions.

This program is written in Python 2.7.

To run the program:

1. Run sixBitEncoding.py in the Python shell (make sure data.dat is in the same directory)
2. Run sixBitDecompress.py in the Python shell

Compression can be observed by looking at size of the encodedOutput.dat file.

Hope you find this interesting!

-Dan
