# Guessing game Lab 5
# Matt Nesbitt

animal = "elephant"

def main():
    guess = input("I am thinking of an animal, What is my name?: ")
    correct = False
    while not correct:
        if guess != "elephant":
            print("That's incorrect! try again!")
            guess = input("What is my name?: ")

        else:
            guess = "elephant"
            print("You have guessed correctly! Congrats!")
            print("Thanks for playing!")
            return
main()
            

    
