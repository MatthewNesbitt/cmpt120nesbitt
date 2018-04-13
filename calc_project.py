from graphics import *
from calc_functions import *

# JA: You can consolidate some of your code
# I coudn't fine the parenthesis in the calculator GUI

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


    displayString = ''
    displayTextElement = Text(Point(150, 25), "")
    displayTextElement.draw(win)

    return win, displayString, displayTextElement

def main():
    scientific = False
    win, displayString, displayTextElement = create_calc (scientific)

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
                    clearNextNumber = True
                    if answer == None:
                        answer = entry
                        displayString = str(answer)
                        entry = 0
                        entryString = ''
                    else:
                        answer, entry = calculation(answer, entry, operation)
                        operation = None
                        displayString = displayString + '\n' + '%20.3f' % (answer) 

                elif key in ['+', '-', '/', '*', '%']:
                    answer, entry = calculation(answer, entry, operation)
                    entryString = ''
                    operation = key
                    displayString = displayString + key
                    clearNextNumber = False
                    
                elif key == '+/-':
                    answer, entry = calculation(answer, entry, operation)                        
                    entryString = ''
                    operation = key
                    displayString = str(answer)
                    clearNextNumber = True

                elif key == 'x2':
                    answer, entry = calculation(answer, entry, operation)
                    operation = key
                    displayString = str(answer) + str('^2')
                    clearNextNumber = True

                elif key  == 'root':
                    answer, entry = calculation(answer, entry, operation)
                    entryString = ''
                    operation = key
                    displayString = key + str(answer)
                    clearNextNumber = True

                elif key == '1/x':
                    x = entry
                    answer, entry = calculation(answer, entry, operation)
                    entryString = ''
                    operation = key
                    displayString = str(answer)
                    clearNextNumber = True

                elif key == 'C':
                    displayString = ''
                    answer = None
                    entry = 0
                    entryString = ''
                    operation = None

                elif key == 'M+':
                    memory = addition(float(memory), entry or answer)
                    displayString = float(memory)

                elif key == 'MR':
                    displayString = float(memory)
                    
                elif key == 'M-':
                    memory = subtraction(float(memory), entry or answer)
                    displayString = float(memory)

                elif key == 'MC':
                    memory = 0

                elif key == 'MS':
                    temp = memory
                    memory = entry
                    entry = temp
                    displayString = float(memory)

                elif key == '10^x':
                    answer, entry = calculation(answer, entry, operation)
                    operation = key
                    displayString = '10^' + str(answer)
                    clearNextNumber = True
                    
                elif key in ['sin', 'cos', 'tan']:
                    answer, entry = calculation(answer, entry, operation)
                    operation = key
                    displayString = key + '(' + str(answer) + ')'
                    clearNextNumber = True

                elif key == 'log':
                    answer, entry = calculation(answer, entry, operation)
                    operation = key
                    displayString = key + '(' + str(answer) + ')'
                    clearNextNumber = True
                    
                elif key == 'ln':
                    answer, entry = calculation(answer, entry, operation)
                    operation = key
                    displayString = key + '(' + str(answer) + ')'
                    clearNextNumber = True
                    
                elif key == 'sin^-1':
                    answer, entry = calculation(answer, entry, operation)
                    operation = key
                    displayString = key + '(' + str(answer) + ')'
                    clearNextNumber = True
                                    
                elif key == 'cos^-1':
                    answer, entry = calculation(answer, entry, operation)
                    operation = key
                    displayString = key + '(' + str(answer) + ')'
                    clearNextNumber = True
                                    
                elif key == 'tan^-1':
                    answer, entry = calculation(answer, entry, operation)
                    operation = key
                    displayString = key + '(' + str(answer) + ')'
                    clearNextNumber = True

                elif key == 'x^y':
                    answer, entry = calculation(answer, entry, operation)
                    entryString = ''
                    operation = key
                    displayString = displayString + '^'
                    clearNextNumber = False

                elif key == 'Sci':
                    win.close()
                    scientific = not scientific
                    win, displayString, displayTextElement = create_calc (scientific)
                    displayString = ''
                    clearNextNumber = False
                    answer = None
                    entry = 0
                    entryString = ''
                    operation = None

                elif key == '(':
                    entryString = ''
                    displayString = displayString + '(' + entryString
                    clearNextNumber = False

                elif key == ')':
                    displayString = displayString + ')'
                    clearNextNumer = False    

                else:
                    if clearNextNumber:
                        displayString = ''
                        clearNextNumber = False
                        answer = None
                        entry = 0
                        entryString = ''
                        operation = None
                    entryString = entryString + key
                    entry = eval(entryString) 
                    displayString = displayString + key

                displayTextElement.undraw()
                displayTextElement = Text(Point(100, 25), displayString)
                displayTextElement.setFace('arial')
                displayTextElement.setSize(10)
                displayTextElement.draw(win)

main()
