import numpy as np
import os

def read_file2(fileIN):
    data = []
    with open(fileIN,"r") as file:
        for line in file:
            split = line.split()
            sentence = []
            for word in split:
                sentence.append(float(word))
            data.append(sentence)
    file.close()
    return data

def next_path(path_pattern):
    """
    Finds the next free path in an sequentially named list of files

    e.g. path_pattern = 'file-%s.txt':
    file-1.txt
    file-2.txt

    Runs in log(n) time where n is the number of existing files in sequence
    
    credit: https://stackoverflow.com/questions/17984809/how-do-i-create-an-incrementing-filename-in-python
    James
    """
    i = 1

    # First do an exponential search
    while os.path.exists(path_pattern % i):
        i = i * 2

    # Result lies somewhere in the interval (i/2..i]
    # We call this interval (a..b] and narrow it down until a + 1 = b
    a, b = (i // 2, i)
    while a + 1 < b:
        c = (a + b) // 2 # interval midpoint
        a, b = (c, b) if os.path.exists(path_pattern % c) else (a, c)

    return path_pattern % b