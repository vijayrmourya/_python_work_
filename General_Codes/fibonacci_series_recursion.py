# Fibonacci Sequence
# Enter a number and have the program generate the Fibonacci sequence of that length.
# input:
# 5
# output:
# 1
# 1
# 2
# 3
# 5

def fibonacciRecursion(numb):
    if (numb <= 1):
        return numb
    else:
        return (fibonacciRecursion(numb - 1) + fibonacciRecursion(numb - 2))

numb = int(input('Enter some random number = '))
print("The Fibonacci Sequence till the given number", numb, ' = ')
for n in range(numb):
    print('Number = ', fibonacciRecursion(n))
