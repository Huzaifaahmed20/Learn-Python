# tip calculator
# ---------------------------------------
# meal = 44.50
# tax = 6.75 / 100
# tip = 15. / 100
# cost = meal
# cost += meal * tax
# totalCost = cost + cost * tip
# print totalCost


# Division in Python
# ---------------------------------------
# one = 7 / 2
# two = 7. / 2
# three = 7 / 2.
# four = 7. / 2.
# five = float(7) / 2
# print one
# print two
# print three
# print four
# print five


# String methods
#  --------------------------------
# name = "Huzaifa"
# length = len(name)
# lowerCase = name.lower()
# upperCase = name.upper()
# alpha = name.isalpha()   check that  if string has no nonletter characters 
# print length
# print lowerCase
# print upperCase


# print number in a set of strings
# -----------------------------------

# print """ this is
# multiline string """

# num = 21
# bigString = "I am " + str(num) + " years old"
# print bigString


# Console Input
# --------------------------
# name = raw%sinput("What Is Your Name: ")
# age = raw%sinput("What is your age: ")
# age = int(age) #need to convert to number otherwise error
# print "So , your name is %s, and your age is %d" % (name,age)


# from datetime import datetime
# print datetime.now()


# if else statement
# def myfun()

# if 10 < 20:
#     return True
# else:
#     return False
#  need to check this


# Latin Langage generator
# ----------------------------------------------

# pyg = 'ay'
# original = raw_input('Enter a word:')
# if len(original) > 0 and original.isalpha():
#   word = original.lower()
#   first = word[0]
#   new_word = word + first + pyg
#   new_word = new_word[1:len(new_word)]
#   print new_word
#   print original
# else:
#   print 'empty'



# Area Calculator
# ---------------------------
# print 'program is running'
# option = raw_input("Enter C for Circle or T for Triangle:")

# if option == 'c' or option == 'C':
#   radius = float(raw_input("Enter circle radius: "))
#   area = (3.14159) * (radius**radius)
#   print str(area)
  
# elif option == 't' or option == 'T':
#     base = float(raw_input('Enter Base of Triangle: '))
#     height = float(raw_input('Enter Height of Triangle: '))
#     area = 1./2 * base * height
#     print str(area)
    
# else:
#     print 'Wrong Input'
      
# print 'Program is Exiting'
      



# Dice Game
# ===========================================
# print """
# Roll a Dice
# """
# from random import randint
# from time import sleep

# def get_user_guess():
#   guess = int(raw_input("Guess the Number: "))
#   return guess

# def roll_dice(number_of_sides):
#   first_roll = randint(1,number_of_sides)
#   second_roll = randint(1,number_of_sides)
#   max_val = number_of_sides * 2 
#   print "Max Value is: %d" % (max_val)
#   guess = get_user_guess()
#   if guess > max_val:
#     print "Invalid Input"
#   else:
#     print "Rolling ..."
#     sleep(2)
#     print "First Roll: %d" % (first_roll)
#     sleep(1)
#     print "Second Roll: %d" % (second_roll)
#     total_roll = first_roll + second_roll
#     print "Total Roll: %d" % (total_roll)
#     print "Result ..."
#     sleep(1)
#     if guess == total_roll:
#       print "User Won yayyy !"
#     else:
#       print "Computer Won !"
    

  

# roll_dice(6)
