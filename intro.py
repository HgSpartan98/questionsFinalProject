# Final Project
# Aeowyn Kendall and Daniel Kim

# We need to build a program which will give the user a choice between
# two quizzes then call questions from a txt file, ask for user input, and
# check the input for certain keywords, and output different text if the
# keywords match

# This code provides intro text

def outputText(instance):

        # Text explaining the general idea
    if instance == 'intro':
        message = ("The following examination is designed to test the " +
                   "memory of a previously incapacitated individual. \n " +
                   "If you answer a question incorrectly, you will not " +
                   "be able to go back, but must proceed to the next \n" +
                   "question. Click anywhere to continue. \n To enter " +
                   "your answer, press enter." )
        
        # Text asking them to click the button corresponding to the test
        # they wish to take
    elif instance == 'choose':
        message = ("Choose the version of the examination you wish to take. " +
                   "The Star Trek version is based on a scene \n from " +
                   "Star Trek: The Voyage Home. In the movie, Spock takes " +
                   "the exam, \n so it was geared toward a wide scope " +
                   "of cultural, tactial, and scientific knowledge. \n " +
                   "The Real Life version was designed by yours truly, " +
                   "the programmers. \n It is in the same spirit as the " +
                   "original exam, but intended to be answerable by the " +
                   "\n average person with some college education. ")


        # Text shown at the beginning of the Star Trek version of the test
    elif instance == 'spock':
        message = ("The following examination is designed to test the " +
                   "memory of a previously incapacitated individual. " +
                   "If you answer a question incorrectly, you will not " +
                   "be able to go back, but must proceed to the next " +
                   "question. Click anywhere to continue.  \n To enter " +
                   "your answer, press enter." )

        # Text shown at the beginning of the Real Life version of the test
    elif instance == 'real':
        message = ("")

    else:
        message = ""

    return message
