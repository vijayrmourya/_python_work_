#!/usr/bin/env python
# coding: utf-8
# Give Two string inputs for the codes to check weather they are anagram or not

# Input:
# vijay 
# mourya

# Output:
# "vijay " & "mourya" are not Anagrams

a = input()
b = input()
c = a.replace(' ', '').lower()
d = b.replace(' ', '').lower()
##solution 1
if sorted(c) == sorted(d):
    print('"' + a + '" & "' + b + '" are Anagrams')
else:
    print('"' + a + '" & "' + b + '" are not Anagrams')

##solution 2
use = ''
if len(c) > len(d):
    use = c
else:
    use = d
flag = 1
for i in use:
    if c.count(i) == d.count(i):
        flag = 0
        continue
    else:
        flag = 1
        break
if flag == 1:
    print('"' + a + '" & "' + b + '" are not Anagrams')
else:
    print('"' + a + '" & "' + b + '" are Anagrams')
