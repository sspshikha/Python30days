# two_digit_number = input("Type a two digit number:")
# print(int(two_digit_number[0])+int(two_digit_number[1]))
import random

# Mathematical operation - +,-,*,/,**
# print(6%3)----reminder
# print(6/3)----quotient----always output is float
# PEMDAS left to right
# ()
# **
# * /
# + -
# print(2**3)
# print(3*3+3/3-3)

# print(3*3/3+3-3)

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# BMI = (weight/(height**2))
# print(round(BMI))

# print(round(8//3))
# f-String

# age = int(input("what is your current age: "))
# Days = (75-age)*365
# Weeks = (75-age)*52
# Months = (75-age)*12
# Years = (75-age)
# print(f"You have {Days} days, {Weeks} weeks, {Months} months, and {Years} years left")

# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("what percentage tip would you like to give? "))
# people = int(input("How many people to split the bill?"))
# #bill_with_tip = tip/100 *bill +bill
# bill_with_tip = bill*(1 + tip/100)
# print(bill_with_tip)
# print("Welcome to the roller_coaster!")
# Height = int(input("Your height in cm? "))
#
# if Height == 120:
#     print("Can ride")
# else:
#     print("can't ride")

# print("Know if a number is odd or even")
# num = float(input("number: "))
# if num % 2 == 0:
#     print("This a even number")
# else:
#     print("This is a odd number")

# print("Welcome to roller_coaster!")
# Height = int(input("Your height in cm :"))
# if (Height >= 120) & (Height < 190):
#     print("You can take a ride")
#     Age = int(input("Your Age: "))
#     if Age >= 18:
#         print("Pay $12")
#     elif (Age >= 12) & (Age < 18):
#         print("Pay $7")
#     else:
#         print("Pay $5")
# else:
#     print("Sorry! you can't take a ride")

# print("Welcome to BMI calculator!")
# Height = float(input("Please enter your height in meters: "))
# Weight = float(input("Please enter your weight in Kgs: "))
# BMI = round(Weight/(Height**2))
# if BMI < 18.5:
#     print(f"Your current BMI is {BMI},You are slightly Underweight")
# elif BMI < 25:
#     print(f"Your current BMI is {BMI},You come under Normal Weight")
# elif BMI < 30:
#     print(f"Your current BMI is {BMI},You are slightly Overweight,a little exercise and diet can take to long way")
# elif BMI < 35:
#     print(f"Your current BMI is {BMI},You fall under Obese, a exercise and diet can take to long way")
# else:
#     print(f"Your current BMI is {BMI},you are Clinically Obese, you need to immediately consult with a doctor")

# Year = int(input("Enter the year: "))
# # if ((Year % 4 == 0) & (Year % 100 != 0)) or (Year % 400 == 0):
# #     print(f"{Year} is a leap year!")
# # else:
# #     print(f"{Year} is not a leap year")
#
# if Year %4 ==0:
#     if Year %100 ==0:
#         if Year %400 ==0:
#             print("Leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("leap year")
# else:
#     print("Not a leap year")

# print("Welcome to roller_coaster!")
# Height = int(input("Your height in cm :"))
# bill = 0
# if (Height >= 120) & (Height < 190):
#     print("You can take a ride")
#     Age = int(input("Your Age: "))
#     if Age < 12:
#         bill = 5
#         print("Child tickets are $5")
#     elif Age <= 18:
#         bill = 7
#         print("Youth tickets are $7")
#     elif (Age >= 45) and (Age <= 55):
#         print("Congratulations! you need to pay $0")
#     else:
#         bill = 12
#         print("Adult tickets are $12")
#     Wants_Photo = input("Would you like to have a photo? Y or N: ")
#     if Wants_Photo == "Y":
#         bill += 3
#
#     print(f"Your total bill is {bill}")
#     # if Wants_Photo == "N" or "n":
#     #     print(f"Your total bill is {bill}")
#
# else:
#     print("Sorry! you can't take a ride")

# print("Welcome to Python pizza Deliveries!")
# size = input("What size pizza do you want? S,M,L : ")
# add_pepperoni = input("Do you want pepperoni? Y or N : ")
# extra_cheese = input("Do you want extra cheese? Y or N : ")
# if size == "S":
#     bill = 15
# elif size == "M":
#     bill = 20
# else:
#     bill = 25
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
# if extra_cheese == "Y":
#     bill += 1
# print(f"Your total bill is ${bill}")

# print("Welcome to the Love Calculator!")
# name1 = input("what is your name? \n")
# name2 = input("What is their name? \n")
# combined_string = name1 + name2
# Your_names = combined_string.lower()
# t = Your_names.count("t")
# r = Your_names.count("r")
# u = Your_names.count("u")
# e = Your_names.count("e")
# true = t+r+u+e
# l = Your_names.count("l")
# o = Your_names.count("o")
# v = Your_names.count("v")
# e = Your_names.count("e")
# love = l+o+v+e
#
# love_socre = int(str(true) + str(love))
# # print(f"love score : {love_socre}")
# if love_socre < 10 or love_socre > 90:
#     print(f"Your score is {love_socre}, you go like coke and mentos")
# elif love_socre > 40 and love_socre < 50:
#     print(f"your score is {love_socre}, you are alright together")
# else:
#     print(f"your score is {love_socre}")

# print('''
#
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_______/
# *******************************************************************************
# ''')
# print("Welcome to Treasure island.\nYour mission is to find the treasure!")
# Turn = str(input("Which turn will you like to take Left or right? L or R :  "))
# if Turn == "L":
#     print("Hey glad to see you alive :)")
#     choice = str(input("Would you like to swim or wait for the boat? type swim or wait :  "))
#     if choice == "wait":
#         print("Hey be carefull you are almost there!")
#         door = str(input("Which colour door will you open??? blue or red or yellow :  "))
#         if door == "yellow":
#             print("congratulations !!! you WON :)")
#         else:
#             print("Game Over :(")
#     else:
#         print("Game Over :(")
# else:
#     print("Game Over :(")

# Randomisation
# import random
# # import Python_data_types
# # import module_1
# random_integer = random.randint(1,10)
# print(random_integer)
# random_float = random.random() *5
# print(random_float)
# # #print(Python_data_types.pi)
# # print(module_1.H)
# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score} !")
# import  random
# input("what will you pick Heads or tails ! if 'Heads' or 'Tails': " )
# random_integer =  random.randint(1,10)
# print(random_integer)
# if (random_integer >=1) and (random_integer <5):
#     print("Heads")
# else:
#     print("Tails")

##Data_Structure -- List

# States_of_India = ['odisha','goa','manipur']
# States_of_India[1] = 'ggb'
# States_of_India.append('deepland')
# States_of_India.extend(['priland','susland'])
# print(States_of_India)
# print(States_of_India[-1])
import random
print("who would like to pay the bill?" )
who_is_paying_bill = input("Put all of your names in this box:  ")
list_of_people_paying_bill = who_is_paying_bill.split(",")
print(list_of_people_paying_bill)
num_items = len(list_of_people_paying_bill)
num_we_got = random.randint(0, num_items-1)
Person_paying = list_of_people_paying_bill[num_we_got]
print(f"{Person_paying} will be paying the bill! :)")














