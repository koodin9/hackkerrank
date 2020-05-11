#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the larrysArray function below.
# only 3 len arr
def rotate_left(a):
    return a[1:] + [a[0]]




# def larrysArray(A):
#     A = a.copy()
#     target_idx = 1
#     print(a)
#     while True:
#         print("===============================")
#
#         print("target_idx : {}".format(target_idx))
#         now_idx = A.index(target_idx) # 대상 item의 현재 위치
#         print("now_idx : {}".format(now_idx))
#         if now_idx == 0: # 정렬 완료.
#             print("(target_idx - 1) : {}".format((target_idx - 1)))
#             A = A[target_idx:]
#             print("modified A : {}".format(A))
#             target_idx += 1  # 정렬된 위치로 옮겨줘야 하는 item
#             continue
#         print("A[:now_idx-2] : {}".format(A[:now_idx-2]))
#         print("A[now_idx:] : {}".format(A[now_idx+1:]))
#         tmp = rotate_left(A[now_idx-2:now_idx+1])
#         print("tmp : {}".format(tmp))
#         A = A[:now_idx-2] + tmp + A[now_idx+1:]
#
#         print(A)

def larrysArray(A):
    for i in range(len(A)-2):
        print("==========================")
        print("A : {}".format(A))
        if A[i]==i+1:
            continue
        else:
            print("i : {}".format(i))
            print("(A.index(i+1)) : {}".format((A.index(i+1))))

            print("(A.index(i+1)-i) : {}".format((A.index(i+1)-i)))
            if (A.index(i+1)-i)%2==0:
                print("hi")
                A.remove(i+1)
                print("A[:i] : {}".format(A[:i]))
                print("A[i:] : {}".format(A[i:]))

                A=A[:i]+[i+1]+A[i:]
            else:
                print("hi2")
                A.remove(i+1)
                print("A[:i] : {}".format(A[:i]))
                print("[A[i+1]]+[A[i]] : {}".format([A[i+1]]+[A[i]]))
                print("A[i+2:] : {}".format(A[i+2:]))
                A=A[:i]+[i+1]+[A[i+1]]+[A[i]]+A[i+2:]
    if A==sorted(A):
        return ("YES")
    else:
        return ("NO")


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)
        print(result)
    #     fptr.write(result + '\n')
    #
    # fptr.close()
