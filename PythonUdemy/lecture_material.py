#print("hello world")

# ex_var = 5
# ex_var = 7
# # float,int,bool,
# first_var = 5
# second_var = -1.5
# third_var = False
# first_var = 23
# # Math operator -- add,sub,mul,div
#
# Addition = 2+3
# Subtraction = 5-2
# division = 3/2
# multiply = 3*6
# exponentiation = 4**4
# floor_division = 16//5
# modulo = 7 % 3
# # Assignment operator
# add_assign = 5
# add_assign = add_assign + 7
# add_assign += 7
# #print(add_assign)
# # add_assign1 = add_assign + 7
# # add_assign1 += 7//2
# # print(add_assign1)
#
# var = 5
# var //= 3
#var = var//3
#print(var)
#######
# operator precedence
# ()
# **
# % ,/,//,*
# +,-
#cal = (9-7)*2**3+10%6//-1*2-1
# 2*8+10%6//-1*2-1
# 2*8+4//-1*2-1
# 16-4*2-1
# 16-8-1
# 7
#print(cal)

# 15/3*2*2-(3+4)
# 15/3*2*2-7
# 20-7
# 13
# var1 = 2+3
# var2 = 4-5
# var3 = var1/var2
# var4 = 7*8
# var5 = 3**8
# var6 = 10//3
# var7 = 17%15

# var1 = 3.7
# print(var1)
# print(0.06)
# print(2//3-1)

#print(123+280)/100--4.03{had to multiply and divide 100 as python is built upon}
# ex3 = 1.23 + 2.80
# print(round(ex3, 2))
#
# penne = 16.68
# arrabiata = 6.98
# garlic = 16.78
# italian = 15.26
# artisan = 3
# meatballs = 4.39
# tolat_price = penne + garlic + arrabiata + italian + artisan + meatballs
# print(round(tolat_price,2))

# ex_1 = "orange"
# print(ex_1[2])
# print("dinubaby"[0])

#slicing
# ex_2 = "Dinesh"
# print(ex_2[0:2])
# print(ex_2[3:5])
# print(ex_2[1:4])

#concatenation
# print("pecan" + " " + "pie")
# concatenated = "R2" + "_" + "D2"
# print(concatenated)   #---R2_D2
# print(concatenated[3])    #---D
# print(concatenated[1:4])   #---2_D


# unchanged = "forrest gump"
# sliced =unchanged[6:]
# print(sliced)
# print(unchanged)

# ex_3 = "Just" + " " + "do" + " " + "it!"
# print(ex_3)
# print(ex_3[10])
# print(ex_3[5:7])
# print(ex_3[8:])
# print(ex_3[0:4])
# slice = "Don't" + " " + ex_3[5:]
# print(slice)

# type() and str() function

# ex_4 = False
# ex_5 = 29
# ex_6 = 4.1352
#
# ex_4 = str(True)
# ex_5 = str(24)
# ex_6 = str(3.52)
#
# print(type(ex_4))
# print(type(ex_5))
# print(type(ex_6))

# What is an escape sequence?
# print("I\thate\tdinesh")
# #"I Love you"
# print('"I hate you"')
# #"\n means new line"
# #print('" means new line"')
# print("\n means new line")
# # "(\n means new line)"
# print("\"(\\n means new line)\"")

#"/* Comments are written here */"
# print("\"/* Comments are written here */\"")

# ex_7 = 3.8
# print(type(ex_7))
# print(str(ex_7) + "is a float.")
# name = "Deepshikha"
# print("\"Hello, I\'m ["+name+"], it\'s nice to meet you!\"")

#print("*******\n" + " *****\n" + "  ***\n" + "   *")

# name = input("Please enter your name : ")
# print("Your name is " + name + ".")
# print(type(name))
# 90 + 10
# int(name) + 10


# name = str(input("What is your name? : "))
# quest = str(input("What is your quest? : "))
# favorite_colour = str(input("What is your favorite colour? : "))
# print("So your name is " + name + ", your quest is " + quest + ", and your favorite colour is " + favorite_colour + ".")

# user_int = int(input("Please enter an integer."))
# print(user_int)
# print(type(user_int))

# print(int(10.9))
#
# print(float("1"))

# string that is an integer --- float("1")----output--1

# num = int(input("Enter a number that will added to 10 : "))
# print("sum : " + str(num + 10))

#function for code reuseability
# def prints_four():
#     print("this")
#     print("is")
#     print("an")
#     print("example")
# #function calling
# prints_four()
# prints_four()
# prints_four()

