#!/bin/python3

import math
import os
import random
import re
import sys

sys.setrecursionlimit(999999)

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#


def nonDivisibleSubset(k, S):
    S_remainder = [s % k for s in S]  # 리스트에 포함된 모든 정수를 k로 나눈 나머지 계산
    result = 0  # 부분집합의 크기
    print(S_remainder)
    for i in range(1, k // 2 + 1):  # (1, k-1), (2, k-2), ... 순회
        print("i : {}".format(i))
        print("k - i : {}".format(k - i))
        if i != k - i: # 두개의 합이 k가 되면 두 element의 합이 k 이므로 제외 시켜야함.
            # i를 나머지로 갖는 정수들과 k-i를 나머지로 갖는 정수들 중 더 많은 쪽을 포함시킴.
            result += max(S_remainder.count(i), S_remainder.count(k - i))
        else:
            # k로 나눈 나머지가 k//2인 정수가 있는지 확인하여 하나만 포함시킴. 예를들어 k : 100, 나머지가 50이면 50+50 이었을때 k로 나누어 떨어지기 때문.
            print("S_remainder.count(i) : {}".format(S_remainder.count(i)))
            print("bool(S_remainder.count(i)) : {}".format(bool(S_remainder.count(i))))
            print("int(bool(S_remainder.count(i))) : {}".format(int(bool(S_remainder.count(i)))))
            result += int(bool(S_remainder.count(i)))

    result += int(bool(S_remainder.count(0)))  # k로 나눈 나머지가 0인 정수가 있는지 확인하여 하나만 포함시킴. k로 나눈 나머지가 2개면 두 정수를 더햇을때 나머지가 0이기 때문

    return result


if __name__ == '__main__':
    # fptr = open(os.environbron['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    print(result)
    #
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
