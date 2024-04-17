# 1 Upper Сase
class StringManipulator: 
    def __init__(self): 
        self.text = "" 
 
    def getString(self): 
        self.text = input("String: ") 
 
    def printString(self): 
        print(self.text.upper()) 
 
str_obj = StringManipulator() 
str_obj.getString() 
str_obj.printString() 

# 2
'''class Shape: 
    def area(self): 
        return 0 
 
 
class Square(Shape): 
    def __init__(self, length): 
        self.length = length 
 
    def area(self): 
        return self.length ** 2 
 
 
# Usage 
square = Square(5) 
print("Square area:", square.area())  # Output: 25 
 
shape = Shape() 
print("Default shape area:", shape.area())  # Output: 0 

# 3
class Shape: 
    def area(self): 
        return 0 
 
class Rectangle(Shape): 
    def __init__(self, length, width): 
        self.length = length 
        self.width = width 
 
    def area(self): 
        return self.length * self.width 
 
rectangle = Rectangle(5, 3) 
print("Rectangle area:", rectangle.area())  # 15 
shape = Shape() 
print("Default shape area:", shape.area())  # 0 

# 4
import math 
 
class Point: 
    def __init__(self, x=0, y=0): 
        self.x = x 
        self.y = y 
 
    def show(self): 
        print(f"Point({self.x}, {self.y})") 
 
    def move(self, x, y): 
        self.x = x 
        self.y = y 
 
    def dist(self, other_point): 
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) 
p1 = Point(3, 4) 
p2 = Point(7, 1) 
 
p1.show()   
p2.show()   
 
p1.move(5, 6) 
p1.show()  
 
print("Distance between points:", p1.dist(p2))   

# 5
class Bank(): 
    def __init__(self, account, money): 
        self.money = money 
        self.account = account 
 
    def balance(self): 
        return self.money 
     
    def owner(self): 
        return self.account 
     
    def deposit(self, money): 
        self.money+=money 
 
        return f"You are deposit {money} money" 
     
    def withdraw(self, money): 
        if self.money - money < 0: 
            return "insufficient funds" 
        else: 
            self.money-=money 
 
            return f"you're balance: {self.money},  and you take {money}" 
         
         
bank = Bank("Dosbol", 12500) 
 
print(bank.balance()) 
 
print(bank.owner()) 
 
print(bank.deposit(500)) 
 
print(bank.withdraw(30000)) 
 
print(bank.withdraw(2500))
# 6
class Prime: 
    def __init__(self, numbers): 
        self.numbers = numbers 
 
    def is_prime(self, num): 
        if num < 2: 
            return False 
        for i in range(2, int(num**0.5) + 1): 
            if num % i == 0: 
                return False 
        return True 
 
    def filter_prime_numbers(self): 
        return list(filter(lambda x: self.is_prime(x), self.numbers)) 
 
n = int(input("n: ")) 
mylist = [] 
for i in range(n): 
    number = int(input("number: ")) 
    mylist.append(number) 
 
prime_filter = Prime(mylist) 
print(prime_filter.filter_prime_numbers())'''