#parts of function
# def function_name():
#     print(2+2)
#
#calling Function
# function_name()

# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# num = int(input("Enter a number : "))
# for num in range(1,num):
#     if num%3 == 0 and num%5 == 0:
#         print("FizzBuzz")
#     elif num%3 == 0:
#         print("Fizz")
#     elif num%5 == 0:
#         print("Buzz")
#     else:
#         print(num)

# num = int(input("Enter a number : "))
# Factorial_of_num = num*(num-1)
# print(Factorial_of_num)

# function parameters

# def function_name(parameter):
#     print(parameter + 2)
#
#
# function_name(68)
#
# # multiple parameters
#
# first_str = "The number "
#
#
# def fun_nam(p1, p2, p3):       # these are parameters
#     print(p1 + str(p2) + p3)


# fun_nam(first_str, 5, " is an integer.")    # these are arguments

# default function

# def default_example(num1=7, num2=8):
#     print(num1*num2)
#     return num1*num2
#
#
# print(default_example() + 44)


# def hello_world_printer():
#     print("hello world")
#
#
# hello_world_printer()

# def name_printer(num):
#     print(num)
#
#
# name = input("Enter your name : ")
# # name_printer(name)
#
# length = int(input("length : "))
# width = int(input("width : "))
# height = int(input("height : "))
#
#
# def vol_of_rect_prism(l, w, h):
#     return l*w*h
#
#
# volume = vol_of_rect_prism(length,width,height)
#
# # print("The volume of the rectangular prism is " + str(vol_of_rect_prism(length,width,height)) + " cubic feet.")
#
# print("The volume of the rectangular prism is " + str(volume) + " cubic feet.")

# F = 1.8*C+32

# Celsius = int(input("Enter temperature in celsius : "))
#
#
# def fahrenheit(C_temp):
#     return (1.8*C_temp+32)
#
#
# fahrenheit_temp = fahrenheit(Celsius)
#
# print("The Farhrenheit equivalent of " + str(Celsius) + " degree Celsius is " + str(fahrenheit_temp))

# Modules

# import random
#
# print(random.randint(1, 10))
#
# # function import
#
# from random import randint
#
# print(randint(10,20))


# universal import

# from random import *
#
# print (random())

from random import randint

# fuel = randint(10, 25)
# miles = randint(200, 400)
# print("The car can travel " + str(miles // fuel) + " miles per gallon.")
# print("The car's fule tank can hold " + str(fuel) + " gallon.")
# print("The car can travel " + str(miles) + " miles on a full tank.")

# Variable scope

# example_1 = "hello world"      #global
#
#
# def loc_ex():
#     example = "this is a string"  #local
#     print(example_1)
#     return example
#
#
# print(example_1)
# print(loc_ex())

# %%%%%%%%%%%%% Why is understanding variable scope important?
# Local variable cannot be used by code in the global scope.
# Global variable can be accessed by code in a local scope.
# The local scope of one function can't use variable from another function's local scope.
# you can use the same  name for different variable as long as they are in different scopes.

# var_2 = 7
#
#
# def test_local_var():
#     var_1 = 3
#     name = "Deepu"
#     print(name)
#     print(var_1)
#     print(var_2)
#
#
# def test_for_another_local_var():
#     var_3 = 9
#     name = "Dubu"
#     print(name)
#     print(var_2)
#     print(var_3)
#     # print(var_1)
#
#
# print (var_2)
# test_local_var()
# test_for_another_local_var()

# Global Statements


# def loc_ex():
#     global fruit
#     fruit = "pear"
#     print(fruit)
#
#
# fruit = "apple"
# loc_ex()
# print(fruit)

# What is the point of scopes anyway?

# Intro to flow control --- Flow chart
# comparison operator  ---------- >, <, >=, <=, !=, == (Returns a boolean value in the output box)

# print(4>2)
# print(1>3)
# print(5.79 < 6)
# print(3<3)
# print(9 >= 9)
# print(1 <= 2)
# print(10 != 100)
# print(10 != 10)
# print(10 == 100)
# print(10 == 10)
# print("hello" == "hello")
# print(("hello" != "world"))
#
# # comparisons are case senstive and floats and integer can be equvalent
# print("hello" == "Hello")
# print(4.0 == 4)
#
# # = vs == (= is used to assign value and == is used for comparison )
#
# # Boolean operator ----- and, or, not
# #AND
# # True and True = True
# # True and False = False
# # False and True = False
# # False and False = False
#
# print(4>1 and "word" == "word")
# print(8.76 == 8.7600 and 2 != 2)
# print("earth" == "Earth" and 6<= 3)
# print(10==5 and 10 != 5)

