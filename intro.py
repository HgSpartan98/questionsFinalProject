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
        message = ("The following examination is designed to test the memory of " +
                   "a previously incapacitated individual. \n If you answer a " +
                   "question incorrectly, you will not be able to go back, " +
                   "but must proceed to the next question.")
        
        # Text asking them to click the button corresponding to the test they wish to take
    elif instance == 'choose':
        message = ("Choose. ")


        # Text shown at the beginning of the Star Trek version of the test
    elif instance == 'spock':
        message = ("The following examination is designed to test the memory of " +
                   "a previously incapacitated individual. If you answer a " +
                   "question incorrectly, you will not be able to go back, " +
                   "but must proceed to the next question.")

        # Text shown at the beginning of the Real Life version of the test
    elif instance == 'real':
        message = ("")

    else:
        message = ""

    return message
