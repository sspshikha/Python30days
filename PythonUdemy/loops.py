# Enter a number - 12
# 12 is a composite number
# Enter a number - 7
# 7 is a prime number
#
# number = int(input("Enter a number = "))
# count = 0
# for i in range(1, number+1):
#     if number % i == 0:
#         count += 1
# print(str(number) + " has " + str(count) + " Factors")
#
# if count == 2:
#     print(str(number) + " is a prime number")
# else:
#     print(str(number) + " is a composite number")

# Enter a number - 30
# Prime numbers within 30 is
# 2
# 3
# 5
# 7
# 9
# ....
#
# dinu bye
# i am sleepy
# good night

# number = int(input("Please enter a number : "))
# count = 0
# for i in range(1, number+1):
#     if number % i == 0:
#         count += 1
#
# if count == 2:
#     print(str(number) + "is a prime number")
# else:
#     print("not prime")

# step-1---prime number with in a range 0 to 20
# step-2---check if all the numbers within the range is prime number or not
# step-3---logic to check for prime number for a single number
# step-4---find the factors of a number and count it
# step-4.5--- to find the factor of a number we need to check all the numbers from (1 to that number)
# is divisible by that number or not
# step-5---if count is ==2 then it is prime number and print it
# step-6---repeat step-3,4,5 for all the numbers in range b/w 0 to 20


# count = 0
# for i in range(1, number+1):
#     if number % i == 0:
#         count += 1
# print("number of factors : " + str(count))
#
# if count == 2:
#     print("it's prime")
# else:
#     print("not prime")

# number = int(input("Enter a range : "))
#
# def check_if_prime(num):
#
#     count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1
#     # print("number of factors : " + str(count))
#
#     if count == 2:
#         print(num)
#     # else:
#     #     print("not prime")
#
#
# #check_if_prime(number)
#
# for i in range(2, number+1):
#     check_if_prime(i)


# 58. Length of Last Word

# input_string = input("Please enter a string : ")
# list_of_input_string = (input_string.split())
# #print(list_of_input_string)
#
#
# for i in list_of_input_string:
#     if i == list_of_input_string[-1]:
#         length_of_last_word = len(i)
#         print("The last word is " + str(i) + " and it's lenght is " + str(length_of_last_word))

# using .format()
#
# name = input("What is the job applicant's name : ")
# degree = input("What did they major in at college? ")
# job = input("What is their current occupation? ")
# experience = input("How many years have they been working in their field? ")
#
# print("{} majored in {}, works as a {}, and has {} years of experience.".format(name, degree, job, experience))
#
# print(f'{name} majored in {degree}, works as a {job}, and has {experience} years of experience.')

# List

# example_list_1 = [5, 4, 3, 2, 1]
# example_list_2 = [2.718, 9.31]
# example_list_3 = ["blue", "green", "red", "yellow", "purple", "orange"]
# example_list_4 = [True, False, False, True, False, True, True, False, True]
# example_list_5 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# example_list_6 = [10, 3.14159, "tree", False, [1, 2, 3]]
#
# print(list("blah"))
#
# # in and not in
#
# checked_list = [1, 2, 3, 4]
# print(1 not in checked_list)

# ex_list = [10, 3.14159, "tree", False, [1, 2, 3]]
# var = list("tree")
# print('e' in var)
# print('a' not in var)

# indexes and list slicing---accessing by index

# indexes_example = ["carpet", "hardwood", "linoleum"]
# # print(indexes_example[1])
# # list_5 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# print(indexes_example[2][2])
#
# # negative
#
# negative = [1, 2, 3, 4, 5]
# print(negative[-1])
# print(negative[-2])
# print(negative[-3])
# print(negative[-4])
# print(negative[-5])

# using items accessed by index in expressions

# mixed = [10, 3.14159, "tree", False, [1, 2, 3]]
# print(mixed[2] + 1.76)

# list slicing

sliced = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sliced[:4])
print(sliced[3:8])
print(sliced[6:])

# reassigning a list's it
































