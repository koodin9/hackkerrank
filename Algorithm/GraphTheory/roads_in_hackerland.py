#!/bin/python3

import os
import sys

#
# Complete the roadsInHackerland function below.
#
def roadsInHackerland(n, roads):
    #
    # Write your code here.
    #
    for start in range(1, n+1):
        print("start : {}".format(start))
        D = [2 * 10 **5] * (n + 1)

        for visiting_node in range(1, n+1):
            if visiting_node == start:
                D[visiting_node] = 0
            for road in roads:
                if road[0] == visiting_node:
                    if D[road[1]] > D[visiting_node] + 2**road[2]:
                        D[road[1]] = D[visiting_node] + 2**road[2]
                if road[1] == visiting_node:
                    if D[road[0]] > D[visiting_node] + 2**road[2]:
                        D[road[0]] = D[visiting_node] + 2**road[2]

        print(D)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    roads = []

    for _ in range(m):
        roads.append(list(map(int, input().rstrip().split())))

    result = roadsInHackerland(n, roads)

    # fptr.write(result + '\n')
    #
    # fptr.close()
