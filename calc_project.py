from graphics import *
from calc_functions import *

# JA: Your calculator doesn't have parenthesis keys

buttons = []


def create_button(win, x1, y1, x2, y2, label, color = 'purple'):
    button = Rectangle(Point(x1,y1), Point(x2, y2))
    button.setFill(color)
    button.draw(win)
    text = Text(button.getCenter(), label)
    text.setSize(10)
    text.draw(win)
    return button, label

def check(button, label, x, y):
    x1 = button.p1.getX()
    y1 = button.p1.getY()
    x2 = button.p2.getX()
    y2 = button.p2.getY()
    if x > x1 and x < x2 and y > y1 and y < y2:
        return label
    return False

def calculation(answer, entry, operation):
    if answer == None:
        answer = entry
        entry = 0
    else:
        if operation == '+':
            answer = addition(answer, entry)
        elif operation == '-':
            answer = subtraction(answer, entry)
        elif operation == '*':
            answer = multiplication(answer, entry)
        elif operation == '/':
            answer = division(answer, entry)
        elif operation == '+/-':
            answer = change_sign(answer)
        elif operation == 'x2':
            answer = square(answer)
        elif operation == '%':
            answer = percent(answer)
        elif operation == 'root':
            answer = square_root(answer)
        elif operation == '1/x':
            answer = over_x(answer)
        elif operation == 'sin':
            answer = sine(answer)
        elif operation == 'cos':
            answer = cosine(answer)
        elif operation == 'tan':
            answer = tangent(answer)
        elif operation == '10^x':
            answer = power_of_ten(answer)
        elif operation == 'log':
            answer = log_button(answer)
        elif operation == 'ln':
            answer = natural_log(answer)
        elif operation == 'sin^-1':
            answer = arc_sin(answer)
        elif operation == 'cos^-1':
            answer = arc_cos(answer)
        elif operation == 'tan^-1':
            answer = arc_tan(answer)
        elif operation == 'x^y':
            answer = x_to_the_y(answer, entry)
            entry = 0
    return answer, entry

