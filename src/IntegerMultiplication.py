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

x = x_temp = 56781231231231239080879787384989092938298019209083020391212222222222222222222323333
y = y_temp = 23333333333333333333333333333333333333333333333333333333333333333333333333333333333

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
