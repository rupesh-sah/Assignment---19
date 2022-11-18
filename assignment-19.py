# Assignment - 19 Full Stack Web Development using Python MySirG

#                          Functions

# (Q.1) Write a python program to create a simple function which prints “MySirG” .

def name():
  print("MySirG")
name()

'''(Q.2) Write a python program to create a function which expects two arguments and print
them in the function body.'''
def names():
  a = "Hii "
  b = "sir"
  c= a+b
  print(c)
names()

'''(Q.3)Write a python program to create a function which expects an unknown number of
arguments.'''
def num1(a,b):
  print(a,b)
num1(1,2)

'''(Q.5) Write a python program to create a function which expects a list as an argument.'''

def my_func():
  fruits = ["apple", "banana", "cherry"]
  print(fruits)
my_func()

'''(Q.6) Write a python program to create a function that finds a maximum of four numbers.'''

def num2(a,b,c,d):
  print(a,b,c,d)
num2(1,2,3,4)

'''(Q.7) Write a python program to sum all the numbers in a list.'''

def sum1():
  list_sum = sum([1,2,3,4])
  print("sum of", list_sum)
sum1()
'''(Q.8) Write a python program to multiply all the numbers in a list.'''
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(multiply((8, 2, 3, -1, 7)))

'''(Q.9) Write a python program to create a function to check whether a number falls in a
given range.'''
def test_range(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(5)

'''(Q.10) Write a python program to create a function to check whether a given number is even
or odd.'''

num = int(input("Enter a Number:")) 
if num % 2 == 0: 
  print("Given number is Even") 
else: 
  print("Given number is Odd")
