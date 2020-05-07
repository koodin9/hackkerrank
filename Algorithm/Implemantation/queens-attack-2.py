#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
# def move_queen(n, updated_row, updated_col, r, c, obstacles):
#     p = 0
#     while True:
#         r = updated_row(r)
#         c = updated_col(c)
#         key = (r - 1) * n + c
#         if (c < 1 or c > n or r < 1 or r > n) or (key in obstacles):
#             return p
#         p += 1
#     return p
#
#
# # Complete the queensAttack function below.
# def queensAttack(n, k, r_q, c_q, obs):
#     obstacles = {}
#     for b in obs:
#         obstacles[(b[0] - 1) * n + b[1]] = None
#
#     p = 0
#     dr = [-1, -1, -1, 0, 0, 1, 1, 1]
#     dc = [0, -1, 1, 1, -1, 0, 1, -1]
#
#     for i in range(8):
#         p += move_queen(n, (lambda r: r + dr[i]), (lambda c: c + dc[i]), r_q, c_q, obstacles)
#
#     return p
def queensAttack(n, k, r_q, c_q, obstacles):
    # print(obstacles)
    dx = [-1,0,1,1,1,0,-1,-1]
    dy = [1,1,1,0,-1,-1,-1,0]

    # chess_plate = [[0 if i == 0 else 1 for i in range(n+1)] for _ in range(n+1)]
    # chess_plate[0] = [0 for _ in range(n+1)]

    # for o in obstacles:
    #     chess_plate[o[0]][o[1]] = 0
    # chess_plate[r_q][c_q] = -1

    ans = 0
    # for i in chess_plate:
    #     print(i)
    for item in zip(dx, dy):
        vx = item[0]
        vy = item[1]
        # print("vx :{}, vy : {}".format(vx,vy))
        start_r = r_q
        start_c = c_q
        # print("start_r : {}, start_c : {}".format(start_r, start_c))
        while True:
            start_r += vx
            start_c += vy
            # print("start_r : {}, start_c : {}".format(start_r, start_c))
            # if 1 <= start_r <= n and  1 <= start_c <= n and chess_plate[start_r][start_c] != 0:
            # print("obstacles.count([{},{}]) : {}".format(start_r, start_c, obstacles.count([start_r,start_c])))
            if 1 <= start_r <= n and  1 <= start_c <= n and not [start_r,start_c] in obstacles:
                # print("now : [{}][{}]".format(start_r, start_c))
                ans += 1
            else:
                break

        # print("==========================")
    return ans

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
