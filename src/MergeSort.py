# -*- coding: utf-8 -*-
"""
Created by MarvinCao on 2016/8/22.
"""
from time import clock
import random

# l_origin = [1, 2, 90, 0, 12, 8, 21, 23, 20]  # list to be sorted
l_base = range(0, 1000000)
l_origin = random.sample(l_base, 30)  # generate the ramdom list


def merge(l1, l2):
    n = len(l1) + len(l2)
    i = j = 0
    l_return = list()
    for k in xrange(0, n):
        if i == len(l1):
            l_return.append(l2[j])
            j += 1
        elif j == len(l2):
            l_return.append(l1[i])
            i += 1
        elif l1[i] <= l2[j]:
            l_return.append(l1[i])
            i += 1
        else:
            l_return.append(l2[j])
            j += 1
    return l_return


def merge_sort(l1):
    n = len(l1)
    if n <= 1:
        return l1
    half_bit = n // 2
    l_first = merge_sort(l1[:-half_bit])
    l_last = merge_sort(l1[-half_bit:])
    l_return = merge(l_first, l_last)
    return l_return


start = clock()
"""
calculate started
"""

l_sorted = merge_sort(l_origin)

"""
calculate ended
"""
finish = clock()

print 'Before sorting : %r' % l_origin
print 'After sorting : %r' % l_sorted
print 'Running time is %.15f seconds.' % ((finish - start)/10000)
