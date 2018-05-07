# Final Project
# Aeowyn Kendall and Daniel Kim

# We need to build a program which will give the user a choice between two quizzes
# then call questions from a txt file, ask for user input, and check the input
# for certain keywords, and output different text if the keywords match.

from graphics import *
import ctypes

def GUI():
    user32 = ctypes.windll.user32
    screensizeX = user32.GetSystemMetrics(0)
    screensizeY = user32.GetSystemMetrics(1)
    win = GraphWin("Memory Test", screensizeX, screensizeY)
    color1 = "red"
    color2 = "blue"

    setBackground(color2)
    
    intro = Text(Point((screensizeX / 2), screensizeY / 10), intro())
    intro.setSize(10)
    intro.draw(win)

#    buttonLeft = Rectangle(Point(
    
    click = getMouse()
