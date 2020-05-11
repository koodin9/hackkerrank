#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
# def almostSorted(arr):
#     sorted_arr = sorted(arr)
#     first_non_ordered_idx = None
#     for i in range(1, len(arr)):
#         if arr[i-1] > arr[i] and not first_non_ordered_idx:
#             first_non_ordered_idx = i
#             print("first_non_ordered_idx : {}".format(first_non_ordered_idx))
#             if arr[:i-1] + [arr[i]] + [arr[i-1]] == sorted_arr:
#                 print("yes")
#                 print("swap {} {}".format(i, i+1))
#         if i == len(arr) - 1:
#             print("last!")
#             if arr[:i-1] + [arr[i]] + [arr[i-1]] == sorted_arr:
#                 print("yes")
#                 print("swap {} {}".format(i, i+1))
#             else:
#                 between_list = arr[first_non_ordered_idx:i]
#                 dsc_list = sorted(between_list, reverse=True)
#                 if between_list == dsc_list:
#                     print("reverse {} {}".format(first_non_ordered_idx - 1, i))
#                 else:
#                     print("no")
#         if first_non_ordered_idx and arr[i] > arr[first_non_ordered_idx-1]:
#             print("hi")
#             print(i)
#             print(arr[i+1:])
#             if arr[i+1:] != sorted(arr[i+1:]):
#                 print("no")
#                 break
#
#             between_list = arr[first_non_ordered_idx:i]
#             asc_list = sorted(between_list)
#             dsc_list = sorted(between_list, reverse=True)
#
#             print("yes")
#             if between_list == asc_list:
#                 print("swap {} {}".format(first_non_ordered_idx-1, i))
#             if between_list == dsc_list:
#                 print("reverse {} {}".format(first_non_ordered_idx - 1, i))
#
#             print("between_list : {}".format(between_list))
#             print("asc_list : {}".format(asc_list))
#             print("dsc_list : {}".format(dsc_list))
#
#             break



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
