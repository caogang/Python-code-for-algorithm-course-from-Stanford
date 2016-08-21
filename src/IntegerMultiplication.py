# -*- coding: utf-8 -*-
"""
Integer Multiplication (The Grade School Algorithm)
Input: 2 n-digit numbers x and y
Output: product x*y
"Primitive Operation"- add or multiply 2 single-digit
numbers
Created by MarvinCao on 2016/8/20.
"""
from time import clock

x = x_temp = 5678192834908324908092813983274981209840923849328038109284901284081203982892374892374897328947328947892374897324873289748932748923748973289472398478932749037490238490112312312222222222222222222222432421342341242318888888888888888888888888888888888888888888899999999999999999999999999923124354765867828903472904791204421
y = y_temp = 1234392840928340823049123478943578672190480923843287489273489723847823657826238947982374974573895629437928374092384987238946289374902374893475675217615237612863932874922738243423423534534645675675675673542343242342342344678236423333333333333333333333333333333333333333344444444444444444444444444444434234234544657863271

#print 'Integer x is %d.' % x_temp
#print 'Integer y is %d.' % y_temp

"""
generate the integer list
"""
x_list = []
while x_temp // 10 != 0:
    single_digit = x_temp % 10
    x_list.append(single_digit)
    x_temp //= 10
x_list.append(x_temp)
y_list = []
while y_temp // 10 != 0:
    single_digit = y_temp % 10
    y_list.append(single_digit)
    y_temp //= 10
y_list.append(y_temp)

#print 'The reverse order of Integer x is %r.' % x_list
#print 'The reverse order of Integer y is %r.' % y_list

start = clock()
"""
calculate the integer multiplication
"""
sum_list = []
y_bit = 1
for y_ele in y_list:
    carry_bit = 0
    sum_ele = 0
    x_bit = 1
    for x_ele in x_list:
        single_sum = x_ele * y_ele + carry_bit
        single_digit = single_sum % 10
        carry_bit = single_sum // 10
        sum_ele += single_digit * x_bit
        x_bit *= 10
    if carry_bit != 0:
        sum_ele += carry_bit * x_bit
    sum_list.append(sum_ele * y_bit)
    y_bit *= 10

#print 'Elements to sum are %r.' % sum_list

sum = sum(sum_list)
"""
calculate ended
"""
finish = clock()

print '%d * %d = %d' %(x, y, sum)
print 'Running time is %.15f seconds.' % ((finish - start)/10000)