# OR
# True or True = True
# True or False = True
# False or True = True
# False or False = False

# print(4>1 or "word" == "word")
# print(8.76 == 8.7600 or 2 != 2)
# print("earth" == "Earth" or 6<= 3)
# print(10==5 or 10 != 5)

# NOT
# not True = False
# not False = True

# print(not 6482 > 0)
# print(not "Python" != "Python")

# if Statements

# if True:
#     "Do the stuff here"

# veg = input("Type the name of a vegetable : ")
#
# if veg == "corn":
#     print("The vegetable is corn.")
#
# else:
#     print("The vegetable is not a corn")
#     print("It's a " + veg)

#      nested if and else statements

# print("Welcome to students portal")
# print("Apply for Loan based on eligibility ")
# high_school_GPA = float(input("Please enter your high school GPA : "))
# accepted_by_institute = (input("Please enter if you got accepted by the institute : "))
#
#
# if high_school_GPA >= 3.7:
#     if accepted_by_institute == "yes":
#         print("Qualifies for low APR loan")
#
#     else:
#         print("Does not qualify low APR loan")
# else:
#     print("Needs higher GPA to qualify")


# score = int(input("Please enter your score : "))
#
# if score >= 90:
#     print("You score is " + str(score) + " and you received 'A' Grade ")
# elif score >= 80:
#     print("You score is " + str(score) + " and you received 'B' Grade ")
# elif score >= 70:
#     print("You score is " + str(score) + " and you received 'C' Grade ")
# elif score >= 60:
#     print("You score is " + str(score) + " and you received 'D' Grade ")
# else:
#     print("You score is " + str(score) + " and you received 'F' Grade ")

# user_num = int(input("Please enter an integer."))
#
# if user_num < 0:
#     print("The number you entered is less than 0.")
# elif user_num == 0:
#     print("The number you entered is 0.")
# elif 0 < user_num <= 100:
#     print("The number you entered can be 1, 100, or anything in between.")
# else:
#     print("The number you entered is greater than 100.")

# from random import randint
#
# random_num = randint(1, 10)
#
#
# if random_num == 1:
#     print("The roman numerical equivalent of " + str(random_num) + " is I ")
# elif random_num == 2:
#     print("The roman numerical equivalent of " + str(random_num) + " is II ")
# elif random_num == 3:
#     print("The roman numerical equivalent of " + str(random_num) + " is III ")
# elif random_num == 4:
#     print("The roman numerical equivalent of " + str(random_num) + " is IV ")
# elif random_num == 5:
#     print("The roman numerical equivalent of " + str(random_num) + " is V ")
# elif random_num == 6:
#     print("The roman numerical equivalent of " + str(random_num) + " is VI ")
# elif random_num == 7:
#     print("The roman numerical equivalent of " + str(random_num) + " is VII ")
# elif random_num == 8:
#     print("The roman numerical equivalent of " + str(random_num) + " is VIII ")
# elif random_num == 9:
#     print("The roman numerical equivalent of " + str(random_num) + " is IX ")
# else:
#     print("The roman numerical equivalent of " + str(random_num) + " is X ")

# truthy and falsy values for strings

# string_example = input("Enter any string other than an empty one.")
#
# if string_example:
#     print("Thank you for entering something.")
# else:
#     print("you did not enter a string.")


# # while loop
# counter = 0
#
# while counter < 3:
#     print("something")
#     counter += 1


# # infinite loop
# counter = 1
#
# while counter < 6:
#     print(counter)

# counter = 10
#
# while counter != 0:
#     print(counter)
#     counter -= 1

# var = int(input("Enter a positive integer : "))
# int_init = var
# summed = 0
# while var > 0:
#     summed += var
#     var -= 1
# print("The initial number you entered is : " + str(int_init))
# print("Sum of all the integer till " + str(int_init) + " is : " + str(summed))

# word = "house"
#
# for letter in word:
#     print(letter)
#

# word = "hello world"
#
# for letter in word:
#     print(letter)

word = "hello world"

# for letter in "hello world":
#     print(letter)


# str_var = input("Please enter a string : ")
#
# print(str_var)
# char_count = 0
#
# for count in str_var:
#     char_count += 1
#
# print(char_count)

# Range()
# using range() with one argument

# one_input = range(5)
# print(type(one_input))
# for num in one_input:
#     print(num)

