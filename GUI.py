# Final Project
# Aeowyn Kendall and Daniel Kim

# We need to build a program which will give the user a choice between two quizzes
# then call questions from a txt file, ask for user input, and check the input
# for certain keywords, and output different text if the keywords match.

from graphics import *
from intro import outputText
from compileDictionary import compileToDictionary
from analyzeAnswer import analyzeAnswer


def GUI():

    # Define Window (win)
    colorBack = color_rgb(15, 55, 80)
    colorButton = color_rgb(220,118,0)
    colorText = "white"
    font = "arial"
    fontSize = 12

    win = GraphWin("Memory Test", 1000, 750)
    win.setCoords(-200, -200, 200, 200)
    win.setBackground(colorBack)

    # Define Cover (cover)
    cover = Rectangle(Point(-200, -200), Point(200, 200))
    cover.setFill(colorBack)
    cover.setFill(colorBack)
    cover.setOutline(colorBack)


    # Define Left Button (buttonLeft) and corresponding text (textLeft)
    buttonLeft = Rectangle(Point(-150, -100), Point(-50, -50))
    buttonLeft.setFill(colorBack)
    buttonLeft.setOutline(colorBack)
    buttonLeft.draw(win)

    textLeft = Text(Point(-100, -75), "")
    textLeft.setSize(fontSize)
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
    textRight.setFace(font)

    # Define Input Box (inputBox)
    inputBox = Entry(Point(0, -50), 40)
    inputBox.setTextColor(colorText)
    inputBox.setFace(font)
    inputBox.setSize(fontSize)
    inputBox.setFill(colorButton)


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
        clickY = click.getY()
        clickX = click.getX()

        if -150 <= clickX <= -50 and -100 <= clickY <= -50:
            dictionaryQ = compileToDictionary("starTrekQ.txt")
            dictionaryA = compileToDictionary("starTrekA.txt")
            message.setText(outputText("spock"))
            break
        
        elif 50 <= clickX <= 150 and -100 <= clickY <= -50:
            dictionaryQ = compileToDictionary("realLifeQ.txt")
            dictionaryA = compileToDictionary("realLifeA.txt")
            message.setText(outputText("real"))
            break

    buttonLeft.setFill(colorBack)
    buttonRight.setFill(colorBack)
    textRight.setText("")
    textLeft.setText("")
    count = 0
    while True:
        try:
            cover.undraw()
            count += 1
            question = dictionaryQ[count]  
            message.setText(question)
            inputBox.draw(win)
            
            while True:
                key = win.getKey()
                if key == "Return":
                    break
            answerGiven = inputBox.getText()
            inputBox.setText("")

            correct = analyzeAnswer(dictionaryA, answerGiven, count)
            
            cover.draw(win)
            inputBox.undraw()
            truth = Text(Point(0, 0), "")
            truth.setSize(20)
            truth.draw(win)
            truth.setTextColor(colorText)
            truth.setFace("arial")

            if correct == True:
                print("Correct")
                truth.setText("CORRECT")
            elif correct == False:
                print("Incorrect")
                truth.setText("INCORRECT")
                
            message.setText("")
            win.getKey()
            
            
        except KeyError:
            break

    win.close()
    




    

try:
    GUI()
except KeyError:
    win.close()