def create_calc(scientific):
    if scientific:

        win = GraphWin("Calc", 223, 327)

        displayScreen = Rectangle(Point(10,10), Point(218,55))
        displayScreen.setFill('yellow')
        displayScreen.draw(win)

        del buttons[:]

        buttons.append(create_button (win, 4, 57.5, 36.5, 93.5, "7"))
        buttons.append(create_button (win, 4, 96, 36.5, 132, "4"))
        buttons.append(create_button (win, 4, 134.5, 36.5, 170.5, "1"))
        buttons.append(create_button (win, 4, 173, 36.5, 209, "+/-", 'purple'))
        buttons.append(create_button (win, 4, 211.5, 36.5, 247.5, "x2", 'purple'))
        buttons.append(create_button (win, 4, 250, 36.5, 286, "", 'purple'))
        buttons.append(create_button (win, 4, 288.5, 36.5, 324.5, "MR", 'purple'))
        buttons.append(create_button (win, 40.5, 57.5, 73, 93.5, "8"))
        buttons.append(create_button (win, 40.5, 96, 73, 132, "5"))
        buttons.append(create_button (win, 40.5, 134.5, 73, 170.5, "2"))
        buttons.append(create_button (win, 40.5, 173, 73, 209, "0"))
        buttons.append(create_button (win, 40.5, 211.5, 73, 247.5, "root", 'purple'))
        buttons.append(create_button (win, 40.5, 250, 73, 286, "M-", 'purple'))
        buttons.append(create_button (win, 40.5, 288.5, 73, 324.5, "MS", 'purple'))
        buttons.append(create_button (win, 77, 57.5, 109.5, 93.5, "9"))
        buttons.append(create_button (win, 77, 96, 109.5, 132, "6"))
        buttons.append(create_button (win, 77, 134.5, 109.5, 170.5, "3"))
        buttons.append(create_button (win, 77, 173, 109.5, 209, "."))
        buttons.append(create_button (win, 77, 211.5, 109.5, 247.5, "1/x", 'purple'))
        buttons.append(create_button (win, 77, 250, 109.5, 286, "C", 'purple'))
        buttons.append(create_button (win, 77, 288.5, 109.5, 324.5, "M+", 'purple'))
        buttons.append(create_button (win, 113.5, 57.5, 146, 93.5, "*", 'purple'))
        buttons.append(create_button (win, 113.5, 96, 146, 132, "/", 'purple'))
        buttons.append(create_button (win, 113.5, 134.5, 146, 170.5, "-", 'purple'))
        buttons.append(create_button (win, 113.5, 173, 146, 209, "+", 'purple'))
        buttons.append(create_button (win, 113.5, 211.5, 146, 247.5, "%", 'purple'))
        buttons.append(create_button (win, 113.5, 250, 146, 286, "=", 'purple'))
        buttons.append(create_button (win, 113.5, 288.5, 146, 324.5, "", 'purple'))
        buttons.append(create_button (win, 150, 57.5, 182.5, 93.5, "sin", 'purple'))
        buttons.append(create_button (win, 150, 96, 182.5, 132, "cos", 'purple'))
        buttons.append(create_button (win, 150, 134.5, 182.5, 170.5, "tan", 'purple'))
        buttons.append(create_button (win, 150, 173, 182.5, 209, "10^x", 'purple'))
        buttons.append(create_button (win, 150, 211.5, 182.5, 247.5, "log", 'purple'))
        buttons.append(create_button (win, 150, 250, 182.5, 286, "ln", 'purple'))
        buttons.append(create_button (win, 150, 288.5, 182.5, 324.5, "MC", 'purple'))
        buttons.append(create_button (win, 186.5, 57.5, 219, 93.5, "sin^-1", 'purple'))
        buttons.append(create_button (win, 186.5, 96, 219, 132, "cos^-1", 'purple'))
        buttons.append(create_button (win, 186.5, 134.5, 219, 170.5, "tan^-1", 'purple'))
        buttons.append(create_button (win, 186.5, 173, 219, 209, "x^y", 'purple'))
        buttons.append(create_button (win, 186.5, 288.5, 219, 324.5, "Sci", 'purple'))
  
    else:
        win = GraphWin("Calc", 150, 327)

        displayScreen = Rectangle (Point(5,5), Point(145,55))
        displayScreen.setFill('white')
        displayScreen.draw(win)

        del buttons[:]

        buttons.append(create_button (win, 4, 57.5, 36.5, 93.5, "7"))
        buttons.append(create_button (win, 4, 96, 36.5, 132, "4"))
        buttons.append(create_button (win, 4, 134.5, 36.5, 170.5, "1"))
        buttons.append(create_button (win, 4, 173, 36.5, 209, "+/-", 'purple'))
        buttons.append(create_button (win, 4, 211.5, 36.5, 247.5, "x2", 'purple'))
        buttons.append(create_button (win, 4, 250, 36.5, 286, "MC", 'purple'))
        buttons.append(create_button (win, 4, 288.5, 36.5, 324.5, "MR", 'purple'))
        buttons.append(create_button (win, 40.5, 57.5, 73, 93.5, "8"))
        buttons.append(create_button (win, 40.5, 96, 73, 132, "5"))
        buttons.append(create_button (win, 40.5, 134.5, 73, 170.5, "2"))
        buttons.append(create_button (win, 40.5, 173, 73, 209, "0"))
        buttons.append(create_button (win, 40.5, 211.5, 73, 247.5, "root", 'purple'))
        buttons.append(create_button (win, 40.5, 250, 73, 286, "M-", 'purple'))
        buttons.append(create_button (win, 40.5, 288.5, 73, 324.5, "MS", 'purple'))
        buttons.append(create_button (win, 77, 57.5, 109.5, 93.5, "9"))
        buttons.append(create_button (win, 77, 96, 109.5, 132, "6"))
        buttons.append(create_button (win, 77, 134.5, 109.5, 170.5, "3"))
        buttons.append(create_button (win, 77, 173, 109.5, 209, "."))
        buttons.append(create_button (win, 77, 211.5, 109.5, 247.5, "1/x", 'purple'))
        buttons.append(create_button (win, 77, 250, 109.5, 286, "C", 'purple'))
        buttons.append(create_button (win, 77, 288.5, 109.5, 324.5, "M+", 'purple'))
        buttons.append(create_button (win, 113.5, 57.5, 146, 93.5, "*", 'purple'))
        buttons.append(create_button (win, 113.5, 96, 146, 132, "/", 'purple'))
        buttons.append(create_button (win, 113.5, 134.5, 146, 170.5, "-", 'purple'))
        buttons.append(create_button (win, 113.5, 173, 146, 209, "+", 'purple'))
        buttons.append(create_button (win, 113.5, 211.5, 146, 247.5, "%", 'purple'))
        buttons.append(create_button (win, 113.5, 250, 146, 286, "=", 'purple'))
        buttons.append(create_button (win, 113.5, 288.5, 146, 324.5, "", 'purple'))
        buttons.append(create_button (win, 113.5, 288.5, 146, 324.5, "Sci", 'purple'))
        buttons.append(create_button (win, 150, 57.5, 182.5, 93.5, "(", 'purple'))
        buttons.append(create_button (win, 150, 96, 182.5, 132, ")", 'purple'))


    displayString1 = ''
    displayString2 = ''
    displayTextElement1 = Text(Point(150, 25), "")
    displayTextElement1.draw(win)
    displayTextElement2 = Text(Point(125, 37.5), "")
    displayTextElement2.draw(win)

    return win, displayString1, displayString2, displayTextElement1, displayTextElement2

