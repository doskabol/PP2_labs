#1
n = int(input())
def sq(n):
    s = []
    for i in range(n + 1):
        s.append(i**2)
    return s

print(sq(n))

#2
n = int(input())
def even(n):
    e = []
    for i in range(n+1):
        if i % 2 == 0:
            e.append(i)
    return e

num = even(n)
print(*num, sep = ",")

#3
n = int(input())
def div(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


print(*div(n), sep=", ")

#4
l = int(input())
r = int(input())

def squares(l, r):
    for i in range(l, r + 1):
        yield i ** 2

print(*squares(l, r), sep=', ')

#5
n = int(input())

def down(n):
    for i in range(n, 0, -1):
        yield i

print(*down(n))

