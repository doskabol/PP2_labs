#1
def ounc(grams):
    ounces = 28.3495231 * grams
    return ounces

#2
def centigrade(far):
    C = (5 / 9) * (far - 32)
    return C

#3
def solve(numheads, numlegs):
    if numlegs % 2 != 0 or numlegs < 2 * numheads or numlegs > 4 * numheads:
        return None, None

    x = (4 * numlegs - numheads) // 2
    y = numheads - x
    return x,y 

#4
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(nums):
    return [num for num in nums if is_prime(num)]


#5
import itertools

def perm(string):
    perms = itertools.permutations(string)
    
    for perm in perms:
        print(''.join(perm))
        
string = input()
perm(string)


#6
def rev(sen):
    ws = sen.split()
    rever = []
    
    for w in ws:
        rever.insert(0, w)
    
    return ' '.join(rever)

s = input()
print(rev(s))


#7
def has_33(a):
    for i in range(len(a) - 1):
        if a[i] == 3 and a[i + 1] == 3:
            return True
    return False

#8
def spy_game(a):
    for i in range(len(a) - 1):
        if a[i] == 0 and a[i + 1] == 0 and a[i+2] == 7:
            return True
    return False

#9
def vol(radi):
    v = (4 * 3.14 * (pow(radi, 3))) / 3
    return v

#10
def uniq(a):
    unique = []
    for i in a:
        if i not in unique:
            unique.append(i)
    return unique

#11
def pal(a):
    for i in range(len(a) // 2):  
        if a[i] == a[len(a) - i - 1]:  
            return True
    return False

#12
def histogram(lst):
    for num in lst:
        print('*' * num)

#13
import random

def g():
    print("Hello! What is your name?")
    n = input()

    print(f"\nWell, {n}, I am thinking of a number between 1 and 20.")

    x = random.randint(1, 20)
    c = 0

    while True:
        print("\nTake a guess.")
        try:
            g = int(input())
            c += 1

            if g < x:
                print("Your guess is too low.")
            elif g > x:
                print("Your guess is too high.")
            else:
                print(f"Good job, {n}! You guessed my number in {c} guesses!")
                break
        except ValueError:
            print("Please enter a valid number.")

g()

from functions1.py import ounc, rev, g

def main():
    grams = float(input("Enter weight in grams: "))
    print(f"{grams} grams is {ounc(grams)} ounces.")
    
    sen = input("Enter a sentence to reverse: ")
    print(f"Reversed sentence: {rev(sen)}")
    
    g()

if __name__ == "__main__":
    main()
