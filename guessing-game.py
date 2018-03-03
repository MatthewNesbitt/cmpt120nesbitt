# Guessing game Lab 5
# Matt Nesbitt

animal = "elephant"

def main():
    guess = input("I am thinking of an animal, What is my name?: ")
    guess = guess.lower()
    correct = False
    while not correct:
        if guess != "elephant":
            print("That's incorrect! try again!")
            guess = input("What is my name?: ")
            guess = guess.lower()
            

        elif guess[0] == 'q':
            quit(0)

        else:
            guess = "elephant"
            print("You have guessed correctly! Congrats!")
            ques2 = input("Are you a fan of elephants? Answer 'y' or 'n'")
            if ques2 == "y":
                print("Awesome! I also like elephants.")
            else:
                print("Oh well, Not everyone likes elephants!")
            return
main()
            

    
