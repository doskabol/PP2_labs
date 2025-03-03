#1 "a" followed by zero or more "b"
import re

a = input()
print(bool(re.fullmatch(r"ab*", a)))
# a = True
# abbb = True
# abc = False

#2 "a" followed by 2-3 "b"
import re

a = input()
print(bool(re.fullmatch(r"ab{2,3}", a)))

# abb = True
# abbb = True
# a = False
# abbbbbb = False


#3 lowercase connected with undercore
import re

a = input()
print(bool(re.fullmatch(r"[a-z]+_[a-z]+", a))) 

#hello_world = True
#helloworld = False
#HeLlO_WoRld = False

#4 upper case followed by lower case

import re 

a = input()
print(bool(re.fullmatch(r"[A-Z][a-z]+", a)))

# Hello = True
# HELLO = False
# hello = False

#5 string that starts with "a" and ends with "b"
import re

a = input()
print(bool(re.fullmatch(r"a.*b", a)))


#6 replace space, comma and dot with :
import re

a = input()
b = re.sub(r"[ ,.]", ":", a)
print(b)

# "Hello, world. How are you?" => "Hello:world:How:are:you?"

#7 snake string to camel string
import re
def snake_to_camel(snake):
    return re.sub(r'_+', ' ', snake).title().replace(" ", "")

a = input()
print(snake_to_camel(a))

#ab_cd = AbCd
#hello_world = HelloWorld

#8 split by uppercase
import re 

a = input()
print(re.split(r"[A-Z]", a))

# HelloWorld = Hello World
# AbcdEfg = Abcd Efg

#9 insert spaces by capital letters
import re

a = input()
b = re.sub(r'([a-z])([A-Z])', r'\1 \2', a)
print(b)

# HelloWorld = Hello World
# AbcdEfg = Abcd Efg


#10 camel to snake
import re

def camel_to_snake(camel):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', a).lower()

a = input
print(camel_to_snake(a))



