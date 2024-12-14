# -*- coding: utf-8 -*-
"""DAY4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LOuOeZygBMWnzc8VWGZNJ3QJkhVapln3
"""

class Solution(object):
    def is_palindrome(self, x):
        # Negative numbers and numbers ending in 0 (but not 0 itself) cannot be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # Check if the original number (or half of it) matches the reversed half
        return x == reversed_half or x == reversed_half // 10



"""14 find GCD OF TWO NUMBERS USING A FUNCTION"""

def gcd(a,b):
  while b:
    a,b = b, a % b
    return a

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
print("GCD:",gcd(num1,num2))



""" 1 reading and writing to a file"""

with open('lines.txt', 'w') as file:
    file.write("First line\nSecond line\nThird line")
with open('lines.txt', 'r') as file:
    lines = file.readlines()
    print("Number of lines:", len(lines))

"""APPENDING DATA TO A FILE"""

with open('paragraph.txt', 'w') as file:
    file.write("Python is a versatile programming language. It is great for beginners and professionals.")

with open('paragraph.txt', 'r') as file:
    content = file.read()
    if "Python" in content:
        print("The word 'Python' exists in the file.")
    else:
        print("The word 'Python' does not exist in the file.")

"""HANDLING DIVISION BY ZERO ERROR"""

try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid integers.")

"""CREATING A CUSTOM OPERATOR"""

class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be a positive number and less than 120."):
        self.age = age
        self.message = message
        super().__init__(self.message)

def set_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    return f"Age is set to {age}"

# Using the custom exception
try:
    print(set_age(130))
except InvalidAgeError as e:
    print(f"Error: {e.message} (Age provided: {e.age})")
