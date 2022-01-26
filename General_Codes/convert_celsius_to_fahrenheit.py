# Python Program to convert temperature in celsius to fahrenheit

# change this value for a different result
celsius = float(input("enter the temperature in celsius:"))

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
celsius = (fahrenheit - 32) / 1.8
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' % (celsius, fahrenheit))

# output
# 37.5 degree Celsius is equal to 99.5 degree Fahrenheit
