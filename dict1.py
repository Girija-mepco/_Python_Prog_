# Read three integers from input
a = int(input())
b = int(input())
m = int(input())

# First line: result of a**b
print(pow(a, b))

# Second line: result of (a**b) % m
print(pow(a, b, m))
