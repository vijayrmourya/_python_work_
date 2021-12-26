# You have to write a program to transform input array into output array.
# Input Array :  2,4,8,5,12,15,6,10,7,30,25,43,46,45,21
# Output Array :  2,4,8, 12, 6, 7, 43,46,21, 5,15,10,30,25,45
# IMPORTANT: Do not use duplicate or extra array, your program will be rejected if you use extra array.
# Hint: All multiples of 5 are moved to last
a = [2, 4, 8, 5, 12, 15, 6, 10, 7, 30, 25, 43, 46, 45, 21]
change = 0
x = len(a) - 1
i = 0
while i < x:
    i = i + 1
    if a[i] % 5 == 0:
        a.append(a.pop(i))
        i = i - 1
        x = x - 1
print(a)
