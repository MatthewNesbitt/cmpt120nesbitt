from random import *

class Player:
    def __init__(self, prob):
        self.prob = prob
        self.score = 0
        self.gamesWon = 0
        self.setsWon = 0

    def winsServe(self):
        return random() <= self.prob

    def incScore(self):
        if self.score == 30:
            self.score = self.score + 10
        else:
            self.score = self.score + 15

    def getScore(self):
        return self.score
