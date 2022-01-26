#!/usr/bin/env python
# coding: utf-8

# problem statement is to have 2 array 1st one with n elements and second one with same element as 1st but one random
# element weil be deleted find that missing element

# input:
# 1 3 9 7 4 2 6 8 5
# 9 7 1 3 6 8 4 2

# output:
# missing number is: 5

a = input().split(' ')
b = input().split(' ')
c = [int(i) for i in a]
d = [int(i) for i in b]
# solution1
print('missing number is: ' + str(sum(c) - sum(d)))

# solution2
flag = 0
for i in c:
    if i not in d:
        print('missing element is: {}'.format(i))
        flag = 1
        break
if flag == 0:
    print('no element missing')
