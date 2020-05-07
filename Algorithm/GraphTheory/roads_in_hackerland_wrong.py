#!/bin/python3

import os
import sys

#
# Complete the roadsInHackerland function below.
#
def roadsInHackerland(n, roads):
    edges = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    for road in roads:
        v1, v2, cost = road
        edges[v1][v2] = 2 ** cost
        edges[v2][v1] = 2 ** cost

    result = []

    for idx in range(1, n + 1):
        cnt = 0
        start_node = idx
        D = [2 * (10 ** 5)] * (n + 1)
        C = [-1] * (n + 1)
        D[start_node] = 0
        while cnt != n:
            C[start_node] = 1
            connected_node = []
            for node in range(1, len(edges[start_node])):
                if edges[start_node][node] != -1:
                    if D[node] > D[start_node] + edges[start_node][node]:
                        D[node] = D[start_node] + edges[start_node][node]
                    connected_node.append((D[node], node))

            min_val_node_cost = 2 * 10 ** 5
            min_val_node = -1
            for tmp in connected_node:
                if C[tmp[1]] != -1:
                    continue
                else :
                    if min_val_node_cost > tmp[0]:
                        min_val_node = tmp[1]
                        min_val_node_cost = tmp[0]

            start_node = min_val_node
            cnt += 1
        for item in D[D.index(0)+1:]:
            if item != 2 * (10 ** 5):
                result.append(item)

    print(result)
    print(format(sum(result), 'b'))
    return format(sum(result), 'b')


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
