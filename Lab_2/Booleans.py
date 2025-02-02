#Example
print(10 > 9)
print(10 == 9)
print(10 < 9)

#Print a message based on whether the condition is True or False:
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Evaluate a string and a number:
print(bool("Hello"))
print(bool(15))

#The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#example
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


#Check if an object is an integer or not:
x = 200
print(isinstance(x, int))

