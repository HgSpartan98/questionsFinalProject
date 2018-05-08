# Final Project
# Aeowyn Kendall and Daniel Kim

# We need to build a program which will give the user a choice between two quizzes
# then call questions from a txt file, ask for user input, and check the input
# for certain keywords, and output different text if the keywords match.

from graphics import *
import ctypes
import textwrap
from intro import outputText

# GetTextDimensions copied from StackOverflow
# https://stackoverflow.com/questions/35771863/how-
# to-calculate-length-of-string-in-pixels-for-specific-font-and-size
def GetTextDimensions(text, points, font):
    class SIZE(ctypes.Structure):
        _fields_ = [("cx", ctypes.c_long), ("cy", ctypes.c_long)]

    hdc = ctypes.windll.user32.GetDC(0)
    hfont = ctypes.windll.gdi32.CreateFontA(points, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, font)
    hfont_old = ctypes.windll.gdi32.SelectObject(hdc, hfont)

    size = SIZE(0, 0)
    ctypes.windll.gdi32.GetTextExtentPoint32A(hdc, text, len(text), ctypes.byref(size))

    ctypes.windll.gdi32.SelectObject(hdc, hfont_old)
    ctypes.windll.gdi32.DeleteObject(hfont)

    return (size.cx, size.cy)

def GUI():

    # Build window
    user32 = ctypes.windll.user32
    screenSizeX = user32.GetSystemMetrics(0)
    screenSizeY = user32.GetSystemMetrics(1)
    winSizeX = (screenSizeX - (screenSizeX / 10))
    winSizeY = (screenSizeY - (screenSizeY / 10))

    print(winSizeX)
    
    win = GraphWin("Memory Test", 500, 500)
    color1 = "red"
    color2 = "blue"

    GetTextDimensions(outputText("intro") ,12, "Times New Roman")
    wrapWidth = (winSizeX - (winSizeX / 100))

    #Intro text
    introWrapped = textwrap.wrap(outputText("intro"), wrapWidth)
    for i in introWrapped:
        print(i)
          
    
    introText = Text(Point((winSizeX / 2), winSizeY / 10), introWrapped)
    introText.setSize(10)
    introText.draw(win)



#    buttonLeft = Rectangle(Point(
    
#    click = getMouse()


GUI()
