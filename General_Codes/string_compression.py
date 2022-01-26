#!/usr/bin/env python
# coding: utf-8
# Compress the given word string

# input:
# aaaAAasHJIYVhkBYUVhbhVBIbtguvU

# output:
# a4A2s1H1J1I2Y2V3h3k1B2U2b2t1g1u1v1

a = input()
a = a.replace(' ', '')
x = []
b = ''
for i in a:
    if i not in x:
        x.append(i)
for i in x:
    b = b + i + str(a.count(i))
print(b)
