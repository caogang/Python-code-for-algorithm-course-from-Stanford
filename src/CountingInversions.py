# -*- coding: utf-8 -*-
"""
Created by MarvinCao on 2016/9/2.
Count Inversions using MergeSort Algorithm
Complexity : O(nlogn)
"""
from time import clock
origin = '9876543210'


def count_split_inversions(sorted_left, sorted_right):
    n = len(sorted_left) + len(sorted_right)
    i = j = 0
    sorted_total = ''
    counts_split = 0
    for k in xrange(0, n):
        if i == len(sorted_left):
            sorted_total += sorted_right[j]
            j += 1
        elif j == len(sorted_right):
            sorted_total += sorted_left[i]
            i += 1
        elif sorted_left[i] <= sorted_right[j]:
            sorted_total += sorted_left[i]
            i += 1
        else:
            sorted_total += sorted_right[j]
            j += 1
            counts_split += (len(sorted_left) - i)
    return counts_split, sorted_total


def count_inversions(data):
    n = len(data)
    if n <= 1:
        return 0, data
    half_bit = n // 2
    counts_left, sorted_left = count_inversions(data[:half_bit])
    counts_right, sorted_right = count_inversions(data[half_bit:])
    counts_split, sorted_total = count_split_inversions(sorted_left, sorted_right)
    return counts_left + counts_right + counts_split, sorted_total

start = clock()
"""
calculate started
"""

counts, sorted_origin = count_inversions(origin)

"""
calculate ended
"""
finish = clock()

print 'Inversions Counts in %s : %d' % (origin, counts)
print 'Running time is %.15f seconds.' % (finish - start)
