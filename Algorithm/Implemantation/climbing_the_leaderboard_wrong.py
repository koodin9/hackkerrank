#!/bin/python3

import math
import os
import random
import re
import sys
#https://github.com/sapanz/Hackerrank-Problem-Solving-Python-Solutions/blob/master/HackerRank-Climbing%20the%20Leaderboard/Climbing_the_Leaderboard.py
# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scores = sorted(list(set(scores)))
    index = 0
    rank_list = []
    n = len(scores)
    for i in alice:
        print(scores)

        while (n > index and i >= scores[index]):
            print("i : {}".format(i))
            print("scores[index] : {}".format(scores[index]))
            index += 1
        print("n : {}".format(n))
        print("index : {}".format(index))
        rank_list.append(n+1-index)
    return rank_list

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
