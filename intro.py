# Final Project
# Aeowyn Kendall and Daniel Kim

# We need to build a program which will give the user a choice between
# two quizzes then call questions from a txt file, ask for user input, and
# check the input for certain keywords, and output different text if the
# keywords match

# This code provides intro text

def outputText(instance):

    if instance == 'intro':
        message = ("The following examination is designed to test the memory of " +
                   "a previously incapacitated individual. \n If you answer a " +
                   "question incorrectly, you will not be able to go back, " +
                   "but must proceed to the next question.")
        
    elif instance == 'trek':
        message = ("")

    elif instance == 'spock':
        message = ("The following examination is designed to test the memory of " +
                   "a previously incapacitated individual. If you answer a " +
                   "question incorrectly, you will not be able to go back, " +
                   "but must proceed to the next question.")

    elif instance == 'real':
        message = ("")
        

    return message
