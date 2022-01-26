# The standard form of a quadratic equation is:
# ax2 + bx + c = 0, where
# a, b and c are real numbers and
# a ≠ 0
# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = int(input("(ax2 + bx + c = 0) : please enter value of 'a'="))
b = int(input("(ax2 + bx + c = 0) : please enter value of 'b'="))
c = int(input("(ax2 + bx + c = 0) : please enter value of 'c'="))

# calculate the discriminant
d = (b ** 2) - (4 * a * c)

# find two solutions
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print('The solution are {0} and {1}'.format(sol1, sol2))

# Output
# Enter a: 1
# Enter b: 5
# Enter c: 6
# The solutions are (-3+0j) and (-2+0j)
