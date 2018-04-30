from graphics import *

class Display:

    """The display is the overall display rectangle and it includes
    one or more text elements (lines)."""

    def __init__(self, win, center, width, height, color = 'lightcyan'):
        # initialize screen and draw it
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.screen = Rectangle(p1,p2)
        self.screen.setFill(color)
        self.screen.draw(win)
        self.win = win

        # initialize text elements (empty to start)
        self.textElems = []
        self.corners = []

    def addLine(self, corner, text=''):
        # create text element, draw it, and store in list
        displayTextElement = Text(corner, text)
        displayTextElement.setFace('arial')
        displayTextElement.setSize(20)
        displayTextElement.draw(self.win)
        self.textElems.append(displayTextElement)
        self.corners.append(corner)

    def setLine(self, line, text):
        # set new text on specific display line (0, 1, 2...)
        # undraw old one first
        self.textElems[line].undraw()

        # then create new one and save it
        displayTextElement = Text(self.corners[line], text)
        displayTextElement.setFace('arial')
        displayTextElement.setSize(20)
        displayTextElement.draw(self.win)
        self.textElems[line] = displayTextElement
