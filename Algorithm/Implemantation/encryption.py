#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    t = math.sqrt(len(s))
    min_row = math.floor(t)
    max_col = math.ceil(t)

    if len(s) > min_row * max_col:
        while min_row <= max_col:
            min_row += 1
            if len(s) <= min_row * max_col:
                break

    print("min_row : {}".format(min_row))
    print("max_col : {}".format(max_col))

    tmp = ""
    my_list = []
    for idx in range(len(s)):
        tmp += s[idx]
        if (idx + 1) % max_col == 0:
            my_list.append(tmp)
            tmp = ""
    my_list.append(tmp)

    ret = []
    for idx in range(max_col):
        tmp = ""
        for w in my_list:
            if len(w) > idx:
                tmp += w[idx]
        ret.append(tmp)

    return ' '.join(ret)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    print(result)
    # fptr.write(result + '\n')
    #
    # fptr.close()
