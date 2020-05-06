#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    alice_rank = []
    scores_mark = [0] * len(scores)
    for a in alice:
        tmp = list(zip(scores, scores_mark))
        tmp.append((a, 1))
        tmp.sort(reverse=True)

        rank_board = []

        for i in range(len(tmp)):
            if not rank_board:
                rank_board.append(1)
            else:
                if tmp[i-1][0] == tmp[i][0]:
                    rank_board.append(rank_board[i - 1])
                else:
                    rank_board.append(rank_board[i - 1] + 1)
            if tmp[i][1] == 1:
                break

        for item in list(zip(rank_board, tmp)):
            if item[1][1] == 1:
                alice_rank.append(item[0])
                break

    return alice_rank

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
