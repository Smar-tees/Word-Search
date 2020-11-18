# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 16:40:17 2020

@author: ralls
"""
"""
Code must work with the provided config file
Code must work with a second config file using the same formatting
Code must be able to a place a word in any orientation (backwards, forwards, horizontal, vertical, diagonal, etc.)
Code must make a reasonable effort to construct a word search if possible
It is ok if your program does not have a 100% success rate for all possible word searches
Where you can get creative:

There are lots of possible strategies for placing your words!

"""
import codecs
from random import randrange
import pandas as pd 
import numpy as np
from copy import deepcopy

file_object = codecs.open('config.txt', 'r', encoding='utf8', errors='ignore')
content_string = file_object.readlines()
file_object.close()

alphabet_list = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'

dimensions = [int(content_string[0]), int(content_string[1])]
y = dimensions[0]
df = pd.DataFrame(index=np.arange(dimensions[0]), columns=np.arange(dimensions[1]))
    
def word_forward(word, word_search, y):
    while True:
        f = 0
        word_search_test = deepcopy(word_search)
        col_num = randrange(y - len(word))
        row_num = randrange(y)
        x = ''
        for i, c in enumerate(word):
            x = i
            if type(word_search_test[col_num + i][row_num]) == str:
                f += 1
                break
            elif i >= len(word):
                f += 1
                break
            elif type(word_search[col_num + i][row_num]) != str:
                word_search_test[col_num + i][row_num] = c
        if f >= 10:
            raise Exception('Cannot find word search that matches')
        if x >= len(word) - 1:
            word_search = word_search_test
            return word_search

def word_backward(word, word_search, y):
    word = word[::-1]
    while True:
        f = 0
        word_search_test = deepcopy(word_search)
        row_num = randrange(y)
        col_num = randrange(y - len(word))
        x = ''
        for i, c in enumerate(word):
            x = i
            if type(word_search_test[col_num + i][row_num]) == str:
                f += 1
                break
            elif i >= len(word):
                f += 1
                break
            elif type(word_search[col_num + i][row_num]) != str:
                word_search_test[col_num + i][row_num] = c
        if f >= 10:
            raise Exception('Cannot find word search that matches')
        if x >= len(word) - 1:
            word_search = word_search_test
            return word_search

def word_vertical(word, word_search, y):
    while True:
        f = 0
        word_search_test = deepcopy(word_search)
        row_num = randrange(y)
        col_num = randrange(y - len(word))
        x = ''
        for i, c in enumerate(word):
            x = i
            if type(word_search_test[row_num][col_num + i]) == str:
                f += 1
                break
            elif i >= len(word):
                f += 1
                break
            elif type(word_search[row_num][col_num + i]) != str:
                word_search_test[row_num][col_num + i] = c
        if f >= 10:
            raise Exception('Cannot find word search that matches')
        if x >= len(word) - 1:
            word_search = word_search_test
            return word_search

def word_diagonal(word, word_search, y):
    while True:
        f = 0
        word_search_test = deepcopy(word_search)
        row_num = randrange(y - len(word))
        col_num = randrange(y - len(word))
        x = ''
        for i, c in enumerate(word):
            x = i
            if type(word_search_test[row_num + i][col_num + i]) == str:
                f += 1
                break
            elif i >= len(word):
                f += 1
                break
            elif type(word_search[row_num + i][col_num + i]) != str:
                word_search_test[row_num + i][col_num + i] = c
        if f >= 10:
            raise Exception('Cannot find word search that matches')
        if x >= len(word) - 1:
            word_search = word_search_test
            return word_search
        
def fill_search(alphabet, word_search):
    for col_num in word_search:
        col = word_search[col_num]
        for i, cell in enumerate(col):
            letter_num = randrange(26)
            letter = alphabet[letter_num]
            if cell not in alphabet:
                cell = letter
            col[i] = cell
        word_search[col_num] = col
    return word_search

def print_search(word_search):
    for col_num in word_search:
        col = word_search[col_num]
        cell_list = []
        for cell in col:
            cell_list.append(cell)
        print(" ".join(map(str,cell_list)))
    return(word_search)

words = content_string[2:]

orient = ['word_forward', 'word_backward', 'word_vertical', 'word_diagonal']

for word in words:
    orient_num = randrange(4)
    used_orient = orient[orient_num]
    if 'forward' in used_orient:
        df = word_forward(word, df, y)
    elif 'backward' in used_orient:
        df = word_backward(word, df, y)
    elif 'vertical' in used_orient:
        df = word_vertical(word, df, y)
    elif 'diagonal' in used_orient:
        df = word_diagonal(word, df, y)

df = fill_search(alphabet_list.split(), df)

df = print_search(df)