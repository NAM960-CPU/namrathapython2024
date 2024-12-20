# -*- coding: utf-8 -*-
"""day3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hqHJYhykpabjlqwOgWiZKqz4ic0Hrw3s
"""



"""FUNCTION AND MODULES"""

def greet(name):
  print("hello," + name + "!")
greet("alice")

"""1 positional argument"""

def add(a,b):
  return a+b

print(add(5,3))

"""2  KEYWORD ARGUMENT"""

def greet(name, message):
  print(message + " ," + name + "!")
greet(name="alice", message="good morning")

"""3 DEFAULT ARGUMENTS"""

def greet(name,message="hello"):
  print(message + "," + name + "!")
greet ("alice")
greet("bob","hi")

"""VARIABLE LENGTH ARGUMENT"""

def rajesh(**numbers):
  for key, value in numbers.items():
        print(f"{key}: {value}")
rajesh(name="rajesh", age=25, city="new york")

"""RETURN STATEMENT"""

def square(num):
  return num * num
square(5)

result = square(7)
print("square is :" ,result)

"""MODULES

2 IMPORTING MODULE
"""

import math
print(math.sqrt(16))

"""IMPORT SPECIFIC FUNCTION"""

from math import pi, sin
print(pi)
print(sin(math.radians(90)))



Skip to main content
day3.ipynb
day3.ipynb_
All changes saved

[ ]

Start coding or generate with AI.
FUNCTION AND MODULES


[16]
0s
def greet(name):
  print("hello," + name + "!")
greet("alice")
hello,alice!
1 positional argument


[21]
0s
def add(a,b):
  return a+b

print(add(5,3))
8
2 KEYWORD ARGUMENT


[24]
0s
def greet(name, message):
  print(message + " ," + name + "!")
greet(name="alice", message="good morning")

good morning ,alice!
3 DEFAULT ARGUMENTS


[28]
0s
def greet(name,message="hello"):
  print(message + "," + name + "!")
greet ("alice")
greet("bob","hi")
hello,alice!
hi,bob!
VARIABLE LENGTH ARGUMENT


[33]
0s
def rajesh(**numbers):
  for key, value in numbers.items():
        print(f"{key}: {value}")
rajesh(name="rajesh", age=25, city="new york")
name: rajesh
age: 25
city: new york
RETURN STATEMENT


[46]
0s
def square(num):
  return num * num
square(5)



25

[47]
0s
result = square(7)
print("square is :" ,result)
square is : 49
MODULES

2 IMPORTING MODULE


[48]
0s
import math
print(math.sqrt(16))
4.0
IMPORT SPECIFIC FUNCTION


[60]
0s
from math import pi, sin
print(pi)
print(sin(math.radians(90

def greet(name):
  print("Hello," + name)
def add(a,b):
  return a+b
import my_module
rajesh.great("alice")
print(rajesh.add(5,3))



"""PRIME NUMBER"""

def is_prime(num):
  if num <= 1:
    return False
  for i in range(2, int(num ** 0.5 ) + 1):
    if num % i == 0:
     return False
  return True

  number =int(input("enter a number: "))
  if is_prime(number):
    print("the number is prime.")
  else:
    print("the number is not prime.")

"""FIBONACCI SERIES"""

def fibonacci(n):
  sequence=[]
  a, b = 0, 1
  for _ in range(n):
    sequence.append(a)
    a, b = b, a+b
  return sequence

terms =int(input("enter the number of terms:"))
print("fibonacci sequence:",fibonacci(terms))

"""FACTORIAL NUMBER"""

def factorial(n):
  if n ==0: