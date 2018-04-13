#Matt Nesbitt
#Intro to Programming Lab #8
#Personality Matrix


grid = [[0, 0, 1, 1],
        [0, 0, 2, 0],
        [1, 0, 2, 5],
        [3, 4, 2, 3],
        [3, 4, 2, 3],
        [4, 0, 1, 5]]

def getInteraction():
    userAction = int(input("Choose an interaction!:"))
    return userAction

def lookupEmotion(currEmotion, userAction):
    i = currEmotion
    j = userAction
    result = grid[i][j]
    if result == 0:
        print("Hey! That makes me angry!")
        return 0       
    elif result == 1:
        print("Gross!")
        return 1       
    elif result == 2:
        print("That's scary!!")
        return 2       
    elif result == 3:
        print("I am happy!")
        return 3       
    elif result == 4:
        print("You are upsetting me.")
        return 4           
    elif result == 5:
        print("That was surprising!!")
        return 5

def main():
    print("Welcome to the Artificial Intelligence Program!")
    print("Interact with me by choosing an emotion and I will respond!")
    print("Enter the number of the interaction you want to use and I will respond to you!: \n"
          "0. Reward,  1.Punish,  2. Threaten,  3. Joke.")
    currEmotion = 3
    while True:
        userAction = getInteraction()
        currEmotion = lookupEmotion(currEmotion, userAction)
main()
