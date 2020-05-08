#!/bin/python3

import os
import sys

#
# Complete the twoStacks function below.
#
def twoStacks(x, a, b, n, m):
    total = 0
    atmp = []
    print(a)
    print(b)
    for i in range(n):
        val = a.pop()
        if total + val > x:
            break
        total += val
        atmp.append(val)
    print(atmp)
    print(total)
    max_count = len(atmp)
    cur_count = max_count
    while m:
        print("m : {}".format(m))
        print("total + b[-1] : {}".format(total + b[-1]))
        if total + b[-1] <= x:
            total += b.pop()
            m -= 1
            cur_count += 1
            if cur_count > max_count:
                print("cur_count : {}".format(cur_count))
                max_count = cur_count
            continue
        if not len(atmp):
            break
        aval = atmp.pop()
        print("atmp : {}".format(atmp))

        total -= aval
        cur_count -= 1

    return max_count

# def twoStacks(x, a, b):
#     #
#     # Write your code here.
#     #
#     subtotal = 0
#     cnt = 0
#     while subtotal < x:
#         if not a or not b:
#             if not a:
#                 subtotal += b.pop()
#             else:
#                 subtotal += a.pop()
#         else:
#             if a[0] < b[0]:
#                 t = a.pop(0)
#                 subtotal += t
#                 print("a pop : {}".format(t))
#             else:
#                 t = b.pop(0)
#                 subtotal += t
#                 print("b pop : {}".format(t))
#             cnt += 1
#
#         if subtotal > x:
#             cnt -= 1
#         # print("a : {}".format(a))
#         # print("b : {}".format(b))
#         print("subtotal : {}".format(subtotal))
#
#     return cnt


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, reversed(input().strip().split(' '))))
        b = list(map(int, reversed(input().strip().split(' '))))

        result = twoStacks(x, a, b, n, m)

        print(result)
    #     fptr.write(str(result) + '\n')
    #
    # fptr.close()
