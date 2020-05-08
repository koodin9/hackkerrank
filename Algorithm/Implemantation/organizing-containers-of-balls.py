#!/bin/python3

import math
import os
import random
import re
import sys
# Simple Logic And Solution in Python3 As asked in the question, we have a multi-dimensional array or list. So it'll
# definitely contains n-number of rows and columns as well. By counting the sum of each elements in a row we can get
# the number of place in each container. And can get the total number of ball of perticular type by counting the sum
# of elements in a column. Then we'll get two arrays #mr(matrix-row) & #mr(matrix-column) by appending the calculated
# sums to it's list (counted row to #mr & counted column to #mc). Then by sorting the both lists we'll get both the
# list in an ascending order. Then comes the final test, if both the lists matches the then organizing of balls is
# POSSIBLE otherwise it's IMPOSSIBLE. Complete the organizingContainers function below.
def organizingContainers(container):
    mr = [] # 컨테이너의 자리. swap은 1:1 교환이므로 각 컨테이너에 들어갈 수 있는 공의 갯수는 정해져 있다.
    mc = [] # 각 공의 갯수. 공의 갯수는 colume을 각각 더해서 숫자를 구할 수 있으며 각 자리에 맞는 갯수가 있어야 하므로 두개의 리스트를 비교하는것으로 해결 가능
    n = len(container)
    for i in range(0, n):
        print(container[i])
        mr.append(sum(container[i]))
        tot = 0
        for j in range(0, n):
            tot += container[j][i]
            print("tot : {}".format(tot))
        mc.append(tot)
    mr.sort()
    mc.sort()

    print("mr : {}".format(mr))
    print("mc : {}".format(mc))

    if mr == mc:
        return "Possible"
    else:
        return "Impossible"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)
        print(result)
    #     fptr.write(result + '\n')
    #
    # fptr.close()
