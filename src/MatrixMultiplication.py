# -*- coding: utf-8 -*-
"""
Input: Two N by N Matrix: X and Y (For simplicity, make an assumption that N is 2^num)
Output: X * Y
Algorithm BaseLine: Straight forward algorithm
Complexity BaseLine: O(N^3) cubic time
Algorithm 1: Divide and Conquer Algorithm
Complexity 1: the same as straight forward algorithm. O(N^3)
Algorithm 2: Strassen's Subcubic Algorithm based on Divide and Conquer Algorithm
Complexity 2: Subcubic running time by only saving a recursive call, beating the cubic time
Created by MarvinCao on 2016/9/3.
"""
from time import clock
import numpy as np
import random
import pylab as pl

test_data = []
'Random case'
l_base = np.linspace(0, 1000, 100000000)
for i in xrange(1, 9):
    n = 2 ** i
    count = n ** 2
    l_origin = random.sample(l_base, count)  # generate the random list
    X = np.reshape(l_origin, (n, n))
    l_origin = random.sample(l_base, count)  # generate the random list
    Y = np.reshape(l_origin, (n, n))
    test_data.append((n, (X, Y)))

result_temp = np.zeros((10000, 10000))       # A big array referred to a temp storage


"""
Algorithm BaseLine: Straight forward algorithm O(N^3)
"""
def mul_baseline(x, y):
    diamension_x = x.shape[0]
    diamension_y = y.shape[0]
    if diamension_x != diamension_y or diamension_x == diamension_y == 0:
        return result_temp, -1
    for i in xrange(0, diamension_x):
        for j in xrange(0, diamension_y):
            sum_ele = 0
            for k in xrange(0, diamension_x):
                sum_ele += (x[i][k] * y[k][j])
            result_temp[i, j] = sum_ele
    return result_temp[:diamension_x, :diamension_y], 0

n_list = []
time_list = []
print 'Algorithm Baseline: Brute Force'
for ele in test_data:
    n = ele[0]
    data = ele[1]
    X = data[0]
    Y = data[1]
    start = clock()
    Z, error = mul_baseline(X, Y)
    finish = clock()
    time = finish - start
    if error == 0:
        # print '%r \n*\n %r \n=\n %r' % (X, Y, Z)
        pass
    else:
        print 'Input error'
    print '%4d <--------> %.15f seconds.' % (n, time)
    n_list.append(n)
    time_list.append(time)
pl.plot(n_list, time_list, 'r')

'''
Algorithm 1: Divide and conquer algorithm O(N^3)
'''
def combine(ae, bg, af, bh, ce, dg, cf, dh):
    half = ae.shape[0]
    err = 0
    result_temp[:half, :half] = ae + bg
    result_temp[:half, half:2*half] = af + bh
    result_temp[half:2*half, :half] = ce + dg
    result_temp[half:2*half, half:2*half] = cf + dh
    return result_temp[:half*2, :half*2], err


def mul_dc(x, y):
    diamension_x = x.shape[0]
    diamension_y = y.shape[0]
    if diamension_x != diamension_y or diamension_x == diamension_y == 0:
        return result_temp, -1
    'Boundary condition'
    if diamension_x == diamension_y == 1:
        result_temp[0, 0] = x[0, 0] * y[0, 0]
        return result_temp[:1, :1], 0
    half = diamension_x / 2
    a = x[:half, :half]
    b = x[:half, half:]
    c = x[half:, :half]
    d = x[half:, half:]
    e = y[:half, :half]
    f = y[:half, half:]
    g = y[half:, :half]
    h = y[half:, half:]
    ae, err = mul_dc(a, e)
    bg, err = mul_dc(b, g)
    af, err = mul_dc(a, f)
    bh, err = mul_dc(b, h)
    ce, err = mul_dc(c, e)
    dg, err = mul_dc(d, g)
    cf, err = mul_dc(c, f)
    dh, err = mul_dc(d, h)
    result, err = combine(ae, bg, af, bh, ce, dg, cf, dh)
    return result, err

n_list = []
time_list = []
print 'Algorithm 1: Divide and conquer algorithm'
for ele in test_data:
    n = ele[0]
    data = ele[1]
    X = data[0]
    Y = data[1]
    start = clock()
    Z, error = mul_dc(X, Y)
    finish = clock()
    time = finish - start
    if error == 0:
    #    print '%r \n*\n %r \n=\n %r' % (X, Y, Z)
        pass
    else:
        print 'Input error'
    print '%4d <--------> %.15f seconds.' % (n, time)
    n_list.append(n)
    time_list.append(time)
pl.plot(n_list, time_list, 'g')


'''
Algorithm 2: Strassen's Subcubic Algorithm based on Divide and Conquer Algorithm
'''
def combine_strassen(p1, p2, p3, p4, p5, p6, p7):
    half = p5.shape[0]
    err = 0
    result_temp[:half, :half] = p5 + p4 - p2 + p6
    result_temp[:half, half:half*2] = p1 + p2
    result_temp[half:half*2, :half] = p3 + p4
    result_temp[half:half*2, half:half*2] = p1 + p5 - p3 - p7
    return result_temp[:half*2, :half*2], err


def mul_strassen(x, y):
    diamension_x = x.shape[0]
    diamension_y = y.shape[0]
    if diamension_x != diamension_y or diamension_x == diamension_y == 0:
        return result_temp, -1
    'Boundary condition'
    if diamension_x == diamension_y == 1:
        result_temp[0, 0] = x[0, 0] * y[0, 0]
        return result_temp[:1, :1], 0
    half = diamension_x / 2
    a = x[:half, :half]
    b = x[:half, half:]
    c = x[half:, :half]
    d = x[half:, half:]
    e = y[:half, :half]
    f = y[:half, half:]
    g = y[half:, :half]
    h = y[half:, half:]
    p1, err = mul_strassen(a, f - h)
    p2, err = mul_strassen(a + b, h)
    p3, err = mul_strassen(c + d, e)
    p4, err = mul_strassen(d, g - e)
    p5, err = mul_strassen(a + d, e + h)
    p6, err = mul_strassen(b - d, g + h)
    p7, err = mul_strassen(a - c, e + f)
    result, err = combine_strassen(p1, p2, p3, p4, p5, p6, p7)
    return result, err

n_list = []
time_list = []
print 'Algorithm 2: Strassen Algorithm based on Divide and Conquer Algorithm'
for ele in test_data:
    n = ele[0]
    data = ele[1]
    X = data[0]
    Y = data[1]
    start = clock()
    Z, error = mul_strassen(X, Y)
    finish = clock()
    time = finish - start
    if error == 0:
        # print '%r \n*\n %r \n=\n %r' % (X, Y, Z)
        pass
    else:
        print 'Input error'
    print '%4d <--------> %.15f seconds.' % (n, time)
    n_list.append(n)
    time_list.append(time)
pl.plot(n_list, time_list, 'b')

pl.show()
