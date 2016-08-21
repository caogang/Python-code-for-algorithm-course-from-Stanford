# -*- coding: utf-8 -*-
"""
Integer Multiplication (The Karatsuba Multiplication Algorithm)
Input: 2 n-digit numbers x and y
Output: product x*y
"Primitive Operation"- add or multiply 2 single-digit
numbers
Created by MarvinCao on 2016/8/20.
"""
import math
from time import clock


def karatsuba_mul(x, y):
    if x == 0 or y == 0:
        return 0
    len_x = len(str(x))
    len_y = len(str(y))
    str_x = str(x)
    str_y = str(y)
    #print len_x, len_y
    if len_x == 1 and len_y == 1:
        return x * y
    else:
        len_max = len_x if len_x >= len_y else len_y
        half_bit = long(math.ceil(len_max / 2))
        #print full_factor, half_factor
        first_x = long(str_x[:-half_bit]) if half_bit < len_x else 0
        last_x = long(str_x[-half_bit:])
        first_y = long(str_y[:-half_bit]) if half_bit < len_y else 0
        last_y = long(str_y[-half_bit:])
        #print first_x, last_x
        #print first_y, last_y
        r1 = karatsuba_mul(first_x, first_y)
        r2 = karatsuba_mul(last_x, last_y)
        r3 = karatsuba_mul(first_x + last_x, first_y + last_y)
        r4 = r3 - r1 - r2
        r = long(str(r1) + half_bit*2*'0') + long(str(r4) + half_bit*'0') + r2
        return r

x = x_temp = 5678192834908324908092813983274981209840923849328038109284901284081203982892374892374897328947328947892374897324873289748932748923748973289472398478932749037490238490112312312222222222222222222222432421342341242318888888888888888888888888888888888888888888899999999999999999999999999923124354765867828903472904791204421
y = y_temp = 1234392840928340823049123478943578672190480923843287489273489723847823657826238947982374974573895629437928374092384987238946289374902374893475675217615237612863932874922738243423423534534645675675675673542343242342342344678236423333333333333333333333333333333333333333344444444444444444444444444444434234234544657863271

start = clock()
"""
calculate started
"""

sum = karatsuba_mul(x, y)

"""
calculate ended
"""
finish = clock()

print '%d * %d = %d' %(x, y, sum)
print 'Running time is %.15f seconds.' % ((finish - start)/10000)
