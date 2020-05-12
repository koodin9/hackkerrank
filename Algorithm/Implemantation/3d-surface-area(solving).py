#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    tot = 0

    new_A = list(map(list, zip(*A)))
    print(A)
    print(new_A)

    for row in A:
        print(row)
        tot += max(row) * 2

        idx = -1
        queue = []
        lowest_box = None
        highest_box = None
        while idx != len(row)-1:
            idx += 1
            if row[idx] > row[idx+1]: # 내려가는 부분 찾기
                queue.append(idx)
            if row[idx] < row[idx+1]: # 다시 올라가는 부분
                queue.append(idx)
            if not highest_box:
                highest_box = row[idx]
            if highest_box < row[idx]:
                highest_box = row[idx]
            if not lowest_box:
                lowest_box = row[idx]
            if lowest_box > row[idx]:
                lowest_box = row[idx]
            if len(queue) == 2: # 패인 부분 확인 완료, tot에 계산하여 추가
                end_asc = queue.pop()
                start_desc = queue.pop()
                tot += row[start_desc] - lowest_box
                if highest_box < row[end_asc]:
                    tot += highest_box - lowest_box
                else:
                    tot += row[end_asc] - lowest_box
                highest_box = None
                lowest_box = None





    print("======================")

    for row in new_A:
        print(row)
        tot += max(row) * 2
        idx = -1
        queue = []
        lowest_box = None
        highest_box = None
        while idx != len(row) - 1:
            idx += 1
            if row[idx] > row[idx + 1]:  # 내려가는 부분 찾기
                queue.append(idx)
            if row[idx] < row[idx + 1]:  # 다시 올라가는 부분
                queue.append(idx)
            if not highest_box:
                highest_box = row[idx]
            if highest_box < row[idx]:
                highest_box = row[idx]
            if not lowest_box:
                lowest_box = row[idx]
            if lowest_box > row[idx]:
                lowest_box = row[idx]
            if len(queue) == 2:  # 패인 부분 확인 완료, tot에 계산하여 추가
                end_asc = queue.pop()
                start_desc = queue.pop()
                tot += row[start_desc] - lowest_box
                if highest_box < row[end_asc]:
                    tot += highest_box - lowest_box
                else:
                    tot += row[end_asc] - lowest_box
                highest_box = None
                lowest_box = None

        print(tot)

    tot += 2 * len(A) * len(new_A)
    return tot


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)
    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
