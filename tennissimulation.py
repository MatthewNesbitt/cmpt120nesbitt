from simstats import SimStats
from tennismatch import TennisMatch

def printIntro():
    print("This program simulates a tennis match")

def getInputs():
    probA = float(input("Enter the probability of A: "))
    probB = float(input("Enter the probability of B: "))
    n = int(input("Number of games to simulate: "))
    return probA, probB, n
    
def main():
    printIntro()
    probA, probB, n = getInputs()
    stats = SimStats()
    for i in range(n):
        theMatch = TennisMatch(probA, probB)
        theMatch.play()
        stats.update(theMatch)
    stats.printReport()

main()
