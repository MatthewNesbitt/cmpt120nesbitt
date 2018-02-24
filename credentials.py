# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Matt Nesbitt
# Created: 2018-2-23

def main():
    first = input("Enter your first name: ").lower()
    last = input("Enter your last name: ").lower()
    uname = first + "." + last + "1"
    password = input("Create a new password: ")
    first = first.lower()
    last = last.lower()
    
    if len(password) <=8:
        print("Fool of a Took! That password is feeble! Please make it more than 8 characters.")
        password = input("Create a new password: ")
    elif all(x.islower() for x in password):
        print("Fool of a Took! That password is feeble! Please include at least 1 uppercase letter..")
        password = input("Create a new password: ")


    if len(password) >=8:
        print("The force is strong in this one…")
        print("Account configured. Your new email address is", uname + "@marist.edu")
    elif any(x.isupper() for x in password):
        print("The force is strong with this one...")
        print("Account configured. Your new email address is", uname + "@marist.edu")

main()
