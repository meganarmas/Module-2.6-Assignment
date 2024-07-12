#Objective: The aim of this assignment is to process and format user input data.
# Task 1: Input Length Validator Write a script that asks for and 
# checks the length of the user's first name and last name. 
# Both should be at least 2 characters long. If not, print an error message.

def longest():
    maxLength = 0
    fullname = ''

names_input = input("What is your first name and last name? Enter name here: ")

if len(names_input) >= 2:
        print(f"The length of your name is {len(names_input)} long")
else:
        print("Error. Less than 2 characters. Please try again")