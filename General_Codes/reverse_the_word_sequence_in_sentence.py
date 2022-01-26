#!/usr/bin/env python
# coding: utf-8
# From the given sentence reverse sequence of all words

# input:
# oh yeah! you're much more of a Thanos.

# output
# Thanos. a of more much you're yeah! oh

# solution1
a = input()
b = a.split(' ')
b = b[::-1]
print(' '.join(b))

# solution2
a = input()
sent = ''
s = ''
for i in range(len(a) - 1, 0, -1):
    if a[i] != ' ':
        s = s + a[i]
        continue
    n = s[::-1]
    s = ''
    sent = sent + n + ' '
# for last word
s = ''
for i in range(0, len(a) - 1):
    if a[i] != ' ':
        s = s + a[i]
        continue
    sent = sent + s + ' '
    break
print(sent)
