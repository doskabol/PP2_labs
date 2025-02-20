#1
import math
n = int(input())
r = math.radians(n)
print(r)

#2
h = float(input())
b1 = float(input())
b2 = float(input())
a = ((b1 + b2) * h) / 2
print(a)

#3
import math
n = int(input()) #number of sides
l = float(input()) #length of sides
a = (n * (l**2)) / 4 * (math.tan(math.pi / n))
print(round(a, 1))

#4
a = float(input())
b = float(input())
s = a * b
print(s)