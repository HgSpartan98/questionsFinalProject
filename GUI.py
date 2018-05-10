# Final Project
# Aeowyn Kendall and Daniel Kim

# We need to build a program which will give the user a choice between two quizzes
# then call questions from a txt file, ask for user input, and check the input
# for certain keywords, and output different text if the keywords match.

from graphics import *
import textwrap
from intro import outputText

def GUI():

    backColor = (color_rgb(5, 30, 100))

    win = GraphWin("Memory Test", 1000, 750)
    win.setCoords(-200, -200, 200, 200)
    rec = Rectangle(Point(-200, -200), Point(200, 200))
    rec.setFill(color_rgb(5, 30, 100))
    rec.draw(win)
    color1 = "red"
    color2 = "blue"
 
    introText = Text(Point(100, 50), outputText("intro"))
    introText.setSize(12)
    introText.draw(win)


#    buttonLeft = Rectangle(Point(

    
#    click = getMouse()


GUI()