# two_input = range(5, 10)
#
# for num in two_input:
#     print(num)
#
# three_input = range(5, 10, 2)
#
# for num in three_input:
#     print(num)


# num = int(input("Enter a number : "))
#
# for num in range(1, 51):
#
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#
#     elif num % 3 == 0:
#         print("Fizz")
#
#     elif num % 5 == 0:
#         print("Buzz")
#
#     else:
#         print(num)

# from math import factorial
#
#
# number = int(input("Please enter a positive number : "))
#
# factorial_of_num = factorial(number)
# print("The factorial of the given number is " + str(factorial_of_num))

# number = int(input("Please enter a positive number : "))


# def num_factorial(num):
#     num_1 = 1
#     for num_1 in range(1, num):
#
#         num *= 1

# num_factorial(number)

# input_num = int(input("Please enter a number : "))
# first_num = input_num


# while input_num > 0:
#     sum_of_numbers += input_num
#     input_num -= 1
#
# def fact_func(var1):
#     factorial_of_numbers = 1
#     for i in range(1, var1 + 1):
#         factorial_of_numbers *= i  # factorial_of_numbers = factorial_of_numbers * i  - 1*1
#     #print (factorial_of_numbers)
#     return  factorial_of_numbers
#
# #var2=fact_func(input_num)
# print(fact_func(input_num))
#
# #print("For " + str(first_num) + " the factorial of number is :  " + str(factorial_of_numbers))


# output1
# -------
# Enter a number = 10
# 22
# 24
# 26
# 28
# 30

# num = int(input("Enter a number = "))
#
# # for i in range(1, num+1):
# #     if i % 2 == 0:
# #         print(int(i))
#
# for i in range(22, num+20+1, 2):
#     print(int(i))

# output2
# ------
# Enter a number = 10
# Factors of 10 are :
# 1
# 2
# 5
# 10

# number = int(input("Enter a number = "))
# print("Factor of " + str(number) + " are : ")
# for i in range(2, number+1, 2):
#     if number % i == 0:
#         print(str(i))
#
#
# Output 3
# ---------

# Enter a num = 12
# Multiples of 12 are
# 12
# 24
# 36
# 48
# 60
# 72
# 84
# 96
# 108
# 120

# number = int(input("Enter a num = "))
# print("Multiples of " + str(number) + " are : ")
# for i in range(1, 10+1):
#     print(str(i*number))
#

# Output 4
# ---------
# Find the absolute of a number-
# Enter a number = -19
# Absolute of -19 is 19
# Enter a number = 23
# Absolute of 23 is 23
#
# number = int(input("Enter a number = "))
#
# if number >= 0:
#     print("Absolute of " + str(number) + " is " + str(number))
# else:
#     print("Absolute of " + str(number) + " is " + str(number*(-1)))

#
# Output 5
# ---------
#
# Welcome to my Calculator App
# ------------------------------
# Please enter the operation you want to do :
# 1- Addition
# 2- Substraction
# 3- Multiplication
# 4- Division
#
# Please Enter one option - 1
#
# You selected Addition Operation.
#
# Please enter 1st Number = 12
# Please enter 2nd Number = 23
#
# Addition of 12 and 23 is 35

want_to_continue = "y"

while want_to_continue == "y":
    print("Welcome to my Calculator App ")
    print("----------------------------")
    print("Please enter the operation you want to do :")
    print("\n1- Addition\n2- Subtraction\n3- Multiplication\n4- Division")
    operation = int(input("\nPlease Enter one option - "))
    num_1 = int(input("\nPlease enter 1st Number = "))
    num_2 = int(input("\nPlease enter 2nd Number = "))
    if operation == 1:
        print("\nYou selected Addition Operation.")
        Addition = num_1 + num_2
        print("Addition of " + str(num_1) + " and " + str(num_2) + " is " + str(Addition))
    elif operation == 2:
        print("\nYou selected Subtraction Operation.")
        Subtraction = num_1 - num_2
        print(" Subtraction of " + str(num_1) + " and " + str(num_2) + " is " + str(Subtraction))
    elif operation == 3:
        print("\nYou selected Multiplication Operation.")
        Multiplication = num_1 * num_2
        print("Multiplication of " + str(num_1) + " and " + str(num_2) + " is " + str(Multiplication))
    elif operation == 4:
        print("\nYou selected Division Operation.")
        Division = num_1 / num_2
        print("Division of " + str(num_1) + " and " + str(num_2) + " is " + str(Division))

    print("Do you want to continue : select 'y' for yes and 'n' for no ")
    want_to_continue = input("Do you want to continue : ")































