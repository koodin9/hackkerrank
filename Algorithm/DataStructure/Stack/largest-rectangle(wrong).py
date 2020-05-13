#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    s = []
    ans = len(h)
    h.append(0)
    print(h)
    for i in range(len(h)):
        left_index = i
        print("now i : {}".format(i))
        while len(s) > 0 and s[-1][0] >= h[i]: # 스택이 비어있지 않고 현재 빌딩에서 바로 왼쪽에 있는 빌딩의 높이가 현재 높이보다 크다면(왼쪽으로 확장 가능한 경우)
            print(s)
            last = s.pop() # 현재 빌딩의 왼쪽 빌딩 정보를 스택에서 pop한다(스택은 현재 빌딩에서 가장 인접한 순서로 데이터를 저장할 수 있음)
            # last[0] : 현재 빌딩 직전 빌딩의 높이, last[1] : 그 빌딩의 인덱스
            left_index = last[1] # 왼쪽으로 인접한 빌딩의 인덱스 정보를 받아옴.
            ans = max(ans, h[i] * (i + 1 - last[1])) # 현재 빌딩 높이를 가지며 가장 인접한 순서대로 left side의 직사각형 크기를 구해준다. (i + 1 -
            # last[1])은 밑변의 크기를 구해줌.
            ans = max(ans, last[0] * (i - last[1])) # 혹은 처음 desc 가 된 빌딩의 높이보다 stack에 들어있는 빌딩의 높이 중 그 보다 작은것이 있고,
            # 그 빌딩의 시작점 부터 현재 빌딩의 idx까지(h[i]가 아닌 last[0]의 높이를 가진 빌딩)이 더 큰 경우가 있을 경우
        s.append((h[i], left_index))

    return ans

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    print(result)
    #
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
