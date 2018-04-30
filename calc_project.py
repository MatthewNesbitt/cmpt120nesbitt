from calc_functions import *
from graphics import *
from button import *
from display import *


class Calculator:
    def __init__(self):
        self.buttons = []


    def do_calculation(self, answer, entry, operation):
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
            elif operation == '√':
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

    def create_window(self, scientific_mode):
        if scientific_mode:
                
            win = GraphWin("Calculator", 446, 654)
            display = Display(win, Point(223, 60), 426, 100)


            del self.buttons[:]
            self.buttons.append(Button(win, Point(40.5, 151), 65, 72, "7"))
            self.buttons.append(Button(win, Point(40.5, 228), 65, 72, "4"))
            self.buttons.append(Button(win, Point(40.5, 305), 65, 72, "1"))
            self.buttons.append(Button(win, Point(40.5, 382), 65, 72, "+/-", 'purple'))
            self.buttons.append(Button(win, Point(40.5, 459), 65, 72, "x2", 'purple'))
            self.buttons.append(Button(win, Point(40.5, 536), 65, 72, "(", 'purple'))
            self.buttons.append(Button(win, Point(40.5, 613), 65, 72, "M+", 'grey'))
            self.buttons.append(Button(win, Point(113.5, 151), 65, 72, "8"))
            self.buttons.append(Button(win, Point(113.5, 228), 65, 72, "5"))
            self.buttons.append(Button(win, Point(113.5, 305), 65, 72, "2"))
            self.buttons.append(Button(win, Point(113.5, 382), 65, 72, "0"))
            self.buttons.append(Button(win, Point(113.5, 459), 65, 72, "√", 'purple'))
            self.buttons.append(Button(win, Point(113.5, 536), 65, 72, ")", 'purple'))
            self.buttons.append(Button(win, Point(113.5, 613), 65, 72, "MR", 'grey'))
            self.buttons.append(Button(win, Point(186.5, 151), 65, 72, "9"))
            self.buttons.append(Button(win, Point(186.5, 228), 65, 72, "6"))
            self.buttons.append(Button(win, Point(186.5, 305), 65, 72, "3"))
            self.buttons.append(Button(win, Point(186.5, 382), 65, 72, "."))
            self.buttons.append(Button(win, Point(186.5, 459), 65, 72, "1/x", 'purple'))
            self.buttons.append(Button(win, Point(186.5, 536), 65, 72, "C", 'purple'))
            self.buttons.append(Button(win, Point(186.5, 613), 65, 72, "MS", 'grey'))
            self.buttons.append(Button(win, Point(259.5, 151), 65, 72, "/", 'purple'))
            self.buttons.append(Button(win, Point(259.5, 228), 65, 72, "*", 'purple'))
            self.buttons.append(Button(win, Point(259.5, 305), 65, 72, "+", 'purple'))
            self.buttons.append(Button(win, Point(259.5, 382), 65, 72, "-", 'purple'))
            self.buttons.append(Button(win, Point(259.5, 459), 65, 72, "%", 'purple'))
            self.buttons.append(Button(win, Point(259.5, 536), 65, 72, "=", 'purple'))
            self.buttons.append(Button(win, Point(259.5, 613), 65, 72, "M-", 'grey'))       
            self.buttons.append(Button(win, Point(332.5, 151), 65, 72, "sin", 'purple'))
            self.buttons.append(Button(win, Point(332.5, 228), 65, 72, "cos", 'purple'))
            self.buttons.append(Button(win, Point(332.5, 305), 65, 72, "tan", 'purple'))
            self.buttons.append(Button(win, Point(332.5, 382), 65, 72, "10^x", 'purple'))
            self.buttons.append(Button(win, Point(332.5, 459), 65, 72, "log", 'purple'))
            self.buttons.append(Button(win, Point(332.5, 536), 65, 72, "ln", 'purple'))
            self.buttons.append(Button(win, Point(332.5, 613), 65, 72, "MC", 'grey'))
            self.buttons.append(Button(win, Point(405.5, 305), 65, 72, "sin^-1", 'purple'))
            self.buttons.append(Button(win, Point(405.5, 382), 65, 72, "cos^-1", 'purple'))
            self.buttons.append(Button(win, Point(405.5, 459), 65, 72, "tan^-1", 'purple'))
            self.buttons.append(Button(win, Point(405.5, 536), 65, 72, "x^y", 'purple'))
            self.buttons.append(Button(win, Point(405.5, 613), 65, 72, "Sci", 'grey'))


        else:
            win = GraphWin("Calculator", 373, 654)

            display = Display(win, Point(183, 60), 353, 100)

            del self.buttons[:]
        
            self.buttons.append(Button(win, Point(40.5, 151), 65, 72, "7"))
            self.buttons.append(Button(win, Point(40.5, 228), 65, 72, "4"))
            self.buttons.append(Button(win, Point(40.5, 305), 65, 72, "1"))
            self.buttons.append(Button(win, Point(40.5, 382), 65, 72, "+/-", 'purple'))
            self.buttons.append(Button(win, Point(40.5, 459), 65, 72, "x2", 'purple'))
            self.buttons.append(Button(win, Point(40.5, 536), 65, 72, "MS", 'purple'))
            self.buttons.append(Button(win, Point(40.5, 613), 65, 72, "M+", 'grey'))
            self.buttons.append(Button(win, Point(113.5, 151), 65, 72, "8"))
            self.buttons.append(Button(win, Point(113.5, 228), 65, 72, "5"))
            self.buttons.append(Button(win, Point(113.5, 305), 65, 72, "2"))
            self.buttons.append(Button(win, Point(113.5, 382), 65, 72, "0"))
            self.buttons.append(Button(win, Point(113.5, 459), 65, 72, "√", 'purple'))
            self.buttons.append(Button(win, Point(113.5, 536), 65, 72, "M-", 'purple'))
            self.buttons.append(Button(win, Point(113.5, 613), 65, 72, "MR", 'grey'))
            self.buttons.append(Button(win, Point(186.5, 151), 65, 72, "9"))
            self.buttons.append(Button(win, Point(186.5, 228), 65, 72, "6"))
            self.buttons.append(Button(win, Point(186.5, 305), 65, 72, "3"))
            self.buttons.append(Button(win, Point(186.5, 382), 65, 72, "."))
            self.buttons.append(Button(win, Point(186.5, 459), 65, 72, "1/x", 'purple'))
            self.buttons.append(Button(win, Point(186.5, 536), 65, 72, "C", 'purple'))
            self.buttons.append(Button(win, Point(186.5, 613), 65, 72, "MC", 'grey'))
            self.buttons.append(Button(win, Point(259.5, 151), 65, 72, "*", 'purple'))
            self.buttons.append(Button(win, Point(259.5, 228), 65, 72, "/", 'purple'))
            self.buttons.append(Button(win, Point(259.5, 305), 65, 72, "-", 'purple'))
            self.buttons.append(Button(win, Point(259.5, 382), 65, 72, "+", 'purple'))
            self.buttons.append(Button(win, Point(259.5, 459), 65, 72, "%", 'purple'))
            self.buttons.append(Button(win, Point(259.5, 536), 65, 72, "=", 'purple'))
            self.buttons.append(Button(win, Point(259.5, 613), 65, 72, "Sci", 'grey'))       
            self.buttons.append(Button(win, Point(332.5, 151), 65, 72, "(", 'purple'))
            self.buttons.append(Button(win, Point(332.5, 228), 65, 72, ")", 'purple'))

        display.addLine(Point(275, 50))
        display.addLine(Point(275, 75))
        display.setLine(0, '')
        display.setLine(1, '')

        return win, display

    def run(self):
        scientific_mode = False
        win, display = self.create_window (scientific_mode)
        answer = None
        entry = 0
        operation = None
        clearNextNumber = False
        memory = 0
        entryString = ''
        displayString1 = ''
        displayString2 = ''
        
        while 1 == 1:
            clicked = win.getMouse()
            x = clicked.getX()
            y = clicked.getY()

            for b in self.buttons:
                if b.clicked(Point(x,y)):
                    key = b.getLabel()
                    if key == '=':
                        clearNextNumber = False
                        if answer == None:
                            answer = entry
                            displayString1 = ''
                            displayString2 = str(answer)
                            entry = 0
                            entryString = ''
                        else:
                            answer, entry = self.do_calculation(answer, entry, operation)
                            operation = None
                            displayString1 = ''
                            displayString2 = '%20.3f' % (answer) 

                    elif key in ['+', '-', '/', '*', '%']:
                        answer, entry = self.do_calculation(answer, entry, operation)
                        entryString = ''
                        operation = key
                        displayString1 = displayString1 + key
                        displayString2 = str(answer)
                        clearNextNumber = False
                        
                    elif key == '+/-':
                        answer, entry = self.do_calculation(answer, entry, operation)
                        operation = key
                        displayString1 = ''
                        displayString2 = str(answer)
                        clearNextNumber = True

                    elif key == 'x2':
                        answer, entry = self.do_calculation(answer, entry, operation)
                        operation = key
                        displayString1 = str(answer) + str('^2')
                        displayString2 = ''
                        clearNextNumber = True

                    elif key  == '√':
                        answer, entry = self.do_calculation(answer, entry, operation)
                        entryString = ''
                        operation = key
                        displayString1 = key + str(answer)
                        displayString2 = str(answer)
                        clearNextNumber = True

                    elif key == '1/x':
                        x = entry
                        answer, entry = self.do_calculation(answer, entry, operation)
                        entryString = ''
                        operation = key
                        displayString1 = '1/' + str(answer)
                        displayString2 = str(answer)
                        clearNextNumber = True

                    elif key == 'C':
                        displayString1 = ''
                        displayString2 = ''
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
                        answer, entry = self.do_calculation(answer, entry, operation)
                        operation = key
                        displayString1 = '10^' + str(answer)
                        displayString2 = ''
                        clearNextNumber = True
                        
                    elif key in ['sin', 'cos', 'tan', 'log', 'ln', 'sin^-1', 'cos^-1', 'tan^-1']:
                        answer, entry = self.do_calculation(answer, entry, operation)
                        operation = key

                        if answer == None:
                            answer = entry
                            displayString1 = key + '(' + entryString + ')'
                            displayString2 = str(answer)
                            entry = 0
                            entryString = ''
                        else:
                            answer, entry = self.do_calculation(answer, entry, operation)
                            operation = None
                            displayString1 = key + '(' + entryString + ')'
                            displayString2 = '%20.3f' % (answer)

                        clearNextNumber = True


                    elif key == 'x^y':
                        answer, entry = self.do_calculation(answer, entry, operation)
                        entryString = ''
                        operation = key
                        displayString1 = displayString1 + '^'
                        displayString2 = str(answer)
                        clearNextNumber = False

                    elif key == 'Sci':
                        win.close()
                        scientific_mode = not scientific_mode
                        win, display = self.create_window (scientific_mode)
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
                        if answer:
                            displayString2 = str(answer)
                        else:
                            displayString2 = ''
                        clearNextNumber = False

                    elif key == ')':
                        displayString1 = displayString1 + ')'
                        if answer:
                            displayString2 = str(answer)
                        else:
                            displayString2 = ''
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
                        displayString2 = key

                    display.setLine(0, displayString1)
                    display.setLine(1, displayString2)
