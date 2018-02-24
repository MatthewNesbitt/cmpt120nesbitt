from graphics import *

win = GraphWin('Calc', 160, 250)

displayTextElement = Text(Point(0, 25), "")

calcGrid = [
    [7, 8, 9, '+'],
    [4, 5, 6, '-'],
    [1, 2, 3, 'x'],
    ['', 0, '+/-', ''],
    ['', '', 'C', '=']
]
buttons = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]

def calcB(x, y, value):
    button = Rectangle(Point(x, y), Point(x + 40, y + 40))
    button.setFill('red')
    button.setOutline('black')
    button.draw(win)
    text = Text(Point(x + 20, y + 20), value)
    text.setTextColor('black')
    text.setSize(15)
    text.draw(win)
    return button

def inner(clicked, button):
    if clicked.getX() > button.p1.getX() and clicked.getX() < button.p2.getX():
        if clicked.getY() > button.p1.getY() and clicked.getY() < button.p2.getY():
            return True
    return False

def clickReact(clicked):
    for m in range(5):
        for n in range(4):
            if clicked.getX() > buttons[m][n].p1.getX() and clicked.getX() < buttons[m][n].p2.getX():
                if clicked.getY() > buttons[m][n].p1.getY() and clicked.getY() < buttons[m][n].p2.getY():
                    return m, n
    return -1, -1


def makeButtons():
    for m in range (5):
        for n in range(4):
            buttons[m][n] = calcB(n * 40, m * 40 + 50, calcGrid[m][n])

def subtraction(op1, op2):
    return op1 - op2

def addition(op1, op2):
    return op1 + op2

def multiplication(op1, op2):
    return op1 * op2

def main():
    makeButtons()
    displayString = ''
    displayTextElement = Text(Point(0, 25), "")
    displayTextElement.draw(win)
    op1 = 0
    op1Entered = False
    op2 = 0
    op2Entered = False
    opr = ''
    oprEntered = False
    while True:
        clicked = win.getMouse()
        row, col = clickReact(clicked)
        
        if row >= 0:
            userInput = calcGrid[row][col]
            if userInput == 'C':
                displayTextElement.undraw()
                displayString = ''
                displayTextElement = Text(Point(0, 25), "")
                displayTextElement.draw(win)
                op1Entered = False
                op2Entered = False
                oprEntered = False
            else:
                if userInput == '=':
                    if opr == '+':
                        answer = addition(op1, op2)
                    elif opr == '-':
                        answer = subtraction(op1, op2)
                    elif opr == 'x':
                        answer = multiplication(op1, op2)
                    displayTextElement.undraw()
                    displayString = str(answer).rjust(75)
                    displayTextElement = Text(Point(0, 25), displayString)
                    displayTextElement.draw(win)
                    op1Entered = False
                    op2Entered = False
                    oprEntered = False
                else:
                    if op1Entered == False:
                        op1Entered = True
                        displayTextElement.undraw()
                        displayString = ''
                        displayTextElement = Text(Point(0, 25), "")
                        displayTextElement.draw(win)
                        op1 = userInput
                    elif oprEntered == False:
                        oprEntered = True
                        opr = userInput
                    elif op2Entered == False:
                        op2Entered = True
                        op2 = userInput
                    buttons[row][col].setFill('red')
                    displayString = (displayString + str(userInput)).rjust(75)
                    displayTextElement.undraw()
                    displayTextElement = Text(Point(0, 25), displayString)
                    displayTextElement.draw(win)

        for i in range(5):
            for j in range(4):
                if (i == row and j == col):
                    buttons[i][j].setFill('red')
main()
