"""
Parse Juan Carlos output for text features

specify whether this is the full set, only training+ val
It should be only trainig + val sets

convert to vector of n x V
Verify the order of the asins
Verify that the size is equal to n


"""

import numpy as np
import time


# sample file from Juan Carlos
fname = '../../DATASETS/dress_attributes/txt_represention/sample_training.txt'

f = open(fname)
txt = f.readlines()
f.close()


# txt is one big string
line_list = txt[0].split('\r')

# each line is of the form
# 'B0009PDO0Y 0:2 1:1 5:1 17:1 ... \r '
one_line = line_list[0]



def get_word_id_and_freq(line):
    """

    """
    word_id = None
    word_freq = None
    advanced_line = None
    #s = line.find(" ")
    e = line.find(":")
    if e == -1:
        return word_id, word_freq, advanced_line
    word_id = line[0:e]
    s = line.find(" ", e)
    word_freq = line[e+1:s]
    advanced_line = line[s+1:]
    #print advanced_line
    # return word_id, freq, and advanced_line
    return word_id, word_freq, advanced_line


def feature_generator(one_line):
    while one_line:
        word_id, word_freq, one_line = get_word_id_and_freq(one_line)
        yield word_id, word_freq


n = len(line_list)  # number of items

V = 100000  # assume a vocabulary of 100,000
# convert to vector of size n x V
txt_vec = np.zeros((n, V), type=int)

for i in range(0, n):
    line = line_list[i]
    s = line.find(' ')  # start of the first feature id
    asin = line[0:s]
    print asin
    # advance line and add space at the end
    one_line = line[s + 1:] + ' '
    while one_line:
        word_id, word_freq, one_line = get_word_id_and_freq(one_line)
        #print word_id, word_freq
        txt_vec[i, int(word_id)] = int(word_freq)

np.savetxt('txt_vec.txt', txt_vec, delimiter=',')







