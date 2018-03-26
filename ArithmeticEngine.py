# CMPT 120 - Lab #6
# Matt Nesbitt
# 23-03-2018
###

def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")

def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")

def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ").lower()

        if cmd in ("add", "sub", "mult", "div"):
            try:
               num1 = int(input("Enter the first number: "))
               num2 = int(input("Enter the second number: "))
            except:
                print("Please enter a number!")
                continue
       
        if cmd == "add":
            result = num1 + num2
            print("The result is " + str(result) + ".\n")

        elif cmd == "sub":
            result = num1 - num2
            print("The result is " + str(result) + ".\n")

        elif cmd == "mult":
            result = num1 * num2
            print("The result is " + str(result) + ".\n")

        elif cmd == "div":
            result = num1 // num2 # You can put this in a try clause for div by 0
            print("The result is " + str(result) + ".\n")

        elif cmd == "quit":
            break
        
        else:
            print(cmd, "is not a valid command.")
            
def main():
    showIntro()
    doLoop()
    showOutro()

main()