def main():
    scientific = False
    win, displayString1, displayString2, displayTextElement1, displayTextElement2 = create_calc (scientific)
    answer = None
    entry = 0
    operation = None
    clearNextNumber = False
    memory = 0
    entryString = ''

    while 1 == 1:
        clicked = win.getMouse()
        x = clicked.getX()
        y = clicked.getY()

        for b in buttons:
            button, label = b
            key = check(button, label, x, y)
            if key:
                if key == '=':
                    clearNextNumber = False
                    if answer == None:
                        answer = entry
                        displayString1 = entryString
                        displayString2 = str(answer)
                        entry = 0
                        entryString = ''
                    else:
                        answer, entry = calculation(answer, entry, operation)
                        operation = None
                        displayString1 = displayString1
                        displayString2 = '%20.3f' % (answer) 

                elif key in ['+', '-', '/', '*', '%']:
                    answer, entry = calculation(answer, entry, operation)
                    entryString = ''
                    operation = key
                    displayString1 = displayString1 + key
                    displayString2 = displayString1
                    clearNextNumber = False
                    
                elif key == '+/-':
                    answer, entry = calculation(answer, entry, operation)
                    entryString = ''
                    operation = key
                    displayString1 = ''
                    displayString2 = str(answer)
                    clearNextNumber = True

                elif key == 'x2':
                    answer, entry = calculation(answer, entry, operation)
                    operation = key
                    displayString1 = str(answer) + str('^2')
                    displayString2 = displayString1
                    clearNextNumber = True

                elif key  == '√':
                    answer, entry = calculation(answer, entry, operation)
                    entryString = ''
                    operation = key
                    displayString1 = key + entry
                    displayString2 = str(answer)
                    clearNextNumber = True

                elif key == '1/x':
                    x = entry
                    answer, entry = calculation(answer, entry, operation)
                    entryString = ''
                    operation = key
                    displayString1 = ''
                    displayString2 = str(answer)
                    clearNextNumber = True

                elif key == 'C':
                    displayString1 = ''
                    displayString2 = displayString1
                    answer = None
                    entry = 0
                    entryString = ''
                    operation = None

                elif key == 'M+':
                    memory = add(float(memory), entry or answer)
                    displayString1 = ''
                    displayString2 = str(memory)

                elif key == 'MR':
                    displayString1 = ''
                    displayString2 = str(memory)
                    
                elif key == 'M-':
                    memory = subtract(float(memory), entry or answer)
                    displayString1 = ''
                    displayString2 = str(memory)

                elif key == 'MC':
                    memory = 0

                elif key == 'MS':
                    temp = memory
                    memory = entry
                    entry = temp
                    displayString1 = ''
                    displayString2 = str(memory)
                    
                elif key == '10^x':
                    answer, entry = calculation(answer, entry, operation)
                    operation = key
                    displayString1 = '10^' + str(answer)
                    displayString2 = displayString1
                    clearNextNumber = True
                    
                elif key in ['sin', 'cos', 'tan', 'log', 'ln', 'sin^-1', 'cos^-1', 'tan^-1']:
                    answer, entry = calculation(answer, entry, operation)
                    operation = key

                    if answer == None:
                        answer = entry
                        displayString1 = key + '(' + entryString + ')'
                        displayString2 = str(answer)
                        entry = 0
                        entryString = ''
                    else:
                        answer, entry = calculation(answer, entry, operation)
                        operation = None
                        displayString1 = key + '(' + entryString + ')'
                        displayString2 = '%20.3f' % (answer)

                    clearNextNumber = True


                elif key == 'x^y':
                    answer, entry = calculation(answer, entry, operation)
                    entryString = ''
                    operation = key
                    displayString1 = displayString1 + '^'
                    displayString2 = str(answer)
                    clearNextNumber = False

                elif key == 'Sci':
                    win.close()
                    scientific = not scientific
                    win, displayString1, displayString2, displayTextElement1, displayTextElement2 = create_calc (scientific)
                    displayString1 = ''
                    displayString2 = ''
                    clearNextNumber = False
                    answer = None
                    entry = 0
                    entryString = ''
                    operation = None

                elif key == '(':
                    entryString = ''
                    displayString1 = displayString1 + '(' + entryString
                    displayString2 = displayString1
                    clearNextNumber = False

                elif key == ')':
                    displayString1 = displayString1 + ')'
                    displayString2 = displayString1
                    clearNextNumer = False

                    
                else:
                    if clearNextNumber:
                        displayString1 = ''
                        displayString2 = ''
                        clearNextNumber = False
                        answer = None
                        entry = 0
                        entryString = ''
                        operation = None
                    entryString = entryString + key
                    if entryString[0] == '.':
                        entry = eval("0" + entryString)
                    else:
                        entry = eval(entryString) 
                    displayString1 = displayString1 + key
                    displayString2 = displayString1

                displayTextElement1.undraw()
                displayTextElement1 = Text(Point(100, 25), displayString1)
                displayTextElement1.setFace('arial')
                displayTextElement1.setSize(10)
                displayTextElement1.draw(win)
                displayTextElement2.undraw()
                displayTextElement2 = Text(Point(100, 37.5), displayString2)
                displayTextElement2.setFace('arial')
                displayTextElement2.setSize(10)
                displayTextElement2.draw(win)

main()
