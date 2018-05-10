# Final Project
# Aeowyn Kendall and Daniel Kim

# We need to build a program which will give the user a choice between two quizzes
# then call questions from a txt file, ask for user input, and check the input
# for certain keywords, and output different text if the keywords match.

from graphics import *
import textwrap
from intro import outputText
from compileDictionary import compileToDictionary
from test import analyseAnswer


def GUI():

    # Define Window (win)
    colorBack = (color_rgb(5, 30, 100))
    colorButton = "goldenrod"
    colorText = "white"
    

    win = GraphWin("Memory Test", 1000, 750)
    win.setCoords(-200, -200, 200, 200)
    win.setBackground(colorBack)


    # Define Left Button (buttonLeft) and corresponding text (textLeft)
    buttonLeft = Rectangle(Point(-150, -100), Point(-50, -50))
    buttonLeft.setFill(colorBack)
    buttonLeft.setOutline(colorBack)
    buttonLeft.draw(win)

    textLeft = Text(Point(-100, -75), "")
    textLeft.setSize(12)
    textLeft.draw(win)
    textLeft.setTextColor(colorText)
    textLeft.setFace("arial")

    # Define Right Button (buttonRight)
    buttonRight = Rectangle(Point(150, -100), Point(50, -50))
    buttonRight.setFill(colorBack)
    buttonRight.setFill(colorBack)
    buttonRight.setOutline(colorBack)
    buttonRight.draw(win)

    textRight = Text(Point(100, -75), "")
    textRight.setSize(12)
    textRight.draw(win)
    textRight.setTextColor(colorText)
    textRight.setFace("arial")


    # Intro Text
    message = Text(Point(0, 50), outputText("intro"))
    message.setSize(12)
    message.draw(win)
    message.setTextColor(colorText)
    message.setFace("arial")
    
    click = win.getMouse()

    # Choose Test and Compile Dictionary
    message.setText(outputText("choose"))

    buttonLeft.setFill(colorButton)
    buttonRight.setFill(colorButton)

    textRight.setText("Real Life")
    textLeft.setText("Star Trek")

    while True:
        click = win.getMouse()
        clickX = click.getY()
        clickY = click.getX()

        if -150 <= clickX <= -50 and -100 <= clickY <= -50:
            dictionaryQ = compileToDictionary("starTrekQ.txt")
            dictionaryA = compileToDictionary("starTrekA.txt")
            message.setText(outputText("spock"))
            break
        
        elif -150 <= clickX <= -50 and -100 <= clickY <= -50:
            dictionaryQ = compileToDictionary("realLifeQ.txt")
            dictionaryA = compileToDictionary("realLifeA.txt")
            message.setText(outputText("real"))
            break

    buttonLeft.setFill(colorBack)
    buttonRight.setFill(colorBack)
    textRight.setText("")
    textLeft.setText("")

    
    
    




    


GUI()
