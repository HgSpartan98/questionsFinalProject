# Final Project
# Aeowyn Kendall and Daniel Kim

# We need to build a program which will give the user a choice between two quizzes
# then call questions from a txt file, ask for user input, and check the input
# for certain keywords, and output different text if the keywords match.

from graphics import *
import ctypes

def GUI():
    user32 = ctypes.windll.user32
    screenSizeX = user32.GetSystemMetrics(0)
    screenSizeY = user32.GetSystemMetrics(1)
    winSizeX = (screenSizeX - (screenSizeX / 10))
    winSizeY = (screenSizeY - (screenSizeY / 10))
    
    win = GraphWin("Memory Test", winSizeX, winSizeY)
    color1 = "red"
    color2 = "blue"

    
    introText = Text(Point((winSizeX / 2), winSizeY / 10), intro())
    introText.setSize(10)
    introText.draw(win)



#    buttonLeft = Rectangle(Point(
    
    click = getMouse()
