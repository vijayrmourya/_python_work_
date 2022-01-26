#!/usr/bin/env python
# coding: utf-8
# For the given array find the largest possible sum from the elements and the list of element

# input:
# 1 3 -5 6 -8 9 -4 2 9 7

# output:
# 37
# [1, 3, 6, 9, 2, 9, 7]

a = input("Please enter the array : ").split(' ')
b = [int(i) for i in a]
large_sum = 0
sum_elements = []
for i in b:
    old_sum = large_sum
    large_sum = large_sum + i
    if old_sum > large_sum:
        large_sum = old_sum
    else:
        sum_elements.append(i)
print("Largest sum is:", large_sum)
print("Array elements of largest sum", sum_elements)
