#1 multiply list
import math
nums = [2, 3, 4, 5]
result = math.prod(nums)
print(result)

#2 sum of uppercase and lowercase
a = "Hello World"
su = 0
sl = 0
for i in a:
    if i.isupper():
        su += 1
    elif i.islower():
        sl += 1
print(su, sl)

# (2, 8) output

#3 palindrome
a = "qazaq"
if a == a[::-1]:
    print("Yes")
else:
    print("No")

#4 delay
import time, math

number = int(input())
delay = int(input())

time.sleep(delay / 1000)

print(f"Square root of {number} after {delay} milliseconds is {math.sqrt(number)}")

#5 tuple true
t = (True, 1, "hello", 5)
print(all(t))

